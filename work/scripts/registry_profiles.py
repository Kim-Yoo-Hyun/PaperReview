#!/usr/bin/env python3
"""Build conservative paper-level evaluation, reproducibility, and lineage profiles.

The profiles are deliberately smaller than a second paper database.  They turn
the existing full-text note structure, manifest links, cue catalogs, and
curated relations into queryable fields while keeping unresolved claims
explicitly unresolved.  A cue in ``04_evaluation.md`` is never promoted to a
verified benchmark, metric, or reproducibility claim by this module.
"""

from __future__ import annotations

import json
import hashlib
import re
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any


PROFILE_VERSION = "1.0"
PROFILE_DATE = str(date.today())

EVALUATION_SETTINGS = {
    "real_robot",
    "simulation",
    "benchmark_or_dataset",
    "source_reported",
    "scope_unresolved",
    "not_recorded",
}
PROTOCOL_STATUSES = {"reported", "not_reported", "not_recorded"}
REPRO_STATUSES = {"reported", "not_reported", "not_recorded"}
ARTIFACT_STATUSES = {
    "released",
    "project_only",
    "not_released",
    "not_identified",
    "not_recorded",
    "not_applicable",
}
LINEAGE_STATUSES = {
    "curated_edges",
    "candidate_only",
    "no_curated_edge_recorded",
}

NOTE_NAMES = (
    "01_overview.md",
    "02_problem.md",
    "03_method.md",
    "04_evaluation.md",
    "05_insights.md",
)

EVALUATION_TYPE_RE = re.compile(
    r"^- \*\*Evaluation type:\*\*\s*`([^`]+)`\s*\.?\s*$", re.MULTILINE
)
ANCHOR_RE = re.compile(r"\bp\.\s*\d+\b|extractive body cue|PDF body", re.IGNORECASE)
TRIAL_RE = re.compile(
    r"(?P<count>\d[\d,]*)\s+(?P<unit>total\s+)?(?P<kind>rollouts?|episodes?|trials?|seeds?|runs?)",
    re.IGNORECASE,
)
RANDOM_SEED_RE = re.compile(r"(?P<count>\d[\d,]*)\s+random\s+seeds?", re.IGNORECASE)


