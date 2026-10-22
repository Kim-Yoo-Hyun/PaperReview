"""Run inside Docker. Inspect immutable public data; do not train or unpickle."""
import concurrent.futures
import hashlib
import io
import json
import os
from pathlib import Path
import pickletools
import platform
import re
import sys
import time
import urllib.request

import h5py
import numpy as np
from PIL import Image

REV = "bbb1e266ed585f1557773de5a3f1e3b4cd944f97"
BASE = f"https://huggingface.co/datasets/AutoLab-SJTU/robofollow-data/resolve/{REV}/"
ROOT = Path("/tmp/c2")
OUT = ROOT / "out"
OUT.mkdir(parents=True, exist_ok=True)
SAMPLE_IDS = [0, 24, 49]
MAX_FILE = 128 * 1024**2
MAX_TOTAL = 1024**3
TASKS = [
    ("r_pick2_via4_to6_short_front", "train"),
    ("r_pick2_via4_to6_long_front", "holdout"),
    ("r_pick2_via5_to6_short_front", "holdout"),
    ("r_pick2_via5_to6_long_front", "train"),
    ("r_pick3_via4_to6_short_front", "holdout"),
    ("r_pick3_via4_to6_long_front", "train"),
    ("r_pick3_via5_to6_short_front", "train"),
    ("r_pick3_via5_to6_long_front", "holdout"),
]


def digest(b):
    return hashlib.sha256(b).hexdigest()


