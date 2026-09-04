#!/usr/bin/env python3
"""Shared schema helpers for the PaperReview machine-readable registry.

The manifest deliberately remains a JSON list for backwards compatibility.
This module adds structured identity, publication, source, taxonomy, curation,
and provenance fields without treating a local PDF as evidence of reading.
"""

from __future__ import annotations

import re
import urllib.parse
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "1.0"
MIGRATION_DATE = "2026-09-01"

PRIMARY_TRACKS = (
    "Planning and control",
    "RL, IL, offline learning, and robot data",
    "Manipulation, contact, tactile, and dexterity",
    "VLA and generalist robot policies",
    "World models, safety, uncertainty, and recovery",
    "Locomotion, whole-body, mobile manipulation, and humanoids",
    "Robotics-enabling 3D perception",
)

PRESENTATIONS = {"unknown", "poster", "oral", "spotlight", "regular"}
PUBLICATION_KINDS = {
    "conference",
    "journal",
    "workshop",
    "preprint",
    "technical_report",
    "other",
}
PUBLICATION_STATUSES = {"peer_reviewed", "preprint", "technical_report", "unverified"}
CODE_STATUSES = {"released", "project_only", "not_released", "not_identified"}
DATA_STATUSES = {"released", "not_released", "not_identified", "not_recorded", "not_applicable"}

# These are intentionally small controlled vocabularies.  They are used for
# navigation and filtering, not as substitutes for paper-level evidence.
CURATION_ROLES = {
    "foundation",
    "method",
    "system",
    "benchmark_or_dataset",
}
FACET_KEYS = {
    "embodiment",
    "modality",
    "learning",
    "control_level",
    "setting",
    "interaction",
}

# Full venue names and legacy abbreviations cannot be classified reliably by
# substring matching alone.  Keep the override table local to the registry so
# the same mapping is used by registration, normalization, and audit.
VENUE_KIND_OVERRIDES = {
    "ieee robotics and automation letters": "journal",
    "nature": "journal",
    "nature machine intelligence": "journal",
    "robotics: science and systems": "conference",
    "naacl": "conference",
    "tmlr": "journal",
    "aistats": "conference",
    "emnlp": "conference",
    "ieee jra": "journal",
    "ieee t-ra": "journal",
    "ijhr": "journal",
    "icaps": "conference",
    "ijcai": "conference",
}

VENUE_IDS = {
    "arxiv": "arxiv",
    "neurips": "neurips",
    "iclr": "iclr",
    "icml": "icml",
    "cvpr": "cvpr",
    "eccv": "eccv",
    "iccv": "iccv",
    "icra": "icra",
    "iros": "iros",
    "rss": "rss",
    "robotics: science and systems": "rss",
    "corl": "corl",
    "ral": "ral",
    "ieee robotics and automation letters": "ral",
    "t-ro": "t-ro",
    "ijrr": "ijrr",
    "science robotics": "science-robotics",
    "nature": "nature",
    "nature machine intelligence": "nature-machine-intelligence",
    "tmlr": "tmlr",
    "aistats": "aistats",
    "emnlp": "emnlp",
    "naacl": "naacl",
    "icaps": "icaps",
    "ijcai": "ijcai",
}

DETAILED_TRACK_TO_PRIMARY = {
    "Planning, control, and whole-body foundations": "Planning and control",
    "Planning, control, simulation, and TAMP extensions": "Planning and control",
    "RL, IL, and policy learning foundations": "RL, IL, offline learning, and robot data",
    "RL, IL, offline learning, and robot data": "RL, IL, offline learning, and robot data",
    "Manipulation, contact, tactile, and dexterity": "Manipulation, contact, tactile, and dexterity",
    "Contact-rich, deformable, force, and dexterous manipulation": "Manipulation, contact, tactile, and dexterity",
    "VLA and generalist robot policies": "VLA and generalist robot policies",
    "VLA, cross-embodiment, and long-horizon planning": "VLA and generalist robot policies",
    "World models, uncertainty, failure detection, and recovery": "World models, safety, uncertainty, and recovery",
    "Safety and robot world models": "World models, safety, uncertainty, and recovery",
    "Locomotion, whole-body control, mobile manipulation, and humanoids": "Locomotion, whole-body, mobile manipulation, and humanoids",
    "Locomotion, mobile manipulation, and humanoid systems": "Locomotion, whole-body, mobile manipulation, and humanoids",
    "Active and embodied 3D Vision": "Robotics-enabling 3D perception",
    "Robotics-enabling 3D perception": "Robotics-enabling 3D perception",
}


