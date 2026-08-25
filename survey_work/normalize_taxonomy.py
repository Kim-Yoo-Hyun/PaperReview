#!/usr/bin/env python3
"""Normalize registry categories/tags without moving paper folders."""

from __future__ import annotations

import json
import re
import urllib.parse
from collections import Counter
from pathlib import Path

try:
    from taxonomy import canonicalize
except ModuleNotFoundError:
    from .taxonomy import canonicalize


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "survey_work" / "sources" / "papers.json"
REGISTRY = ROOT / "PAPER.md"
NOTES = ["01_overview.md", "02_problem.md", "03_method.md", "04_evaluation.md", "05_insights.md"]


def venue_label(value: str) -> str:
    value = re.sub(r"\b20\d{2}\b", "", value)
    value = re.sub(r"\bregular\b", "", value, flags=re.I)
    value = re.sub(r"\bSpotlightPoster\b", "Spotlight/Poster", value, flags=re.I)
    return re.sub(r"\s+", " ", value).strip(" -_/")


def update_note(path: Path, paper: dict) -> bool:
    text = path.read_text(encoding="utf-8")
    updated = re.sub(r"^- Category: .*?$", f"- Category: {paper['category']}", text, count=1, flags=re.M)
    updated = re.sub(r"^- Tags: .*?$", f"- Tags: {', '.join(paper['tags'])}", updated, count=1, flags=re.M)
    updated = re.sub(r"^- PDF status:.*?\n", "", updated, flags=re.M)
    if updated != text:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def registry(papers: list[dict]) -> str:
    groups: dict[str, list[dict]] = {}
    for item in papers:
        groups.setdefault(item["category"], []).append(item)
    lines = [
        "# PAPER Registry", "",
        "- Generated: 2026-08-25 KST",
        f"- Total papers with folders: {len(papers)}",
        "- Long-term reading tiers: [READING_PLAN.md](./research/READING_PLAN.md) and [READING_TIERS.csv](./research/READING_TIERS.csv)",
        "- Reading progress and synthesis: [READING_STATUS.csv](./research/READING_STATUS.csv), [READING_STATUS.md](./research/READING_STATUS.md), [synthesis/README.md](./synthesis/README.md)",
        "- Scope: Robotics-first literature registry spanning robot learning/control, VLA, and robotics-enabling 3D vision.",
        "- Taxonomy: one canonical category per paper; cross-cutting roles are represented with normalized tags.", "",
    ]
    for category in sorted(groups, key=str.casefold):
        lines += [f"## {category}", "", "| Year | Venue | Paper | Tags | PDF | Code/Project |", "|---:|---|---|---|---|---|"]
        for item in sorted(groups[category], key=lambda x: (x["year"], x["title"].casefold())):
            folder = urllib.parse.quote(item["folder"])
            pdf = f"[paper.pdf](./{folder}/paper.pdf)" if (ROOT / item["folder"] / "paper.pdf").exists() else "missing"
            project = item.get("project") or "not identified"
            project = f"[link]({project})" if project.startswith("http") else project
            lines.append(f"| {item['year']} | {venue_label(item['venue'])} | [{item['title']}](./{folder}/01_overview.md) | {', '.join(item['tags'])} | {pdf} | {project} |")
        lines.append("")
    lines += ["## Keyword Index", ""]
    tags: dict[str, list[dict]] = {}
    for item in papers:
        for tag in item["tags"]:
            tags.setdefault(tag, []).append(item)
    for tag in sorted(tags, key=str.casefold):
        refs = ", ".join(
            f"[{re.sub(r'[^A-Za-z0-9]+', '-', p['title']).strip('-')[:24]}](./{urllib.parse.quote(p['folder'])}/01_overview.md)"
            for p in tags[tag][:12]
        )
        lines.append(f"- **{tag}**: {refs}")
    return "\n".join(lines) + "\n"


def main() -> None:
    papers = json.loads(MANIFEST.read_text(encoding="utf-8"))
    before_categories = len({p["category"] for p in papers})
    changed_notes = 0
    for paper in papers:
        paper.pop("pdf_status", None)
        canonicalize(paper)
        folder = ROOT / paper["folder"]
        for name in NOTES:
            changed_notes += update_note(folder / name, paper)
    MANIFEST.write_text(json.dumps(papers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REGISTRY.write_text(registry(papers), encoding="utf-8")
    print({
        "papers": len(papers),
        "categories_before": before_categories,
        "categories_after": len({p["category"] for p in papers}),
        "tag_types_after": len(Counter(tag for p in papers for tag in p["tags"])),
        "note_headers_changed": changed_notes,
    })


if __name__ == "__main__":
    main()
