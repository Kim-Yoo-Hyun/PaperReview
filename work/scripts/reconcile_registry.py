#!/usr/bin/env python3
"""Reconcile registry evidence, curation facets, identities, and relations.

This is deliberately a small migration layer.  The JSON manifest remains the
canonical paper entity store; review manifests and the reading tracker are
inputs, while the generated index/resource view is built separately.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import urllib.parse
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

try:
    from registry_schema import (
        CURATION_ROLES,
        FACET_KEYS,
        publication_kind,
        publication_status,
        venue_id_for,
    )
except ModuleNotFoundError:
    from .registry_schema import (
        CURATION_ROLES,
        FACET_KEYS,
        publication_kind,
        publication_status,
        venue_id_for,
    )


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
META = ROOT / "work" / "sources" / "registry_meta.json"
TIERS = ROOT / "research" / "READING_TIERS.csv"
STATUS = ROOT / "research" / "READING_STATUS.csv"
REVIEW_MANIFESTS = [
    (ROOT / "work" / "sources" / "fulltext_review_manifest.json", "historical"),
    (ROOT / "work" / "sources" / "fulltext_reference_reinforcement_2026-09-02_review_manifest.json", "reference"),
    (ROOT / "work" / "sources" / "fulltext_core_next_review_manifest.json", "current"),
]
REVIEW_SCOPE_PRIORITY = {"historical": 0, "reference": 1, "current": 2}

EVIDENCE_RANK = {
    "CURATION_ONLY": 0,
    "ABSTRACT_CHECKED": 1,
    "FULL_TEXT_CHECKED": 2,
    "EXPERIMENT_CHECKED": 3,
}
VALID_EVIDENCE = set(EVIDENCE_RANK)
GENERIC_RATIONALE = (
    "Retained from the existing registry for broad literature coverage; "
    "paper-specific admission rationale requires manual review."
)

# Only high-confidence, directed curation edges are seeded here.  They are
# not a replacement for a full citation graph.  The source and basis fields
# make the distinction explicit and allow later manual promotion/demotion.
RELATION_SEEDS = [
    {
        "from": "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control",
        "type": "extends",
        "to": "RT-1: Robotics Transformer for Real-World Control at Scale",
        "basis": "named follow-up in the robot-policy lineage; verify against the paper references",
        "confidence": "inferred",
    },
    {
        "from": "Octo: An Open-Source Generalist Robot Policy",
        "type": "uses_dataset",
        "to": "Open X-Embodiment: Robotic Learning Datasets and RT-X Models",
        "basis": "the Octo record identifies Open X-Embodiment as its pretraining data lineage",
        "confidence": "manual",
    },
    {
        "from": "OpenVLA: An Open-Source Vision-Language-Action Model",
        "type": "uses_dataset",
        "to": "Open X-Embodiment: Robotic Learning Datasets and RT-X Models",
        "basis": "the OpenVLA record identifies Open X-Embodiment as its robot-data source",
        "confidence": "manual",
    },
    {
        "from": "π0.5: a Vision-Language-Action Model with Open-World Generalization",
        "type": "extends",
        "to": "π0: A Vision-Language-Action Flow Model for General Robot Control",
        "basis": "explicit model-version lineage in the paper title and official publication path",
        "confidence": "manual",
    },
    {
        "from": "GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots",
        "type": "extends",
        "to": "NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots",
        "basis": "explicit improved-version lineage in the official NVIDIA model pages",
        "confidence": "manual",
    },
    {
        "from": "GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots",
        "type": "extends",
        "to": "GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots",
        "basis": "explicit improved-version lineage in the official NVIDIA model pages",
        "confidence": "manual",
    },
    {
        "from": "Demonstrating GPU Parallelized Robot Simulation and Rendering for Generalizable Embodied AI with ManiSkill3",
        "type": "extends",
        "to": "ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations",
        "basis": "named ManiSkill3 evolution of the ManiSkill simulator/benchmark family",
        "confidence": "inferred",
    },
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def normalized_url(value: str | None) -> str:
    return (value or "").strip().casefold()


def read_tier_maps() -> tuple[dict[str, str], dict[str, str], dict[str, str]]:
    tiers: dict[str, str] = {}
    tracks: dict[str, str] = {}
    sequences: dict[str, str] = {}
    with TIERS.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            path = row["overview_path"]
            tiers[path] = row["tier"]
            tracks[path] = row.get("primary_track", "")
            sequences[path] = row.get("sequence", "")
    return tiers, tracks, sequences


def read_status() -> dict[str, dict[str, str]]:
    if not STATUS.exists():
        return {}
    with STATUS.open(newline="", encoding="utf-8") as handle:
        return {row.get("paper_id", ""): row for row in csv.DictReader(handle)}


def read_reviews() -> tuple[dict[str, dict], dict[str, dict], dict[str, dict]]:
    """Return review records, note metadata, and top-level manifest metadata."""

    reviews: dict[str, dict] = {}
    scopes: dict[str, str] = {}
    manifests: dict[str, dict] = {}
    for path, scope in REVIEW_MANIFESTS:
        if not path.exists():
            continue
        payload = load_json(path)
        manifests[str(path.relative_to(ROOT))] = {
            "payload": payload,
            "scope": scope,
            "path": path,
        }
        for record in payload.get("records", []):
            paper_id = record.get("paper_id")
            if paper_id:
                # The current CORE/NEXT review takes precedence over targeted
                # reference reinforcement, which in turn takes precedence
                # over the old remaining-corpus snapshot where scopes overlap.
                if paper_id not in reviews or REVIEW_SCOPE_PRIORITY.get(scope, 0) > REVIEW_SCOPE_PRIORITY.get(scopes.get(paper_id, ""), 0):
                    reviews[paper_id] = record
                    scopes[paper_id] = scope
    return reviews, scopes, manifests


def note_evidence(folder: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for name in ("01_overview.md", "02_problem.md", "03_method.md", "04_evaluation.md", "05_insights.md"):
        path = folder / name
        if not path.exists():
            values[name] = "MISSING"
            continue
        match = re.search(r"Evidence maturity:\s*`([^`]+)`", path.read_text(encoding="utf-8", errors="ignore"))
        value = match.group(1) if match else "MISSING"
        values[name] = value if value in VALID_EVIDENCE else "MISSING"
    return values


def review_evidence(record: dict | None) -> str | None:
    if not record:
        return None
    value = record.get("evidence_level")
    if value in VALID_EVIDENCE:
        return value
    method = str(record.get("extraction_method") or "").casefold()
    basis = str(record.get("note_basis") or "").casefold()
    if "abstract only" in method or "abstract only" in basis:
        return "ABSTRACT_CHECKED"
    if record.get("status") in {"downloaded", "reused", "source_exception"}:
        return "FULL_TEXT_CHECKED"
    return None


def max_evidence(*values: str | None) -> str:
    present = [value for value in values if value in EVIDENCE_RANK]
    return max(present, key=EVIDENCE_RANK.get) if present else "CURATION_ONLY"


def text_for_facets(item: dict) -> str:
    return " ".join(
        [
            str(item.get("title") or ""),
            str(item.get("category") or ""),
            " ".join(str(tag) for tag in item.get("tags", [])),
        ]
    ).casefold()


def contains(text: str, *needles: str) -> bool:
    return any(needle.casefold() in text for needle in needles)


def build_facets(item: dict) -> dict[str, list[str]]:
    text = text_for_facets(item)
    facets = {key: [] for key in FACET_KEYS}

    def add(key: str, *values: str) -> None:
        for value in values:
            if value not in facets[key]:
                facets[key].append(value)

    if contains(text, "humanoid", "biped"):
        add("embodiment", "humanoid")
    if contains(text, "quadruped", "legged", "anymal"):
        add("embodiment", "legged")
    if contains(text, "bimanual", "dual-arm", "dual arm"):
        add("embodiment", "bimanual")
    if contains(text, "dexterous", "in-hand", "in hand", "dexterous hand"):
        add("embodiment", "dexterous_hand")
    if contains(text, "mobile manipulation", "mobile robot", "navigation"):
        add("embodiment", "mobile")
    if contains(text, "aerial", "drone", "uav"):
        add("embodiment", "aerial")
    if contains(text, "underwater"):
        add("embodiment", "underwater")
    if contains(text, "multi-robot", "multi robot"):
        add("embodiment", "multi_robot")
    if contains(text, "manipulation", "robot arm", "grasp", "assembly"):
        add("embodiment", "arm")

    if contains(text, "rgb", "image", "vision", "camera"):
        add("modality", "rgb")
    if contains(text, "depth", "rgb-d", "rgbd"):
        add("modality", "depth")
    if contains(text, "point cloud", "point-cloud", "3d geometry", "gaussian splatting", "nerf"):
        add("modality", "point_cloud")
    if contains(text, "lidar", "li-dar"):
        add("modality", "lidar")
    if contains(text, "tactile", "touch"):
        add("modality", "tactile")
    if contains(text, "force", "wrench", "impedance"):
        add("modality", "force_torque")
    if contains(text, "propriocept"):
        add("modality", "proprioception")
    if contains(text, "language", "vision-language", "vla", "instruction"):
        add("modality", "language")
    if contains(text, "video"):
        add("modality", "video")
    if contains(text, "audio"):
        add("modality", "audio")

    if contains(text, "reinforcement learning", "reinforcement", "offline rl", "policy optimization"):
        add("learning", "reinforcement_learning")
    if contains(text, "imitation learning", "behavior cloning", "demonstration"):
        add("learning", "imitation_learning")
    if contains(text, "offline rl", "offline reinforcement"):
        add("learning", "offline_rl")
    if contains(text, "diffusion policy", "action diffusion", "diffusion"):
        add("learning", "diffusion")
    if contains(text, "flow matching", "flow-based policy", "meanflow"):
        add("learning", "flow_matching")
    if contains(text, "vla", "vision-language-action"):
        add("learning", "vla")
    if contains(text, "world model", "world models"):
        add("learning", "world_model")
    if contains(text, "self-supervised", "self supervised"):
        add("learning", "self_supervised")
    if contains(text, "optimization", "optimal control", "mpc", "planning"):
        add("learning", "optimization_or_planning")

    if contains(text, "task planning", "tamp", "symbolic planning", "long-horizon planning"):
        add("control_level", "task_planning")
    if contains(text, "motion planning", "trajectory", "path planning", "rrt", "prm"):
        add("control_level", "motion_planning")
    if contains(text, "state estimation", "slam", "mapping", "perception"):
        add("control_level", "state_estimation")
    if contains(text, "policy", "visuomotor", "robot learning", "vla"):
        add("control_level", "policy")
    if contains(text, "control", "controller", "mpc", "impedance", "force control"):
        add("control_level", "feedback_control")
    if contains(text, "whole-body", "whole body"):
        add("control_level", "whole_body")
    if contains(text, "recovery", "failure detection", "safety", "barrier function"):
        add("control_level", "safety_or_recovery")

    if contains(text, "simulation", "simulator", "mujoco", "isaac", "habitat", "maniskill", "robosuite"):
        add("setting", "simulation")
    if contains(text, "real robot", "real-world", "real world", "hardware"):
        add("setting", "real_robot")
    if contains(text, "sim-to-real", "sim2real", "sim to real"):
        add("setting", "sim_to_real")
    if contains(text, "real-time", "realtime", "low latency"):
        add("setting", "real_time")
    if contains(text, "long-horizon", "long horizon", "lifelong"):
        add("setting", "long_horizon")

    if contains(text, "contact", "tactile", "force", "impedance", "peg-in-hole"):
        add("interaction", "contact_rich")
    if contains(text, "grasp", "manipulation"):
        add("interaction", "grasping")
    if contains(text, "deformable", "cloth", "soft object"):
        add("interaction", "deformable")
    if contains(text, "assembly", "insertion", "peg-in-hole"):
        add("interaction", "assembly")
    if contains(text, "locomotion", "walking", "legged"):
        add("interaction", "locomotion")
    if contains(text, "navigation", "slam", "mapping"):
        add("interaction", "navigation")
    if contains(text, "whole-body", "whole body"):
        add("interaction", "whole_body")

    return {key: sorted(values) for key, values in facets.items()}


def role_for(item: dict) -> str:
    paper_type = item.get("paper_type")
    mapping = {
        "theory_or_foundation": "foundation",
        "benchmark_or_dataset": "benchmark_or_dataset",
        "system": "system",
        "method": "method",
    }
    return mapping.get(paper_type, "method")


def generated_admission_reason(tier: str, item: dict, track: str) -> str:
    category = item.get("category") or "the selected literature scope"
    if tier == "CORE":
        return (
            f"Included in CORE as a reusable prerequisite for the {track or category} "
            "reading spine and downstream robotics comparisons."
        )
    if tier == "NEXT":
        return (
            f"Included in NEXT as a specialized or frontier extension of the "
            f"{track or category} research line after the shared CORE spine."
        )
    if tier == "REFERENCE":
        return (
            f"Retained as an on-demand reference for {category}; it is not part "
            "of the current intensive reading sequence."
        )
    return (
        f"Retained as searchable historical material for {category}; it is outside "
        "the current robotics-first intensive scope."
    )


def tier_reason(tier: str, track: str) -> str:
    if tier == "CORE":
        return f"Common foundation and prerequisite for the {track or 'robotics'} spine."
    if tier == "NEXT":
        return f"Specialized or frontier extension selected after CORE for the {track or 'robotics'} branch."
    if tier == "REFERENCE":
        return "Important on-demand reference, but not required in the current intensive sequence."
    return "Historical or adjacent material retained for search; outside the current intensive scope."


def relation_for_seed(seed: dict, ids_by_title: dict[str, str], papers_by_id: dict[str, dict]) -> tuple[str, dict] | None:
    source_id = ids_by_title.get(seed["from"])
    target_id = ids_by_title.get(seed["to"])
    if not source_id or not target_id:
        return None
    source = papers_by_id[source_id]
    return source_id, {
        "type": seed["type"],
        "paper_id": target_id,
        "confidence": seed["confidence"],
        "status": "curated",
        "basis": seed["basis"],
        "source": source.get("page") or source.get("sources", {}).get("primary", {}).get("url"),
        "managed_by": "reconcile_registry_v1",
    }


def reconcile(apply: bool) -> dict:
    papers = load_json(MANIFEST)
    original_manifest_hash = sha256(MANIFEST)
    tiers, tracks, sequences = read_tier_maps()
    status_rows = read_status()
    reviews, review_scopes, review_manifests = read_reviews()
    papers_by_id = {paper["paper_id"]: paper for paper in papers}
    ids_by_title = {paper["title"]: paper["paper_id"] for paper in papers}
    current_intensive_ids = {
        paper["paper_id"]
        for paper in papers
        if tiers.get(f"./{paper['folder']}/01_overview.md") in {"CORE", "NEXT"}
    }

    primary_url_counts = Counter(
        normalized_url((paper.get("sources") or {}).get("primary", {}).get("url"))
        for paper in papers
        if isinstance((paper.get("sources") or {}).get("primary"), dict)
    )
    shared_primary = {
        url for url, count in primary_url_counts.items() if url and count > 1
    }

    evidence_before = Counter(paper.get("provenance", {}).get("content_evidence") for paper in papers)
    evidence_after = Counter()
    generated_rationales = 0
    relation_count_before = sum(len(paper.get("relations", [])) for paper in papers)
    seeded_relations = 0
    source_index_count = 0
    no_identifier = 0
    category_values = set()

    for paper in papers:
        paper_id = paper["paper_id"]
        folder = ROOT / paper["folder"]
        tier = tiers.get(f"./{paper['folder']}/01_overview.md", "ARCHIVE")
        track = tracks.get(f"./{paper['folder']}/01_overview.md", "")
        category_values.add(paper.get("category", ""))

        publication = dict(paper.get("publication") or {})
        venue = paper.get("venue_canonical") or paper.get("venue") or publication.get("venue", "")
        kind = publication_kind(venue)
        # Only repair heuristic/unknown classifications.  Explicit
        # technical-report and preprint records remain untouched.
        if publication.get("kind") in {None, "other"} or publication.get("status") == "unverified":
            publication["kind"] = kind
            publication["status"] = publication_status(kind, venue)
        publication["venue_id"] = publication.get("venue_id") or venue_id_for(venue)
        paper["publication"] = publication

        sources = dict(paper.get("sources") or {})
        primary = sources.get("primary")
        if isinstance(primary, dict) and primary.get("url"):
            url = normalized_url(primary["url"])
            primary["scope"] = "venue_index" if url in shared_primary else "paper_specific"
            checked_on = paper.get("provenance", {}).get("metadata_checked_on")
            if checked_on:
                primary["verified_on"] = checked_on
            source_index_count += int(url in shared_primary)
            sources["primary"] = primary
        paper["sources"] = sources

        identifiers = paper.get("identifiers") or {}
        no_identifier += int(not identifiers)

        curation = dict(paper.get("curation") or {})
        role = role_for(paper)
        existing_roles = [value for value in curation.get("roles", []) if value in CURATION_ROLES]
        curation["roles"] = existing_roles or [role]
        curation["role_basis"] = curation.get("role_basis") or "paper_type_and_canonical_category"
        curation["scope_status"] = {
            "CORE": "active",
            "NEXT": "active",
            "REFERENCE": "adjacent",
            "ARCHIVE": "archive",
        }.get(tier, "archive")
        curation["tier_reason"] = tier_reason(tier, track or paper.get("primary_track", ""))
        generated_reason = curation.get("rationale_basis") == "tier_and_taxonomy_generated"
        if (
            not curation.get("admission_reason")
            or curation.get("admission_reason") == GENERIC_RATIONALE
            or generated_reason
        ):
            admission_reason = generated_admission_reason(tier, paper, track or paper.get("primary_track", ""))
            if curation.get("admission_reason") != admission_reason:
                generated_rationales += 1
            curation["admission_reason"] = admission_reason
            if curation.get("rationale_status") != "recorded":
                curation["rationale_status"] = "pending"
                curation["rationale_basis"] = "tier_and_taxonomy_generated"
        else:
            curation.setdefault("rationale_basis", "manual_curation")
        paper["curation"] = curation

        paper["facets"] = build_facets(paper)
        paper["facet_provenance"] = "curation taxonomy cue; exact task/evaluation role remains in paper notes."

        notes = note_evidence(folder)
        review = reviews.get(paper_id)
        note_max = max_evidence(*notes.values())
        review_level = review_evidence(review)
        current_level = paper.get("provenance", {}).get("content_evidence")
        overall = max_evidence(current_level, note_max, review_level)
        evidence_after[overall] += 1

        provenance = dict(paper.get("provenance") or {})
        provenance["content_evidence"] = overall
        provenance["note_evidence"] = notes
        provenance["identifier_status"] = "identified" if identifiers else "source_only"
        provenance["primary_source_scope"] = (
            "venue_index"
            if isinstance(primary, dict) and normalized_url(primary.get("url")) in shared_primary
            else "paper_specific"
        )
        if review:
            selected_scope = review_scopes.get(paper_id, "unknown")
            review_path = next(
                path for path, payload in review_manifests.items()
                if payload["scope"] == selected_scope
                and any(row.get("paper_id") == paper_id for row in payload["payload"].get("records", []))
            )
            provenance["review"] = {
                "manifest": review_path,
                "scope": selected_scope,
                "reviewed_on": review.get("reviewed_on"),
                "status": review.get("status"),
                "source_kind": review.get("source_kind"),
                "extraction_method": review.get("extraction_method"),
                "extraction_quality": review.get("extraction_quality"),
                "pages": review.get("pages"),
                "sha256": review.get("sha256"),
            }
        else:
            provenance["review"] = {"scope": "not_reviewed", "status": "not_recorded"}
        provenance["evidence_reconciliation"] = {
            "method": "review_manifest_then_note_evidence_max",
            "reconciled_on": str(date.today()),
            "tracker_status_is_independent": True,
        }
        paper["provenance"] = provenance

    # Preserve manually added relations and only add the explicitly managed
    # seed edges when an identical edge is not already present.
    for seed in RELATION_SEEDS:
        result = relation_for_seed(seed, ids_by_title, papers_by_id)
        if not result:
            continue
        source_id, relation = result
        existing = papers_by_id[source_id].setdefault("relations", [])
        if not any(
            row.get("type") == relation["type"] and row.get("paper_id") == relation["paper_id"]
            for row in existing
        ):
            existing.append(relation)
            seeded_relations += 1

    # Evidence in the intensive tracker reflects source verification, not the
    # user's reading status.  Historical review records remain valid evidence
    # when a later tier reassignment places the paper in CORE/NEXT.  Keep
    # status and all personal fields untouched.
    tracker_updates = 0
    for paper_id, row in status_rows.items():
        review = reviews.get(paper_id)
        level = review_evidence(review)
        if level and row.get("evidence_level") != level:
            row["evidence_level"] = level
            tracker_updates += 1

    # Add snapshot metadata to review manifests without rewriting their record
    # evidence.  The old 666-paper manifest is explicitly historical because
    # its tier scope predates the current registry.  The intensive manifest is
    # partial_current when a later tier expansion adds papers beyond its
    # reviewed scope.
    changed_review_manifests = {}
    review_scope_gaps = {}
    for path, payload in review_manifests.items():
        document = payload["payload"]
        record_counts = Counter(row.get("tier") for row in document.get("records", []))
        reviewed_ids = {row.get("paper_id") for row in document.get("records", []) if row.get("paper_id")}
        if payload["scope"] == "historical":
            snapshot_status = "historical"
            alignment_note = "Historical review scope; do not interpret as the current non-CORE/NEXT complement."
        elif payload["scope"] == "reference":
            snapshot_status = "reference_reinforcement"
            alignment_note = (
                "Targeted full-text reinforcement for REFERENCE papers; this manifest is not a current intensive-scope complement."
            )
        else:
            missing_ids = current_intensive_ids - reviewed_ids
            outside_ids = reviewed_ids - current_intensive_ids
            if not missing_ids and not outside_ids:
                snapshot_status = "current"
                alignment_note = "Current CORE/NEXT scope is aligned to the current tier file."
            else:
                snapshot_status = "partial_current"
                alignment_note = (
                    "Current review scope covers only a subset of the current CORE/NEXT set; "
                    "unreviewed papers remain separately provenance-labeled."
                )
            review_scope_gaps[path] = {
                "reviewed_intensive": len(reviewed_ids & current_intensive_ids),
                "current_intensive": len(current_intensive_ids),
                "unreviewed_intensive": len(current_intensive_ids - reviewed_ids),
                "reviewed_outside_intensive": len(reviewed_ids - current_intensive_ids),
            }
        document["registry_snapshot"] = {
            "status": snapshot_status,
            "paper_count_at_reconciliation": len(papers),
            "input_manifest_sha256_before_reconciliation": original_manifest_hash,
            "tier_counts_in_review": dict(record_counts),
            "current_intensive_count": len(current_intensive_ids),
            "reviewed_intensive_count": len(reviewed_ids & current_intensive_ids),
            "unreviewed_intensive_count": len(current_intensive_ids - reviewed_ids),
            "alignment_note": alignment_note,
        }
        changed_review_manifests[payload["path"]] = document

    result = {
        "mode": "apply" if apply else "dry-run",
        "papers": len(papers),
        "evidence_before": dict(evidence_before),
        "evidence_after": dict(evidence_after),
        "generated_rationales": generated_rationales,
        "relation_count_before": relation_count_before,
        "seeded_relations": seeded_relations,
        "source_index_records": source_index_count,
        "papers_without_public_identifier": no_identifier,
        "tracker_evidence_updates": tracker_updates,
        "review_manifests": [str(path.relative_to(ROOT)) for path in changed_review_manifests],
        "review_scope_gaps": review_scope_gaps,
        "categories": len(category_values),
    }
    if not apply:
        return result

    MANIFEST.write_text(json.dumps(papers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if STATUS.exists():
        fieldnames = list(next(iter(status_rows.values())).keys()) if status_rows else []
        with STATUS.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
            writer.writeheader()
            writer.writerows(status_rows.values())
    for path, document in changed_review_manifests.items():
        path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    meta = load_json(META)
    meta["paper_count"] = len(papers)
    meta["generated_on"] = str(date.today())
    meta["manifest_sha256"] = sha256(MANIFEST)
    meta["last_reconciled_on"] = str(date.today())
    meta["reconciliation_policy"] = "review manifest evidence is paper-level; per-note evidence is retained under provenance.note_evidence; tracker status remains user-controlled."
    META.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result["manifest_sha256"] = meta["manifest_sha256"]
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write reconciled manifest, tracker evidence, and review metadata")
    args = parser.parse_args()
    print(json.dumps(reconcile(args.apply), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