def _text(value: Any) -> str:
    return str(value or "").strip()


def canonical_venue(value: Any) -> str:
    """Return a venue-only label while preserving the raw label separately."""

    raw = _text(value)
    if raw.casefold() == "arxiv":
        return "arXiv"
    label = re.sub(r"\b20\d{2}\b", "", raw)
    label = re.sub(r"\bSpotlightPoster\b", "", label, flags=re.IGNORECASE)
    label = re.sub(r"\b(?:poster|spotlight|oral|regular)\b", "", label, flags=re.IGNORECASE)
    label = re.sub(r"\s+", " ", label).strip(" -_/")
    if label.casefold() == "arxiv":
        return "arXiv"
    return label or raw or "Unknown"


def venue_year(value: Any) -> int | None:
    match = re.search(r"\b(20\d{2})\b", _text(value))
    return int(match.group(1)) if match else None


def presentation_from_venue(value: Any) -> str:
    raw = _text(value).casefold()
    if "spotlight" in raw:
        return "spotlight"
    if re.search(r"\boral\b", raw):
        return "oral"
    if re.search(r"\bposter\b", raw) or "spotlightposter" in raw:
        return "poster"
    if re.search(r"\bregular\b", raw):
        return "regular"
    return "unknown"


def publication_kind(venue: str) -> str:
    label = venue.casefold()
    if label in VENUE_KIND_OVERRIDES:
        return VENUE_KIND_OVERRIDES[label]
    if label == "arxiv":
        return "preprint"
    if "technical report" in label or label in {"tech report", "report"}:
        return "technical_report"
    if "workshop" in label:
        return "workshop"
    journal_markers = (
        "journal",
        "transactions",
        "ra-l",
        "t-ro",
        "t-its",
        "tac",
        "ijrr",
        "jmlr",
        "autonomous robots",
        "machine learning",
        "neural computation",
        "artificial intelligence",
        "science robotics",
        "sensors",
        "tog",
    )
    if any(marker in label for marker in journal_markers):
        return "journal"
    conference_markers = (
        "icra",
        "iros",
        "rss",
        "corl",
        "neurips",
        "iclr",
        "icml",
        "cvpr",
        "eccv",
        "iccv",
        "3dv",
        "aaai",
        "isrr",
        "ismar",
        "wacv",
        "siggraph",
        "nips",
    )
    if any(marker in label for marker in conference_markers):
        return "conference"
    return "other"


def venue_id_for(venue: str) -> str:
    """Return a stable compact venue key without creating another venue catalog."""

    label = _text(venue).casefold()
    if label in VENUE_IDS:
        return VENUE_IDS[label]
    value = re.sub(r"[^a-z0-9]+", "-", label).strip("-")
    return value or "unknown"


def publication_status(kind: str, venue: str) -> str:
    if kind == "preprint":
        return "preprint"
    if kind == "technical_report":
        return "technical_report"
    if kind in {"conference", "journal", "workshop"}:
        return "peer_reviewed"
    return "unverified"


def _clean_identifier(value: str) -> str:
    return value.strip().rstrip(".,;:)").strip()


def extract_identifiers(*urls: Any) -> dict[str, str]:
    """Extract stable public identifiers from URLs without network lookup."""

    identifiers: dict[str, str] = {}
    for value in urls:
        url = _text(value)
        if not url:
            continue
        arxiv = re.search(
            r"arxiv\.org/(?:abs|pdf|html)/([A-Za-z0-9][A-Za-z0-9.\-]*(?:v\d+)?)",
            url,
            flags=re.IGNORECASE,
        )
        if arxiv and "arxiv" not in identifiers:
            identifier = _clean_identifier(arxiv.group(1))
            identifier = re.sub(r"v\d+$", "", identifier, flags=re.IGNORECASE)
            identifiers["arxiv"] = identifier
        doi = re.search(r"(?:doi\.org/|\bdoi:\s*)(10\.\d{4,9}/[^\s\"<>]+)", url, flags=re.IGNORECASE)
        if doi and "doi" not in identifiers:
            identifiers["doi"] = _clean_identifier(doi.group(1))
        openreview = re.search(r"openreview\.net/(?:forum|pdf|attachment)\?id=([^&#]+)", url, flags=re.IGNORECASE)
        if openreview and "openreview" not in identifiers:
            identifiers["openreview"] = urllib.parse.unquote(_clean_identifier(openreview.group(1)))
    return identifiers


