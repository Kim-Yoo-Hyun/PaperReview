"""Bounded, read-only public metadata audit. Run inside Docker; never train models.

Downloads only small metadata payloads into container memory. Does not fetch videos,
weights, PDFs, or execute upstream code. Prints a JSON evidence report to stdout.
"""
import collections
import hashlib
import io
import json
import platform
import urllib.parse
import urllib.request

import pyarrow.parquet as pq

MAX_BYTES = 64 * 1024 * 1024


def get(url):
    request = urllib.request.Request(url, headers={"User-Agent": "C4-Literature-Audit/1.0"})
    with urllib.request.urlopen(request, timeout=45) as response:
        data = response.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError("metadata size cap exceeded")
    return data


def js(url):
    return json.loads(get(url))


def summarize_rows(rows):
    keys = sorted({key for row in rows for key in row})
    out = {"rows": len(rows), "columns": keys, "non_null_counts": {}, "values": {}}
    for key in keys:
        values = [row.get(key) for row in rows]
        out["non_null_counts"][key] = sum(value is not None for value in values)
        # Full scalar value counts only when compact; otherwise retain cardinality/examples.
        if all(isinstance(v, (str, int, float, bool, type(None))) for v in values):
            counts = collections.Counter(str(v) for v in values)
            out["values"][key] = {"unique": len(counts), "counts": dict(counts) if len(counts) <= 55 else None,
                                  "first_values": list(counts)[:3]}
    out["first_rows"] = rows[:2]
    if "episode_index" in keys and "quality_label" in keys:
        episodes = {}
        for row in rows:
            episodes.setdefault(row["episode_index"], row)
        out["episode_summary"] = {
            "episodes": len(episodes),
            "quality_counts": dict(collections.Counter(r["quality_label"] for r in episodes.values())),
            "source_counts": dict(collections.Counter(r["data_source"] for r in episodes.values())),
            "all_episodes_start_timestamp_zero": all(r["timestamp"] == 0 for r in episodes.values()),
            "id_examples_by_source": {s: [r["id"] for r in episodes.values() if r["data_source"] == s][:3]
                                      for s in sorted({r["data_source"] for r in episodes.values()})},
        }
    if "file_name" in keys:
        out["source_prefix_counts"] = dict(collections.Counter(r["file_name"].split("/")[0] for r in rows)) if any("/" in r["file_name"] for r in rows) else None
    return out


def audit_dataset(repo):
    api = "https://huggingface.co/api/datasets/" + repo
    metadata = js(api)
    revision = metadata["sha"]
    files = [x["rfilename"] for x in metadata.get("siblings", [])]
    selected = [p for p in files if (p.endswith(".parquet") or p.endswith(".jsonl") or
                                     p in ("meta/info.json", "export_summary.json", "robometer_categorical_maps.json"))]
    out = {"repository": repo, "revision": revision, "repository_file_count": len(files),
           "selected_metadata_paths": selected, "payloads": [], "errors": []}
    if len(selected) > 50:
        out["errors"].append("metadata path cap: only first 50 inspected")
    for path in selected[:50]:
        url = "https://huggingface.co/datasets/" + repo + "/resolve/" + revision + "/" + path
        try:
            data = get(url)
            item = {"path": path, "url": url, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
            if path.endswith(".parquet"):
                table = pq.read_table(io.BytesIO(data))
                item["schema"] = str(table.schema)
                item.update(summarize_rows(table.to_pylist()))
            elif path.endswith(".jsonl"):
                rows = [json.loads(line) for line in data.decode().splitlines() if line.strip()]
                item.update(summarize_rows(rows))
            else:
                item["content"] = json.loads(data)
            out["payloads"].append(item)
        except Exception as error:
            out["errors"].append({"path": path, "error": str(error)})
    return out


report = {"date": "2026-10-21", "scope": "actual metadata payloads, no video decoding/model inference/policy training",
          "runtime": {"python": platform.python_version(), "machine": platform.machine(), "system": platform.system()},
          "datasets": []}
for name in ["robometer/rbm-1m-ood", "teetone/RoboReward"]:
    try:
        report["datasets"].append(audit_dataset(name))
    except Exception as error:
        report["datasets"].append({"repository": name, "error": str(error)})
print(json.dumps(report, ensure_ascii=False, indent=2))
