"""Docker-only bounded audit of the public AutoEval export.

Uses JSON and pickle opcode inspection only: no pickle.load, upstream imports,
image decoding, model inference, or robot connections. Samples are a schema
probe, not a random sample for performance estimation.
"""
import concurrent.futures
import datetime
import hashlib
import json
import pickletools
import urllib.request
from collections import Counter

REPO = "zhouzypaul/auto_eval"
REVISION = "97fd71792d05e8a96a09c962843f5bdba3006ff5"
CAP = 16 * 1024 * 1024


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "C5-bounded-data-audit"})
    with urllib.request.urlopen(request, timeout=45) as response:
        payload = response.read(CAP + 1)
    if len(payload) > CAP:
        raise ValueError("Payload over 16MiB cap; not parsed")
    return payload


def inspect(path):
    url = f"https://huggingface.co/datasets/{REPO}/resolve/{REVISION}/{path}"
    result = {"path": path, "url": url}
    try:
        payload = fetch(url)
        result.update(bytes=len(payload), sha256=hashlib.sha256(payload).hexdigest())
        if path.endswith(".json"):
            obj = json.loads(payload)
            result["keys"] = sorted(obj)
            result["value_types"] = {k: type(v).__name__ for k, v in obj.items()}
            result["time"] = obj.get("time")
        elif path.endswith(".pkl"):
            strings = set()
            opcodes = Counter()
            last_op = None
            for op, arg, pos in pickletools.genops(payload):
                opcodes[op.name] += 1
                last_op = op.name
                if isinstance(arg, str) and len(arg) <= 160:
                    strings.add(arg)
            result.update(opcode_counts=dict(opcodes), complete_stop=(last_op == "STOP"),
                          string_atoms=sorted(strings),
                          interpretation="String atoms are schema cues, not decoded values or confirmed top-level fields.")
    except Exception as exc:
        result["error"] = str(exc)
    return result


def main():
    api_url = f"https://huggingface.co/api/datasets/{REPO}/revision/{REVISION}"
    inventory = json.loads(fetch(api_url))
    assert inventory["sha"] == REVISION
    paths = sorted(x["rfilename"] for x in inventory["siblings"])
    metadata = [p for p in paths if p.endswith("/metadata.json")]
    trajectories = [p for p in paths if p.endswith(".pkl")]
    per_run = Counter(p.split("/")[1] for p in trajectories)
    empty_runs = [p.split("/")[1] for p in metadata if not per_run[p.split("/")[1]]]
    # Equally spaced indices in lexicographic path order, not time order.
    n = min(24, len(metadata))
    selected_meta = [metadata[i * (len(metadata) - 1) // (n - 1)] for i in range(n)]
    selected_traj = []
    unavailable = []
    for index in [0, len(metadata) // 2, len(metadata) - 1]:
        candidate = metadata[index].replace("metadata.json", "traj_0.pkl")
        if candidate in paths:
            selected_traj.append(candidate)
        else:
            unavailable.append(candidate)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(inspect, selected_meta + selected_traj))
    result = {
        "audited_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "repository": REPO, "revision": REVISION, "api_url": api_url,
        "inventory_file_count": len(paths), "metadata_file_count": len(metadata),
        "trajectory_file_count": len(trajectories),
        "metadata_runs_without_trajectory_count": len(empty_runs),
        "trajectory_counts_per_metadata_run": dict(sorted(Counter(per_run[p.split("/")[1]] for p in metadata).items())),
        "requested_sample_paths_not_in_inventory": unavailable,
        "inventory_paths_sha256": hashlib.sha256("\n".join(paths).encode()).hexdigest(),
        "selection": "24 evenly spaced metadata paths and first trajectory in first/middle/last metadata folders; lexicographic order",
        "metadata_sample_count": len(selected_meta), "trajectory_sample_count": len(selected_traj),
        "payload_bytes": sum(r.get("bytes", 0) for r in records),
        "pickle_execution": False, "image_decoding": False, "performance_estimation": False,
        "records": records, "errors": [r for r in records if "error" in r],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return bool(result["errors"])


if __name__ == "__main__":
    raise SystemExit(main())
