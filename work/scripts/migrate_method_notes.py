#!/usr/bin/env python3
"""Normalize ``03_method.md`` and add a formulation-aware method record.

The repository has two useful but different kinds of method notes: a small
number of manually curated notes and a large number of extraction scaffolds.
This migration gives both kinds the same interface while keeping the evidence
boundary visible.  CORE/NEXT papers additionally reuse the reviewed problem
profiles and the method cues already present in the old note.  The migration
does not change reading status or evidence level.

The generated note is deliberately a method record rather than a second
metadata card.  Bibliographic metadata remains in ``01_overview.md``; this
file keeps only the canonical pointer and the evidence/provenance guardrail.
Run without ``--apply`` for a dry run.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

try:
    from migrate_problem_notes import DOMAIN_SCOPE, PROFILES as PROBLEM_PROFILES
except ModuleNotFoundError:  # import as work.scripts.migrate_method_notes
    try:
        from .migrate_problem_notes import DOMAIN_SCOPE, PROFILES as PROBLEM_PROFILES
    except ImportError:
        # Keep direct importlib-based audits usable from the repository root.
        import importlib.util

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
    "## Method in One Sentence",
    "## Design Rationale",
    "## Source Evidence Cues",
    "## Pipeline",
    "## Objective / Update Rule",
    "## Variables and Parameters",
    "## Observation–State–Action Interface",
    "## Temporal and Runtime Contract",
    "## Training vs Inference",
    "## Method-Specific Formal Details",
    "## Evaluation Link",
    "## Failure and Ablation Link",
    "## Reproduction Checklist",
    "## Verification Questions",
)


def parse_sections(markdown: str) -> dict[str, str]:
    """Return level-two sections while ignoring the note title and metadata."""

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


def first_section(sections: dict[str, str], *names: str) -> str:
    for name in names:
        value = sections.get(name, "").strip()
        if value:
            return value
    return ""


def strip_list_marker(value: str) -> str:
    return re.sub(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)", "", value.strip()).strip()


def clean_line(value: str, limit: int = 420) -> str:
    value = strip_list_marker(value)
    value = re.sub(r"\s+", " ", value).strip()
    value = value.replace("paper.pdf", "원문")
    if len(value) > limit:
        value = value[: limit - 1].rstrip() + "…"
    return value


def useful_lines(block: str, limit: int = 6) -> list[str]:
    """Keep content-bearing cues and discard generated placeholders/metadata."""

    result: list[str] = []
    ignored = (
        "자동 추출 실패",
        "자동 추출 없음",
        "본문 확인 필요",
        "본문 수동 확인 필요",
        "full text의 해당 section",
        "unverified",
        "정독 시",
        "source cue와 사전 구조화",
        "metadata registration",
        "survey-keyword",
        "code/project",
        "year/venue",
        "category:",
        "tags:",
        "paper link:",
        "official paper:",
        "source audit:",
    )
    for raw in block.splitlines():
        value = clean_line(raw)
        if not value or value.startswith((">", "|---", "| ---")):
            continue
        low = value.casefold()
        if low.startswith(tuple(x.casefold() for x in ignored)):
            continue
        # PDF-to-text tables and figure labels frequently get concatenated
        # into a sentence.  Keeping those strings would turn a method note
        # into an extraction log, so retain the surrounding prose only when
        # it is not obviously a table artifact.
        if re.search(
            r"task number|number of demonstrations|success rate\s*:|training steps|method input\s*&\s*encoder|"
            r"\b(?:count|episode time|explored areas)\s*:\s*\d|"
            r"(?:^|\s)\d+(?:\.\d+)?\s+\d+(?:\.\d+)?\s+\d+(?:\.\d+)?(?:\s|$)",
            low,
        ):
            continue
        numeric_tokens = re.findall(r"\b\d+(?:\.\d+)?\b", value)
        if re.search(r"\b(?:table|figure|fig\.)\s*\d", low) and len(numeric_tokens) >= 4:
            continue
        if "success rate" in low and len(numeric_tokens) >= 3:
            continue
        if "success rate distribution" in low or "open-loop evaluation" in low:
            continue
        if value.startswith("|") and value.endswith("|"):
            # Tables from a generated legacy note are less useful than the
            # narrative cue and often contain only metadata.
            cells = [cell.strip() for cell in value.strip("|").split("|")]
            value = " — ".join(cell for cell in cells if cell)
        if value and value not in result:
            result.append(value)
        if len(result) >= limit:
            break
    return result


def compact_cue(block: str, fallback: str, limit: int = 2) -> str:
    values = useful_lines(block, limit)
    if not values:
        return fallback
    text = " ".join(values).strip()
    return text if text.endswith((".", "다.", "다?", "다!", "?", "!")) else text + "."


def escape_cell(value: str) -> str:
    return re.sub(r"\s+", " ", str(value).replace("|", "\\|").replace("\n", " ")).strip()


def read_tracker() -> dict[str, dict[str, str]]:
    if not STATUS.exists():
        return {}
    tracker: dict[str, dict[str, str]] = {}
    with STATUS.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            overview = row.get("overview_path", "").removeprefix("./")
            if not overview:
                continue
            folder = overview.removesuffix("/01_overview.md")
            tracker[folder] = row
            tracker[folder.casefold()] = row
    return tracker


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
        return (
            "registry/abstract 또는 기존 note cue 기반 method scaffold; exact method detail은 본문 수동 확인 필요. "
            "tracker의 reading status/evidence는 변경하지 않았다."
        )
    basis = profile_data.get("body_basis", "BODY_FORMULATION_REVIEWED")
    messages = {
        "FULL_TEXT_FORMULATION_REVIEWED": (
            "source PDF 또는 공식 full-text source의 method/formulation 관련 본문 cue를 검토해 pipeline과 interface를 구조화했다."
        ),
        "BODY_FORMULATION_REVIEWED": (
            "source PDF 또는 공식 full-text source의 method/formulation 관련 본문 cue를 검토해 pipeline과 interface를 구조화했다."
        ),
        "BODY_FORMULATION_REVIEWED_CORRECTED_SOURCE": (
            "원래 source가 논문과 불일치해 검증된 저자/공식 source의 본문 cue를 다시 확인한 뒤 pipeline과 interface를 구조화했다."
        ),
        "ABSTRACT_AND_PROCEEDINGS_FORMULATION": (
            "공식 abstract/proceedings와 available method cue를 바탕으로 구조화했다; exact module equation/page는 본문 확인 필요."
        ),
        "ABSTRACT_AND_CLASSIC_FORMULATION": (
            "공식 abstract와 canonical method formulation을 바탕으로 구조화했다; source-specific equation/page는 본문 확인 필요."
        ),
        "ABSTRACT_OR_PROJECT_PAGE_FORMULATION": (
            "공식 abstract/project page 수준의 method cue를 바탕으로 구조화했다; detailed implementation은 본문 확인 필요."
        ),
        "ABSTRACT_OR_PROGRAM_PAGE_FORMULATION": (
            "공식 abstract/program page 수준의 method cue를 바탕으로 구조화했다; detailed implementation은 본문 확인 필요."
        ),
        "ABSTRACT_AND_REVIEW_FORMULATION": (
            "공식 abstract와 review-level method cue를 바탕으로 구조화했다; detailed implementation은 본문 확인 필요."
        ),
    }
    return messages.get(basis, messages["BODY_FORMULATION_REVIEWED"]) + " tracker의 reading status/evidence는 이 migration에서 변경하지 않았다."


def source_cues(old: str, overview: str) -> dict[str, list[str]]:
    old_sections = parse_sections(old)
    overview_sections = parse_sections(overview)

    # Preserve the source cues after the first migration so rerunning the
    # script is stable and does not erase the useful legacy extraction.
    preserved = useful_lines(old_sections.get("Source Evidence Cues", ""), 8)
    if preserved:
        normalized = [
            re.sub(
                r"^(?:brief/method cue|rationale cue|core/pipeline cue|interface cue)\s*:\s*",
                "",
                value,
                flags=re.IGNORECASE,
            ).strip()
            for value in preserved
            if not value.casefold().startswith("**source anchor:")
        ]
        normalized = list(dict.fromkeys(value for value in normalized if value))
        return {"all": normalized, "core": normalized, "rationale": normalized[:3]}

    groups = {
        "brief": ("Brief Method", "Abstract Method Cue", "Method in One Sentence"),
        "rationale": ("원리적 동기", "Design Rationale", "왜 문제인가"),
        "core": ("핵심 방법론", "Pipeline", "Method-Specific Formal Details"),
        "interface": ("Interface", "Observation–State–Action Interface"),
    }
    collected: dict[str, list[str]] = {}
    for key, names in groups.items():
        values: list[str] = []
        for name in names:
            values.extend(useful_lines(old_sections.get(name, ""), 6))
        collected[key] = list(dict.fromkeys(values))[:8]

    if not collected["brief"]:
        collected["brief"] = useful_lines(first_section(overview_sections, "Core Idea", "Problem"), 4)
    if not collected["rationale"]:
        collected["rationale"] = useful_lines(first_section(overview_sections, "Problem", "Limitation"), 3)
    if not collected["core"]:
        collected["core"] = collected["brief"][:]
    if not collected["interface"]:
        collected["interface"] = useful_lines(first_section(overview_sections, "Interface", "Input / Output"), 3)
    collected["all"] = list(
        dict.fromkeys(
            [f"Brief/method cue: {line}" for line in collected["brief"]]
            + [f"Rationale cue: {line}" for line in collected["rationale"]]
            + [f"Core/pipeline cue: {line}" for line in collected["core"]]
            + [f"Interface cue: {line}" for line in collected["interface"]]
        )
    )[:8]
    return collected


def cue_for(cues: dict[str, list[str]], index: int, fallback: str) -> str:
    values = cues.get("core", []) + cues.get("brief", []) + cues.get("interface", [])
    if values and index < len(values):
        return values[index]
    if values:
        return values[index % len(values)]
    return fallback


def source_evidence(cues: dict[str, list[str]], anchor: str, *, limit: int = 6) -> str:
    lines = cues.get("all", [])[:limit]
    if not lines:
        lines = [f"Method/formulation anchor: {anchor}"]
    rendered = [f"- {line}" for line in lines]
    rendered.append(f"- **Source anchor:** {anchor}")
    return "\n".join(rendered)


def source_location(profile_data: dict[str, Any] | None, *, detail: str = "method/formulation cue") -> str:
    if not profile_data:
        return "현재 note cue; exact source section/page 확인 필요"
    anchor = profile_data.get("anchor", "paper-specific method section")
    basis = profile_data.get("body_basis", "")
    if basis.startswith("ABSTRACT"):
        return f"{detail}: {anchor}; exact equation/section/page 확인 필요"
    return f"{detail}: {anchor}; equation 번호/page는 원문과 대조 필요"


# These are deliberately conservative canonical equations.  They are only
# emitted for well-known formulations whose variables are also listed below;
# the source column still tells the reader to verify numbering/page.
SPECIAL_FORMAL: dict[str, str] = {
    "A New Approach to Linear Filtering and Prediction Problems":
        "State/observation cue: xₖ=Fₖxₖ₋₁+wₖ, yₖ=Hₖxₖ+vₖ; prediction propagates mean/covariance and the innovation update applies a gain Kₖ.",
    "A Formal Basis for the Heuristic Determination of Minimum Cost Paths":
        "Best-first priority f(n)=g(n)+h(n), where g is cost-so-far and h is a lower-bound estimate of remaining cost; admissibility is the optimality condition.",
    "Planning and Acting in Partially Observable Stochastic Domains":
        "Belief update b′(s′)∝O(o|s′)ΣₛT(s′|s,a)b(s), followed by a policy/value backup in belief space.",
    "A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation":
        "Operational inertia Λ=(J A⁻¹Jᵀ)⁻¹ and wrench/torque mapping τ=JᵀF expose task-space dynamics; dynamically consistent null-space terms handle redundancy.",
    "Hybrid Position/Force Control of Manipulators":
        "A selection matrix S separates force-controlled and position-controlled task directions; the complementary subspaces are combined at the Cartesian command/interface.",
    "Impedance Control: An Approach to Manipulation: Part I—Theory":
        "Desired interaction is expressed as M_d ẍ+D_d ẋ+K_d(x−x_d)=F_ext, specifying a motion–force relationship rather than hard position or force tracking.",
    "Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces":
        "Samples q∈C_free become vertices V and collision-free local connections become edges E; query planning searches the resulting roadmap G=(V,E).",
    "Rapidly-Exploring Random Trees: A New Tool for Path Planning":
        "A random q_rand selects q_near and a steer operation produces q_new; a collision-free edge is appended to the tree until the goal region is reached.",
    "CHOMP: Gradient Optimization Techniques for Efficient Motion Planning":
        "Trajectory ξ is optimized by a smoothness/obstacle cost gradient, with a covariant preconditioner turning functional cost variation into a trajectory update.",
    "TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning":
        "A nonlinear trajectory problem is repeatedly approximated by a local convex subproblem and solved under signed-distance/collision and kinematic constraints.",
    "Control-Limited Differential Dynamic Programming":
        "Local dynamic-programming expansions use derivatives of the dynamics/cost while explicitly enforcing bounded control through a constrained backward/forward pass.",
    "Policy Gradient Methods for Reinforcement Learning with Function Approximation":
        "The policy-gradient estimator has the form ∇θJ(θ)=E[∇θ log πθ(a|s) Qπ(s,a)], with a baseline/advantage reducing variance when valid.",
    "Trust Region Policy Optimization":
        "A surrogate policy objective is optimized subject to a KL-divergence trust-region constraint so the updated policy stays close to the behavior policy.",
    "Proximal Policy Optimization Algorithms":
        "The clipped surrogate min(r_t(θ)Â_t, clip(r_t(θ),1−ε,1+ε)Â_t) limits destructive policy-ratio updates.",
    "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor":
        "The objective maximizes expected return plus entropy, J(π)=E[Σ(r_t+αH(π(·|s_t)))], using off-policy actor/critic updates.",
    "Hindsight Experience Replay":
        "Failed transitions are relabeled with an achieved goal g′, changing the goal-conditioned reward while reusing the same trajectory for off-policy learning.",
    "Conservative Q-Learning for Offline Reinforcement Learning":
        "The offline value objective adds a conservative penalty that lowers Q on out-of-distribution actions relative to dataset actions before policy improvement.",
    "Offline Reinforcement Learning with Implicit Q-Learning":
        "Expectile regression estimates a value below/near high-return dataset actions, and an advantage-weighted behavior update avoids querying a learned policy on unsupported actions.",
    "Decision Transformer: Reinforcement Learning via Sequence Modeling":
        "A causal sequence model predicts a_t from return-to-go, state and previous actions, treating offline control as conditional trajectory modeling.",
    "Denoising Diffusion Probabilistic Models":
        "A forward noising chain q(x_t|x_{t−1}) is learned in reverse with a denoiser ε_θ(x_t,t); generation iteratively removes noise.",
    "Flow Matching for Generative Modeling":
        "A vector field v_θ(x_t,t) is trained to match a prescribed probability path, then integrated as an ODE from a simple base distribution to data.",
    "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion":
        "The policy denoises an action horizon conditioned on observation o_t and executes a receding action chunk, turning multimodal behavior cloning into conditional diffusion sampling.",
    "Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions":
        "Action dimensions/tokens are modeled autoregressively with Q-values so a high-dimensional action can be selected by sequential maximization under an offline dataset.",
    "Control Barrier Function Based Quadratic Programs for Safety Critical Systems":
        "A QP selects the closest safe control to a nominal command while enforcing a barrier condition such as ḣ(x,u)+α(h(x))≥0.",
    "RMA: Rapid Motor Adaptation for Legged Robots":
        "A history encoder infers a latent environment/terrain parameter z from proprioceptive history, and a policy conditioned on z adapts the base locomotion controller online.",
    "PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation":
        "Point-wise features are aggregated with a symmetric function such as max pooling, making the global representation invariant to point ordering.",
    "3D Gaussian Splatting for Real-Time Radiance Field Rendering":
        "The scene is represented by anisotropic Gaussians with position, covariance, opacity and color; differentiable splatting renders views while optimizing these parameters.",
    "PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning":
        "A symbolic optimistic plan is refined by black-box stream sampling; failed or successful samples update the certified facts used by the next planning attempt.",
}


VARIABLE_PRESETS: dict[str, list[tuple[str, str, str, str]]] = {
    "A New Approach to Linear Filtering and Prediction Problems": [
        ("xₖ", "state vector", "latent state at k", "state model"),
        ("yₖ", "measurement vector", "observation at k", "observation model"),
        ("Fₖ, Hₖ", "matrices", "transition and observation operators", "prediction/update"),
        ("Qₖ, Rₖ", "covariance matrices", "process and measurement noise", "uncertainty propagation"),
        ("Pₖ, Kₖ", "covariance / gain", "posterior error covariance and innovation gain", "measurement update"),
    ],
    "A Formal Basis for the Heuristic Determination of Minimum Cost Paths": [
        ("n", "graph node", "candidate state", "search frontier"),
        ("g(n)", "scalar cost", "cost from start to n", "path ranking"),
        ("h(n)", "scalar lower bound", "estimated remaining cost", "heuristic ranking"),
        ("f(n)", "scalar cost", "g(n)+h(n)", "node expansion priority"),
        ("OPEN/CLOSED", "sets", "frontier and expanded nodes", "duplicate handling"),
    ],
    "Planning and Acting in Partially Observable Stochastic Domains": [
        ("S, A, Ω", "sets", "states, actions and observations", "POMDP interface"),
        ("T(s′|s,a)", "transition probability", "state dynamics", "belief prediction"),
        ("O(o|s′)", "observation probability", "sensor model", "belief correction"),
        ("bₜ(s)", "probability distribution", "belief over hidden state", "policy/value input"),
        ("R(s,a), γ", "reward / discount", "decision objective", "backup/optimization"),
    ],
    "A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation": [
        ("q, q̇", "joint position/velocity", "robot configuration state", "dynamics"),
        ("x, J(q)", "task pose / Jacobian", "operational coordinate and differential map", "task interface"),
        ("A(q), Λ", "inertia matrices", "joint and operational inertia", "task-space dynamics"),
        ("F, τ", "wrench / torque", "task command and joint actuation", "controller output"),
        ("N", "null-space projector", "redundancy direction", "secondary objective"),
    ],
    "Hybrid Position/Force Control of Manipulators": [
        ("x, x_d", "Cartesian pose", "measured and desired position", "position loop"),
        ("F, F_d", "wrench", "measured and desired contact force", "force loop"),
        ("S", "selection matrix", "force-controlled directions", "hybrid command"),
        ("C", "task/contact frame", "coordinate frame for natural constraints", "error decomposition"),
        ("τ", "joint torque", "combined position/force command", "actuation"),
    ],
    "Impedance Control: An Approach to Manipulation: Part I—Theory": [
        ("x, x_d", "pose / desired pose", "motion state and reference", "impedance error"),
        ("F_ext", "external wrench", "environment interaction", "dynamic response"),
        ("M_d,D_d,K_d", "desired matrices", "inertia, damping, stiffness", "impedance law"),
        ("τ", "joint torque", "actuator command realizing impedance", "execution"),
    ],
}


DOMAIN_VARIABLES: dict[str, list[tuple[str, str, str, str]]] = {
    "planning": [
        ("s / q", "state or configuration", "planning state", "search/optimization"),
        ("a / ξ", "action or trajectory", "candidate decision", "planner output"),
        ("J or c", "scalar cost", "path/task objective", "ranking/optimization"),
        ("C_free / G", "feasible set or graph", "collision/constraint representation", "feasibility"),
    ],
    "estimation": [
        ("xₜ", "latent state", "estimated robot/world state", "filter input/output"),
        ("yₜ", "observation", "sensor measurement", "measurement update"),
        ("Pₜ / Σₜ", "covariance", "state uncertainty", "confidence interface"),
        ("F/H or f/h", "model operators", "transition/observation mapping", "prediction/update"),
    ],
    "control": [
        ("q, q̇", "joint state", "configuration and velocity", "dynamics/control"),
        ("x, x_d", "task state/reference", "task-space error", "task command"),
        ("u / τ", "control input", "actuator command", "closed-loop execution"),
        ("J / A / constraints", "model terms", "kinematics/dynamics/feasibility", "control solve"),
    ],
    "simulation": [
        ("sₜ", "simulator state", "physical state", "rollout"),
        ("aₜ", "control input", "policy/controller command", "dynamics step"),
        ("f_θ", "dynamics model", "transition or differentiable simulator", "prediction"),
        ("rₜ", "cost/reward", "learning or planning signal", "optimization"),
    ],
    "world_model": [
        ("oₜ", "observation", "image/proprioception/tactile input", "encoding"),
        ("zₜ", "latent state", "compact world representation", "dynamics/policy input"),
        ("aₜ", "action", "condition for future prediction", "latent rollout"),
        ("p_θ(zₜ₊₁|zₜ,aₜ)", "transition distribution", "learned dynamics", "planning/evaluation"),
    ],
    "safety": [
        ("sₜ / τₜ", "state/trajectory", "runtime safety context", "risk estimation"),
        ("h(s)", "barrier/risk score", "safe-set or failure margin", "constraint"),
        ("u_nom", "nominal command", "task policy output", "safe filter input"),
        ("u_safe", "filtered/recovery command", "command satisfying safety condition", "execution"),
    ],
    "vla": [
        ("oₜ", "image/proprioception/point cloud", "robot observation", "multimodal encoder"),
        ("l / g", "language/goal", "task conditioning", "policy context"),
        ("zₜ", "fused latent", "action-relevant scene/task state", "action decoder input"),
        ("aₜ:ₜ₊H", "action chunk", "predicted control horizon", "receding execution"),
    ],
    "manipulation": [
        ("P / G", "point cloud/geometry", "object and scene representation", "grasp/contact proposal"),
        ("T ∈ SE(3)", "pose transform", "grasp or end-effector pose", "motion planning"),
        ("c / ξ", "contact mode/trajectory", "interaction decision", "execution"),
        ("f / τ", "wrench/torque", "contact feedback/actuation", "closed loop"),
    ],
    "tactile": [
        ("I_v / I_t", "vision/tactile observation", "multi-modal contact input", "encoding"),
        ("cₜ", "contact state", "contact mode or surface cue", "state estimation"),
        ("fₜ", "force/wrench", "interaction measurement", "feedback"),
        ("aₜ / τₜ", "action/torque", "contact-aware command", "execution"),
    ],
    "3d_perception": [
        ("I / P", "image/point cloud", "raw visual geometry", "feature extraction"),
        ("T / G", "pose/map/scene graph", "world-coordinate structure", "fusion/query"),
        ("z", "semantic feature", "open-vocabulary or task representation", "grounding"),
        ("r / a", "robot query/action", "downstream target or motion cue", "robot interface"),
    ],
    "navigation": [
        ("I / P", "visual/depth input", "scene geometry", "mapping"),
        ("M / G", "map/graph", "free space and semantic structure", "planning"),
        ("ξ", "path/waypoint sequence", "navigation decision", "controller input"),
        ("u", "velocity/control", "executed motion", "feedback"),
    ],
    "locomotion": [
        ("sₜ", "proprioception/terrain observation", "locomotion state", "policy input"),
        ("cₜ / zₜ", "command/latent adaptation", "task or terrain context", "conditioning"),
        ("aₜ / τₜ", "joint action/torque", "whole-body command", "execution"),
        ("qₜ, contactₜ", "pose/contact state", "feedback and stability", "adaptation"),
    ],
    "humanoid": [
        ("oₜ / p_ref", "observation/reference pose", "whole-body task input", "retargeting/policy"),
        ("zₜ", "latent skill/context", "motion or embodiment context", "controller conditioning"),
        ("aₜ / τₜ", "joint target/torque", "whole-body command", "execution"),
        ("contact / qₜ", "contact and body state", "balance/feedback signal", "recovery"),
    ],
    "rl": [
        ("sₜ", "state/observation", "policy input", "action selection"),
        ("aₜ", "action", "control decision", "environment step"),
        ("rₜ", "reward", "learning signal", "return/critic"),
        ("π_θ / Q_φ / V_ψ", "policy/value functions", "parametric estimator", "update"),
    ],
    "offline_rl": [
        ("D={(s,a,r,s′)}", "offline dataset", "fixed transition support", "value/policy learning"),
        ("Q_φ / V_ψ", "value function", "return estimate", "conservative/implicit update"),
        ("π_θ", "policy", "action distribution", "policy extraction"),
        ("μ_D", "behavior support", "dataset action distribution", "OOD constraint"),
    ],
    "il": [
        ("D={(oₜ,aₜ)}", "demonstrations", "expert observation-action pairs", "supervised learning"),
        ("π_θ", "policy", "action predictor", "behavior cloning"),
        ("hₜ", "history/latent", "temporal context", "prediction"),
        ("aₜ:ₜ₊H", "action sequence", "chunk or trajectory output", "execution"),
    ],
    "generative": [
        ("x₀", "data/action sample", "target distribution sample", "forward/noising path"),
        ("xₜ", "noisy/interpolated state", "generation-time state", "denoiser/flow input"),
        ("ε_θ / v_θ", "score/velocity field", "learned generative direction", "sampling"),
        ("t", "noise/time variable", "schedule or ODE time", "conditioning"),
    ],
    "robot_data": [
        ("D", "demonstration corpus", "robot/task/embodiment trajectories", "data pipeline"),
        ("oₜ / aₜ", "observation/action", "training sample", "policy learning"),
        ("e / m", "embodiment/task metadata", "conditioning/context", "cross-domain transfer"),
        ("π_θ", "learned policy", "downstream action interface", "deployment"),
    ],
    "benchmark": [
        ("E", "task/environment suite", "evaluation domains", "benchmark harness"),
        ("o / a", "observation/action schema", "standardized interface", "method execution"),
        ("m", "metric", "success/quality measure", "comparison"),
        ("b", "baseline", "reference method", "attribution of gain"),
    ],
    "vision": [
        ("I", "image", "visual input", "encoder"),
        ("z", "feature representation", "pretrained visual state", "downstream task"),
        ("y", "label/query", "supervision or task prompt", "training/inference"),
        ("θ", "network parameters", "learned representation", "optimization"),
    ],
    "sim2real": [
        ("s_sim / s_real", "sim/real state", "domain-specific observation", "policy input"),
        ("δ", "domain parameter", "randomized dynamics/appearance", "training variation"),
        ("π_θ", "policy", "control mapping", "deployment"),
        ("e", "transfer error", "sim-to-real mismatch", "robustness evaluation"),
    ],
    "general": [
        ("oₜ", "observation", "paper input", "representation"),
        ("zₜ", "state/latent", "decision context", "method core"),
        ("aₜ / yₜ", "action/prediction", "paper output", "execution/evaluation"),
        ("θ", "parameters", "learned/optimized quantities", "update"),
    ],
}


def variables_for(title: str, domain: str, profile_data: dict[str, Any] | None) -> list[tuple[str, str, str, str]]:
    values = VARIABLE_PRESETS.get(title) or DOMAIN_VARIABLES.get(domain, DOMAIN_VARIABLES["general"])
    return values


def domain_modules(profile_data: dict[str, Any], cues: dict[str, list[str]]) -> list[dict[str, str]]:
    domain = profile_data.get("domain", "general")
    model = profile_data.get("model", "paper-specific state/representation")
    objective = profile_data.get("objective", "paper-specific objective")

    templates: dict[str, list[tuple[str, str, str, str, str, str]]] = {
        "estimation": [
            ("State-space representation", "state와 observation model을 명시", model, "transition/observation operators와 noise statistics를 사용해 sufficient statistic을 정의", "state mean와 uncertainty representation", "다음 prediction/control이 uncertainty를 소비할 수 있음"),
            ("Recursive prediction", "이전 posterior를 다음 시점 prior로 전파", "posterior estimate와 covariance", "dynamics를 적용해 mean/covariance를 propagate", "prior state와 prior uncertainty", "online update가 전체 history 재계산을 피함"),
            ("Innovation update", "새 measurement로 prior를 보정", "prior와 measurement", "innovation/gain을 계산해 posterior를 갱신", "filtered state와 covariance", "센서 feedback이 closed loop에 들어감"),
        ],
        "planning": [
            ("State / search-space representation", "결정 가능한 state와 feasibility를 표현", model, "graph, tree, belief 또는 symbolic state를 구성", "search state와 admissible decision set", "후속 search가 task/motion constraints를 볼 수 있음"),
            ("Search / trajectory optimization", "goal을 향해 candidate를 개선", "search state와 objective", "확장, heuristic, sampling 또는 local optimization으로 candidate를 생성", "plan/trajectory candidate", "cost와 feasibility를 동시에 비교"),
            ("Feasibility and execution interface", "계획을 실행 가능한 출력으로 변환", "candidate와 constraints", "collision/contact/dynamics check, smoothing 또는 refinement", "waypoint, action 또는 controller reference", "planner-controller 경계를 명시"),
        ],
        "control": [
            ("Task and error representation", "motion/force/contact 목표를 제어 가능한 error로 변환", model, "task frame, Jacobian, impedance 또는 selection으로 error를 분해", "desired task acceleration/wrench", "contact-relevant objective가 joint command에 노출"),
            ("Dynamics and constraint solve", "desired behavior를 feasible command로 변환", "task error와 robot model/constraints", "inverse dynamics, QP, MPC 또는 operational mapping을 계산", "feasible torque/command", "actuator/contact/whole-body constraints를 반영"),
            ("Feedback and actuation", "실제 state/wrench로 command를 수정", "sensor feedback와 nominal command", "closed-loop correction, saturation 또는 null-space action", "joint actuation와 next-state response", "model error와 disturbance에 대응"),
        ],
        "simulation": [
            ("Physics state and interface", "robot/environment state를 simulator 변수로 표현", model, "rigid-body/contact/dynamics state를 step interface로 구성", "simulator state", "rollout과 controller가 같은 state contract를 사용"),
            ("Parallel or differentiable rollout", "candidate action의 consequence를 계산", "state와 action", "physics transition 또는 differentiable rollout을 반복", "predicted trajectory/reward", "model-based optimization/data generation을 가능하게 함"),
            ("Controller / learning interface", "simulation result를 policy update나 real transfer에 사용", "rollout과 task objective", "gradient, dataset 또는 randomized experience를 policy에 전달", "updated policy/controller", "simulation과 deployment의 mismatch를 측정"),
        ],
        "world_model": [
            ("Observation encoder", "raw observation을 compact state로 변환", model, "visual/proprioceptive/tactile encoder 또는 latent inference", "latent state zₜ", "long history를 manageable state로 압축"),
            ("Latent dynamics rollout", "action-conditioned future를 예측", "zₜ와 action", "learned transition/video/action diffusion을 roll out", "future latent/observation/reward", "planning과 counterfactual evaluation을 지원"),
            ("Policy/planner interface", "예측을 decision으로 연결", "predicted future와 objective", "candidate action 평가 또는 policy optimization", "action/option sequence", "world model error가 closed-loop failure로 드러남"),
        ],
        "safety": [
            ("Risk / failure representation", "runtime state의 위험 신호를 계산", model, "uncertainty, barrier, failure classifier 또는 recovery zone을 추정", "risk/failure score", "policy output을 안전 판단과 연결"),
            ("Safe filtering or recovery", "nominal action을 constraint 안으로 변환", "nominal action과 risk/constraint", "QP filter, backup policy 또는 correction plan을 선택", "safe/recovery command", "failure 전에 intervention"),
            ("Closed-loop monitoring", "실행 결과를 다시 risk model에 반영", "executed command와 next observation", "threshold/update/replan을 수행", "continue, correct 또는 abort decision", "false positive/negative trade-off를 평가"),
        ],
        "vla": [
            ("Multimodal observation encoding", "vision, language, proprioception 또는 3D 입력을 결합", model, "pretrained encoder/adapter/attention으로 task-conditioned representation을 구성", "fused policy context", "web/semantic prior와 robot state를 같은 interface로 연결"),
            ("Action policy / decoder", "context에서 action 또는 skill을 생성", "fused context와 history", "autoregressive, diffusion, flow 또는 skill-conditioned decoder를 적용", "action/skill chunk", "continuous control output의 표현력을 결정"),
            ("Receding execution and feedback", "예측을 부분 실행하고 다시 관측", "action chunk와 current observation", "chunk 일부를 실행한 뒤 replan/terminate/recover", "next action and feedback state", "long-horizon/contact robustness를 좌우"),
        ],
        "manipulation": [
            ("Geometry / contact representation", "object와 contact-relevant geometry를 표현", model, "point cloud, affordance, grasp/contact graph 또는 SE(3) descriptor를 추출", "candidate contact/pose state", "visual geometry가 action space를 제한"),
            ("Pose / trajectory generation", "candidate를 feasible manipulation motion으로 변환", "geometry/contact state와 goal", "grasp sampling, trajectory optimization 또는 generative action model을 적용", "pose/trajectory/action candidate", "kinematic/contact feasibility를 평가"),
            ("Execution and correction", "contact outcome에 따라 manipulation을 닫힌 loop로 실행", "candidate와 force/tactile/visual feedback", "tracking, regrasp, correction 또는 recovery", "next action/task state", "open-loop plan의 contact failure를 드러냄"),
        ],
        "tactile": [
            ("Multi-modal contact encoding", "vision과 touch를 contact-relevant feature로 변환", model, "tactile image/force와 visual state를 encode/fuse", "contact feature/state", "hidden contact geometry를 보완"),
            ("Contact inference / dynamics", "contact mode와 object response를 추정", "contact feature와 action history", "mode classifier, tactile dynamics 또는 force-aware model을 update", "contact state/force prediction", "다음 action의 uncertainty를 줄임"),
            ("Force-aware action correction", "interaction feedback으로 command를 조절", "predicted contact와 current wrench/touch", "policy/control law가 action/force를 재계산", "contact-safe action/torque", "contact-rich task의 failure recovery를 지원"),
        ],
        "3d_perception": [
            ("Geometry extraction", "image/point input에서 3D structure를 복원", model, "depth, pose, point, Gaussian 또는 correspondence representation을 추정", "geometric state/map", "occlusion과 metric spatial relation을 노출"),
            ("Semantic / temporal fusion", "geometry에 language/semantic/state를 정렬", "geometric state와 text/visual feature/history", "feature lifting, scene graph, map update 또는 temporal fusion", "queryable semantic 3D state", "robot task와 open vocabulary를 연결"),
            ("Robot query interface", "3D state를 planner/policy가 소비", "map/feature와 task query", "grounding, target selection, collision/free-space 또는 action cue 생성", "goal/pose/path/action input", "downstream behavior를 통해 perception value를 검증"),
        ],
        "navigation": [
            ("Scene map construction", "sensor stream을 geometric/semantic map으로 변환", model, "mapping, localization 또는 Gaussian/scene-graph update", "world-coordinate map", "navigation decision의 spatial memory를 제공"),
            ("Safe path decision", "goal과 uncertainty를 고려한 route를 생성", "map, goal, risk/collision model", "graph search, local planning 또는 safety corridor optimization", "path/waypoints", "geometry와 safety assumption을 함께 테스트"),
            ("Motion execution", "path를 velocity/actuation으로 추종", "path와 current pose", "tracking/replanning을 수행", "control command", "drift·latency·dynamic obstacle feedback을 반영"),
        ],
        "locomotion": [
            ("Command / terrain representation", "body state와 terrain/task context를 표현", model, "proprioception/history/reference를 encode", "locomotion context", "보행 mode와 terrain adaptation을 조건화"),
            ("Whole-body policy/controller", "context에서 joint target/torque를 생성", "context와 contact/body state", "RL policy, reference tracking 또는 whole-body control을 적용", "joint action/torque", "balance/contact constraints와 skill motion을 결합"),
            ("Adaptation and feedback", "실제 contact/disturbance에 대응", "new observation/history", "latent adaptation, recovery 또는 replan을 수행", "updated command", "sim-to-real robustness와 failure recovery를 검증"),
        ],
        "humanoid": [
            ("Reference / embodiment interface", "human/task reference를 robot-compatible state로 변환", model, "retargeting, pose/skill conditioning 또는 multimodal encoding", "whole-body reference/context", "high-DOF intent를 action interface로 축소"),
            ("Whole-body execution", "reference를 balance-aware command로 변환", "context, body state, contacts", "policy, WBC, inverse dynamics 또는 hierarchical controller를 적용", "joint target/torque", "contact and actuator constraints를 반영"),
            ("Recovery / adaptation", "fall, mismatch 또는 disturbance 뒤 behavior를 복구", "feedback/history and failure signal", "adaptation, motion completion 또는 reinitialization", "recovery command", "long-horizon deployment boundary를 노출"),
        ],
        "rl": [
            ("Policy/value representation", "state에서 action과 return estimate를 표현", model, "actor/critic 또는 policy/value networks를 evaluate", "πθ action and Q/V estimate", "learning signal을 action choice에 연결"),
            ("Rollout and return construction", "environment interaction으로 update target 생성", "state, action, reward, next state", "trajectory/advantage/TD target을 계산", "training target", "credit assignment와 data efficiency를 결정"),
            ("Policy/value update", "objective를 최적화하고 다음 policy 생성", "target and parameters", "gradient, trust-region, entropy 또는 replay update", "updated policy/controller", "stability·exploration·constraint trade-off를 결정"),
        ],
        "offline_rl": [
            ("Fixed dataset support", "온라인 exploration 없이 transition 분포를 정의", model, "demonstration/replay dataset과 behavior support를 organize", "offline training batches", "data coverage와 OOD boundary를 명시"),
            ("Conservative / implicit value learning", "dataset 밖 action의 과대추정을 억제", "batch transitions and value parameters", "conservative penalty, expectile 또는 uncertainty-aware value update", "Q/V estimate", "offline extrapolation error를 통제"),
            ("Policy extraction", "learned value를 실행 policy로 변환", "Q/V and behavior support", "argmax, advantage weighting 또는 sequence decoding", "action policy", "deployment action이 dataset support 안에 있는지 확인"),
        ],
        "il": [
            ("Demonstration representation", "expert trajectory를 policy input/target으로 구성", model, "observation, history, goal과 action sequence를 align", "training pairs/latent context", "demonstration coverage를 측정 가능하게 함"),
            ("Policy fitting", "expert action distribution을 학습", "training pairs/context", "behavior cloning, sequence model, diffusion 또는 adversarial objective를 optimize", "policy/action distribution", "multimodality와 compounding error를 결정"),
            ("Closed-loop rollout", "학습 policy의 distribution shift를 확인", "current observation/history", "action/chunk을 실행하고 feedback으로 계속 예측", "trajectory and failure signal", "offline imitation claim을 실제 control로 연결"),
        ],
        "generative": [
            ("Forward/noise or probability path", "data를 simple/noisy state로 연결", model, "noise schedule, interpolation 또는 path를 정의", "x_t/path state", "학습 가능한 reverse target을 제공"),
            ("Denoiser / vector-field learning", "생성 방향을 학습", "x_t and time t", "score, noise, velocity 또는 flow matching objective를 optimize", "ε/v/score estimate", "distributional expressivity와 training stability를 결정"),
            ("Sampling / action interface", "learned field를 sample 또는 action으로 변환", "base noise and condition", "iterative denoising/ODE integration을 수행", "sample/action trajectory", "inference steps와 control latency를 결정"),
        ],
        "robot_data": [
            ("Data collection / normalization", "heterogeneous robot data를 공통 sample로 정리", model, "trajectory, task, embodiment, sensor/action schema를 align", "normalized dataset", "cross-robot supervision을 가능하게 함"),
            ("Coverage / augmentation", "data support와 variation을 확장", "dataset and metadata", "retargeting, relabeling, synthetic/teleop augmentation 또는 filtering", "expanded training distribution", "generalization claim의 실제 범위를 결정"),
            ("Policy training interface", "data를 downstream model이 소비", "normalized observations/actions", "BC, pretraining 또는 action-token learning을 수행", "policy/checkpoint", "data scale와 action schema가 method effect와 분리됨"),
        ],
        "benchmark": [
            ("Task and interface definition", "method 비교를 위한 task/state/action contract를 고정", model, "environment, embodiment, task variation과 split을 정의", "benchmark episodes", "비교 가능성을 확보"),
            ("Baseline harness", "동일 protocol로 baseline과 제안법 실행", "episodes and method interfaces", "baseline/ablation/seed를 통제해 rollout", "comparable trajectories", "gain을 method module에 귀속"),
            ("Metric and failure reporting", "success뿐 아니라 failure/latency/generalization을 측정", "trajectories and logs", "metric aggregation과 failure taxonomy를 적용", "comparison table and failure cases", "benchmark overfitting을 드러냄"),
        ],
        "vision": [
            ("Visual representation", "raw image를 task-relevant feature로 변환", model, "backbone/attention/equivariant encoder를 apply", "feature z", "downstream robot state의 visual part를 제공"),
            ("Pretraining / objective", "representation을 학습 또는 align", "images and labels/text", "supervised, contrastive, self-supervised 또는 generative update", "trained parameters", "data prior와 invariance를 결정"),
            ("Downstream interface", "feature를 robot task에 연결", "z and task query", "projection/fusion/policy head를 use", "prediction/pose/action cue", "robot behavior metric으로 utility를 검증"),
        ],
        "sim2real": [
            ("Domain parameterization", "sim/real mismatch를 명시", model, "dynamics, visual, sensor, latency variation을 parameterize/randomize", "training domains", "robustness target을 구체화"),
            ("Policy/controller learning", "variation을 견디는 mapping을 학습", "randomized state/trajectory", "RL/IL/control objective로 policy를 train", "policy/controller", "simulator bias에 대한 sensitivity를 측정"),
            ("Real deployment and adaptation", "real feedback으로 transfer를 확인", "real observation and action", "calibration, adaptation 또는 fallback을 apply", "real command/performance", "transfer failure boundary를 드러냄"),
        ],
        "general": [
            ("Input representation", "paper input을 decision-ready representation으로 변환", model, "paper-specific encoder/transform/feature extraction", "state/feature", "후속 모듈의 interface를 고정"),
            ("Core method", "주어진 representation에서 목표를 최적화", "state/feature and objective", "paper-specific algorithm/model/control law", "prediction/plan/action", "paper contribution이 위치하는 모듈"),
            ("Output / feedback", "결과를 environment 또는 downstream task에 연결", "output and observation feedback", "execution/evaluation/replanning", "next output or metric", "closed-loop relevance를 확인"),
        ],
    }
    rows = templates.get(domain, templates["general"])
    rendered: list[dict[str, str]] = []
    for index, (name, purpose, input_value, operation, output, benefit) in enumerate(rows):
        cue = cue_for(cues, index, operation)
        # Keep the template's semantic role while attaching the paper-specific
        # cue.  This makes the table useful even when the old note only had a
        # short abstract extraction.
        if cue and cue != operation:
            operation = f"{operation}. Source method cue: {cue}"
        rendered.append(
            {
                "module": name,
                "purpose": purpose,
                "input": input_value,
                "operation": operation,
                "output": output,
                "benefit": benefit,
                "evidence": "본문 method/formulation cue; exact subsection/page는 source audit와 대조 필요",
            }
        )
    return rendered


def render_pipeline(rows: list[dict[str, str]]) -> str:
    lines = [
        "| Module | Purpose | Input | Operation | Output | Interface / expected benefit | Evidence |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                escape_cell(row[key])
                for key in ("module", "purpose", "input", "operation", "output", "benefit", "evidence")
            )
            + " |"
        )
    return "\n".join(lines)


def render_variables(title: str, domain: str, profile_data: dict[str, Any] | None) -> str:
    rows = variables_for(title, domain, profile_data)
    if title in VARIABLE_PRESETS:
        source = source_location(profile_data, detail="equation/notation")
    else:
        source = (
            "domain-normalized interface notation from the reviewed problem/method cue; "
            + source_location(profile_data, detail="exact equation/notation")
        )
    lines = [
        "| Symbol / parameter | Type / unit | Meaning | Used in | Source |",
        "|---|---|---|---|---|",
    ]
    for symbol, kind, meaning, used_in in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    escape_cell(symbol),
                    escape_cell(kind),
                    escape_cell(meaning),
                    escape_cell(used_in),
                    escape_cell(source),
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def runtime_contract(domain: str, title: str) -> dict[str, str]:
    if title == "A New Approach to Linear Filtering and Prediction Problems":
        return {
            "horizon": "현재 시점 filtering, 미래 prediction, 과거 smoothing을 구분한다.",
            "rate": "새 observation마다 한 번의 recursion; original paper는 robot control rate를 지정하지 않는다.",
            "memory": "filtered mean/covariance가 sufficient statistic이며 smoothing은 추가 history가 필요할 수 있다.",
            "compute": "matrix prediction/update가 핵심이며 state dimension과 covariance 연산이 비용을 결정한다.",
            "training": "학습 단계 없음; transition/observation/noise statistics가 주어진 model-based estimator다.",
            "inference": "online prediction → innovation update로 estimate와 covariance를 출력한다.",
        }
    if title == "A Formal Basis for the Heuristic Determination of Minimum Cost Paths":
        return {
            "horizon": "start에서 goal까지의 query horizon; goal test와 path cost가 종료를 결정한다.",
            "rate": "event/query-driven search이며 numeric control frequency는 formulation에 없다.",
            "memory": "OPEN/CLOSED와 parent/cost record를 유지한다.",
            "compute": "node expansion, priority queue와 heuristic evaluation이 query cost를 결정한다.",
            "training": "학습 없음; heuristic과 graph/cost model이 사전 제공된다.",
            "inference": "query마다 frontier를 확장하고 goal에 도달한 path를 반환한다.",
        }
    if title == "Planning and Acting in Partially Observable Stochastic Domains":
        return {
            "horizon": "finite-horizon policy tree 또는 discounted/infinite-horizon belief planning으로 표현된다.",
            "rate": "action-observation event마다 belief를 갱신한다; robot control rate는 paper formulation 밖이다.",
            "memory": "observation history를 belief bₜ로 압축하며 policy tree/value representation을 추가로 유지한다.",
            "compute": "belief branching, backup와 policy-tree size가 horizon/observation cardinality에 따라 증가한다.",
            "training": "기본 formulation은 learned policy training보다 known POMDP model planning이다.",
            "inference": "belief에서 action을 선택하고 observation을 받은 뒤 다음 belief로 진행한다.",
        }
    if title in {
        "A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation",
        "Hybrid Position/Force Control of Manipulators",
        "Impedance Control: An Approach to Manipulation: Part I—Theory",
    }:
        return {
            "horizon": "instantaneous task-space/reference tracking을 반복하는 receding closed loop다.",
            "rate": "센서·actuator feedback loop마다 실행되며 original formulation에는 numeric rate가 없다.",
            "memory": "현재 q/q̇, task reference와 wrench/force feedback; 명시적 long history는 필요하지 않다.",
            "compute": "Jacobian/dynamics inversion 또는 task-space control solve와 sensor bandwidth가 latency를 결정한다.",
            "training": "학습 없음; robot model, task frame/gains/selection과 desired dynamics를 설계한다.",
            "inference": "매 control tick에서 task error/contact feedback을 읽고 torque/command를 다시 계산한다.",
        }
    if title == "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion":
        return {
            "horizon": "observation-conditioned action horizon H를 denoise하고 receding-horizon으로 일부 action을 실행한다.",
            "rate": "diffusion sampling/inference rate와 low-level robot control rate가 분리되며 numeric value는 본문 확인 필요.",
            "memory": "현재 observation 또는 짧은 observation history와 noisy action trajectory를 유지한다.",
            "compute": "denoising iteration 수, action horizon H와 visual/temporal backbone이 latency를 결정한다.",
            "training": "demonstration action trajectory에 conditional diffusion/denoising objective를 학습한다.",
            "inference": "noise에서 conditioned action chunk를 반복 denoise하고 chunk 일부를 실행한 뒤 replan한다.",
        }
    values: dict[str, dict[str, str]] = {
        "planning": {
            "horizon": "start/goal 또는 task sequence까지의 long-horizon plan; exact horizon은 paper-specific.",
            "rate": "query/event-driven planning 뒤 controller가 partial plan을 실행; numeric rate 확인 필요.",
            "memory": "graph/tree/roadmap/plan and current state; history size는 method-specific.",
            "compute": "collision checking, search branching 또는 optimization iterations가 latency를 결정한다.",
            "training": "대체로 학습 없음 또는 offline model construction; learned component 여부 확인 필요.",
            "inference": "현재 state/goal에서 plan을 query하고 feasibility feedback으로 재계획한다.",
        },
        "rl": {
            "horizon": "rollout/return horizon과 episode termination; exact n-step/discount는 본문 확인 필요.",
            "rate": "training update와 environment step이 분리되며 deployment control rate는 별도 contract다.",
            "memory": "replay/rollout buffer와 actor/critic parameters; recurrent history 여부 확인 필요.",
            "compute": "environment interaction, value/policy update와 batch size가 비용을 결정한다.",
            "training": "rollout 또는 fixed data에서 reward/return target을 만들고 policy/value를 update한다.",
            "inference": "학습된 policy/controller가 observation마다 action을 출력하며 exploration 설정을 분리한다.",
        },
        "offline_rl": {
            "horizon": "offline trajectory/discounted return horizon; deployment horizon과 분리한다.",
            "rate": "training은 batch update, inference는 environment control tick; exact values 확인 필요.",
            "memory": "fixed dataset, value/policy parameters와 optional context/history.",
            "compute": "dataset size, conservative/value update와 sequence/action decoding이 비용을 결정한다.",
            "training": "새 online data를 수집하지 않고 dataset support 안에서 value/policy를 학습한다.",
            "inference": "학습된 policy가 현재 observation/history에서 action을 선택한다; OOD action 여부를 점검한다.",
        },
        "il": {
            "horizon": "single-step 또는 action chunk/trajectory horizon; exact chunk length는 본문 확인 필요.",
            "rate": "training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인.",
            "memory": "current observation, temporal history 또는 recurrent/sequence context.",
            "compute": "backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다.",
            "training": "demonstration observation-action sequence로 policy/action distribution을 fit한다.",
            "inference": "현재 observation/history에서 action을 예측·부분 실행하고 next observation으로 갱신한다.",
        },
        "vla": {
            "horizon": "instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific.",
            "rate": "policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요.",
            "memory": "image-language-proprioception history, transformer context 또는 persistent memory.",
            "compute": "multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다.",
            "training": "web/robot pretraining, demonstrations 또는 fine-tuning stage를 분리해 확인한다.",
            "inference": "observation+language를 encode해 action/skill chunk를 출력하고 feedback으로 replanning한다.",
        },
        "generative": {
            "horizon": "noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요.",
            "rate": "training update와 iterative sampling/inference rate가 분리된다.",
            "memory": "current noisy sample, condition과 time/noise embedding.",
            "compute": "number of denoising/ODE steps와 network evaluation이 latency를 결정한다.",
            "training": "data/noise/path pair로 denoiser/score/velocity field를 학습한다.",
            "inference": "base noise에서 iterative sample/action을 생성하고 downstream controller가 실행한다.",
        },
        "3d_perception": {
            "horizon": "single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요.",
            "rate": "per-frame/streaming inference와 downstream policy/control rate가 분리된다.",
            "memory": "camera poses, map/scene graph/Gaussian state와 temporal feature.",
            "compute": "3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다.",
            "training": "visual/3D/text supervision 또는 pretrained encoder adaptation; exact split 확인 필요.",
            "inference": "scene observation을 map/feature로 변환해 planner/policy query를 제공한다.",
        },
        "tactile": {
            "horizon": "contact episode 또는 action chunk horizon; contact event timing이 핵심이다.",
            "rate": "tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요.",
            "memory": "recent tactile/force history와 visual state; recurrent memory 여부 확인 필요.",
            "compute": "sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다.",
            "training": "vision/tactile/action demonstrations 또는 simulated contact data로 encoder/policy를 학습한다.",
            "inference": "touch/force feedback을 읽고 action/torque를 짧은 horizon으로 수정한다.",
        },
        "locomotion": {
            "horizon": "gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다.",
            "rate": "high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요.",
            "memory": "proprioceptive history, terrain latent와 contact/body state.",
            "compute": "policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다.",
            "training": "대개 simulation RL/IL과 domain randomization 또는 privileged teacher stage를 분리한다.",
            "inference": "observation/history에서 command/torque를 출력하고 contact feedback으로 adaptation/recovery한다.",
        },
        "humanoid": {
            "horizon": "reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다.",
            "rate": "motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요.",
            "memory": "body pose, contact, reference/history와 fall/recovery state.",
            "compute": "high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다.",
            "training": "motion/teleoperation data, simulation RL/BC와 sim-to-real adaptation stage를 분리한다.",
            "inference": "reference/observation을 whole-body action으로 변환하고 contact/fall feedback으로 조정한다.",
        },
        "estimation": {
            "horizon": "현재 observation의 filtering과 필요 시 future prediction/history smoothing horizon을 구분한다.",
            "rate": "observation arrival마다 estimator update; numeric sensor/control rate는 paper-specific.",
            "memory": "state estimate와 uncertainty summary; smoothing이면 observation/history buffer가 추가된다.",
            "compute": "state dimension, covariance/model update와 sensor synchronization이 latency를 결정한다.",
            "training": "model-based estimator라면 학습 없음; learned estimator 여부는 본문 확인 필요.",
            "inference": "measurement를 받아 state/uncertainty를 update하고 downstream planner/controller에 전달한다.",
        },
        "control": {
            "horizon": "instantaneous or receding-horizon reference tracking; exact prediction horizon은 본문 확인 필요.",
            "rate": "sensor/actuator control tick마다 feedback solve; numeric rate는 paper-specific.",
            "memory": "현재 joint/task state, reference, contact/wrench feedback; long history 여부 확인 필요.",
            "compute": "dynamics/Jacobian evaluation, QP/MPC/inverse-dynamics solve와 actuator latency가 결정한다.",
            "training": "classical controller는 학습 없음; learned component이 있으면 offline/online stage를 분리한다.",
            "inference": "current state/error를 읽고 feasible torque/force/velocity command를 매 tick 재계산한다.",
        },
        "manipulation": {
            "horizon": "grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요.",
            "rate": "perception/planning rate와 low-level contact control rate가 분리된다.",
            "memory": "object/contact state, current pose와 tactile/force history; exact window 확인 필요.",
            "compute": "point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다.",
            "training": "demonstrations, synthetic contact data 또는 optimization setup을 본문에서 구분한다.",
            "inference": "geometry/contact observation에서 grasp/trajectory를 만들고 feedback으로 correction/replan한다.",
        },
        "world_model": {
            "horizon": "latent rollout/planning horizon과 real execution horizon을 분리한다.",
            "rate": "world-model prediction rate, planner rate와 low-level control rate가 분리된다.",
            "memory": "latent state, observation/action history와 imagined rollout buffer.",
            "compute": "encoder/decoder, rollout length와 uncertainty/sample count가 latency를 결정한다.",
            "training": "observation/action sequence에서 latent representation과 dynamics objective를 학습한다.",
            "inference": "current latent에서 candidate future를 imagine하고 policy/planner action을 선택한다.",
        },
        "safety": {
            "horizon": "현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요.",
            "rate": "nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다.",
            "memory": "risk score, recent trajectory/history와 recovery state.",
            "compute": "risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다.",
            "training": "failure data, safe-set/model 또는 policy training stage를 분리한다.",
            "inference": "nominal action을 monitor하고 필요 시 shield/filter/recovery action으로 바꾼다.",
        },
        "simulation": {
            "horizon": "simulator step, rollout length와 task episode horizon을 분리한다.",
            "rate": "simulation step rate와 learned policy/control rate를 별도로 기록한다.",
            "memory": "sim state, contact state와 rollout/replay buffer.",
            "compute": "physics solver, parallel environments와 differentiable rollout cost가 결정한다.",
            "training": "simulation rollout에서 policy/model/controller를 학습하거나 data를 생성한다.",
            "inference": "controller/action을 simulator step에 적용하고 next state를 반환한다.",
        },
        "navigation": {
            "horizon": "map-level start-goal plan과 local controller horizon을 계층적으로 분리한다.",
            "rate": "mapping/localization, global planner, local planner와 base controller rate를 구분한다.",
            "memory": "map/scene graph, pose history와 current local goal.",
            "compute": "map update, collision checking, path search와 replanning frequency가 결정한다.",
            "training": "learned perception/planner가 있으면 data/simulation stage를 classical planner와 구분한다.",
            "inference": "sensor stream으로 map을 갱신하고 goal/path/velocity를 재계획한다.",
        },
        "robot_data": {
            "horizon": "trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다.",
            "rate": "data recording/action sampling rate와 policy inference/control rate를 분리한다.",
            "memory": "trajectory, embodiment/task metadata와 dataset index.",
            "compute": "data decoding, normalization/augmentation과 downstream training budget이 결정한다.",
            "training": "heterogeneous trajectories를 normalize/condition해 policy or representation을 학습한다.",
            "inference": "learned policy가 shared observation/action schema로 target embodiment command를 출력한다.",
        },
        "benchmark": {
            "horizon": "benchmark episode/task horizon과 method rollout horizon을 명시해야 한다.",
            "rate": "benchmark step/control rate, reset and evaluation throughput을 분리한다.",
            "memory": "episode logs, seed/split metadata와 method state/history.",
            "compute": "environment throughput, policy inference와 evaluation parallelism이 결정한다.",
            "training": "benchmark training split과 held-out evaluation split을 구분한다.",
            "inference": "동일 interface와 protocol로 각 baseline/method를 실행하고 metrics/failures를 기록한다.",
        },
        "vision": {
            "horizon": "single image 또는 video/window input; downstream action horizon과 구분한다.",
            "rate": "feature extraction rate와 downstream robot control rate를 분리한다.",
            "memory": "image batch, temporal feature/history 또는 map state.",
            "compute": "backbone resolution, feature memory와 downstream head가 latency를 결정한다.",
            "training": "pretraining objective와 downstream fine-tuning/evaluation stage를 분리한다.",
            "inference": "image/video를 feature/query로 변환해 downstream grounding/state/policy에 제공한다.",
        },
        "sim2real": {
            "horizon": "sim training episode와 real deployment episode; adaptation window를 별도로 기록한다.",
            "rate": "sim step/policy rate와 real sensor/actuator rate를 분리한다.",
            "memory": "domain parameter/latent adaptation, proprioceptive history와 calibration state.",
            "compute": "randomized simulation throughput, adaptation encoder와 real-time policy inference가 결정한다.",
            "training": "randomized/privileged simulation stage와 optional real adaptation을 구분한다.",
            "inference": "real-observable input으로 policy를 실행하고 mismatch/adaptation feedback을 반영한다.",
        },
    }
    default = {
        "horizon": "paper-specific horizon; 본문 확인 필요.",
        "rate": "paper-specific inference/control rate; 본문 확인 필요.",
        "memory": "paper-specific history/state memory; 본문 확인 필요.",
        "compute": "representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요.",
        "training": "paper-specific training/offline setup; 본문 확인 필요.",
        "inference": "paper-specific inference/deployment loop; 본문 확인 필요.",
    }
    return values.get(domain, default)


def evaluation_cues(markdown: str) -> dict[str, list[str]]:
    sections = parse_sections(markdown)
    aliases = {
        "dataset": ("Dataset / Benchmark", "Dataset", "Benchmark"),
        "protocol": ("Evaluation Protocol and Results", "Main Results", "Protocol", "Evaluation Scope"),
        "metric": ("Metrics", "Metric"),
        "baseline": ("Baselines", "Baseline"),
        "ablation": ("Ablations", "Ablation", "Failure and Reproducibility"),
        "failure": ("Limitations and Reproducibility", "Failure and Reproducibility", "Reproducibility Notes"),
    }
    output: dict[str, list[str]] = {}
    for key, names in aliases.items():
        values: list[str] = []
        for name in names:
            values.extend(useful_lines(sections.get(name, ""), 6))
        output[key] = list(dict.fromkeys(values))[:6]
    # In many legacy 04 notes the Baselines heading was left as a placeholder
    # even though the protocol paragraph names the comparison methods.  Use
    # those explicit comparison cues as a link, but retain the 04 provenance
    # marker rather than presenting them as newly verified results.
    protocol_lines = output.get("protocol", [])
    if not output.get("baseline"):
        output["baseline"] = [
            line
            for line in protocol_lines
            if re.search(r"baseline|compare|compared|against|prior|state[- ]of[- ]the[- ]art|sota", line, re.I)
        ][:6]
    if not output.get("ablation"):
        output["ablation"] = [
            line
            for line in protocol_lines
            if re.search(r"ablat|w/o|without|remove|variant|deconstruct|necessity|component", line, re.I)
        ][:6]
    return output


def eval_value(values: list[str], fallback: str) -> str:
    if not values:
        return fallback
    return " ".join(values[:2])


def render_evaluation_link(rows: list[dict[str, str]], eval_data: dict[str, list[str]]) -> str:
    baseline = eval_value(eval_data.get("baseline", []), "04_evaluation.md에 method-specific baseline이 기록되지 않음 — 본문 확인 필요")
    ablation = eval_value(eval_data.get("ablation", []), "04_evaluation.md에 module ablation이 기록되지 않음 — 본문 확인 필요")
    protocol = eval_value(eval_data.get("protocol", []), "04_evaluation.md에 protocol/result cue가 기록되지 않음 — 본문 확인 필요")
    metrics = eval_value(eval_data.get("metric", []), "04_evaluation.md에 metric cue가 기록되지 않음 — 본문 확인 필요")

    lines = [
        "> **Reading rule:** 아래 표는 04의 baseline/ablation cue를 method module에 연결하는 audit link다. 새로운 결과 수치를 주장하지 않으며, 원래의 protocol과 값은 [04_evaluation.md](./04_evaluation.md)에 둔다.",
        "",
        "| Method module | What the evaluation should isolate | Baseline / ablation link | Evidence |",
        "|---|---|---|---|",
    ]
    for index, row in enumerate(rows):
        if index == 0:
            comparison = baseline
        elif index == 1:
            comparison = f"Baseline: {baseline}; module removal/variant cue: {ablation}"
        else:
            comparison = f"Execution/recovery ablation: {ablation}; protocol cue: {protocol}"
        lines.append(
            "| "
            + " | ".join(
                [
                    escape_cell(row["module"]),
                    escape_cell(row["benefit"]),
                    escape_cell(comparison),
                    escape_cell("04_evaluation.md cue; exact table/section 확인 필요"),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            f"- **Protocol / metric cue:** {protocol}",
            f"- **Metric cue:** {metrics}",
            f"- **Dataset / benchmark cue:** {eval_value(eval_data.get('dataset', []), '04_evaluation.md에 dataset/benchmark cue가 기록되지 않음 — 본문 확인 필요')}",
        ]
    )
    return "\n".join(lines)


def assumptions_and_failure(profile_data: dict[str, Any]) -> str:
    assumptions = profile_data.get("assumptions", [])
    lines = ["| Strong assumption | Why it matters to method | Failure / stress test |", "|---|---|---|"]
    for assumption, reason, failure in assumptions[:4]:
        lines.append("| " + " | ".join(escape_cell(value) for value in (assumption, reason, failure)) + " |")
    return "\n".join(lines)


def render_intensive(
    item: dict[str, Any],
    old: str,
    overview: str,
    evaluation: str,
    tracker: dict[str, dict[str, str]],
    profile_data: dict[str, Any],
) -> str:
    title = str(item["title"])
    evidence = evidence_for(item, old, overview, tracker)
    cues = source_cues(old, overview)
    domain = profile_data.get("domain", "general")
    rows = domain_modules(profile_data, cues)
    runtime = runtime_contract(domain, title)
    formal = SPECIAL_FORMAL.get(title)
    if formal is None:
        formal = (
            "정확한 method-specific equation/loss/control law는 아래의 verified formulation bridge와 source cue를 기준으로 본문에서 대조한다. "
            "현재 note는 근거 없는 수식 번호나 hyperparameter를 추가하지 않는다."
        )
    source = source_location(profile_data)
    scope = DOMAIN_SCOPE.get(domain, DOMAIN_SCOPE["general"])

    return (
        f"# Method — {title}\n\n"
        "> Canonical metadata: [01_overview.md](./01_overview.md).\n"
        f"> Evidence maturity: `{evidence}`.\n"
        f"> Analysis basis: {basis_text(profile_data)}\n\n"
        "## Method in One Sentence\n\n"
        f"{profile_data['changes']}\n\n"
        "## Design Rationale\n\n"
        f"{profile_data['bottleneck']}\n\n"
        "## Source Evidence Cues\n\n"
        f"{source_evidence(cues, profile_data['anchor'])}\n\n"
        "## Pipeline\n\n"
        f"{render_pipeline(rows)}\n\n"
        "## Objective / Update Rule\n\n"
        f"- **Primary objective:** {profile_data['objective']}\n"
        f"- **State/model bridge:** {profile_data['model']}\n"
        f"- **Constraint or regularization boundary:** {profile_data['constraints']}\n"
        "- **Optimization/update:** module별 update와 optimizer/gain/solver의 exact choice는 아래 formal cue와 source anchor를 기준으로 확인한다; 근거 없는 수치·optimizer는 추가하지 않았다.\n"
        f"- **Source:** {source}\n\n"
        "## Variables and Parameters\n\n"
        f"{render_variables(title, domain, profile_data)}\n\n"
        "## Observation–State–Action Interface\n\n"
        f"- **Observation / input:** {scope[1]}\n"
        f"- **State / latent representation:** {scope[2]}\n"
        f"- **Action / output:** {scope[3]}\n"
        f"- **Planner–controller / policy–environment interface:** {profile_data['loop']}\n\n"
        "## Temporal and Runtime Contract\n\n"
        f"- **Horizon:** {runtime['horizon']}\n"
        f"- **Inference/control rate:** {runtime['rate']}\n"
        f"- **History / memory:** {runtime['memory']}\n"
        f"- **Compute / latency dependency:** {runtime['compute']}\n\n"
        "## Training vs Inference\n\n"
        f"- **Training / offline setup:** {runtime['training']}\n"
        f"- **Inference / online execution:** {runtime['inference']}\n"
        "- **Boundary to keep separate:** training throughput, policy inference rate, low-level actuator rate와 feedback latency를 하나의 숫자로 합치지 않는다. paper-specific values는 본문 확인 필요.\n\n"
        "## Method-Specific Formal Details\n\n"
        f"- **Canonical equation/law cue:** {formal}\n"
        f"- **Verified formulation bridge:** {profile_data['model']}\n"
        f"- **Source location:** {source}\n\n"
        "## Evaluation Link\n\n"
        f"{render_evaluation_link(rows, evaluation_cues(evaluation))}\n\n"
        "## Failure and Ablation Link\n\n"
        f"{assumptions_and_failure(profile_data)}\n\n"
        "- **Ablation to request if absent:** remove the paper-specific core module while holding input, data, compute, horizon and controller interface fixed.\n"
        "- **Failure evidence location:** [04_evaluation.md](./04_evaluation.md)의 failure/limitation 및 reproducibility cue; 현재 note에 새로운 failure claim을 만들지 않는다.\n\n"
        "## Reproduction Checklist\n\n"
        "1. [ ] 01 overview와 source anchor에서 observation/state/action, exact notation과 model assumptions를 확인한다.\n"
        "2. [ ] Pipeline의 각 module을 input/output contract와 함께 구현하고, source-specific equation/solver/decoder를 고정한다.\n"
        "3. [ ] Training/offline setup, inference rate, horizon, memory, compute budget을 분리해 기록한다.\n"
        "4. [ ] 04의 baseline과 module-removal/variant ablation을 같은 task, data, seed, budget으로 실행한다.\n"
        "5. [ ] primary metric뿐 아니라 failure mode, latency, assumption sensitivity와 closed-loop recovery를 보고한다.\n\n"
        "## Verification Questions\n\n"
        f"- **Equation/source:** {source}\n"
        "- **Module attribution:** 04의 baseline/ablation이 어느 pipeline module을 실제로 제거·대체하는가?\n"
        "- **Runtime:** action horizon/chunk, memory window, inference rate와 low-level control rate가 각각 얼마인가?\n"
        "- **Evidence boundary:** 현재 evidence level에서 직접 확인되지 않은 exact value, negative result, reproducibility detail을 추가하지 않았는가?\n"
    )


def render_scaffold(
    item: dict[str, Any],
    old: str,
    overview: str,
    evaluation: str,
    tracker: dict[str, dict[str, str]],
) -> str:
    title = str(item["title"])
    evidence = evidence_for(item, old, overview, tracker)
    cues = source_cues(old, overview)
    overview_sections = parse_sections(overview)
    method_sentence = compact_cue(
        "\n".join(cues.get("brief", []) + cues.get("core", [])),
        "현재 source 범위에서 핵심 method는 본문 확인 필요.",
    )
    rationale = compact_cue(
        "\n".join(cues.get("rationale", [])),
        compact_cue(first_section(overview_sections, "Problem", "Limitation"), "설계 rationale은 본문 확인 필요."),
    )
    interface = compact_cue(
        "\n".join(cues.get("interface", [])),
        "observation/state/action/control interface는 본문 확인 필요.",
    )
    eval_data = evaluation_cues(evaluation)
    placeholder_rows = [
        {
            "module": "Paper-specific method module",
            "purpose": "목적과 bottleneck은 본문 확인 필요",
            "input": interface,
            "operation": method_sentence,
            "output": "output/action/estimate는 본문 확인 필요",
            "benefit": "paper-specific benefit은 04와 대조",
            "evidence": "기존 note cue; exact method section/page 확인 필요",
        }
    ]
    runtime = runtime_contract("general", title)
    fake_profile = None
    source = source_location(fake_profile)
    return (
        f"# Method — {title}\n\n"
        "> Canonical metadata: [01_overview.md](./01_overview.md).\n"
        f"> Evidence maturity: `{evidence}`.\n"
        f"> Analysis basis: {basis_text(None)}\n\n"
        "## Method in One Sentence\n\n"
        f"{method_sentence}\n\n"
        "## Design Rationale\n\n"
        f"{rationale}\n\n"
        "## Source Evidence Cues\n\n"
        f"{source_evidence(cues, '현재 note/01 overview cue; exact method location 확인 필요')}\n\n"
        "## Pipeline\n\n"
        f"{render_pipeline(placeholder_rows)}\n\n"
        "## Objective / Update Rule\n\n"
        "- **Objective/loss/control law:** 본문 확인 필요.\n"
        "- **Optimization/update:** 본문 확인 필요.\n"
        "- **Constraint/regularization:** 본문 확인 필요.\n"
        f"- **Source:** {source}\n\n"
        "## Variables and Parameters\n\n"
        f"{render_variables(title, 'general', None)}\n\n"
        "## Observation–State–Action Interface\n\n"
        f"- **Observation / input:** {interface}\n"
        "- **State / latent representation:** 본문 확인 필요.\n"
        "- **Action / output:** 본문 확인 필요.\n"
        "- **Planner–controller / policy–environment interface:** 본문 확인 필요.\n\n"
        "## Temporal and Runtime Contract\n\n"
        f"- **Horizon:** {runtime['horizon']}\n"
        f"- **Inference/control rate:** {runtime['rate']}\n"
        f"- **History / memory:** {runtime['memory']}\n"
        f"- **Compute / latency dependency:** {runtime['compute']}\n\n"
        "## Training vs Inference\n\n"
        "- **Training / offline setup:** 본문 확인 필요.\n"
        "- **Inference / online execution:** 본문 확인 필요.\n"
        "- **Boundary to keep separate:** training, inference, control rate, horizon과 memory를 각각 본문에서 확인한다.\n\n"
        "## Method-Specific Formal Details\n\n"
        "- Exact equation/loss/control law와 variable meaning은 본문 확인 필요.\n\n"
        "## Evaluation Link\n\n"
        f"{render_evaluation_link(placeholder_rows, eval_data)}\n\n"
        "## Failure and Ablation Link\n\n"
        "- Strongest assumption, failure mode와 module ablation은 본문 및 04_evaluation.md에서 확인 필요.\n"
        "- 현재 note cue만으로 baseline/ablation의 causal attribution을 확정하지 않는다.\n\n"
        "## Reproduction Checklist\n\n"
        "1. [ ] method section에서 module input/output와 exact objective를 확인한다.\n"
        "2. [ ] variable/unit, horizon, rate, memory와 implementation dependency를 기록한다.\n"
        "3. [ ] 04의 baseline, ablation, metric, split과 failure protocol을 대조한다.\n\n"
        "## Verification Questions\n\n"
        "- **Still to verify:** exact method equation, variable table source, training/inference boundary, runtime contract과 module-level evaluation attribution.\n"
    )


def render_note(
    item: dict[str, Any],
    old: str,
    overview: str,
    evaluation: str,
    tracker: dict[str, dict[str, str]],
) -> tuple[str, bool]:
    title = str(item["title"])
    profile_data = PROBLEM_PROFILES.get(title)
    if profile_data is not None:
        return render_intensive(item, old, overview, evaluation, tracker, profile_data), True
    return render_scaffold(item, old, overview, evaluation, tracker), False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write normalized notes; default is dry-run")
    parser.add_argument("--show", type=int, default=0, help="show the first N generated notes in dry-run mode")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    tracker = read_tracker()
    counts: Counter[str] = Counter()
    changed = 0
    missing_evaluations: list[str] = []
    previews: list[str] = []

    for item in manifest:
        folder = resolve_folder(str(item["folder"]))
        method_path = folder / "03_method.md"
        overview_path = folder / "01_overview.md"
        evaluation_path = folder / "04_evaluation.md"
        old = method_path.read_text(encoding="utf-8")
        overview = overview_path.read_text(encoding="utf-8")
        evaluation = evaluation_path.read_text(encoding="utf-8") if evaluation_path.exists() else ""
        new, intensive = render_note(item, old, overview, evaluation, tracker)
        counts["CORE/NEXT detailed profile" if intensive else "registry scaffold"] += 1
        changed += int(new != old)
        if not evaluation_path.exists():
            missing_evaluations.append(title := str(item["title"]))
        if args.show and len(previews) < args.show:
            previews.append(f"--- {method_path}\n{new}")
        if args.apply and new != old:
            method_path.write_text(new, encoding="utf-8")

    mode = "apply" if args.apply else "dry-run"
    print(
        {
            "mode": mode,
            "registry_papers": len(manifest),
            "notes_to_update": changed,
            "intensive_profiles": len(PROBLEM_PROFILES),
            "missing_evaluation_notes": len(missing_evaluations),
            "profile_or_scaffold": dict(counts),
        }
    )
    for title in missing_evaluations:
        print(f"MISSING EVALUATION: {title}")
    for preview in previews:
        print(preview)


if __name__ == "__main__":
    main()