def _section(text: str, heading: str) -> str:
    """Return one level-2 note section, excluding the next level-2 section."""

    match = re.search(
        rf"^##\s+{re.escape(heading)}\s*$",
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    if not match:
        return ""
    remainder = text[match.end() :]
    next_heading = re.search(r"^##\s+", remainder, flags=re.MULTILINE)
    return remainder[: next_heading.start()] if next_heading else remainder


def _body_lines(section: str) -> list[str]:
    lines: list[str] = []
    for raw in section.splitlines():
        line = raw.strip()
        if not line or line.startswith(">"):
            continue
        if line.startswith("|---") or line.startswith("| ---"):
            continue
        if line.startswith("- Exact success denominator"):
            continue
        if line.startswith("- Names are treated as evaluation resources"):
            continue
        if line.startswith("| Audit field") or line.startswith("| Trials/episodes/seeds"):
            continue
        lines.append(line)
    return lines


def _has_anchor(section: str) -> bool:
    return bool(ANCHOR_RE.search(section))


def _section_status(section: str, *, no_cue: tuple[str, ...] = ()) -> str:
    if not section:
        return "not_recorded"
    lines = _body_lines(section)
    body = "\n".join(lines)
    if not body or not _has_anchor(body):
        lowered = body.casefold()
        if any(pattern.casefold() in lowered for pattern in no_cue):
            return "not_reported"
        return "not_recorded"
    lowered = body.casefold()
    if any(pattern.casefold() in lowered for pattern in no_cue) and not re.search(
        r"\bp\.\s*\d+\b|extractive body cue", body, flags=re.IGNORECASE
    ):
        return "not_reported"
    return "reported"


def _evaluation_type(text: str) -> str:
    match = EVALUATION_TYPE_RE.search(text)
    return match.group(1).strip() if match else "not_recorded"


def _settings(evaluation_type: str) -> list[str]:
    normalized = evaluation_type.casefold()
    if "real-robot" in normalized or "hardware" in normalized:
        return ["real_robot"]
    if "simulation" in normalized:
        return ["simulation"]
    if "benchmark" in normalized or "dataset" in normalized:
        return ["benchmark_or_dataset"]
    if "source-reported" in normalized:
        return ["source_reported"]
    if "scope unresolved" in normalized:
        return ["scope_unresolved"]
    return ["not_recorded"]


def _trial_evidence(text: str, source_note: str) -> list[dict[str, Any]]:
    """Extract only explicitly numbered trial/seed cues, retaining raw text."""

    evidence: list[dict[str, Any]] = []
    sections = "\n".join(
        _section(text, heading)
        for heading in (
            "Experimental Matrix",
            "Main Results / Claim–Evidence Map",
            "Statistics, Efficiency, and Reproducibility",
        )
    )
    for raw_line in sections.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("| Audit field"):
            continue
        matches = list(TRIAL_RE.finditer(line)) + list(RANDOM_SEED_RE.finditer(line))
        for match in matches:
            count = int(match.group("count").replace(",", ""))
            unit = match.groupdict().get("kind") or "random seeds"
            unit = unit.casefold().rstrip("s")
            if "seed" in match.group(0).casefold():
                unit = "seed"
            record = {
                "count": count,
                "unit": unit,
                "text": line[:280],
                "source": source_note,
                "basis": "04_evaluation.md body cue; exact condition remains paper-specific",
            }
            if record not in evidence:
                evidence.append(record)
            if len(evidence) >= 12:
                return evidence
    return evidence


def _cue_resources(path: Path, catalog_name: str, id_key: str) -> dict[str, list[dict[str, str]]]:
    by_paper: dict[str, list[dict[str, str]]] = defaultdict(list)
    if not path.exists():
        return by_paper
    payload = json.loads(path.read_text(encoding="utf-8"))
    for entry in payload.get("entries", []):
        resource_id = entry.get(id_key)
        if not resource_id:
            continue
        for reference in entry.get("paper_references", []):
            paper_id = reference.get("paper_id")
            if not paper_id:
                continue
            value = {
                "resource_id": resource_id,
                "name": entry.get("name", resource_id),
                "evidence": "cue_only",
                "source": reference.get("source") or "04_evaluation.md",
            }
            if value not in by_paper[paper_id]:
                by_paper[paper_id].append(value)
    return by_paper


def _explicit_data_status(text: str, paper_type: str, benchmark_cues: list[dict]) -> tuple[str, str]:
    """Classify only explicit artifact statements; otherwise keep it unknown."""

    # Restrict the search to a generous but local window around data words so
    # a sentence such as "we release code" cannot become a data release claim.
    data_release = re.compile(
        r"(?:dataset|data(?:set)?|demonstration(?:s)?|trajectory data|robot data)"
        r"[^.\n]{0,120}(?:publicly\s+)?(?:available|released|open[- ]source|open sourced)"
        r"|(?:publicly\s+)?(?:release|released|open[- ]source|open sourced)"
        r"[^.\n]{0,120}(?:dataset|data(?:set)?|demonstration(?:s)?|trajectory data|robot data)",
        flags=re.IGNORECASE,
    )
    data_not_released = re.compile(
        r"(?:dataset|data(?:set)?|demonstration(?:s)?|trajectory data|robot data)"
        r"[^.\n]{0,120}(?:not\s+(?:publicly\s+)?(?:available|released)|unavailable|not\s+released)",
        flags=re.IGNORECASE,
    )
    if data_not_released.search(text):
        return "not_released", "note_cue"
    if data_release.search(text):
        return "released", "note_cue"
    if benchmark_cues:
        return "not_identified", "full_text_note_audited; no explicit data artifact release statement"
    if paper_type == "theory_or_foundation":
        return "not_applicable", "paper_type and evaluation note scope; no data artifact cue"
    return "not_identified", "full_text note audited; no explicit data artifact status identified"


def _checkpoint_status(text: str) -> tuple[str, str]:
    not_released = re.compile(
        r"(?:checkpoint|model weights?|pretrained weights?).{0,100}"
        r"(?:not\s+(?:publicly\s+)?(?:available|released)|unavailable|not\s+released)",
        flags=re.IGNORECASE,
    )
    released = re.compile(
        r"(?:we|authors?|the paper)\s+(?:publicly\s+)?(?:release|released|open[- ]source|open sourced)"
        r"[^.\n]{0,100}(?:checkpoint|model weights?|pretrained weights?)"
        r"|(?:checkpoint|model weights?|pretrained weights?)[^.\n]{0,100}"
        r"(?:publicly\s+)?(?:available|released)",
        flags=re.IGNORECASE,
    )
    if not_released.search(text):
        return "not_released", "note_cue"
    if released.search(text):
        return "reported", "note_cue"
    return "not_recorded", "no explicit checkpoint availability cue"


def _repro_status(text: str, headings: tuple[str, ...], needles: tuple[str, ...]) -> str:
    section = "\n".join(_section(text, heading) for heading in headings)
    if not section or not _has_anchor(section):
        return "not_recorded"
    body = section.casefold()
    return "reported" if any(needle.casefold() in body for needle in needles) else "not_recorded"


def _queue_adjacency(text: str, title_to_id: dict[str, str]) -> list[str]:
    values: list[str] = []
    pattern = re.compile(
        r"\*\*Reading (?:predecessor|successor) in the generated track queue:\*\*\s*(.+?)\s*"
        r"\(queue adjacency, not a confirmed citation\)",
        flags=re.IGNORECASE,
    )
    for match in pattern.finditer(text):
        label = match.group(1).strip()
        if label.casefold() == "not recorded":
            continue
        paper_id = title_to_id.get(label.casefold())
        if paper_id and paper_id not in values:
            values.append(paper_id)
    return values


def _legacy_summary_candidates(summary: Any, papers: list[dict]) -> list[str]:
    """Return exact title matches only; do not turn short labels into edges."""

    if not isinstance(summary, str) or not summary.strip():
        return []
    normalized = re.sub(r"[^a-z0-9]+", "", summary.casefold())
    values: list[str] = []
    for paper in papers:
        title = paper.get("title", "")
        title_key = re.sub(r"[^a-z0-9]+", "", title.casefold())
        if paper.get("paper_id") and len(title_key) >= 28 and title_key in normalized:
            values.append(paper["paper_id"])
    return values


def _source_url(paper: dict) -> str | None:
    sources = paper.get("sources") or {}
    primary = sources.get("primary")
    if isinstance(primary, dict) and primary.get("url"):
        return primary["url"]
    return paper.get("page") or None


def enrich_profiles(
    papers: list[dict],
    root: Path,
    *,
    reviewed_on: str | None = None,
) -> dict[str, int]:
    """Attach complete profiles to every paper and return coverage counters."""

    reviewed_on = reviewed_on or str(date.today())
    benchmark_by_paper = _cue_resources(
        root / "work" / "sources" / "benchmark_catalog.json",
        "benchmark",
        "benchmark_id",
    )
    metric_by_paper = _cue_resources(
        root / "work" / "sources" / "metric_catalog.json",
        "metric",
        "metric_id",
    )
    title_to_id = {paper.get("title", "").casefold(): paper.get("paper_id") for paper in papers}

    incoming: dict[str, list[str]] = defaultdict(list)
    for paper in papers:
        for relation in paper.get("relations", []):
            target_id = relation.get("paper_id")
            if target_id:
                incoming[target_id].append(paper.get("paper_id"))

    counters = {
        "evaluation_profiles": 0,
        "reproducibility_profiles": 0,
        "lineage_profiles": 0,
        "data_released": 0,
        "data_not_released": 0,
        "data_not_identified": 0,
        "data_not_applicable": 0,
        "trial_cue_papers": 0,
        "curated_lineage_papers": 0,
        "lineage_candidate_papers": 0,
        "lineage_unlinked_papers": 0,
    }

    for paper in papers:
        folder = root / paper["folder"]
        evaluation_path = folder / "04_evaluation.md"
        evaluation_text = evaluation_path.read_text(encoding="utf-8", errors="ignore") if evaluation_path.exists() else ""
        source_note = f"{paper['folder']}/04_evaluation.md" if evaluation_path.exists() else None
        evaluation_type = _evaluation_type(evaluation_text)
        benchmark_cues = benchmark_by_paper.get(paper.get("paper_id"), [])
        metric_cues = metric_by_paper.get(paper.get("paper_id"), [])
        sections = {
            "dataset_or_benchmark": _section(evaluation_text, "Dataset / Benchmark Role"),
            "metrics": _section(evaluation_text, "Metrics and Success Definition"),
            "baselines": _section(evaluation_text, "Baselines and Fairness"),
            "ablations": _section(evaluation_text, "Ablations and Sensitivity"),
            "generalization": _section(evaluation_text, "Generalization and Failure Cases"),
            "statistics": _section(evaluation_text, "Statistics, Efficiency, and Reproducibility"),
        }
        protocol = {
            "dataset_or_benchmark": _section_status(
                sections["dataset_or_benchmark"], no_cue=("not stated or recoverable", "not found")
            ),
            "metrics": _section_status(sections["metrics"], no_cue=("not reported", "not found")),
            "baselines": _section_status(sections["baselines"], no_cue=("no baseline sentence selected", "not found")),
            "ablations": _section_status(sections["ablations"], no_cue=("not reported", "not found")),
            "split_or_generalization": _section_status(
                sections["generalization"], no_cue=("not reported", "not found")
            ),
            "trials_or_seeds": "reported" if _trial_evidence(evaluation_text, source_note or "") else "not_recorded",
            "statistics": _section_status(sections["statistics"], no_cue=("not reported", "not found")),
            "failure_cases": _section_status(sections["generalization"], no_cue=("not reported", "not found")),
        }
        trials = _trial_evidence(evaluation_text, source_note or "")
        if trials:
            counters["trial_cue_papers"] += 1
        evaluation_profile = {
            "profile_version": PROFILE_VERSION,
            "status": "structured_note_cues" if evaluation_path.exists() else "not_recorded",
            "type": evaluation_type,
            "settings": _settings(evaluation_type),
            "protocol": protocol,
            "trial_evidence": trials,
            "benchmark_cues": benchmark_cues,
            "metric_cues": metric_cues,
            "source_note": source_note,
            "reviewed_on": reviewed_on,
            "basis": (
                "04_evaluation.md body-derived section cues; benchmark and metric links remain cue_only; "
                "unresolved role, split, aggregation, and condition are not promoted to verified metadata."
            ),
        }
        paper["evaluation_profile"] = evaluation_profile
        counters["evaluation_profiles"] += 1

        artifact = dict(paper.get("artifacts") or {})
        data_status, data_basis = _explicit_data_status(
            evaluation_text,
            paper.get("paper_type", ""),
            benchmark_cues,
        )
        if artifact.get("data_status") not in ARTIFACT_STATUSES or artifact.get("data_status") in {
            None,
            "not_recorded",
        }:
            artifact["data_status"] = data_status
        else:
            data_status = artifact["data_status"]
            data_basis = "existing manifest artifact status preserved"
        paper["artifacts"] = artifact
        checkpoint_status, checkpoint_basis = _checkpoint_status(
            "\n".join(
                (folder / name).read_text(encoding="utf-8", errors="ignore")
                for name in ("01_overview.md", "03_method.md", "04_evaluation.md")
                if (folder / name).exists()
            )
        )
        sources = paper.get("sources") or {}
        code_source = sources.get("code") or sources.get("project")
        code_url = code_source.get("url") if isinstance(code_source, dict) else None
        environment_status = _repro_status(
            evaluation_text,
            ("Embodiment / Environment",),
            ("robot/hardware/simulator", "task/environment", "observation/sensor"),
        )
        run_conditions_status = "reported" if protocol["trials_or_seeds"] == "reported" or protocol["statistics"] == "reported" else "not_recorded"
        reproducibility = {
            "profile_version": PROFILE_VERSION,
            "status": "metadata_audited",
            "code": {
                "status": artifact.get("code_status", "not_identified"),
                "source": code_url,
                "evidence": "manifest_link" if code_url else "not_identified",
            },
            "data": {
                "status": data_status,
                "source": None,
                "evidence": data_basis,
            },
            "checkpoint": {"status": checkpoint_status, "evidence": checkpoint_basis},
            "configuration": {
                "status": _repro_status(
                    "\n".join(
                        (folder / name).read_text(encoding="utf-8", errors="ignore")
                        for name in ("03_method.md", "04_evaluation.md")
                        if (folder / name).exists()
                    ),
                    ("Temporal and Runtime Contract", "Statistics, Efficiency, and Reproducibility"),
                    ("hyperparameter", "learning rate", "control rate", "implementation", "random seed"),
                ),
                "evidence": "note_cue_or_not_recorded",
            },
            "environment": {"status": environment_status, "evidence": "04_evaluation.md section cue"},
            "run_conditions": {"status": run_conditions_status, "evidence": "04_evaluation.md trial/statistics cue"},
            "reviewed_on": reviewed_on,
            "source_note": source_note,
            "basis": (
                "manifest artifact links plus full-text evaluation/method note cues; availability is not a claim "
                "of reproducible execution unless an explicit source or experiment check exists."
            ),
        }
        paper["reproducibility"] = reproducibility
        counters["reproducibility_profiles"] += 1
        counters[f"data_{data_status}"] = counters.get(f"data_{data_status}", 0) + 1

    for paper in papers:
        paper_id = paper.get("paper_id")
        outgoing = [relation.get("paper_id") for relation in paper.get("relations", []) if relation.get("paper_id")]
        incoming_ids = sorted(set(incoming.get(paper_id, [])))
        queue_ids = _queue_adjacency(
            (root / paper["folder"] / "05_insights.md").read_text(encoding="utf-8", errors="ignore")
            if (root / paper["folder"] / "05_insights.md").exists()
            else "",
            title_to_id,
        )
        summary_candidates = _legacy_summary_candidates(paper.get("lineage"), papers)
        if outgoing or incoming_ids:
            status = "curated_edges"
            counters["curated_lineage_papers"] += 1
        elif queue_ids or summary_candidates:
            status = "candidate_only"
            counters["lineage_candidate_papers"] += 1
        else:
            status = "no_curated_edge_recorded"
            counters["lineage_unlinked_papers"] += 1
        paper["lineage_profile"] = {
            "profile_version": PROFILE_VERSION,
            "status": status,
            "outgoing_paper_ids": outgoing,
            "incoming_paper_ids": incoming_ids,
            "queue_adjacency_paper_ids": queue_ids,
            "legacy_summary_candidate_paper_ids": summary_candidates,
            "legacy_summary_present": bool(isinstance(paper.get("lineage"), str) and paper.get("lineage").strip()),
            "audited_on": reviewed_on,
            "audit_scope": "all_registry",
            "basis": (
                "manifest relations are curated edges; queue adjacency and legacy lineage matches are retained "
                "as non-relational candidates. Absence of an edge is not a claim that the paper has no citations."
            ),
        }
        counters["lineage_profiles"] += 1
    return counters


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Enrich papers.json with conservative registry profiles")
    parser.add_argument("--apply", action="store_true", help="write the manifest and registry metadata")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    manifest_path = root / "work" / "sources" / "papers.json"
    meta_path = root / "work" / "sources" / "registry_meta.json"
    papers = json.loads(manifest_path.read_text(encoding="utf-8"))
    counters = enrich_profiles(papers, root)
    counters["papers"] = len(papers)
    counters["mode"] = "apply" if args.apply else "dry-run"
    print(json.dumps(counters, ensure_ascii=False, indent=2))
    if not args.apply:
        return
    manifest_path.write_text(json.dumps(papers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        meta["metadata_profile_version"] = PROFILE_VERSION
        meta["metadata_profile_reviewed_on"] = str(date.today())
        meta["evaluation_profile_count"] = counters["evaluation_profiles"]
        meta["reproducibility_profile_count"] = counters["reproducibility_profiles"]
        meta["lineage_profile_count"] = counters["lineage_profiles"]
        meta["manifest_sha256"] = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
        meta["relation_count"] = sum(len(paper.get("relations", [])) for paper in papers)
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
