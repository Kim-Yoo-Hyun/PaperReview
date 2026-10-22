"""Read-only public-source audit. Run inside Docker; never imports upstream code.

Source bytes stay in the container. Output contains hashes and inventories only.
An inventory hit is a discovery cue, not evidence of a usable longitudinal log.
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import urllib.request


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "C5-literature-audit"})
    with urllib.request.urlopen(request, timeout=40) as response:
        data = response.read(4 * 1024 * 1024 + 1)
    if len(data) > 4 * 1024 * 1024:
        raise ValueError("Payload exceeds bounded source-audit cap")
    return data


def get_json(url):
    return json.loads(fetch(url))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sources", help="JSON mapping repo to pinned commit and file list")
    args = parser.parse_args()
    specs = json.loads(pathlib.Path(args.sources).read_text()) if args.sources else {
        "zhouzypaul/auto_eval": {},
        "architsharma97/medal": {},
        "yangzhao-666/MoReFree": {},
    }
    result = {"audited_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "upstream_code_executed": False, "repositories": [], "errors": []}
    for repo, spec in specs.items():
        try:
            base = "https://api.github.com/repos/" + repo
            sha = spec.get("commit") or get_json(base + "/commits/HEAD")["sha"]
            tree = get_json(base + "/git/trees/" + sha + "?recursive=1")
            if tree.get("truncated"):
                raise ValueError("Truncated tree cannot support a complete inventory")
            paths = [x["path"] for x in tree["tree"] if x["type"] == "blob"]
            releases = get_json(base + "/releases?per_page=100")
            item = {"repository": repo, "commit": sha, "tree_truncated": False,
                    "blob_paths": paths, "release_count_first_page": len(releases),
                    "release_assets": [{"release": r["tag_name"], "name": a["name"],
                                        "url": a["browser_download_url"]}
                                       for r in releases for a in r.get("assets", [])],
                    "files": []}
            for path in spec.get("files", ["README.md"]):
                url = "https://raw.githubusercontent.com/" + repo + "/" + sha + "/" + path
                payload = fetch(url)
                dest = pathlib.Path("/tmp/c5_sources") / repo / path
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(payload)
                item["files"].append({"path": path, "url": url,
                                      "bytes": len(payload), "lines": len(payload.splitlines()),
                                      "sha256": hashlib.sha256(payload).hexdigest()})
            result["repositories"].append(item)
        except Exception as exc:
            result["errors"].append({"repository": repo, "error": str(exc)})
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return bool(result["errors"])


if __name__ == "__main__":
    raise SystemExit(main())
