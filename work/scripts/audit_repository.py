#!/usr/bin/env python3
"""Read-only integrity audit for the PaperReview literature system."""

from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
import urllib.parse
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
NOTE_NAMES = ["01_overview.md", "02_problem.md", "03_method.md", "04_evaluation.md", "05_insights.md"]
STATUSES = {"UNREAD", "SKIMMED", "READ", "SYNTHESIZED", "REPRODUCED"}
EVIDENCE = {"CURATION_ONLY", "ABSTRACT_CHECKED", "FULL_TEXT_CHECKED", "EXPERIMENT_CHECKED"}


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().casefold()
    return re.sub(r"[^a-z0-9]+", "", value)


def main() -> None:
    errors: list[str] = []
    warnings: list[str] = []
    papers = json.loads(MANIFEST.read_text(encoding="utf-8"))
    registry = (ROOT / "PAPER.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\| (?:\d{4}|Unknown) \| [^|]+? \| \[([^\]]+)\]\(\.\/([^)]+/01_overview\.md)\)", registry, re.M)
    declared = re.search(r"Total papers with folders: (\d+)", registry)
    if not declared or int(declared.group(1)) != len(rows) or len(rows) != len(papers):
        errors.append(f"registry/manifest count mismatch: declared={declared.group(1) if declared else None}, rows={len(rows)}, manifest={len(papers)}")
    for key, values in {
        "normalized title": [norm(p["title"]) for p in papers],
        "folder": [p["folder"] for p in papers],
    }.items():
        duplicates = [value for value, count in Counter(values).items() if count > 1]
        if duplicates:
            errors.append(f"duplicate {key}: {len(duplicates)} groups")
    missing_notes = []
    for item in papers:
        folder = ROOT / item["folder"]
        for name in NOTE_NAMES:
            if not (folder / name).exists():
                missing_notes.append(str(folder / name))
    if missing_notes:
        errors.append(f"missing standard notes: {len(missing_notes)}")
    with (ROOT / "research" / "READING_TIERS.csv").open(newline="", encoding="utf-8") as handle:
        tiers = list(csv.DictReader(handle))
    with (ROOT / "research" / "READING_STATUS.csv").open(newline="", encoding="utf-8") as handle:
        status = list(csv.DictReader(handle))
    counts = Counter(row["tier"] for row in tiers)
    if len(tiers) != len(papers):
        errors.append(f"tier rows {len(tiers)} != papers {len(papers)}")
    if any(row["status"] not in STATUSES for row in status):
        errors.append("invalid reading status")
    if any(row.get("evidence_level") not in EVIDENCE for row in status):
        errors.append("invalid evidence level")
    if len(status) != counts["CORE"] + counts["NEXT"]:
        errors.append("intensive tracker size mismatch")
    queue_paths: list[str] = []
    for path in sorted((ROOT / "synthesis").glob("0*.md")):
        text = path.read_text(encoding="utf-8")
        block = text.split("<!-- READING_QUEUE:START -->", 1)[1].split("<!-- READING_QUEUE:END -->", 1)[0]
        queue_paths += re.findall(r"\]\((\.\./[^)]+/01_overview\.md)\)", block)
    expected = {".." + row["overview_path"][1:] for row in status}
    if len(queue_paths) != len(expected) or set(queue_paths) != expected:
        errors.append(f"synthesis queue mismatch: rows={len(queue_paths)}, unique={len(set(queue_paths))}, expected={len(expected)}")
    variants: dict[str, set[str]] = defaultdict(set)
    for item in papers:
        for tag in item.get("tags", []):
            variants[tag.casefold()].add(tag)
    case_variants = [value for value in variants.values() if len(value) > 1]
    if case_variants:
        errors.append(f"tag case variants: {case_variants}")
    generic = 0
    for row in status:
        if row["tier"] != "CORE":
            continue
        folder = (ROOT / row["overview_path"].lstrip("./")).parent
        text = "\n".join((folder / name).read_text(errors="ignore") for name in NOTE_NAMES)
        generic += any(term in text for term in ("자동 추출 실패", "survey-level 해석", "paper-specific cue"))
    if generic:
        warnings.append(f"CORE papers retaining old scaffold markers: {generic}")
    print({
        "papers": len(papers), "categories": len({p['category'] for p in papers}),
        "tier_counts": dict(counts), "intensive": len(status),
        "standard_note_files": len(papers) * len(NOTE_NAMES),
        "errors": errors, "warnings": warnings,
    })
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