def save(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def fetch(path):
    target = ROOT / "data" / path
    if not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(BASE + path, timeout=45) as response:
            size = int(response.headers.get("Content-Length", "0"))
            if size > MAX_FILE:
                raise ValueError(f"file cap: {path} {size}")
            data = response.read(MAX_FILE + 1)
            if len(data) > MAX_FILE:
                raise ValueError(f"file cap: {path}")
            target.write_bytes(data)
    data = target.read_bytes()
    return target, {"path": path, "url": BASE + path, "bytes": len(data), "sha256": digest(data)}


def prefix(task):
    return f"scene3/scene3_{task}/"


def inspect_hdf(path):
    result = {"datasets": {}, "attributes": {}, "image_decode_checks": {}}
    with h5py.File(path, "r") as file:
        result["attributes"] = {str(k): str(v) for k, v in file.attrs.items()}

        def visit(name, item):
            if not isinstance(item, h5py.Dataset):
                return
            row = {"shape": list(item.shape), "dtype": str(item.dtype)}
            if item.ndim and item.dtype.kind in "fiu" and item.size <= 200000:
                data = item[...]
                row.update(finite=bool(np.isfinite(data).all()), sha256=digest(data.tobytes()))
                if name == "joint_action/vector":
                    row["first_frame_sha256"] = digest(data[0].tobytes())
                    row["first_frame"] = data[0].tolist()
                    row["last_frame"] = data[-1].tolist()
            result["datasets"][name] = row
            if name.endswith("/rgb") and item.ndim:
                checks = []
                for i in sorted(set([0, int(item.shape[0]) // 2, int(item.shape[0]) - 1])):
                    try:
                        raw = item[i]
                        encoded = raw.tobytes() if hasattr(raw, "tobytes") else bytes(raw)
                        with Image.open(io.BytesIO(encoded)) as image:
                            image.load()
                            checks.append({"frame": i, "size": list(image.size), "mode": image.mode,
                                           "encoded_sha256": digest(encoded), "decoded_sha256": digest(image.tobytes())})
                    except Exception as exc:
                        checks.append({"frame": i, "error": f"{type(exc).__name__}: {exc}"})
                result["image_decode_checks"][name] = checks

        file.visititems(visit)
    result["time_lengths"] = sorted({x["shape"][0] for x in result["datasets"].values() if x["shape"]})
    return result


def inspect_pickle(path):
    # Opcode inspection only: never call pickle.load/loads or execute REDUCE/GLOBAL.
    strings, globals_, counts = set(), set(), {}
    for op, arg, pos in pickletools.genops(path.read_bytes()):
        counts[op.name] = counts.get(op.name, 0) + 1
        if op.name == "GLOBAL":
            globals_.add(str(arg))
        if op.name in {"UNICODE", "BINUNICODE", "SHORT_BINUNICODE", "BINUNICODE8"}:
            strings.add(str(arg))
    return {"inspection": "pickletools opcodes only; no deserialization",
            "strings": sorted(strings), "global_opcodes": sorted(globals_), "opcode_counts": counts}


def main():
    started = time.time()
    metadata = json.loads((ROOT / "dataset.txt").read_bytes())
    files = {x["rfilename"] for x in metadata["siblings"]}
    inventories, episodes, evidence = [], [], []
    for task, partition in TASKS:
        pre = prefix(task)
        selected = sorted(p for p in files if p.startswith(pre))
        data_ids = sorted(int(re.search(r"episode(\d+)\.hdf5$", p).group(1)) for p in selected if re.search(r"/data/episode\d+\.hdf5$", p))
        row = {"task_id": task, "partition": partition, "hdf5_episode_ids": data_ids, "metadata": {}}
        for name in ["seed.txt", "seeds.json", "scene_info.json", "collection.json", "complete.json"]:
            if pre + name not in files:
                continue
            p, ev = fetch(pre + name)
            evidence.append(ev)
            value = p.read_text() if name.endswith(".txt") else json.loads(p.read_bytes())
            row["metadata"][name] = value
        seed_text = row["metadata"].get("seed.txt", "")
        seeds = [int(s) for s in seed_text.split()]
        row["seed_count"] = len(seeds)
        row["seed_ids"] = seeds
        info = row["metadata"].get("scene_info.json", {})
        for i in data_ids:
            episodes.append({"task_id": task, "task_partition": partition, "episode_id": i,
                             "seed_from_ordered_seed_txt": seeds[i] if i < len(seeds) else None,
                             "seed_mapping_verified_against_payload": False,
                             "initial_physics_state_hash": None,
                             "hdf5_path": pre + f"data/episode{i}.hdf5",
                             "instruction_present": pre + f"instructions/episode{i}.json" in files,
                             "planner_trace_present": pre + f"_traj_data/episode{i}.pkl" in files,
                             "scene_info": info.get(f"episode_{i}"),
                             "payload_selected": partition == "train" and i in SAMPLE_IDS})
        # Keep all metadata in the report, but avoid 400 copies of scene_info here.
        row["metadata"].pop("scene_info.json", None)
        inventories.append(row)
    save("episode_manifest.json", {"dataset_revision": REV, "episodes": episodes,
         "scope": "Inventory plus declared metadata, not success labels or a frozen evaluation split"})
    save("task_metadata.json", inventories)
    print("Inventories complete", len(episodes), flush=True)

    instructions = []
    instruction_paths = [prefix(task) + f"instructions/episode{i}.json" for task, part in TASKS
                         if part == "train" for i in range(50)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for p, ev in pool.map(fetch, instruction_paths):
            evidence.append(ev)
            instructions.append({"path": ev["path"], "value": json.loads(p.read_bytes()), "sha256": ev["sha256"]})
    save("instruction_audit.json", {"training_files": len(instructions), "entries": instructions})
    print("Training instruction files read", len(instructions), flush=True)

    payloads = []
    for task, partition in TASKS:
        if partition != "train":
            continue
        for i in SAMPLE_IDS:
            row = {"task_id": task, "episode_id": i, "partition": partition}
            for kind, suffix in [("hdf5", f"data/episode{i}.hdf5"), ("planner", f"_traj_data/episode{i}.pkl")]:
                try:
                    p, ev = fetch(prefix(task) + suffix)
                    evidence.append(ev)
                    row[kind + "_file"] = ev
                    row[kind] = inspect_hdf(p) if kind == "hdf5" else inspect_pickle(p)
                except Exception as exc:
                    row[kind + "_error"] = f"{type(exc).__name__}: {exc}"
            payloads.append(row)
            save("payload_audit.json", {"sample_ids_fixed_before_inspection": SAMPLE_IDS, "episodes": payloads})
            total = sum(p.stat().st_size for p in (ROOT / "data").rglob("*") if p.is_file())
            print("Payload inspected", task, i, "cache bytes", total, flush=True)
            if total > MAX_TOTAL:
                raise RuntimeError("Total data budget exceeded")
    save("download_manifest.json", {"dataset_revision": REV, "files": evidence})
    save("audit_execution.json", {"python": sys.version, "platform": platform.platform(),
         "h5py": h5py.__version__, "numpy": np.__version__, "script_sha256": digest(Path(__file__).read_bytes()),
         "elapsed_seconds": time.time() - started, "episodes_inspected": len(payloads),
         "training_instruction_files": len(instructions), "simulation_executed": False,
         "model_inference_executed": False, "training_executed": False, "pickle_executed": False})
    print("Payload audit complete", len(payloads), flush=True)


if __name__ == "__main__":
    if not Path("/.dockerenv").exists():
        raise SystemExit("This data audit must run in Docker")
    main()
