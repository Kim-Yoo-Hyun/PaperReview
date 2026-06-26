#!/usr/bin/env python3
"""Retry missing PDFs sequentially to avoid rate limits."""

from __future__ import annotations

import json
import time
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "survey_work" / "selected_papers.json"
HEADERS = {
    "User-Agent": "Mozilla/5.0 literature-survey-bot (academic personal use)",
}


def needs_pdf(paper: dict) -> bool:
    pdf = ROOT / paper["folder"] / "paper.pdf"
    return not pdf.exists() or pdf.stat().st_size < 20_000


def wait_for(url: str, attempt: int) -> None:
    if "openreview.net" in url:
        time.sleep(min(10 + attempt * 10, 60))
    else:
        time.sleep(min(2 + attempt * 2, 20))


def download(url: str, out: Path) -> tuple[bool, str]:
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".pdf.tmp")
    for attempt in range(5):
        try:
            with requests.get(url, headers=HEADERS, timeout=180, stream=True, allow_redirects=True) as r:
                if r.status_code == 429:
                    wait_for(url, attempt)
                    continue
                if r.status_code != 200:
                    last = f"HTTP {r.status_code}"
                    wait_for(url, attempt)
                    continue
                with tmp.open("wb") as f:
                    for chunk in r.iter_content(chunk_size=1024 * 64):
                        if chunk:
                            f.write(chunk)
                if tmp.read_bytes()[:4] != b"%PDF" or tmp.stat().st_size < 20_000:
                    last = "downloaded file is not a valid PDF"
                    wait_for(url, attempt)
                    continue
                tmp.replace(out)
                return True, "downloaded"
        except Exception as exc:
            last = str(exc)
            wait_for(url, attempt)
    if tmp.exists():
        tmp.unlink()
    return False, last


def main() -> None:
    papers = json.loads(MANIFEST.read_text(encoding="utf-8"))
    missing = [p for p in papers if needs_pdf(p)]
    print(f"missing before retry: {len(missing)}")
    ok = 0
    failed = []
    for idx, paper in enumerate(missing, 1):
        url = paper.get("pdf")
        out = ROOT / paper["folder"] / "paper.pdf"
        if not url:
            failed.append((paper["title"], "missing pdf url"))
            continue
        print(f"[{idx}/{len(missing)}] {paper['title'][:90]}")
        success, message = download(url, out)
        err = out.with_name("paper_pdf_error.txt")
        if success:
            ok += 1
            if err.exists():
                err.unlink()
            print("  ok")
        else:
            err.write_text(f"{url}\n{message}\n", encoding="utf-8")
            failed.append((paper["title"], message))
            print(f"  failed: {message}")
        if "openreview.net" in url:
            time.sleep(3)
    print(f"retried ok: {ok}")
    print(f"failed: {len(failed)}")
    for title, reason in failed[:50]:
        print(f"- {title}: {reason}")


if __name__ == "__main__":
    main()
