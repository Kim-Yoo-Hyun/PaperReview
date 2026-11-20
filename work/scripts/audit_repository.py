#!/usr/bin/env python3
"""Read-only integrity audit for the PaperReview literature system."""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
import re
import sys
import unicodedata
import urllib.parse
from collections import Counter, defaultdict
from pathlib import Path

try:
    from render_source_audit import render as render_source_audit
    from registry_profiles import ARTIFACT_STATUSES, EVALUATION_SETTINGS, LINEAGE_STATUSES, PROTOCOL_STATUSES, REPRO_STATUSES
    from registry_schema import CURATION_ROLES, DATA_STATUSES, FACET_KEYS, PRIMARY_TRACKS, SCHEMA_VERSION, validate_record_shape, venue_id_for
except ModuleNotFoundError:
    from .render_source_audit import render as render_source_audit
    from .registry_profiles import ARTIFACT_STATUSES, EVALUATION_SETTINGS, LINEAGE_STATUSES, PROTOCOL_STATUSES, REPRO_STATUSES
    from .registry_schema import CURATION_ROLES, DATA_STATUSES, FACET_KEYS, PRIMARY_TRACKS, SCHEMA_VERSION, validate_record_shape, venue_id_for


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"


def path_has_exact_case(relative: str) -> bool:
    """Detect paths that work on case-insensitive hosts but break on Linux."""
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts:
        return False
    current = ROOT
    for part in path.parts:
        if not current.is_dir() or part not in {entry.name for entry in current.iterdir()}:
            return False
        current = current / part
    return current.exists()


NOTE_NAMES = ["01_overview.md", "02_problem.md", "03_method.md", "04_evaluation.md", "05_insights.md"]
STATUSES = {"UNREAD", "SKIMMED", "READ", "SYNTHESIZED", "REPRODUCED"}
EVIDENCE = {"CURATION_ONLY", "ABSTRACT_CHECKED", "FULL_TEXT_CHECKED", "EXPERIMENT_CHECKED"}
RELATION_TYPES = {
    "version_of",
    "same_work_as",
    "extends",
    "replicates",
    "baseline_for",
    "uses_dataset",
    "evaluates_on",
    "builds_on",
    "supersedes",
}
RELATION_CONFIDENCES = {"manual", "verified", "inferred"}
RELATION_STATUSES = {"curated", "imported", "unverified"}
RELATION_EVIDENCE_SCOPES = {
    "paper_body",
    "official_abstract",
    "official_project",
    "title_lineage",
    "registry_identity",
    "citation_reference",
    "official_source",
}
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TRACKER_REQUIRED_FIELDS = {
    "SKIMMED": ("problem_and_assumptions", "next_action"),
    "READ": (
        "problem_and_assumptions",
        "observation_state_action_control",
        "embodiment_task_data_metrics",
        "failure_modes",
        "research_relevance",
        "next_action",
    ),
    "SYNTHESIZED": (
        "problem_and_assumptions",
        "observation_state_action_control",
        "embodiment_task_data_metrics",
        "failure_modes",
        "research_relevance",
        "next_action",
    ),
    "REPRODUCED": (
        "problem_and_assumptions",
        "observation_state_action_control",
        "embodiment_task_data_metrics",
        "failure_modes",
        "research_relevance",
        "next_action",
        "personal_notes",
    ),
}
MINIMUM_EVIDENCE_BY_STATUS = {
    "SKIMMED": "ABSTRACT_CHECKED",
    "READ": "FULL_TEXT_CHECKED",
    "SYNTHESIZED": "FULL_TEXT_CHECKED",
    "REPRODUCED": "EXPERIMENT_CHECKED",
}
SYNTHESIS_BY_TRACK = {
    "Planning and control": "01_control.md",
    "RL, IL, offline learning, and robot data": "02_learning.md",
    "Manipulation, contact, tactile, and dexterity": "03_manipulation.md",
    "VLA and generalist robot policies": "04_vla.md",
    "World models, safety, uncertainty, and recovery": "05_safety.md",
    "Locomotion, whole-body, mobile manipulation, and humanoids": "06_mobility.md",
    "Robotics-enabling 3D perception": "07_perception.md",
}
CATALOGS = {
    "benchmark": ROOT / "work" / "sources" / "benchmark_catalog.json",
    "metric": ROOT / "work" / "sources" / "metric_catalog.json",
}
RESOURCES = ROOT / "work" / "sources" / "resources.json"
REGISTRY_INDEX = ROOT / "research" / "REGISTRY_INDEX.csv"
REGISTRY_STATS = ROOT / "research" / "REGISTRY_STATS.md"
NOTE_REVIEW_MANIFEST_SPECS = [
    {
        "path": ROOT / "work" / "sources" / "fulltext_insights_review_manifest_2026-09-03.json",
        "scope": "insights",
        "note_name": "05_insights.md",
    },
]


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().casefold()
    return re.sub(r"[^a-z0-9]+", "", value)


