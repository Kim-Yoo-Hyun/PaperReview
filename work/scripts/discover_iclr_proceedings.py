#!/usr/bin/env python3
"""Discover official ICLR proceedings PDFs for blocked OpenReview records."""

from __future__ import annotations

import argparse
import csv
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
PAPERS = ROOT / "work" / "sources" / "papers.json"
TIERS = ROOT / "research" / "READING_TIERS.csv"
DEFAULT_DIR = ROOT / "tmp" / "pdfs" / "fulltext_remaining_2026-09-01"
DEFAULT_OUT = DEFAULT_DIR / "iclr_candidates.json"
MANIFEST = DEFAULT_DIR / "download_manifest.jsonl"
USER_AGENT = "PaperReview-proceedings-source-audit/2026-09-01 (academic literature curation)"


def selected_failed_iclr() -> list[dict[str, Any]]:
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
        if papers[paper_id].get("venue") == "ICLR"
    ]


def find_links(html: str, title: str) -> list[dict[str, str]]:
    target = re.sub(r"\s+", " ", title.lower()).strip()
    soup = BeautifulSoup(html, "html.parser")
    candidates: list[dict[str, str]] = []
    for anchor in soup.select('a[href*="Abstract-Conference.html"]'):
        text = re.sub(r"\s+", " ", anchor.get_text(" ", strip=True).lower()).strip()
        href = anchor.get("href", "")
        if not href or (target not in text and text not in target):
            continue
        abstract_url = "https://proceedings.iclr.cc" + href if href.startswith("/") else href
        paper_url = abstract_url.replace("/hash/", "/file/").replace(
            "-Abstract-Conference.html", "-Paper-Conference.pdf"
        )
        candidates.append({"abstract_url": abstract_url, "pdf_url": paper_url})
    return candidates


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--sleep", type=float, default=0.4)
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    records: dict[str, Any] = {}
    if output.exists():
        try:
            records = json.loads(output.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            records = {}
    items = selected_failed_iclr()
    if args.limit > 0:
        items = items[: args.limit]
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html"})
    for index, item in enumerate(items, start=1):
        if item["paper_id"] in records and records[item["paper_id"]].get("checked_at"):
            print(f"[{index}/{len(items)}] {item['paper_id']} cached", flush=True)
            continue
        search_url = "https://proceedings.iclr.cc/papers/search?q=" + quote(item["title"])
        try:
            response = session.get(search_url, timeout=(15, 45))
            response.raise_for_status()
            candidates = find_links(response.text, item["title"])
            records[item["paper_id"]] = {
                "paper_id": item["paper_id"],
                "registry_title": item["title"],
                "checked_at": datetime.now(timezone.utc).isoformat(),
                "search_url": search_url,
                "candidates": candidates,
            }
            print(f"[{index}/{len(items)}] {item['paper_id']} candidates={len(candidates)}", flush=True)
        except Exception as exc:  # noqa: BLE001 - preserve source audit
            records[item["paper_id"]] = {
                "paper_id": item["paper_id"],
                "registry_title": item["title"],
                "checked_at": datetime.now(timezone.utc).isoformat(),
                "search_url": search_url,
                "error": f"{type(exc).__name__}: {exc}",
            }
            print(f"[{index}/{len(items)}] {item['paper_id']} error={exc}", flush=True)
        output.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if index < len(items):
            time.sleep(max(0.0, args.sleep))
    print({"checked": len(items), "with_candidates": sum(bool(x.get("candidates")) for x in records.values()), "output": str(output)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
