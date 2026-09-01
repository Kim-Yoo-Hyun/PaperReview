#!/usr/bin/env python3
"""Discover official NeurIPS 2025 proceedings PDFs for blocked records."""

from __future__ import annotations

import argparse
import csv
import difflib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
PAPERS = ROOT / "work" / "sources" / "papers.json"
TIERS = ROOT / "research" / "READING_TIERS.csv"
DEFAULT_DIR = ROOT / "tmp" / "pdfs" / "fulltext_remaining_2026-09-01"
DEFAULT_OUT = DEFAULT_DIR / "neurips_candidates.json"
MANIFEST = DEFAULT_DIR / "download_manifest.jsonl"
USER_AGENT = "PaperReview-proceedings-source-audit/2026-09-01 (academic literature curation)"


def normalize(value: str) -> str:
    value = value.lower().replace("&", " and ").replace("∞", " infinity ")
    value = re.sub(r"\\[a-z]+", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def selected_failed_neurips() -> list[dict[str, Any]]:
    papers = {item["paper_id"]: item for item in json.loads(PAPERS.read_text(encoding="utf-8"))}
    with TIERS.open(newline="", encoding="utf-8") as handle:
        selected = {
            row["paper_id"]
            for row in csv.DictReader(handle)
            if row["tier"] not in {"CORE", "NEXT"}
        }
    failed = {
        json.loads(line)["paper_id"]
        for line in MANIFEST.read_text(encoding="utf-8").splitlines()
        if line.strip() and json.loads(line).get("status") == "failed"
    }
    return [
        papers[paper_id]
        for paper_id in sorted(selected & failed)
        if papers[paper_id].get("venue") == "NeurIPS" and papers[paper_id].get("year") == 2025
    ]


def index_titles(html: str) -> list[tuple[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    result: list[tuple[str, str]] = []
    for abstract in soup.select('a[href*="Abstract-Conference.html"]'):
        title = abstract.get_text(" ", strip=True)
        if title and abstract.get("href"):
            result.append((title, abstract["href"]))
    return result


def best_match(title: str, entries: list[tuple[str, str]]) -> tuple[str, str, float] | None:
    target = normalize(title)
    best: tuple[str, str, float] | None = None
    for candidate_title, abstract_path in entries:
        candidate = normalize(candidate_title)
        score = difflib.SequenceMatcher(None, target, candidate).ratio()
        if best is None or score > best[2]:
            best = (candidate_title, abstract_path, score)
    return best


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    items = selected_failed_neurips()
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html"})
    index_url = "https://proceedings.neurips.cc/paper_files/paper/2025/vol38-main-conference"
    response = session.get(index_url, timeout=(20, 120))
    response.raise_for_status()
    entries = index_titles(response.text)
    records: dict[str, Any] = {}
    for item in items:
        match = best_match(item["title"], entries)
        candidates: list[dict[str, Any]] = []
        if match and match[2] >= 0.94:
            _, abstract_path, score = match
            abstract_url = "https://proceedings.neurips.cc" + abstract_path
            paper_url = abstract_url.replace("/hash/", "/file/").replace(
                "-Abstract-Conference.html", "-Paper-Conference.pdf"
            )
            candidates.append({"abstract_url": abstract_url, "pdf_url": paper_url, "score": round(score, 4)})
        records[item["paper_id"]] = {
            "paper_id": item["paper_id"],
            "registry_title": item["title"],
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "index_url": index_url,
            "candidates": candidates,
            "best_match": {
                "title": match[0],
                "score": round(match[2], 4),
            }
            if match
            else None,
        }
        print(item["paper_id"], "candidates=", len(candidates), records[item["paper_id"]]["best_match"], flush=True)
    output.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print({"selected": len(items), "with_candidates": sum(bool(x["candidates"]) for x in records.values()), "output": str(output)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