def valid_http(value: str | None) -> bool:
    return bool(value and re.match(r"^https?://", value, flags=re.IGNORECASE))


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_catalog(path: Path, kind: str, paper_ids: set[str], errors: list[str]) -> int:
    if not path.exists():
        errors.append(f"missing {kind} catalog: {path.relative_to(ROOT)}")
        return 0
    try:
        catalog = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid {kind} catalog JSON: {exc}")
        return 0
    if catalog.get("schema_version") != SCHEMA_VERSION or catalog.get("catalog_type") != kind:
        errors.append(f"invalid {kind} catalog schema metadata")
    entries = catalog.get("entries", [])
    if not isinstance(entries, list):
        errors.append(f"invalid {kind} catalog entries")
        return 0
    ids = []
    for entry in entries:
        entry_id = entry.get(f"{kind}_id", "")
        ids.append(entry_id)
        if not entry_id.startswith(f"{kind}:"):
            errors.append(f"invalid {kind} catalog id: {entry_id}")
        for reference in entry.get("paper_references", []):
            if reference.get("paper_id") not in paper_ids:
                errors.append(f"{kind} catalog points to unknown paper_id: {reference.get('paper_id')}")
            if reference.get("evidence") != "cue_only":
                errors.append(f"{kind} catalog reference is missing cue_only evidence: {entry_id}")
    duplicates = [value for value, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append(f"duplicate {kind} catalog ids: {duplicates}")
    return len(entries)


def audit_resources(path: Path, paper_ids: set[str], errors: list[str]) -> int:
    if not path.exists():
        errors.append(f"missing combined resource view: {path.relative_to(ROOT)}")
        return 0
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid combined resource view JSON: {exc}")
        return 0
    if payload.get("schema_version") != SCHEMA_VERSION:
        errors.append("invalid combined resource view schema metadata")
    entries = payload.get("entries", [])
    if not isinstance(entries, list):
        errors.append("invalid combined resource view entries")
        return 0
    ids = []
    allowed_types = {"benchmark_or_dataset", "metric", "code_or_project"}
    for entry in entries:
        resource_id = entry.get("resource_id", "")
        ids.append(resource_id)
        if not resource_id or entry.get("resource_type") not in allowed_types:
            errors.append(f"invalid combined resource entry: {resource_id}")
        if entry.get("resource_type") == "code_or_project" and not valid_http(entry.get("url")):
            errors.append(f"invalid code/project resource URL: {resource_id}")
        references = entry.get("paper_references", [])
        references += [{"paper_id": value} for value in entry.get("paper_ids", [])]
        for reference in references:
            if reference.get("paper_id") not in paper_ids:
                errors.append(f"resource points to unknown paper_id: {resource_id}")
    duplicates = [value for value, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append(f"duplicate combined resource ids: {duplicates}")
    return len(entries)


def audit_registry_index(path: Path, papers_by_id: dict[str, dict], errors: list[str]) -> int:
    if not path.exists():
        errors.append(f"missing generated registry index: {path.relative_to(ROOT)}")
        return 0
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        errors.append(f"invalid generated registry index: {exc}")
        return 0
    required = {
        "paper_id", "title", "year", "venue", "category", "tier", "roles",
        "facets", "evidence_level", "reading_status", "primary_source",
        "identifier_status", "primary_source_scope",
        "overview_path", "outgoing_relations", "incoming_relation_count",
        "evaluation_type", "evaluation_settings", "evaluation_protocol",
        "benchmark_cues", "metric_cues", "reproducibility_status",
        "checkpoint_status", "configuration_status", "environment_status",
        "run_conditions_status", "lineage_status", "lineage_outgoing_count",
        "lineage_incoming_count", "lineage_candidate_count",
    }
    fields = set(rows[0]) if rows else set()
    missing = sorted(required - fields)
    if missing:
        errors.append(f"generated registry index missing fields: {missing}")
    ids = [row.get("paper_id", "") for row in rows]
    if len(rows) != len(papers_by_id):
        errors.append(f"generated registry index rows {len(rows)} != papers {len(papers_by_id)}")
    if len(set(ids)) != len(ids):
        errors.append("generated registry index has duplicate paper_id")
    for row in rows:
        item = papers_by_id.get(row.get("paper_id"))
        if not item:
            errors.append(f"generated registry index points to unknown paper_id: {row.get('paper_id')}")
            continue
        if row.get("title") != item.get("title") or row.get("year") != str(item.get("year")):
            errors.append(f"generated registry index identity mismatch: {row.get('paper_id')}")
        expected_identifier = "identified" if any(item.get("identifiers", {}).values()) else "source_only"
        if row.get("identifier_status") != expected_identifier:
            errors.append(f"generated registry index identifier status mismatch: {row.get('paper_id')}")
        primary = (item.get("sources") or {}).get("primary") or {}
        expected_scope = primary.get("scope") or (item.get("provenance") or {}).get("primary_source_scope", "")
        if row.get("primary_source_scope") != expected_scope:
            errors.append(f"generated registry index source scope mismatch: {row.get('paper_id')}")
        try:
            facets = json.loads(row.get("facets", "{}"))
        except json.JSONDecodeError:
            errors.append(f"generated registry index has invalid facets JSON: {row.get('paper_id')}")
            facets = {}
        if not isinstance(facets, dict) or any(key not in FACET_KEYS for key in facets):
            errors.append(f"generated registry index has invalid facets: {row.get('paper_id')}")
        try:
            indexed_relations = json.loads(row.get("outgoing_relations", "[]"))
        except json.JSONDecodeError:
            errors.append(f"generated registry index has invalid outgoing_relations: {row.get('paper_id')}")
            indexed_relations = []
        expected_relations = [
            {
                "type": relation.get("type"),
                "paper_id": relation.get("paper_id"),
                "confidence": relation.get("confidence"),
            }
            for relation in item.get("relations", [])
        ]
        if indexed_relations != expected_relations:
            errors.append(f"generated registry index relation mismatch: {row.get('paper_id')}")
        incoming = sum(
            1
            for candidate in papers_by_id.values()
            for relation in candidate.get("relations", [])
            if relation.get("paper_id") == row.get("paper_id")
        )
        if row.get("incoming_relation_count") != str(incoming):
            errors.append(f"generated registry index incoming relation mismatch: {row.get('paper_id')}")
        evaluation = item.get("evaluation_profile") or {}
        if row.get("evaluation_type") != evaluation.get("type", ""):
            errors.append(f"generated registry index evaluation type mismatch: {row.get('paper_id')}")
        if row.get("evaluation_settings") != ";".join(evaluation.get("settings", [])):
            errors.append(f"generated registry index evaluation setting mismatch: {row.get('paper_id')}")
        try:
            indexed_protocol = json.loads(row.get("evaluation_protocol", "{}"))
        except json.JSONDecodeError:
            errors.append(f"generated registry index evaluation protocol is invalid: {row.get('paper_id')}")
            indexed_protocol = {}
        if indexed_protocol != (evaluation.get("protocol") or {}):
            errors.append(f"generated registry index evaluation protocol mismatch: {row.get('paper_id')}")
        reproducibility = item.get("reproducibility") or {}
        if row.get("reproducibility_status") != reproducibility.get("status", ""):
            errors.append(f"generated registry index reproducibility mismatch: {row.get('paper_id')}")
        expected_repro_statuses = {
            "checkpoint_status": (reproducibility.get("checkpoint") or {}).get("status", ""),
            "configuration_status": (reproducibility.get("configuration") or {}).get("status", ""),
            "environment_status": (reproducibility.get("environment") or {}).get("status", ""),
            "run_conditions_status": (reproducibility.get("run_conditions") or {}).get("status", ""),
        }
        for field, expected in expected_repro_statuses.items():
            if row.get(field) != expected:
                errors.append(f"generated registry index {field} mismatch: {row.get('paper_id')}")
        lineage = item.get("lineage_profile") or {}
        if row.get("lineage_status") != lineage.get("status", ""):
            errors.append(f"generated registry index lineage status mismatch: {row.get('paper_id')}")
        expected_lineage_counts = {
            "lineage_outgoing_count": len(lineage.get("outgoing_paper_ids", [])),
            "lineage_incoming_count": len(lineage.get("incoming_paper_ids", [])),
            "lineage_candidate_count": len(
                set(lineage.get("queue_adjacency_paper_ids", []))
                | set(lineage.get("legacy_summary_candidate_paper_ids", []))
            ),
        }
        for field, expected in expected_lineage_counts.items():
            if row.get(field) != str(expected):
                errors.append(f"generated registry index {field} mismatch: {row.get('paper_id')}")
    return len(rows)


def note_evidence_for(path: Path) -> str:
    match = re.search(r"Evidence maturity:\s*`([^`]+)`", path.read_text(encoding="utf-8", errors="ignore"))
    value = match.group(1) if match else "MISSING"
    return value if value in EVIDENCE else "MISSING"


def audit_registry_profiles(
    item: dict,
    paper_ids: set[str],
    errors: list[str],
    incoming_by_id: dict[str, list[str]],
) -> None:
    """Validate the all-paper metadata profiles without judging paper claims."""

    paper_id = item.get("paper_id")
    folder = item.get("folder", "")
    expected_note = f"{folder}/04_evaluation.md"
    evaluation = item.get("evaluation_profile")
    if not isinstance(evaluation, dict):
        errors.append(f"missing evaluation_profile: {paper_id}")
    else:
        if evaluation.get("status") not in {"structured_note_cues", "not_recorded"}:
            errors.append(f"invalid evaluation_profile.status: {paper_id}")
        if not isinstance(evaluation.get("type"), str) or not evaluation.get("type"):
            errors.append(f"invalid evaluation_profile.type: {paper_id}")
        settings = evaluation.get("settings")
        if not isinstance(settings, list) or not settings or any(value not in EVALUATION_SETTINGS for value in settings):
            errors.append(f"invalid evaluation_profile.settings: {paper_id}")
        protocol = evaluation.get("protocol")
        expected_protocol = {
            "dataset_or_benchmark",
            "metrics",
            "baselines",
            "ablations",
            "split_or_generalization",
            "trials_or_seeds",
            "statistics",
            "failure_cases",
        }
        if not isinstance(protocol, dict) or set(protocol) != expected_protocol:
            errors.append(f"invalid evaluation_profile.protocol keys: {paper_id}")
        elif any(value not in PROTOCOL_STATUSES for value in protocol.values()):
            errors.append(f"invalid evaluation_profile.protocol value: {paper_id}")
        source_note = evaluation.get("source_note")
        if source_note not in {expected_note, None}:
            errors.append(f"evaluation_profile source_note mismatch: {paper_id}")
        if source_note and not (ROOT / source_note).exists():
            errors.append(f"evaluation_profile source_note missing: {paper_id}")
        if evaluation.get("reviewed_on") and not DATE_PATTERN.match(str(evaluation.get("reviewed_on"))):
            errors.append(f"invalid evaluation_profile.reviewed_on: {paper_id}")
        for cue_key in ("benchmark_cues", "metric_cues"):
            cues = evaluation.get(cue_key)
            if not isinstance(cues, list):
                errors.append(f"invalid evaluation_profile.{cue_key}: {paper_id}")
                continue
            for cue in cues:
                if not isinstance(cue, dict) or cue.get("evidence") != "cue_only":
                    errors.append(f"evaluation_profile {cue_key} is not cue_only: {paper_id}")
        trial_evidence = evaluation.get("trial_evidence")
        if not isinstance(trial_evidence, list):
            errors.append(f"invalid evaluation_profile.trial_evidence: {paper_id}")
        else:
            for record in trial_evidence:
                if not isinstance(record, dict) or not isinstance(record.get("count"), int) or record.get("count") < 0:
                    errors.append(f"invalid evaluation_profile trial evidence: {paper_id}")

    reproducibility = item.get("reproducibility")
    if not isinstance(reproducibility, dict):
        errors.append(f"missing reproducibility profile: {paper_id}")
    else:
        if reproducibility.get("status") not in {"metadata_audited", "not_recorded"}:
            errors.append(f"invalid reproducibility.status: {paper_id}")
        for key in ("code", "data", "checkpoint", "configuration", "environment", "run_conditions"):
            value = reproducibility.get(key)
            if not isinstance(value, dict):
                errors.append(f"invalid reproducibility.{key}: {paper_id}")
                continue
            status = value.get("status")
            allowed = ARTIFACT_STATUSES if key in {"code", "data"} else REPRO_STATUSES
            if status not in allowed:
                errors.append(f"invalid reproducibility.{key}.status: {paper_id}")
        artifact = item.get("artifacts") or {}
        if (reproducibility.get("code") or {}).get("status") != artifact.get("code_status"):
            errors.append(f"reproducibility/code artifact mismatch: {paper_id}")
        if (reproducibility.get("data") or {}).get("status") != artifact.get("data_status"):
            errors.append(f"reproducibility/data artifact mismatch: {paper_id}")
        source_note = reproducibility.get("source_note")
        if source_note not in {expected_note, None}:
            errors.append(f"reproducibility source_note mismatch: {paper_id}")
        if source_note and not (ROOT / source_note).exists():
            errors.append(f"reproducibility source_note missing: {paper_id}")
        if reproducibility.get("reviewed_on") and not DATE_PATTERN.match(str(reproducibility.get("reviewed_on"))):
            errors.append(f"invalid reproducibility.reviewed_on: {paper_id}")

    lineage = item.get("lineage_profile")
    if not isinstance(lineage, dict):
        errors.append(f"missing lineage_profile: {paper_id}")
        return
    if lineage.get("status") not in LINEAGE_STATUSES:
        errors.append(f"invalid lineage_profile.status: {paper_id}")
    for key in (
        "outgoing_paper_ids",
        "incoming_paper_ids",
        "queue_adjacency_paper_ids",
        "legacy_summary_candidate_paper_ids",
    ):
        values = lineage.get(key)
        if not isinstance(values, list) or len(values) != len(set(values)) or any(value not in paper_ids for value in values):
            errors.append(f"invalid lineage_profile.{key}: {paper_id}")
    expected_outgoing = [relation.get("paper_id") for relation in item.get("relations", []) if relation.get("paper_id")]
    if lineage.get("outgoing_paper_ids") != expected_outgoing:
        errors.append(f"lineage_profile outgoing mismatch: {paper_id}")
    expected_incoming = sorted(set(incoming_by_id.get(paper_id, [])))
    if lineage.get("incoming_paper_ids") != expected_incoming:
        errors.append(f"lineage_profile incoming mismatch: {paper_id}")
    if not isinstance(lineage.get("legacy_summary_present"), bool):
        errors.append(f"invalid lineage_profile.legacy_summary_present: {paper_id}")
    if lineage.get("audit_scope") != "all_registry":
        errors.append(f"invalid lineage_profile.audit_scope: {paper_id}")
    if lineage.get("audited_on") and not DATE_PATTERN.match(str(lineage.get("audited_on"))):
        errors.append(f"invalid lineage_profile.audited_on: {paper_id}")


def audit_note_review_manifest(
    spec: dict,
    papers_by_id: dict[str, dict],
    errors: list[str],
) -> dict[str, dict]:
    """Validate a note-scoped full-text manifest and index its records.

    Note manifests are intentionally audited independently of paper-level
    review precedence.  The returned index is used below to check that the
    provenance attachment in ``papers.json`` points to the same record.
    """

    path = spec["path"]
    relative = str(path.relative_to(ROOT))
    if not path.exists():
        errors.append(f"missing note review manifest: {relative}")
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid note review manifest JSON: {relative}: {exc}")
        return {}
    records = payload.get("records")
    if not isinstance(records, list):
        errors.append(f"invalid note review manifest records: {relative}")
        return {}
    snapshot = payload.get("registry_snapshot") or {}
    if snapshot.get("status") != "note_level":
        errors.append(f"note review manifest is not marked note_level: {relative}")
    if snapshot.get("note_name") != spec["note_name"]:
        errors.append(f"note review manifest note_name mismatch: {relative}")
    if payload.get("paper_count") not in {None, len(records)}:
        errors.append(f"note review manifest paper_count mismatch: {relative}")
    index: dict[str, dict] = {}
    for record in records:
        paper_id = record.get("paper_id")
        if not paper_id or paper_id in index:
            errors.append(f"duplicate or missing paper_id in note review manifest: {relative}")
            continue
        index[paper_id] = record
        item = papers_by_id.get(paper_id)
        if not item:
            errors.append(f"note review manifest points to unknown paper_id: {relative} {paper_id}")
            continue
        if record.get("title") != item.get("title"):
            errors.append(f"note review manifest title mismatch: {paper_id}")
        if record.get("folder") and record.get("folder") != item.get("folder"):
            errors.append(f"note review manifest folder mismatch: {paper_id}")
        note_path = ROOT / item["folder"] / spec["note_name"]
        if not note_path.exists():
            errors.append(f"note review manifest note missing: {paper_id} {spec['note_name']}")
            continue
        record_evidence = record.get("evidence_level")
        if record_evidence not in EVIDENCE:
            errors.append(f"invalid note review evidence: {paper_id}")
        elif note_evidence_for(note_path) != record_evidence:
            errors.append(f"note review evidence mismatch: {paper_id} {spec['note_name']}")
        if record.get("source_kind") != "PDF":
            errors.append(f"note review source is not PDF: {paper_id}")
        if record.get("status") not in {"downloaded", "reused"}:
            errors.append(f"invalid note review status: {paper_id}")
    if snapshot.get("reviewed_paper_count") not in {None, len(index)}:
        errors.append(f"note review snapshot count mismatch: {relative}")
    return {
        paper_id: {
            "manifest": relative,
            "scope": spec["scope"],
            "note_name": spec["note_name"],
            "record": record,
        }
        for paper_id, record in index.items()
    }


def comparison_matrix_paths(path: Path) -> list[str]:
    """Return registry overview paths linked from one hand-maintained matrix."""

    text = path.read_text(encoding="utf-8")
    marker = "## Comparison Matrix"
    if marker not in text:
        return []
    section = text.split(marker, 1)[1]
    next_heading = re.search(r"\n## (?!Comparison Matrix)", section)
    if next_heading:
        section = section[: next_heading.start()]
    links = re.findall(r"\]\((\.\./[^)#]+/01_overview\.md)(?:#[^)]+)?\)", section)
    return ["./" + urllib.parse.unquote(value[3:]) for value in links]


def audit_markdown_documents(errors: list[str]) -> dict[str, int]:
    """Audit all Markdown, including notes, instructions and historical context.

    Code examples are not links. Historical missing targets should be retained
    as explicit text instead of clickable links to removed files.
    """
    paths = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
    link_re = re.compile(r"(?<!\\)\[[^\]\n]*\]\(([^)\n]+)\)")
    checked = 0
    for path in paths:
        content = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        if not re.search(r"(?m)^# .+", content):
            errors.append(f"Markdown H1 missing: {relative}")
        fence = None
        table_columns = None
        for number, line in enumerate(content.splitlines(), 1):
            marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
            if marker:
                run, tail = marker.groups()
                if fence is None:
                    fence = run
                elif run[0] == fence[0] and len(run) >= len(fence) and not tail.strip():
                    fence = None
                table_columns = None
                continue
            if fence:
                continue
            if line.startswith("|") and line.rstrip().endswith("|"):
                columns = len(re.findall(r"(?<!\\)\|", line)) - 1
                if table_columns is None:
                    table_columns = columns
                elif columns != table_columns:
                    errors.append(f"Markdown table column mismatch: {relative}:{number} ({columns} != {table_columns})")
            else:
                table_columns = None
            prose = re.sub(r"(`+).*?\1", "", line)
            for raw_target in link_re.findall(prose):
                target = raw_target.strip()
                if target.startswith("<") and ">" in target:
                    target = target[1:target.index(">")]
                else:
                    target = re.split(r'\s+["\x27]', target, maxsplit=1)[0]
                parsed = urllib.parse.urlsplit(target)
                if parsed.scheme or target.startswith("//") or not parsed.path:
                    continue
                resolved = (path.parent / urllib.parse.unquote(parsed.path)).resolve()
                try:
                    resolved.relative_to(ROOT.resolve())
                except ValueError:
                    errors.append(f"Markdown link escapes repository: {relative}:{number} -> {raw_target}")
                    continue
                checked += 1
                if not resolved.exists():
                    errors.append(f"Markdown link target missing: {relative}:{number} -> {raw_target}")
        if fence:
            errors.append(f"Markdown code fence unclosed: {relative}")
    return {"files": len(paths), "links": checked}


TEMPLATE4_AXES = {
    "method_tags": {"IL", "RL", "모델기반", "고전제어", "하이브리드"},
    "task_tags": {"조작", "이동", "내비게이션", "전신제어", "모바일매니퓰레이션"},
    "embodiment_tags": {"단팔", "양팔", "모바일매니퓰레이터", "휴머노이드", "사족보행", "기타"},
    "modality_tags": {"RGB", "depth", "촉각", "언어", "고유수용감각", "기타"},
    "data_source_tags": {"실제로봇", "시뮬", "인간영상", "합성", "혼합"},
}


def valid_tag_list(values, allowed):
    return isinstance(values, list) and bool(values) and (
        values == ["unknown"] or all(isinstance(v, str) and v in allowed for v in values)
        and len(set(values)) == len(values)
    )


def audit_taxonomy_batches(batches, registry_ids, errors, warnings):
    """Validate foreign keys and Appendix IDs across the registered YAML batches."""
    batch_ids = set()
    matched_registry_ids = set()
    citations = set()
    for batch in batches:
        relative = batch["path"]
        if not path_has_exact_case(relative):
            errors.append(f"missing taxonomy batch: {relative}")
            continue
        try:
            import yaml
        except ImportError:
            warnings.append(f"PyYAML unavailable, YAML contents unchecked: {relative}")
            continue
        try:
            records = yaml.safe_load((ROOT / relative).read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"invalid taxonomy YAML: {relative}: {exc}")
            continue
        if not isinstance(records, list) or len(records) != batch["record_count"]:
            errors.append(f"taxonomy batch count mismatch: {relative}")
            continue
        for record in records:
            if not isinstance(record, dict):
                errors.append(f"invalid taxonomy record: {relative}")
                continue
            paper_id = record.get(batch["registry_key"])
            appendix_id = record.get("id", "")
            if paper_id not in registry_ids or paper_id in matched_registry_ids:
                errors.append(f"invalid or repeated taxonomy registry_id: {paper_id}")
            if not isinstance(appendix_id, str) or not re.fullmatch(r"[0-9]{4}-[a-z0-9-]+-[a-z0-9-]+", appendix_id):
                errors.append(f"invalid Appendix ID: {appendix_id}")
                continue
            if appendix_id in batch_ids:
                errors.append(f"invalid or repeated Appendix ID: {appendix_id}")
            for field, allowed in TEMPLATE4_AXES.items():
                if not valid_tag_list(record.get(field), allowed):
                    errors.append(f"invalid {field}: {appendix_id}")
            openness = record.get("openness")
            if not isinstance(openness, dict) or set(openness) != {"code", "weights", "data"} or any(
                value not in ("Y", "N", "부분", "unknown") for value in openness.values()
            ):
                errors.append(f"invalid openness: {appendix_id}")
            if record.get("changed_from", {}).get("id") != paper_id:
                errors.append(f"missing previous registry identity: {appendix_id}")
            if "vla" in record:
                vla = record["vla"]
                evaluation = vla.get("evaluation", {})
                if (not valid_tag_list(vla.get("action_representation"), {"이산 토큰", "연속(diffusion·flow matching)", "하이브리드"})
                    or not valid_tag_list(vla.get("training"), {"SFT", "RL 파인튜닝", "co-training(웹데이터 병행)", "기타"})
                    or vla.get("architecture") not in {"단일 모델", "이중 시스템(고수준 추론 + 저수준 제어)", "기타", "unknown"}
                    or not all(vla.get("backbone", {}).get(key) for key in ("name", "size"))
                    or not evaluation.get("sim_benchmarks")
                    or not (evaluation.get("real_robot_tasks") == "unknown" or type(evaluation.get("real_robot_tasks")) is int and evaluation["real_robot_tasks"] >= 0)):
                    errors.append(f"invalid VLA taxonomy: {appendix_id}")
            if "humanoid" in record:
                humanoid = record["humanoid"]
                if (not valid_tag_list(humanoid.get("control_scope"), {"로코모션", "상체 조작", "전신", "손 정밀조작"})
                    or not valid_tag_list(humanoid.get("training"), {"sim-to-real RL", "모션 리타게팅", "텔레오퍼레이션 모방", "모델기반"})
                    or not valid_tag_list(humanoid.get("hand_type"), {"그리퍼", "다지 손", "없음"})
                    or not humanoid.get("hardware")):
                    errors.append(f"invalid humanoid taxonomy: {appendix_id}")
            matched_registry_ids.add(paper_id)
            batch_ids.add(appendix_id)
            citations.update(record.get("prior_work", []))
    for target in sorted(citations - batch_ids - registry_ids - {"unknown"}):
        errors.append(f"unresolved taxonomy prior_work: {target}")
    return len(matched_registry_ids)


def audit_external_reviews(meta, registry_ids, errors, warnings):
    """Check the dated evidence snapshots independently of subsequent admissions or tier changes."""
    coverage = meta.get("external_coverage")
    deep = meta.get("tier1_deep_review")
    if not coverage or not deep:
        return
    try:
        import yaml
    except ImportError:
        warnings.append("PyYAML unavailable, external review snapshots unchecked")
        return
    try:
        with gzip.open(ROOT / coverage["titles"], "rt", encoding="utf-8") as stream:
            header = json.loads(next(stream))
            lists = set(header["source_lists"])
            if len(lists) != coverage["source_count"]:
                errors.append("external coverage source count mismatch")
            keys = set()
            unmatched_links = set()
            for line in stream:
                row = json.loads(line)
                if row["key"] in keys or not row["found_in"] or set(row["found_in"]) - lists:
                    errors.append(f"invalid external title/source: {row['title']}")
                keys.add(row["key"])
                status = row["status"]
                if status in {"exact", "alias"} and row["registry_id"] not in registry_ids:
                    errors.append(f"unresolved external match: {row['title']}")
                if status in {"possible", "unmatched"} and row["registry_id"] is not None:
                    errors.append(f"unexpected registry ID on unmatched title: {row['title']}")
                if status == "unmatched":
                    unmatched_links.add(frozenset(row["found_in"].items()))
        candidates = yaml.safe_load((ROOT / coverage["candidates"]).read_text())
        if len({r["id"] for r in candidates}) != len(candidates) or len(candidates) != coverage["candidate_count"]:
            errors.append("external candidate count or identity mismatch")
        for row in candidates:
            if frozenset(row["found_in"].items()) not in unmatched_links or not row["content_source"]:
                errors.append(f"missing candidate evidence: {row['id']}")
        batch = yaml.safe_load((ROOT / deep["path"]).read_text())
        included = {r["registry_id"] for r in batch["records"]}
        excluded = set(batch["cohort"]["screened_out"])
        if (len(batch["records"]) != len(included) or len(included) != deep["included"]
            or len(included | excluded) != deep["screened"] or included & excluded
            or (included | excluded) - registry_ids):
            errors.append("Tier 1 review cohort mismatch")
        for r in batch["records"]:
            if r["tier"] != 1 or not (r.get("vla") or r.get("humanoid")):
                errors.append(f"invalid Tier 1 review: {r['registry_id']}")
            for edge in r["prior_work"] if isinstance(r["prior_work"], list) else []:
                if edge["registry_id"] not in registry_ids or edge["type"] not in {"확장", "대체", "비판", "결합"}:
                    errors.append(f"invalid direct predecessor: {r['registry_id']}")
            for scope in r.get("vla", {}).get("real_robot_tasks", {}).get("reported_scopes", []):
                if "#page=" not in scope["source"] or not scope["location"] or not scope["scope"]:
                    errors.append(f"unlocated real-robot task count: {r['registry_id']}")
    except (OSError, ValueError, KeyError, TypeError, StopIteration, yaml.YAMLError) as exc:
        errors.append(f"external review snapshot unreadable: {exc}")


def audit_gapfill_batches(batches, registry_ids, errors, warnings):
    """Keep admission decisions and source-located predecessor IDs resolvable."""
    if not batches:
        return
    try:
        import yaml
    except ImportError:
        warnings.append("PyYAML unavailable, gapfill batches unchecked")
        return
    for descriptor in batches:
        try:
            batch = yaml.safe_load((ROOT / descriptor["path"]).read_text(encoding="utf-8"))
            groups = batch["groups"]
            counts = {name: len(rows) for name, rows in groups.items()}
            if counts != descriptor["groups"] or batch["batch"] != descriptor["batch"]:
                errors.append(f"gapfill batch metadata mismatch: {descriptor['path']}")
            seen = set()
            for row in groups["A"]:
                paper_id = row["registry_id"]
                if (paper_id not in registry_ids or paper_id in seen or not row["found_in"]
                    or row["added_in"] != batch["batch"] or not row["existence_source"]["url"]):
                    errors.append(f"invalid gapfill admission: {paper_id}")
                seen.add(paper_id)
                relations = row["prior_work_relations"]
                if set(row["prior_work"]) != {r["registry_id"] for r in relations}:
                    errors.append(f"gapfill predecessor list mismatch: {paper_id}")
                for edge in relations:
                    if (edge["registry_id"] not in registry_ids or edge["registry_id"] == paper_id
                        or edge["type"] not in {"확장", "대체", "비판", "결합"}
                        or not edge["basis"] or not edge["source"]):
                        errors.append(f"invalid gapfill predecessor: {paper_id}")
            for row in groups["C"]:
                if row["existing_id"] not in registry_ids or row["existing_id"] in seen:
                    errors.append(f"invalid gapfill duplicate: {row['existing_id']}")
        except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
            errors.append(f"gapfill batch unreadable: {exc}")


def main() -> None:
    errors: list[str] = []
    warnings: list[str] = []
    papers = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if not isinstance(papers, list):
        errors.append("manifest is not a JSON list")
        papers = []
    paper_ids = {p.get("paper_id") for p in papers}
    if len(paper_ids) != len(papers) or None in paper_ids:
        errors.append("paper_id is missing or duplicated")
    meta_path = ROOT / "work" / "sources" / "registry_meta.json"
    taxonomy_record_count = 0
    if not meta_path.exists():
        errors.append("missing registry_meta.json")
    else:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        taxonomy_record_count = audit_taxonomy_batches(meta.get("taxonomy_batches", []), paper_ids, errors, warnings)
        audit_external_reviews(meta, paper_ids, errors, warnings)
        audit_gapfill_batches(meta.get("gapfill_batches", []), paper_ids, errors, warnings)
        if source_audit := meta.get("source_audit"):
            try:
                evidence = (ROOT / source_audit["path"]).read_text(encoding="utf-8")
                audited = [json.loads(line) for line in evidence.splitlines()]
                if {row["id"] for row in audited} - set(paper_ids):
                    errors.append("source audit contains unrecognized stable paper IDs")
                report = (ROOT / source_audit["report"]).read_text(encoding="utf-8")
                if report != render_source_audit(audited, source_audit):
                    errors.append("source audit report differs from its dated evidence ledger")
            except (OSError, ValueError, KeyError, TypeError) as exc:
                errors.append(f"could not validate dated source audit: {exc}")
        if meta.get("schema_version") != SCHEMA_VERSION or meta.get("paper_count") != len(papers):
            errors.append("registry metadata schema/count mismatch")
        if meta.get("manifest_sha256") and meta.get("manifest_sha256") != file_sha256(MANIFEST):
            errors.append("registry metadata manifest_sha256 mismatch")
    schema_path = ROOT / "work" / "sources" / "registry.schema.json"
    if not schema_path.exists():
        errors.append("missing registry.schema.json")
    else:
        try:
            from jsonschema import Draft202012Validator

            schema_errors = sorted(
                Draft202012Validator(json.loads(schema_path.read_text(encoding="utf-8"))).iter_errors(papers),
                key=lambda error: list(error.path),
            )
            for error in schema_errors[:20]:
                errors.append(f"manifest JSON Schema: {'.'.join(str(x) for x in error.path)}: {error.message}")
            if len(schema_errors) > 20:
                errors.append(f"manifest JSON Schema: {len(schema_errors) - 20} additional errors")
        except ImportError:
            # The dependency-free validator below remains authoritative in
            # minimal environments where jsonschema is not installed.
            pass
    registry = (ROOT / "PAPER.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\| (?:\d{4}|Unknown) \| [^|]+? \| \[([^\]]+)\]\(\.\/([^)]+/01_overview\.md)\)", registry, re.M)
    declared = re.search(r"Total papers with folders: (\d+)", registry)
    if not declared or int(declared.group(1)) != len(rows) or len(rows) != len(papers):
        errors.append(f"registry/manifest count mismatch: declared={declared.group(1) if declared else None}, rows={len(rows)}, manifest={len(papers)}")
    for key, values in {
        "normalized title": [norm(p["title"]) for p in papers],
        "folder": [p["folder"] for p in papers],
    }.items():
        duplicates = [value for value, count in Counter(values).items() if count > 1]
        if duplicates:
            errors.append(f"duplicate {key}: {len(duplicates)} groups")
    normalized_categories: dict[str, set[str]] = defaultdict(set)
    for paper in papers:
        normalized_categories[norm(paper.get("category", ""))].add(paper.get("category", ""))
    category_aliases = [values for values in normalized_categories.values() if len(values) > 1]
    if category_aliases:
        errors.append(f"category aliases are not normalized: {category_aliases}")
    paper_by_path = {
        f"./{p['folder']}/01_overview.md": p
        for p in papers
        if p.get("folder")
    }

    def paper_for_path(path: str) -> dict | None:
        return paper_by_path.get(path) or paper_by_path.get(urllib.parse.unquote(path))

    primary_url_counts: Counter[str] = Counter()
    for item in papers:
        primary = (item.get("sources") or {}).get("primary")
        if isinstance(primary, dict) and primary.get("url"):
            primary_url_counts[primary["url"].casefold()] += 1
    shared_primary_urls = {url for url, count in primary_url_counts.items() if count > 1}

    for item in papers:
        intensive = False
        # The tier lookup below is authoritative for whether a canonical track
        # is required; validate the nested shape here and refine it after CSV load.
        shape_errors = validate_record_shape(item, intensive=intensive)
        if shape_errors:
            errors.append(f"{item.get('title', '<untitled>')} registry schema: {', '.join(shape_errors)}")
        if item.get("page") and not valid_http(item.get("page")):
            errors.append(f"invalid primary source URL: {item.get('paper_id')}")
        publication = item.get("publication") or {}
        if publication.get("venue_id") and not isinstance(publication.get("venue_id"), str):
            errors.append(f"invalid venue_id: {item.get('paper_id')}")
        primary = (item.get("sources") or {}).get("primary")
        if isinstance(primary, dict) and primary.get("url"):
            expected_scope = "venue_index" if primary["url"].casefold() in shared_primary_urls else "paper_specific"
            if primary.get("scope") != expected_scope:
                errors.append(f"primary source scope mismatch: {item.get('paper_id')}")
        relation_keys: set[tuple[str, str]] = set()
        for relation in item.get("relations", []):
            if not isinstance(relation, dict):
                errors.append(f"invalid relation record: {item.get('paper_id')}")
                continue
            relation_type = relation.get("type", "")
            target_id = relation.get("paper_id", "")
            if relation_type not in RELATION_TYPES:
                errors.append(f"invalid relation type: {item.get('paper_id')} {relation_type}")
            if target_id not in paper_ids:
                errors.append(f"relation points to unknown paper_id: {item.get('paper_id')}")
            if target_id == item.get("paper_id"):
                errors.append(f"relation self-edge: {item.get('paper_id')} {relation_type}")
            relation_key = (relation_type, target_id)
            if relation_key in relation_keys:
                errors.append(f"duplicate relation edge: {item.get('paper_id')} {relation_type} {target_id}")
            relation_keys.add(relation_key)
            if relation.get("source") and not valid_http(relation.get("source")):
                errors.append(f"invalid relation source URL: {item.get('paper_id')}")
            if relation.get("confidence") and relation.get("confidence") not in RELATION_CONFIDENCES:
                errors.append(f"invalid relation confidence: {item.get('paper_id')} {target_id}")
            if relation.get("status") and relation.get("status") not in RELATION_STATUSES:
                errors.append(f"invalid relation status: {item.get('paper_id')} {target_id}")
            if relation.get("evidence_scope") and relation.get("evidence_scope") not in RELATION_EVIDENCE_SCOPES:
                errors.append(f"invalid relation evidence scope: {item.get('paper_id')} {target_id}")
            if relation.get("reviewed_on") and not DATE_PATTERN.match(str(relation.get("reviewed_on"))):
                errors.append(f"invalid relation reviewed_on: {item.get('paper_id')} {target_id}")
            managed = relation.get("status") == "curated" or relation.get("managed_by") == "reconcile_registry_v1"
            if managed:
                missing_provenance = [
                    field
                    for field in ("confidence", "basis", "source", "evidence_scope", "reviewed_on", "managed_by")
                    if not str(relation.get(field) or "").strip()
                ]
                if missing_provenance:
                    errors.append(
                        f"curated relation missing provenance: {item.get('paper_id')} {relation_type} {target_id}; "
                        f"missing {', '.join(missing_provenance)}"
                    )
    identifier_values: dict[tuple[str, str], list[str]] = defaultdict(list)
    for item in papers:
        for namespace, identifier in (item.get("identifiers") or {}).items():
            identifier_values[(namespace, str(identifier).casefold())].append(item.get("paper_id", ""))
    paper_by_id = {item.get("paper_id"): item for item in papers}
    incoming_by_id: dict[str, list[str]] = defaultdict(list)
    for source in papers:
        for relation in source.get("relations", []):
            target_id = relation.get("paper_id")
            if target_id:
                incoming_by_id[target_id].append(source.get("paper_id"))
    for item in papers:
        audit_registry_profiles(item, paper_ids, errors, incoming_by_id)
    note_review_index: dict[str, dict] = {}
    for spec in NOTE_REVIEW_MANIFEST_SPECS:
        note_review_index.update(audit_note_review_manifest(spec, paper_by_id, errors))
    duplicate_identifiers = {
        key: values for key, values in identifier_values.items() if len(values) > 1
    }
    unresolved_identifier_duplicates = 0
    for _, values in duplicate_identifiers.items():
        for left_index, left_id in enumerate(values):
            for right_id in values[left_index + 1 :]:
                left_relations = {
                    (relation.get("type"), relation.get("paper_id"))
                    for relation in paper_by_id.get(left_id, {}).get("relations", [])
                }
                right_relations = {
                    (relation.get("type"), relation.get("paper_id"))
                    for relation in paper_by_id.get(right_id, {}).get("relations", [])
                }
                relation_types = {"version_of", "same_work_as"}
                related = any(kind in relation_types and target == right_id for kind, target in left_relations) or any(
                    kind in relation_types and target == left_id for kind, target in right_relations
                )
                if not related:
                    unresolved_identifier_duplicates += 1
    if unresolved_identifier_duplicates:
        errors.append(f"duplicate public identifiers without explicit version relation: {unresolved_identifier_duplicates}")
    missing_notes = []
    for item in papers:
        folder = ROOT / item["folder"]
        if not path_has_exact_case(item["folder"]):
            errors.append(f"paper folder spelling/case mismatch: {item['paper_id']} {item['folder']}")
        for name in NOTE_NAMES:
            if not (folder / name).exists():
                missing_notes.append(str(folder / name))
    if missing_notes:
        errors.append(f"missing standard notes: {len(missing_notes)}")
    with (ROOT / "research" / "READING_TIERS.csv").open(newline="", encoding="utf-8") as handle:
        tiers = list(csv.DictReader(handle))
    with (ROOT / "research" / "READING_STATUS.csv").open(newline="", encoding="utf-8") as handle:
        status = list(csv.DictReader(handle))
    history_path = ROOT / "research" / "READING_STATUS_HISTORY.csv"
    history = []
    if history_path.exists():
        with history_path.open(newline="", encoding="utf-8") as handle:
            history = list(csv.DictReader(handle))
    all_reading = status + history
    reading_ids = [row.get("paper_id", "") for row in all_reading]
    if len(reading_ids) != len(set(reading_ids)):
        errors.append("duplicate paper across active tracker/history")
    counts = Counter(row["tier"] for row in tiers)
    if len(tiers) != len(papers):
        errors.append(f"tier rows {len(tiers)} != papers {len(papers)}")
    if any(row["status"] not in STATUSES for row in all_reading):
        errors.append("invalid reading status")
    if any(row.get("evidence_level") not in EVIDENCE for row in all_reading):
        errors.append("invalid evidence level")
    if len(status) != counts["CORE"] + counts["NEXT"]:
        errors.append("intensive tracker size mismatch")
    tier_by_paper_id = {row.get("paper_id", ""): row for row in tiers}
    status_by_paper_id = {row.get("paper_id", ""): row for row in status}
    expected_active_ids = {row["paper_id"] for row in tiers if row["tier"] in {"CORE", "NEXT"}}
    if set(status_by_paper_id) != expected_active_ids:
        errors.append("intensive tracker membership mismatch")
    for row in all_reading:
        tier_row = tier_by_paper_id.get(row.get("paper_id"))
        if not tier_row or row.get("tier") != tier_row["tier"]:
            errors.append(f"reading tier mismatch: {row.get('paper_id')}")
    for row in history:
        if row.get("tier") not in {"REFERENCE", "ARCHIVE"} or row.get("sequence"):
            errors.append(f"invalid inactive reading history: {row.get('paper_id')}")
    for tier in ("CORE", "NEXT"):
        sequence = [row.get("sequence") for row in status if row["tier"] == tier]
        if sequence != [str(index) for index in range(1, len(sequence) + 1)]:
            errors.append(f"non-contiguous reading sequence: {tier}")
    evidence_rank = {value: index for index, value in enumerate(["CURATION_ONLY", "ABSTRACT_CHECKED", "FULL_TEXT_CHECKED", "EXPERIMENT_CHECKED"])}
    for row in all_reading:
        paper_id = row.get("paper_id", "")
        current_status = row.get("status", "")
        required_fields = TRACKER_REQUIRED_FIELDS.get(current_status, ())
        missing_fields = [field for field in required_fields if not row.get(field, "").strip()]
        if missing_fields:
            errors.append(
                f"reading status analysis incomplete: {paper_id} {current_status}; "
                f"missing {', '.join(missing_fields)}"
            )
        minimum_evidence = MINIMUM_EVIDENCE_BY_STATUS.get(current_status)
        if minimum_evidence and row.get("evidence_level") in evidence_rank:
            if evidence_rank[row["evidence_level"]] < evidence_rank[minimum_evidence]:
                errors.append(
                    f"reading status/evidence mismatch: {paper_id} {current_status} requires {minimum_evidence}"
                )

    matrix_paths_by_track: dict[str, list[str]] = {}
    matrix_path_owner: dict[str, str] = {}
    for track, filename in SYNTHESIS_BY_TRACK.items():
        matrix_path = ROOT / "synthesis" / filename
        if not matrix_path.exists():
            errors.append(f"missing synthesis matrix: synthesis/{filename}")
            matrix_paths_by_track[track] = []
            continue
        paths = comparison_matrix_paths(matrix_path)
        matrix_paths_by_track[track] = paths
        duplicate_paths = [value for value, count in Counter(paths).items() if count > 1]
        if duplicate_paths:
            errors.append(f"duplicate comparison-matrix paper rows in {filename}: {len(duplicate_paths)}")
        for overview_path in paths:
            if overview_path not in paper_by_path:
                errors.append(f"comparison matrix points to unknown overview_path: {filename} {overview_path}")
                continue
            previous_owner = matrix_path_owner.get(overview_path)
            if previous_owner and previous_owner != filename:
                errors.append(
                    f"paper appears in multiple comparison matrices: {overview_path} ({previous_owner}, {filename})"
                )
            matrix_path_owner[overview_path] = filename

    completed_matrix_rows = 0
    for row in all_reading:
        if row.get("status") not in {"READ", "SYNTHESIZED", "REPRODUCED"}:
            continue
        paper_id = row.get("paper_id", "")
        overview_path = row.get("overview_path", "")
        item = paper_for_path(overview_path)
        track = item.get("primary_track", "") if item else row.get("primary_track", "")
        expected_matrix = matrix_paths_by_track.get(track, [])
        if overview_path not in expected_matrix:
            errors.append(
                f"completed reading paper missing from comparison matrix: {paper_id} ({track})"
            )
        else:
            completed_matrix_rows += 1
    for item in papers:
        provenance = item.get("provenance") or {}
        urls = {(item["sources"].get(key) or {}).get("url") for key in ("project", "code")} - {None}
        legacy_project = item.get("project") or ""
        if (urls or legacy_project.startswith("http")) and legacy_project not in urls:
            errors.append(f"project display disagrees with project/code sources: {item['paper_id']}")
        note_map = provenance.get("note_evidence")
        if not isinstance(note_map, dict):
            errors.append(f"missing provenance.note_evidence: {item.get('paper_id')}")
            continue
        actual_values = {}
        for name in NOTE_NAMES:
            note_path = ROOT / item["folder"] / name
            if note_path.exists():
                content = note_path.read_text(encoding="utf-8")
                title = re.search(r"(?m)^# (.+)$", content)
                displayed = re.sub(r"^(?:Overview|Problem|Method|Evaluation|Insights)\s*[-—:]\s*", "", title.group(1)) if title else ""
                if " ".join(displayed.split()) != " ".join(item["title"].split()):
                    errors.append(f"note title mismatch: {item.get('paper_id')} {name}")
                cited = re.search(r"(?im)^> .*?canonical paper source: (https?://[^;\s]+)", content)
                if cited and cited.group(1).rstrip(".") != item["page"].rstrip("."):
                    errors.append(f"note cites a stale canonical source: {item['paper_id']} {name}")
                if name == "01_overview.md":
                    for label, expected in (("Official paper", item["page"]),
                                            ("Authors", ", ".join(item.get("authors") or []))):
                        header = re.search(rf"(?m)^- {label}: (.+)$", content)
                        if expected and header and header.group(1) != expected:
                            errors.append(f"overview {label} mismatch: {item['paper_id']}")
                    project = re.search(r"(?m)^- Code/Project: (.+)$", content)
                    if project and (urls or project[1].startswith("http")) and project[1] not in urls:
                        errors.append(f"overview project/code disagrees with sources: {item['paper_id']}")
                    for label, expected in (("Tags", ", ".join(item["tags"])), ("Category", item["category"])):
                        header = re.search(rf"(?m)^- {label}: (.+)$", content)
                        if header and header.group(1) != expected:
                            errors.append(f"overview {label} mismatch: {item.get('paper_id')}")
            actual_values[name] = note_evidence_for(note_path) if note_path.exists() else "MISSING"
            if note_map.get(name) != actual_values[name]:
                errors.append(f"note evidence mismatch: {item.get('paper_id')} {name}")
        max_note = max(
            (value for value in actual_values.values() if value in evidence_rank),
            key=evidence_rank.get,
            default="CURATION_ONLY",
        )
        paper_evidence = provenance.get("content_evidence")
        if paper_evidence not in EVIDENCE:
            errors.append(f"invalid paper content evidence: {item.get('paper_id')}")
        elif evidence_rank[paper_evidence] < evidence_rank[max_note]:
            errors.append(f"paper evidence is below note evidence: {item.get('paper_id')}")
        review = provenance.get("review")
        if isinstance(review, dict) and review.get("manifest"):
            review_path = ROOT / review["manifest"]
            if not review_path.exists():
                errors.append(f"review manifest path does not exist: {item.get('paper_id')}")
        attached_note_reviews = provenance.get("note_review") or {}
        if not isinstance(attached_note_reviews, dict):
            errors.append(f"invalid provenance.note_review: {item.get('paper_id')}")
            attached_note_reviews = {}
        for note_name, attached in attached_note_reviews.items():
            if note_name not in NOTE_NAMES or not isinstance(attached, dict):
                errors.append(f"invalid note review attachment: {item.get('paper_id')} {note_name}")
                continue
            if attached.get("manifest"):
                attached_path = ROOT / attached["manifest"]
                if not attached_path.exists():
                    errors.append(f"note review manifest path does not exist: {item.get('paper_id')} {note_name}")
        expected_entry = note_review_index.get(item.get("paper_id"))
        expected_note_reviews = (
            {expected_entry["note_name"]: expected_entry}
            if expected_entry
            else {}
        )
        for note_name, expected in expected_note_reviews.items():
            attached = attached_note_reviews.get(note_name)
            if not isinstance(attached, dict):
                errors.append(f"missing note review provenance: {item.get('paper_id')} {note_name}")
                continue
            if attached.get("manifest") != expected.get("manifest") or attached.get("note_name") != note_name:
                errors.append(f"note review provenance mismatch: {item.get('paper_id')} {note_name}")
        if item.get("paper_id") in status_by_paper_id:
            tracker_evidence = status_by_paper_id[item["paper_id"]].get("evidence_level")
            if tracker_evidence != paper_evidence:
                errors.append(f"tracker/manifest evidence mismatch: {item.get('paper_id')}")
    tier_fields = set(tiers[0]) if tiers else set()
    status_fields = set(status[0]) if status else set()
    if "primary_track" not in tier_fields:
        errors.append("READING_TIERS.csv missing primary_track")
    if "primary_track" not in status_fields:
        errors.append("READING_STATUS.csv missing primary_track")
    if "paper_id" not in tier_fields:
        errors.append("READING_TIERS.csv missing paper_id")
    if "paper_id" not in status_fields:
        errors.append("READING_STATUS.csv missing paper_id")
    for row in tiers:
        item = paper_for_path(row.get("overview_path", ""))
        if not item:
            errors.append(f"tier row points to unknown overview_path: {row.get('overview_path')}")
            continue
        expected_track = item.get("primary_track") or ""
        overview_text = (ROOT / item["folder"] / "01_overview.md").read_text(encoding="utf-8")
        note_tier = re.search(r"(?m)^- Tier: (.+)$", overview_text)
        if note_tier and note_tier.group(1).strip() != row.get("tier"):
            errors.append(f"overview tier header mismatch: {item.get('paper_id')}")
        if row.get("primary_track", "") != expected_track:
            errors.append(f"primary_track mismatch in tiers: {row.get('overview_path')}")
        if row.get("paper_id", "") != item.get("paper_id", ""):
            errors.append(f"paper_id mismatch in tiers: {row.get('overview_path')}")
        if row.get("tier") in {"CORE", "NEXT"} and expected_track not in PRIMARY_TRACKS:
            errors.append(f"intensive paper missing canonical primary_track: {item.get('paper_id')}")
    for row in all_reading:
        item = paper_for_path(row.get("overview_path", ""))
        if not item:
            errors.append(f"status row points to unknown overview_path: {row.get('overview_path')}")
            continue
        if row.get("primary_track", "") != (item.get("primary_track") or ""):
            errors.append(f"primary_track mismatch in status: {row.get('overview_path')}")
        if row.get("paper_id", "") != item.get("paper_id", ""):
            errors.append(f"paper_id mismatch in status: {row.get('overview_path')}")
    catalog_counts = {
        kind: audit_catalog(path, kind, paper_ids, errors)
        for kind, path in CATALOGS.items()
    }
    resource_count = audit_resources(RESOURCES, paper_ids, errors)
    index_count = audit_registry_index(REGISTRY_INDEX, paper_by_id, errors)
    markdown_audit = audit_markdown_documents(errors)
    if not REGISTRY_STATS.exists():
        errors.append(f"missing generated registry statistics: {REGISTRY_STATS.relative_to(ROOT)}")
    queue_paths: list[str] = []
    for path in sorted((ROOT / "synthesis").glob("0*.md")):
        text = path.read_text(encoding="utf-8")
        block = text.split("<!-- READING_QUEUE:START -->", 1)[1].split("<!-- READING_QUEUE:END -->", 1)[0]
        queue_paths += re.findall(r"\]\((\.\./[^)]+/01_overview\.md)\)", block)
    expected = {".." + row["overview_path"][1:] for row in status}
    if len(queue_paths) != len(expected) or set(queue_paths) != expected:
        errors.append(f"synthesis queue mismatch: rows={len(queue_paths)}, unique={len(set(queue_paths))}, expected={len(expected)}")
    variants: dict[str, set[str]] = defaultdict(set)
    for item in papers:
        for tag in item.get("tags", []):
            variants[tag.casefold()].add(tag)
    case_variants = [value for value in variants.values() if len(value) > 1]
    if case_variants:
        errors.append(f"tag case variants: {case_variants}")
    generic = 0
    for row in status:
        if row["tier"] != "CORE":
            continue
        folder = (ROOT / urllib.parse.unquote(row["overview_path"].removeprefix("./"))).parent
        text = "\n".join((folder / name).read_text(errors="ignore") for name in NOTE_NAMES)
        generic += any(term in text for term in ("자동 추출 실패", "survey-level 해석", "paper-specific cue"))
    if generic:
        warnings.append(f"CORE papers retaining old scaffold markers: {generic}")
    matrix_count = sum(len(set(paths)) for paths in matrix_paths_by_track.values())
    print({
        "papers": len(papers), "categories": len({p['category'] for p in papers}),
        "tier_counts": dict(counts), "intensive": len(status),
        "inactive_reading_history": len(history),
        "standard_note_files": len(papers) * len(NOTE_NAMES),
        "catalog_entries": catalog_counts,
        "combined_resources": resource_count,
        "registry_index_rows": index_count,
        "normalized_taxonomy_records": taxonomy_record_count,
        "markdown_files_checked": markdown_audit["files"],
        "markdown_links_checked": markdown_audit["links"],
        "comparison_matrix_rows": matrix_count,
        "completed_matrix_rows": completed_matrix_rows,
        "errors": errors, "warnings": warnings,
    })
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