def source_kind(url: Any) -> str | None:
    value = _text(url)
    if not value:
        return None
    if not re.match(r"https?://", value, flags=re.IGNORECASE):
        return "unverified"
    host = urllib.parse.urlparse(value).netloc.casefold()
    if "arxiv.org" in host:
        return "arxiv"
    if "openreview.net" in host:
        return "openreview"
    if "thecvf.com" in host or "openaccess.thecvf.com" in host:
        return "cvf"
    if "proceedings.mlr.press" in host:
        return "pmlr"
    if "doi.org" in host:
        return "doi"
    if "github.com" in host or "gitlab.com" in host or "bitbucket.org" in host:
        return "code"
    return "publisher_or_project"


def _source(url: Any, role: str) -> dict[str, str] | None:
    value = _text(url)
    if not value or value.casefold().startswith("not identified") or value.casefold() == "not released":
        return None
    return {"url": value, "kind": source_kind(value) or role}


def artifact_code_status(project: Any) -> str:
    value = _text(project)
    lowered = value.casefold()
    if not value or lowered.startswith("not identified"):
        return "not_identified"
    if lowered == "not released":
        return "not_released"
    if re.search(r"https?://(?:www\.)?(?:github|gitlab|bitbucket)\.", value, flags=re.IGNORECASE):
        return "released"
    if re.match(r"https?://", value, flags=re.IGNORECASE):
        return "project_only"
    return "not_identified"


def _keyword_text(item: dict[str, Any]) -> str:
    return " ".join(
        [
            _text(item.get("title")),
            _text(item.get("category")),
            " ".join(_text(tag) for tag in item.get("tags", [])),
        ]
    ).casefold()


def primary_track_for(
    category: Any = "",
    tags: list[str] | None = None,
    detailed_track: str | None = None,
    title: Any = "",
) -> str | None:
    if detailed_track in DETAILED_TRACK_TO_PRIMARY:
        return DETAILED_TRACK_TO_PRIMARY[detailed_track]
    text = " ".join([_text(category), _text(title), " ".join(_text(x) for x in (tags or []))]).casefold()
    ordered = [
        (("vla", "vision-language-action", "generalist policy", "robot policy"), PRIMARY_TRACKS[3]),
        (("world model", "world models", "safety", "uncertainty", "failure detection", "recovery"), PRIMARY_TRACKS[4]),
        (("locomotion", "humanoid", "whole-body", "whole body", "mobile manipulation", "legged"), PRIMARY_TRACKS[5]),
        (("tactile", "contact", "dexter", "manipulation", "grasp", "force control"), PRIMARY_TRACKS[2]),
        (("planning", "control", "tamp", "trajectory", "motion planning", "mpc"), PRIMARY_TRACKS[0]),
        (("reinforcement learning", "imitation learning", "offline rl", "robot learning", "robot data", "sim-to-real", "policy learning"), PRIMARY_TRACKS[1]),
        (("3d", "3d vision", "point cloud", "slam", "scene graph", "neural field", "geometry", "perception", "mapping"), PRIMARY_TRACKS[6]),
    ]
    for needles, track in ordered:
        if any(needle in text for needle in needles):
            return track
    return None


def paper_type_for(item: dict[str, Any]) -> str:
    text = _keyword_text(item)
    if any(word in text for word in ("benchmark", "dataset", "suite", "evaluation framework")):
        return "benchmark_or_dataset"
    if any(word in text for word in ("theory", "formal basis", "foundations", "foundation", "control law")):
        return "theory_or_foundation"
    if any(word in text for word in ("system", "framework", "simulator", "engine")):
        return "system"
    return "method"


def _note_evidence(root: Path | None, folder: str) -> str | None:
    if root is None:
        return None
    for name in ("05_insights.md", "01_overview.md"):
        path = root / folder / name
        if not path.exists():
            continue
        match = re.search(r"Evidence maturity:\s*`([^`]+)`", path.read_text(encoding="utf-8", errors="ignore"))
        if match and match.group(1) in {"CURATION_ONLY", "ABSTRACT_CHECKED", "FULL_TEXT_CHECKED", "EXPERIMENT_CHECKED"}:
            return match.group(1)
    return None


