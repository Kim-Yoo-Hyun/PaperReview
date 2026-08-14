#!/usr/bin/env python3
"""Add the curated robotics expansion without redownloading the full survey."""

from __future__ import annotations

import concurrent.futures
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import build_lit_survey as survey


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "survey_work"
EXTRA = WORK / "extra_papers_robotics.json"
MANIFEST = WORK / "selected_papers.json"
LOG = WORK / "robotics_augmentation_log.json"
AUDIT = WORK / "robotics_note_audit_report.json"


SAM2 = {
    "title": "SAM 2: Segment Anything in Images and Videos",
    "year": 2025,
    "venue": "ICLR",
    "category": "Foundations: Vision Foundation Models",
    "tags": ["segmentation", "foundation model", "prompting", "video segmentation", "memory"],
    "folder": "2025/ICLR/2025_ICLR_SAM-2-Segment-Anything-in-Images-and-Videos",
    "pdf": "https://arxiv.org/pdf/2408.00714",
    "page": "https://arxiv.org/abs/2408.00714",
    "project": "https://github.com/facebookresearch/sam2",
    "pdf_status": "not-present-locally",
}


def prepare(item: dict) -> dict:
    paper = dict(item)
    if paper.get("arxiv"):
        paper.setdefault("pdf", survey.arxiv_pdf(paper["arxiv"]))
        paper.setdefault("page", survey.arxiv_abs(paper["arxiv"]))
    return paper


def main() -> int:
    existing = json.loads(MANIFEST.read_text(encoding="utf-8"))
    extras = [prepare(item) for item in json.loads(EXTRA.read_text(encoding="utf-8"))]
    extra_titles = {paper["title"].casefold() for paper in extras}
    baseline_titles = {
        paper["title"].casefold()
        for paper in existing
        if paper["title"].casefold() not in extra_titles
    }
    baseline_titles.add(SAM2["title"].casefold())

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        extras = list(executor.map(survey.download_pdf, extras))

    for paper in extras:
        survey.write_notes(paper)

    by_title = {paper["title"].casefold(): paper for paper in existing}
    by_title.setdefault(SAM2["title"].casefold(), SAM2)
    for paper in extras:
        by_title[paper["title"].casefold()] = paper
    merged = list(by_title.values())

    survey.write_registry(merged)
    survey.write_manifest(merged)

    subprocess.run(
        [
            sys.executable,
            str(WORK / "regenerate_notes_from_pdf.py"),
            f"--only-source={EXTRA}",
            f"--report={AUDIT}",
        ],
        cwd=ROOT,
        check=True,
    )

    log = {
        "date": datetime.now().astimezone().isoformat(timespec="seconds"),
        "papers_before": len(baseline_titles),
        "papers_added": len(extras),
        "papers_after": len(merged),
        "downloaded": [paper["title"] for paper in extras if paper.get("pdf_status") == "downloaded"],
        "failed": [
            {"title": paper["title"], "status": paper.get("pdf_status", "unknown")}
            for paper in extras
            if paper.get("pdf_status") != "downloaded"
        ],
    }
    LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(log, ensure_ascii=False, indent=2))
    return 0 if not log["failed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
