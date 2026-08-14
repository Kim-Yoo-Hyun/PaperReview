#!/usr/bin/env python3
"""Register the targeted robotics missing-link papers without downloading PDFs."""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

import build_lit_survey as survey


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "survey_work"
EXTRA = WORK / "extra_papers_robotics_missing_links.json"
MANIFEST = WORK / "selected_papers.json"
REGISTRY = ROOT / "PAPER.md"
LOG = WORK / "robotics_missing_links_augmentation_log.json"


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def header(paper: dict) -> str:
    return f"""- Year/Venue: {paper['year']} / {paper['venue']}
- Category: {paper['category']}
- Tags: {', '.join(paper['tags'])}
- Official paper: {paper['page']}
- Official PDF: {paper['pdf']}
- Code/Project: {paper['project']}
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.
"""


def write_notes(paper: dict) -> None:
    folder = ROOT / paper["folder"]
    folder.mkdir(parents=True, exist_ok=True)
    common = header(paper)
    notes = {
        "01_overview.md": f"""# {paper['title']}

{common}
## Why This Paper Is Here

{paper['role']}

## Problem

{paper['problem']}

## Core Idea

{bullets(paper['method'])}

## Observation / State / Action Interface

{paper['interface']}

## Evaluation Scope

{bullets(paper['evaluation'])}

## Limitations to Verify

{bullets(paper['limitations'])}

## Reading Lineage

`{paper['lineage']}`
""",
        "02_problem.md": f"""# Problem — {paper['title']}

{common}
## Target Problem

{paper['problem']}

## Core Assumptions

{bullets(paper['assumptions'])}

## Closed-Loop Position

이 논문은 현재 robotics loop에서 `{paper['lineage']}` 연결을 담당한다. 실제 정독 시 observation/state/action/control 중 어느 interface를 고정하고 어느 부분을 학습하는지 확인한다.

## Falsification Question

{paper['limitations'][0]}
""",
        "03_method.md": f"""# Method — {paper['title']}

{common}
## Pipeline

{bullets(paper['method'])}

## Interface

{paper['interface']}

## Implementation Audit

- Objective, horizon, control rate와 architecture detail은 full text 정독 후 확정한다.
- Official abstract가 지지하지 않는 loss, data size 또는 hardware detail은 추정하지 않는다.
- 후속 구현에서는 `{paper['lineage']}`의 앞뒤 논문과 공통 interface를 먼저 맞춘다.
""",
        "04_evaluation.md": f"""# Evaluation — {paper['title']}

{common}
## Verified Evaluation Scope

{bullets(paper['evaluation'])}

## Required Comparison Fields

- Embodiment/task와 simulation/real-robot 여부
- Observation, action representation, action horizon과 control rate
- Data source, demonstration quality와 train/test generalization split
- Success뿐 아니라 latency, intervention, failure severity와 reproducibility cost

## Reproducible Minimum

{paper['reproduction']}

## Manual Review Needed

- Exact trial count, uncertainty interval, baseline configuration와 ablation은 full text에서 확인한다.
""",
        "05_insights.md": f"""# Insights — {paper['title']}

{common}
## Paper-Supported Direction

{paper['role']}

## Researcher Interpretation

- Foundation/frontier connection: `{paper['lineage']}`
- 가장 먼저 반박할 가정: {paper['assumptions'][0]}
- 현재 gap과 연결할 때 success만 보지 않고 downstream control 또는 evaluation protocol의 변화를 확인한다.

## Limitations / Failure Modes to Audit

{bullets(paper['limitations'])}

## Minimum Experiment

{paper['reproduction']}

## Status

`UNREAD` — 이 노트는 official abstract 기반의 reading scaffold이며 정독 완료를 의미하지 않는다.
""",
    }
    for name, content in notes.items():
        (folder / name).write_text(content, encoding="utf-8")


def registry_row(paper: dict) -> str:
    project = f"[link]({paper['project']})"
    return (
        f"| {paper['year']} | {paper['venue']} | "
        f"[{paper['title']}](./{paper['folder']}/01_overview.md) | "
        f"{', '.join(paper['tags'])} | missing | {project} |"
    )


def update_registry(papers: list[dict], old_total: int) -> None:
    text = REGISTRY.read_text(encoding="utf-8")
    for paper in papers:
        if f"](./{paper['folder']}/01_overview.md)" in text:
            raise RuntimeError(f"Registry path already exists: {paper['folder']}")
        heading = f"## {paper['category']}"
        start = text.find(heading)
        if start < 0:
            raise RuntimeError(f"Missing registry category: {paper['category']}")
        next_heading = text.find("\n## ", start + len(heading))
        if next_heading < 0:
            next_heading = len(text)
        section = text[start:next_heading]
        rows = [line for line in section.splitlines() if re.match(r"^\| \d{4} \|", line)]
        rows.append(registry_row(paper))
        rows.sort(key=lambda line: (int(line.split("|")[1].strip()), line.casefold()))
        non_rows = [line for line in section.splitlines() if not re.match(r"^\| \d{4} \|", line)]
        insert_at = next(i for i, line in enumerate(non_rows) if line.startswith("|---:")) + 1
        rebuilt = non_rows[:insert_at] + rows + non_rows[insert_at:]
        text = text[:start] + "\n".join(rebuilt).rstrip() + "\n" + text[next_heading:]

    new_total = old_total + len(papers)
    text = re.sub(r"- Generated: .*", "- Generated: 2026-08-12 KST", text, count=1)
    text = text.replace(
        f"- Total papers with folders: {old_total}",
        f"- Total papers with folders: {new_total}",
        1,
    )
    text = re.sub(
        r"- Long-term reading tiers: .*",
        "- Long-term reading tiers: [READING_PLAN.md](./research/READING_PLAN.md) and [READING_TIERS.csv](./research/READING_TIERS.csv)",
        text,
        count=1,
    )
    text = re.sub(
        r"- Reading progress and synthesis: .*",
        "- Reading progress and synthesis: [READING_STATUS.csv](./research/READING_STATUS.csv), [READING_STATUS.md](./research/READING_STATUS.md), [synthesis/README.md](./synthesis/README.md)",
        text,
        count=1,
    )
    REGISTRY.write_text(text, encoding="utf-8")


def main() -> None:
    existing = json.loads(MANIFEST.read_text(encoding="utf-8"))
    extras = json.loads(EXTRA.read_text(encoding="utf-8"))
    existing_titles = {paper["title"].casefold() for paper in existing}
    duplicates = [paper["title"] for paper in extras if paper["title"].casefold() in existing_titles]
    if duplicates:
        raise RuntimeError(f"Duplicate titles: {duplicates}")

    for paper in extras:
        paper["folder"] = survey.folder_name(paper)
        paper["pdf_status"] = "not-downloaded"
        write_notes(paper)

    old_total = len(existing)
    update_registry(extras, old_total)
    standard_keys = [
        "title", "year", "venue", "category", "tags", "folder",
        "pdf", "page", "project", "pdf_status",
    ]
    merged = existing + [{key: paper.get(key) for key in standard_keys} for paper in extras]
    MANIFEST.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    LOG.write_text(
        json.dumps(
            {
                "date": datetime.now().astimezone().isoformat(timespec="seconds"),
                "papers_before": old_total,
                "papers_added": len(extras),
                "papers_after": len(merged),
                "pdf_policy": "official links only; no PDFs downloaded",
                "titles": [paper["title"] for paper in extras],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"registered {len(extras)} papers: {old_total} -> {len(merged)}")


if __name__ == "__main__":
    main()
