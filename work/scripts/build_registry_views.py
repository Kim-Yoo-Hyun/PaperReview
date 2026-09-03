#!/usr/bin/env python3
"""Build compact registry views without introducing extra paper sources.

The manifest remains canonical.  This script only derives one combined
resource view and one filter-friendly paper index from the manifest, tiers,
tracker, and existing cue catalogs.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
BENCHMARK_CATALOG = ROOT / "work" / "sources" / "benchmark_catalog.json"
METRIC_CATALOG = ROOT / "work" / "sources" / "metric_catalog.json"
RESOURCES = ROOT / "work" / "sources" / "resources.json"
INDEX = ROOT / "research" / "REGISTRY_INDEX.csv"
STATS = ROOT / "research" / "REGISTRY_STATS.md"
TIERS = ROOT / "research" / "READING_TIERS.csv"
STATUS = ROOT / "research" / "READING_STATUS.csv"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def compact_hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:12]


def path_key(folder: str) -> str:
    return f"./{folder}/01_overview.md"


def read_tiers() -> dict[str, dict[str, str]]:
    with TIERS.open(newline="", encoding="utf-8") as handle:
        return {row["paper_id"]: row for row in csv.DictReader(handle)}


def read_status() -> dict[str, dict[str, str]]:
    if not STATUS.exists():
        return {}
    with STATUS.open(newline="", encoding="utf-8") as handle:
        return {row["paper_id"]: row for row in csv.DictReader(handle)}


def build_resources(papers: list[dict]) -> dict:
    entries: list[dict] = []

    for path, resource_type, source_catalog in (
        (BENCHMARK_CATALOG, "benchmark_or_dataset", "benchmark_catalog.json"),
        (METRIC_CATALOG, "metric", "metric_catalog.json"),
    ):
        if not path.exists():
            continue
        catalog = load_json(path)
        for item in catalog.get("entries", []):
            if resource_type == "benchmark_or_dataset":
                resource_id = item.get("benchmark_id")
            else:
                resource_id = item.get("metric_id")
            if not resource_id:
                continue
            entry = {
                "resource_id": resource_id,
                "resource_type": resource_type,
                "name": item.get("name", resource_id),
                "aliases": item.get("aliases", []),
                "family": item.get("family"),
                "paper_references": item.get("paper_references", []),
                "evidence": "cue_only",
                "source_catalog": source_catalog,
            }
            if resource_type == "metric":
                entry["default_direction"] = item.get("default_direction")
            entries.append(entry)

    code_by_url: dict[str, dict] = {}
    for paper in papers:
        sources = paper.get("sources") or {}
        artifact = paper.get("artifacts") or {}
        source = sources.get("code") or sources.get("project")
        if not isinstance(source, dict) or not source.get("url"):
            continue
        url = source["url"].strip()
        key = url.casefold()
        current = code_by_url.setdefault(
            key,
            {
                "resource_id": f"code:{compact_hash(url)}",
                "resource_type": "code_or_project",
                "name": url.rstrip("/").rsplit("/", 1)[-1] or url,
                "url": url,
                "paper_ids": [],
                "availability": set(),
                "verified_on": [],
                "evidence": "manifest_link",
            },
        )
        if paper["paper_id"] not in current["paper_ids"]:
            current["paper_ids"].append(paper["paper_id"])
        current["availability"].add(artifact.get("code_status", "not_identified"))
        checked_on = (paper.get("provenance") or {}).get("metadata_checked_on")
        if checked_on:
            current["verified_on"].append(checked_on)

    for entry in code_by_url.values():
        availability = entry.pop("availability")
        entry["availability"] = (
            "released"
            if "released" in availability
            else "project_only"
            if "project_only" in availability
            else "not_released"
            if "not_released" in availability
            else "not_identified"
        )
        dates = sorted(set(entry.pop("verified_on")))
        entry["verified_on"] = dates[-1] if dates else None
        entries.append(entry)

    entries.sort(key=lambda item: item["resource_id"])
    return {
        "schema_version": "1.0",
        "generated_on": str(date.today()),
        "source_of_truth": "work/sources/papers.json plus benchmark_catalog.json and metric_catalog.json",
        "evidence_policy": "benchmark/metric references remain cue_only; code_or_project entries record linked manifest URLs and do not prove reproducibility.",
        "entries": entries,
    }


def resource_ids_by_paper(resources: dict) -> dict[str, list[str]]:
    output: dict[str, list[str]] = defaultdict(list)
    for entry in resources.get("entries", []):
        refs = entry.get("paper_references", [])
        paper_ids = [ref.get("paper_id") for ref in refs if ref.get("paper_id")]
        paper_ids += [value for value in entry.get("paper_ids", []) if value]
        for paper_id in paper_ids:
            if entry["resource_id"] not in output[paper_id]:
                output[paper_id].append(entry["resource_id"])
    return output


def build_index(papers: list[dict], resources: dict) -> list[dict[str, str]]:
    tiers = read_tiers()
    status = read_status()
    ids_by_paper = resource_ids_by_paper(resources)
    fieldnames = [
        "paper_id",
        "title",
        "year",
        "venue",
        "publication_kind",
        "publication_status",
        "category",
        "primary_track",
        "tier",
        "sequence",
        "roles",
        "facets",
        "evidence_level",
        "reading_status",
        "curation_status",
        "identifier_status",
        "primary_source_scope",
        "primary_source",
        "code_status",
        "data_status",
        "resource_ids",
        "admission_reason",
        "tier_reason",
        "outgoing_relations",
        "incoming_relation_count",
        "overview_path",
    ]
    incoming_relations: Counter[str] = Counter()
    for paper in papers:
        for relation in paper.get("relations", []):
            target_id = relation.get("paper_id")
            if target_id:
                incoming_relations[target_id] += 1
    rows = []
    for paper in sorted(papers, key=lambda item: (item["year"], item["title"].casefold())):
        paper_id = paper["paper_id"]
        tier = tiers.get(paper_id, {})
        tracker = status.get(paper_id, {})
        publication = paper.get("publication") or {}
        provenance = paper.get("provenance") or {}
        curation = paper.get("curation") or {}
        sources = paper.get("sources") or {}
        primary = sources.get("primary") or {}
        rows.append(
            {
                "paper_id": paper_id,
                "title": paper["title"],
                "year": str(paper["year"]),
                "venue": publication.get("venue", paper.get("venue", "")),
                "publication_kind": publication.get("kind", ""),
                "publication_status": publication.get("status", ""),
                "category": paper.get("category", ""),
                "primary_track": paper.get("primary_track") or "",
                "tier": tier.get("tier", ""),
                "sequence": tier.get("sequence", ""),
                "roles": ";".join(curation.get("roles", [])),
                "facets": json.dumps(paper.get("facets", {}), ensure_ascii=False, separators=(",", ":")),
                "evidence_level": tracker.get("evidence_level") or provenance.get("content_evidence", ""),
                "reading_status": tracker.get("status") or "N/A",
                "curation_status": curation.get("rationale_status", ""),
                "identifier_status": provenance.get("identifier_status", "source_only"),
                "primary_source_scope": provenance.get("primary_source_scope", ""),
                "primary_source": primary.get("url", ""),
                "code_status": (paper.get("artifacts") or {}).get("code_status", ""),
                "data_status": (paper.get("artifacts") or {}).get("data_status", ""),
                "resource_ids": ";".join(sorted(ids_by_paper.get(paper_id, []))),
                "admission_reason": curation.get("admission_reason") or "",
                "tier_reason": curation.get("tier_reason") or "",
                "outgoing_relations": json.dumps(
                    [
                        {
                            "type": relation.get("type"),
                            "paper_id": relation.get("paper_id"),
                            "confidence": relation.get("confidence"),
                        }
                        for relation in paper.get("relations", [])
                    ],
                    ensure_ascii=False,
                    separators=(",", ":"),
                ),
                "incoming_relation_count": str(incoming_relations.get(paper_id, 0)),
                "overview_path": path_key(paper["folder"]),
            }
        )
    return fieldnames, rows


def build_stats(papers: list[dict], resources: dict, rows: list[dict[str, str]]) -> str:
    def table(title: str, counter: Counter) -> list[str]:
        lines = [f"## {title}", "", "| Value | Count |", "|---|---:|"]
        lines.extend(f"| {key or '(empty)'} | {value} |" for key, value in counter.most_common())
        return lines + [""]

    tier = Counter(row["tier"] for row in rows)
    evidence = Counter(row["evidence_level"] for row in rows)
    status = Counter(row["reading_status"] for row in rows if row["reading_status"] != "N/A")
    rationale = Counter(row["curation_status"] for row in rows)
    identifiers = Counter(row["identifier_status"] for row in rows)
    sources = Counter(row["primary_source_scope"] for row in rows)
    roles = Counter(role for row in rows for role in row["roles"].split(";") if role)
    publication = Counter(row["publication_kind"] for row in rows)
    code = Counter(row["code_status"] for row in rows)
    data = Counter(row["data_status"] for row in rows)
    relation_rows = [
        (paper["paper_id"], relation)
        for paper in papers
        for relation in paper.get("relations", [])
    ]
    relations = len(relation_rows)
    relation_types = Counter(relation.get("type", "") for _, relation in relation_rows)
    relation_confidence = Counter(relation.get("confidence", "") for _, relation in relation_rows)
    relation_scopes = Counter(relation.get("evidence_scope", "") for _, relation in relation_rows)
    outgoing_papers = {paper_id for paper_id, _ in relation_rows}
    target_papers = {relation.get("paper_id") for _, relation in relation_rows if relation.get("paper_id")}
    paper_by_id = {paper["paper_id"]: paper for paper in papers}

    def relation_paper_label(paper_id: str) -> str:
        paper = paper_by_id.get(paper_id) or {}
        title = str(paper.get("title") or "unknown paper").replace("|", "\\|")
        return f"`{paper_id}` {title}"
    missing_note_evidence = Counter()
    for paper in papers:
        for name, value in (paper.get("provenance", {}).get("note_evidence") or {}).items():
            if value == "MISSING":
                missing_note_evidence[name] += 1
    lines = [
        "# Registry Statistics",
        "",
        f"- Generated: {date.today()} KST",
        "- Source: [papers.json](../work/sources/papers.json)",
        "- This is a generated diagnostic view; edit the manifest, tracker, or tier generator instead.",
        "",
        "## Snapshot",
        "",
        f"- Papers: **{len(papers)}**",
        f"- Resources in the combined view: **{len(resources.get('entries', []))}**",
        f"- Curated relation edges: **{relations}**",
        f"- Papers with outgoing relations: **{len(outgoing_papers)}**",
        f"- Papers participating in a relation: **{len(outgoing_papers | target_papers)}**",
        f"- Papers without DOI/arXiv/OpenReview identifier: **{sum(value == 'source_only' for value in identifiers.elements())}**",
        "",
    ]
    lines += table("Tier", tier)
    lines += table("Evidence level", evidence)
    lines += table("Reading status (intensive set)", status)
    lines += table("Curation rationale status", rationale)
    lines += table("Curation roles", roles)
    lines += table("Publication kind", publication)
    lines += table("Identifier status", identifiers)
    lines += table("Primary source scope", sources)
    lines += table("Code status", code)
    lines += table("Data status", data)
    lines += table("Relation type", relation_types)
    lines += table("Relation confidence", relation_confidence)
    lines += table("Relation evidence scope", relation_scopes)
    lines += [
        "## Curated relation edges",
        "",
        "The manifest is the source of truth; this table is a compact human-readable edge view.",
        "",
        "| From paper | Relation | To paper | Confidence | Evidence scope |",
        "|---|---|---|---|---|",
    ]
    for source_id, relation in sorted(
        relation_rows,
        key=lambda item: (
            relation_paper_label(item[0]).casefold(),
            str(item[1].get("type") or ""),
            relation_paper_label(str(item[1].get("paper_id") or "")).casefold(),
        ),
    ):
        lines.append(
            f"| {relation_paper_label(source_id)} | `{relation.get('type', '')}` | "
            f"{relation_paper_label(str(relation.get('paper_id') or ''))} | "
            f"`{relation.get('confidence', '')}` | `{relation.get('evidence_scope', '')}` |"
        )
    lines += [""]
    lines += ["## Note evidence gaps", "", "| Note | Missing evidence header |", "|---|---:|"]
    lines.extend(f"| {name} | {count} |" for name, count in sorted(missing_note_evidence.items()))
    lines += ["", "## Interpretation", "", "- `reading_status` is user-controlled and is intentionally independent from `evidence_level`.", "- Facets are curation cues for filtering; exact task, split, metric, and failure claims remain in the paper notes.", "- `benchmark_catalog.json` and `metric_catalog.json` remain cue-only navigation inputs; the combined resource view does not promote them to verified evaluation evidence.", "- Relation edges are directed curation links, not an exhaustive citation graph: a method points to a predecessor/data dependency, while a baseline points to the evaluated paper. Managed edges retain a basis, source, confidence, evidence scope, and review date.", ""]
    return "\n".join(lines)


def build(apply: bool) -> dict:
    papers = load_json(MANIFEST)
    resources = build_resources(papers)
    fieldnames, rows = build_index(papers, resources)
    stats = build_stats(papers, resources, rows)
    result = {
        "mode": "apply" if apply else "dry-run",
        "papers": len(papers),
        "resources": len(resources["entries"]),
        "index_rows": len(rows),
        "relations": sum(len(paper.get("relations", [])) for paper in papers),
    }
    if not apply:
        return result
    RESOURCES.write_text(json.dumps(resources, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with INDEX.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    STATS.write_text(stats + "\n", encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write resources and generated registry views")
    args = parser.parse_args()
    print(json.dumps(build(args.apply), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
