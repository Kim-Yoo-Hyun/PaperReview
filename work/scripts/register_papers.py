#!/usr/bin/env python3
"""Register paper metadata and curation notes; never download PDFs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    import build_lit_survey as survey
    from normalize_taxonomy import registry
    from taxonomy import canonicalize
except ModuleNotFoundError:
    from . import build_lit_survey as survey
    from .normalize_taxonomy import registry
    from .taxonomy import canonicalize


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
NOTE_NAMES = ["01_overview.md", "02_problem.md", "03_method.md", "04_evaluation.md", "05_insights.md"]
REQUIRED = {"title", "year", "venue", "category", "tags", "page"}


def notes(item: dict) -> dict[str, str]:
    common = f"""- Year/Venue: {item['year']} / {item['venue']}
- Category: {item['category']}
- Tags: {', '.join(item['tags'])}
- Official paper: {item['page']}
- Code/Project: {item.get('project', 'not identified')}
- Source audit: metadata registration only; full-text claims are UNVERIFIED.
"""
    warning = "> Evidence maturity: `CURATION_ONLY`. 이 문서는 정독 완료를 뜻하지 않는다.\n"
    return {
        "01_overview.md": f"# {item['title']}\n\n{warning}\n{common}\n## Why This Paper Is Here\n\n{item.get('role', 'Registry admission rationale must be verified during reading.')}\n\n## Problem\n\nUNVERIFIED — official abstract/full text에서 확인한다.\n\n## Core Idea\n\nUNVERIFIED — method section에서 확인한다.\n\n## Interface\n\nUNVERIFIED — observation/state/action/control interface를 확인한다.\n\n## Evaluation Scope\n\nUNVERIFIED — embodiment, task, data, metrics와 baselines를 확인한다.\n",
        "02_problem.md": f"# Problem — {item['title']}\n\n{warning}\n{common}\n## Target Problem and Assumptions\n\nUNVERIFIED — 문제 formulation, bottleneck과 핵심 가정을 full text에서 확인한다.\n\n## Closed-Loop Position\n\n`observation → state/world model → task & motion decision → policy/control → contact → feedback/recovery` 중 위치를 정독 후 기록한다.\n",
        "03_method.md": f"# Method — {item['title']}\n\n{warning}\n{common}\n## Pipeline\n\nUNVERIFIED — objective, representation, temporal horizon와 planner/controller interface를 확인한다.\n\n## Implementation Audit\n\nLoss, architecture, data scale, control rate와 hardware detail은 source location과 함께 기록한다.\n",
        "04_evaluation.md": f"# Evaluation — {item['title']}\n\n{warning}\n{common}\n## Protocol\n\nUNVERIFIED — embodiment, simulator/real robot, task, dataset split, metric, baseline와 trial count를 확인한다.\n\n## Failure and Reproducibility\n\nUNVERIFIED — negative result, failure condition, code/checkpoint와 compute dependency를 확인한다.\n",
        "05_insights.md": f"# Insights — {item['title']}\n\n{warning}\n{common}\n## Reading Dependency\n\nUNVERIFIED — 어떤 CORE에서 출발하고 어떤 frontier로 이어지는지 확인한다.\n\n## Research Use\n\n정독 후 paper-supported conclusion과 researcher interpretation을 분리한다.\n\n## Minimal Reproduction\n\nUNVERIFIED — 가장 작은 반증 실험을 정의한다.\n",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path, help="JSON list of paper metadata")
    parser.add_argument("--apply", action="store_true", help="write changes; default is dry-run")
    args = parser.parse_args()
    incoming = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(incoming, list):
        raise SystemExit("input must be a JSON list")
    existing = json.loads(MANIFEST.read_text(encoding="utf-8"))
    titles = {item["title"].casefold() for item in existing}
    accepted = []
    skipped = []
    for raw in incoming:
        missing = sorted(REQUIRED - raw.keys())
        if missing:
            raise SystemExit(f"{raw.get('title', '<untitled>')}: missing {missing}")
        item = canonicalize(dict(raw))
        if item["title"].casefold() in titles:
            skipped.append(item["title"])
            continue
        item["folder"] = survey.folder_name(item)
        item.setdefault("pdf", "")
        item.setdefault("project", "not identified")
        accepted.append(item)
        titles.add(item["title"].casefold())
    print({"mode": "apply" if args.apply else "dry-run", "accepted": len(accepted), "skipped_existing": len(skipped)})
    if not args.apply:
        for item in accepted:
            print(f"+ {item['title']} -> {item['folder']}")
        return
    for item in accepted:
        folder = ROOT / item["folder"]
        folder.mkdir(parents=True, exist_ok=True)
        for name, content in notes(item).items():
            path = folder / name
            if path.exists():
                raise SystemExit(f"refusing to overwrite {path}")
            path.write_text(content, encoding="utf-8")
    merged = existing + accepted
    MANIFEST.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "PAPER.md").write_text(registry(merged), encoding="utf-8")


if __name__ == "__main__":
    main()