def _note_source_audit(root: Path | None, folder: str) -> str | None:
    if root is None:
        return None
    path = root / folder / "01_overview.md"
    if not path.exists():
        return None
    match = re.search(r"^- Source audit:\s*(.+)$", path.read_text(encoding="utf-8", errors="ignore"), flags=re.MULTILINE)
    return match.group(1).strip() if match else None


def _next_internal_id(items: list[dict[str, Any]]) -> str:
    numbers = []
    for item in items:
        match = re.fullmatch(r"pr-(\d{4,})", _text(item.get("paper_id")))
        if match:
            numbers.append(int(match.group(1)))
    return f"pr-{max(numbers, default=0) + 1:04d}"


def next_paper_id(items: list[dict[str, Any]]) -> str:
    return _next_internal_id(items)


def enrich_record(
    item: dict[str, Any],
    *,
    paper_id: str | None = None,
    detailed_track: str | None = None,
    primary_track: str | None = None,
    root: Path | None = None,
    migrated_on: str = MIGRATION_DATE,
) -> dict[str, Any]:
    """Add or refresh structured fields while preserving legacy fields."""

    raw_venue = _text(item.get("venue"))
    canonical = canonical_venue(raw_venue)
    item["venue_as_recorded"] = item.get("venue_as_recorded") or raw_venue
    item["venue"] = canonical
    item["venue_canonical"] = canonical

    identifiers = dict(item.get("identifiers") or {})
    extracted = extract_identifiers(item.get("page"), item.get("pdf"), item.get("project"))
    for key, value in extracted.items():
        identifiers.setdefault(key, value)
    item["identifiers"] = identifiers

    kind = publication_kind(canonical)
    publication = dict(item.get("publication") or {})
    publication.update(
        {
            "venue": canonical,
            "year": item.get("year"),
            "venue_year": venue_year(raw_venue) or item.get("year"),
            "kind": publication.get("kind") or kind,
            "status": publication.get("status") or publication_status(kind, canonical),
            "presentation": publication.get("presentation") or presentation_from_venue(raw_venue),
            "venue_id": publication.get("venue_id") or venue_id_for(canonical),
        }
    )
    item["publication"] = publication

    sources = dict(item.get("sources") or {})
    sources.setdefault("primary", _source(item.get("page"), "primary"))
    sources.setdefault("preprint", _source(
        f"https://arxiv.org/abs/{identifiers['arxiv']}" if identifiers.get("arxiv") else None,
        "arxiv",
    ))
    sources.setdefault("paper_pdf", _source(item.get("pdf"), "pdf"))
    sources.setdefault("project", _source(item.get("project"), "project"))
    project = _text(item.get("project"))
    sources.setdefault(
        "code",
        _source(project, "code") if artifact_code_status(project) == "released" else None,
    )
    item["sources"] = sources

    artifacts = dict(item.get("artifacts") or {})
    artifacts.setdefault("code_status", artifact_code_status(item.get("project")))
    artifacts.setdefault("data_status", "not_recorded")
    artifacts["local_pdf_cache"] = bool(root and item.get("folder") and (root / item["folder"] / "paper.pdf").exists())
    item["artifacts"] = artifacts

    chosen_track = primary_track or item.get("primary_track") or primary_track_for(
        item.get("category"), item.get("tags", []), detailed_track, item.get("title")
    )
    item["primary_track"] = chosen_track
    item["paper_type"] = item.get("paper_type") or paper_type_for(item)
    item["relations"] = list(item.get("relations") or [])

    curation = dict(item.get("curation") or {})
    role = item.get("role")
    rationale_status = "pending"
    if curation.get("admission_reason") is None and role:
        curation["admission_reason"] = role
        curation.setdefault("rationale_basis", "existing_role")
        rationale_status = "recorded"
    if curation.get("admission_reason") is None:
        curation["admission_reason"] = (
            "Retained from the existing registry for broad literature coverage; "
            "paper-specific admission rationale requires manual review."
        )
        curation.setdefault("rationale_basis", "registry_carryover")
    curation.setdefault("rationale_status", rationale_status)
    item["curation"] = curation

    source_audit = item.get("source_audit") or _note_source_audit(root, item.get("folder", ""))
    if source_audit and not item.get("source_audit"):
        item["source_audit"] = source_audit
    provenance = dict(item.get("provenance") or {})
    provenance.setdefault("metadata_source_kind", source_kind(item.get("page")) or "unverified")
    note_evidence = _note_evidence(root, item.get("folder", ""))
    evidence_candidate = note_evidence or item.get("evidence") or "CURATION_ONLY"
    evidence_rank = {"CURATION_ONLY": 0, "ABSTRACT_CHECKED": 1, "FULL_TEXT_CHECKED": 2, "EXPERIMENT_CHECKED": 3}
    current_evidence = provenance.get("content_evidence")
    if current_evidence not in evidence_rank or evidence_rank[evidence_candidate] > evidence_rank[current_evidence]:
        provenance["content_evidence"] = evidence_candidate
    provenance.setdefault("source_audit_status", "recorded" if source_audit else "not_recorded")
    date_match = re.search(r"\b(20\d{2}-\d{2}-\d{2})\b", _text(source_audit))
    if provenance.get("metadata_checked_on") is None:
        provenance["metadata_checked_on"] = date_match.group(1) if date_match else None
    if provenance.get("source_audit_note") is None:
        provenance["source_audit_note"] = source_audit
    provenance["schema_version"] = SCHEMA_VERSION
    provenance["schema_migrated_on"] = migrated_on
    item["provenance"] = provenance

    if paper_id:
        item["paper_id"] = paper_id
    else:
        item.setdefault("paper_id", None)
    return item


