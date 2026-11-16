#!/usr/bin/env python3
"""Docker-only, standard-library audit of the pinned public demonstration archive."""
import argparse
import base64
from collections import Counter, defaultdict
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import platform
import re
import struct
import sys
import tarfile
import urllib.request

REV = "46d0cf698cacacc02edcf5301a7f30547e9b8cdb"
URL = f"https://huggingface.co/StellarEdge/StellaVLA/resolve/{REV}/libero/demo/demo_pack.tar"
SHA = "699e71722960be7d2450d7c2fb6eed8b05bfd53e5fb08e4b9eba029ebd113bff"
SIZE = 12840960
TARGETS = [
    ("d1", "put the bowl on the plate"),
    ("d2", "put the bowl on top of the cabinet"),
    ("d3", "put the wine bottle on the rack"),
]

def norm(value):
    return " ".join(str(value).lower().strip().split())

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def image_header(raw):
    if raw.startswith(b"\x89PNG\r\n\x1a\n") and len(raw) >= 24:
        w, h = struct.unpack(">II", raw[16:24])
        return {"format": "PNG", "width": w, "height": h, "validation": "HEADER_ONLY_NOT_PIXEL_DECODE"}
    if raw[:2] == b"\xff\xd8":
        pos = 2
        while pos + 4 <= len(raw):
            if raw[pos] != 255:
                pos += 1
                continue
            while pos < len(raw) and raw[pos] == 255:
                pos += 1
            if pos >= len(raw):
                break
            marker = raw[pos]
            pos += 1
            if marker in (0xd8, 0xd9) or 0xd0 <= marker <= 0xd7:
                continue
            if marker == 0xda:
                break
            length = int.from_bytes(raw[pos:pos+2], "big")
            if length < 2 or pos + length > len(raw):
                break
            if marker in {0xc0,0xc1,0xc2,0xc3,0xc5,0xc6,0xc7,0xc9,0xca,0xcb,0xcd,0xce,0xcf}:
                h, w = struct.unpack(">HH", raw[pos+3:pos+7])
                return {"format": "JPEG", "width": w, "height": h, "validation": "HEADER_ONLY_NOT_PIXEL_DECODE"}
            pos += length
    return {"format": "UNKNOWN", "validation": "NOT_DECODED"}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", default="/scratch/demo_pack.tar")
    parser.add_argument("--preview", action="store_true", help="Emit selected first/last images as JSON base64; never write them to the repository.")
    args = parser.parse_args()
    if not Path("/.dockerenv").exists():
        raise RuntimeError("Run through resume_assets.sh in local Docker; no host payload download.")
    archive = Path(args.archive)
    archive.parent.mkdir(parents=True, exist_ok=True)
    if not archive.exists():
        req = urllib.request.Request(URL, headers={"User-Agent": "PaperReview-GAP-RETRIEVAL-A1"})
        with urllib.request.urlopen(req, timeout=45) as response:
            raw = response.read(SIZE + 1)
        if len(raw) != SIZE or digest(raw) != SHA:
            raise RuntimeError("Archive size/checksum mismatch; payload not accepted.")
        archive.write_bytes(raw)
    raw = archive.read_bytes()
    if len(raw) != SIZE or digest(raw) != SHA:
        raise RuntimeError("Cached archive size/checksum mismatch.")
    tf = tarfile.open(fileobj=io.BytesIO(raw), mode="r:*")
    members = {}
    for member in tf.getmembers():
        name = PurePosixPath(member.name)
        if name.is_absolute() or ".." in name.parts or member.issym() or member.islnk():
            raise RuntimeError("Unsafe tar member; no extraction performed.")
        if member.isfile():
            key = str(name)
            if key in members:
                raise RuntimeError("Duplicate tar path.")
            members[key] = member
    manifests = [n for n in members if PurePosixPath(n).name == "manifest.json"]
    if len(manifests) != 1:
        raise RuntimeError(f"Expected one manifest, found {manifests}")
    manifest_path = manifests[0]
    manifest_raw = tf.extractfile(members[manifest_path]).read()
    manifest = json.loads(manifest_raw)
    base = PurePosixPath(manifest_path).parent
    pools = manifest.get("pools", {})
    payloads = manifest.get("payloads", {})
    mapping = manifest.get("lang_to_task", {})
    issues = []
    frame_hash_groups = defaultdict(list)
    payload_hash_groups = defaultdict(list)
    frame_info = {}
    payload_info = {}
    def read_frame(frame):
        rel = PurePosixPath(frame)
        if rel.is_absolute() or ".." in rel.parts:
            raise ValueError("unsafe frame path")
        name = str(base / rel)
        if name not in members:
            raise ValueError(f"missing frame: {name}")
        data = tf.extractfile(members[name]).read()
        if name not in frame_info:
            frame_info[name] = {"path": name, "sha256": digest(data), "bytes": len(data), **image_header(data)}
            frame_hash_groups[digest(data)].append(name)
        return frame_info[name], data

    for key, payload in payloads.items():
        if not isinstance(payload, dict):
            issues.append({"payload":key,"problem":"not an object"})
            continue
        frames = []
        for frame in payload.get("frames", []):
            try:
                info, _ = read_frame(frame)
                frames.append(info)
            except (ValueError, TypeError) as error:
                issues.append({"payload":key,"problem":str(error)})
        canonical = json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",",":")).encode()
        payload_hash_groups[digest(canonical)].append(key)
        payload_info[key] = {
            "keys": sorted(payload),
            "canonical_json_sha256": digest(canonical),
            "demo_instruction": payload.get("demo_instruction"),
            "declared_identity": {k: payload.get(k) for k in ["suite", "task_idx", "ep_idx"]},
            "frames": frames,
            "frame_count": len(payload.get("frames", [])),
            "frame_state_count": len(payload.get("demo_frame_states", [])),
            "structured_text": {
                field: {"type": type(payload.get(field)).__name__,
                        "characters": len(str(payload.get(field, ""))),
                        "sha256": digest(str(payload.get(field, "")).encode())}
                for field in ["demo_task_plan", "demo_initial_state", "demo_final_state", "demo_subtask_summary"]
            },
            "plan_steps": re.findall(r"^\d+\. (.+)$", payload.get("demo_task_plan", ""), re.MULTILINE),
            "provenance_or_success_fields": {k:v for k,v in payload.items() if any(w in k.lower() for w in ["success","source","split","episode","trajectory"])},
        }
        if not frames or len(frames) != len(payload.get("demo_frame_states", [])):
            issues.append({"payload": key, "problem": "empty frames or frame/state count mismatch"})
    pool_rows = []
    for pool_key, ids in pools.items():
        suite = pool_key.split("|t", 1)[0]
        missing = [str(e) for e in ids if f"{suite}#{e}" not in payloads]
        pool_rows.append({"pool":pool_key, "count":len(ids), "ordered_episode_ids":ids, "missing_payload_ids":missing})
        if missing:
            issues.append({"pool":pool_key,"problem":"missing payload references","ids":missing})
        for episode in ids:
            payload = payloads.get(f"{suite}#{episode}", {})
            if str(payload.get("ep_idx")) != str(episode) or payload.get("suite") != suite or str(payload.get("task_idx")) != pool_key.split("|t", 1)[1]:
                issues.append({"pool":pool_key,"episode":episode,"problem":"declared identity mismatch"})
    for suite, entries in mapping.items():
        for language, task_index in entries.items():
            for episode in pools.get(f"{suite}|t{task_index}", []):
                if norm(payloads.get(f"{suite}#{episode}", {}).get("demo_instruction")) != norm(language):
                    issues.append({"suite":suite,"language":language,"problem":"public language/payload instruction mismatch"})
    selected = []
    for symbol, language in TARGETS:
        task_index = mapping.get("libero_goal", {}).get(norm(language))
        pool_key = f"libero_goal|t{task_index}" if task_index is not None else None
        ids = pools.get(pool_key, [])
        keys = sorted(f"libero_goal#{e}" for e in ids if f"libero_goal#{e}" in payload_info)
        row = {"symbol":symbol,"runtime_instruction":language,"demo_task_index":task_index,"pool_key":pool_key,"pool_size":len(ids),"payload_id":keys[0] if keys else None}
        if keys:
            row["payload"] = payload_info[keys[0]]
            row["exact_payload_instruction_match"] = norm(payload_info[keys[0]]["demo_instruction"]) == norm(language)
        else:
            row["qualification"] = "NO_EXACT_RUNTIME_MAPPING_OR_POOL"
            issues.append({"symbol":symbol,"problem":"required exact-language pool unavailable"})
        selected.append(row)
    if args.preview:
        previews=[]
        for row in selected:
            if not row["payload_id"]:
                continue
            payload=payloads[row["payload_id"]]
            frame_names=payload.get("frames",[])
            for idx in sorted({0,len(frame_names)-1}):
                if not frame_names:
                    continue
                info,data=read_frame(frame_names[idx])
                mime={"PNG":"image/png","JPEG":"image/jpeg"}.get(info["format"])
                if mime:
                    previews.append({"symbol":row["symbol"],"payload_id":row["payload_id"],"frame_index":idx,"instruction":payload.get("demo_instruction"),"data_url":f"data:{mime};base64,"+base64.b64encode(data).decode()})
        print(json.dumps({"previews":previews}))
        return
    frames_by_shape=Counter((f["format"],f.get("width"),f.get("height")) for f in frame_info.values())
    lexical = []
    for _, query in TARGETS[:2]:
        query_tokens = set(re.findall(r"[a-z0-9]+", query.lower()))
        scores = []
        for row in selected:
            if not row["payload_id"]:
                continue
            instruction = norm(row["payload"]["demo_instruction"])
            tokens = set(re.findall(r"[a-z0-9]+", instruction))
            scores.append({"instruction":instruction,"payload_id":row["payload_id"],"score":len(tokens & query_tokens)/len(tokens | query_tokens)})
        scores.sort(key=lambda r: (-r["score"], r["instruction"]))
        lexical.append({"query":query,"ranked_groups":scores,"S_candidates":[r["payload_id"] for r in scores[:2]],"scope":"METADATA_RULE_ONLY_NO_VISUAL_EMBEDDING_OR_POLICY"})
    report = {
        "task_id":"GAP-RETRIEVAL-A1","scope":"PUBLIC_ASSET_STRUCTURE_ONLY",
        "runtime":{"python":platform.python_version(),"platform":platform.platform(),"machine":platform.machine(),"docker_only":True,
                   "image_id":os.environ.get("RETRIEVAL_AUDIT_IMAGE_ID"),"audit_script_sha256":digest(Path(__file__).read_bytes())},
        "archive":{"url":URL,"revision":REV,"bytes":len(raw),"sha256":digest(raw),"checksum_verified":True,"container_path":str(archive),"extracted":False},
        "manifest":{"path":manifest_path,"sha256":digest(manifest_raw),"keys":sorted(manifest),"meta":manifest.get("meta")},
        "counts":{"archive_files":len(members),"pools":len(pools),"payloads":len(payloads),"referenced_unique_frames":len(frame_info)},
        "language_maps":mapping,
        "pools":pool_rows,
        "selected_candidates":selected,
        "lexical_prefilter":lexical,
        "payload_frame_count_distribution":dict(sorted(Counter(p["frame_count"] for p in payload_info.values()).items())),
        "frame_shapes":[{"format":k[0],"width":k[1],"height":k[2],"count":v} for k,v in sorted(frames_by_shape.items())],
        "duplicate_payload_json":[ids for ids in payload_hash_groups.values() if len(ids)>1],
        "duplicate_frame_bytes":[paths for paths in frame_hash_groups.values() if len(paths)>1],
        "issues":issues,
        "unverified":["image pixel decode/content except separately documented manual previews","native success and trajectory provenance","train/evaluation overlap and episode identity mapping","DINOv2/Stella weight load, token ceiling and inference","paired simulator initial states, alternate predicates and controller"],
        "policy_runs":0,"embeddings_computed":0,
    }
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if issues:
        sys.exit(2)

if __name__ == "__main__":
    main()
