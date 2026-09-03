#!/usr/bin/env python3
"""Run a conservative semantic QA pass over the CORE/NEXT paper notes.

The existing full-text renderer intentionally favors recall: it keeps useful
body cues even when section recovery or a paper-specific field is uncertain.
That is appropriate for a first registry-wide pass, but it can leave a note
with a generic fallback or with an evaluation sentence selected as a failure
cue.  This script performs a second, section-aware pass over the same
validated PDFs.  It appends a compact paper-specific QA block to all five
standard notes, rewrites only the generic fallback phrases, and replaces the
generic researcher-interpretation sections in ``05_insights.md`` with cues
selected from contribution, method, results, and explicit limitation text.

It never changes tiers, reading status, tracker fields, or registry metadata.
The first sweep deliberately skips OCR; low-confidence PDFs are recorded for
manual/OCR follow-up instead of being silently treated as reliable evidence.
Run without ``--apply`` for a report-only dry run.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path
from typing import Any, Iterable

from review_fulltext_notes import (
    Evidence,
    anchor,
    body_terms,
    extract_document,
    infer_evidence,
    load_download_manifest,
    resolve_folder,
    short_cue,
    similar,
    title_token_overlap,
)
from audit_note_artifacts import clean_line as clean_extractive_line


ROOT = Path(__file__).resolve().parents[2]
PAPERS = ROOT / "work" / "sources" / "papers.json"
TIERS = ROOT / "research" / "READING_TIERS.csv"
DEFAULT_PDF_DIR = ROOT / "tmp" / "pdfs" / "core_next_semantic_qa_2026-09-03"
DEFAULT_DOWNLOAD_MANIFEST = DEFAULT_PDF_DIR / "download_manifest.jsonl"
DEFAULT_REPORT = ROOT / "work" / "sources" / "core_next_semantic_qa_2026-09-03.json"

NOTE_NAMES = ("01_overview.md", "02_problem.md", "03_method.md", "04_evaluation.md", "05_insights.md")
BT = chr(96)

GENERIC_REPLACEMENTS = {
    "paper-specific bottleneck not recovered": "PDF body did not state a recoverable bottleneck; no claim inferred",
    "paper-specific contribution not recovered": "PDF body did not state a recoverable contribution; no claim inferred",
    "paper-specific mechanism not recovered": "PDF body did not yield a recoverable mechanism statement; no claim inferred",
    "paper-specific outcome not recovered": "PDF body did not yield a recoverable outcome statement; no claim inferred",
    "explicit failure boundary not recovered": "PDF body did not yield an explicit failure/limitation statement; no failure inferred",
    "paper-specific objective not recovered": "PDF body did not yield a recoverable objective statement; no claim inferred",
    "paper-specific state terms not recovered": "PDF body did not yield recoverable state terms; no state claim inferred",
    "paper-specific terms not recovered": "PDF body did not yield recoverable interface terms; no interface claim inferred",
    "paper-specific horizon - see PDF temporal cues": "PDF body temporal cue was not selected; timing remains unresolved",
    "paper-specific rate - see PDF temporal cues": "PDF body control-rate cue was not selected; rate remains unresolved",
    "paper-specific history/memory - see PDF temporal cues": "PDF body memory cue was not selected; history remains unresolved",
    "paper-specific compute/latency - see PDF reproduction cues": "PDF body compute/latency cue was not selected; runtime remains unresolved",
    "paper-specific training setup - see PDF method cues": "PDF body training cue was not selected; training setup remains unresolved",
    "paper-specific inference setup - see PDF method cues": "PDF body inference cue was not selected; inference setup remains unresolved",
}

NEGATIVE_TERMS = (
    "failure", "fail", "fails", "failed", "limitation", "future work", "cannot", "unable",
    "does not", "do not", "did not", "struggle", "degrad", "unstable", "out-of-distribution",
    "out of distribution", "occlusion", "noise", "collision", "slip", "fall", "remain",
    "sensitive", "sensitivity", "brittle", "poorly", "worse", "incorrect", "unsafe",
)
HARD_NEGATIVE_TERMS = (
    "failure", "fail", "fails", "failed", "limitation", "cannot", "unable", "does not",
    "do not", "did not", "struggle", "degrad", "unstable", "out-of-distribution",
    "out of distribution", "occlusion", "noise", "collision", "slip", "fall", "sensitive",
    "sensitivity", "brittle", "poorly", "worse", "incorrect", "unsafe", "lack", "limited",
    "limit", "inaccurate",
)
CONTRIBUTION_TERMS = (
    "we propose", "we introduce", "we present", "our method", "our approach", "our framework",
    "key contribution", "main contribution", "contributions", "novel", "designed to", "enables",
    "consists of", "is composed", "we develop", "we show",
)
METHOD_TERMS = (
    "architecture", "pipeline", "module", "encoder", "decoder", "transformer", "attention",
    "policy", "controller", "planner", "algorithm", "optimization", "objective", "loss",
    "training", "inference", "representation", "latent", "dynamics", "trajectory", "action",
    "observation", "state", "force", "contact", "input", "output", "feedback", "embedding",
)
EVAL_TERMS = (
    "experiment", "evaluation", "result", "results", "benchmark", "dataset", "baseline",
    "compared", "comparison", "ablation", "success rate", "accuracy", "error", "score",
    "performance", "real-world", "robot", "%", "table", "figure", "outperform", "improve",
)
EXCLUDED_SECTIONS = (
    "reference", "bibliograph", "acknowledg", "related work", "literature review", "front matter",
)


def load_items() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, str]]]:
    papers = {item["paper_id"]: item for item in json.loads(PAPERS.read_text(encoding="utf-8"))}
    with TIERS.open(newline="", encoding="utf-8") as handle:
        rows = {row["paper_id"]: row for row in csv.DictReader(handle)}
    return papers, rows


def low_section(value: Evidence) -> str:
    return f"{value.section} {value.parent}".casefold()


def clean_section_label(value: str) -> str:
    """Make unresolved section recovery explicit in generated citations."""
    return re.sub(
        r"\bsection not recovered\b",
        "section boundary not confidently recovered",
        safe(value),
        flags=re.I,
    )


def clean_evidence_text(value: str) -> str:
    """Remove high-confidence PDF chrome before ranking or emitting a cue."""
    cleaned = clean_extractive_line(value, Counter())
    return cleaned.strip() if cleaned else ""


def contains_any(text: str, terms: Iterable[str]) -> int:
    low = text.casefold()
    return sum(term.casefold() in low for term in terms)


def ranked(
    values: Iterable[Evidence],
    terms: Iterable[str],
    *,
    preferred_sections: Iterable[str] = (),
    negative: bool = False,
    allow_captions: bool = False,
    max_items: int = 2,
) -> list[Evidence]:
    preferred = tuple(value.casefold() for value in preferred_sections)
    result: list[Evidence] = []
    candidates: list[Evidence] = []
    for value in values:
        section = low_section(value)
        if any(token in section for token in EXCLUDED_SECTIONS):
            continue
        text = clean_evidence_text(value.text)
        if len(text) < 35:
            continue
        term_score = contains_any(text, terms)
        neg_score = contains_any(text, NEGATIVE_TERMS)
        hard_neg_score = contains_any(text, HARD_NEGATIVE_TERMS)
        if negative and hard_neg_score == 0:
            continue
        score = 2.0 * term_score + 2.4 * hard_neg_score + 0.6 * neg_score if negative else 2.0 * term_score
        if any(token in section for token in preferred):
            score += 3.0
        if negative:
            # Future-work and conclusion paragraphs often mention a generic
            # limitation without identifying the mechanism's actual failure
            # regime. Prefer a dedicated limitation/failure section or a
            # measured negative result instead.
            if "future work" in section:
                score -= 3.0
            if "conclusion" in section:
                score -= 1.0
            if "limitation" in section or "failure" in section:
                score += 2.5
        if value.page <= 2 and not negative:
            score += 0.4
        is_caption = bool(re.search(r"(?:^|\s)(?:fig(?:ure)?\.?|table|tab\.)\s*\d+\s*[:.]", text, flags=re.I))
        if is_caption and not allow_captions:
            continue
        if is_caption:
            score -= 1.5
        # Contribution/method lines with a long citation list or a repeated
        # title are weak semantic evidence even if they contain "we".
        if text.count("[") >= 4 or text.count("(") >= 8:
            score -= 0.8
        candidates.append(Evidence(value.page, value.section, text, score, value.parent))
    candidates.sort(key=lambda value: (-value.score, value.page, len(value.text)))
    for value in candidates:
        if any(similar(value.text, previous.text) for previous in result):
            continue
        result.append(value)
        if len(result) >= max_items:
            break
    return result


def first_or(values: list[Evidence], fallback: str) -> str:
    return short_cue(values[0].text, 30) if values else fallback


def safe(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("|", "/")).strip()


def cue(values: list[Evidence], fallback: str) -> str:
    if not values:
        return fallback
    value = values[0]
    return f"{safe(short_cue(value.text, 30))} (p. {value.page}, {clean_section_label(value.section)})"


def evidence_anchor(values: list[Evidence], fallback: str) -> str:
    """Use the shared anchor formatter with an explicit section boundary."""
    return clean_section_label(anchor(values, fallback))


def evidence_bundle(document: dict[str, Any]) -> dict[str, list[Evidence]]:
    inferred = infer_evidence(document)
    all_body = list(document.get("sentences", []))
    problem_pool = inferred["problem"] + inferred["abstract"] + inferred["conclusion"]
    contribution_pool = inferred["changes"] + inferred["method"] + inferred["abstract"]
    method_pool = inferred["method"] + inferred["objective"] + inferred["interface"]
    evaluation_pool = inferred["results"] + inferred["metrics"] + inferred["baseline"] + inferred["dataset"] + inferred["captions"]
    failure_pool = all_body + inferred["failure"]
    return {
        "problem": ranked(problem_pool, ("challenge", "problem", "bottleneck", "limitation", "however", "difficult", "lack", "cannot", "fails"), preferred_sections=("introduction", "background", "problem", "motivation"), max_items=2),
        "contribution": ranked(contribution_pool, CONTRIBUTION_TERMS, preferred_sections=("contribution", "introduction", "method", "approach"), max_items=2),
        "method": ranked(method_pool, METHOD_TERMS, preferred_sections=("method", "approach", "architecture", "algorithm", "model", "policy"), max_items=2),
        "objective": ranked(inferred["objective"] + inferred["equations"] + inferred["method"], ("objective", "loss", "reward", "cost", "constraint", "optimiz", "gradient", "equation", "update"), preferred_sections=("objective", "loss", "optimization", "training", "algorithm", "formulation"), max_items=2),
        "evaluation": ranked(evaluation_pool, EVAL_TERMS, preferred_sections=("experiment", "evaluation", "result", "benchmark", "ablation", "implementation"), allow_captions=True, max_items=3),
        "failure": ranked(failure_pool, NEGATIVE_TERMS, preferred_sections=("limitation", "failure", "discussion", "future", "conclusion", "result", "evaluation", "experiment"), negative=True, max_items=2),
        "interface": ranked(inferred["interface"] + inferred["method"] + inferred["changes"], ("input", "output", "observation", "action", "image", "image set", "camera", "view", "pixel", "ray", "point", "language", "instruction", "force", "contact", "pose", "velocity", "torque", "feedback", "embedding"), preferred_sections=("problem", "formulation", "method", "approach", "system"), max_items=2),
        "temporal": ranked(inferred["temporal"] + inferred["repro"], ("horizon", "history", "sequence", "frame", "frequency", "hz", "fps", "latency", "real-time", "step", "episode", "memory"), preferred_sections=("method", "implementation", "experiment", "evaluation"), max_items=2),
        "dataset": ranked(inferred["dataset"] + inferred["results"], ("dataset", "benchmark", "environment", "task", "episode", "trajectory", "robot", "hardware", "simulation", "real-world", "split"), preferred_sections=("dataset", "benchmark", "experiment", "evaluation"), max_items=2),
        "metric": ranked(inferred["metrics"] + inferred["results"] + inferred["captions"], ("success rate", "accuracy", "error", "reward", "return", "score", "performance", "robustness", "%", "iou", "distance", "completion"), preferred_sections=("result", "evaluation", "experiment", "benchmark"), allow_captions=True, max_items=2),
        "baseline": ranked(inferred["baseline"] + inferred["ablation"] + inferred["results"], ("baseline", "compared", "comparison", "prior work", "state-of-the-art", "outperform", "ablation", "without", "oracle"), preferred_sections=("comparison", "result", "evaluation", "ablation", "experiment"), allow_captions=True, max_items=2),
        "ablation": ranked(inferred["ablation"] + inferred["results"], ("ablation", "without", "remove", "variant", "sensitivity", "effect of", "replace", "freeze"), preferred_sections=("ablation", "analysis", "evaluation", "experiment"), allow_captions=True, max_items=2),
    }


def generic_counts(text: str) -> dict[str, int]:
    patterns = {
        "not_recovered": r"\bnot recovered\b",
        "cue_empty": r"cue 없음",
        "paper_specific_placeholder": r"paper-specific [^\n]{0,100}(?:not recovered|not stated)",
        "generic_body_fallback": r"(?:body cue 없음|not recovered in the selected body cues|selected body cue 없음)",
    }
    return {name: len(re.findall(pattern, text, flags=re.I)) for name, pattern in patterns.items()}


def clean_generic(text: str) -> str:
    for old, new in GENERIC_REPLACEMENTS.items():
        text = text.replace(old, new)
    text = text.replace(
        " body cue 없음",
        " was not selected from the PDF body; no claim inferred",
    )
    text = text.replace("cue 없음", "PDF body cue not selected; no claim inferred")
    text = text.replace(
        "exact value not recovered from the selected body cues",
        "exact value was not selected from the PDF body",
    )
    text = text.replace(
        "exact profile 확인 필요",
        "exact profile was not selected from the PDF body",
    )
    # Do not erase legitimate evidence-boundary language.  Only phrases that
    # present an unqualified generated placeholder are rewritten.
    text = re.sub(
        r"\b(paper-specific(?: [A-Za-z0-9_/-]+){0,8}) not recovered\b",
        r"PDF body did not yield a recoverable \1 statement; no claim inferred",
        text,
        flags=re.I,
    )
    text = re.sub(
        r"\b((?:problem/motivation|method/contribution|claim/result|abstract/introduction|method|objective/update|dataset/benchmark|metric definition|baseline/ablation) body cue) not recovered\b",
        r"\1 was not selected from the PDF body; no claim inferred",
        text,
        flags=re.I,
    )
    text = re.sub(r"\bsection not recovered\b", "section boundary not confidently recovered", text, flags=re.I)
    text = re.sub(r"\bnot recovered\b", "not stated or recoverable in the selected PDF body", text, flags=re.I)
    return text


def replace_block(text: str, heading: str, next_heading: str, content: str) -> str:
    pattern = re.compile(
        rf"(?ms)^{re.escape(heading)}\s*$.*?(?=^{re.escape(next_heading)}\s*$)"
    )
    replacement = heading + "\n\n" + content.rstrip() + "\n\n"
    if pattern.search(text):
        # Body cues can contain backslashes from extracted equations.  A
        # callable replacement keeps those characters literal rather than
        # letting ``re`` interpret them as replacement-template escapes.
        return pattern.sub(lambda _match: replacement, text, count=1)
    return text.rstrip() + "\n\n" + replacement


def replace_tail(text: str, heading: str, content: str) -> str:
    pattern = re.compile(rf"(?ms)^{re.escape(heading)}\s*$.*\Z")
    replacement = heading + "\n\n" + content.rstrip() + "\n"
    if pattern.search(text):
        return pattern.sub(lambda _match: replacement, text, count=1)
    return text.rstrip() + "\n\n" + replacement


def insights_rewrite(text: str, bundle: dict[str, list[Evidence]], item: dict[str, Any], row: dict[str, str]) -> str:
    mechanism = cue(bundle["contribution"] or bundle["method"], "PDF body did not yield a recoverable mechanism statement; no claim inferred")
    interface = cue(bundle["interface"] or bundle["method"], "PDF body did not yield a recoverable input/output interface; no claim inferred")
    outcome = cue(bundle["evaluation"] or bundle["metric"], "PDF body did not yield a recoverable evaluation outcome; no claim inferred")
    failure = cue(bundle["failure"], "PDF body did not yield an explicit failure/limitation statement; no failure inferred")
    dataset = cue(bundle["dataset"], "PDF body did not yield a recoverable task/dataset setup; no setup inferred")
    metric = cue(bundle["metric"], "PDF body did not yield a recoverable metric statement; no metric inferred")
    baseline = cue(bundle["baseline"], "PDF body did not yield a recoverable baseline/comparison statement; no comparison inferred")
    ablation = cue(bundle["ablation"], "PDF body did not yield a recoverable ablation/stress condition; no ablation inferred")
    objective = cue(bundle["objective"], "PDF body did not yield a recoverable objective/update statement; no objective inferred")
    question = (
        f"Under the paper's stated interface ({safe(short_cue(bundle['interface'][0].text, 22)) if bundle['interface'] else 'the stated input/output interface'}), "
        f"does the paper-specific mechanism ({safe(short_cue((bundle['contribution'] or bundle['method'])[0].text, 22)) if (bundle['contribution'] or bundle['method']) else 'the proposed mechanism'}) "
        f"retain the reported evaluation outcome ({safe(short_cue((bundle['metric'] or bundle['evaluation'])[0].text, 18)) if (bundle['metric'] or bundle['evaluation']) else 'the primary body metric'}) "
        f"when tested against the paper's strongest explicit boundary ({safe(short_cue(bundle['failure'][0].text, 18)) if bundle['failure'] else 'an explicitly measured limitation condition'})?"
    )
    reject = (
        f"Reject the hypothesis if the body-reported metric ({safe(short_cue(bundle['metric'][0].text, 18)) if bundle['metric'] else 'primary metric'}) does not improve at matched observation, action, data and compute, "
        "or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain."
    )
    reproduction = "\n".join(
        [
            f"1. Reconstruct the PDF-described interface and mechanism: {interface}; preserve the objective/update rule: {objective}.",
            f"2. Use the paper-reported task/data/environment cue: {dataset}.",
            f"3. Compare against the reported or matched baseline: {baseline}.",
            f"4. Report the body metric with its denominator and aggregation: {metric}.",
            f"5. Re-run the reported ablation or stress/failure condition: {ablation}; if none is reported, design one around: {failure}.",
            "6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.",
        ]
    )
    success = (
        f"A faithful reproduction must recover the mechanism at {evidence_anchor(bundle['contribution'] or bundle['method'], 'mechanism anchor unavailable in the PDF body')}, "
        f"match the reported outcome at {evidence_anchor(bundle['evaluation'] or bundle['metric'], 'result anchor unavailable in the PDF body')}, "
        f"and measure the boundary at {evidence_anchor(bundle['failure'], 'explicit failure/limitation anchor unavailable in the PDF body')}."
    )
    lesson = "\n".join(
        [
            f"- **Paper-specific interface:** {interface}.",
            f"- **Paper-specific mechanism:** {mechanism}.",
            f"- **Evidence boundary:** the reported outcome is {outcome}; the relevant task/metric cue is {metric}. The PDF does not establish downstream robotics benefit beyond those conditions.",
            f"- **Failure implication:** {failure}.",
            "- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.",
        ]
    )
    text = clean_generic(text)
    text = replace_block(text, "### Reusable lesson in the robotics loop", "### Dependency and evolution", lesson)
    text = replace_block(text, "### Minimal reproduction", "### What would count as a successful reproduction", reproduction)
    text = replace_block(text, "### What would count as a successful reproduction", "## Falsifiable research question", "- " + success)
    text = replace_tail(text, "## Falsifiable research question", question + "\n\n**Reject the hypothesis if** " + reject)
    return text


def qa_block(kind: str, item: dict[str, Any], row: dict[str, str], bundle: dict[str, list[Evidence]], document: dict[str, Any], record: dict[str, Any]) -> str:
    contribution = cue(bundle["contribution"], "PDF body did not yield an explicit contribution statement; no claim inferred")
    problem = cue(bundle["problem"], "PDF body did not yield an explicit bottleneck statement; no bottleneck inferred")
    method = cue(bundle["method"], "PDF body did not yield a recoverable method/interface statement; no method detail inferred")
    objective = cue(bundle["objective"], "PDF body did not yield a recoverable objective/update statement; no objective inferred")
    evaluation = cue(bundle["evaluation"], "PDF body did not yield a recoverable evaluation setup/result statement; no result inferred")
    metric = cue(bundle["metric"], "PDF body did not yield a recoverable metric statement; no metric inferred")
    baseline = cue(bundle["baseline"], "PDF body did not yield a recoverable baseline/comparison statement; no comparison inferred")
    failure = cue(bundle["failure"], "PDF body did not yield an explicit failure/limitation statement; no failure inferred")
    temporal = cue(bundle["temporal"], "PDF body did not yield a recoverable temporal/runtime cue; timing remains unresolved")
    overlap = record.get("title_token_overlap_first_two_pages", 0)
    quality = record.get("extraction_quality", "unknown")
    return (
        "## Semantic QA — PDF body cross-check\n\n"
        f"> Cross-checked on {date.today().isoformat()} against the validated PDF body ({record.get('pages', document.get('pages', 0))} pages; {record.get('extraction_method', document.get('extraction_method', 'unknown'))}; extraction quality: {quality}; title-token overlap: {overlap}). This block is a source-quality correction and does not change reading status.\n\n"
        + {
            "01_overview.md": (
                f"- **Problem/bottleneck:** {problem}.\n"
                f"- **Actual contribution:** {contribution}.\n"
                f"- **Evaluation boundary:** {evaluation}.\n"
                f"- **Explicit failure boundary:** {failure}."
            ),
            "02_problem.md": (
                f"- **Target problem:** {problem}.\n"
                f"- **Formulation-changing contribution:** {contribution}.\n"
                f"- **Assumption/failure evidence:** {failure}.\n"
                "- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it."
            ),
            "03_method.md": (
                f"- **Paper-specific method/interface:** {method}.\n"
                f"- **Objective/update evidence:** {objective}.\n"
                f"- **Temporal/runtime evidence:** {temporal}.\n"
                "- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor."
            ),
            "04_evaluation.md": (
                f"- **Evaluation setup/result:** {evaluation}.\n"
                f"- **Metric evidence:** {metric}.\n"
                f"- **Baseline/ablation evidence:** {baseline}.\n"
                f"- **Failure/negative evidence:** {failure}."
            ),
            "05_insights.md": (
                f"- **Paper-supported mechanism:** {contribution}.\n"
                f"- **Paper-supported outcome:** {evaluation}.\n"
                f"- **Strongest explicit boundary:** {failure}.\n"
                "- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage."
            ),
        }[kind]
        + "\n"
    )


def process_pdf(args: tuple[str, Path, dict[str, Any]]) -> dict[str, Any]:
    paper_id, pdf_path, item = args
    try:
        document = extract_document(pdf_path, allow_ocr=False)
        return {"paper_id": paper_id, "item": item, "document": document, "error": None}
    except Exception as exc:  # pragma: no cover - individual corrupt PDFs are reported
        return {"paper_id": paper_id, "item": item, "document": None, "error": f"{type(exc).__name__}: {exc}"}


def process_pdf_with_ocr(args: tuple[str, Path, dict[str, Any]]) -> dict[str, Any]:
    """Re-extract one low-confidence PDF with the canonical OCR fallback."""
    paper_id, pdf_path, item = args
    try:
        document = extract_document(pdf_path, allow_ocr=True)
        return {"paper_id": paper_id, "item": item, "document": document, "error": None}
    except Exception as exc:  # pragma: no cover - individual corrupt PDFs are reported
        return {"paper_id": paper_id, "item": item, "document": None, "error": f"{type(exc).__name__}: {exc}"}


def update_note(path: Path, content: str, kind: str, bundle: dict[str, list[Evidence]], item: dict[str, Any], row: dict[str, str], document: dict[str, Any], record: dict[str, Any]) -> str:
    old = path.read_text(encoding="utf-8", errors="ignore")
    before_counts = generic_counts(old)
    new = clean_generic(old)
    if kind == "05_insights.md":
        new = insights_rewrite(new, bundle, item, row)
    # Remove only a previous block generated by this script, leaving all
    # manually maintained lineage and interpretation outside that block intact.
    new = re.sub(r"(?ms)\n## Semantic QA — PDF body cross-check\s*\n.*\Z", "", new).rstrip()
    new += "\n\n" + qa_block(kind, item, row, bundle, document, record)
    path.write_text(new.rstrip() + "\n", encoding="utf-8")
    after_counts = generic_counts(new)
    return json.dumps({"before": before_counts, "after": after_counts}, ensure_ascii=False)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-dir", type=Path, default=DEFAULT_PDF_DIR)
    parser.add_argument("--download-manifest", type=Path, default=DEFAULT_DOWNLOAD_MANIFEST)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument(
        "--ocr-low-confidence",
        action="store_true",
        help="re-run the fast-sweep low-confidence PDFs through the canonical OCR fallback",
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    pdf_dir = args.pdf_dir if args.pdf_dir.is_absolute() else ROOT / args.pdf_dir
    download_manifest = args.download_manifest if args.download_manifest.is_absolute() else ROOT / args.download_manifest
    report_path = args.report if args.report.is_absolute() else ROOT / args.report
    papers, tiers = load_items()
    selected = [
        (paper_id, papers[paper_id])
        for paper_id, row in sorted(tiers.items())
        if row.get("tier") in {"CORE", "NEXT"} and paper_id in papers
    ]
    downloads = load_download_manifest(download_manifest) if download_manifest.exists() else {}
    pdf_tasks: list[tuple[str, Path, dict[str, Any]]] = []
    source_boundary: list[dict[str, Any]] = []
    for paper_id, item in selected:
        record = downloads.get(paper_id, {})
        pdf_path = pdf_dir / f"{paper_id}.pdf"
        if record.get("status") in {"downloaded", "reused"} and pdf_path.exists():
            pdf_tasks.append((paper_id, pdf_path, item))
        else:
            source_boundary.append({
                "paper_id": paper_id,
                "title": item.get("title"),
                "download_status": record.get("status", "missing"),
                "error": record.get("error", "PDF not available in this task cache"),
                "disposition": "not included in PDF-body QA; retain existing source-boundary note",
            })

    extracted: dict[str, dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(process_pdf, task): task[0] for task in pdf_tasks}
        for index, future in enumerate(as_completed(futures), start=1):
            result = future.result()
            extracted[result["paper_id"]] = result
            if index % 25 == 0 or index == len(pdf_tasks):
                print(f"[{index}/{len(pdf_tasks)}] PDF body QA extracted", flush=True)

    if args.ocr_low_confidence:
        ocr_tasks = []
        for paper_id, pdf_path, item in pdf_tasks:
            result = extracted.get(paper_id)
            document = result.get("document") if result else None
            if not document:
                ocr_tasks.append((paper_id, pdf_path, item))
                continue
            overlap = title_token_overlap(item["title"], document)
            if (
                document.get("extraction_quality") == "low"
                or overlap < 0.5
                or len(document.get("headings", [])) < 2
            ):
                ocr_tasks.append((paper_id, pdf_path, item))
        print(f"OCR fallback queue: {len(ocr_tasks)} PDFs", flush=True)
        with ThreadPoolExecutor(max_workers=max(1, min(args.workers, 8))) as executor:
            futures = {executor.submit(process_pdf_with_ocr, task): task[0] for task in ocr_tasks}
            for index, future in enumerate(as_completed(futures), start=1):
                result = future.result()
                extracted[result["paper_id"]] = result
                if index % 10 == 0 or index == len(ocr_tasks):
                    print(f"[{index}/{len(ocr_tasks)}] OCR PDF body QA extracted", flush=True)

    records: list[dict[str, Any]] = []
    quality_counts: Counter[str] = Counter()
    method_counts: Counter[str] = Counter()
    changed_files = 0
    low_confidence: list[str] = []
    extraction_errors: list[dict[str, str]] = []
    for paper_id, item in selected:
        row = tiers[paper_id]
        result = extracted.get(paper_id)
        download_record = dict(downloads.get(paper_id, {}))
        if not result or result.get("error") or not result.get("document"):
            extraction_errors.append({"paper_id": paper_id, "error": (result or {}).get("error", "PDF extraction result missing")})
            continue
        document = result["document"]
        bundle = evidence_bundle(document)
        overlap = title_token_overlap(item["title"], document)
        quality = document.get("extraction_quality", "unknown")
        quality_counts[quality] += 1
        method_counts[document.get("extraction_method", "unknown")] += 1
        record = {
            "paper_id": paper_id,
            "title": item["title"],
            "tier": row.get("tier"),
            "primary_track": row.get("primary_track", ""),
            "pdf_status": download_record.get("status"),
            "pdf_source": download_record.get("url"),
            "pages": document.get("pages"),
            "text_chars": document.get("text_chars"),
            "extraction_method": document.get("extraction_method"),
            "extraction_quality": quality,
            "title_token_overlap_first_two_pages": overlap,
            "section_heading_count": len(document.get("headings", [])),
            "evidence_counts": {name: len(values) for name, values in bundle.items()},
            "anchors": {
                name: evidence_anchor(values, "not selected from PDF body")
                for name, values in bundle.items()
                if name in {"problem", "contribution", "method", "objective", "evaluation", "failure", "interface", "metric", "baseline", "ablation"}
            },
            "cues": {
                name: safe(short_cue(values[0].text, 32)) if values else None
                for name, values in bundle.items()
                if name in {"problem", "contribution", "method", "objective", "evaluation", "failure", "interface", "metric", "baseline", "ablation"}
            },
            "generic_marker_before": {},
            "generic_marker_after": {},
            "note_files_changed": 0,
            "qa_disposition": "PDF_BODY_CROSS_CHECKED",
        }
        if quality == "low" or overlap < 0.5 or len(document.get("headings", [])) < 2:
            record["qa_disposition"] = "PDF_BODY_LOW_CONFIDENCE"
            low_confidence.append(paper_id)
        folder = resolve_folder(str(item["folder"]))
        for name in NOTE_NAMES:
            note_path = folder / name
            old_text = note_path.read_text(encoding="utf-8", errors="ignore")
            record["generic_marker_before"][name] = generic_counts(old_text)
            cleaned = clean_generic(old_text)
            if name == "05_insights.md":
                cleaned = insights_rewrite(cleaned, bundle, item, row)
            cleaned = re.sub(r"(?ms)\n## Semantic QA — PDF body cross-check\s*\n.*\Z", "", cleaned).rstrip()
            cleaned += "\n\n" + qa_block(name, item, row, bundle, document, {
                **download_record,
                "pages": document.get("pages"),
                "extraction_method": document.get("extraction_method"),
                "extraction_quality": quality,
                "title_token_overlap_first_two_pages": overlap,
            })
            record["generic_marker_after"][name] = generic_counts(cleaned)
            if cleaned != old_text:
                record["note_files_changed"] += 1
                changed_files += 1
                if args.apply:
                    note_path.write_text(cleaned.rstrip() + "\n", encoding="utf-8")
        records.append(record)

    report = {
        "review_date": date.today().isoformat(),
        "scope": "CORE/NEXT",
        "selected_paper_count": len(selected),
        "pdf_body_cross_checked_count": len(records),
        "source_boundary_count": len(source_boundary),
        "note_files_changed": changed_files if args.apply else sum(record["note_files_changed"] for record in records),
        "mode": "apply" if args.apply else "dry-run",
        "method": {
            "body_parser": "review_fulltext_notes.extract_document",
            "section_inference": "section-aware contribution/method/evaluation/failure ranking",
            "ocr_in_first_sweep": False,
            "generic_fallback_policy": "replace unqualified placeholders; retain unresolved fields as explicit no-claim boundaries",
            "tracker_changed": False,
            "tier_changed": False,
        },
        "extraction_quality": dict(quality_counts),
        "extraction_methods": dict(method_counts),
        "low_confidence_paper_ids": low_confidence,
        "source_boundary_papers": source_boundary,
        "extraction_errors": extraction_errors,
        "records": sorted(records, key=lambda record: record["paper_id"]),
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print({
        "mode": report["mode"],
        "selected": report["selected_paper_count"],
        "pdf_body_cross_checked": report["pdf_body_cross_checked_count"],
        "source_boundary": report["source_boundary_count"],
        "note_files_changed": report["note_files_changed"],
        "low_confidence": len(low_confidence),
        "extraction_errors": len(extraction_errors),
        "report": str(report_path),
    })
    return 0 if not extraction_errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
