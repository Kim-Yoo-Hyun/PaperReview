#!/usr/bin/env python3
"""Read-only integrity audit for the PaperReview literature system."""

from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
import urllib.parse
from collections import Counter, defaultdict
from pathlib import Path

try:
    from registry_schema import PRIMARY_TRACKS, SCHEMA_VERSION, validate_record_shape
except ModuleNotFoundError:
    from .registry_schema import PRIMARY_TRACKS, SCHEMA_VERSION, validate_record_shape


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
NOTE_NAMES = ["01_overview.md", "02_problem.md", "03_method.md", "04_evaluation.md", "05_insights.md"]
STATUSES = {"UNREAD", "SKIMMED", "READ", "SYNTHESIZED", "REPRODUCED"}
EVIDENCE = {"CURATION_ONLY", "ABSTRACT_CHECKED", "FULL_TEXT_CHECKED", "EXPERIMENT_CHECKED"}
CATALOGS = {
    "benchmark": ROOT / "work" / "sources" / "benchmark_catalog.json",
    "metric": ROOT / "work" / "sources" / "metric_catalog.json",
}


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().casefold()
    return re.sub(r"[^a-z0-9]+", "", value)


def valid_http(value: str | None) -> bool:
    return bool(value and re.match(r"^https?://", value, flags=re.IGNORECASE))


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
    if not meta_path.exists():
        errors.append("missing registry_meta.json")
    else:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        if meta.get("schema_version") != SCHEMA_VERSION or meta.get("paper_count") != len(papers):
            errors.append("registry metadata schema/count mismatch")
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
    paper_by_path = {
        f"./{p['folder']}/01_overview.md": p
        for p in papers
        if p.get("folder")
    }

    def paper_for_path(path: str) -> dict | None:
        return paper_by_path.get(path) or paper_by_path.get(urllib.parse.unquote(path))

    for item in papers:
        intensive = False
        # The tier lookup below is authoritative for whether a canonical track
        # is required; validate the nested shape here and refine it after CSV load.
        shape_errors = validate_record_shape(item, intensive=intensive)
        if shape_errors:
            errors.append(f"{item.get('title', '<untitled>')} registry schema: {', '.join(shape_errors)}")
        if item.get("page") and not valid_http(item.get("page")):
            errors.append(f"invalid primary source URL: {item.get('paper_id')}")
        for relation in item.get("relations", []):
            if relation.get("paper_id") not in paper_ids:
                errors.append(f"relation points to unknown paper_id: {item.get('paper_id')}")
    identifier_values: dict[tuple[str, str], list[str]] = defaultdict(list)
    for item in papers:
        for namespace, identifier in (item.get("identifiers") or {}).items():
            identifier_values[(namespace, str(identifier).casefold())].append(item.get("paper_id", ""))
    paper_by_id = {item.get("paper_id"): item for item in papers}
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
        for name in NOTE_NAMES:
            if not (folder / name).exists():
                missing_notes.append(str(folder / name))
    if missing_notes:
        errors.append(f"missing standard notes: {len(missing_notes)}")
    with (ROOT / "research" / "READING_TIERS.csv").open(newline="", encoding="utf-8") as handle:
        tiers = list(csv.DictReader(handle))
    with (ROOT / "research" / "READING_STATUS.csv").open(newline="", encoding="utf-8") as handle:
        status = list(csv.DictReader(handle))
    counts = Counter(row["tier"] for row in tiers)
    if len(tiers) != len(papers):
        errors.append(f"tier rows {len(tiers)} != papers {len(papers)}")
    if any(row["status"] not in STATUSES for row in status):
        errors.append("invalid reading status")
    if any(row.get("evidence_level") not in EVIDENCE for row in status):
        errors.append("invalid evidence level")
    if len(status) != counts["CORE"] + counts["NEXT"]:
        errors.append("intensive tracker size mismatch")
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
        if row.get("primary_track", "") != expected_track:
            errors.append(f"primary_track mismatch in tiers: {row.get('overview_path')}")
        if row.get("paper_id", "") != item.get("paper_id", ""):
            errors.append(f"paper_id mismatch in tiers: {row.get('overview_path')}")
        if row.get("tier") in {"CORE", "NEXT"} and expected_track not in PRIMARY_TRACKS:
            errors.append(f"intensive paper missing canonical primary_track: {item.get('paper_id')}")
    for row in status:
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
        folder = (ROOT / row["overview_path"].lstrip("./")).parent
        text = "\n".join((folder / name).read_text(errors="ignore") for name in NOTE_NAMES)
        generic += any(term in text for term in ("자동 추출 실패", "survey-level 해석", "paper-specific cue"))
    if generic:
        warnings.append(f"CORE papers retaining old scaffold markers: {generic}")
    print({
        "papers": len(papers), "categories": len({p['category'] for p in papers}),
        "tier_counts": dict(counts), "intensive": len(status),
        "standard_note_files": len(papers) * len(NOTE_NAMES),
        "catalog_entries": catalog_counts,
        "errors": errors, "warnings": warnings,
    })
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
