#!/usr/bin/env python3
"""Host stdlib only: inspect local Docker and orchestrate container-only P0."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import uuid

HERE = Path(__file__).resolve().parent
PLAN = json.loads((HERE / "PLAN.json").read_text())


def call(argv, timeout=30):
    try:
        p = subprocess.run(argv, capture_output=True, text=True, timeout=timeout)
        return {"command": argv, "returncode": p.returncode,
                "stdout": p.stdout[-16000:], "stderr": p.stderr[-6000:]}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"command": argv, "returncode": -1, "error": str(exc)}


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def check(output):
    record = {"utc": dt.datetime.now(dt.timezone.utc).isoformat(),
              "host": {"system": platform.system(), "machine": platform.machine()},
              "steps": [], "status": "CHECKING", "native_executed": False}

    def finish(status, code):
        record["status"] = status
        save(output / "local_check.json", record)
        return code, record

    if not shutil.which("docker"):
        return finish("BLOCKED_DOCKER_CLI", 3)
    # Do not silently switch from an environment override to another daemon.
    if os.environ.get("DOCKER_HOST"):
        return finish("BLOCKED_DOCKER_HOST_OVERRIDE_USE_EXPLICIT_LOCAL_CONTEXT", 3)
    context = call(["docker", "context", "show"])
    record["steps"].append(context)
    if context["returncode"]:
        return finish("BLOCKED_CONTEXT", 3)
    name = context["stdout"].strip()
    inspect = call(["docker", "context", "inspect", name])
    record["steps"].append(inspect)
    try:
        endpoint = json.loads(inspect["stdout"])[0]["Endpoints"]["docker"]["Host"]
    except (KeyError, IndexError, ValueError):
        return finish("BLOCKED_CONTEXT_METADATA", 3)
    record.update(context=name, endpoint=endpoint)
    if not endpoint.startswith("unix://"):
        return finish("BLOCKED_NONLOCAL_ENDPOINT", 3)
    info = call(["docker", "--context", name, "info", "--format", "{{json .}}"])
    record["steps"].append(info)
    if info["returncode"]:
        return finish("BLOCKED_DAEMON", 3)
    data = json.loads(info["stdout"])
    record["daemon"] = {k: data.get(k) for k in ("OSType", "Architecture", "MemTotal", "NCPU", "ServerVersion")}
    if platform.system() != "Linux" or platform.machine() not in ("x86_64", "AMD64"):
        return finish("BLOCKED_HOST_PLATFORM", 3)
    if data.get("OSType") != "linux" or data.get("Architecture") not in ("x86_64", "amd64"):
        return finish("BLOCKED_DAEMON_PLATFORM", 3)
    if data.get("MemTotal", 0) < PLAN["hardware"]["minimum_docker_ram_gib"] * 2**30:
        return finish("BLOCKED_DOCKER_RAM", 3)
    # This read-only check does not claim GPU allocation or EGL success.
    record["gpu_allocation"] = "NOT_CHECKED; run performs a container probe before payload fetch"
    return finish("LOCAL_METADATA_READY", 0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["check", "run"])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = (args.output or HERE / "runs" / (dt.datetime.now().strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:6])).resolve()
    if output.exists() and any(output.iterdir()):
        raise SystemExit("Choose a new empty output directory; existing evidence is preserved.")
    output.mkdir(parents=True, exist_ok=True)
    code, local = check(output)
    print(local["status"], str(output), flush=True)
    if code or args.mode == "check":
        return code
    docker = ["docker", "--context", local["context"]]
    stamp = uuid.uuid4().hex[:10]
    active = set()
    stages = []
    summary = {"status": "RUNNING", "stages": stages, "scope": "P0 qualification only; no training or VLA control",
               "image": PLAN["image"], "cache_volume": PLAN["cache_volume"]}

    def stream(argv, label):
        print(label, flush=True)
        # No long buffered wait: show output as the container/build progresses.
        with (output / (label + ".log")).open("w") as log:
            proc = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            try:
                for line in proc.stdout:
                    log.write(line)
                    log.flush()
                    print(line, end="", flush=True)
                rc = proc.wait()
            finally:
                if proc.poll() is None:
                    proc.terminate()
                    proc.wait(timeout=30)
        stages.append({"stage": label, "returncode": rc})
        save(output / "launcher_result.json", summary)
        if rc:
            raise RuntimeError(label + " failed: " + str(rc))

    def container(image, command, label, network=False, cache=False, gpu=True):
        name = "pose-active-" + stamp + "-" + label
        active.add(name)
        argv = docker + ["run", "--rm", "--name", name, "--label", PLAN["label"],
                         "--platform", PLAN["platform"], "--network", "bridge" if network else "none",
                         "--shm-size", "2g", "-e", "NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics",
                         "--mount", "type=bind,src=" + str(output) + ",dst=/out"]
        if gpu:
            argv += ["--gpus", "all"]
        if cache:
            argv += ["--mount", "type=volume,src=" + PLAN["cache_volume"] + ",dst=/cache"]
        stream(argv + [image] + command, label)
        active.discard(name)

    try:
        gpu_code = (
            "import torch,json; assert torch.cuda.is_available(); "
            "p=torch.cuda.get_device_properties(0); "
            "print(json.dumps(dict(name=p.name,memory=p.total_memory,major=p.major,cuda=torch.version.cuda))); "
            "assert p.major>=8 and p.total_memory>=" + str(PLAN["hardware"]["minimum_gpu_vram_gib"] * 2**30) + "; "
            "assert torch.cuda.is_bf16_supported()"
        )
        container(PLAN["base_image"], ["python", "-c", gpu_code], "gpu")
        stream(docker + ["build", "--platform", PLAN["platform"], "--label", PLAN["label"],
                         "-t", PLAN["image"], str(HERE)], "build")
        container(PLAN["image"], ["python", "checks.py"], "checks", gpu=False)
        container(PLAN["image"], ["python", "probe.py", "environment", "--output", "/out"], "environment", cache=True)
        container(PLAN["image"], ["python", "probe.py", "fetch", "--output", "/out"], "fetch", network=True, cache=True)
        container(PLAN["image"], ["python", "probe.py", "run", "--output", "/out"], "native", cache=True)
        summary["status"] = "P0_QUALIFICATION_PASSED_NO_POLICY_EFFECT_CLAIM"
        save(output / "image_inspect.json", call(docker + ["image", "inspect", PLAN["image"]]))
        return 0
    except (RuntimeError, OSError, KeyboardInterrupt) as exc:
        summary.update(status="STOPPED", reason=str(exc))
        return 4
    finally:
        # Only our uniquely named containers; never prune user's images/volumes.
        cleanup = [call(docker + ["rm", "-f", name]) for name in sorted(active)]
        summary["cleanup"] = cleanup
        summary["retained_assets"] = "Named cache and built image intentionally reusable; no broad prune"
        save(output / "launcher_result.json", summary)


if __name__ == "__main__":
    sys.exit(main())
