#!/usr/bin/env python3
"""Normalize registry categories/tags without moving paper folders."""

from __future__ import annotations

import hashlib
import json
import re
import urllib.parse
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

try:
    from taxonomy import canonicalize
    from registry_schema import canonical_venue, enrich_record
except ModuleNotFoundError:
    from .taxonomy import canonicalize
    from .registry_schema import canonical_venue, enrich_record


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
META = ROOT / "work" / "sources" / "registry_meta.json"
REGISTRY = ROOT / "PAPER.md"
NOTES = ["01_overview.md", "02_problem.md", "03_method.md", "04_evaluation.md", "05_insights.md"]


def venue_label(value: str) -> str:
    return canonical_venue(value)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def update_note(path: Path, paper: dict) -> bool:
    text = path.read_text(encoding="utf-8")
    updated = re.sub(r"^- Category: .*?$", f"- Category: {paper['category']}", text, count=1, flags=re.M)
    updated = re.sub(r"^- Tags: .*?$", f"- Tags: {', '.join(paper['tags'])}", updated, count=1, flags=re.M)
    aliases = paper.get("aliases") or []
    if aliases:
        alias_line = f"- Aliases: {', '.join(aliases)}"
        if re.search(r"^- Aliases: .*?$", updated, flags=re.M):
            updated = re.sub(r"^- Aliases: .*?$", alias_line, updated, count=1, flags=re.M)
        else:
            updated = re.sub(
                r"^(- Tags: .*?$)",
                rf"\1\n{alias_line}",
                updated,
                count=1,
                flags=re.M,
            )
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
        "# 논문 목록", "",
        f"- Generated: {datetime.now(ZoneInfo('Asia/Seoul')).date().isoformat()} KST",
        f"- Total papers with folders: {len(papers)}",
        "", '<a id="keyword-index"></a>', '<a id="alias-index"></a>', "",
        "분야별 표에서 제목과 태그를 찾을 수 있다. 별칭은 해당 논문의 제목 뒤에 표시한다. "
        "여러 분야를 한 번에 검색할 때는 색인의 `tags`와 `aliases` 열을 사용한다. "
        "[전체 검색 색인](./research/REGISTRY_INDEX.csv) · [읽기 계획](./research/READING_PLAN.md) · [원장](./work/sources/papers.json)", "",
    ]
    for category in sorted(groups, key=str.casefold):
        lines += [f"## {category}", "", "| Year | Venue | Paper | Tags | PDF | Code/Project |", "|---:|---|---|---|---|---|"]
        for item in sorted(groups[category], key=lambda x: (x["year"], x["title"].casefold())):
            folder = urllib.parse.quote(item["folder"])
            pdf = f"[paper.pdf](./{folder}/paper.pdf)" if (ROOT / item["folder"] / "paper.pdf").exists() else "missing"
            project = item.get("project") or "not identified"
            sources = item.get("sources") or {}
            for kind in ("project", "code"):
                source = sources.get(kind) or {}
                if source.get("url"):
                    project = source["url"]
                    break
            project = f"[link]({project})" if project.startswith("http") else project
            paper_link = f"[{item['title']}](./{folder}/01_overview.md)"
            aliases = [alias.replace("\\", "\\\\").replace("|", "\\|") for alias in item.get("aliases", [])]
            if aliases:
                paper_link += " (" + ", ".join(aliases) + ")"
            lines.append(f"| {item['year']} | {venue_label(item.get('venue_canonical', item['venue']))} | {paper_link} | {', '.join(item['tags'])} | {pdf} | {project} |")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    papers = json.loads(MANIFEST.read_text(encoding="utf-8"))
    before_categories = len({p["category"] for p in papers})
    changed_notes = 0
    for paper in papers:
        paper.pop("pdf_status", None)
        canonicalize(paper)
        if "publication" in paper:
            enrich_record(paper, root=ROOT)
        folder = ROOT / paper["folder"]
        for name in NOTES:
            changed_notes += update_note(folder / name, paper)
    MANIFEST.write_text(json.dumps(papers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REGISTRY.write_text(registry(papers), encoding="utf-8")
    if META.exists():
        meta = json.loads(META.read_text(encoding="utf-8"))
        meta["paper_count"] = len(papers)
        meta["generated_on"] = datetime.now(ZoneInfo("Asia/Seoul")).date().isoformat()
        meta["manifest_sha256"] = sha256(MANIFEST)
        META.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print({
        "papers": len(papers),
        "categories_before": before_categories,
        "categories_after": len({p["category"] for p in papers}),
        "tag_types_after": len(Counter(tag for p in papers for tag in p["tags"])),
        "note_headers_changed": changed_notes,
    })


if __name__ == "__main__":
    main()
