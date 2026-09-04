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
    from registry_profiles import enrich_profiles
    from registry_schema import (
        CURATION_ROLES,
        FACET_KEYS,
        publication_kind,
        publication_status,
        venue_id_for,
    )
except ModuleNotFoundError:
    from .registry_profiles import enrich_profiles
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
    (ROOT / "work" / "sources" / "fulltext_all_review_manifest_2026-09-02.json", "all"),
]
REVIEW_SCOPE_PRIORITY = {"historical": 0, "reference": 1, "current": 2, "all": 3}
NOTE_REVIEW_MANIFESTS = [
    {
        "path": ROOT / "work" / "sources" / "fulltext_insights_review_manifest_2026-09-03.json",
        "scope": "insights",
        "note_name": "05_insights.md",
    },
]

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
# not a replacement for a full citation graph.  The source, basis, evidence
# scope, and review date make the distinction explicit and allow later manual
# promotion/demotion.  The edge direction is always ``from`` paper -> ``to``
# paper: a method points to its conceptual/method/data predecessor, and a
# baseline paper points to the paper that evaluates it.
RELATION_SEEDS = [
    {
        "from": "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control",
        "type": "extends",
        "to": "RT-1: Robotics Transformer for Real-World Control at Scale",
        "basis": "named follow-up in the robot-policy lineage; verify against the paper references",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
    },
    {
        "from": "Octo: An Open-Source Generalist Robot Policy",
        "type": "uses_dataset",
        "to": "Open X-Embodiment: Robotic Learning Datasets and RT-X Models",
        "basis": "the Octo record identifies Open X-Embodiment as its pretraining data lineage",
        "confidence": "manual",
        "evidence_scope": "paper_body",
    },
    {
        "from": "OpenVLA: An Open-Source Vision-Language-Action Model",
        "type": "uses_dataset",
        "to": "Open X-Embodiment: Robotic Learning Datasets and RT-X Models",
        "basis": "the OpenVLA record identifies Open X-Embodiment as its robot-data source",
        "confidence": "manual",
        "evidence_scope": "paper_body",
    },
    {
        "from": "π0.5: a Vision-Language-Action Model with Open-World Generalization",
        "type": "extends",
        "to": "π0: A Vision-Language-Action Flow Model for General Robot Control",
        "basis": "explicit model-version lineage in the paper title and official publication path",
        "confidence": "manual",
        "evidence_scope": "title_lineage",
    },
    {
        "from": "GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots",
        "type": "extends",
        "to": "NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots",
        "basis": "explicit improved-version lineage in the official NVIDIA model pages",
        "confidence": "manual",
        "evidence_scope": "official_project",
    },
    {
        "from": "GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots",
        "type": "extends",
        "to": "GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots",
        "basis": "explicit improved-version lineage in the official NVIDIA model pages",
        "confidence": "manual",
        "evidence_scope": "official_project",
    },
    {
        "from": "Demonstrating GPU Parallelized Robot Simulation and Rendering for Generalizable Embodied AI with ManiSkill3",
        "type": "extends",
        "to": "ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations",
        "basis": "named ManiSkill3 evolution of the ManiSkill simulator/benchmark family",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
    },
    # Existing sparse admission edges are repeated with provenance so the
    # reconciliation pass can enrich them without overwriting their current
    # confidence value.
    {
        "from": "3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations",
        "type": "extends",
        "to": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
        "basis": "the paper defines DP3 as a 3D visuomotor diffusion policy and its method/evaluation notes identify the Diffusion Policy formulation as the direct policy lineage",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation",
        "type": "extends",
        "to": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
        "basis": "the paper accelerates visuomotor diffusion policies through consistency distillation and uses Diffusion Policy as the direct policy reference",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "Diffusion Meets DAgger: Supercharging Eye-in-hand Imitation Learning",
        "type": "extends",
        "to": "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning",
        "basis": "the paper explicitly frames its method as combining diffusion policy learning with the DAgger data-aggregation formulation",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space",
        "type": "extends",
        "to": "PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation",
        "basis": "the abstract identifies PointNet as the pioneer, states its missing local-structure limitation, and applies PointNet recursively in the proposed hierarchy",
        "confidence": "verified",
        "evidence_scope": "official_abstract",
    },
    {
        "from": "ORB-SLAM: A Versatile and Accurate Monocular SLAM System",
        "type": "builds_on",
        "to": "PTAM: Parallel Tracking and Mapping for Small AR Workspaces",
        "basis": "the introduction explicitly says that ORB-SLAM builds on the main ideas of PTAM",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "3D Gaussian Splatting for Real-Time Radiance Field Rendering",
        "type": "builds_on",
        "to": "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis",
        "basis": "the introduction positions 3D Gaussian Splatting against the continuous NeRF radiance-field formulation; this is a representation-family dependency, not a claim of identical implementation",
        "confidence": "inferred",
        "evidence_scope": "paper_body",
    },
    {
        "from": "Policy Gradient Methods for Reinforcement Learning with Function Approximation",
        "type": "builds_on",
        "to": "Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning",
        "basis": "the paper develops the function-approximation policy-gradient form around Williams's REINFORCE method, whose earlier formulation is the registry predecessor",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "Trust Region Policy Optimization",
        "type": "builds_on",
        "to": "Policy Gradient Methods for Reinforcement Learning with Function Approximation",
        "basis": "the method section identifies the standard policy-gradient update as a limiting case of its trust-region objective",
        "confidence": "inferred",
        "evidence_scope": "paper_body",
    },
    {
        "from": "Proximal Policy Optimization Algorithms",
        "type": "extends",
        "to": "Trust Region Policy Optimization",
        "basis": "the abstract states that PPO retains benefits of TRPO while being simpler, and the method section replaces the hard trust-region constraint with a clipped surrogate objective",
        "confidence": "verified",
        "evidence_scope": "official_abstract",
    },
    {
        "from": "Constrained Policy Optimization",
        "type": "extends",
        "to": "Trust Region Policy Optimization",
        "basis": "the paper calls CPO a practical approximation based on trust-region methods and adds constrained-MDP safety guarantees to that policy-search family",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
        "type": "builds_on",
        "to": "Denoising Diffusion Probabilistic Models",
        "basis": "the method represents a visuomotor policy as a conditional denoising-diffusion process, reusing the diffusion-model generation framework",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "π0: A Vision-Language-Action Flow Model for General Robot Control",
        "type": "builds_on",
        "to": "Flow Matching for Generative Modeling",
        "basis": "the method supervises continuous action tokens with conditional flow matching and uses the Flow Matching formulation as its generative policy interface",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching",
        "type": "builds_on",
        "to": "Flow Matching for Generative Modeling",
        "basis": "the introduction and method formulate PointFlowMatch with conditional flow matching, described as a flexible generalization of diffusion-based generation",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation",
        "type": "builds_on",
        "to": "Flow Matching for Generative Modeling",
        "basis": "the method explicitly uses conditional consistency flow matching and cites the flow-matching formulation for its one-step action generation",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation",
        "type": "extends",
        "to": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
        "basis": "the method trains its slow latent policy in a way similar to Diffusion Policy and adds a fast tactile-feedback branch",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation",
        "type": "extends",
        "to": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
        "basis": "the paper instantiates a hierarchical, kinematics-aware diffusion policy for robot action trajectories; the edge denotes policy-family extension rather than a claim that every module is copied",
        "confidence": "inferred",
        "evidence_scope": "paper_body",
    },
    {
        "from": "ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY",
        "type": "extends",
        "to": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
        "basis": "the paper explicitly frames ET-SEED as a trajectory-level SE(3)-equivariant diffusion policy and evaluates the resulting policy against diffusion-policy baselines",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space",
        "type": "extends",
        "to": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
        "basis": "the abstract and introduction define Spherical Diffusion Policy as an SE(3)-equivariant diffusion-policy specialization addressing the base policy's 3D generalization boundary",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning",
        "type": "extends",
        "to": "Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning",
        "basis": "the official NVIDIA abstract explicitly describes Isaac Lab as the natural successor to Isaac Gym",
        "confidence": "verified",
        "evidence_scope": "official_project",
    },
    {
        "from": "π0: A Vision-Language-Action Flow Model for General Robot Control",
        "type": "uses_dataset",
        "to": "Open X-Embodiment: Robotic Learning Datasets and RT-X Models",
        "basis": "the pretraining-data section identifies a subset of OXE/Open X-Embodiment in the π0 training mixture",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "OpenVLA: An Open-Source Vision-Language-Action Model",
        "type": "uses_dataset",
        "to": "DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset",
        "basis": "the pretraining section and training-mixture table identify DROID as a component of the Open-X robot-data mixture",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
        "type": "baseline_for",
        "to": "OpenVLA: An Open-Source Vision-Language-Action Model",
        "basis": "the OpenVLA experiments include a matched Diffusion Policy comparison with aligned input/output specifications",
        "confidence": "verified",
        "evidence_scope": "paper_body",
        "source_url": "https://proceedings.mlr.press/v270/kim25c.html",
    },
    {
        "from": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
        "type": "baseline_for",
        "to": "Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching",
        "basis": "the PointFlowMatch evaluation compares against Diffusion Policy as an image-based policy baseline under the same manipulation benchmark setting",
        "confidence": "verified",
        "evidence_scope": "paper_body",
        "source_url": "https://arxiv.org/abs/2409.07343",
    },
    {
        "from": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
        "type": "baseline_for",
        "to": "FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation",
        "basis": "the FlowPolicy evaluation explicitly compares its 3D flow policy with the 2D Diffusion Policy baseline",
        "confidence": "verified",
        "evidence_scope": "paper_body",
        "source_url": "https://ojs.aaai.org/index.php/AAAI/article/view/33617",
    },
    {
        "from": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
        "type": "baseline_for",
        "to": "Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation",
        "basis": "the experiments compare the proposed slow-fast visual-tactile policy with vanilla Diffusion Policy under the same contact-rich tasks",
        "confidence": "verified",
        "evidence_scope": "paper_body",
        "source_url": "https://www.roboticsproceedings.org/rss21/p052.html",
    },
    {
        "from": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
        "type": "baseline_for",
        "to": "CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity",
        "basis": "the CodeDiffuser evaluation explicitly includes Diffusion Policy among the compared imitation-learning methods",
        "confidence": "verified",
        "evidence_scope": "paper_body",
        "source_url": "https://www.roboticsproceedings.org/rss21/p072.html",
    },
    {
        "from": "3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations",
        "type": "baseline_for",
        "to": "ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY",
        "basis": "the ET-SEED experiments explicitly include 3D Diffusion Policy (DP3) as a direct 3D visuomotor baseline",
        "confidence": "verified",
        "evidence_scope": "paper_body",
        "source_url": "https://openreview.net/forum?id=OheAR2xrtb",
    },
    # Family/version and simulator dependencies recovered from the existing
    # paper-level lineage summaries.  These remain inferred curation edges;
    # they are not intended to stand in for exhaustive citation extraction.
    {
        "from": "PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning",
        "type": "extends",
        "to": "FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning",
        "basis": "the registry lineage summary and the PDDLStream planning-family cue place PDDLStream after FFRob; retain as a family-level dependency until the reference section is manually checked",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
    },
    {
        "from": "Perpetual Humanoid Control for Real-time Simulated Avatars",
        "type": "builds_on",
        "to": "AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control",
        "basis": "the method note states that the PHC discriminator uses the AMP observations, loss formulation, and gradient penalty; the edge records method dependency rather than identical implementation",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting",
        "type": "extends",
        "to": "Perpetual Humanoid Control for Real-time Simulated Avatars",
        "basis": "the existing lineage summary places MaskedMimic after AMP/PHC and its queue/whole-body family position supports a unified extension relation",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
    },
    {
        "from": "HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots",
        "type": "extends",
        "to": "MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting",
        "basis": "the HOVER lineage summary explicitly places it after AMP/PHC/MaskedMimic; this is a family-level controller dependency pending reference-section verification",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
    },
    {
        "from": "SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control",
        "type": "extends",
        "to": "HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots",
        "basis": "the SONIC lineage summary explicitly places the scaled motion-tracking controller after HOVER; retain as an inferred family edge",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
    },
    {
        "from": "Habitat 2.0: Training Home Assistants to Rearrange their Habitat",
        "type": "extends",
        "to": "Habitat: A Platform for Embodied AI Research",
        "basis": "the official benchmark family/version naming and registry lineage summary identify Habitat 2.0 as the physics and rearrangement extension of Habitat",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
    },
    {
        "from": "Habitat 3.0: A Co-Habitat for Humans, Avatars, and Robots",
        "type": "extends",
        "to": "Habitat 2.0: Training Home Assistants to Rearrange their Habitat",
        "basis": "the paper-level lineage summary states that Habitat 3.0 extends Habitat 2.0 toward social, humanoid, and human-in-the-loop evaluation",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
    },
    {
        "from": "Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments",
        "type": "extends",
        "to": "Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning",
        "basis": "the Orbit lineage summary identifies Isaac Gym/Isaac Sim as its GPU simulation predecessor and the framework is presented as an interactive robot-learning extension",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
    },
    {
        "from": "Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning",
        "type": "extends",
        "to": "Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments",
        "basis": "the Isaac Lab lineage summary places it after Orbit, while the official successor relation to Isaac Gym is already recorded separately",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
    },
    {
        "from": "ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations",
        "type": "builds_on",
        "to": "SAPIEN: A SimulAted Part-Based Interactive ENvironment",
        "basis": "the ManiSkill record identifies SAPIEN as its simulation substrate in the paper-level lineage summary; this is a simulator dependency, not a benchmark-equivalence claim",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
    },
    {
        "from": "Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning",
        "type": "builds_on",
        "to": "MuJoCo: A Physics Engine for Model-Based Control",
        "basis": "the registry lineage summary places the Meta-World manipulation suite on the MuJoCo simulation family; exact implementation dependence remains paper-specific",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
    },
    {
        "from": "robosuite: A Modular Simulation Framework and Benchmark for Robot Learning",
        "type": "builds_on",
        "to": "MuJoCo: A Physics Engine for Model-Based Control",
        "basis": "the robosuite record identifies MuJoCo as its simulation substrate and benchmark lineage predecessor",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
    },
    {
        "from": "DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation",
        "type": "extends",
        "to": "GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force",
        "basis": "the tactile-sensor lineage summary places DIGIT after GelSight as a compact, low-cost vision-based tactile design; retain as an inferred hardware-family relation",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
    },
    {
        "from": "TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors",
        "type": "builds_on",
        "to": "DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation",
        "basis": "the TACTO evaluation includes simulated DIGIT imprints and a real DIGIT measurement comparison; the edge records sensor-model dependency, not simulator validation by itself",
        "confidence": "verified",
        "evidence_scope": "paper_body",
    },
    {
        "from": "DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos",
        "type": "extends",
        "to": "DreamGen: Unlocking Generalization in Robot Learning through Video World Models",
        "basis": "the registry lineage summary and generated reading adjacency place DreamDojo after DreamGen in the video-world-model-to-robot-policy line; retain as an inferred family edge pending citation verification",
        "confidence": "inferred",
        "evidence_scope": "title_lineage",
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
                # The all-registry pass is the latest complete source audit.
                # It takes precedence over the current CORE/NEXT review,
                # targeted reference reinforcement, and old snapshots where
                # scopes overlap.
                if paper_id not in reviews or REVIEW_SCOPE_PRIORITY.get(scope, 0) > REVIEW_SCOPE_PRIORITY.get(scopes.get(paper_id, ""), 0):
                    reviews[paper_id] = record
                    scopes[paper_id] = scope
    return reviews, scopes, manifests


def read_note_reviews() -> tuple[dict[str, dict[str, dict]], dict[str, dict]]:
    """Read note-scoped review manifests without entering paper-level precedence.

    A targeted pass over ``05_insights.md`` is evidence about that note, not a
    replacement for the all-registry paper review.  Keeping this input on a
    separate path prevents a partial note pass from changing the selected
    paper-level review source or the current intensive-scope accounting.
    """

    note_reviews: dict[str, dict[str, dict]] = defaultdict(dict)
    manifests: dict[str, dict] = {}
    for spec in NOTE_REVIEW_MANIFESTS:
        path = spec["path"]
        if not path.exists():
            continue
        payload = load_json(path)
        relative = str(path.relative_to(ROOT))
        manifests[relative] = {"payload": payload, **spec}
        for record in payload.get("records", []):
            paper_id = record.get("paper_id")
            if paper_id:
                note_reviews[paper_id][spec["note_name"]] = {
                    "record": record,
                    "manifest": relative,
                    "scope": spec["scope"],
                    "note_name": spec["note_name"],
                }
    return dict(note_reviews), manifests


def note_review_summary(entry: dict) -> dict:
    """Keep stable note provenance fields while avoiding the whole record copy."""

    record = entry.get("record") or {}
    return {
        "manifest": entry.get("manifest"),
        "scope": entry.get("scope"),
        "note_name": entry.get("note_name"),
        "reviewed_on": record.get("reviewed_on") or record.get("review_date"),
        "status": record.get("status"),
        "source_kind": record.get("source_kind"),
        "evidence_level": review_evidence(record),
        "extraction_method": record.get("extraction_method"),
        "extraction_quality": record.get("extraction_quality"),
        "pages": record.get("pages"),
        "sha256": record.get("sha256"),
        "note_basis": record.get("note_basis"),
    }


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


def priority_admission_reason(tier: str, item: dict, track: str) -> str:
    """Create a paper-specific one-line rationale for active reading tiers.

    This is used only by the explicit backfill flag.  It combines the stable
    title, curation role, and existing registry focus tags; it does not infer
    claims from PDF availability or note presence.
    """

    role = (item.get("curation") or {}).get("roles", [])
    role_name = role[0] if role else role_for(item)
    role_phrase = {
        "foundation": "a reusable formulation or system primitive",
        "method": "an algorithmic or policy mechanism",
        "system": "an integrated robotics system and deployment interface",
        "benchmark_or_dataset": "a benchmark, dataset, or evaluation protocol",
    }.get(role_name, "a robotics research contribution")
    tags = [str(value).strip() for value in item.get("tags", []) if str(value).strip()]
    focus = ", ".join(tags[:3]) or item.get("category") or "the selected robotics problem"
    title = item.get("title", "This paper").strip()
    if tier == "CORE":
        return (
            f"{title} is a CORE prerequisite because it establishes {role_phrase} "
            f"around {focus}, providing a reference point for {track or 'robotics'} "
            "comparisons in the observation-to-action loop."
        )
    return (
        f"{title} is a NEXT comparison paper because it extends {role_phrase} "
        f"around {focus} in {track or 'robotics'}, exposing a specialized frontier "
        "after the shared CORE spine."
    )


def retained_admission_reason(tier: str, item: dict, track: str) -> str:
    """Create a paper-specific rationale for the non-intensive registry tiers.

    This is intentionally a curation-level statement.  It uses the manifest's
    title, role, category, and tags; it does not claim that a PDF or experiment
    was reviewed.
    """

    role = (item.get("curation") or {}).get("roles", [])
    role_name = role[0] if role else role_for(item)
    role_phrase = {
        "foundation": "a reusable formulation or system primitive",
        "method": "an algorithmic or policy mechanism",
        "system": "an integrated system or deployment interface",
        "benchmark_or_dataset": "a benchmark, dataset, or evaluation protocol",
    }.get(role_name, "a research contribution")
    tags = [str(value).strip() for value in item.get("tags", []) if str(value).strip()]
    focus = ", ".join(tags[:3]) or item.get("category") or "the selected literature scope"
    title = item.get("title", "This paper").strip()
    line = track or item.get("category") or "the robotics-first registry"
    if tier == "REFERENCE":
        return (
            f"{title} is retained as REFERENCE because it provides {role_phrase} "
            f"around {focus} for targeted comparison in {line}; it is not required "
            "for the current intensive reading spine."
        )
    return (
        f"{title} is retained as ARCHIVE because its {role_phrase} around {focus} "
        f"preserves historical or adjacent context for {line}; it is outside the "
        "current robotics-first intensive scope."
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
    relation = {
        "type": seed["type"],
        "paper_id": target_id,
        "confidence": seed["confidence"],
        "status": "curated",
        "basis": seed["basis"],
        "source": seed.get("source_url") or source.get("page") or source.get("sources", {}).get("primary", {}).get("url"),
        "managed_by": "reconcile_registry_v1",
        "evidence_scope": seed.get("evidence_scope", "official_source"),
        "reviewed_on": seed.get("reviewed_on") or str(date.today()),
    }
    return source_id, relation


def reconcile(
    apply: bool,
    backfill_priority_rationales: bool = False,
    backfill_reference_archive_rationales: bool = False,
) -> dict:
    papers = load_json(MANIFEST)
    original_manifest_hash = sha256(MANIFEST)
    tiers, tracks, sequences = read_tier_maps()
    status_rows = read_status()
    reviews, review_scopes, review_manifests = read_reviews()
    note_reviews, note_review_manifests = read_note_reviews()
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
    backfilled_rationales = 0
    backfilled_retained_rationales = 0
    relation_count_before = sum(len(paper.get("relations", [])) for paper in papers)
    seeded_relations = 0
    enriched_relations = 0
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
        if (
            backfill_priority_rationales
            and tier in {"CORE", "NEXT"}
            and curation.get("rationale_status") != "recorded"
        ):
            curation["admission_reason"] = priority_admission_reason(tier, paper, track or paper.get("primary_track", ""))
            curation["rationale_status"] = "recorded"
            curation["rationale_basis"] = "curation_backfill_2026-09-02"
            curation["rationale_reviewed_on"] = str(date.today())
            backfilled_rationales += 1
            paper["curation"] = curation
        if (
            backfill_reference_archive_rationales
            and tier in {"REFERENCE", "ARCHIVE"}
            and curation.get("rationale_status") != "recorded"
        ):
            curation["admission_reason"] = retained_admission_reason(
                tier,
                paper,
                track or paper.get("primary_track", ""),
            )
            curation["rationale_status"] = "recorded"
            curation["rationale_basis"] = "curation_backfill_reference_archive_2026-09-02"
            curation["rationale_reviewed_on"] = str(date.today())
            backfilled_retained_rationales += 1
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
        # Note-scoped review provenance is intentionally separate from the
        # paper-level ``review`` source above.  A targeted insights pass may
        # cover only a subset of papers and must not replace the complete
        # paper-level review manifest.
        note_review_map = dict(provenance.get("note_review") or {})
        for note_name, entry in note_reviews.get(paper_id, {}).items():
            note_review_map[note_name] = note_review_summary(entry)
        if note_review_map:
            provenance["note_review"] = note_review_map
        provenance["evidence_reconciliation"] = {
            "method": "review_manifest_then_note_evidence_max; note_review manifests attach note-level provenance without changing paper-level review precedence",
            "reconciled_on": str(date.today()),
            "tracker_status_is_independent": True,
        }
        paper["provenance"] = provenance

    # Preserve manually added relations and only add the explicitly managed
    # seed edges when an identical edge is not already present.  If a sparse
    # relation was registered before the curation seed existed, fill only
    # missing provenance fields; never replace an existing confidence value or
    # other user-supplied field.
    for seed in RELATION_SEEDS:
        result = relation_for_seed(seed, ids_by_title, papers_by_id)
        if not result:
            continue
        source_id, relation = result
        existing = papers_by_id[source_id].setdefault("relations", [])
        match = next(
            (
                row
                for row in existing
                if row.get("type") == relation["type"] and row.get("paper_id") == relation["paper_id"]
            ),
            None,
        )
        if match is None:
            existing.append(relation)
            seeded_relations += 1
        else:
            changed = False
            for key, value in relation.items():
                if value not in (None, "") and match.get(key) in (None, ""):
                    match[key] = value
                    changed = True
            if changed:
                enriched_relations += 1

    profile_updates = enrich_profiles(papers, ROOT, reviewed_on=str(date.today()))

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
    changed_note_review_manifests = {}
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

    # Note-review manifests receive a lightweight registry snapshot, but are
    # never included in the paper-level scope-gap calculation above.
    for relative, payload in note_review_manifests.items():
        document = payload["payload"]
        records = document.get("records", [])
        reviewed_ids = {row.get("paper_id") for row in records if row.get("paper_id")}
        document["registry_snapshot"] = {
            "status": "note_level",
            "paper_count_at_reconciliation": len(papers),
            "input_manifest_sha256_before_reconciliation": original_manifest_hash,
            "note_name": payload["note_name"],
            "reviewed_paper_count": len(reviewed_ids),
            "tier_counts_in_review": dict(Counter(row.get("tier") for row in records)),
            "alignment_note": (
                "Note-scoped review provenance only; this manifest does not replace the paper-level review source "
                "and is not used for tier or intensive-scope assignment."
            ),
            "cache_policy": "task-scoped PDF cache is disposable and is not part of the registry source of truth",
        }
        changed_note_review_manifests[payload["path"]] = document

    result = {
        "mode": "apply" if apply else "dry-run",
        "papers": len(papers),
        "evidence_before": dict(evidence_before),
        "evidence_after": dict(evidence_after),
        "generated_rationales": generated_rationales,
        "backfilled_priority_rationales": backfilled_rationales,
        "backfilled_reference_archive_rationales": backfilled_retained_rationales,
        "relation_count_before": relation_count_before,
        "seeded_relations": seeded_relations,
        "enriched_relations": enriched_relations,
        "metadata_profiles": profile_updates,
        "source_index_records": source_index_count,
        "papers_without_public_identifier": no_identifier,
        "tracker_evidence_updates": tracker_updates,
        "review_manifests": [str(path.relative_to(ROOT)) for path in changed_review_manifests],
        "note_review_manifests": [str(path.relative_to(ROOT)) for path in changed_note_review_manifests],
        "note_review_papers": sum(len(entries) for entries in note_reviews.values()),
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
    for path, document in changed_note_review_manifests.items():
        path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    meta = load_json(META)
    meta["paper_count"] = len(papers)
    meta["generated_on"] = str(date.today())
    meta["manifest_sha256"] = sha256(MANIFEST)
    meta["last_reconciled_on"] = str(date.today())
    meta["reconciliation_policy"] = "review manifest evidence is paper-level; per-note evidence is retained under provenance.note_evidence; note-scoped review manifests are retained under provenance.note_review without changing paper-level review precedence; tracker status remains user-controlled."
    meta["relation_count"] = sum(len(paper.get("relations", [])) for paper in papers)
    meta["relation_policy"] = "Directed curated edges in papers.json are not a full citation graph; each managed edge records type, target paper_id, confidence, basis, source, evidence_scope, and reviewed_on."
    meta["metadata_profile_version"] = "1.0"
    meta["metadata_profile_reviewed_on"] = str(date.today())
    meta["evaluation_profile_count"] = profile_updates.get("evaluation_profiles", 0)
    meta["reproducibility_profile_count"] = profile_updates.get("reproducibility_profiles", 0)
    meta["lineage_profile_count"] = profile_updates.get("lineage_profiles", 0)
    META.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result["manifest_sha256"] = meta["manifest_sha256"]
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write reconciled manifest, tracker evidence, and review metadata")
    parser.add_argument(
        "--backfill-priority-rationales",
        action="store_true",
        help="record paper-specific admission rationales for pending CORE/NEXT entries",
    )
    parser.add_argument(
        "--backfill-reference-archive-rationales",
        action="store_true",
        help="record paper-specific retention rationales for pending REFERENCE/ARCHIVE entries",
    )
    args = parser.parse_args()
    print(
        json.dumps(
            reconcile(
                args.apply,
                args.backfill_priority_rationales,
                args.backfill_reference_archive_rationales,
            ),
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
