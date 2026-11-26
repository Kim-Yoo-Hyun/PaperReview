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
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
BENCHMARK_CATALOG = ROOT / "work" / "sources" / "benchmark_catalog.json"
METRIC_CATALOG = ROOT / "work" / "sources" / "metric_catalog.json"
RESOURCES = ROOT / "work" / "sources" / "resources.json"
INDEX = ROOT / "research" / "REGISTRY_INDEX.csv"
STATS = ROOT / "research" / "REGISTRY_STATS.md"
TIERS = ROOT / "research" / "READING_TIERS.csv"
STATUS = ROOT / "research" / "READING_STATUS.csv"
STATUS_HISTORY = ROOT / "research" / "READING_STATUS_HISTORY.csv"


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
    records = {}
    for path in (STATUS_HISTORY, STATUS):
        if path.exists():
            with path.open(newline="", encoding="utf-8") as handle:
                records.update({row["paper_id"]: row for row in csv.DictReader(handle)})
    return records


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
        link_dates = (source.get("verified_on"), (paper.get("provenance") or {}).get("metadata_checked_on"))
        current["verified_on"].extend(date_checked for date_checked in link_dates if date_checked)

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


def build_index(papers: list[dict], resources: dict) -> tuple[list[str], list[dict[str, str]]]:
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
        "evaluation_type",
        "evaluation_settings",
        "evaluation_protocol",
        "benchmark_cues",
        "metric_cues",
        "reproducibility_status",
        "checkpoint_status",
        "configuration_status",
        "environment_status",
        "run_conditions_status",
        "lineage_status",
        "lineage_outgoing_count",
        "lineage_incoming_count",
        "lineage_candidate_count",
        "resource_ids",
        "admission_reason",
        "tier_reason",
        "outgoing_relations",
        "incoming_relation_count",
        "overview_path",
        "tags",
        "aliases",
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
        evaluation = paper.get("evaluation_profile") or {}
        evaluation_protocol = evaluation.get("protocol") or {}
        reproducibility = paper.get("reproducibility") or {}
        lineage = paper.get("lineage_profile") or {}
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
                "sequence": tracker.get("sequence", "") if tier.get("tier") in {"CORE", "NEXT"} else "",
                "roles": ";".join(curation.get("roles", [])),
                "facets": json.dumps(paper.get("facets", {}), ensure_ascii=False, separators=(",", ":")),
                "evidence_level": tracker.get("evidence_level") or provenance.get("content_evidence", ""),
                "reading_status": tracker.get("status") or "N/A",
                "curation_status": curation.get("rationale_status", ""),
                "identifier_status": "identified" if any(paper.get("identifiers", {}).values()) else "source_only",
                "primary_source_scope": primary.get("scope") or provenance.get("primary_source_scope", ""),
                "primary_source": primary.get("url", ""),
                "code_status": (paper.get("artifacts") or {}).get("code_status", ""),
                "data_status": (paper.get("artifacts") or {}).get("data_status", ""),
                "evaluation_type": evaluation.get("type", ""),
                "evaluation_settings": ";".join(evaluation.get("settings", [])),
                "evaluation_protocol": json.dumps(evaluation_protocol, ensure_ascii=False, separators=(",", ":")),
                "benchmark_cues": json.dumps(evaluation.get("benchmark_cues", []), ensure_ascii=False, separators=(",", ":")),
                "metric_cues": json.dumps(evaluation.get("metric_cues", []), ensure_ascii=False, separators=(",", ":")),
                "reproducibility_status": reproducibility.get("status", ""),
                "checkpoint_status": (reproducibility.get("checkpoint") or {}).get("status", ""),
                "configuration_status": (reproducibility.get("configuration") or {}).get("status", ""),
                "environment_status": (reproducibility.get("environment") or {}).get("status", ""),
                "run_conditions_status": (reproducibility.get("run_conditions") or {}).get("status", ""),
                "lineage_status": lineage.get("status", ""),
                "lineage_outgoing_count": str(len(lineage.get("outgoing_paper_ids", []))),
                "lineage_incoming_count": str(len(lineage.get("incoming_paper_ids", []))),
                "lineage_candidate_count": str(
                    len(set(lineage.get("queue_adjacency_paper_ids", []))
                    | set(lineage.get("legacy_summary_candidate_paper_ids", [])))
                ),
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
                "tags": ";".join(paper.get("tags", [])),
                "aliases": ";".join(paper.get("aliases", [])),
            }
        )
    return fieldnames, rows


