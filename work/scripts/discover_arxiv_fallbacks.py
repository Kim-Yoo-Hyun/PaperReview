#!/usr/bin/env python3
"""Find official arXiv copies for registry papers whose primary PDF is blocked.

This is a discovery helper only.  It writes candidate arXiv identifiers to the
task-scoped temporary directory; it does not change the registry or notes.
Candidates are accepted only when the arXiv title is a close match to the
registry title.  The downloader performs the final PDF validation.
"""

from __future__ import annotations

import argparse
import csv
import difflib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
PAPERS = ROOT / "work" / "sources" / "papers.json"
TIERS = ROOT / "research" / "READING_TIERS.csv"
DEFAULT_OUT = ROOT / "tmp" / "pdfs" / "fulltext_remaining_2026-09-01" / "arxiv_candidates.json"
USER_AGENT = "PaperReview-arxiv-source-audit/2026-09-01 (academic literature curation)"


def normalize(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"\\[a-z]+", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def selected_items() -> list[dict[str, Any]]:
    papers = {item["paper_id"]: item for item in json.loads(PAPERS.read_text(encoding="utf-8"))}
    with TIERS.open(newline="", encoding="utf-8") as handle:
        selected = {
            row["paper_id"]
            for row in csv.DictReader(handle)
            if row["tier"] not in {"CORE", "NEXT"}
        }
    manifest = ROOT / "tmp" / "pdfs" / "fulltext_remaining_2026-09-01" / "download_manifest.jsonl"
    failed = {
        json.loads(line)["paper_id"]
        for line in manifest.read_text(encoding="utf-8").splitlines()
        if line.strip() and json.loads(line).get("status") == "failed"
    }
    return [papers[paper_id] for paper_id in sorted(selected & failed)]


def parse_results(html: str, registry_title: str) -> list[dict[str, Any]]:
    target = normalize(registry_title)
    results: list[dict[str, Any]] = []
    soup = BeautifulSoup(html, "html.parser")
    for result in soup.select("li.arxiv-result"):
        title_node = result.select_one("p.title")
        abs_link = result.select_one('a[href*="/abs/"]')
        if not title_node or not abs_link:
            continue
        title = title_node.get_text(" ", strip=True)
        href = abs_link.get("href", "")
        match = re.search(r"/abs/([^/?#]+)", href)
        if not match:
            continue
        score = difflib.SequenceMatcher(None, target, normalize(title)).ratio()
        results.append(
            {
                "arxiv": match.group(1),
                "title": title,
                "score": round(score, 4),
                "abstract_url": f"https://arxiv.org/abs/{match.group(1)}",
                "pdf_url": f"https://arxiv.org/pdf/{match.group(1)}.pdf",
            }
        )
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--sleep", type=float, default=1.0)
    parser.add_argument("--min-score", type=float, default=0.78)
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    output = args.output if args.output.is_absolute() else ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    existing: dict[str, Any] = {}
    if output.exists():
        try:
            existing = json.loads(output.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing = {}

    items = selected_items()
    if args.limit > 0:
        items = items[: args.limit]
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html"})
    started = time.monotonic()
    for index, item in enumerate(items, start=1):
        if item["paper_id"] in existing and existing[item["paper_id"]].get("checked_at"):
            print(f"[{index}/{len(items)}] {item['paper_id']} cached", flush=True)
            continue
        query = quote_plus(item["title"])
        url = f"https://arxiv.org/search/?query={query}&searchtype=title&abstracts=show&order=-announced_date_first&size=50"
        try:
            response = session.get(url, timeout=(15, 45))
            response.raise_for_status()
            results = parse_results(response.text, item["title"])
            accepted = [result for result in results if result["score"] >= args.min_score]
            existing[item["paper_id"]] = {
                "paper_id": item["paper_id"],
                "registry_title": item["title"],
                "checked_at": datetime.now(timezone.utc).isoformat(),
                "source_search_url": url,
                "candidates": accepted[:10],
                "top_results": results[:10],
            }
            print(
                f"[{index}/{len(items)}] {item['paper_id']} "
                f"results={len(results)} accepted={len(accepted)}",
                flush=True,
            )
        except Exception as exc:  # noqa: BLE001 - preserve audit result
            existing[item["paper_id"]] = {
                "paper_id": item["paper_id"],
                "registry_title": item["title"],
                "checked_at": datetime.now(timezone.utc).isoformat(),
                "error": f"{type(exc).__name__}: {exc}",
            }
            print(f"[{index}/{len(items)}] {item['paper_id']} error={exc}", flush=True)
        output.write_text(json.dumps(existing, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if index < len(items):
            time.sleep(max(0.0, args.sleep))
    accepted_count = sum(bool(value.get("candidates")) for value in existing.values())
    print(
        {
            "checked_this_run": len(items),
            "papers_with_candidates": accepted_count,
            "output": str(output),
            "elapsed_seconds": round(time.monotonic() - started, 1),
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