def validate_record_shape(item: dict[str, Any], *, intensive: bool = False) -> list[str]:
    """Dependency-free validation used by the repository audit."""

    errors: list[str] = []
    required = ("paper_id", "title", "year", "venue", "category", "tags", "folder", "page", "primary_track", "publication", "identifiers", "sources", "artifacts", "curation", "provenance", "relations")
    for key in required:
        if key not in item:
            errors.append(f"missing {key}")
    if not re.fullmatch(r"pr-\d{4,}", _text(item.get("paper_id"))):
        errors.append("invalid paper_id")
    if intensive and item.get("primary_track") not in PRIMARY_TRACKS:
        errors.append("invalid intensive primary_track")
    if item.get("primary_track") is not None and item.get("primary_track") not in PRIMARY_TRACKS:
        errors.append("invalid primary_track")
    publication = item.get("publication") if isinstance(item.get("publication"), dict) else {}
    if publication.get("kind") not in PUBLICATION_KINDS:
        errors.append("invalid publication.kind")
    if publication.get("status") not in PUBLICATION_STATUSES:
        errors.append("invalid publication.status")
    if publication.get("presentation") not in PRESENTATIONS:
        errors.append("invalid publication.presentation")
    artifacts = item.get("artifacts") if isinstance(item.get("artifacts"), dict) else {}
    if artifacts.get("code_status") not in CODE_STATUSES:
        errors.append("invalid artifacts.code_status")
    if artifacts.get("data_status") not in DATA_STATUSES:
        errors.append("invalid artifacts.data_status")
    if not isinstance(artifacts.get("local_pdf_cache"), bool):
        errors.append("invalid artifacts.local_pdf_cache")
    provenance = item.get("provenance") if isinstance(item.get("provenance"), dict) else {}
    if provenance.get("content_evidence") not in {"CURATION_ONLY", "ABSTRACT_CHECKED", "FULL_TEXT_CHECKED", "EXPERIMENT_CHECKED"}:
        errors.append("invalid provenance.content_evidence")
    if provenance.get("schema_version") != SCHEMA_VERSION:
        errors.append("invalid provenance.schema_version")
    if not isinstance(item.get("relations"), list):
        errors.append("relations is not a list")
    curation = item.get("curation") if isinstance(item.get("curation"), dict) else {}
    roles = curation.get("roles")
    if roles is not None:
        if not isinstance(roles, list) or any(role not in CURATION_ROLES for role in roles):
            errors.append("invalid curation.roles")
    facets = item.get("facets")
    if facets is not None:
        if not isinstance(facets, dict) or any(key not in FACET_KEYS for key in facets):
            errors.append("invalid facets")
        elif any(not isinstance(values, list) or any(not isinstance(value, str) for value in values) for values in facets.values()):
            errors.append("invalid facets values")
    return errors
