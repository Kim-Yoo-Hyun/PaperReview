#!/usr/bin/env python3
"""Rewrite selected standard notes for a targeted full-text pass.

The companion downloader keeps the PDFs in a task-scoped temporary directory.
This reviewer extracts the body with the existing page-aware evidence parser,
then renders 01_overview through 05_insights with explicit provenance.  It
does not change tier membership, reading status, or tracker evidence.

Run without ``--apply`` for a complete dry run.  The PDF cache is intentionally
left in place until the caller has validated the generated notes and manifest.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import unquote

import requests

from review_fulltext_notes import (
    Evidence,
    anchor,
    body_evidence_label,
    body_terms,
    combined_evidence,
    cue_lines,
    evaluation_note,
    evaluation_type,
    extract_document,
    get_formulation,
    get_runtime,
    get_scope,
    heading_list,
    infer_domain,
    infer_evidence,
    load_download_manifest,
    md_table,
    method_note,
    note_header,
    problem_note,
    resolve_folder,
    short_cue,
    title_token_overlap,
)


ROOT = Path(__file__).resolve().parents[2]
PAPERS = ROOT / "work" / "sources" / "papers.json"
TIERS = ROOT / "research" / "READING_TIERS.csv"
DEFAULT_PDF_DIR = ROOT / "tmp" / "pdfs" / "fulltext_core_next_2026-09-02"
DEFAULT_REVIEW_MANIFEST = ROOT / "work" / "sources" / "fulltext_core_next_review_manifest.json"
BT = chr(96)

# Two current CORE/NEXT entries do not expose a downloadable PDF through the
# official source at review time.  They are kept in scope with an explicit
# source boundary rather than being silently filled from a summary or a
# guessed method.  The ICML page contains the accepted paper abstract; the
# NVIDIA page is the authors' technical report/model page and contains the
# model/data/training/evaluation discussion.
SOURCE_EXCEPTIONS: dict[str, dict[str, str]] = {
    "pr-0813": {
        "url": "https://icml.cc/virtual/2026/poster/64203",
        "source_kind": "official ICML proceedings page (abstract only; public PDF unavailable)",
        "evidence_level": "ABSTRACT_CHECKED",
    },
    "pr-0918": {
        "url": "https://research.nvidia.com/labs/gear/gr00t-n1_6/",
        "source_kind": "official NVIDIA technical page body (no public PDF identified)",
        "evidence_level": "FULL_TEXT_CHECKED",
    },
    "pr-0917": {
        "url": "https://research.nvidia.com/labs/gear/gr00t-n1_5/",
        "source_kind": "official NVIDIA technical page body (no public PDF identified)",
        "evidence_level": "FULL_TEXT_CHECKED",
    },
}


class SourceBlockParser(HTMLParser):
    """Extract readable headings/paragraphs/list items without browser chrome."""

    BLOCK_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "dt", "dd"}
    SKIP_TAGS = {"script", "style", "svg", "noscript", "nav", "footer", "header", "form"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.skip_depth = 0
        self.active_tag: str | None = None
        self.active_text: list[str] = []
        self.blocks: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.casefold()
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth or tag not in self.BLOCK_TAGS:
            return
        self.flush()
        self.active_tag = tag
        self.active_text = []

    def handle_endtag(self, tag: str) -> None:
        tag = tag.casefold()
        if tag in self.SKIP_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        if self.active_tag == tag:
            self.flush()

    def handle_data(self, data: str) -> None:
        if self.skip_depth == 0 and self.active_tag:
            self.active_text.append(data)

    def flush(self) -> None:
        if self.active_tag and self.active_text:
            text = re.sub(r"\s+", " ", " ".join(self.active_text)).strip()
            if text:
                self.blocks.append((self.active_tag, text))
        self.active_tag = None
        self.active_text = []


def extract_source_document(url: str, title: str, source_kind: str) -> dict[str, Any]:
    response = requests.get(url, timeout=45, headers={"User-Agent": "PaperReview-source-audit/2026"})
    response.raise_for_status()
    parser = SourceBlockParser()
    parser.feed(response.text)
    parser.close()
    blocks = [(tag, text) for tag, text in parser.blocks if len(text) >= 20]
    headings: list[tuple[int, str]] = []
    page_lines: list[str] = []
    sentences: list[Evidence] = []
    current_section = source_kind
    for tag, text in blocks:
        if tag.startswith("h"):
            current_section = text
            headings.append((1, text))
            page_lines.append(text)
            continue
        page_lines.append(text)
        # Importing the existing sentence splitter keeps HTML fallback cues
        # subject to the same minimum-length/noise rule as PDF cues.
        from review_fulltext_notes import looks_like_noise, sentence_list

        for sentence in sentence_list(text):
            if not looks_like_noise(sentence):
                sentences.append(Evidence(1, current_section, sentence, parent=source_kind))
    raw = "\n\n".join(page_lines)
    page_rows = [{"page": 1, "raw": raw, "text": re.sub(r"\s+", " ", raw).strip(), "section": current_section}]
    return {
        "pages": 1,
        "page_rows": page_rows,
        "headings": headings,
        "section_parents": {heading: source_kind for _, heading in headings},
        "sentences": sentences,
        "text_chars": len(page_rows[0]["text"]),
        "extraction_method": source_kind,
        "extraction_quality": "high" if len(page_rows[0]["text"]) >= 6000 else "medium" if len(page_rows[0]["text"]) >= 1500 else "low",
        "reference_start_page": None,
    }


def load_items() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, str]], list[dict[str, str]]]:
    papers = {item["paper_id"]: item for item in json.loads(PAPERS.read_text(encoding="utf-8"))}
    with TIERS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    tiers = {row["paper_id"]: row for row in rows}
    return papers, tiers, rows


def source_url(item: dict[str, Any]) -> str:
    sources = item.get("sources") or {}
    primary = sources.get("primary") or {}
    value = primary.get("url") if isinstance(primary, dict) else None
    return str(value or item.get("page") or item.get("pdf") or "source URL not recorded")


def project_url(item: dict[str, Any]) -> str:
    for value in (
        item.get("project"),
        (item.get("sources") or {}).get("project", {}).get("url")
        if isinstance((item.get("sources") or {}).get("project"), dict)
        else None,
        (item.get("sources") or {}).get("code", {}).get("url")
        if isinstance((item.get("sources") or {}).get("code"), dict)
        else None,
    ):
        if isinstance(value, str) and value.startswith(("http://", "https://")):
            return value
    return "not identified"


def tag_text(item: dict[str, Any], row: dict[str, str]) -> str:
    raw = item.get("tags") or row.get("tags") or []
    if isinstance(raw, str):
        return raw
    return ", ".join(str(value) for value in raw[:7]) or "paper-specific tags not recorded"


def retrieval_source(record: dict[str, Any], item: dict[str, Any]) -> tuple[str, str]:
    retrieved = record.get("url") or record.get("resolved_url") or item.get("pdf") or source_url(item)
    if "chatpaper.com/api/v1/articles/download" in str(retrieved):
        return (
            "public full-text mirror used for retrieval (canonical paper source retained)",
            str(retrieved),
        )
    if "icdst.org" in str(retrieved):
        return (
            "public full-text transcription mirror used for retrieval (canonical paper source retained)",
            str(retrieved),
        )
    if str(record.get("source_kind") or "PDF") == "PDF":
        return "PDF retrieval source", str(retrieved)
    return "body source", str(retrieved)


def body_header(item: dict[str, Any], row: dict[str, str], record: dict[str, Any], *, pointer: bool = False) -> str:
    label, retrieved = retrieval_source(record, item)
    prefix = "> Canonical metadata: [01_overview.md](./01_overview.md).\n" if pointer else ""
    source_kind = str(record.get("source_kind") or "PDF")
    evidence_level = str(record.get("evidence_level") or "FULL_TEXT_CHECKED")
    evidence_label = body_evidence_label(record)
    if source_kind == "PDF":
        basis = (
            f"full-text PDF body checked on {date.today().isoformat()} "
            f"({record['pages']} pages; {record['extraction_method']}; extraction quality: {record['extraction_quality']})"
        )
        anchor_note = "exact tables/equations remain at the cited page anchors"
    else:
        basis = (
            f"{source_kind} checked on {date.today().isoformat()} "
            f"({record['pages']} source page(s); {record['extraction_method']}; extraction quality: {record['extraction_quality']})"
        )
        anchor_note = "exact tables/equations or section details remain at the cited source anchors"
    if evidence_level == "ABSTRACT_CHECKED":
        boundary_note = "Evidence boundary: abstract/source-page only; method details, exact metrics, limitations and failure cases require full-text review."
    elif source_kind == "PDF":
        boundary_note = f"Evidence boundary: selected {evidence_label} sentences, captions and section anchors were used; exact table/equation values remain at those anchors."
    else:
        boundary_note = f"Evidence boundary: selected {evidence_label} statements and source anchors were used; no PDF was identified at review time."
    origin_note = (
        f" PDF provenance note: {record['pdf_origin']}."
        if record.get("pdf_origin")
        else ""
    )
    return (
        prefix
        + f"> Evidence maturity: {BT}{evidence_level}{BT}.\n"
        + f"> Analysis basis: {basis}; "
        + f"canonical paper source: {source_url(item)}; {label}: {retrieved}.{origin_note} "
        + f"The note is an evidence-anchored {evidence_label} analysis; {anchor_note}. "
        + f"{boundary_note} "
        + "Reading tracker status remains user-controlled; registry source evidence is reconciled separately.\n\n"
    )


def first(values: list[Evidence], fallback: str) -> str:
    return short_cue(values[0].text, 32) if values else fallback


def section_digest(ev: dict[str, list[Evidence]]) -> str:
    return cue_lines(
        combined_evidence(
            ev["abstract"],
            ev["problem"],
            ev["changes"],
            ev["method"],
            ev["results"],
            ev["failure"],
            limit=14,
        ),
        "selected body cue 없음",
        12,
    )


def overview_note(
    item: dict[str, Any],
    row: dict[str, str],
    record: dict[str, Any],
    ev: dict[str, list[Evidence]],
    document: dict[str, Any],
    domain: str,
) -> str:
    track = row.get("primary_track") or item.get("primary_track") or item.get("category", "unclassified")
    tags = tag_text(item, row)
    scope = get_scope(domain)
    problem = ev["problem"] or ev["abstract"][:2]
    changes = ev["changes"] or ev["method"][:2]
    method = ev["method"] or changes
    interface = ev["interface"]
    results = ev["results"] or ev["numeric"]
    failures = ev["failure"] or ev["conclusion"][:3]
    dataset = ev["dataset"]
    metrics = ev["metrics"]
    code = project_url(item)
    paper_type = item.get("paper_type") or "not recorded"
    eval_type = evaluation_type(item, domain, ev)
    observation = first(interface[:1], scope[1])
    state = ", ".join(body_terms(interface + ev["method"], 12)) or scope[2]
    action = first(interface[1:3], scope[3])
    source_kind = str(record.get("source_kind") or "PDF")
    evidence_level = str(record.get("evidence_level") or "FULL_TEXT_CHECKED")
    evidence_label = body_evidence_label(record)
    if source_kind == "PDF":
        source_audit = (
            f"full-text PDF body checked on {date.today().isoformat()} "
            f"({document['pages']} pages; {document['extraction_method']}; "
            f"title-token overlap first two pages={record['title_token_overlap_first_two_pages']})"
        )
    else:
        source_audit = (
            f"{source_kind} checked on {date.today().isoformat()} "
            f"({document['pages']} source page(s); {document['extraction_method']})"
        )
    if evidence_level == "ABSTRACT_CHECKED":
        boundary_note = "abstract/source-page only; method details, exact metrics, limitations and failure cases require full-text review"
    elif source_kind == "PDF":
        boundary_note = "selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors"
    else:
        boundary_note = "selected official source-body statements; no PDF was identified at review time"
    origin_note = (
        f" PDF provenance note: {record['pdf_origin']}."
        if record.get("pdf_origin")
        else ""
    )
    why = (
        f"{track}의 {domain} 문제를 이해하기 위해 읽는다. 본문은 "
        f"{first(problem, 'paper-specific bottleneck not recovered')}를 문제로 두고, "
        f"{first(changes, 'paper-specific contribution not recovered')}를 통해 "
        "observation-to-action closed loop의 한 지점을 바꾼다."
    )
    return (
        f"# {item['title']}\n\n"
        f"> Evidence maturity: {BT}{evidence_level}{BT}.\n"
        f"> Analysis basis: {source_audit}; canonical paper source: {source_url(item)}.{origin_note}\n"
        f"> {'PDF retrieval source' if source_kind == 'PDF' else 'Body source'}: {retrieval_source(record, item)[1]}. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.\n\n"
        f"> Evidence boundary: {boundary_note}.\n\n"
        f"- Year/Venue: {item.get('year', row.get('year', 'not recorded'))} / {item.get('venue', row.get('venue', 'not recorded'))}\n"
        f"- Authors: not duplicated here when not verified in the registry source\n"
        f"- Primary track: {track}\n"
        f"- Tier: {row.get('tier', 'not recorded')}\n"
        f"- Tags: {tags}\n"
        f"- Official paper: {source_url(item)}\n"
        f"- Full-text retrieval: {retrieval_source(record, item)[1]}\n"
        f"- Code/Project: {code}\n"
        f"- Paper type: {paper_type}\n"
        f"- Source audit: {source_audit}\n\n"
        "## Why This Paper Is Here\n\n"
        f"{why}\n\n"
        "## Problem and Motivation\n\n"
        f"{cue_lines(combined_evidence(ev['abstract'], ev['problem'], limit=7), 'problem/motivation body cue 없음', 7)}\n\n"
        "## Core Idea\n\n"
        f"{cue_lines(combined_evidence(ev['changes'], ev['method'], limit=9), 'method/contribution body cue 없음', 8)}\n\n"
        "## Observation, State, and Output Interface\n\n"
        + md_table(
            ["Role", f"{evidence_label} evidence", "Robotics interpretation", "Anchor"],
            [
                ["Observation/input", observation, scope[1], anchor(interface[:2])],
                ["State/latent", state, scope[2], anchor((interface + ev["method"])[:3])],
                ["Output/action", action, scope[3], anchor(interface[1:4])],
                ["Objective/outcome", first(ev["objective"], scope[4]), scope[4], anchor(ev["objective"][:3])],
            ],
        )
        + "\n\n## Main Claims and Actual Contribution\n\n"
        + cue_lines(combined_evidence(ev["changes"], ev["results"], limit=10), "claim/result body cue 없음", 8)
        + "\n\n- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.\n\n"
        + "## Evaluation Scope\n\n"
        + md_table(
            ["Dimension", "Body-grounded record", "Boundary", "Anchor"],
            [
                ["Evaluation type", eval_type, "do not infer unreported downstream behavior", anchor(ev["results"][:2] or ev["dataset"][:2])],
                ["Embodiment/environment", first(dataset[:2], "not recovered"), "hardware/simulator version and reset protocol", anchor(dataset[:2])],
                ["Dataset/benchmark", first(dataset[2:4] or dataset, "not recovered"), "role, split, size and leakage", anchor(dataset[:4])],
                ["Metric", first(metrics, "not recovered"), "definition, denominator, direction and uncertainty", anchor(metrics[:3])],
                ["Baseline/ablation", first(ev["baseline"] + ev["ablation"], "not recovered"), "fair input/data/compute/action matching", anchor((ev["baseline"] + ev["ablation"])[:3])],
            ],
        )
        + "\n\n## Explicit Limitations and Failure Boundary\n\n"
        + cue_lines(failures, "explicit limitation/failure cue not recovered from the body", 7)
        + "\n\n## Why Read It\n\n"
        + f"{why} Revisit {anchor(combined_evidence(ev['problem'], ev['method'], ev['results'], limit=6))} to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.\n"
    )


def clean_old_lineage(text: str) -> list[str]:
    """Keep only short, non-boilerplate lineage statements from the old note."""
    values: list[str] = []
    in_section = False
    for line in text.splitlines():
        if line.startswith("## "):
            in_section = line.casefold() in {"## dependency and evolution", "## dependency position", "## reading dependency and lineage"}
            continue
        if not in_section:
            continue
        value = re.sub(r"^\s*[-*]\s*", "", line).strip()
        if not value or value.startswith(">") or len(value) > 260:
            continue
        if "not recorded" in value.casefold() or "confirm it" in value.casefold():
            continue
        if value not in values:
            values.append(value)
    return values[:4]


def neighbors(item_id: str, row: dict[str, str], rows: list[dict[str, str]]) -> tuple[str, str]:
    same = [r for r in rows if r.get("primary_track") == row.get("primary_track") and r.get("tier") in {"CORE", "NEXT"}]
    index = next((i for i, value in enumerate(same) if value.get("paper_id") == item_id), None)
    if index is None:
        return "not recorded", "not recorded"
    previous = same[index - 1]["title"] if index > 0 else "start of this track queue"
    following = same[index + 1]["title"] if index + 1 < len(same) else "end of this track queue"
    return previous, following


def question_text(
    item: dict[str, Any],
    row: dict[str, str],
    ev: dict[str, list[Evidence]],
) -> str:
    method_terms = body_terms(ev["changes"] + ev["method"], 5)
    mechanism = ", ".join(method_terms[:3]) or "the paper-specific mechanism"
    metric = short_cue(ev["metrics"][0].text, 18) if ev["metrics"] else "the primary body-reported metric"
    baseline = short_cue(ev["baseline"][0].text, 16) if ev["baseline"] else "a matched simpler baseline"
    failure = short_cue(ev["failure"][0].text, 16) if ev["failure"] else "the paper's strongest untested assumption"
    return (
        f"고정된 observation/action/data/compute budget에서 {mechanism} mechanism이 "
        f"{baseline} 대비 {metric}을 개선하고, {failure} 조건에서도 closed-loop failure를 늘리지 않는가?"
    )


def insights_note(
    item: dict[str, Any],
    row: dict[str, str],
    record: dict[str, Any],
    ev: dict[str, list[Evidence]],
    document: dict[str, Any],
    domain: str,
    old_insights: str,
    rows: list[dict[str, str]],
) -> str:
    track = row.get("primary_track") or item.get("primary_track") or item.get("category", "unclassified")
    scope = get_scope(domain)
    evidence_label = body_evidence_label(record)
    previous, following = neighbors(item["paper_id"], row, rows)
    problem = ev["problem"] or ev["abstract"][:2]
    new = combined_evidence(ev["changes"], ev["method"], limit=7)
    failures = ev["failure"] or ev["conclusion"][:4]
    results = ev["results"] or ev["numeric"]
    interface = ev["interface"]
    old_lineage = clean_old_lineage(old_insights)
    body_mechanism = first(new, "paper-specific mechanism not recovered")
    body_outcome = first(results, "paper-specific outcome not recovered")
    body_failure = first(failures, "explicit failure boundary not recovered")
    research_lesson = (
        f"이 논문의 재사용 가능한 지점은 {first(interface[:2], scope[1])}를 "
        f"{first(interface[1:3], scope[3])}로 변환하는 body-defined interface를 분리해 보는 것이다. "
        f"따라서 {scope[2]}가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 {body_failure}에서 "
        "feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다."
    )
    return (
        f"# Insights — {item['title']}\n\n"
        + body_header(item, row, record, pointer=True)
        + "## Paper-supported conclusion\n\n"
        + f"> **Evidence boundary:** The following claims are restricted to selected {evidence_label} sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.\n\n"
        + "### What was actually new\n\n"
        + cue_lines(new or ev["abstract"], "body contribution cue 없음", 7)
        + f"\n- **Contribution anchor:** {anchor(new, '본문 contribution anchor 없음')}\n\n"
        + "### Strongest assumption and failure boundary\n\n"
        + cue_lines(combined_evidence(problem, failures, limit=8), "explicit assumption/failure cue not recovered", 7)
        + f"\n- **Boundary to test:** {body_failure}\n\n"
        + "### Claim–evidence link\n\n"
        + md_table(
            ["Claim target", "Body evidence", "Anchor"],
            [
                ["Mechanism/contribution", body_mechanism, anchor(new[:2])],
                ["Reported outcome", body_outcome, anchor(results[:2])],
                ["Failure/limitation", body_failure, anchor(failures[:2])],
            ],
        )
        + "\n\n## Researcher interpretation\n\n"
        + "### Reusable lesson in the robotics loop\n\n"
        + f"- **Closed-loop position:** `{scope[1]} → {scope[2]} → {scope[3]}`.\n"
        + f"- {research_lesson}\n"
        + f"- The paper-specific mechanism to preserve in a reproduction is: {body_mechanism}\n"
        + "- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.\n\n"
        + "### Dependency and evolution\n\n"
        + f"- **Registry position:** `{row.get('tier', 'not recorded')}` in `{track}`; tags: `{tag_text(item, row)}`.\n"
        + f"- **Reading predecessor in the generated track queue:** {previous} (queue adjacency, not a confirmed citation).\n"
        + f"- **Reading successor in the generated track queue:** {following} (queue adjacency, not a confirmed citation).\n"
        + (f"- **Legacy lineage cue retained for manual reference audit:** {'; '.join(old_lineage)}\n" if old_lineage else "- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.\n")
        + f"- **Body-defined next pressure:** {body_failure}; this is the most direct route from the paper's reported scope to a falsifiable extension.\n\n"
        + "### Minimal reproduction\n\n"
        + "1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.\n"
        + f"2. Use the paper-reported resource/task cue: {first(ev['dataset'], 'dataset/benchmark role not recovered')}.\n"
        + f"3. Compare against the body-reported baseline or a matched simpler baseline: {first(ev['baseline'], 'baseline not recovered')}.\n"
        + f"4. Report the body metric and its denominator/aggregation: {first(ev['metrics'], 'metric definition not recovered')}.\n"
        + f"5. Re-run the body-reported ablation/failure condition: {first(ev['ablation'] + ev['failure'], 'ablation/failure condition not recovered')}.\n"
        + "6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.\n\n"
        + "### What would count as a successful reproduction\n\n"
        + f"- The reported mechanism is present at {anchor(ev['method'][:3], 'method anchor 없음')}; the primary result is directionally consistent at {anchor(results[:3], 'result anchor 없음')}; and the failure boundary is measured rather than omitted.\n\n"
        + "## Falsifiable research question\n\n"
        + question_text(item, row, ev)
        + "\n\n**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-dir", type=Path, default=DEFAULT_PDF_DIR)
    parser.add_argument("--download-manifest", type=Path, default=None)
    parser.add_argument("--review-manifest", type=Path, default=DEFAULT_REVIEW_MANIFEST)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--paper-ids", default="", help="comma-separated paper IDs for a targeted refresh")
    parser.add_argument(
        "--tiers",
        default="CORE,NEXT",
        help="comma-separated tiers eligible for this pass (default: CORE,NEXT)",
    )
    parser.add_argument(
        "--notes",
        default="01_overview.md,02_problem.md,03_method.md,04_evaluation.md,05_insights.md",
        help="comma-separated standard note files to write",
    )
    parser.add_argument(
        "--replace-manifest",
        action="store_true",
        help="replace a targeted review manifest instead of merging selected records into it",
    )
    args = parser.parse_args()

    pdf_dir = args.pdf_dir if args.pdf_dir.is_absolute() else ROOT / args.pdf_dir
    download_path = args.download_manifest or (pdf_dir / "download_manifest.jsonl")
    if not download_path.is_absolute():
        download_path = ROOT / download_path
    review_path = args.review_manifest if args.review_manifest.is_absolute() else ROOT / args.review_manifest
    papers, tiers, rows = load_items()
    selected_tiers = {value.strip().upper() for value in args.tiers.split(",") if value.strip()}
    invalid_tiers = selected_tiers - {"CORE", "NEXT", "REFERENCE", "ARCHIVE"}
    if not selected_tiers or invalid_tiers:
        parser.error(f"invalid --tiers value: {sorted(invalid_tiers) or args.tiers}")
    standard_notes = {
        "01_overview.md",
        "02_problem.md",
        "03_method.md",
        "04_evaluation.md",
        "05_insights.md",
    }
    selected_notes = {value.strip() for value in args.notes.split(",") if value.strip()}
    invalid_notes = selected_notes - standard_notes
    if not selected_notes or invalid_notes:
        parser.error(f"invalid --notes value: {sorted(invalid_notes) or args.notes}")
    all_selected = [
        papers[paper_id]
        for paper_id, row in sorted(tiers.items())
        if row.get("tier") in selected_tiers
    ]
    requested_ids = {value.strip() for value in args.paper_ids.split(",") if value.strip()}
    selected = [item for item in all_selected if item["paper_id"] in requested_ids] if requested_ids else all_selected
    if args.start:
        selected = selected[args.start:]
    if args.limit:
        selected = selected[:args.limit]
    # An exceptions-only refresh can run after the task PDF cache has been
    # removed; ordinary PDF selections still fail through the missing check
    # below when no download manifest is available.
    downloads = load_download_manifest(download_path) if download_path.exists() else {}
    missing = [
        item["paper_id"]
        for item in selected
        if item["paper_id"] not in SOURCE_EXCEPTIONS
        and (downloads.get(item["paper_id"], {}).get("status") not in {"downloaded", "reused"}
        or not (pdf_dir / f"{item['paper_id']}.pdf").exists()
        )
    ]
    if missing:
        print({"mode": "apply" if args.apply else "dry-run", "missing_fulltext": len(missing), "sample": missing[:20]})
        return 2

    outputs: list[tuple[Path, str]] = []
    review_records: list[dict[str, Any]] = []
    domains: Counter[str] = Counter()
    qualities: Counter[str] = Counter()
    for index, item in enumerate(selected, start=1):
        row = tiers[item["paper_id"]]
        pdf_path = pdf_dir / f"{item['paper_id']}.pdf"
        record = dict(downloads.get(item["paper_id"], {}))
        record.setdefault("paper_id", item["paper_id"])
        record.setdefault("title", item["title"])
        record.setdefault("folder", item.get("folder", ""))
        record.setdefault("target", str((pdf_dir / f"{item['paper_id']}.pdf").relative_to(ROOT)))
        exception = SOURCE_EXCEPTIONS.get(item["paper_id"])
        if pdf_path.exists() and record.get("status") in {"downloaded", "reused"}:
            document = extract_document(pdf_path)
            record.setdefault("source_kind", "PDF")
            record.setdefault("evidence_level", "FULL_TEXT_CHECKED")
        elif exception:
            document = extract_source_document(exception["url"], item["title"], exception["source_kind"])
            record.update(
                {
                    "status": "source_exception",
                    "url": exception["url"],
                    "source_kind": exception["source_kind"],
                    "evidence_level": exception["evidence_level"],
                    "source_boundary": "official source was checked; no downloadable public PDF was available at review time",
                }
            )
        else:
            raise SystemExit(f"full-text source is missing for {item['paper_id']}")
        document["paper_title"] = item["title"]
        ev = infer_evidence(document)
        domain = infer_domain(item, row)
        domains[domain] += 1
        qualities[document["extraction_quality"]] += 1
        record.update(
            {
                "tier": row["tier"],
                "track": row.get("primary_track", ""),
                "domain": domain,
                "pages": document["pages"],
                "text_chars": document["text_chars"],
                "extraction_method": document["extraction_method"],
                "extraction_quality": document["extraction_quality"],
                "title_token_overlap_first_two_pages": title_token_overlap(item["title"], document),
                "section_heading_count": len(document["headings"]),
                "evidence_counts": {key: len(value) for key, value in ev.items()},
                "note_basis": (
                    "full-text PDF body with page-aware extractive cues"
                    if record.get("source_kind", "PDF") == "PDF"
                    else f"{record.get('source_kind')} with source-aware extractive cues"
                ),
                "reviewed_on": date.today().isoformat(),
            }
        )
        review_records.append(record)
        folder = resolve_folder(unquote(item["folder"]))
        old_insights = (folder / "05_insights.md").read_text(encoding="utf-8")
        note_outputs = {
            "01_overview.md": overview_note(item, row, record, ev, document, domain),
            "02_problem.md": problem_note(item, domain, record, ev, document),
            "03_method.md": method_note(item, domain, record, ev, document),
            "04_evaluation.md": evaluation_note(item, domain, record, ev, document),
            "05_insights.md": insights_note(item, row, record, ev, document, domain, old_insights, rows),
        }
        outputs.extend((folder / name, note_outputs[name]) for name in sorted(selected_notes))
        record["note_files_written"] = len(selected_notes)
        if index % 25 == 0 or index == len(selected):
            print(f"[{index}/{len(selected)}] extracted and rendered; tier={row['tier']} domain={domain}", flush=True)

    print(
        {
            "mode": "apply" if args.apply else "dry-run",
            "selected": len(selected),
            "note_file_updates": len(outputs),
            "domain_counts": dict(domains),
            "extraction_quality": dict(qualities),
        }
    )
    if not args.apply:
        return 0

    for path, content in outputs:
        path.write_text(content.rstrip() + "\n", encoding="utf-8")
    review_path.parent.mkdir(parents=True, exist_ok=True)
    records_for_manifest = review_records
    if (args.start or args.limit or requested_ids) and review_path.exists() and not args.replace_manifest:
        existing = json.loads(review_path.read_text(encoding="utf-8"))
        merged = {
            record["paper_id"]: record
            for record in existing.get("records", [])
            if record.get("paper_id")
        }
        merged.update({record["paper_id"]: record for record in review_records})
        records_for_manifest = [merged[key] for key in sorted(merged)]
    if selected_tiers <= {"CORE", "NEXT"}:
        manifest_scope = "CORE/NEXT papers selected from READING_TIERS.csv"
    else:
        manifest_scope = (
            "Targeted full-text PDF review; selected tiers: "
            + ",".join(sorted(selected_tiers))
        )
    review_payload = {
        "review_date": date.today().isoformat(),
        "scope": manifest_scope,
        "paper_count": len(records_for_manifest),
        "note_file_count": sum(record.get("note_files_written", 5) for record in records_for_manifest),
        "pdf_cache": str(pdf_dir.relative_to(ROOT)),
        "tracker_changed": False,
        "tier_snapshot": dict(Counter(record["tier"] for record in records_for_manifest)),
        "source_kind_counts": dict(Counter(record.get("source_kind", "PDF") for record in records_for_manifest)),
        "source_exceptions": [
            record["paper_id"] for record in records_for_manifest if record.get("status") == "source_exception"
        ],
        "records": records_for_manifest,
    }
    review_path.write_text(json.dumps(review_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
