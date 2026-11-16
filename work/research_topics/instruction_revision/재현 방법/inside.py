"""Docker-only artifact staging and one bounded native qualification.

This recipe is unbuilt/unexecuted until qualified on a compatible local GPU host.
"""
import base64
import hashlib
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(path)


def verify(path, item):
    import google_crc32c  # Pinned by the openpi lock; installed only in the image.

    crc, md5, sha = google_crc32c.Checksum(), hashlib.md5(), hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            crc.update(block)
            md5.update(block)
            sha.update(block)
            size += len(block)
    if size != item["size"] or base64.b64encode(crc.digest()).decode() != item["crc32c"]:
        raise ValueError(f"Size/CRC32C mismatch: {item['relative_path']}")
    if item.get("md5_base64") and base64.b64encode(md5.digest()).decode() != item["md5_base64"]:
        raise ValueError(f"MD5 mismatch: {item['relative_path']}")
    if item.get("expected_sha256") and sha.hexdigest() != item["expected_sha256"]:
        raise ValueError(f"SHA256 mismatch: {item['relative_path']}")
    return {"path": item["relative_path"], "generation": item["generation"],
            "size": size, "sha256": sha.hexdigest(), "crc32c_verified": True}


def artifacts(download):
    spec = json.loads(Path("/recipe/ARTIFACTS.json").read_text())
    checked = []
    for item in spec["files"]:
        relative = Path(item["relative_path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("Unsafe artifact path")
        target = Path("/data") / relative
        if not target.exists():
            if not download:
                raise FileNotFoundError(f"Run assets stage first: {relative}")
            target.parent.mkdir(parents=True, exist_ok=True)
            url = ("https://storage.googleapis.com/download/storage/v1/b/"
                   + item["bucket"] + "/o/" + urllib.parse.quote(item["object"], safe="")
                   + "?alt=media&generation=" + item["generation"])
            temporary = target.with_suffix(target.suffix + ".partial")
            print(f"Fetching pinned generation: {relative} ({item['size']} bytes)", flush=True)
            with urllib.request.urlopen(url, timeout=120) as response, temporary.open("wb") as stream:
                generation = response.headers.get("x-goog-generation")
                if generation and generation != item["generation"]:
                    raise ValueError("Returned generation differs from requested generation")
                while block := response.read(8 * 1024 * 1024):
                    stream.write(block)
            verify(temporary, item)
            temporary.replace(target)
        checked.append(verify(target, item))
    result = {"verified_at": datetime.now(timezone.utc).isoformat(), "files": checked}
    if download:
        write_json("/data/VERIFIED_ARTIFACTS.json", result)
    return result


def output(command, **kwargs):
    return subprocess.check_output(command, text=True, **kwargs).strip()


def smoke():
    run = Path("/runs") / (datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ") + f"-{os.getpid()}")
    run.mkdir(parents=True, exist_ok=False)
    plan = json.loads(Path("/recipe/RESUME_PLAN.json").read_text())
    report = {"status": "RUNNING", "qualification_only": True, "research_effect": "UNMEASURED",
              "run": str(run), "image_id": os.environ.get("REVISION_IMAGE_ID"),
              "started_at": datetime.now(timezone.utc).isoformat(), "plan": plan,
              "stage": "artifact_verification"}
    server = None
    try:
        report["artifacts"] = artifacts(download=False)
        report["recipe_sha256"] = {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in Path("/recipe").iterdir() if p.is_file()
        }
        report["resteer_revision"] = output(["git", "-C", "/opt/resteer", "rev-parse", "HEAD"])
        report["openpi_revision"] = output(["git", "-C", "/opt/resteer/third_party/openpi", "rev-parse", "HEAD"])
        if report["resteer_revision"] != plan["sources"]["resteer"]["revision"]:
            raise RuntimeError("ReSteer revision mismatch")
        if report["openpi_revision"] != plan["sources"]["openpi"]["revision"]:
            raise RuntimeError("openpi revision mismatch")
        report["stage"] = "gpu_visibility"
        report["gpu"] = output(["nvidia-smi", "--query-gpu=name,uuid,driver_version,memory.total", "--format=csv,noheader"])
        policy_python = "/opt/resteer/third_party/openpi/.venv/bin/python"
        report["installed_packages"] = {}
        for name, python in {"sim": "/opt/resteer/.venv/bin/python", "policy": policy_python}.items():
            report["installed_packages"][name] = json.loads(output([
                python, "-c", "import importlib.metadata as m,json,sys; "
                "print(json.dumps({'python':sys.version,'packages':"
                "{d.metadata['Name']:d.version for d in m.distributions()}}))"
            ]))
        report["system_packages"] = output(["dpkg-query", "-W", "-f=${Package}=${Version}\\n"])
        report["stage"] = "jax_cuda_backend"
        report["jax_devices"] = output([
            policy_python, "-c",
            "import jax; d=jax.devices(); assert d and all(x.platform=='gpu' for x in d); print(d)"
        ], timeout=120)
        # The child exits before the model server starts, releasing its CUDA context.
        deadline = time.monotonic() + plan["qualification"]["wall_time_seconds"]
        report["stage"] = "server_start"
        write_json(run / "runtime_manifest.json", report)
        with (run / "server.log").open("w") as log:
            server = subprocess.Popen([
                policy_python, "/opt/resteer/third_party/openpi/scripts/serve_policy.py",
                "--port", "8000", "policy:checkpoint", "--policy.config=pi05_libero",
                "--policy.dir=/data/checkpoints/pi05_libero"
            ], cwd="/opt/resteer", stdout=log, stderr=subprocess.STDOUT)
            while True:
                if server.poll() is not None:
                    raise RuntimeError(f"Policy server exited {server.returncode}; see server.log")
                if time.monotonic() >= deadline:
                    raise TimeoutError("Policy startup budget exceeded")
                try:
                    with socket.create_connection(("127.0.0.1", 8000), timeout=1):
                        break
                except OSError:
                    time.sleep(1)
            report["stage"] = "native_io_switch"
            write_json(run / "runtime_manifest.json", report)
            with (run / "probe.log").open("w") as probe_log:
                subprocess.run([
                    "/opt/resteer/.venv/bin/python", "/recipe/native_probe.py", str(run)
                ], check=True, timeout=max(1, deadline - time.monotonic()),
                   stdout=probe_log, stderr=subprocess.STDOUT, cwd="/opt/resteer")
            report["native"] = json.loads((run / "native_result.json").read_text())
            if report["native"]["status"] != "PASS_IO_ONLY":
                raise RuntimeError("Native IO qualification did not pass")
        report["status"] = "PASS_IO_ONLY"
    except Exception as error:
        report["status"] = "FAILED"
        report["error"] = f"{type(error).__name__}: {error}"
    finally:
        if server is not None and server.poll() is None:
            server.terminate()
            try:
                server.wait(timeout=15)
            except subprocess.TimeoutExpired:
                server.kill()
                server.wait()
        report["finished_at"] = datetime.now(timezone.utc).isoformat()
        write_json(run / "runtime_manifest.json", report)
        Path("/runs/LATEST").write_text(run.name + "\n")
    print(json.dumps({"status": report["status"], "run": str(run), "stage": report["stage"]}), flush=True)
    return 0 if report["status"] == "PASS_IO_ONLY" else 1


if __name__ == "__main__":
    if not Path("/.dockerenv").exists():
        raise SystemExit("Run this program inside the prepared local Docker image only.")
    mode = sys.argv[1] if len(sys.argv) > 1 else "help"
    if mode == "assets":
        result = artifacts(download=True)
        print(json.dumps({"status": "ASSETS_VERIFIED_ONLY", "files": len(result["files"])}))
    elif mode == "smoke":
        raise SystemExit(smoke())
    elif mode == "results":
        latest = Path("/runs/LATEST").read_text().strip()
        if Path(latest).name != latest:
            raise SystemExit("Invalid run name")
        print((Path("/runs") / latest / "runtime_manifest.json").read_text())
    else:
        raise SystemExit("Use assets, smoke or results through resume.sh")
