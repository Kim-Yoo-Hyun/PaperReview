"""Read public upstream source into Docker memory; emit hashes and short cues only."""
import hashlib
import json
import re
import urllib.request
from datetime import datetime, timezone

PATTERN = re.compile(r"proprio|state|cuda|memory|checkpoint|grad.*hook|register_hook|octo|coming soon|timeline|inference.*GB|pi05_libero|pi0_libero", re.I)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "PaperReview-D1-evidence-audit"})
    with urllib.request.urlopen(req, timeout=25) as r:
        raw = r.read(2_000_001)
    if len(raw) > 2_000_000:
        raise ValueError("bounded source read exceeded 2 MB")
    return raw


def inspect(repo, wanted):
    base = "https://api.github.com/repos/" + repo
    meta = json.loads(fetch(base))
    commit = json.loads(fetch(base + "/commits/" + meta["default_branch"]))["sha"]
    tree = json.loads(fetch(base + "/git/trees/" + commit + "?recursive=1"))
    paths = [x["path"] for x in tree["tree"] if x["type"] == "blob"]
    picked = [p for p in paths if p in wanted]
    if repo == "GeWu-Lab/GAP":
        picked += [p for p in paths if p.endswith(".py") and p not in picked][:6]
    files = []
    for path in picked:
        url = f"https://raw.githubusercontent.com/{repo}/{commit}/{path}"
        raw = fetch(url)
        lines = raw.decode("utf-8").splitlines()
        cues = [{"line": i, "text": line[:220]} for i, line in enumerate(lines, 1) if PATTERN.search(line)][:32]
        files.append({"path": path, "url": url, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "cues": cues})
    return {"repository": repo, "commit": commit, "tree_truncated": tree.get("truncated"),
            "blob_count": len(paths), "paths": paths if repo == "GeWu-Lab/GAP" else [],
            "files": files, "execution": "read_only_source_audit; dependencies/models not installed or run"}


def main():
    targets = {
        "GeWu-Lab/GAP": ["README.md", "environment.yml", "costdirection.py", "gap/policies/policy.py", "gap/policies/visual_encoder.py", "gap/cfgs/config.yaml", "gap/cfgs/task/assembly.yaml"],
        "Physical-Intelligence/openpi": ["README.md", "pyproject.toml", "examples/libero/README.md", "examples/libero/main.py", "src/openpi/policies/libero_policy.py", "src/openpi/training/config.py"],
    }
    results = []
    for repo, wanted in targets.items():
        try:
            results.append(inspect(repo, wanted))
        except Exception as e:
            results.append({"repository": repo, "error": str(e), "execution": "not_run"})
    print(json.dumps({"checked_at_utc": datetime.now(timezone.utc).isoformat(), "repositories": results}, indent=2))


if __name__ == "__main__":
    main()
