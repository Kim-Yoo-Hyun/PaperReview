#!/usr/bin/env python3
"""Write page-anchored 02/03/04 notes from validated full-text PDFs.

The input PDFs are task-scoped temporary caches produced by
download_fulltext_pdfs.py. The script extracts body evidence with PyMuPDF,
uses pdftotext/tesseract only when the text layer is insufficient, and writes
the common note schema for non-CORE/NEXT papers only.

It deliberately does not change the reading tracker or registry metadata.
Run without --apply for a dry run.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import unicodedata
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote

import fitz

try:
    from enrich_remaining_notes import (
        DOMAIN_FORMULATION,
        DOMAIN_MODULES,
        DOMAIN_SCOPE,
        infer_domain,
        runtime_contract,
        resolve_folder,
    )
except ModuleNotFoundError:  # pragma: no cover
    from .enrich_remaining_notes import (
        DOMAIN_FORMULATION,
        DOMAIN_MODULES,
        DOMAIN_SCOPE,
        infer_domain,
        runtime_contract,
        resolve_folder,
    )


ROOT = Path(__file__).resolve().parents[2]
PAPERS = ROOT / "work" / "sources" / "papers.json"
TIERS = ROOT / "research" / "READING_TIERS.csv"
DEFAULT_PDF_DIR = ROOT / "tmp" / "pdfs" / "fulltext_remaining_2026-09-01"
DEFAULT_REVIEW_MANIFEST = ROOT / "work" / "sources" / "fulltext_review_manifest.json"
BT = chr(96)

LIGATURES = {
    "ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl",
    "’": "'", "“": '"', "”": '"', "−": "-", "–": "-", "—": "-",
}
STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "with", "from",
    "by", "as", "is", "are", "was", "were", "be", "this", "that", "these", "those",
    "we", "our", "their", "it", "its", "which", "can", "may", "also", "into", "than",
    "such", "both", "each", "all", "via", "based", "paper", "method", "approach",
    "results", "work", "show", "shows", "shown", "propose", "proposed", "using", "used",
}
SECTION_RE = re.compile(r"^\s*(?:(?:\d+(?:\.\d+)*|[IVX]+)[.)]?\s+)?[A-Z][^.!?]{2,96}$")
NUMBERED_HEADING_RE = re.compile(
    r"^\s*(?:\d+(?:\.\d+)*|[IVX]+)[.)]?\s+[A-Z0-9]"
)
APPENDIX_HEADING_RE = re.compile(r"^\s*[A-C][.)]\s+[A-Z0-9]")
APPENDIX_NUMBERED_HEADING_RE = re.compile(r"^\s*[A-C](?:\.\d+)+[.)]?\s+[A-Z0-9]")
APPENDIX_PREFIX_RE = re.compile(r"^\s*[A-C](?:\.\d+)*[.)]?\s*$")
CAPTION_START_RE = re.compile(r"^\s*(?:Figure|Fig\.|Table|Tab\.)\s*\d+\s*[:.]")
NUMBER_RE = re.compile(
    r"(?:\b\d+(?:\.\d+)?\s*(?:%|Hz|fps|ms|s|steps?|epochs?|episodes?|trials?|"
    r"seeds?|frames?|trajectories?|rollouts?|samples?|points?|dimensions?|layers?|"
    r"parameters?|hours?|GPUs?|robots?|tasks?|scenes?|objects?|tokens?|"
    r"meters?|centimeters?|degrees?)\b|"
    r"\b(?:N|n)\s*=\s*\d+|\b\d+(?:\.\d+)?\s*[x×]\b|"
    r"\b\d+(?:\.\d+)?\s*(?:±|\\+/-)\s*\d+(?:\.\d+)?|\b\d+(?:\.\d+)?%\b)",
    re.I,
)

PROBLEM_TERMS = (
    "challenge", "problem", "bottleneck", "difficult", "difficulty", "limitation",
    "existing", "prior", "current", "cannot", "fails", "failure", "lack", "gap",
    "intractable", "scalability", "generalize", "generalization", "uncertainty",
)
CHANGE_TERMS = (
    "we propose", "we introduce", "we present", "our method", "our approach",
    "our framework", "contribution", "novel", "develop", "designed", "allows",
    "enables", "consists of", "we show",
)
METHOD_TERMS = (
    "architecture", "network", "module", "encoder", "decoder", "transformer",
    "attention", "policy", "controller", "planner", "algorithm", "optimization",
    "objective", "loss", "training", "inference", "model", "representation",
    "feature", "latent", "dynamics", "trajectory", "action", "observation",
    "state", "force", "contact", "simulator",
)
OBJECTIVE_TERMS = (
    "objective", "loss", "optimiz", "minimiz", "maximiz", "gradient", "reward",
    "return", "likelihood", "probability", "constraint", "regulariz", "equation",
    "update", "target network", "advantage", "value function", "cost function",
    "arg max", "arg min", "cost", "feasibility", "progress", "cross-entropy",
    "cross entropy", "next-token", "causal", "prediction objective", "action prediction",
    "token prediction",
)
INTERFACE_TERMS = (
    "observation", "input", "output", "state", "action", "command", "policy",
    "goal", "proprioception", "image", "video", "point cloud", "depth", "language",
    "instruction", "pose", "velocity", "torque", "force", "wrench", "map",
    "feedback", "sensor",
)
TEMPORAL_TERMS = (
    "time step", "timestep", "horizon", "history", "sequence", "frame", "chunk",
    "frequency", "hz", "fps", "latency", "real-time", "online", "receding",
    "rollout", "episode", "step", "memory", "temporal", "delay", "control rate",
)
DATASET_TERMS = (
    "dataset", "benchmark", "environment", "task", "episode", "trajectory", "scene",
    "object", "robot", "simulator", "simulation", "demonstration", "training set",
    "test set", "validation", "held-out", "unseen", "real-world", "hardware",
)
METRIC_TERMS = (
    "accuracy", "success rate", "success", "reward", "return", "error", "loss",
    "precision", "recall", "f1", "iou", "bleu", "map", "spl", "collision",
    "distance", "completion", "rate", "score", "performance", "robustness",
    "variance", "standard deviation", "confidence",
)
BASELINE_TERMS = (
    "baseline", "compared", "comparison", "prior work", "state-of-the-art", "sota",
    "outperform", "strong baseline", "oracle", "ablation", "without",
)
ABLATION_TERMS = (
    "ablation", "without", "remove", "removing", "variant", "component", "effect of",
    "sensitivity", "replace", "freeze", "fine-tun", "pretrain",
)
FAILURE_TERMS = (
    "failure", "fail", "limitation", "future work", "does not", "cannot", "unstable",
    "degrade", "degradation", "out-of-distribution", "out of distribution", "robust",
    "noise", "occlusion", "disturbance", "recovery", "unsafe", "collision", "slip",
    "fall",
)
REPRO_TERMS = (
    "implementation", "hardware", "gpu", "cpu", "training time", "compute", "runtime",
    "seed", "trial", "run", "code", "checkpoint", "hyperparameter", "learning rate",
    "batch size", "steps", "epochs", "inference time", "throughput",
)


@dataclass(frozen=True)
class Evidence:
    page: int
    section: str
    text: str
    score: float = 0.0
    parent: str = ""


def normalize(value: str) -> str:
    for source, target in LIGATURES.items():
        value = value.replace(source, target)
    value = re.sub(r"(?<=\w)-\s*\n\s*(?=\w)", "", value)
    return re.sub(r"\s+", " ", value).strip()


def clean_sentence(value: str) -> str:
    value = normalize(value).replace("|", "/")
    # PDF text layers often append author footnotes or acceptance stamps to a
    # real sentence.  Keep the paper sentence prefix, but never let those
    # front-matter fragments become evidence in a note.
    value = re.sub(r"^\s*accepted\s+[a-z]+,?\s+20\d{2}\s+", "", value, flags=re.I)
    value = re.split(r"\s*[\u2217*]?equal contribution\b", value, maxsplit=1, flags=re.I)[0]
    return re.sub(r"\s+", " ", value).strip(" -")


def short_cue(value: str, max_words: int = 25, max_chars: int = 240) -> str:
    value = clean_sentence(value)
    words = value.split()
    if len(words) > max_words:
        value = " ".join(words[:max_words]) + " ..."
    if len(value) > max_chars:
        value = value[: max_chars - 4].rstrip() + " ..."
    return value


def md_cell(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value).replace("|", "/").replace("\n", " ")).strip()


def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(md_cell(item) for item in headers) + " |",
        "|" + "|".join("---" for _ in headers) + "|",
    ]
    lines.extend("| " + " | ".join(md_cell(item) for item in row) + " |" for row in rows)
    return "\n".join(lines)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def heading_name(line: str) -> str | None:
    value = clean_sentence(line).strip(" .")
    if not value or len(value) > 100 or len(value.split()) > 14:
        return None
    low = value.casefold()
    if re.match(r"^\s*\d{4}\b", value):
        return None
    # Legacy reprints/transcriptions sometimes place an address or publisher
    # footer immediately after a page number.  It is not a section boundary.
    if re.search(
        r"\b\d{3,5}\s+[A-Z][A-Za-z'-]*(?:\s+[A-Z][A-Za-z'-]*){0,3}\s+"
        r"(?:Ave(?:nue)?|Street|St\.?|Road|Rd\.?|Drive|Dr\.?|Lane|Ln\.?)\b",
        value,
    ):
        return None
    # A one-level list item such as ``5 The probability distributions ...``
    # can look like a numbered heading in older OCR/transcription PDFs.
    # Keep short section names (e.g. ``2 Method``), but reject long sentence
    # fragments unless they carry a deeper section number.
    if re.match(r"^\s*\d+\s+[A-Z]", value) and not re.match(r"^\s*\d+\.\d+", value):
        if len(re.findall(r"[A-Za-z][A-Za-z'-]*", value)) > 6:
            return None
    known = {
        "abstract", "introduction", "related work", "background", "preliminaries",
        "problem formulation", "problem statement", "method", "methodology", "approach",
        "model", "architecture", "algorithm", "implementation details", "experiments",
        "experiment", "evaluation", "results", "result", "dataset", "datasets",
        "ablation studies", "ablation study", "qualitative results", "quantitative results",
        "discussion", "limitations", "limitation", "failure analysis", "conclusion",
        "future work", "appendix", "references", "supplementary material",
        "task definition", "existing works", "data collection", "network architecture",
        "loss function", "qualitative analysis", "quantitative analysis", "real-world evaluation",
        "downstream application evaluation", "depth fidelity evaluation", "training details",
        "bibliography", "acknowledgements", "acknowledgments", "supplement", "appendices",
        "additional quantitative analysis", "additional qualitative analysis",
        "model and data updates", "model and data improvements", "experimental results",
        "architecture validation", "data-limited post-training in simulated environments",
        "real gr-1 language following", "learning to manipulate novel objects from human ego videos",
        "generalization to novel behaviors using neural trajectories", "post-training on unitree g1",
        "bimanual yam demo videos", "agibot demo videos", "unitree g1 locomanipulation demo videos",
        "experiments",
    }
    if low in known:
        return value
    # Figure labels, equation fragments, URLs, author lines and table rows are
    # frequently title-cased by PDF extraction but are not section boundaries.
    if any(char in value for char in "=[]{}/@") or re.search(r"\d\s*$", value):
        return None
    if (
        NUMBERED_HEADING_RE.match(value)
        or APPENDIX_HEADING_RE.match(value)
        or APPENDIX_NUMBERED_HEADING_RE.match(value)
    ):
        words = re.findall(r"[A-Za-z][A-Za-z'-]*", value)
        if len(words) > 8 or re.search(r"[,;:]", value):
            return None
        if words and words[-1].casefold() in {
            "a", "an", "and", "as", "at", "by", "for", "from", "in", "into",
            "of", "on", "or", "the", "to", "with", "without",
        }:
            return None
        return value
    return None


def appendix_title(line: str) -> str | None:
    """Recover appendix titles extracted as a letter/number on its own line."""
    value = clean_sentence(line).strip(" .")
    if not value or len(value.split()) > 8 or re.search(r"[,;:]", value):
        return None
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", value)
    if not words or words[-1].casefold() in {
        "a", "an", "and", "as", "at", "by", "for", "from", "in", "into",
        "of", "on", "or", "the", "to", "with", "without",
    }:
        return None
    if not value[0].isupper():
        return None
    return value


def sentence_list(value: str) -> list[str]:
    value = normalize(value)
    if not value:
        return []
    pieces = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(\[])", value)
    result = []
    for piece in pieces:
        # The author-footnote marker is sometimes concatenated to the last
        # line of a body paragraph.  Dropping that mixed fragment is safer
        # than retaining a truncated sentence as evidence.
        if re.search(r"\b equal contribution\b", piece, re.I):
            continue
        piece = clean_sentence(piece)
        if 35 <= len(piece) <= 900:
            result.append(piece)
    return result


def looks_like_noise(value: str) -> bool:
    low = value.casefold()
    if "@" in value or "http://" in low or "https://" in low:
        return True
    if low.startswith((
        "arxiv:", "copyright", "proceedings of", "figure ", "table ",
        "manuscript received", "accepted ", "published ",
    )):
        return True
    if re.fullmatch(r"[\W\d_]+", value) or sum(char.isalpha() for char in value) < 25:
        return True
    return False


def evidence_is_usable(value: Evidence, document: dict[str, Any]) -> bool:
    """Reject front matter, bibliography entries, and diagram remnants.

    PDF text extraction often places a figure's labels in the same paragraph as
    the surrounding method text.  Those labels are useful for visual review but
    should not be selected as a paper's method or failure evidence.
    """
    section = f"{value.section} {value.parent}".casefold()
    text = clean_sentence(value.text)
    low = text.casefold()
    reference_start = document.get("reference_start_page")
    if reference_start and value.page >= reference_start:
        appendix_context = any(token in section for token in ("appendix", "implementation", "supplement"))
        if not appendix_context:
            return False
    if section in {"references", "bibliography", "acknowledgements", "acknowledgments"}:
        return False
    if "front matter" in section:
        return False
    if "reference" in section or "bibliograph" in section or "acknowledg" in section:
        return False
    if re.match(r"^\[\d{1,3}\]", text) and re.search(r"\b(?:19|20)\d{2}\b", text):
        return False
    if low.startswith(("figure ", "fig. ", "table ", "tab. ")):
        return False

    # A repeated paper title followed by short diagram labels is a common
    # extraction artifact.  Do not discard a genuine abstract/introduction
    # sentence that happens to mention the title.
    title = clean_sentence(str(document.get("paper_title", ""))).casefold()
    title_tokens = [word for word in re.findall(r"[a-z0-9]+", title) if word not in STOPWORDS]
    text_tokens = re.findall(r"[a-z0-9]+", low)
    if (
        len(title_tokens) >= 4
        and section not in {"abstract", "introduction"}
        and value.page <= 4
        and len(text_tokens) >= len(title_tokens)
        and len(set(title_tokens[: min(6, len(title_tokens))]) & set(text_tokens[:12]))
        >= min(5, len(title_tokens[: min(6, len(title_tokens))]))
        and sum(low.count(token) for token in ("rgb", "visual", "encoder", "patch", "feature", "map", "input", "output")) >= 2
    ):
        return False
    return not looks_like_noise(text)


def caption_evidence(document: dict[str, Any]) -> list[Evidence]:
    """Return compact Figure/Table caption evidence for evaluation notes."""
    result: list[Evidence] = []
    for row in document["page_rows"]:
        lines = row["raw"].splitlines()
        index = 0
        while index < len(lines):
            if not CAPTION_START_RE.match(lines[index]):
                index += 1
                continue
            parts = [lines[index].strip()]
            index += 1
            while index < len(lines) and lines[index].strip() and len(parts) < 8:
                if CAPTION_START_RE.match(lines[index]) or heading_name(lines[index]):
                    break
                parts.append(lines[index].strip())
                index += 1
            text = clean_sentence(" ".join(parts))
            if len(text) >= 35:
                result.append(Evidence(row["page"], "Figure/Table caption", text))
    return result


def extract_document(path: Path, *, allow_ocr: bool = True) -> dict[str, Any]:
    """Extract a PDF into page-aware evidence rows.

    ``allow_ocr`` is opt-out for the normal note-generation path.  A semantic
    QA pass may disable it for a fast first sweep and then route only the
    resulting low-quality files through OCR; this keeps one canonical parser
    while avoiding an all-document OCR bottleneck.
    """
    document = fitz.open(path)
    page_rows: list[dict[str, Any]] = []
    try:
        for index in range(document.page_count):
            page = document.load_page(index)
            raw = page.get_text("text")
            page_rows.append({"page": index + 1, "raw": raw, "text": normalize(raw)})
    finally:
        document.close()

    text_chars = sum(len(row["text"]) for row in page_rows)
    raw_text = "\n".join(row["raw"] for row in page_rows)
    unusable_text_layer = text_layer_unusable(raw_text)
    original_page_count = len(page_rows)
    extraction_method = "PyMuPDF text"
    sparse_text_layer = unusable_text_layer or text_chars < 1500 or (
        original_page_count >= 4 and text_chars / max(1, original_page_count) < 250
    )
    if sparse_text_layer:
        try:
            result = subprocess.run(
                ["pdftotext", "-layout", str(path), "-"],
                check=False,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="ignore",
                timeout=90,
            )
        except (OSError, subprocess.TimeoutExpired):
            result = None
        if result and result.returncode == 0 and len(normalize(result.stdout)) > text_chars and not text_layer_unusable(result.stdout):
            flat = normalize(result.stdout)
            page_rows = [{"page": 1, "raw": result.stdout, "text": flat}]
            text_chars = len(flat)
            extraction_method = "pdftotext fallback"

    if allow_ocr and (unusable_text_layer or text_chars < 1500 or (
        original_page_count >= 4 and text_chars / max(1, original_page_count) < 250
    )):
        ocr_rows: list[dict[str, Any]] = []
        document = fitz.open(path)
        try:
            for index in range(min(document.page_count, 60)):
                page = document.load_page(index)
                pixmap = page.get_pixmap(matrix=fitz.Matrix(1.3, 1.3), alpha=False)
                try:
                    result = subprocess.run(
                        ["tesseract", "stdin", "stdout", "--psm", "3"],
                        input=pixmap.tobytes("png"),
                        capture_output=True,
                        text=False,
                        timeout=90,
                    )
                except (OSError, subprocess.TimeoutExpired):
                    result = None
                if result and result.returncode == 0:
                    ocr_text = result.stdout.decode("utf-8", errors="ignore")
                    ocr_rows.append({
                        "page": index + 1,
                        "raw": ocr_text,
                        "text": normalize(ocr_text),
                    })
        finally:
            document.close()
        ocr_chars = sum(len(row["text"]) for row in ocr_rows)
        if ocr_chars > 0 and (unusable_text_layer or ocr_chars > text_chars):
            page_rows = ocr_rows
            text_chars = ocr_chars
            extraction_method = "tesseract OCR fallback"

    headings: list[tuple[int, str]] = []
    section_parents: dict[str, str] = {}
    current_section = "Body text (section not recovered)"
    current_parent = "Body text (section not recovered)"
    sentences: list[Evidence] = []
    for row in page_rows:
        segments: list[tuple[str, str, str]] = []
        buffer: list[str] = []
        segment_section = current_section
        segment_parent = current_parent

        def flush_segment() -> None:
            if buffer:
                segment = normalize("\n".join(buffer))
                if segment:
                    segments.append((segment, segment_section, segment_parent))
                buffer.clear()

        lines = row["raw"].splitlines()
        line_index = 0
        while line_index < len(lines):
            line = lines[line_index]
            stripped = line.strip()
            abstract_inline = re.match(r"^\s*Abstract\s*[-:—]\s*(.+)$", line, re.I)
            if abstract_inline:
                flush_segment()
                found = "Abstract"
                headings.append((row["page"], found))
                current_section = found
                current_parent = found
                section_parents[found] = current_parent
                segment_section = current_section
                segment_parent = current_parent
                buffer.append(abstract_inline.group(1))
                line_index += 1
                continue
            # Some proceedings extract a section number and its title as two
            # separate lines (e.g. ``5`` followed by ``Method``).  Join only
            # that high-confidence pattern; otherwise table/figure labels
            # such as a standalone ``Method`` must remain body text.
            number_only = re.fullmatch(r"\s*\d+(?:\.\d+)*\s*", line)
            appendix_only = APPENDIX_PREFIX_RE.fullmatch(line)
            next_heading = heading_name(lines[line_index + 1]) if line_index + 1 < len(lines) else None
            next_appendix_title = (
                appendix_title(lines[line_index + 1])
                if line_index + 1 < len(lines) else None
            )
            if (number_only or appendix_only) and (next_heading or next_appendix_title) and (
                (
                    next_heading
                    and next_heading.casefold() in {
                "abstract", "introduction", "related work", "background", "preliminaries",
                "method", "methodology", "approach", "experiments", "experiment",
                "evaluation", "results", "dataset", "discussion", "conclusion",
                "appendix", "references", "bibliography",
                    }
                )
                or (appendix_only and next_appendix_title)
            ):
                flush_segment()
                found = f"{stripped} {next_heading or next_appendix_title}"
                headings.append((row["page"], found))
                current_section = found
                if not re.match(r"^\s*(?:\d+\.\d+|[A-C]\.\d+)", found):
                    current_parent = found
                section_parents[found] = current_parent
                segment_section = current_section
                segment_parent = current_parent
                line_index += 2
                continue

            found = heading_name(line)
            if found and found.casefold() not in {"abstract"}:
                low_found = found.casefold()
                # Known unnumbered section names need a visual text boundary.
                # This prevents table/diagram labels from hijacking the
                # section assigned to the surrounding body paragraph.
                is_numbered = bool(NUMBERED_HEADING_RE.match(found))
                visual_boundary = (
                    line_index == 0
                    or not lines[line_index - 1].strip()
                    or (line_index + 1 < len(lines) and not lines[line_index + 1].strip())
                )
                boundary_exception = low_found in {
                    "references", "bibliography", "acknowledgements", "acknowledgments",
                }
                if not is_numbered and not visual_boundary and not boundary_exception:
                    found = None
                if "reference" in current_section.casefold() and not (
                    re.match(r"^[A-C](?:[.)]|$)", found or "")
                ):
                    found = None
            if found:
                flush_segment()
                headings.append((row["page"], found))
                current_section = found
                if not re.match(r"^\s*(?:\d+\.\d+|[A-C]\.\d+)", found):
                    current_parent = found
                section_parents[found] = current_parent
                segment_section = current_section
                segment_parent = current_parent
                line_index += 1
                continue
            if not line.strip():
                flush_segment()
                line_index += 1
                continue
            buffer.append(line)
            line_index += 1
        flush_segment()
        row["segments"] = segments
        row["section"] = segments[0][1] if segments else current_section
        for segment, section, parent in segments:
            for sentence in sentence_list(segment):
                if not looks_like_noise(sentence):
                    sentences.append(Evidence(row["page"], section, sentence, parent=parent))
    quality = "high" if text_chars >= 6000 else "medium" if text_chars >= 1500 else "low"
    reference_pages: list[int] = []
    for row in page_rows:
        lines = row["raw"].splitlines()
        explicit_marker = any(
            re.search(
                r"^\s*(?:(?:[IVX]+|\d+)[.)]?\s+)?(?:REFERENCES|BIBLIOGRAPHY)\b",
                line,
                re.I,
            )
            for line in lines
        )
        if extraction_method == "tesseract OCR fallback":
            reference_entries = sum(
                bool(re.match(r"^\s*(?:\[\d{1,3}\]|\(\d{1,3}\))\s+", line))
                for line in lines
            )
            fuzzy_marker = any(
                clean_sentence(line).casefold() in {"re", "ref", "refs"}
                for line in lines
            )
            late_page = row["page"] >= max(3, round(len(page_rows) * 0.6))
            if explicit_marker or (late_page and reference_entries >= 2) or (late_page and fuzzy_marker and reference_entries >= 1):
                reference_pages.append(row["page"])
        elif explicit_marker:
            reference_pages.append(row["page"])
    return {
        "pages": len(page_rows),
        "page_rows": page_rows,
        "headings": headings,
        "section_parents": section_parents,
        "sentences": sentences,
        "text_chars": text_chars,
        "extraction_method": extraction_method,
        "extraction_quality": quality,
        "reference_start_page": min(reference_pages) if reference_pages else None,
    }


def in_section(evidence: Evidence, include: Iterable[str]) -> bool:
    low = f"{evidence.section} {evidence.parent}".casefold()
    return any(token.casefold() in low for token in include)


def score_text(text: str, terms: Iterable[str]) -> float:
    low = text.casefold()
    score = 0.0
    for term in terms:
        normalized_term = term.casefold()
        present = (
            bool(re.search(rf"\b{re.escape(normalized_term)}\b", low))
            if len(normalized_term) <= 3
            else normalized_term in low
        )
        if present:
            score += 1.0 + (0.35 if " " in term else 0.0)
    return score


def similar(left: str, right: str) -> bool:
    left_words = set(re.findall(r"[a-z0-9]{4,}", left.casefold()))
    right_words = set(re.findall(r"[a-z0-9]{4,}", right.casefold()))
    if not left_words or not right_words:
        return False
    return len(left_words & right_words) / max(1, min(len(left_words), len(right_words))) > 0.72


def pick(
    sentences: list[Evidence],
    terms: Iterable[str],
    *,
    sections: Iterable[str] = (),
    max_items: int = 4,
    require_number: bool = False,
    first_pages: int | None = None,
    boost_terms: Iterable[str] = (),
) -> list[Evidence]:
    section_terms = tuple(sections)
    ranked: list[Evidence] = []
    for evidence in sentences:
        if first_pages is not None and evidence.page > first_pages:
            continue
        score = score_text(evidence.text, terms)
        if score <= 0 or (require_number and not NUMBER_RE.search(evidence.text)):
            continue
        score += 1.5 * score_text(evidence.text, boost_terms)
        if section_terms:
            score += 1.2 if in_section(evidence, section_terms) else 0
        if evidence.page <= 2:
            score += 0.25
        ranked.append(Evidence(evidence.page, evidence.section, evidence.text, score, evidence.parent))
    ranked.sort(key=lambda item: (-item.score, item.page, len(item.text)))
    selected: list[Evidence] = []
    page_counts: Counter[int] = Counter()
    for evidence in ranked:
        if page_counts[evidence.page] >= 2 or any(similar(evidence.text, previous.text) for previous in selected):
            continue
        selected.append(evidence)
        page_counts[evidence.page] += 1
        if len(selected) >= max_items:
            break
    return selected


def first_body_sentences(document: dict[str, Any], max_items: int = 5) -> list[Evidence]:
    sentences = [value for value in document["sentences"] if evidence_is_usable(value, document)]
    preferred: list[Evidence] = []
    for evidence in sentences:
        if evidence.page > 3:
            break
        if evidence.section.casefold() == "abstract" or in_section(evidence, ("introduction",)):
            if not any(similar(evidence.text, previous.text) for previous in preferred):
                preferred.append(evidence)
            if len(preferred) >= max_items:
                return preferred
    if preferred:
        return preferred
    fallback: list[Evidence] = []
    for evidence in sentences:
        if evidence.page > 3:
            break
        if not any(similar(evidence.text, previous.text) for previous in fallback):
            fallback.append(evidence)
        if len(fallback) >= max_items:
            break
    return fallback


def combined_evidence(*groups: list[Evidence], limit: int = 12) -> list[Evidence]:
    result: list[Evidence] = []
    for group in groups:
        for value in group:
            if any(similar(value.text, previous.text) for previous in result):
                continue
            result.append(value)
            if len(result) >= limit:
                return result
    return result


def cue_lines(values: list[Evidence], fallback: str, limit: int = 4) -> str:
    if not values:
        return f"- {fallback}"
    return "\n".join(
        f"- **p. {value.page} / {value.section} - extractive body cue:** {short_cue(value.text)}"
        for value in values[:limit]
    )


def anchor(values: list[Evidence], fallback: str = "본문 anchor 없음") -> str:
    if not values:
        return fallback
    return ", ".join(f"p. {item.page} ({item.section})" for item in values[:6])


def body_terms(values: list[Evidence], limit: int = 12) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for evidence in values:
        for word in re.findall(r"[A-Za-z][A-Za-z0-9_/-]{2,}", evidence.text):
            low = word.casefold()
            if low in STOPWORDS or low in seen or len(word) > 36:
                continue
            if word.islower() and len(word) < 4:
                continue
            result.append(word)
            seen.add(low)
            if len(result) >= limit:
                return result
    return result


def title_token_overlap(title: str, document: dict[str, Any]) -> float:
    """Measure whether the first two extracted pages belong to this paper."""
    title_tokens = {
        word for word in re.findall(r"[a-z0-9]+", normalize(title).casefold())
        if word not in STOPWORDS and len(word) >= 3
    }
    first_pages = " ".join(row["text"] for row in document["page_rows"][:2]).casefold()
    body_tokens = set(re.findall(r"[a-z0-9]+", first_pages))
    if not title_tokens:
        return 0.0
    return round(len(title_tokens & body_tokens) / len(title_tokens), 3)


def text_layer_unusable(value: str) -> bool:
    """Detect legacy PDFs whose nominal text layer is an encoded glyph dump."""
    if len(value) < 300:
        return True
    non_whitespace = [char for char in value if not char.isspace()]
    if not non_whitespace:
        return True
    control_ratio = sum(
        unicodedata.category(char).startswith("C")
        and char not in "\n\r\t"
        for char in value
    ) / max(1, len(value))
    printable_ratio = sum(char.isprintable() or char in "\n\r\t" for char in value) / max(1, len(value))
    # A normal research PDF may contain a small number of math/symbol glyphs,
    # but a mapped-font dump has a large control/non-printable fraction.
    return control_ratio > 0.03 or printable_ratio < 0.90


def numeric_cues(values: list[Evidence], limit: int = 6) -> list[Evidence]:
    return [value for value in values if NUMBER_RE.search(value.text)][:limit]


def infer_evidence(document: dict[str, Any]) -> dict[str, list[Evidence]]:
    sentences = [value for value in document["sentences"] if evidence_is_usable(value, document)]
    if len(sentences) < 8:
        # OCR can collapse section labels into front matter.  Keep the usable
        # fallback broad, but never reintroduce bibliography/reference entries.
        sentences = [
            value for value in document["sentences"]
            if "reference" not in value.section.casefold()
            and "bibliograph" not in value.section.casefold()
            and "front matter" not in f"{value.section} {value.parent}".casefold()
            and not re.match(r"^\[\d{1,3}\]", value.text)
        ]
    captions = caption_evidence(document)

    def excluded(value: Evidence, terms: Iterable[str]) -> bool:
        low = f"{value.section} {value.parent}".casefold()
        return any(term.casefold() in low for term in terms)

    intro = [
        value for value in sentences
        if in_section(value, ("introduction", "background", "motivation", "problem", "preliminar", "task definition"))
        and not excluded(value, ("related work", "reference", "bibliograph", "acknowledg"))
    ]
    if len(intro) < 4:
        intro = [
            value for value in sentences
            if value.page <= min(4, document["pages"])
            and not excluded(value, ("related work", "literature", "reference", "bibliograph", "acknowledg"))
        ]

    method_exclusions = (
        "related work", "literature", "front matter", "experiment", "evaluation", "result",
        "comparison", "ablation", "conclusion", "reference", "bibliograph", "acknowledg",
        "performance",
    )
    method = [
        value for value in sentences
        if in_section(value, ("method", "approach", "model", "architecture", "algorithm", "controller", "policy", "action", "planning", "optimization", "training", "loss", "objective", "formulation", "construction", "implementation"))
        and not excluded(value, method_exclusions)
    ]
    if len(method) < 4:
        # OCR and older two-column PDFs do not always expose section headings;
        # their method is normally concentrated in the first half of the body.
        method = [
            value for value in sentences
            if value.page <= max(4, min(8, document["pages"] // 2 + 1))
            and not excluded(value, method_exclusions)
        ]

    evaluation = [
        value for value in sentences
        if in_section(value, ("experiment", "evaluation", "result", "dataset", "benchmark", "implementation", "analysis"))
        and not excluded(value, ("related work", "reference", "bibliograph", "acknowledg", "conclusion"))
    ]
    if len(evaluation) < 4:
        evaluation = [
            value for value in sentences
            if value.page >= max(1, document["pages"] // 3)
            and not excluded(value, ("related work", "literature", "reference", "bibliograph", "acknowledg", "conclusion"))
        ]
    if len(method) < 4:
        method = [value for value in sentences if not excluded(value, method_exclusions)] or sentences
    if len(evaluation) < 4:
        evaluation = [
            value for value in sentences
            if not excluded(value, ("related work", "literature", "reference", "bibliograph", "acknowledg", "conclusion"))
        ] or sentences
    interface_pool = [
        value for value in (intro + method)
        if not excluded(value, ("experiment", "evaluation", "result", "comparison", "ablation", "conclusion", "reference", "bibliograph", "acknowledg", "related work", "literature"))
    ]
    conclusion = [
        value for value in sentences
        if in_section(value, ("conclusion", "discussion", "limitation", "future", "failure"))
        and not excluded(value, ("reference", "bibliograph", "acknowledg"))
    ]
    if len(conclusion) < 2:
        conclusion = sentences[-min(80, len(sentences)):]
    return {
        "abstract": first_body_sentences(document),
        "problem": pick(
            intro,
            PROBLEM_TERMS,
            sections=("introduction", "background"),
            max_items=5,
            boost_terms=("challenge", "bottleneck", "limitation", "fails", "failure", "cannot", "lack", "gap", "however", "difficult", "restricted", "inefficient"),
        ),
        "changes": pick(
            intro + method[:80],
            CHANGE_TERMS,
            sections=("introduction", "method", "approach"),
            max_items=5,
            boost_terms=("we propose", "we introduce", "we present", "our framework", "our method", "contribution", "enables", "consists of"),
        ),
        "method": pick(
            method,
            METHOD_TERMS,
            sections=("method", "approach", "model", "architecture", "algorithm"),
            max_items=7,
            boost_terms=("takes as input", "outputs", "consists of", "we use", "we propose", "we introduce", "is composed", "first", "then"),
        ),
        "objective": pick(
            method,
            OBJECTIVE_TERMS,
            sections=("method", "algorithm", "optimization", "training", "loss", "formulation"),
            max_items=6,
            boost_terms=("loss", "objective", "minimiz", "maximiz", "reward", "cost", "constraint", "gradient", "equation", "update rule"),
        ),
        "interface": pick(
            interface_pool,
            INTERFACE_TERMS,
            sections=("method", "approach", "system", "problem", "preliminar"),
            max_items=7,
            boost_terms=("input", "output", "observation", "state", "action", "policy", "instruction", "feedback"),
        ),
        "temporal": pick(sentences, TEMPORAL_TERMS, sections=("method", "implementation", "experiment", "evaluation"), max_items=6),
        "dataset": pick(evaluation, DATASET_TERMS, sections=("dataset", "experiment", "evaluation", "benchmark"), max_items=8, boost_terms=("dataset", "benchmark", "split", "episodes", "scenes", "robot", "hardware", "real-world")),
        "metrics": pick(evaluation + captions, METRIC_TERMS, sections=("result", "evaluation", "experiment", "benchmark"), max_items=8, boost_terms=("success rate", "accuracy", "iou", "spl", "reward", "error", "score", "%")),
        "baseline": pick(evaluation + captions, BASELINE_TERMS, sections=("comparison", "experiment", "evaluation", "result"), max_items=7, boost_terms=("baseline", "compared", "outperform", "state-of-the-art", "oracle")),
        "ablation": pick(evaluation + captions, ABLATION_TERMS, sections=("ablation", "analysis", "experiment", "evaluation"), max_items=7, boost_terms=("ablation", "without", "remove", "variant", "sensitivity", "effect")),
        "results": pick(evaluation + captions, ("outperform", "achieve", "improve", "success", "accuracy", "results", "performance", "score"), sections=("result", "evaluation", "experiment"), max_items=8, boost_terms=("achieve", "outperform", "improve", "success rate", "%", "significantly")),
        "failure": pick(conclusion + evaluation + captions, FAILURE_TERMS, sections=("limitation", "failure", "discussion", "conclusion", "future"), max_items=7, boost_terms=("failure", "fails", "limitation", "cannot", "unstable", "collision", "slip", "fall")),
        "conclusion": conclusion,
        "repro": pick(method + evaluation, REPRO_TERMS, sections=("implementation", "experiment", "training", "evaluation"), max_items=8),
        "equations": pick(method, ("min", "max", "argmin", "argmax", "loss", "objective", "equation", "constraint", "update", "gradient"), max_items=8, boost_terms=("equation", "loss", "objective", "constraint", "gradient", "argmin", "argmax")),
        "numeric": numeric_cues(evaluation + method, 8),
        "captions": captions,
    }


def heading_list(document: dict[str, Any], keywords: Iterable[str]) -> list[str]:
    result = []
    for page, heading in document["headings"]:
        if any(keyword.casefold() in heading.casefold() for keyword in keywords):
            label = f"{heading} (p. {page})"
            if label not in result:
                result.append(label)
    return result[:12]


def get_scope(domain: str) -> tuple[str, str, str, str, str]:
    scope = DOMAIN_SCOPE.get(domain) or DOMAIN_SCOPE.get("general")
    if scope:
        return tuple(scope)  # type: ignore[return-value]
    return ("paper-defined system/task", "paper-defined input", "paper-defined state", "paper-defined output", "paper-defined outcome")


def get_formulation(domain: str) -> tuple[str, str, str, str]:
    return DOMAIN_FORMULATION.get(domain) or DOMAIN_FORMULATION["general"]


def get_runtime(domain: str) -> dict[str, str]:
    try:
        values = runtime_contract(domain, "")
        return {
            key: value.replace("본문 확인 필요", "exact value not recovered from the selected body cues")
            for key, value in values.items()
        }
    except (KeyError, TypeError):
        return {
            "horizon": "paper-specific horizon - see PDF temporal cues",
            "rate": "paper-specific rate - see PDF temporal cues",
            "memory": "paper-specific history/memory - see PDF temporal cues",
            "compute": "paper-specific compute/latency - see PDF reproduction cues",
            "training": "paper-specific training setup - see PDF method cues",
            "inference": "paper-specific inference setup - see PDF method cues",
        }


def body_evidence_label(record: dict[str, Any]) -> str:
    """Name the evidence source without calling an abstract/page a PDF body."""
    source_kind = str(record.get("source_kind") or "PDF")
    evidence_level = str(record.get("evidence_level") or "FULL_TEXT_CHECKED")
    if source_kind == "PDF":
        return "PDF body"
    if evidence_level == "ABSTRACT_CHECKED":
        return "abstract/source-page"
    return "official source body"


def note_header(kind: str, item: dict[str, Any], record: dict[str, Any]) -> str:
    canonical = item.get("page") or item.get("pdf") or "source URL not recorded"
    retrieval = record.get("url") or record.get("resolved_url") or item.get("pdf") or canonical
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
    if "chatpaper.com/api/v1/articles/download" in str(retrieval):
        retrieval_label = "public full-text mirror used for retrieval (canonical paper source retained)"
    elif "icdst.org" in str(retrieval):
        retrieval_label = "public full-text transcription mirror used for retrieval (canonical paper source retained)"
    else:
        retrieval_label = "PDF retrieval source" if source_kind == "PDF" else "body source"
    origin_note = (
        f" PDF provenance note: {record['pdf_origin']}."
        if record.get("pdf_origin")
        else ""
    )
    return (
        f"# {kind} - {item['title']}\n\n"
        "> Canonical metadata: [01_overview.md](./01_overview.md).\n"
        f"> Evidence maturity: {BT}{evidence_level}{BT}.\n"
        f"> Analysis basis: {basis}; "
        f"canonical paper source: {canonical}; {retrieval_label}: {retrieval}. "
        f"{origin_note} "
        f"The note is an evidence-anchored {evidence_label} analysis; {anchor_note}. "
        f"{boundary_note} "
        "Reading tracker status remains user-controlled; registry source evidence is reconciled separately.\n\n"
    )


def problem_note(item: dict[str, Any], domain: str, record: dict[str, Any], ev: dict[str, list[Evidence]], document: dict[str, Any]) -> str:
    scope = get_scope(domain)
    evidence_label = body_evidence_label(record)
    state, action, objective, success = get_formulation(domain)
    problem = ev["problem"] or ev["abstract"][:2]
    changes = ev["changes"] or ev["method"][:2]
    interface = ev["interface"][:4]
    failures = ev["failure"][:4]
    assumption_rows = [
        [f"body cue at p. {value.page}", short_cue(value.text, 18), "reported limitation/failure wording; scope must be verified"]
        for value in failures
    ] or [["no explicit assumption/failure cue", "domain stress test only", "not a paper claim"]]
    problem_sentence = short_cue(problem[0].text, 30) if problem else f"{evidence_label} problem statement was not recovered."
    change_sentence = short_cue(changes[0].text, 30) if changes else f"{evidence_label} contribution statement was not recovered."
    state_terms = ", ".join(body_terms(interface + problem, 10)) or "paper-specific state terms not recovered"
    equation_anchor = anchor(ev["equations"], "no optimization/equation sentence selected")
    return (
        note_header("Problem", item, record)
        + "## Problem in One Sentence\n\n"
        + f"{evidence_label} framing ({anchor(problem, 'p. 1-2')}): {problem_sentence}\n\n"
        + "## PDF Body Digest\n\n"
        + cue_lines(combined_evidence(ev["abstract"], problem, changes, limit=7), "abstract/introduction body cue 없음", 7)
        + "\n\n"
        + "## System and Scope\n\n"
        + md_table(
            ["Dimension", f"{evidence_label} evidence", "Registry/robotics interpretation", "Boundary"],
            [
                ["Target problem", short_cue(problem[0].text, 22) if problem else "problem cue 없음", scope[0], "body wording is the source claim"],
                ["Observation / input", short_cue(interface[0].text, 22) if interface else "input cue 없음", scope[1], f"exact sensor/frame/preprocessing from {evidence_label}"],
                ["State / latent", state_terms, scope[2], "notation and tensor shape require body check"],
                ["Output / action", ", ".join(body_terms(interface[2:] + changes, 8)) or "not recovered", scope[3], "exact unit/frame/decoder require body check"],
                ["Target outcome", success, scope[4], "metric/denominator are in 04 evidence"],
            ],
        )
        + "\n\n## Formal Problem Formulation\n\n"
        + md_table(
            ["Formulation field", f"{evidence_label}-grounded record", "Evidence anchor"],
            [
                ["State / observation variable", f"{state}; body terms: {state_terms}", anchor(interface[:3])],
                ["Decision / output variable", f"{action}; body terms: {', '.join(body_terms(changes + interface, 8)) or 'not recovered'}", anchor(changes[:3])],
                ["Objective / loss / cost", f"{objective}; cue terms: {', '.join(body_terms(ev['objective'] + ev['equations'], 8)) or 'not recovered'}", equation_anchor],
                ["Constraint / feasibility", "paper-specific constraints are recorded only where the body states them; otherwise unresolved", anchor(ev["objective"][-3:])],
                ["Success / guarantee", success, anchor(ev["metrics"][:3] or ev["results"][:3])],
            ],
        )
        + f"\n\n- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited {evidence_label} anchors.\n\n"
        + "## Bottleneck in Prior Work\n\n"
        + cue_lines(problem[1:] or problem, "introductory bottleneck cue 없음 - inspect Introduction and Related Work")
        + "\n\n## What the Paper Changes\n\n"
        + f"{evidence_label} contribution framing ({anchor(changes, 'Introduction/Method')}): {change_sentence}\n\n"
        + cue_lines(changes[1:], "additional contribution cue 없음", 4)
        + "\n\n## Assumptions and Failure Boundary\n\n"
        + md_table(["Body anchor", "Observed limitation/failure cue", "Interpretation boundary"], assumption_rows)
        + "\n\n- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.\n\n"
        + "## Position in the Robotics Loop\n\n"
        + f"{domain} writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. "
        + f"Evidence interface anchors: {anchor(interface, 'no interface anchor')}. The downstream handoff is claimed only when the body describes it.\n\n"
        + "## Verification Questions\n\n"
        + f"- **Evidence anchors reviewed:** problem {anchor(problem)}, interface {anchor(interface)}, objective {equation_anchor}.\n"
        + "- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?\n"
        + "- What are the observation frame, state memory, output/action frame, horizon and termination rule?\n"
        + "- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?\n"
        + "- Does the evaluation measure the stated target, or only an upstream proxy?\n"
    )


def method_note(item: dict[str, Any], domain: str, record: dict[str, Any], ev: dict[str, list[Evidence]], document: dict[str, Any]) -> str:
    scope = get_scope(domain)
    evidence_label = body_evidence_label(record)
    formulation = get_formulation(domain)
    runtime = get_runtime(domain)
    method = ev["method"] or ev["changes"]
    objective = ev["objective"] or ev["equations"]
    interface = ev["interface"]
    temporal = ev["temporal"]
    method_section_list = heading_list(document, ("method", "approach", "model", "architecture", "algorithm", "controller", "policy"))
    method_sentence = short_cue(method[0].text, 30) if method else f"{evidence_label} method statement was not recovered."
    modules = DOMAIN_MODULES.get(domain) or DOMAIN_MODULES.get("general")
    pipeline_rows = []
    for index, module in enumerate(modules[:3]):
        module_cue = method[index:index + 2] or method[:1]
        pipeline_rows.append([module[0], module[1], module[2], module[3], module[4], short_cue(module_cue[0].text, 22) if module_cue else "module cue 없음", anchor(module_cue, "no anchor")])
    temporal_numbers = numeric_cues(temporal + ev["repro"], 5)
    interface_terms = ", ".join(body_terms(interface, 14)) or "paper-specific terms not recovered"
    train_infer = [
        value for value in ev["method"] + ev["repro"]
        if any(term in value.text.casefold() for term in ("train", "pretrain", "inference", "online", "rollout", "fine-tun"))
    ]
    return (
        note_header("Method", item, record)
        + "## Method in One Sentence\n\n"
        + f"{evidence_label} method statement ({anchor(method, 'Method/Approach')}): {method_sentence}\n\n"
        + "## Method Body Digest\n\n"
        + cue_lines(combined_evidence(method, objective, interface, limit=10), "method body cue 없음", 8)
        + "\n\n"
        + "## Design Rationale\n\n"
        + cue_lines(ev["changes"][:3] or ev["problem"][:3], "design rationale cue 없음", 4)
        + "\n\n## Source Evidence Cues\n\n"
        + cue_lines(method, "method section cue 없음", 7)
        + (f"\n- **Detected method headings:** {'; '.join(method_section_list)}" if method_section_list else "\n- **Detected method headings:** none reliably recovered")
        + "\n\n## Pipeline\n\n"
        + md_table(["Module", "Purpose", "Input", "Operation", "Output", f"{evidence_label} cue", "Anchor"], pipeline_rows)
        + "\n\n- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.\n\n"
        + "## Objective / Update Rule\n\n"
        + cue_lines(objective, "objective/update cue 없음 - inspect equations and algorithm boxes", 6)
        + f"\n- **Formal bridge:** {formulation[0]} -> {formulation[1]} -> {formulation[2]} -> {formulation[3]}.\n"
        + f"- **Equation/algorithm anchors:** {anchor(ev['equations'], 'none selected')}.\n"
        + "- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.\n\n"
        + "## Variables and Parameters\n\n"
        + md_table(
            ["Role", "PDF-derived terms", "Normalized robotics interpretation", "Status"],
            [
                ["Input/observation", interface_terms, scope[1], "body cue; exact tensor/frame verify"],
                ["State/latent", ", ".join(body_terms(ev["interface"] + ev["method"], 10)) or "not recovered", scope[2], "body cue; notation verify"],
                ["Action/output", ", ".join(body_terms(ev["changes"] + ev["interface"], 10)) or "not recovered", scope[3], "body cue; unit/decoder verify"],
                ["Objective/constraint", ", ".join(body_terms(objective, 10)) or "not recovered", formulation[2], "equation anchor required"],
            ],
        )
        + "\n\n## Observation–State–Action Interface\n\n"
        + cue_lines(interface, "observation/state/action interface cue 없음", 7)
        + f"\n- **Normalized interface:** observation={scope[1]}; state={scope[2]}; output/action={scope[3]}.\n"
        + "- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.\n\n"
        + "## Temporal and Runtime Contract\n\n"
        + md_table(
            ["Contract", "Generic domain prior", f"{evidence_label} cue", "Unresolved detail"],
            [
                ["Horizon", runtime.get("horizon", "not resolved"), short_cue(temporal[0].text, 22) if temporal else "not recovered", "episode/sequence/action-chunk boundary"],
                ["Rate / latency", runtime.get("rate", "not resolved"), short_cue(temporal[1].text, 22) if len(temporal) > 1 else "not recovered", "Hz/fps, inference time and control rate"],
                ["Memory", runtime.get("memory", "not resolved"), short_cue(next((v.text for v in temporal if "history" in v.text.casefold() or "memory" in v.text.casefold()), "not recovered"), 22), "window and reset"],
                ["Compute", runtime.get("compute", "not resolved"), short_cue(temporal_numbers[0].text, 22) if temporal_numbers else "not recovered", "hardware, batch and throughput"],
            ],
        )
        + "\n\n## Training vs Inference\n\n"
        + cue_lines(train_infer, "training/inference separation cue 없음", 6)
        + "\n\n- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.\n\n"
        + "## Method-Specific Formal Details\n\n"
        + "- **Body-defined terms:** " + (", ".join(body_terms(method + objective + interface, 20)) or "not recovered") + ".\n"
        + f"- **Relevant PDF headings:** {'; '.join(method_section_list) if method_section_list else 'not reliably recovered'}.\n"
        + "- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.\n\n"
        + "## Evaluation Link\n\n"
        + md_table(
            ["Method component", "Evaluation evidence to inspect", "PDF anchor"],
            [
                [modules[0][0], short_cue((ev["dataset"] + ev["metrics"])[0].text, 22) if ev["dataset"] + ev["metrics"] else "no linked eval cue", anchor((ev["dataset"] + ev["metrics"])[:2])],
                [modules[1][0], short_cue((ev["baseline"] + ev["ablation"])[0].text, 22) if ev["baseline"] + ev["ablation"] else "no linked comparison cue", anchor((ev["baseline"] + ev["ablation"])[:2])],
                [modules[2][0], short_cue((ev["results"] + ev["failure"])[0].text, 22) if ev["results"] + ev["failure"] else "no linked outcome cue", anchor((ev["results"] + ev["failure"])[:2])],
            ],
        )
        + "\n\n## Failure and Ablation Link\n\n"
        + cue_lines(ev["ablation"] + ev["failure"], "ablation/failure cue 없음", 7)
        + "\n\n- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.\n\n"
        + "## Reproduction Checklist\n\n"
        + "1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.\n"
        + "2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.\n"
        + "3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.\n"
        + "4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.\n"
        + "5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.\n\n"
        + "## Verification Questions\n\n"
        + f"- **Evidence anchors reviewed:** method {anchor(method)}, objective {anchor(objective)}, temporal {anchor(temporal)}.\n"
        + "- Which module is genuinely new, and which is inherited infrastructure or a baseline?\n"
        + "- What exact computation consumes each observation and emits each action/output?\n"
        + "- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?\n"
        + "- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?\n"
    )


def evaluation_type(item: dict[str, Any], domain: str, ev: dict[str, list[Evidence]]) -> str:
    if domain == "benchmark" or str(item.get("paper_type", "")) == "benchmark_or_dataset":
        return "BENCHMARK / DATASET"
    body_text = " ".join(value.text for value in ev["dataset"] + ev["results"]).casefold()
    if any(token in body_text for token in ("real robot", "real-world", "physical robot", "hardware")):
        return "EMPIRICAL / REAL-ROBOT OR HARDWARE"
    if "simulat" in body_text or "simulator" in body_text:
        return "EMPIRICAL / SIMULATION"
    if not ev["dataset"] and not ev["metrics"] and not ev["results"]:
        return "THEORY / ANALYTIC OR SCOPE UNRESOLVED"
    if any("experiment" in value.section.casefold() or "evaluation" in value.section.casefold() or "result" in value.section.casefold() for value in ev["results"]):
        return "EMPIRICAL / SOURCE-REPORTED EVALUATION"
    return "SYSTEM / EVALUATION SCOPE UNRESOLVED"


def evaluation_note(item: dict[str, Any], domain: str, record: dict[str, Any], ev: dict[str, list[Evidence]], document: dict[str, Any]) -> str:
    scope = get_scope(domain)
    evidence_label = body_evidence_label(record)
    etype = evaluation_type(item, domain, ev)
    dataset, metrics = ev["dataset"], ev["metrics"]
    baselines, ablations = ev["baseline"], ev["ablation"]
    results = ev["results"] or ev["numeric"]
    failures, repro = ev["failure"], ev["repro"]
    eval_sections = heading_list(document, ("experiment", "evaluation", "result", "dataset", "benchmark", "implementation"))
    matrix_values = results[:5] or dataset[:3] or ev["abstract"][:2]
    matrix_rows = [[value.section, etype, short_cue(value.text, 24), anchor([value])] for value in matrix_values]
    if not matrix_rows:
        matrix_rows = [["no experiment cue", etype, "body experiment statement not recovered", "verify PDF"]]
    metric_rows = [[short_cue(value.text, 24), "definition/direction/unit from same section", anchor([value])] for value in metrics[:8]]
    if not metric_rows:
        metric_rows = [["no metric sentence selected", "not reported; do not infer from keyword", "verify Results/Evaluation"]]
    baseline_rows = [[short_cue(value.text, 24), "comparison identity and matched condition", anchor([value])] for value in baselines[:6]]
    if not baseline_rows:
        baseline_rows = [["no baseline sentence selected", "not reported", "verify comparison table"]]
    ablation_rows = [[short_cue(value.text, 24), "component/input/data sensitivity", anchor([value])] for value in ablations[:6]]
    if not ablation_rows:
        ablation_rows = [["no ablation sentence selected", "not reported; proposed stress test only", "verify ablation section"]]
    numeric_rows = [[short_cue(value.text, 26), anchor([value])] for value in ev["numeric"][:6]]
    if not numeric_rows:
        numeric_rows = [["no numeric result/condition sentence selected", "verify tables/figures"]]
    failure_rows = [["body limitation/failure cue", short_cue(value.text, 24), anchor([value])] for value in failures[:6]]
    if not failure_rows:
        failure_rows = [["no explicit failure cue selected", "unreported; domain stress test remains open", "verify Discussion/Conclusion"]]
    repro_rows = [[short_cue(value.text, 24), anchor([value])] for value in repro[:8]]
    if not repro_rows:
        repro_rows = [["no implementation/reproducibility sentence selected", "verify appendix and code/project"]]
    result_sentence = short_cue(results[0].text, 30) if results else "evaluation statement was not recovered."
    claim_sentence = short_cue((ev["changes"] or ev["abstract"] or [Evidence(0, "", "paper contribution")])[0].text, 24)
    return (
        note_header("Evaluation", item, record)
        + "## Evaluation in One Sentence\n\n"
        + f"{evidence_label} evaluation/result cue ({anchor(results, 'Evaluation/Results')}): {result_sentence}\n\n"
        + "## Evaluation Body Digest\n\n"
        + cue_lines(combined_evidence(dataset, metrics, results, failures, limit=12), "evaluation body cue 없음", 8)
        + "\n\n"
        + "## Evaluation Type and Scope\n\n"
        + f"- **Evaluation type:** {BT}{etype}{BT}.\n"
        + f"- **Target system/task:** {scope[0]}.\n"
        + f"- **Input boundary:** {scope[1]}.\n"
        + f"- **Output/decision under evaluation:** {scope[3]}.\n"
        + f"- **Primary target:** {scope[4]}.\n"
        + f"- **Detected evaluation headings:** {'; '.join(eval_sections) if eval_sections else 'not reliably recovered'}.\n\n"
        + "## Experimental Matrix\n\n"
        + md_table(["Body section", "Type", f"{evidence_label} experiment/result cue", "Anchor"], matrix_rows)
        + "\n\n## Dataset / Benchmark Role\n\n"
        + cue_lines(dataset, "dataset/benchmark/environment role cue 없음", 8)
        + "\n\n- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.\n\n"
        + "## Figures / Tables as Body Evidence\n\n"
        + cue_lines(ev["captions"], "figure/table caption cue 없음", 8)
        + "\n\n"
        + "## Embodiment / Environment\n\n"
        + md_table(
            ["Dimension", f"{evidence_label}-grounded cue", "Unresolved condition", "Anchor"],
            [
                ["Robot/hardware/simulator", short_cue(dataset[0].text, 24) if dataset else "not recovered", "embodiment, simulator version and control stack", anchor(dataset[:2])],
                ["Task/environment", short_cue(dataset[1].text, 24) if len(dataset) > 1 else "not recovered", "reset, timeout, object/scene variation", anchor(dataset[1:3])],
                ["Observation/sensor", scope[1], "calibration, preprocessing, privileged input", anchor(ev["interface"][:2])],
                ["Output/decision", scope[3], "action frame, controller and termination", anchor(ev["interface"][2:4])],
            ],
        )
        + "\n\n## Metrics and Success Definition\n\n"
        + md_table(["Metric/result evidence", "Definition and aggregation to verify", "Anchor"], metric_rows)
        + "\n\n- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.\n\n"
        + "## Baselines and Fairness\n\n"
        + md_table(["PDF baseline/comparison cue", "Fair comparison field", "Anchor"], baseline_rows)
        + "\n\n"
        + md_table(
            ["Fairness dimension", "Required matched condition"],
            [
                ["Observation/action", "sensor modality, frame, preprocessing, action space and controller"],
                ["Data", "training split, demonstrations, pretraining, labels and leakage"],
                ["Compute", "parameter budget, inference steps, hardware, latency and control rate"],
                ["Protocol", "reset/timeout, seeds, trials, held-out variation and success denominator"],
            ],
        )
        + "\n\n## Ablations and Sensitivity\n\n"
        + md_table(["PDF ablation/sensitivity cue", "What it isolates", "Anchor"], ablation_rows)
        + "\n\n## Main Results / Claim–Evidence Map\n\n"
        + md_table(
            ["Claim or target", "Result/condition cue", "Evidence strength", "Anchor"],
            [
                [claim_sentence, short_cue(results[0].text, 24) if results else "no result cue", f"{evidence_label} cue; verify exact table/figure and matched conditions", anchor(results)],
                ["Primary metric/result", short_cue(results[1].text, 24) if len(results) > 1 else "not separately recovered", "numeric claim only at cited anchor", anchor(results[1:2])],
            ],
        )
        + "\n\n- Numeric sentences retained from the body:\n"
        + cue_lines(ev["numeric"], "no numeric body cue", 6)
        + "\n\n## Generalization and Failure Cases\n\n"
        + md_table(["Body cue type", "Observed cue or missing regime", "Anchor"], failure_rows)
        + "\n\n- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.\n\n"
        + "## Statistics, Efficiency, and Reproducibility\n\n"
        + md_table(["Body reproducibility cue", "Anchor"], repro_rows)
        + "\n\n"
        + md_table(
            ["Audit field", "Current status"],
            [
                ["Trials/episodes/seeds", "use only body sentences above; otherwise not reported"],
                ["Mean/standard deviation/confidence interval", "use only body table/figure; otherwise not reported"],
                ["Latency/throughput", "separate inference latency, control rate and simulator throughput"],
                ["Train/eval split/leakage", "verify dataset/protocol section"],
                ["Code/checkpoint/environment", "see 01_overview.md; not duplicated as evidence"],
            ],
        )
        + "\n\n## Limitations and Verification Questions\n\n"
        + cue_lines(failures, "explicit limitation/failure sentence not recovered", 6)
        + "\n\n"
        + f"- **Evidence anchors reviewed:** datasets {anchor(dataset)}, metrics {anchor(metrics)}, baselines {anchor(baselines)}, results {anchor(results)}.\n"
        + "- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?\n"
        + "- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?\n"
        + "- What negative result or untested regime does the paper leave open?\n"
    )


def load_items() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, str]]]:
    papers = {item["paper_id"]: item for item in json.loads(PAPERS.read_text(encoding="utf-8"))}
    with TIERS.open(newline="", encoding="utf-8") as handle:
        tiers = {row["paper_id"]: row for row in csv.DictReader(handle)}
    return papers, tiers


def load_download_manifest(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        raise SystemExit(f"download manifest is missing: {path}")
    result = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            record = json.loads(line)
            result[record["paper_id"]] = record
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-dir", type=Path, default=DEFAULT_PDF_DIR)
    parser.add_argument("--download-manifest", type=Path, default=None)
    parser.add_argument("--review-manifest", type=Path, default=DEFAULT_REVIEW_MANIFEST)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--start", type=int, default=0)
    args = parser.parse_args()

    pdf_dir = args.pdf_dir if args.pdf_dir.is_absolute() else ROOT / args.pdf_dir
    download_manifest_path = args.download_manifest or (pdf_dir / "download_manifest.jsonl")
    if not download_manifest_path.is_absolute():
        download_manifest_path = ROOT / download_manifest_path
    papers, tiers = load_items()
    selected = [
        papers[paper_id]
        for paper_id, row in sorted(tiers.items())
        if row["tier"] not in {"CORE", "NEXT"}
    ]
    if args.start:
        selected = selected[args.start:]
    if args.limit:
        selected = selected[:args.limit]
    download_records = load_download_manifest(download_manifest_path)
    missing = [
        item["paper_id"]
        for item in selected
        if download_records.get(item["paper_id"], {}).get("status") not in {"downloaded", "reused"}
        or not (pdf_dir / f"{item['paper_id']}.pdf").exists()
    ]
    if missing:
        print({"mode": "apply" if args.apply else "dry-run", "missing_fulltext": len(missing), "sample": missing[:20]})
        return 2

    review_records: list[dict[str, Any]] = []
    outputs: list[tuple[Path, str]] = []
    domain_counts: Counter[str] = Counter()
    quality_counts: Counter[str] = Counter()
    for index, item in enumerate(selected, start=1):
        record = dict(download_records[item["paper_id"]])
        pdf_path = pdf_dir / f"{item['paper_id']}.pdf"
        document = extract_document(pdf_path)
        document["paper_title"] = item["title"]
        evidence = infer_evidence(document)
        domain = infer_domain(item, tiers[item["paper_id"]])
        domain_counts[domain] += 1
        quality_counts[document["extraction_quality"]] += 1
        record.update({
            "tier": tiers[item["paper_id"]]["tier"],
            "track": tiers[item["paper_id"]].get("primary_track", ""),
            "domain": domain,
            "pages": document["pages"],
            "text_chars": document["text_chars"],
            "extraction_method": document["extraction_method"],
            "extraction_quality": document["extraction_quality"],
            "title_token_overlap_first_two_pages": title_token_overlap(item["title"], document),
            "section_heading_count": len(document["headings"]),
            "evidence_counts": {key: len(value) for key, value in evidence.items()},
            "note_basis": "full-text PDF body with page-aware extractive cues",
            "reviewed_on": date.today().isoformat(),
        })
        review_records.append(record)
        folder = resolve_folder(unquote(item["folder"]))
        outputs.extend([
            (folder / "02_problem.md", problem_note(item, domain, record, evidence, document)),
            (folder / "03_method.md", method_note(item, domain, record, evidence, document)),
            (folder / "04_evaluation.md", evaluation_note(item, domain, record, evidence, document)),
        ])
        if index % 25 == 0 or index == len(selected):
            print(f"[{index}/{len(selected)}] extracted and rendered; domain={domain}", flush=True)

    print({
        "mode": "apply" if args.apply else "dry-run",
        "selected": len(selected),
        "note_file_updates": len(outputs),
        "domain_counts": dict(domain_counts),
        "extraction_quality": dict(quality_counts),
    })
    if not args.apply:
        return 0

    for path, content in outputs:
        path.write_text(content.rstrip() + "\n", encoding="utf-8")
    review_path = args.review_manifest if args.review_manifest.is_absolute() else ROOT / args.review_manifest
    review_path.parent.mkdir(parents=True, exist_ok=True)
    review_payload = {
        "review_date": date.today().isoformat(),
        "scope": "non-CORE/NEXT papers selected from READING_TIERS.csv",
        "paper_count": len(review_records),
        "note_file_count": len(outputs),
        "pdf_cache": str(pdf_dir.relative_to(ROOT)),
        "tracker_changed": False,
        "records": review_records,
    }
    review_path.write_text(json.dumps(review_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
