#!/usr/bin/env python3
"""Migrate the paper manifest to the structured PaperReview registry schema.

The default mode is a dry-run. The migration never downloads, deletes, or
rewrites paper notes; it only enriches the machine-readable manifest and the
small manifest metadata file when ``--apply`` is supplied.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

try:
    from normalize_taxonomy import registry
    from registry_schema import MIGRATION_DATE, SCHEMA_VERSION, enrich_record
    from taxonomy import canonicalize
except ModuleNotFoundError:
    from .normalize_taxonomy import registry
    from .registry_schema import MIGRATION_DATE, SCHEMA_VERSION, enrich_record
    from .taxonomy import canonicalize


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
META = ROOT / "work" / "sources" / "registry_meta.json"
TIERS = ROOT / "research" / "READING_TIERS.csv"
REGISTRY = ROOT / "PAPER.md"


def load_tier_context() -> dict[str, tuple[str, str]]:
    if not TIERS.exists():
        return {}
    with TIERS.open(newline="", encoding="utf-8") as handle:
        return {
            row.get("overview_path", ""): (row.get("tier", ""), row.get("track", ""))
            for row in csv.DictReader(handle)
            if row.get("overview_path")
        }


def migrate(papers: list[dict], *, root: Path = ROOT) -> list[dict]:
    context = load_tier_context()
    used_ids = {item.get("paper_id") for item in papers if item.get("paper_id")}
    next_id = max(
        [int(value.removeprefix("pr-")) for value in used_ids if str(value).startswith("pr-") and str(value)[3:].isdigit()]
        or [0]
    ) + 1
    output = []
    for original in papers:
        item = dict(original)
        canonicalize(item)
        path = f"./{item['folder']}/01_overview.md"
        tier, detailed_track = context.get(path, ("", ""))
        paper_id = item.get("paper_id")
        if not paper_id:
            paper_id = f"pr-{next_id:04d}"
            next_id += 1
        enriched = enrich_record(
            item,
            paper_id=paper_id,
            detailed_track=detailed_track if tier in {"CORE", "NEXT"} else None,
            root=root,
            migrated_on=MIGRATION_DATE,
        )
        output.append(enriched)
    return output


def build_meta(count: int) -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "manifest": "work/sources/papers.json",
        "schema": "work/sources/registry.schema.json",
        "generated_on": MIGRATION_DATE,
        "paper_count": count,
        "identity_policy": "paper_id is the stable internal identity; DOI/arXiv/OpenReview identifiers are optional public identifiers.",
        "version_policy": "Use relations with type=version_of or same_work_as when a preprint and publication must remain separate.",
        "evidence_policy": "Manifest provenance records source scope; note evidence and reading status are not inferred from local PDF presence.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write the enriched manifest and registry metadata")
    parser.add_argument("--no-registry", action="store_true", help="do not refresh the generated PAPER.md")
    args = parser.parse_args()

    papers = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if not isinstance(papers, list):
        raise SystemExit("papers.json must be a JSON list")
    migrated = migrate(papers)
    changed = sum(before != after for before, after in zip(papers, migrated))
    ids = {item.get("paper_id") for item in migrated}
    tracks = {item.get("primary_track") for item in migrated if item.get("primary_track")}
    print(
        {
            "mode": "apply" if args.apply else "dry-run",
            "papers": len(migrated),
            "records_changed": changed,
            "stable_ids": len(ids),
            "primary_tracks": len(tracks),
            "structured_fields": ["paper_id", "identifiers", "publication", "sources", "artifacts", "primary_track", "curation", "provenance"],
        }
    )
    if not args.apply:
        return
    MANIFEST.write_text(json.dumps(migrated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    META.write_text(json.dumps(build_meta(len(migrated)), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not args.no_registry:
        REGISTRY.write_text(registry(migrated), encoding="utf-8")


if __name__ == "__main__":
    main()
