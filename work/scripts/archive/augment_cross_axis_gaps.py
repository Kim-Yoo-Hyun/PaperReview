#!/usr/bin/env python3
"""Add papers that close cross-axis gaps across 3D vision, robotics, and VLA."""

from __future__ import annotations

import concurrent.futures
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import build_lit_survey as survey


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work"
EXTRA = WORK / "extra_papers_cross_axis_gaps.json"
MANIFEST = WORK / "selected_papers.json"
LOG = WORK / "cross_axis_gaps_augmentation_log.json"
AUDIT = WORK / "cross_axis_gaps_note_audit_report.json"
LINK_ONLY_TITLES = {
    "Learning to Be Uncertain: Pre-training World Models with Horizon-Calibrated Uncertainty".casefold()
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

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        extras = list(executor.map(survey.download_pdf, extras))

    by_title = {paper["title"].casefold(): paper for paper in existing}
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

    unsuccessful = [
        paper for paper in extras if paper.get("pdf_status") != "downloaded"
    ]
    linked_only = [
        paper for paper in unsuccessful if paper["title"].casefold() in LINK_ONLY_TITLES
    ]
    hard_failed = [
        paper for paper in unsuccessful if paper["title"].casefold() not in LINK_ONLY_TITLES
    ]
    log = {
        "date": datetime.now().astimezone().isoformat(timespec="seconds"),
        "papers_before": len(baseline_titles),
        "papers_added": len(extras),
        "papers_after": len(merged),
        "downloaded": [
            paper["title"] for paper in extras if paper.get("pdf_status") == "downloaded"
        ],
        "linked_only": [
            {"title": paper["title"], "status": paper.get("pdf_status", "unknown")}
            for paper in linked_only
        ],
        "failed": [
            {"title": paper["title"], "status": paper.get("pdf_status", "unknown")}
            for paper in hard_failed
        ],
    }
    LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(log, ensure_ascii=False, indent=2))
    return 0 if not hard_failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