def build_stats(papers: list[dict], resources: dict, rows: list[dict[str, str]]) -> str:
    def distribution(values) -> str:
        return " · ".join(f"`{name or 'unknown'}` {count:,}" for name, count in Counter(values).most_common())

    today = datetime.now(ZoneInfo("Asia/Seoul")).date()
    tiers = Counter(row["tier"] for row in rows)
    active = Counter(row["reading_status"] for row in rows if row["tier"] in {"CORE", "NEXT"})
    history = Counter(row["reading_status"] for row in rows
                      if row["tier"] not in {"CORE", "NEXT"} and row["reading_status"] != "N/A")
    years = Counter(paper["year"] for paper in papers)
    recent = range(today.year - 2, today.year + 1)
    venues = Counter(paper["venue_canonical"] for paper in papers).most_common(8)
    relations = [(paper["paper_id"], edge) for paper in papers for edge in paper.get("relations", [])]
    sources = {source for source, _ in relations}
    targets = {edge["paper_id"] for _, edge in relations if edge.get("paper_id")}
    trial_cues = sum(json.loads(row["evaluation_protocol"]).get("trials_or_seeds") == "reported" for row in rows)
    source_only = sum(row["identifier_status"] == "source_only" for row in rows)
    missing_notes = sum(value == "MISSING" for paper in papers
                        for value in (paper.get("provenance", {}).get("note_evidence") or {}).values())
    lines = [
        "# 레지스트리 통계", "",
        f"{today} KST 기준 **{len(papers):,}편**. 연도·발표처·태그를 조합해 찾을 때는 [검색 색인](./REGISTRY_INDEX.csv), "
        "교정 후 오류율과 미확인 항목은 [원문 감사](./SOURCE_AUDIT.md)를 사용한다.", "",
        "## 등록 분포", "",
        "| 등급 | 편수 |", "|---|---:|",
        *(f"| {tier} | {tiers[tier]} |" for tier in ("CORE", "NEXT", "REFERENCE", "ARCHIVE")), "",
        "| 등록 연도 | 편수 |", "|---|---:|",
        *(f"| {year} | {years[year]} |" for year in recent),
        f"| 그 밖의 연도 | {len(papers) - sum(years[y] for y in recent)} |", "",
        "| 발표처·공개처 | 편수 |", "|---|---:|",
        *(f"| {venue} | {count} |" for venue, count in venues),
        f"| 그 밖의 발표처·공개처 | {len(papers) - sum(count for _, count in venues)} |", "",
        "프리프린트는 등록한 공개 연도를 따른다. 등급별 선정 이유는 [읽기 계획](./READING_PLAN.md)에 있다.", "",
        "## 읽기 상태", "",
        "| 사용자 기록 | 현재 정독 대상 | 이전 정독 대상 |", "|---|---:|---:|",
        *(f"| {status} | {active[status]} | {history[status]} |"
          for status in ("UNREAD", "SKIMMED", "READ", "SYNTHESIZED", "REPRODUCED")),
        f"| 합계 | {sum(active.values())} | {sum(history.values())} |", "",
        "이전 대상의 분석은 재편입 시 복원된다. [현재 기록](./READING_STATUS.csv) · [이전 기록](./READING_STATUS_HISTORY.csv)", "",
        "## 원문과 공개 자료", "",
        "| 확인 범위 | 원장 분포 |", "|---|---|",
        f"| 판본 유형 | {distribution(row['publication_kind'] for row in rows)} |",
        f"| 문헌 검토 근거 | {distribution(p.get('provenance', {}).get('content_evidence') for p in papers)} |",
        f"| 코드 배포 | {distribution(row['code_status'] for row in rows)} |",
        f"| 데이터 배포 | {distribution(row['data_status'] for row in rows)} |",
        f"| 체크포인트 기록 | {distribution(row['checkpoint_status'] for row in rows)} |", "",
        f"DOI·arXiv·OpenReview ID 없이 원문 주소로 식별한 논문은 {source_only}편, 근거가 `MISSING`으로 표시된 표준 노트는 {missing_notes}개다. "
        "코드·데이터의 `not_identified`는 공개 여부 미확인, 체크포인트의 `reported`는 노트에 관련 기록이 있다는 뜻이다. "
        "논문별 판정에는 [감사 원장](../work/sources/batches/source_audit_2026_11.jsonl)을 참조한다.", "",
        "## 평가 자료와 인용 관계", "",
        f"[통합 자료 목록](../work/sources/resources.json)에 벤치마크·지표·배포처 {len(resources.get('entries', []))}개가 있다. "
        f"시행 횟수나 시드가 검색 단서로 기록된 논문은 {trial_cues}편이다. 실제 평가 분할·지표·실행 조건은 해당 논문의 평가 노트에서 확인한다.", "",
        f"원장의 방향성 있는 관계 {len(relations)}개는 출발 논문 {len(sources)}편, 양끝을 합쳐 {len(sources | targets)}편에 걸친다. "
        "색인의 `outgoing_relations`에서 상대 ID를 찾고 원장의 `relations`에서 관계 방향·유형·근거를 확인한다. "
        "[논문 원장](../work/sources/papers.json) · [OpenVLA 인용 계보](./OPENVLA_LINEAGE.md)", "",
    ]
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
