#!/usr/bin/env python3
"""Add humanoid papers inside the existing robotics taxonomy."""

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
EXTRA = WORK / "extra_papers_robotics_humanoid.json"
MANIFEST = WORK / "selected_papers.json"
LOG = WORK / "robotics_humanoid_augmentation_log.json"
AUDIT = WORK / "robotics_humanoid_note_audit_report.json"
SUPERSEDED_TITLES = {
    "Biped Walking Pattern Generation by Using Preview Control of Zero-Moment Point".casefold()
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
        and paper["title"].casefold() not in SUPERSEDED_TITLES
    }

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        extras = list(executor.map(survey.download_pdf, extras))

    by_title = {
        paper["title"].casefold(): paper
        for paper in existing
        if paper["title"].casefold() not in SUPERSEDED_TITLES
    }
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
