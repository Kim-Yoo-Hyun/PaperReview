#!/usr/bin/env python3
"""Download and validate full-text PDFs for a selected registry tier set.

The files are deliberately stored in a task-scoped temporary directory rather
than in paper folders.  The companion review script consumes this manifest and
the temporary PDFs; the temporary directory is removed only after the notes and
the final validation have completed.

This script does not change the registry, reading status, or evidence level.
It is safe to run repeatedly: a previously validated file is reused unless
``--force`` is passed.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urljoin, urlparse

import requests

try:
    import fitz  # PyMuPDF
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyMuPDF (fitz) is required to validate downloaded PDFs") from exc


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
TIERS = ROOT / "research" / "READING_TIERS.csv"
DEFAULT_OUT = ROOT / "tmp" / "pdfs" / "fulltext_remaining_2026-09-01"
DEFAULT_LOG = DEFAULT_OUT / "download_manifest.jsonl"
DISCOVERED_ARXIV = DEFAULT_OUT / "arxiv_candidates.json"
DISCOVERED_ICLR = DEFAULT_OUT / "iclr_candidates.json"
DISCOVERED_NEURIPS = DEFAULT_OUT / "neurips_candidates.json"
DISCOVERED_PMLR = DEFAULT_OUT / "pmlr_candidates.json"

USER_AGENT = (
    "PaperReview-fulltext-audit/2026-09-01 "
    "(academic literature curation; contact repository owner if needed)"
)

# These entries fill only registry records whose PDF field was empty.  The
# links are official arXiv/PMLR/OpenReview pages or author/institution-hosted
# copies found during the source audit.
PDF_FALLBACKS = {
    "pr-0829": "https://people.csail.mit.edu/tlp/pdf/2011/hpnICRA11Final.pdf",
    "pr-0841": "https://arxiv.org/pdf/2203.06173.pdf",
    "pr-0844": "https://proceedings.mlr.press/v100/yu20a/yu20a.pdf",
    "pr-0845": "https://proceedings.mlr.press/v100/dasari20a/dasari20a.pdf",
    "pr-0846": "https://arxiv.org/pdf/2009.12293.pdf",
    "pr-0847": "https://arxiv.org/pdf/2107.14483.pdf",
    "pr-0850": "https://arxiv.org/pdf/2012.08456.pdf",
    "pr-0853": "https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf",
    "pr-0854": "https://arxiv.org/pdf/1602.01783.pdf",
    "pr-0862": "https://arxiv.org/pdf/2301.04195.pdf",
    "pr-0863": "https://arxiv.org/pdf/2511.04831.pdf",
    # Official preprints located during the full-text source audit.
    "pr-0150": "https://arxiv.org/pdf/2601.21602.pdf",
    "pr-0151": "https://arxiv.org/pdf/2602.02459.pdf",
    "pr-0152": "https://arxiv.org/pdf/2508.20072.pdf",
    "pr-0153": "https://arxiv.org/pdf/2607.03449.pdf",
    "pr-0154": "https://arxiv.org/pdf/2602.21157.pdf",
    "pr-0155": "https://arxiv.org/pdf/2601.05248.pdf",
    "pr-0157": "https://arxiv.org/pdf/2509.23155.pdf",
    "pr-0158": "https://arxiv.org/pdf/2506.18088.pdf",
    "pr-0159": "https://arxiv.org/pdf/2512.20014.pdf",
    "pr-0160": "https://arxiv.org/pdf/2602.01166.pdf",
    "pr-0162": "https://arxiv.org/pdf/2511.02776.pdf",
    "pr-0163": "https://arxiv.org/pdf/2605.10118.pdf",
    "pr-0164": "https://arxiv.org/pdf/2605.17522.pdf",
    "pr-0166": "https://arxiv.org/pdf/2606.27807.pdf",
    "pr-0167": "https://arxiv.org/pdf/2602.00222.pdf",
    "pr-0169": "https://arxiv.org/pdf/2608.01899.pdf",
    "pr-0456": "https://arxiv.org/pdf/2602.05508.pdf",
    "pr-0457": "https://arxiv.org/pdf/2510.10726.pdf",
    "pr-0459": "https://arxiv.org/pdf/2607.02515.pdf",
    "pr-0461": "https://arxiv.org/pdf/2603.14232.pdf",
    "pr-0462": "https://arxiv.org/pdf/2604.26238.pdf",
    "pr-0463": "https://arxiv.org/pdf/2601.01075.pdf",
    "pr-0464": "https://arxiv.org/pdf/2508.02831.pdf",
    "pr-0467": "https://arxiv.org/pdf/2409.19152.pdf",
    "pr-0468": "https://arxiv.org/pdf/2404.15259.pdf",
    "pr-0469": "https://arxiv.org/pdf/2406.04343.pdf",
    "pr-0470": "https://arxiv.org/pdf/2411.19271.pdf",
    "pr-0471": "https://arxiv.org/pdf/2408.10154.pdf",
    "pr-0472": "https://arxiv.org/pdf/2408.08206.pdf",
    "pr-0473": "https://arxiv.org/pdf/2312.00206.pdf",
    "pr-0474": "https://arxiv.org/pdf/2407.17310.pdf",
    "pr-0475": "https://arxiv.org/pdf/2502.07505.pdf",
    "pr-0476": "https://arxiv.org/pdf/2408.07825.pdf",
    "pr-0477": "https://arxiv.org/pdf/2406.13896.pdf",
    "pr-0478": "https://arxiv.org/pdf/2312.17250.pdf",
    "pr-0479": "https://arxiv.org/pdf/2409.09896.pdf",
    "pr-0480": "https://arxiv.org/pdf/2412.05557.pdf",
    "pr-0481": "https://arxiv.org/pdf/2411.06173.pdf",
    "pr-0161": "https://arxiv.org/pdf/2511.19912.pdf",
    "pr-0466": "https://arxiv.org/pdf/2605.18507.pdf",
    # OpenReview's public PDF endpoints returned an access challenge during
    # this audit. ChatPaper's public download endpoint serves the cached
    # OpenReview PDF; the reviewer verifies its title/authors/page text before
    # using it as full-text evidence.
    "pr-0149": "https://chatpaper.com/api/v1/articles/download/327408",
    "pr-0165": "https://chatpaper.com/api/v1/articles/download/326105",
    "pr-0458": "https://chatpaper.com/api/v1/articles/download/331054",
    "pr-0460": "https://chatpaper.com/api/v1/articles/download/331577",
    "pr-0465": "https://chatpaper.com/api/v1/articles/download/328620",
    # OpenReview/venue pages whose public PDF endpoint was challenged during
    # the CORE/NEXT pass; the matching arXiv version is used and verified by
    # page count and first-page title overlap before it can become evidence.
    "pr-0071": "https://arxiv.org/pdf/2410.00371",
    "pr-0076": "https://arxiv.org/pdf/2412.05268",
    "pr-0083": "https://arxiv.org/pdf/2410.07864",
    "pr-0086": "https://arxiv.org/pdf/2510.17439",
    "pr-0096": "https://arxiv.org/pdf/2512.16909",
    "pr-0105": "https://arxiv.org/pdf/2505.21351",
    "pr-0111": "https://arxiv.org/pdf/2506.04308",
    "pr-0168": "https://arxiv.org/pdf/2602.00807",
    "pr-0745": "https://arxiv.org/pdf/2210.02747",
    "pr-0858": "https://arxiv.org/pdf/2401.12963",
    "pr-0861": "https://arxiv.org/pdf/2108.10470",
    "pr-0864": "https://arxiv.org/pdf/2310.12931",
    "pr-0866": "https://arxiv.org/pdf/2210.13702",
    "pr-0868": "https://arxiv.org/pdf/2410.21229",
    "pr-0870": "https://arxiv.org/pdf/2505.12705",
    "pr-0872": "https://arxiv.org/pdf/2511.07820",
    "pr-0919": "https://arxiv.org/pdf/2508.13103",
    "pr-0920": "https://ojs.aaai.org/index.php/AAAI/article/download/38919/42881",
    "pr-0921": "https://ojs.aaai.org/index.php/AAAI/article/download/34866/37021",
    "pr-0922": "https://arxiv.org/pdf/2404.16423",
    "pr-0923": "https://ojs.aaai.org/index.php/AAAI/article/download/33610/35765",
    "pr-0924": "https://ojs.aaai.org/index.php/AAAI/article/download/33617/35772",
    # RSS proceedings downloads can be large or terminate early under a
    # long-lived chunked response.  These official arXiv versions are used
    # only as retrieval fallbacks; the registry's proceedings source remains
    # canonical.
    "pr-0929": "https://arxiv.org/pdf/2403.10454.pdf",
    "pr-0931": "https://arxiv.org/pdf/2402.17768.pdf",
    "pr-0934": "https://arxiv.org/pdf/2402.19432.pdf",
    # ICML's 2024 event page does not expose the article PDF directly.
    "pr-0939": "https://arxiv.org/pdf/2403.09631.pdf",
    "pr-0156": "https://arxiv.org/pdf/2605.22283",
    "pr-0825": "https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/5/1384/files/2025/02/1985-impedance-control-an-approach-to-manipulation-part-I-theory.pdf",
    "pr-0826": "https://graphics.stanford.edu/courses/cs348a-21-winter/Handouts/Besl92.pdf",
    "pr-0827": "https://people.eecs.berkeley.edu/~jfc/papers/92/FCicra92.pdf",
    "pr-0828": "https://www.scispace.com/pdf/biped-walking-pattern-generation-by-using-preview-control-of-84qdve2k8v.pdf",
    "pr-0830": "http://mlg.eng.cam.ac.uk/pub/pdf/DeiRas11.pdf",
    "pr-0831": "https://homes.cs.washington.edu/~todorov/papers/TodorovIROS12.pdf",
    "pr-0833": "https://nolanwagener.github.io/media/mppi/paper.pdf",
    "pr-0834": "https://arxiv.org/pdf/1608.01335",
    "pr-0848": "https://web.stanford.edu/class/cs114/readings/MK-Yuan.pdf",
    "pr-0849": "https://arxiv.org/pdf/2005.14679",
    "pr-0851": "https://xbpeng.github.io/projects/AMP/AMP_2021.pdf",
    "pr-0855": "https://arxiv.org/pdf/1806.06920",
    # The ASME endpoint is a scan with no usable text layer.  This public
    # transcription mirror preserves the article body as searchable PDF text;
    # the DOI remains the canonical bibliographic source and equations are
    # still treated as page-anchored evidence rather than copied verbatim.
    "pr-0823": "https://dl.icdst.org/pdfs/files/4133b00a8bb6a836906454c19812cdc6.pdf",
    "pr-0551": "https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/PRM/prmbasic_01.pdf",
    "pr-0552": "https://msl.cs.illinois.edu/~lavalle/papers/Lav98c.pdf",
    "pr-0558": "https://web.archive.org/web/20240419050012id_/http://rll.berkeley.edu/trajopt/ijrr/2013-IJRR-TRAJOPT.pdf",
    "pr-0820": "https://www.roboticsproceedings.org/rss21/p103.pdf",
    "pr-0827": "https://users.cs.duke.edu/~tomasi/public/ReadingGroup/Ferrari%20and%20Canny%20ICRA%201992.pdf",
    "pr-0828": "https://people.csail.mit.edu/katiebyl/kb/DW2008/papers_of_tangential_interest/kajita03.pdf",
    "pr-0831": "https://www.roboti.us/lab/papers/TodorovIROS12.pdf",
}

PREFERRED_FALLBACK_IDS = {"pr-0551", "pr-0552", "pr-0558", "pr-0820", "pr-0823"}


def read_selected(
    tier_names: set[str] | None = None,
    paper_ids: set[str] | None = None,
) -> list[dict[str, Any]]:
    papers = {item["paper_id"]: item for item in json.loads(MANIFEST.read_text())}
    selected_tiers = tier_names or {"REFERENCE", "ARCHIVE"}
    with TIERS.open(newline="", encoding="utf-8") as handle:
        selected_ids = {
            row["paper_id"]
            for row in csv.DictReader(handle)
            if row["tier"] in selected_tiers
        }
    if paper_ids:
        selected_ids &= paper_ids
    return [papers[paper_id] for paper_id in sorted(selected_ids)]


def arxiv_fallback(item: dict[str, Any]) -> str | None:
    arxiv_id = (item.get("identifiers") or {}).get("arxiv")
    if not arxiv_id:
        return None
    return f"https://arxiv.org/pdf/{arxiv_id}.pdf"


def pmlr_fallback(item: dict[str, Any]) -> str | None:
    page = item.get("page") or ""
    match = re.search(r"proceedings\.mlr\.press/(v[^/]+/[^/]+)\.html", page)
    if not match:
        return None
    stem = match.group(1)
    return f"https://proceedings.mlr.press/{stem}/{stem.rsplit('/', 1)[-1]}.pdf"


def openreview_fallback(item: dict[str, Any]) -> str | None:
    page = item.get("page") or ""
    if "openreview.net" not in page:
        return None
    match = re.search(r"[?&]id=([^&]+)", page)
    if match:
        return f"https://openreview.net/pdf?id={match.group(1)}"
    return None


def discovered_arxiv_fallback(item: dict[str, Any]) -> str | None:
    if not DISCOVERED_ARXIV.exists():
        return None
    try:
        records = json.loads(DISCOVERED_ARXIV.read_text(encoding="utf-8"))
        candidates = records.get(item["paper_id"], {}).get("candidates", [])
        for candidate in candidates:
            arxiv_id = candidate.get("arxiv")
            if candidate.get("score", 0) >= 0.78 and arxiv_id:
                return f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    except (OSError, json.JSONDecodeError, AttributeError):
        return None
    return None


def discovered_iclr_fallback(item: dict[str, Any]) -> str | None:
    if not DISCOVERED_ICLR.exists():
        return None
    try:
        records = json.loads(DISCOVERED_ICLR.read_text(encoding="utf-8"))
        candidates = records.get(item["paper_id"], {}).get("candidates", [])
        for candidate in candidates:
            url = candidate.get("pdf_url")
            if isinstance(url, str) and url.startswith("https://proceedings.iclr.cc/"):
                return url
    except (OSError, json.JSONDecodeError, AttributeError):
        return None
    return None


def discovered_venue_fallback(path: Path, paper_id: str, prefix: str) -> str | None:
    if not path.exists():
        return None
    try:
        records = json.loads(path.read_text(encoding="utf-8"))
        candidates = records.get(paper_id, {}).get("candidates", [])
        for candidate in candidates:
            url = candidate.get("pdf_url")
            if isinstance(url, str) and url.startswith(prefix):
                return url
    except (OSError, json.JSONDecodeError, AttributeError):
        return None
    return None


def candidates(item: dict[str, Any]) -> list[str]:
    urls: list[str] = []
    preferred_fallback = (
        PDF_FALLBACKS.get(item["paper_id"])
        if item["paper_id"] in PREFERRED_FALLBACK_IDS
        else None
    )
    ordered = (
        # Prefer validated alternate copies for legacy scans or records whose
        # prior local cache failed the title/source audit; canonical publisher
        # metadata remains in the registry and note header.
        preferred_fallback,
        item.get("pdf"),
        item.get("page") if str(item.get("page", "")).lower().endswith(".pdf") else None,
        ((item.get("sources") or {}).get("paper_pdf") or {}).get("url"),
        PDF_FALLBACKS.get(item["paper_id"]),
        arxiv_fallback(item),
        discovered_arxiv_fallback(item),
        discovered_iclr_fallback(item),
        discovered_venue_fallback(
            DISCOVERED_NEURIPS, item["paper_id"], "https://proceedings.neurips.cc/"
        ),
        discovered_venue_fallback(
            DISCOVERED_PMLR, item["paper_id"], "https://raw.githubusercontent.com/mlresearch/"
        ),
        pmlr_fallback(item),
        openreview_fallback(item),
    )
    for url in ordered:
        if isinstance(url, str) and url.startswith(("http://", "https://")) and url not in urls:
            urls.append(url)
    return urls


def overview_pdf_candidates(item: dict[str, Any]) -> list[str]:
    """Recover explicit PDF links that were recorded only in the overview."""
    overview = ROOT / unquote(str(item.get("folder", ""))) / "01_overview.md"
    if not overview.exists():
        return []
    try:
        text = overview.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    result: list[str] = []
    for raw in re.findall(r"https?://[^)\s>]+", text):
        url = html.unescape(raw).rstrip(".,;\"]")
        lower = url.casefold()
        if ".pdf" not in lower and "/pdf/" not in lower and "download" not in lower:
            continue
        if url not in result:
            result.append(url)
    return result


def discover_page_pdf_links(
    item: dict[str, Any],
    session: requests.Session,
    timeout: tuple[float, float],
) -> list[str]:
    """Find PDF/download anchors on official paper or proceedings pages.

    Several proceedings and publisher pages do not expose their PDF URL in
    the structured registry metadata.  Discovery is restricted to the paper's
    recorded primary/page URLs and only returns links that look like a PDF or
    an explicit article download endpoint.
    """
    pages: list[str] = []
    for value in (
        item.get("page"),
        ((item.get("sources") or {}).get("primary") or {}).get("url"),
    ):
        if not isinstance(value, str) or not value.startswith(("http://", "https://")):
            continue
        if value not in pages and not value.casefold().endswith(".pdf"):
            pages.append(value)
    found: list[tuple[int, str]] = []
    for page_url in pages:
        try:
            response = session.get(page_url, timeout=timeout, allow_redirects=True)
            if response.status_code >= 400:
                continue
            source_url = response.url or page_url
            body = response.text
        except requests.RequestException:
            continue
        for href in re.findall(r"(?:href|data-href)\s*=\s*[\"']([^\"']+)", body, re.I):
            absolute = urljoin(source_url, html.unescape(href).strip())
            parsed = urlparse(absolute)
            if parsed.scheme not in {"http", "https"}:
                continue
            lower = absolute.casefold()
            score = 0
            if ".pdf" in lower:
                score += 10
            if "/article/download/" in lower or "/download/" in lower:
                score += 8
            if "/pdf" in lower or "download" in lower:
                score += 3
            if score and absolute not in {url for _, url in found}:
                found.append((score, absolute))
    found.sort(key=lambda pair: (-pair[0], pair[1]))
    return [url for _, url in found[:12]]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_pdf(path: Path) -> tuple[int, int, str | None]:
    with path.open("rb") as handle:
        magic = handle.read(5)
    if magic != b"%PDF-":
        raise ValueError("downloaded response is not a PDF")
    document = fitz.open(path)
    try:
        pages = document.page_count
        first_text = document.load_page(0).get_text("text") if pages else ""
    finally:
        document.close()
    if pages < 1:
        raise ValueError("PDF has no pages")
    return pages, len(first_text), magic.decode("ascii", errors="ignore")


def download_one(
    item: dict[str, Any],
    output_dir: Path,
    *,
    timeout: tuple[float, float],
    force: bool,
) -> dict[str, Any]:
    paper_id = item["paper_id"]
    target = output_dir / f"{paper_id}.pdf"
    base: dict[str, Any] = {
        "paper_id": paper_id,
        "title": item["title"],
        "folder": item["folder"],
        "target": str(target.relative_to(ROOT)),
        "candidate_urls": candidates(item) + overview_pdf_candidates(item),
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }

    if target.exists() and not force:
        try:
            pages, first_chars, magic = validate_pdf(target)
            base.update(
                {
                    "status": "reused",
                    "url": None,
                    "http_status": None,
                    "content_type": "local-cache",
                    "bytes": target.stat().st_size,
                    "pages": pages,
                    "first_page_text_chars": first_chars,
                    "pdf_magic": magic,
                    "sha256": sha256(target),
                    "attempts": [],
                }
            )
            return base
        except Exception:
            target.unlink(missing_ok=True)

    attempts: list[dict[str, Any]] = []
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "application/pdf,*/*;q=0.8"})
    for url in discover_page_pdf_links(item, session, timeout):
        if url not in base["candidate_urls"]:
            base["candidate_urls"].append(url)
    for url in base["candidate_urls"]:
        attempt: dict[str, Any] = {"url": url}
        temporary = target.with_suffix(".partial")
        temporary.unlink(missing_ok=True)
        try:
            response = session.get(url, stream=True, allow_redirects=True, timeout=timeout)
            attempt["http_status"] = response.status_code
            attempt["content_type"] = response.headers.get("content-type", "")
            response.raise_for_status()
            with temporary.open("wb") as handle:
                for chunk in response.iter_content(chunk_size=1024 * 256):
                    if chunk:
                        handle.write(chunk)
            pages, first_chars, magic = validate_pdf(temporary)
            os.replace(temporary, target)
            attempt["result"] = "valid_pdf"
            attempts.append(attempt)
            base.update(
                {
                    "status": "downloaded",
                    "url": url,
                    "resolved_url": response.url,
                    "http_status": response.status_code,
                    "content_type": response.headers.get("content-type", ""),
                    "bytes": target.stat().st_size,
                    "pages": pages,
                    "first_page_text_chars": first_chars,
                    "pdf_magic": magic,
                    "sha256": sha256(target),
                    "attempts": attempts,
                }
            )
            return base
        except Exception as exc:  # noqa: BLE001 - preserve per-source audit
            attempt["result"] = "failed"
            attempt["error"] = f"{type(exc).__name__}: {exc}"
            attempts.append(attempt)
            temporary.unlink(missing_ok=True)
        finally:
            try:
                response.close()
            except UnboundLocalError:
                pass
    base.update(
        {
            "status": "failed",
            "url": None,
            "http_status": None,
            "content_type": None,
            "bytes": 0,
            "pages": 0,
            "first_page_text_chars": 0,
            "pdf_magic": None,
            "sha256": None,
            "attempts": attempts,
            "error": "all candidate URLs failed PDF validation",
        }
    )
    return base


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--tiers",
        default="REFERENCE,ARCHIVE",
        help="comma-separated tiers to download (default: REFERENCE,ARCHIVE)",
    )
    parser.add_argument(
        "--paper-ids",
        default="",
        help="optional comma-separated paper IDs to restrict the selected tiers",
    )
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--connect-timeout", type=float, default=20.0)
    parser.add_argument("--read-timeout", type=float, default=180.0)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    output_dir = args.output_dir if args.output_dir.is_absolute() else ROOT / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    selected_tiers = {
        value.strip().upper()
        for value in args.tiers.split(",")
        if value.strip()
    }
    invalid_tiers = selected_tiers - {"CORE", "NEXT", "REFERENCE", "ARCHIVE"}
    if not selected_tiers or invalid_tiers:
        parser.error(f"invalid --tiers value: {sorted(invalid_tiers) or args.tiers}")
    paper_ids = {value.strip() for value in args.paper_ids.split(",") if value.strip()}
    items = read_selected(selected_tiers, paper_ids or None)
    records: list[dict[str, Any]] = []
    started = time.monotonic()
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {
            executor.submit(
                download_one,
                item,
                output_dir,
                timeout=(args.connect_timeout, args.read_timeout),
                force=args.force,
            ): item["paper_id"]
            for item in items
        }
        for index, future in enumerate(as_completed(futures), start=1):
            record = future.result()
            records.append(record)
            print(
                f"[{index}/{len(items)}] {record['paper_id']} "
                f"{record['status']} pages={record.get('pages', 0)} "
                f"bytes={record.get('bytes', 0)}",
                flush=True,
            )

    records.sort(key=lambda record: record["paper_id"])
    log_path = output_dir / "download_manifest.jsonl"
    # Targeted retries should not erase the audit rows for the rest of the
    # selected tier.  Merge the new rows with an existing task manifest when
    # present; the selected IDs always win.
    merged_records: dict[str, dict[str, Any]] = {}
    if log_path.exists():
        try:
            for line in log_path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    record = json.loads(line)
                    if record.get("paper_id"):
                        merged_records[record["paper_id"]] = record
        except (OSError, json.JSONDecodeError):
            merged_records = {}
    merged_records.update({record["paper_id"]: record for record in records})
    records = [merged_records[key] for key in sorted(merged_records)]
    with log_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    counts: dict[str, int] = {}
    for record in records:
        counts[record["status"]] = counts.get(record["status"], 0) + 1
    elapsed = round(time.monotonic() - started, 1)
    print({"selected": len(items), "counts": counts, "elapsed_seconds": elapsed, "manifest": str(log_path)})
    return 0 if counts.get("failed", 0) == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
