#!/usr/bin/env python3
"""Normalize ``04_evaluation.md`` and build an evidence-first eval record.

All registry papers receive the same evaluation schema and lose copied
bibliographic metadata.  CORE/NEXT papers additionally receive an evaluation
matrix, dataset-role audit, embodiment/runtime fields, baseline-fairness table,
ablation plan, claim/evidence map, and statistical/reproducibility audit.

The source material is intentionally bounded.  Existing legacy cues are kept
as cues, not silently promoted to reported facts.  Missing information is
labelled ``not found``, ``not reported``, ``not applicable``, or
``verification required``.  Reading status and evidence level are never
changed by this script.  Run without ``--apply`` for a dry run.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

try:
    from migrate_problem_notes import DOMAIN_SCOPE, PROFILES as PROBLEM_PROFILES
except ModuleNotFoundError:  # import as work.scripts.migrate_evaluation_notes
    try:
        from .migrate_problem_notes import DOMAIN_SCOPE, PROFILES as PROBLEM_PROFILES
    except ImportError:
        _problem_path = Path(__file__).with_name("migrate_problem_notes.py")
        _problem_spec = importlib.util.spec_from_file_location("migrate_problem_notes", _problem_path)
        if _problem_spec is None or _problem_spec.loader is None:
            raise
        _problem_module = importlib.util.module_from_spec(_problem_spec)
        _problem_spec.loader.exec_module(_problem_module)
        DOMAIN_SCOPE = _problem_module.DOMAIN_SCOPE
        PROBLEM_PROFILES = _problem_module.PROFILES


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
STATUS = ROOT / "research" / "READING_STATUS.csv"

VALID_EVIDENCE = {
    "CURATION_ONLY",
    "ABSTRACT_CHECKED",
    "FULL_TEXT_CHECKED",
    "EXPERIMENT_CHECKED",
}

COMMON_HEADINGS = (
    "## Evaluation in One Sentence",
    "## Evaluation Type and Scope",
    "## Experimental Matrix",
    "## Dataset / Benchmark Role",
    "## Embodiment / Environment",
    "## Metrics and Success Definition",
    "## Baselines and Fairness",
    "## Ablations and Sensitivity",
    "## Main Results / Claim–Evidence Map",
    "## Generalization and Failure Cases",
    "## Statistics, Efficiency, and Reproducibility",
    "## Limitations and Verification Questions",
)

LEGACY_METADATA_PATTERNS = (
    r"(?im)^\s*-\s*Year/Venue:",
    r"(?im)^\s*-\s*Category:",
    r"(?im)^\s*-\s*Tags:",
    r"(?im)^\s*-\s*(?:Paper|Official paper):",
    r"(?im)^\s*-\s*Code/Project:",
    r"(?im)^\s*-\s*Source audit:",
    r"(?i)paper\.pdf",
)

LEGACY_BASIS_REPLACEMENTS = {
    "source PDF 또는 공식 full-text source의 problem/method/evaluation cue와 기존 note를 대조해 구조화했다; exact table/page와 trial details는 원문 확인 필요. tracker의 reading status/evidence는 변경하지 않았다.": "source PDF 또는 공식 full-text source의 problem/method formulation profile과 기존 evaluation cue를 결합해 구조화했다; exact evaluation table/page와 trial details는 원문 확인 필요. tracker의 reading status/evidence는 변경하지 않았다.",
    "검증된 저자/공식 source의 본문 cue와 기존 evaluation cue를 대조해 구조화했다; exact table/page와 trial details는 원문 확인 필요. tracker의 reading status/evidence는 변경하지 않았다.": "검증된 저자/공식 source의 problem/method formulation cue와 기존 evaluation cue를 대조해 구조화했다; exact evaluation table/page와 trial details는 원문 확인 필요. tracker의 reading status/evidence는 변경하지 않았다.",
}


EVAL_OVERRIDES: dict[str, dict[str, Any]] = {
    "A New Approach to Linear Filtering and Prediction Problems": {
        "type": "THEORY / ANALYTIC EXAMPLES",
        "scope": "filtering, prediction, smoothing의 유도와 nonstationary prediction examples; downstream robot benchmark는 현재 source에서 보고되지 않음.",
        "dataset": [("not applicable", "이론/예시 중심; dataset split 없음")],
        "metrics": [("quadratic estimation error / error covariance", "analytic objective; numeric experiment metric은 not reported")],
        "baseline": "not applicable as a learned benchmark; comparison is against the stated projection/estimation alternatives in the formulation.",
        "ablation": "not applicable as a modern component ablation; linear-Gaussian assumption sensitivity is the relevant stress test.",
    },
    "A Formal Basis for the Heuristic Determination of Minimum Cost Paths": {
        "type": "THEORY / SEARCH ANALYSIS",
        "scope": "minimum-cost path optimality와 heuristic/node-expansion properties; modern robot benchmark는 현재 source에서 보고되지 않음.",
        "dataset": [("not applicable", "graph examples/analysis; train-test split 없음")],
        "metrics": [("path cost", "primary objective"), ("node expansions / search effort", "efficiency analysis; exact values not recorded")],
        "baseline": "uninformed or other admissible search is the conceptual comparison; named experimental baseline is not reported in the current note.",
        "ablation": "heuristic admissibility/consistency and heuristic informativeness are the relevant sensitivity axes; component ablation is not applicable.",
    },
    "Planning and Acting in Partially Observable Stochastic Domains": {
        "type": "THEORY / PLANNING ALGORITHM",
        "scope": "POMDP belief-state planning, policy-tree value and Witness-style computation; current note has no named robot benchmark.",
        "dataset": [("not applicable", "formal domain/model rather than dataset evaluation")],
        "metrics": [("expected discounted return / value", "formal objective; numeric result not recorded")],
        "baseline": "fully observable planning or alternative belief/policy-tree backup is the conceptual comparison; named baseline not found.",
        "ablation": "observation uncertainty, horizon and belief representation sensitivity; reported component ablation not found.",
    },
    "A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation": {
        "type": "CONTROL THEORY / SYSTEM FORMULATION",
        "scope": "operational-space motion/force dynamics, redundancy and singularity treatment; current note does not contain a reproducible experiment table.",
        "dataset": [("not applicable", "controller formulation; dataset split 없음")],
        "metrics": [("task-space tracking and contact-force error", "control target; numeric result not recorded")],
        "baseline": "joint-space or non-operational controller is the conceptual comparison; named implementation baseline not found.",
        "ablation": "task/force selection, null-space objective and model/singularity handling; reported ablation not found.",
    },
    "Hybrid Position/Force Control of Manipulators": {
        "type": "CONTROL THEORY / SYSTEM FORMULATION",
        "scope": "natural/artificial constraint 기반 position-force subspace control; current note contains no reproducible experiment table.",
        "dataset": [("not applicable", "controller formulation; dataset split 없음")],
        "metrics": [("position tracking and contact-force error", "control target; numeric result not recorded")],
        "baseline": "pure position or pure force control is the conceptual comparison; named implementation baseline not found.",
        "ablation": "selection matrix/contact-frame and model-error sensitivity; reported component ablation not found.",
    },
    "Impedance Control: An Approach to Manipulation: Part I—Theory": {
        "type": "CONTROL THEORY / INTERACTION FORMULATION",
        "scope": "desired inertia-damping-stiffness interaction law; current note has no reproducible benchmark table.",
        "dataset": [("not applicable", "theory/controller formulation")],
        "metrics": [("motion-force interaction response / stability", "formal target; numeric result not recorded")],
        "baseline": "hard position or direct force control is the conceptual comparison; named baseline not found.",
        "ablation": "desired impedance gains and environment stiffness/bandwidth sensitivity; reported ablation not found.",
    },
    "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion": {
        "type": "EMPIRICAL / MIXED SIMULATION AND REAL ROBOT",
        "scope": "current evaluation cue reports 15 tasks across 4 manipulation benchmarks with state/image variants and simulated/real settings; exact benchmark names and table mapping require body verification.",
        "dataset": [("15 tasks / 4 robot manipulation benchmarks", "evaluation-suite cue; exact benchmark names, split and task allocation not fully resolved")],
        "metrics": [("success rate", "protocol/result cue; exact per-task aggregation not resolved")],
        "baseline": "current protocol says prior state-of-the-art robot-learning methods; named baseline/configuration is not fully recorded.",
        "ablation": "state-vs-image observation and architecture/conditioning variants are evaluation cues; exact component table not recorded.",
    },
    "Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics": {
        "type": "SYSTEM / REAL-ROBOT MOBILE MANIPULATION",
        "scope": "open-ended pick-and-drop in 10 novel real-world home environments; the current note reports a 58.5% success cue.",
        "dataset": [("10 novel real-world home environments", "evaluation environment cue; episode/task count not resolved"), ("ScanNet200 / Objaverse / LERF", "auxiliary/perception resource cue; not treated as the final robot evaluation dataset until body verification")],
        "metrics": [("open-vocabulary mobile-manipulation success rate", "reported result cue; exact denominator/trial protocol not resolved")],
        "baseline": "state-of-the-art OVMM comparison is claimed in the current cue; named baseline configurations are not recorded.",
        "ablation": "open-knowledge perception, navigation and grasping primitive contribution; reported module ablation not found in the current note.",
    },
    "PointVLA: Injecting the 3D World into Vision-Language-Action Models": {
        "type": "EMPIRICAL / SIMULATION AND REAL ROBOT VLA",
        "scope": "RoboTwin cue with simulated and real-world VLA manipulation; protocol names OpenVLA, Diffusion Policy and DexVLA comparisons.",
        "dataset": [("RoboTwin", "evaluation benchmark cue; split, task count and data-role separation require body verification")],
        "metrics": [("success rate", "evaluation metric cue; per-task aggregation not resolved")],
        "baseline": "OpenVLA, Diffusion Policy and DexVLA are named in the protocol cue; same-data/compute/observation fairness is not recorded.",
        "ablation": "3D modular feature injector and skip-block analysis are method cues; exact w/o-3D and block-level result table requires body verification.",
    },
    "VGGT: Visual Geometry Grounded Transformer": {
        "type": "EMPIRICAL / 3D VISION SYSTEM",
        "scope": "camera estimation, multi-view depth, dense point reconstruction and point tracking are named as evaluation tasks; dataset-role mapping remains unresolved.",
        "dataset": [("ScanNet / Replica / KITTI / Objaverse / DTU / ETH3D / Habitat", "legacy resource cues; train/eval/pretraining role not resolved")],
        "metrics": [("camera/depth/reconstruction/tracking metrics", "task-level target; current keyword list is not accepted as verified metric set")],
        "baseline": "MASt3R and prior multi-view systems appear in the protocol cue; exact baseline table/configuration not recorded.",
        "ablation": "multi-image processing, feature/geometry fusion and post-processing sensitivity; reported ablation not found.",
    },
}


DOMAIN_METRICS = {
    "planning": "path cost, feasibility, success/reachability, search effort",
    "estimation": "state error/MSE and uncertainty calibration",
    "control": "tracking error, force/contact error, stability and constraint violation",
    "simulation": "rollout fidelity, physical plausibility, throughput and downstream task success",
    "world_model": "prediction error, imagined-task return, calibration and horizon degradation",
    "safety": "task success, intervention rate, violation/failure probability and risk calibration",
    "vla": "task success, instruction following, generalization, latency and failure rate",
    "manipulation": "task completion, grasp/contact success, pose/force error and robustness",
    "tactile": "contact/slip success, force/pose error and recovery rate",
    "3d_perception": "geometric accuracy, semantic consistency and downstream planning/manipulation utility",
    "navigation": "goal success, SPL/path efficiency, collision and localization/replanning error",
    "locomotion": "velocity/progress, stability, energy and terrain generalization",
    "humanoid": "tracking, balance, task success, falls and recovery",
    "mobile_manipulation": "long-horizon success, reachability, collision and recovery",
    "rl": "return/task success, sample efficiency, constraint violation and stability",
    "offline_rl": "offline return, OOD action rate, calibration and closed-loop success",
    "il": "imitation error, task success, compounding error and robustness",
    "generative": "distribution fit, sample/action quality, multimodality and sampling latency",
    "robot_data": "coverage, transfer, data efficiency and downstream task success",
    "benchmark": "success/quality score, generalization, reproducibility and failure breakdown",
    "vision": "recognition/grounding quality and downstream robot utility",
    "sim2real": "real task success, stability, transfer gap and robustness",
}


def parse_sections(markdown: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in markdown.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections.setdefault(current, [])
        elif line.startswith("# ") and current is not None:
            current = None
        elif current is not None:
            sections[current].append(line)
    return {key: "\n".join(value).strip() for key, value in sections.items()}


def strip_list_marker(value: str) -> str:
    return re.sub(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)", "", value.strip()).strip()


def clean_line(value: str, limit: int = 480) -> str:
    value = strip_list_marker(value)
    value = re.sub(r"\s+", " ", value).strip()
    value = re.sub(r"\s*\.\.\.\s*", " … ", value)
    value = value.replace("paper.pdf", "원문")
    if len(value) > limit:
        value = value[: limit - 1].rstrip() + "…"
    return value


def useful_lines(block: str, limit: int = 6) -> list[str]:
    values: list[str] = []
    ignored_prefixes = (
        "year/venue:",
        "category:",
        "tags:",
        "paper link:",
        "official paper:",
        "code/project:",
        "source audit:",
        "자동 추출",
        "본문 확인 필요",
        "본문 수동 확인 필요",
        "unverified",
        "정독 시",
        "자동 추출 기준",
        "source cue와 사전 구조화",
    )
    for raw in block.splitlines():
        value = clean_line(raw)
        if not value or value.startswith((">", "|---", "| ---")):
            continue
        low = value.casefold()
        if low.startswith(ignored_prefixes) or "원문" in low and "method section" in low:
            continue
        if re.search(
            r"task number|number of demonstrations|success rate\s*:|training steps|method input\s*&\s*encoder|"
            r"success rate distribution|open-loop evaluation|\bcount\s*:\s*\d",
            low,
        ):
            continue
        numeric_tokens = re.findall(r"\b\d+(?:\.\d+)?\b", value)
        if re.search(r"\b(?:table|figure|fig\.)\s*\d", low) and len(numeric_tokens) >= 4:
            continue
        if value.startswith("|") and value.endswith("|"):
            cells = [cell.strip() for cell in value.strip("|").split("|")]
            value = " — ".join(cell for cell in cells if cell)
        if value and value not in values:
            values.append(value)
        if len(values) >= limit:
            break
    return values


def compact(values: list[str], fallback: str, limit: int = 2) -> str:
    if not values:
        return fallback
    text = " ".join(values[:limit]).strip()
    return text if text.endswith((".", "다.", "?", "!")) else text + "."


def already_normalized(markdown: str) -> bool:
    """Keep an applied note stable and avoid mining its own audit tables."""
    return (
        all(heading in markdown for heading in COMMON_HEADINGS)
        and "Canonical metadata:" in markdown
        and not any(re.search(pattern, markdown) for pattern in LEGACY_METADATA_PATTERNS)
    )


def preserve_normalized_note(markdown: str) -> str:
    """Apply harmless provenance wording fixes without re-mining audit tables."""
    for old, new in LEGACY_BASIS_REPLACEMENTS.items():
        markdown = markdown.replace(old, new)
    return markdown


def escape_cell(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value).replace("|", "\\|").replace("\n", " ")).strip()


def read_tracker() -> dict[str, dict[str, str]]:
    if not STATUS.exists():
        return {}
    result: dict[str, dict[str, str]] = {}
    with STATUS.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            overview = row.get("overview_path", "").removeprefix("./")
            if not overview:
                continue
            folder = overview.removesuffix("/01_overview.md")
            result[folder] = row
            result[folder.casefold()] = row
    return result


def resolve_folder(folder_name: str) -> Path:
    direct = ROOT / folder_name
    if direct.is_dir():
        return direct
    current = ROOT
    for part in Path(folder_name).parts:
        matches = [child for child in current.iterdir() if child.name.casefold() == part.casefold()]
        if len(matches) != 1:
            raise FileNotFoundError(folder_name)
        current = matches[0]
    return current


def extract_evidence(markdown: str) -> str:
    match = re.search(
        r"(?im)^\s*(?:>\s*)?(?:[-*]\s*)?Evidence maturity\s*:\s*(?:`([^`]+)`|([^\.\n]+))",
        markdown,
    )
    if not match:
        return ""
    value = (match.group(1) or match.group(2) or "").strip()
    return value if value in VALID_EVIDENCE else ""


def evidence_for(item: dict[str, Any], old: str, overview: str, tracker: dict[str, dict[str, str]]) -> str:
    row = tracker.get(str(item["folder"])) or tracker.get(str(item["folder"]).casefold())
    if row and row.get("evidence_level") in VALID_EVIDENCE:
        return row["evidence_level"]
    for source in (overview, old):
        value = extract_evidence(source)
        if value:
            return value
    return "CURATION_ONLY"


def basis_text(profile_data: dict[str, Any] | None) -> str:
    if profile_data is None:
        return "registry/abstract 또는 기존 evaluation cue 기반 scaffold; exact experiment detail은 본문 수동 확인 필요. tracker의 reading status/evidence는 변경하지 않았다."
    basis = profile_data.get("body_basis", "BODY_FORMULATION_REVIEWED")
    if basis.startswith("ABSTRACT"):
        return "공식 abstract/proceedings/project/program source와 기존 evaluation cue를 바탕으로 구조화했다; exact table, split, trial과 result는 본문 확인 필요. tracker의 reading status/evidence는 변경하지 않았다."
    if basis == "BODY_FORMULATION_REVIEWED_CORRECTED_SOURCE":
        return "검증된 저자/공식 source의 problem/method formulation cue와 기존 evaluation cue를 대조해 구조화했다; exact evaluation table/page와 trial details는 원문 확인 필요. tracker의 reading status/evidence는 변경하지 않았다."
    return "source PDF 또는 공식 full-text source의 problem/method formulation profile과 기존 evaluation cue를 결합해 구조화했다; exact evaluation table/page와 trial details는 원문 확인 필요. tracker의 reading status/evidence는 변경하지 않았다."


def source_cues(old: str, overview: str) -> dict[str, list[str]]:
    sections = parse_sections(old)
    overview_sections = parse_sections(overview)
    aliases = {
        "dataset": ("Dataset / Benchmark", "Dataset", "Benchmark"),
        "protocol": ("Evaluation Protocol and Results", "Main Results", "Protocol", "Evaluation Scope", "Verified Evaluation Scope"),
        "metrics": ("Metrics", "Metric"),
        "baseline": ("Baselines", "Baseline"),
        "ablation": ("Ablations", "Ablation", "Failure and Reproducibility"),
        "repro": ("Reproducibility Notes", "Limitations and Reproducibility", "Reproducible Minimum"),
        "failure": ("Failure and Reproducibility", "Limitations and Reproducibility", "Manual Review Needed"),
    }
    result: dict[str, list[str]] = {}
    for key, names in aliases.items():
        values: list[str] = []
        for name in names:
            values.extend(useful_lines(sections.get(name, ""), 8))
        result[key] = list(dict.fromkeys(values))[:8]
    if not result["protocol"]:
        result["protocol"] = useful_lines(
            overview_sections.get("Evaluation Scope", ""), 4
        )
    return result


def source_location(section: str, *, detail: str = "evaluation cue") -> str:
    if not section:
        return f"04_evaluation.md {detail}; exact section/table/figure/page 확인 필요"
    return f"04_evaluation.md `{section}`; exact table/figure/page 확인 필요"


def section_name(markdown: str, aliases: tuple[str, ...]) -> str:
    sections = parse_sections(markdown)
    for name in aliases:
        if sections.get(name, "").strip():
            return name
    return ""


def line_section(markdown: str, aliases: tuple[str, ...]) -> tuple[str, str]:
    sections = parse_sections(markdown)
    for name in aliases:
        value = sections.get(name, "").strip()
        if value:
            return name, value
    return "", ""


def infer_type(title: str, domain: str, cues: dict[str, list[str]]) -> str:
    override = EVAL_OVERRIDES.get(title, {}).get("type")
    if override:
        return override
    text = " ".join(sum(cues.values(), [])).casefold()
    if domain == "benchmark" or "benchmark" in title.casefold() or "environment" in title.casefold():
        return "BENCHMARK / INFRASTRUCTURE"
    if any(token in text for token in ("theoretical", "theorem", "derivation", "analytic", "mathematical", "conceptual")):
        return "THEORY / ANALYTIC OR SYSTEM FORMULATION"
    if any(token in text for token in ("real robot", "real-world", "hardware", "physical robot", "on the robot")):
        return "SYSTEM / REAL-ROBOT OR MIXED"
    return "EMPIRICAL / LEARNING OR SIMULATION"


def scope_for(profile_data: dict[str, Any] | None, item: dict[str, Any]) -> tuple[str, str, str, str, str]:
    if profile_data:
        return tuple(DOMAIN_SCOPE.get(profile_data.get("domain", "general"), DOMAIN_SCOPE["general"]))  # type: ignore[return-value]
    return (
        f"{item.get('category', 'paper-specific')} task/system",
        "observation/input은 본문 확인 필요",
        "state/latent/evaluation state는 본문 확인 필요",
        "prediction/plan/action은 본문 확인 필요",
        "primary metric과 closed-loop utility는 본문 확인 필요",
    )


def profile_domain(profile_data: dict[str, Any] | None) -> str:
    return profile_data.get("domain", "general") if profile_data else "general"


def extract_numeric_context(values: list[str], patterns: tuple[str, ...]) -> str:
    for value in values:
        for pattern in patterns:
            match = re.search(pattern, value, re.I)
            if match:
                return match.group(0)
    return ""


def method_modules(folder: Path, domain: str) -> list[str]:
    path = folder / "03_method.md"
    if path.exists():
        text = path.read_text(errors="ignore")
        block = text.split("## Pipeline", 1)[-1].split("## Objective / Update Rule", 1)[0]
        modules: list[str] = []
        for line in block.splitlines():
            if not line.startswith("|") or line.startswith("|---") or "Module" in line:
                continue
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if cells and cells[0] and cells[0] not in modules:
                modules.append(cells[0].replace("\\|", "|"))
        if modules:
            return modules[:4]
    return {
        "planning": ["state/search representation", "search or optimization", "feasibility/execution"],
        "control": ["task/error representation", "dynamics/constraint solve", "feedback/actuation"],
        "vla": ["multimodal encoding", "action decoder", "receding execution"],
        "3d_perception": ["geometry extraction", "semantic/temporal fusion", "robot query"],
        "rl": ["policy/value", "rollout target", "parameter update"],
    }.get(domain, ["input representation", "core method", "output/feedback"])


def dataset_records(title: str, profile_data: dict[str, Any] | None, cues: dict[str, list[str]], eval_type: str) -> list[tuple[str, str, str]]:
    override = EVAL_OVERRIDES.get(title, {}).get("dataset")
    if override:
        return [(str(resource), str(role), "override/profile cue; exact source location 확인 필요") for resource, role in override]
    lines = cues.get("dataset", [])
    protocol_text = " ".join(cues.get("protocol", [])).casefold()
    if not lines:
        if "not applicable" in eval_type.casefold() or eval_type.startswith("THEORY"):
            return [("not applicable", "theory/system formulation or no dataset cue in current note", "not applicable")]
        return [("not found", "dataset/benchmark name is not recorded in the current evaluation note", "본문 확인 필요")]
    records: list[tuple[str, str, str]] = []
    for line in lines[:6]:
        resource = line
        role = "legacy dataset/benchmark cue; train/eval/pretraining/auxiliary role unresolved"
        if line.casefold() in protocol_text:
            role = "mentioned in protocol cue; evaluation role and split still require body verification"
        records.append((resource, role, source_location("Dataset / Benchmark", detail="dataset role cue")))
    return records


def metric_records(title: str, profile_data: dict[str, Any] | None, cues: dict[str, list[str]], domain: str) -> list[tuple[str, str, str]]:
    override = EVAL_OVERRIDES.get(title, {}).get("metrics")
    if override:
        return [(str(metric), str(role), "profile/protocol cue; exact metric definition/table 확인 필요") for metric, role in override]
    values = cues.get("metrics", [])[:6]
    protocol = " ".join(cues.get("protocol", []))
    if not values:
        values = [line for line in cues.get("protocol", []) if re.search(r"success|accuracy|error|loss|return|reward|rate|SPL|IoU|mAP|PSNR|SSIM|ATE|RPE|collision|precision|recall|F1", line, re.I)][:3]
    records: list[tuple[str, str, str]] = []
    for value in values:
        if len(value.split()) <= 5 and value.casefold() not in protocol.casefold():
            role = "legacy keyword cue; metric role and direction not verified"
        else:
            role = "protocol/evaluation cue; exact definition, direction and aggregation require body verification"
        records.append((value, role, source_location("Metrics", detail="metric cue")))
    target = DOMAIN_METRICS.get(domain, "primary task metric and failure/latency measures")
    if not records:
        records.append((target, "evaluation target inferred from problem scope, not a reported result", "02 problem scope; exact paper metric 확인 필요"))
    elif domain not in {"general", "benchmark"}:
        records.append((target, "downstream metric target; not claimed as paper-reported metric", "02 problem scope; exact paper metric 확인 필요"))
    return records[:6]


def baseline_records(title: str, cues: dict[str, list[str]], eval_type: str) -> list[tuple[str, str, str, str]]:
    override = EVAL_OVERRIDES.get(title, {}).get("baseline")
    if override:
        return [(str(override), "comparison identity/claim", "not reported", "override/protocol cue; exact baseline table 확인 필요")]
    values = list(cues.get("baseline", []))
    for line in cues.get("protocol", []):
        if re.search(r"baseline|compare|compared|against|prior|state[- ]of[- ]the[- ]art|SOTA|previous", line, re.I):
            values.append(line)
    values = list(dict.fromkeys(values))[:5]
    if not values:
        if eval_type.startswith("THEORY") or "FORMULATION" in eval_type:
            values = ["not applicable / conceptual comparison only"]
        else:
            values = ["not found in current note"]
    return [
        (value, "comparison identity or claimed comparison", "not reported", source_location("Baselines", detail="baseline cue"))
        for value in values
    ]


def ablation_records(title: str, cues: dict[str, list[str]], modules: list[str], domain: str, eval_type: str) -> list[tuple[str, str, str, str]]:
    override = EVAL_OVERRIDES.get(title, {}).get("ablation")
    records: list[tuple[str, str, str, str]] = []
    if override:
        records.append((str(override), modules[1] if len(modules) > 1 else modules[0], "isolate the paper-specific mechanism", "cue; exact ablation table 확인 필요"))
    for line in cues.get("ablation", []) + cues.get("protocol", []):
        if re.search(r"ablat|w/o|without|remove|variant|component|sensitivity|necessity|deconstruct", line, re.I):
            records.append((line, modules[1] if len(modules) > 1 else modules[0], "reported/candidate component comparison", "legacy cue; reported status and result require body verification"))
    dedup: list[tuple[str, str, str, str]] = []
    seen: set[str] = set()
    for record in records:
        if record[0] not in seen:
            dedup.append(record)
            seen.add(record[0])
    if not dedup:
        if eval_type.startswith("THEORY") or "FORMULATION" in eval_type:
            dedup.append(("not applicable; assumption/sensitivity analysis is the relevant comparison", modules[1] if len(modules) > 1 else modules[0], "test formulation boundary", "not reported in current note"))
        else:
            dedup.append(("not reported — remove the core module while holding data/input/compute fixed", modules[1] if len(modules) > 1 else modules[0], "causal attribution of the core module", "minimum audit to run; not a paper-reported ablation"))
    if len(dedup) < 3 and not eval_type.startswith("THEORY"):
        factors = {
            "vla": "input modality or action horizon variant",
            "3d_perception": "3D geometry/semantic fusion variant",
            "tactile": "vision-only versus tactile/force input",
            "locomotion": "adaptation/history or privileged-input variant",
            "world_model": "rollout horizon/model-prediction variant",
        }
        factor = factors.get(domain, "data scale, observation or runtime variant")
        dedup.append((f"not reported — {factor}", modules[0], "sensitivity to the main interface assumption", "minimum audit to run; not a paper-reported ablation"))
    return dedup[:5]


def render_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for row in rows:
        lines.append("| " + " | ".join(escape_cell(value) for value in row) + " |")
    return "\n".join(lines)


def explicit_trial_seed(cues: dict[str, list[str]]) -> tuple[str, str, str]:
    all_lines = sum(cues.values(), [])
    trial = extract_numeric_context(all_lines, (r"(?:\d+\s+)?(?:trials?|episodes?|runs?)\s*(?:=|:)?\s*\d+", r"\bN\s*=\s*\d+", r"\bn\s*=\s*\d+"))
    seed = extract_numeric_context(all_lines, (r"(?:\d+\s+)?seeds?\s*(?:=|:)?\s*\d+", r"random seeds?\s*(?:=|:)?\s*\d+"))
    stats = ""
    for value in all_lines:
        if "±" in value or re.search(r"mean|standard deviation|confidence interval|std", value, re.I):
            stats = value
            break
    return trial or "not reported", seed or "not reported", stats or "not reported"


def render_experiment_matrix(
    profile_data: dict[str, Any] | None,
    scope: tuple[str, str, str, str, str],
    eval_type: str,
    cues: dict[str, list[str]],
    datasets: list[tuple[str, str, str]],
    metrics: list[tuple[str, str, str]],
    baselines: list[tuple[str, str, str, str]],
) -> str:
    protocol = cues.get("protocol", [])
    trial, seed, _ = explicit_trial_seed(cues)
    setting_text = " ".join(protocol[:2])
    low = setting_text.casefold()
    if "simulat" in low and ("real" in low or "physical" in low):
        setting = "mixed simulation + real cue"
    elif "simulat" in low or "sim-only" in low:
        setting = "simulation cue"
    elif "real robot" in low or "real-world" in low or "hardware" in low:
        setting = "real-robot/system cue"
    elif eval_type.startswith("THEORY"):
        setting = "analytic/formulation examples"
    else:
        setting = "setting not found in current note"
    dataset = datasets[0][0] if datasets else "not found"
    baseline = baselines[0][0] if baselines else "not found"
    metric = metrics[0][0] if metrics else scope[4]
    result = compact(protocol, "result/evidence cue not found in current note", 2)
    claim = scope[4] if profile_data else "paper-specific evaluation claim"
    source = source_location("Evaluation Protocol and Results", detail="claim/result cue")
    rows = [[claim, setting, f"{dataset}; split/role unresolved", scope[0], baseline, f"{metric}; {result}", f"trials: {trial}; seeds: {seed}", source]]
    return render_table(
        ["Experiment / claim", "Type & setting", "Dataset / split", "Robot / system", "Baseline", "Metric / result cue", "Trials / seeds", "Source"],
        rows,
    )


def render_dataset_role(records: list[tuple[str, str, str]]) -> str:
    rows = [[resource, role, "not reported", source] for resource, role, source in records]
    return render_table(["Resource", "Role", "Split / size", "Source"], rows)


def render_environment(scope: tuple[str, str, str, str, str], cues: dict[str, list[str]], eval_type: str) -> str:
    all_lines = sum(cues.values(), [])
    setting = compact(cues.get("protocol", []), "evaluation setting not found in current note", 2)
    robot = compact([line for line in all_lines if re.search(r"robot|hardware|simulator|humanoid|quadruped|arm|Franka|ANYmal|environment", line, re.I)], "robot/simulator platform not reported", 2)
    sensor = scope[1]
    rate = extract_numeric_context(all_lines, (r"\d+(?:\.\d+)?\s*Hz", r"control rate\s*(?:=|:)?\s*[^,;.]+", r"frequency\s*(?:=|:)?\s*[^,;.]+")) or "not reported"
    task = compact([line for line in cues.get("protocol", []) if re.search(r"task|benchmark|episode|environment|manipulat|navigation|control|tracking|pick|grasp", line, re.I)], "task/episode definition not found", 2)
    variation = compact([line for line in all_lines if re.search(r"novel|unseen|general|transfer|robust|varied|challenge|real-world", line, re.I)], "generalization condition not found", 2)
    rows = [
        ["Evaluation type", eval_type, "provisional classification from current source cue; verify body", "source cue / title/domain"],
        ["Robot / simulator / hardware", robot, "reported status not fully resolved", source_location("Evaluation Protocol and Results", detail="platform cue")],
        ["Observation / sensor", sensor, "scope cue from problem profile; exact sensor/calibration verify", "02 problem scope"],
        ["Control / inference rate", rate, "numeric value only if explicitly present", source_location("Evaluation Protocol and Results", detail="rate cue")],
        ["Task / episode unit", task, "task count, reset, timeout and denominator not reported unless stated", source_location("Evaluation Protocol and Results", detail="task cue")],
        ["Generalization split/variation", variation, "split and unseen dimensions require body verification", source_location("Evaluation Protocol and Results", detail="generalization cue")],
    ]
    return render_table(["Dimension", "Recorded cue", "Interpretation / missing detail", "Source"], rows)


def render_metrics(metrics: list[tuple[str, str, str]]) -> str:
    rows = [[metric, "direction/unit not reported", role, source] for metric, role, source in metrics]
    return render_table(["Metric / success signal", "Direction / unit", "Status", "Source"], rows)


def render_baselines(baselines: list[tuple[str, str, str, str]]) -> str:
    rows = [[name, tests, same, source] for name, tests, same, source in baselines]
    table = render_table(["Baseline / comparison cue", "What it should isolate", "Same data/observation/compute?", "Source"], rows)
    fairness = render_table(
        ["Fairness dimension", "Current record", "Required check"],
        [
            ["Observation/action interface", "not reported", "hold sensor modality, action space and preprocessing fixed"],
            ["Data/pretraining", "not reported", "match demonstrations, pretraining and additional labels"],
            ["Compute/runtime", "not reported", "match parameter budget, inference steps, latency and control rate"],
            ["Evaluation protocol", "not reported", "match task split, reset/timeout, seeds and success denominator"],
        ],
    )
    return table + "\n\n" + "**Baseline fairness audit**\n\n" + fairness


def render_ablations(ablations: list[tuple[str, str, str, str]]) -> str:
    rows = [[factor, component, interpretation, source] for factor, component, interpretation, source in ablations]
    return render_table(["Ablation / sensitivity factor", "Method component", "Expected interpretation", "Reported status / source"], rows)


def render_results(profile_data: dict[str, Any] | None, scope: tuple[str, str, str, str, str], cues: dict[str, list[str]], eval_type: str) -> str:
    protocol = cues.get("protocol", [])
    if protocol:
        result = compact(protocol, "", 3)
        status = "legacy protocol cue; exact main table/figure and conditions require verification"
    else:
        result = "not found in current note"
        status = "no result cue available; do not infer a result from metadata or keyword matches"
    claim = scope[4] if profile_data else "paper-specific primary claim"
    rows = [[claim, result, eval_type, status, source_location("Evaluation Protocol and Results", detail="main-result cue")]]
    return render_table(["Claim / target", "Evidence or result cue", "Evaluation type", "Strength", "Source"], rows)


def render_failure(profile_data: dict[str, Any] | None, cues: dict[str, list[str]], scope: tuple[str, str, str, str, str]) -> str:
    rows: list[list[str]] = []
    if profile_data:
        for assumption, _, failure in profile_data.get("assumptions", [])[:4]:
            rows.append([assumption, failure, "profile/formulation-derived stress test; not necessarily paper-reported", "02 problem profile; exact failure evidence verify"])
    for line in cues.get("failure", [])[:4]:
        rows.append(["legacy limitation/failure cue", line, "current note cue; source strength unresolved", source_location("Limitations and Reproducibility", detail="failure cue")])
    if not rows:
        rows.append(["paper-specific assumptions", "failure condition not reported in current note", "verification required", "본문 확인 필요"])
    return render_table(["Assumption / regime", "Failure or stress test", "Status", "Source"], rows)


def render_statistics(cues: dict[str, list[str]], eval_type: str) -> str:
    trial, seed, stats = explicit_trial_seed(cues)
    all_lines = sum(cues.values(), [])
    latency = extract_numeric_context(all_lines, (r"\d+(?:\.\d+)?\s*(?:ms|s)\b", r"latency\s*(?:=|:)?\s*[^,;.]+")) or "not reported"
    compute = compact([line for line in cues.get("repro", []) if re.search(r"GPU|CPU|compute|memory|batch|parameter|checkpoint|code|repository|hardware", line, re.I)], "not reported", 2)
    split = compact([line for line in cues.get("dataset", []) + cues.get("protocol", []) if re.search(r"split|train|test|validation|held[- ]out|unseen", line, re.I)], "not reported", 2)
    rows = [
        ["Trials / episodes", trial, "not reported means no count was found; it is not zero", source_location("Evaluation Protocol and Results", detail="trial cue")],
        ["Random seeds / repeats", seed, "not reported", source_location("Evaluation Protocol and Results", detail="seed cue")],
        ["Mean ± std / CI", stats, "not reported", source_location("Evaluation Protocol and Results", detail="statistical cue")],
        ["Latency / throughput", latency, "numeric value only if explicitly present", source_location("Reproducibility Notes", detail="efficiency cue")],
        ["Compute / hardware dependency", compute, "not reported unless current note contains a cue", source_location("Reproducibility Notes", detail="compute cue")],
        ["Train/eval split and leakage control", split, "role and split require body verification", source_location("Dataset / Benchmark", detail="split cue")],
        ["Code / checkpoint / environment", "see 01_overview.md; not duplicated here", "availability/configuration not reprinted as metadata", "01_overview.md"],
        ["Evaluation mode", eval_type, "system/theory/empirical distinction must govern what statistics are applicable", "evaluation type audit"],
    ]
    return render_table(["Reproducibility field", "Recorded value/cue", "Status", "Source"], rows)


def render_limits(profile_data: dict[str, Any] | None, datasets: list[tuple[str, str, str]], baselines: list[tuple[str, str, str, str]], ablations: list[tuple[str, str, str, str]], cues: dict[str, list[str]]) -> str:
    missing: list[str] = []
    if not datasets or datasets[0][0] in {"not found", "not applicable"}:
        missing.append("dataset/benchmark role")
    if not baselines or baselines[0][0] in {"not found in current note", "not applicable / conceptual comparison only"}:
        missing.append("baseline identity/fairness")
    if not ablations or "not reported" in ablations[0][3]:
        missing.append("reported ablation")
    trial, seed, _ = explicit_trial_seed(cues)
    if trial == "not reported" or seed == "not reported":
        missing.append("trial/seed statistics")
    lines = [
        "- **Evidence boundary:** evaluation cue를 reported result로 승격하지 않았으며, exact table/figure/page는 원문 확인이 필요하다.",
        "- **Missing comparison fields:** " + (", ".join(missing) if missing else "현재 note에서 명시적 누락을 찾지 못함; body verification remains required") + ".",
        "- **Interpretation rule:** `not applicable`은 평가 유형상 해당하지 않음을, `not found`는 현재 note에서 이름을 찾지 못했음을, `not reported`는 paper/source에서 보고 여부가 확인되지 않았음을 뜻한다.",
        "- **Do not overclaim:** success/accuracy cue만으로 generalization, robustness, causality 또는 real-robot reproducibility를 주장하지 않는다.",
    ]
    if profile_data:
        lines.append("- **Research-facing limitation:** " + profile_data.get("constraints", "paper-specific assumptions and evaluation boundary require body verification") + "")
    return "\n".join(lines)


def render_verification(profile_data: dict[str, Any] | None, eval_type: str) -> str:
    target = profile_data.get("anchor", "paper-specific experiment section") if profile_data else "paper-specific experiment section"
    return "\n".join(
        [
            f"- **Source anchor:** {target}; exact dataset table, split, baseline configuration, ablation table and result figure must be located.",
            f"- **Evaluation type check:** this note classifies the evidence as `{eval_type}`; confirm that theory/system/learning/benchmark fields are not being mixed.",
            "- **Claim–condition check:** every result must name task, embodiment/simulator, input/action interface, metric, baseline, trials/seeds and source location.",
            "- **Reproduction check:** record reset/timeout/success denominator, preprocessing, checkpoint, compute, inference/control rate and failure handling before comparing numbers.",
            "- **Statistical check:** distinguish one demonstration/episode/example from repeated trials and report uncertainty when the source provides it.",
        ]
    )


def render_intensive(
    item: dict[str, Any],
    folder: Path,
    old: str,
    overview: str,
    tracker: dict[str, dict[str, str]],
    profile_data: dict[str, Any],
) -> str:
    title = str(item["title"])
    domain = profile_domain(profile_data)
    cues = source_cues(old, overview)
    eval_type = infer_type(title, domain, cues)
    scope = scope_for(profile_data, item)
    modules = method_modules(folder, domain)
    datasets = dataset_records(title, profile_data, cues, eval_type)
    metrics = metric_records(title, profile_data, cues, domain)
    baselines = baseline_records(title, cues, eval_type)
    ablations = ablation_records(title, cues, modules, domain, eval_type)
    evidence = evidence_for(item, old, overview, tracker)
    return (
        f"# Evaluation — {title}\n\n"
        "> Canonical metadata: [01_overview.md](./01_overview.md).\n"
        f"> Evidence maturity: `{evidence}`.\n"
        f"> Analysis basis: {basis_text(profile_data)}\n\n"
        "## Evaluation in One Sentence\n\n"
        f"{EVAL_OVERRIDES.get(title, {}).get('scope', '현재 source cue에서 확인되는 evaluation은 ' + scope[4] + '를 검증하는 범위이며, exact protocol과 result는 아래 audit에서 분리한다.')}\n\n"
        "## Evaluation Type and Scope\n\n"
        f"- **Evaluation type:** `{eval_type}` (provisional; source body에서 확인 필요)\n"
        f"- **Target system/task:** {scope[0]}\n"
        f"- **Input/observation boundary:** {scope[1]}\n"
        f"- **Output/decision under evaluation:** {scope[3]}\n"
        f"- **Primary target:** {scope[4]}\n"
        "- **Scope rule:** theory/formulation papers use assumptions, theorem/analytic examples or controller behavior; empirical papers use matched task/data/baseline/trial records; benchmark papers use task/protocol/score definitions.\n\n"
        "## Experimental Matrix\n\n"
        f"{render_experiment_matrix(profile_data, scope, eval_type, cues, datasets, metrics, baselines)}\n\n"
        "## Dataset / Benchmark Role\n\n"
        f"{render_dataset_role(datasets)}\n\n"
        "- Dataset names found only by legacy keyword extraction are not accepted as verified evaluation datasets until their role is located in the experiment section.\n\n"
        "## Embodiment / Environment\n\n"
        f"{render_environment(scope, cues, eval_type)}\n\n"
        "## Metrics and Success Definition\n\n"
        f"{render_metrics(metrics)}\n\n"
        "- **Success/failure/timeout definition:** not reported in the current note unless stated above; exact denominator, collision/contact rule and termination condition require body verification.\n\n"
        "## Baselines and Fairness\n\n"
        f"{render_baselines(baselines)}\n\n"
        "## Ablations and Sensitivity\n\n"
        f"{render_ablations(ablations)}\n\n"
        "## Main Results / Claim–Evidence Map\n\n"
        f"{render_results(profile_data, scope, cues, eval_type)}\n\n"
        "## Generalization and Failure Cases\n\n"
        f"{render_failure(profile_data, cues, scope)}\n\n"
        "- **Untested regime audit:** embodiment, sensor noise/calibration, contact mode, long horizon, unseen object/task/scene and recovery behavior are not assumed covered unless the source explicitly reports them.\n\n"
        "## Statistics, Efficiency, and Reproducibility\n\n"
        f"{render_statistics(cues, eval_type)}\n\n"
        "## Limitations and Verification Questions\n\n"
        f"{render_limits(profile_data, datasets, baselines, ablations, cues)}\n\n"
        f"{render_verification(profile_data, eval_type)}\n"
    )


def render_scaffold(item: dict[str, Any], folder: Path, old: str, overview: str, tracker: dict[str, dict[str, str]]) -> str:
    cues = source_cues(old, overview)
    eval_type = infer_type(str(item["title"]), "general", cues)
    scope = scope_for(None, item)
    modules = method_modules(folder, "general")
    datasets = dataset_records(str(item["title"]), None, cues, eval_type)
    metrics = metric_records(str(item["title"]), None, cues, "general")
    baselines = baseline_records(str(item["title"]), cues, eval_type)
    ablations = ablation_records(str(item["title"]), cues, modules, "general", eval_type)
    evidence = evidence_for(item, old, overview, tracker)
    sentence = compact(cues.get("protocol", []), "현재 evaluation claim과 scope는 본문 확인 필요.", 2)
    return (
        f"# Evaluation — {item['title']}\n\n"
        "> Canonical metadata: [01_overview.md](./01_overview.md).\n"
        f"> Evidence maturity: `{evidence}`.\n"
        f"> Analysis basis: {basis_text(None)}\n\n"
        "## Evaluation in One Sentence\n\n"
        f"{sentence}\n\n"
        "## Evaluation Type and Scope\n\n"
        f"- **Evaluation type:** `{eval_type}` (provisional; 본문 확인 필요)\n"
        f"- **Target system/task:** {scope[0]}\n"
        "- Exact evaluation scope, sim/real status와 evaluation unit은 본문 확인 필요.\n\n"
        "## Experimental Matrix\n\n"
        f"{render_experiment_matrix(None, scope, eval_type, cues, datasets, metrics, baselines)}\n\n"
        "## Dataset / Benchmark Role\n\n"
        f"{render_dataset_role(datasets)}\n\n"
        "- Legacy dataset/metric keyword cue는 experiment section에서 role과 definition을 확인하기 전까지 reported fact로 사용하지 않는다.\n\n"
        "## Embodiment / Environment\n\n"
        f"{render_environment(scope, cues, eval_type)}\n\n"
        "## Metrics and Success Definition\n\n"
        f"{render_metrics(metrics)}\n\n"
        "- Success/failure/timeout definition은 본문 확인 필요.\n\n"
        "## Baselines and Fairness\n\n"
        f"{render_baselines(baselines)}\n\n"
        "## Ablations and Sensitivity\n\n"
        f"{render_ablations(ablations)}\n\n"
        "## Main Results / Claim–Evidence Map\n\n"
        f"{render_results(None, scope, cues, eval_type)}\n\n"
        "## Generalization and Failure Cases\n\n"
        f"{render_failure(None, cues, scope)}\n\n"
        "## Statistics, Efficiency, and Reproducibility\n\n"
        f"{render_statistics(cues, eval_type)}\n\n"
        "## Limitations and Verification Questions\n\n"
        "- Current note is a scaffold; exact dataset role, baseline fairness, ablations, trial/seed statistics, failure criteria와 source location은 본문 확인 필요.\n"
        f"{render_verification(None, eval_type)}"
    )


def render_note(item: dict[str, Any], folder: Path, old: str, overview: str, tracker: dict[str, dict[str, str]]) -> tuple[str, bool]:
    profile_data = PROBLEM_PROFILES.get(str(item["title"]))
    if profile_data:
        return render_intensive(item, folder, old, overview, tracker, profile_data), True
    return render_scaffold(item, folder, old, overview, tracker), False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write normalized notes; default is dry-run")
    parser.add_argument("--show", type=int, default=0, help="show the first N generated notes")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    tracker = read_tracker()
    counts: Counter[str] = Counter()
    changed = 0
    missing: list[str] = []
    previews: list[str] = []
    for item in manifest:
        folder = resolve_folder(str(item["folder"]))
        path = folder / "04_evaluation.md"
        overview_path = folder / "01_overview.md"
        old = path.read_text(encoding="utf-8")
        overview = overview_path.read_text(encoding="utf-8")
        if already_normalized(old):
            # The current note contains evidence tables generated from the
            # legacy note.  Re-mining those tables would turn a second run
            # into information loss, so migration is intentionally one-way
            # unless the note still has the legacy metadata/header shape.
            new = preserve_normalized_note(old)
            intensive = str(item["title"]) in PROBLEM_PROFILES
        else:
            new, intensive = render_note(item, folder, old, overview, tracker)
        counts["CORE/NEXT detailed evaluation" if intensive else "registry evaluation scaffold"] += 1
        changed += int(new != old)
        if not (folder / "03_method.md").exists():
            missing.append(str(item["title"]))
        if args.show and len(previews) < args.show:
            previews.append(f"--- {path}\n{new}")
        if args.apply and new != old:
            path.write_text(new, encoding="utf-8")

    print({
        "mode": "apply" if args.apply else "dry-run",
        "registry_papers": len(manifest),
        "notes_to_update": changed,
        "intensive_profiles": len(PROBLEM_PROFILES),
        "missing_method_notes": len(missing),
        "profile_or_scaffold": dict(counts),
    })
    for title in missing:
        print(f"MISSING METHOD: {title}")
    for preview in previews:
        print(preview)


if __name__ == "__main__":
    main()
