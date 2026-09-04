#!/usr/bin/env python3
"""Build the long-term robotics-first reading plan and full registry tier index."""

from __future__ import annotations

import csv
import json
import re
import urllib.parse
from collections import OrderedDict
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

try:
    from registry_schema import DETAILED_TRACK_TO_PRIMARY
except ModuleNotFoundError:
    from .registry_schema import DETAILED_TRACK_TO_PRIMARY


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "PAPER.md"
RESEARCH = ROOT / "research"
PLAN = RESEARCH / "READING_PLAN.md"
INDEX = RESEARCH / "READING_TIERS.csv"
STATUS = RESEARCH / "READING_STATUS.csv"
SYNTHESIS = ROOT / "synthesis"


CORE_GROUPS = OrderedDict(
    [
        (
            "Planning, control, and whole-body foundations",
            [
                "=A New Approach to Linear Filtering and Prediction Problems",
                "=A Formal Basis for the Heuristic Determination of Minimum Cost Paths",
                "=Planning and Acting in Partially Observable Stochastic Domains",
                "Unified Approach for Motion and Force",
                "=Hybrid Position/Force Control of Manipulators",
                "=Impedance Control: An Approach to Manipulation: Part I—Theory",
                "Probabilistic Roadmaps",
                "Rapidly-Exploring Random Trees",
                "CHOMP:",
                "TrajOpt:",
                "=MuJoCo: A Physics Engine for Model-Based Control",
                "=Information Theoretic MPC for Model-Based Reinforcement Learning",
                "PDDLStream:",
                "Dynamic Whole-Body Motion Generation",
                "Hierarchical Quadratic Programming",
                "Whole-Body Nonlinear Model Predictive Control",
            ],
        ),
        (
            "RL, IL, and policy learning foundations",
            [
                "=Learning to Predict by the Methods of Temporal Differences",
                "=Q-Learning",
                "=Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning",
                "=Policy Gradient Methods for Reinforcement Learning with Function Approximation",
                "=PILCO: A Model-Based and Data-Efficient Approach to Policy Search",
                "A Reduction of Imitation Learning",
                "Guided Policy Search under Unknown Dynamics",
                "Generative Adversarial Imitation Learning",
                "Trust Region Policy Optimization",
                "Proximal Policy Optimization Algorithms",
                "Soft Actor-Critic",
                "Domain Randomization for Transferring",
                "What Matters in Learning from Offline Human Demonstrations",
                "Implicit Behavioral Cloning",
                "Implicit Q-Learning",
                "Decision Transformer:",
                "Denoising Diffusion Probabilistic Models",
                "Flow Matching for Generative Modeling",
                "Diffusion Policy: Visuomotor",
                "Q-Transformer",
            ],
        ),
        (
            "Manipulation, contact, tactile, and dexterity",
            [
                "=Planning Optimal Grasps",
                "=GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force",
                "Contact-Invariant Optimization",
                "GraspNet-1Billion",
                "Contact-GraspNet",
                "Factory: Fast Contact",
                "Global Planning for Contact-Rich Manipulation",
                "Tactile-Driven Non-Prehensile",
                "RoboPack",
                "DexTrack",
            ],
        ),
        (
            "VLA and generalist robot policies",
            [
                "Learning Transferable Visual Models From Natural Language Supervision",
                "CLIPort",
                "PaLM-E:",
                "RT-1:",
                "RT-2:",
                "VoxPoser",
                "Open X-Embodiment",
                "Octo: An Open",
                "OpenVLA",
                "π0: A Vision-Language-Action Flow Model",
                "π0.5",
            ],
        ),
        (
            "Safety and robot world models",
            [
                "=World Models",
                "DayDreamer",
                "TD-MPC2",
                "Control Barrier Function Based",
                "Recovery RL",
            ],
        ),
        (
            "Locomotion, mobile manipulation, and humanoid systems",
            [
                "=Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point",
                "=AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control",
                "RMA:",
                "Robust Perceptive Locomotion",
                "ANYmal Parkour",
                "HumanoidBench",
                "OmniH2O",
                "Mobile ALOHA",
            ],
        ),
        (
            "Robotics-enabling 3D perception",
            [
                "=A Method for Registration of 3-D Shapes",
                "=PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation",
                "DROID-SLAM",
                "=3D Gaussian Splatting for Real-Time Radiance Field Rendering",
                "ConceptFusion",
                "RVT:",
                "DUSt3R:",
            ],
        ),
    ]
)


NEXT_GROUPS = OrderedDict(
    [
        (
            "Planning, control, simulation, and TAMP extensions",
            [
                "=Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning",
                "=FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning",
                "=Kinodynamic Trajectory Following with STELA: Simultaneous Trajectory Estimation & Local Adaptation",
                "=Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation",
                "=Neural Assembler: Learning to Generate Fine-Grained Robotic Assembly Instructions from Multi-View Images",
                "=Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning",
                "=Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation",
                "=FOCI: Trajectory Optimization on Gaussian Splats",
                "=Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness",
                "=Parallel and Proximal Linear-Quadratic Methods for Real-Time Constrained Model-Predictive Control",
                "=Differentiable Robust Model Predictive Control",
                "=Linear-time Differential Inverse Kinematics: an Augmented Lagrangian Perspective",
                "=NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration",
            ],
        ),
        (
            "RL, IL, offline learning, and robot data",
            [
                "=Behavior Transformers: Cloning k modes with one stone",
                "=R3M: A Universal Visual Representation for Robot Manipulation",
                "=Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?",
                "=Maximum a Posteriori Policy Optimisation",
                "=MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale",
                "=Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning",
                "=Eureka: Human-Level Reward Design via Coding Large Language Models",
                "=DrEureka: Language Model Guided Sim-To-Real Transfer",
                "Continuous Control with Deep",
                "Addressing Function Approximation Error",
                "Hindsight Experience Replay",
                "Constrained Policy Optimization",
                "Conservative Q-Learning",
                "MOPO:",
                "Minimalist Approach to Offline",
                "Learning Complex Dexterous Manipulation",
                "Learning Latent Plans from Play",
                "Relay Policy Learning",
                "RLBench:",
                "MimicGen",
                "DROID: A Large-Scale",
                "=Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots",
                "=SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning",
                "=Robot Fine-Tuning Made Easy: Pre-Training Rewards and Policies for Autonomous Real-World Reinforcement Learning",
                "=RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning",
                "=Demonstrating GPU Parallelized Robot Simulation and Rendering for Generalizable Embodied AI with ManiSkill3",
                "=RoboVerse: A Unified Platform, Benchmark and Dataset for Scalable and Generalizable Robot Learning",
                "=DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies",
                "=Dex1B: Learning with 1B Demonstrations for Dexterous Manipulation",
                "=Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation",
                "=Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation",
                "=You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations",
                "=RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation",
                "=Bridging Perception and Action: Spatially-Grounded Mid-Level Representations for Robot Generalization",
                "=DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning",
                "=AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems",
                "=Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning",
                "=MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation",
                "=Efficient Online Reinforcement Learning with Offline Data",
                "=Diffusion Meets DAgger: Supercharging Eye-in-hand Imitation Learning",
                "=Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation",
                "=Any-point Trajectory Modeling for Policy Learning",
                "=Evaluating Real-World Robot Manipulation Policies in Simulation",
                "=Benchmarking Knowledge Transfer for Lifelong Robot Learning",
                "=MimicPlay: Long-Horizon Imitation Learning by Watching Human Play",
            ],
        ),
        (
            "Contact-rich, deformable, force, and dexterous manipulation",
            [
                "=Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation",
                "=UMPNet: Universal Manipulation Policy Network for Articulated Objects",
                "=Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation",
                "=GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping",
                "=ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation",
                "=Gaussian Splatting Visual MPC for Granular Media Manipulation",
                "=Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects",
                "=DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation",
                "=DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality",
                "Control-Limited Differential",
                "In-Hand Manipulation via Motion Cones",
                "Towards Tight Convex Relaxations",
                "Physics-Driven Data Generation",
                "Complementarity-Free Multi-Contact",
                "SoftGym",
                "DiffSkill",
                "Neural Descriptor Fields",
                "Diffusion-EDFs",
                "IndustReal",
                "Binding Touch to Everything",
                "DenseMatcher:",
                "G3Flow:",
                "Reactive Diffusion Policy:",
                "AT-VLA",
                "ForceVLA2",
                "Dexterous World Models",
                "EquAct:",
                "Tabero:",
                "TactAlign:",
                "DexterityGen:",
                "=V-HOP: Visuo-Haptic 6D Object Pose Tracking",
                "=PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands",
                "=GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty",
                "=Demonstrating REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly",
                "=Robust Peg-in-Hole Assembly under Uncertainties via Compliant and Interactive Contact-Rich Manipulation",
                "=FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning",
                "=CordViP: Correspondence-based Visuomotor Policy for Dexterous Manipulation in Real-World",
                "=FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation",
                "=Sparsh: Self-supervised touch representations for vision-based tactile sensing",
                "=Octopi: Object Property Reasoning with Large Tactile-Language Models",
                "=OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation",
                "=FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation",
                "=Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware",
                "=Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching",
                "=3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations",
            ],
        ),
        (
            "VLA, cross-embodiment, and long-horizon planning",
            [
                "=A Generalist Agent",
                "=CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks",
                "=AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents",
                "=RT-H: Action Hierarchies Using Language",
                "=Gemini Robotics: Bringing AI into the Physical World",
                "=NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots",
                "BC-Z",
                "Perceiver-Actor",
                "VIMA:",
                "Inner Monologue",
                "SayPlan",
                "XSkill",
                "Scaling Proprioceptive-Visual Learning with Heterogeneous",
                "FAST: Efficient Action Tokenization",
                "Fine-Tuning Vision-Language-Action Models",
                "AtomicVLA",
                "PALM:",
                "ActiveVLA",
                "Spatial Memory for Out-of-Vision",
                "Counterfactual VLA",
                "Any3D-VLA",
                "MomaGraph",
                "AVA-VLA:",
                "VLA-Arena:",
                "=SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models",
                "=From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors",
                "=Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks",
                "=Learning to Act Anywhere with Task-centric Latent Actions",
                "=CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision",
                "=NaVILA: Legged Robot Vision-Language-Action Model for Navigation",
                "=ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy",
                "=CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity",
                "=PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation",
                "=Manual2Skill: Learning to Read Manuals and Acquire Robotic Skills for Furniture Assembly Using Vision-Language Models",
                "=SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics",
                "=Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer",
                "=GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots",
                "=GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots",
                "=Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy",
                "=ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation",
                "=VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation",
                "=3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation",
                "=GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data",
                "=Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation",
                "=RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation",
                "=AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation",
                "=SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models",
                "=Vision-Language Foundation Models as Effective Robot Imitators",
                "=Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation",
                "=RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation",
                "=Latent Action Pretraining from Videos",
                "=3D-VLA: A 3D Vision-Language-Action Generative World Model",
                "=VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions",
                "=MIRAGE: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting",
                "=Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation",
                "=LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models",
            ],
        ),
        (
            "World models, uncertainty, failure detection, and recovery",
            [
                "=DreamGen: Unlocking Generalization in Robot Learning through Video World Models",
                "=DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos",
                "Learning Latent Dynamics for Planning from Pixels",
                "Dream to Control",
                "Mastering Diverse Domains through World Models",
                "PIN-WM",
                "Unified World Models",
                "FlowDreamer",
                "Can We Detect Failures Without Failure Data?",
                "SAFE: Multitask",
                "WorldGym",
                "WMPO",
                "FLARE:",
                "Can VLMs Diagnose and Recover",
                "Temporal Difference Calibration",
                "Memory Retrieval in Visuomotor Policies",
                "=Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid",
                "=Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation",
                "=Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift",
                "=Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos",
                "=Map Space Belief Prediction for Manipulation-Enhanced Mapping",
                "=Unified Video Action Model",
                "=From Foresight to Forethought: VLM-In-the-Loop Policy Steering via Latent Alignment",
                "=Prompting with the Future: Open-World Model Predictive Control with Interactive Digital Twins",
                "=Self-Correcting Robot Manipulation via Gaussian-Splatted Foresight",
                "=WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation",
                "=RoboDreamer: Learning Compositional World Models for Robot Imagination",
                "=Learning Interactive Real-World Simulators",
                "=SafeMimic: Towards Safe and Autonomous Human-to-Robot Imitation for Mobile Manipulation",
                "=Ctrl-World: A Controllable Generative World Model for Robot Manipulation",
            ],
        ),
        (
            "Locomotion, whole-body control, mobile manipulation, and humanoids",
            [
                "=Perpetual Humanoid Control for Real-time Simulated Avatars",
                "=MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting",
                "=HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots",
                "=SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control",
                "DeepMimic",
                "Sim-to-Real: Learning Agile Locomotion",
                "Learning Quadrupedal Locomotion over Challenging Terrain",
                "Extreme Parkour",
                "Walk These Ways",
                "HumanPlus",
                "ASAP:",
                "LangWBC",
                "RoboPanoptes",
                "Demonstrating OK-Robot",
                "HWC-Loco",
                "VIRAL",
                "=Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation",
                "=Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation",
                "=AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control",
                "=Demonstrating MOSART: Opening Articulated Structures in the Real World",
                "=HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit",
                "=Flying Hand: End-Effector-Centric Framework for Versatile Aerial Manipulation Teleoperation and Policy Learning",
                "=SPIN: Simultaneous Perception, Interaction and Navigation",
                "=WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts",
                "=ViNT: A Foundation Model for Visual Navigation",
                "=GOAT: GO to Any Thing",
            ],
        ),
        (
            "Active and embodied 3D Vision",
            [
                "Where2Act",
                "FlowBot3D",
                "Ditto: Building Digital Twins",
                "VLMaps",
                "SUGAR: Pre-training 3D Visual Representations for Robotics",
                "Splat-Nav",
                "RoboSpatial:",
                "PointVLA",
                "=Vysics: Object Reconstruction Under Occlusion by Fusing Vision and Contact-Rich Physics",
                "=Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery",
                "=Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects",
                "=Clio: Real-time Task-Driven Open-Set 3D Scene Graphs",
                "=HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting",
                "=VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting",
                "=RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics",
                "=VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation",
                "=Volumetric Environment Representation for Vision-Language Navigation",
                "=IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation",
                "=Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation",
            ],
        ),
    ]
)


SYNTHESIS_FILES = OrderedDict(
    [
        (
            "01_planning_control.md",
            [
                "Planning, control, and whole-body foundations",
                "Planning, control, simulation, and TAMP extensions",
            ],
        ),
        (
            "02_rl_il_offline.md",
            [
                "RL, IL, and policy learning foundations",
                "RL, IL, offline learning, and robot data",
            ],
        ),
        (
            "03_manipulation_contact.md",
            [
                "Manipulation, contact, tactile, and dexterity",
                "Contact-rich, deformable, force, and dexterous manipulation",
            ],
        ),
        (
            "04_vla_generalist.md",
            [
                "VLA and generalist robot policies",
                "VLA, cross-embodiment, and long-horizon planning",
            ],
        ),
        (
            "05_world_models_safety.md",
            [
                "Safety and robot world models",
                "World models, uncertainty, failure detection, and recovery",
            ],
        ),
        (
            "06_locomotion_whole_body.md",
            [
                "Locomotion, mobile manipulation, and humanoid systems",
                "Locomotion, whole-body control, mobile manipulation, and humanoids",
            ],
        ),
        (
            "07_robotics_3d_perception.md",
            [
                "Robotics-enabling 3D perception",
                "Active and embodied 3D Vision",
            ],
        ),
    ]
)


ROW_RE = re.compile(
    r"^\| (?P<year>\d{4}) \| (?P<venue>[^|]+) \| "
    r"\[(?P<title>[^]]+)\]\((?P<path>\./[^)]+/01_overview\.md)\) \| "
    r"(?P<tags>[^|]+) \| (?P<pdf>[^|]+) \|"
)
REFERENCE_TAG_RE = re.compile(
    r"robot|vla|manipulation|locomotion|slam|navigation|world model|"
    r"reinforcement learning|imitation learning|whole.body|tactile|dexter",
    re.IGNORECASE,
)

# Explicit audit decisions for 3D-heavy reference papers. These papers remain
# in the registry and are searchable, but their current contribution is
# generic reconstruction/scene rendering rather than robot state estimation,
# active perception, or closed-loop behavior. Keep this list ID-based so the
# decision survives registry title/path formatting changes.
ARCHIVE_3D_RECONSTRUCTION_IDS = frozenset(
    {
        "pr-0312",  # ReconFusion
        "pr-0386",  # Generative Gaussian Splatting
        "pr-0337",  # PartGen
        "pr-0423",  # G4Splat
        "pr-0361",  # HAD
        "pr-0431",  # WorldSplat
        "pr-0310",  # SuGaR
        "pr-0382",  # DeGauss
        "pr-0410",  # SplatFormer
        "pr-0755",  # LangSplat
        "pr-0225",  # CLIP-GS
        "pr-0776",  # Dr. Splat
        "pr-0790",  # SceneSplat
        "pr-0807",  # LightSplat
    }
)

# Explicit second-pass reclassification decisions. These papers are not pure
# render/reconstruction entries: they either provide state-estimation/world
# modeling foundations or expose a direct planning/control interface. Keep the
# decisions ID-based so they survive title/path formatting changes.
REFERENCE_RECLASSIFIED_IDS = frozenset(
    {
        "pr-0402",  # CG-SLAM: dense RGB-D tracking and mapping
        "pr-0369",  # VarSplat: uncertainty-aware RGB-D SLAM
        "pr-0463",  # Flow Equivariant World Models: action-conditioned memory
        "pr-0233",  # PhysSplat: physics simulation rather than reconstruction only
        "pr-0056",  # VGGT: generic visual-geometry foundation
        "pr-0757",  # Open3DSG: open-vocabulary scene-graph foundation
        "pr-0794",  # EmbodiedSplat: online semantic 3D perception without policy evaluation
    }
)

# State-estimation foundations intentionally retained in REFERENCE by the
# current audit rule. They are important comparison prerequisites, but are not
# part of the active long-term CORE/NEXT sequence in this repository.
REFERENCE_3D_STATE_FOUNDATION_IDS = frozenset({"pr-0554", "pr-0016"})


def parse_registry() -> list[dict[str, str]]:
    registry_text = REGISTRY.read_text()
    rows = []
    for line in registry_text.splitlines():
        match = ROW_RE.match(line)
        if match:
            row = {key: value.strip() for key, value in match.groupdict().items()}
            rows.append(row)
    declared_match = re.search(r"Total papers with folders: (\d+)", registry_text)
    if not declared_match:
        raise RuntimeError("PAPER.md does not declare its total paper count")
    declared_total = int(declared_match.group(1))
    if len(rows) != declared_total:
        raise RuntimeError(
            f"Registry declares {declared_total} papers but contains {len(rows)} table rows"
        )
    return rows


def resolve_groups(
    rows: list[dict[str, str]], groups: OrderedDict[str, list[str]]
) -> OrderedDict[str, list[dict[str, str]]]:
    resolved = OrderedDict()
    for group, queries in groups.items():
        papers = []
        for query in queries:
            if query.startswith("="):
                hits = [row for row in rows if row["title"] == query[1:]]
            else:
                hits = [row for row in rows if query.lower() in row["title"].lower()]
            if len(hits) != 1:
                titles = [row["title"] for row in hits]
                raise RuntimeError(f"Query {query!r} resolved to {len(hits)} papers: {titles}")
            papers.append(hits[0])
        resolved[group] = papers
    return resolved


def manifest_primary_tracks() -> dict[str, str | None]:
    manifest = ROOT / "work" / "sources" / "papers.json"
    if not manifest.exists():
        return {}
    items = json.loads(manifest.read_text(encoding="utf-8"))
    tracks = {}
    for item in items:
        if not item.get("folder"):
            continue
        tracks[f"./{item['folder']}/01_overview.md"] = item.get("primary_track")
        tracks[f"./{urllib.parse.quote(item['folder'])}/01_overview.md"] = item.get("primary_track")
    return tracks


def manifest_paper_ids() -> dict[str, str | None]:
    manifest = ROOT / "work" / "sources" / "papers.json"
    if not manifest.exists():
        return {}
    items = json.loads(manifest.read_text(encoding="utf-8"))
    ids = {}
    for item in items:
        if not item.get("folder"):
            continue
        value = item.get("paper_id")
        ids[f"./{item['folder']}/01_overview.md"] = value
        ids[f"./{urllib.parse.quote(item['folder'])}/01_overview.md"] = value
    return ids


def classify(rows: list[dict[str, str]]) -> tuple[dict[str, str], dict[str, str], dict[str, str | None]]:
    core_groups = resolve_groups(rows, CORE_GROUPS)
    next_groups = resolve_groups(rows, NEXT_GROUPS)
    tier_by_path: dict[str, str] = {}
    track_by_path: dict[str, str] = {}
    primary_track_by_path: dict[str, str | None] = {}
    manifest_tracks = manifest_primary_tracks()
    manifest_ids = manifest_paper_ids()
    known_manifest_ids = {paper_id for paper_id in manifest_ids.values() if paper_id}
    missing_archive_ids = sorted(ARCHIVE_3D_RECONSTRUCTION_IDS - known_manifest_ids)
    if missing_archive_ids:
        raise RuntimeError(
            "3D archive audit IDs are missing from the manifest: "
            + ", ".join(missing_archive_ids)
        )

    for tier, groups in (("CORE", core_groups), ("NEXT", next_groups)):
        for track, papers in groups.items():
            for paper in papers:
                path = paper["path"]
                if path in tier_by_path:
                    raise RuntimeError(f"Duplicate curated paper: {paper['title']}")
                tier_by_path[path] = tier
                track_by_path[path] = track
                primary_track_by_path[path] = DETAILED_TRACK_TO_PRIMARY[track]

    # Preserve established REFERENCE/ARCHIVE decisions from the generated index.
    # CORE/NEXT remain explicit in the groups above; new uncategorized papers fall
    # back to the robotics/VLA relevance rule below.
    existing_tiers: dict[str, str] = {}
    if INDEX.exists():
        with INDEX.open(newline="") as file:
            for old_row in csv.DictReader(file):
                if old_row.get("tier") in {"REFERENCE", "ARCHIVE"}:
                    existing_tiers[old_row.get("overview_path", "")] = old_row["tier"]

    for row in rows:
        path = row["path"]
        if path in tier_by_path:
            continue
        if manifest_ids.get(path) in REFERENCE_RECLASSIFIED_IDS:
            tier_by_path[path] = "REFERENCE"
            track_by_path[path] = "Curated reference"
            primary_track_by_path[path] = manifest_tracks.get(path)
            continue
        if manifest_ids.get(path) in REFERENCE_3D_STATE_FOUNDATION_IDS:
            tier_by_path[path] = "REFERENCE"
            track_by_path[path] = "Curated reference"
            primary_track_by_path[path] = manifest_tracks.get(path)
            continue
        if manifest_ids.get(path) in ARCHIVE_3D_RECONSTRUCTION_IDS:
            tier_by_path[path] = "ARCHIVE"
            track_by_path[path] = "Outside current robotics-first scope"
            primary_track_by_path[path] = manifest_tracks.get(path)
            continue
        existing_tier = existing_tiers.get(path)
        if existing_tier == "REFERENCE":
            tier_by_path[path] = "REFERENCE"
            track_by_path[path] = "Curated reference"
            primary_track_by_path[path] = manifest_tracks.get(path)
        elif existing_tier == "ARCHIVE":
            tier_by_path[path] = "ARCHIVE"
            track_by_path[path] = "Outside current robotics-first scope"
            primary_track_by_path[path] = manifest_tracks.get(path)
        elif REFERENCE_TAG_RE.search(row["tags"]):
            tier_by_path[path] = "REFERENCE"
            track_by_path[path] = "Robotics/VLA tag reference"
            primary_track_by_path[path] = manifest_tracks.get(path)
        else:
            tier_by_path[path] = "ARCHIVE"
            track_by_path[path] = "Outside current robotics-first scope"
            primary_track_by_path[path] = manifest_tracks.get(path)
    assigned_archive_ids = {
        manifest_ids.get(path)
        for path, tier in tier_by_path.items()
        if tier == "ARCHIVE"
    }
    missing_assigned_archive_ids = sorted(
        ARCHIVE_3D_RECONSTRUCTION_IDS - assigned_archive_ids
    )
    if missing_assigned_archive_ids:
        raise RuntimeError(
            "3D archive audit IDs were not assigned ARCHIVE: "
            + ", ".join(missing_assigned_archive_ids)
        )
    return tier_by_path, track_by_path, primary_track_by_path


def write_index(
    rows: list[dict[str, str]],
    tier_by_path: dict[str, str],
    track_by_path: dict[str, str],
    primary_track_by_path: dict[str, str | None],
    paper_id_by_path: dict[str, str | None],
) -> None:
    order = {"CORE": 0, "NEXT": 1, "REFERENCE": 2, "ARCHIVE": 3}
    curated_rank: dict[str, int] = {}
    rank = 0
    for groups in (resolve_groups(rows, CORE_GROUPS), resolve_groups(rows, NEXT_GROUPS)):
        for papers in groups.values():
            for paper in papers:
                curated_rank[paper["path"]] = rank
                rank += 1
    sorted_rows = sorted(
        rows,
        key=lambda row: (
            order[tier_by_path[row["path"]]],
            curated_rank.get(row["path"], 10_000),
            track_by_path[row["path"]],
            int(row["year"]),
            row["title"].lower(),
        ),
    )
    with INDEX.open("w", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(
            [
                "tier",
                "track",
                "primary_track",
                "paper_id",
                "year",
                "venue",
                "title",
                "overview_path",
                "tags",
            ]
        )
        for row in sorted_rows:
            writer.writerow(
                [
                    tier_by_path[row["path"]],
                    track_by_path[row["path"]],
                    primary_track_by_path.get(row["path"]) or "",
                    paper_id_by_path.get(row["path"]) or "",
                    row["year"],
                    row["venue"],
                    row["title"],
                    row["path"],
                    row["tags"],
                ]
            )


def plan_section(
    tier: str, groups: OrderedDict[str, list[dict[str, str]]]
) -> list[str]:
    total = sum(len(papers) for papers in groups.values())
    lines = [f"## {tier} — {total} papers", ""]
    sequence = 0
    for track, papers in groups.items():
        lines.extend([f"### {track} — {len(papers)}", ""])
        for paper in papers:
            sequence += 1
            lines.append(
                f"{sequence}. [{paper['title']}]({'.' + paper['path']}) "
                f"— {paper['year']} {paper['venue']}."
            )
        lines.append("")
    return lines


def write_plan(
    rows: list[dict[str, str]], tier_by_path: dict[str, str]
) -> None:
    core_groups = resolve_groups(rows, CORE_GROUPS)
    next_groups = resolve_groups(rows, NEXT_GROUPS)
    counts = {
        tier: sum(value == tier for value in tier_by_path.values())
        for tier in ("CORE", "NEXT", "REFERENCE", "ARCHIVE")
    }
    lines = [
        "# Long-Term Robotics Reading Plan",
        "",
        f"- Updated: {datetime.now(ZoneInfo('Asia/Seoul')).date().isoformat()} KST",
        "- Source registry: [PAPER.md](../PAPER.md)",
        "- Full tier index: [READING_TIERS.csv](./READING_TIERS.csv)",
        "- Reading tracker: [READING_STATUS.csv](./READING_STATUS.csv)",
        f"- Intensive-reading set: **{counts['CORE'] + counts['NEXT']} papers** "
        f"(CORE {counts['CORE']} + NEXT {counts['NEXT']})",
        "- Research stance: Robotics is the main axis; 3D Vision is selected when it changes robot state estimation, planning, control, or evaluation.",
        "",
        "## Default Reading Policy — Core First, Topic Independent",
        "",
        "이 문서는 연구 주제와 무관하게 동일한 기본 순서를 제공한다. 먼저 공통 foundation과 canonical formulation을 읽고, 그 뒤에 연구 질문에 맞는 전문화 논문으로 분기한다.",
        "",
        "`observation → state/world model → task & motion decision → policy/control → contact → feedback/failure recovery`",
        "",
        f"1. **CORE {counts['CORE']}편:** 아래의 CORE 순서를 공통 spine으로 사용한다. 연구 주제가 VLA, manipulation, locomotion, 3D perception 중 무엇이든 CORE를 먼저 읽는다.",
        f"2. **NEXT {counts['NEXT']}편:** CORE를 기본적으로 통과한 뒤 연구 질문과 직접 연결되는 branch를 선택한다. NEXT 내부의 track 순서는 탐색용이며 CORE보다 앞설 수 없다.",
        f"3. **REFERENCE {counts['REFERENCE']}편:** CORE/NEXT를 읽는 중 필요한 정의·baseline·benchmark가 생길 때 on-demand로 조회한다.",
        f"4. **ARCHIVE {counts['ARCHIVE']}편:** 현재 순서에는 넣지 않고 검색·역사 자료로 보존한다.",
        "",
        "### 운영 원칙",
        "",
        "- 주제별 시간 배분은 CORE를 건너뛰는 근거가 아니다. 연구 주제는 CORE 이후 NEXT의 branch 선택에만 사용한다.",
        f"- CORE의 track 제목은 taxonomy와 navigation을 위한 것이며, 논문을 골라 읽기 위한 선택지가 아니다. 기본적으로 1번부터 {counts['CORE']}번까지 진행한다.",
        "- 특정 프로젝트의 우선순위가 생겨도 canonical order를 수정하지 않고 paper note와 해당 track synthesis의 `Open Questions`에 기록한다. 별도 project overlay는 만들지 않는다.",
        "",
        "## Priority Criteria",
        "",
        "읽기 순서와 tier를 정할 때는 아래 순서를 우선하며 PDF 보유 여부는 고려하지 않는다.",
        "",
        "1. 공통 foundation 또는 후속 연구의 핵심 prerequisite인가",
        "2. 문제 formulation, state/action/control interface를 바꾸었는가",
        "3. 여러 robotics 문제에 재사용 가능한 개념적 수명이 있는가",
        "4. 실제 robot의 closed-loop decision, contact, adaptation, deployment와 연결되는가",
        "5. 기존 접근의 bottleneck과 실패 조건을 명확히 드러내는가",
        "6. evaluation protocol, metric, baseline이 비교 가능하고 재검증 가능한가",
        "7. 최신 흐름에서 기존 foundation의 한계를 검증하거나 확장하는가",
        "8. 현재 연구에서 반박·재사용·확장할 수 있는 명시적 contribution이 있는가",
        "",
    ]
    lines.extend([
        "## Tier Definitions",
        "",
        "| Tier | Papers | Use |",
        "|---|---:|---|",
        f"| CORE | {counts['CORE']} | 연구 주제와 무관한 공통 spine. 기본 순서대로 먼저 정독한다. |",
        f"| NEXT | {counts['NEXT']} | CORE 이후 연구 질문에 따라 branch를 선택한다. |",
        f"| REFERENCE | {counts['REFERENCE']} | 설계·실험 중 필요한 논문만 찾아 읽는다. 완독 목표가 아니다. |",
        f"| ARCHIVE | {counts['ARCHIVE']} | 현재 robotics-first 범위 밖의 검색·역사 자료. 삭제하지 않지만 읽기 큐에서 제외한다. |",
        "",
        "CORE와 NEXT만 장기 정독 대상이다. REFERENCE와 ARCHIVE의 개별 분류는 CSV에서 검색·필터링한다.",
        "",
        "## Completion Rule",
        "",
        "논문 하나를 완료 처리하려면 overview만 읽는 것으로 끝내지 않고 다음 네 가지를 남긴다.",
        "",
        "1. 문제 설정과 기존 접근 대비 핵심 가정",
        "2. observation/state/action/control interface",
        "3. 실험의 embodiment, task, data, metric, failure mode",
        "4. 현재 연구에 재사용할 요소와 반박하거나 확장할 지점",
        "",
        "## Canonical Execution Order",
        "",
        f"1. **CORE 1–{counts['CORE']}:** 아래 CORE 목록의 전 논문을 공통 foundation spine으로 읽는다. 각 track heading은 탐색용 분류이며, 주제에 따라 CORE 일부를 생략하지 않는다.",
        f"2. **NEXT 1–{counts['NEXT']}:** CORE 완료 후에만 연구 질문에 맞는 전문화 branch를 고른다. 같은 branch 안에서는 목록 순서와 prerequisite를 우선한다.",
        "3. **REFERENCE:** CORE/NEXT에서 생긴 구체적인 정의·baseline·benchmark 요구를 해결할 때만 추가한다.",
        "4. **Project overlays:** 기존 RP-2/I-02 계열 project overlay는 삭제 정책에 따라 active reading source로 사용하지 않는다. 필요한 구현·검증 질문은 해당 paper note와 track synthesis의 `Open Questions`에 남긴다.",
        "",
        "## Dependency-Based Reading Batches",
        "",
        "각 batch는 달력 기반 일정이 아니라 prerequisite 단위다. 한 batch 전체를 끝내야 다음으로 갈 필요는 없지만, 같은 계보에서는 왼쪽 논문을 먼저 읽는다.",
        "",
        "| Batch | Core question | Required spine | Branch after the spine | Exit artifact |",
        "|---|---|---|---|---|",
        "| A. Decision, mechanics, and feasibility | partial observability 아래 robot action의 belief, feasibility와 constraint는 어떻게 표현되는가? | POMDP → Operational Space Control → PRM/RRT → CHOMP/TrajOpt → PDDLStream | HQP / Whole-Body NMPC / contact optimization | belief/state·planner·controller별 decision variable과 guarantee 표 |",
        "| B. Learning objectives and data | policy가 expert, reward, value와 logged data에서 무엇을 학습하는가? | DAgger/GPS/GAIL → TRPO/PPO/SAC → RoboMimic → IBC/IQL | CQL/MOPO/TD3+BC, RLBench, MimicGen/DROID | objective × data-support × interaction 비교 표 |",
        "| C. Generative action policies | multimodal continuous action을 어떤 생성 과정으로 나타내는가? | DDPM / Flow Matching → Diffusion Policy → π0 | Diffusion-EDFs, Reactive Diffusion Policy, FAST | sampling step·chunk·latency·feedback 비교 표 |",
        "| D. Generalist VLA and scaling | semantic prior와 heterogeneous robot data가 action으로 어떻게 연결되는가? | CLIP/CLIPort/PaLM-E → RT-1/RT-2 → Open X-Embodiment → Octo/OpenVLA | OpenVLA-OFT, π0/π0.5, memory/planning VLA | data × embodiment × action interface 비교 표 |",
        "| E. Contact, safety, and recovery | 접촉 변화와 실패를 얼마나 빨리 감지하고 수정하는가? | contact/grasp foundations → tactile dynamics/control → CBF/Recovery RL → FAIL-Detect/SAFE | ForceVLA2, WorldGym/WMPO | perturbation·force·intervention·recovery protocol |",
        "| F. Embodiment specialization | 동일 학습 원리가 legged, humanoid와 mobile manipulation에서 무엇이 달라지는가? | RMA → perceptive locomotion/parkour → HumanoidBench/OmniH2O/Mobile ALOHA | LangWBC, ASAP, HWC-Loco, VIRAL | dynamics/contact/whole-body coupling 비교 표 |",
        "| G. Action-relevant 3D | 더 좋은 geometry가 실제 robot decision을 언제 개선하는가? | PointNet → DROID-SLAM/3DGS → ConceptFusion/RVT/DUSt3R | VGGT/SUGAR, active 3D, PointVLA/Any3D-VLA | representation 고정 ablation과 downstream metric |",
        "",
        "Batch exit artifact를 채우기 전에는 해당 계보를 `SYNTHESIZED`로 올리지 않는다. Batch는 CORE-first 기본 순서를 보완하는 비교 단위이며, 연구 주제가 다르다는 이유로 CORE보다 앞세우지 않는다.",
        "",
        "## Research Lenses Across Tracks",
        "",
        "- Robot learning을 behavior cloning으로 한정하지 않고 offline-to-online improvement, reward/value learning, failure/suboptimal data 활용까지 본다.",
        "- Contact를 예외가 아니라 state, dynamics, constraint, feedback signal로 다룬다.",
        "- Locomotion과 manipulation의 결합, balance와 task interaction의 공동 제어를 본다.",
        "- Safety를 constraint, uncertainty, monitoring, intervention, recovery의 여러 시간 척도로 나눈다.",
        "- Geometry가 learned policy 안에서 equivariance, 3D state, spatial memory, collision/contact structure로 어떤 역할을 하는지 본다.",
        "- Architecture보다 data coverage, quality, curation, embodiment diversity와 scaling law를 함께 비교한다.",
        "- Generative action model의 inference latency와 실제 closed-loop control frequency를 확인한다.",
        "- Tabletop success rate를 넘어 long horizon, real-world disturbances, sensor degradation, compromised contact, recovery를 평가한다.",
        "",
    ])
    lines.extend(plan_section("CORE", core_groups))
    lines.extend([
        f"CORE {counts['CORE']}편을 기본적으로 모두 읽은 뒤에 NEXT branch를 선택한다. 아래 NEXT track은 주제별 선택지이지 CORE를 대체하는 우선순위가 아니다.",
        "",
    ])
    lines.extend(plan_section("NEXT", next_groups))
    lines.extend(
        [
            "## REFERENCE — On-Demand Reading",
            "",
            "CORE/NEXT에는 포함되지 않지만 중요한 foundation, baseline, representation, dataset, benchmark 또는 Robotics/VLA 관련 논문이다. 연구 설계 중 필요할 때 찾아 읽으며 완독 목표로 삼지 않는다.",
            "",
            "## ARCHIVE — Search Only",
            "",
            "현재 robotics-first 방향과 직접 연결되지 않는 논문이다. 향후 연구축이 바뀌거나 특정 3D/VLM 배경이 필요할 때 다시 승격할 수 있으며, 레지스트리와 로컬 노트는 그대로 보존한다.",
            "",
        ]
    )
    PLAN.write_text("\n".join(lines))


def write_status(
    rows: list[dict[str, str]],
    tier_by_path: dict[str, str],
    track_by_path: dict[str, str],
    primary_track_by_path: dict[str, str | None],
    paper_id_by_path: dict[str, str | None],
) -> None:
    """Create/update the intensive-reading tracker while preserving user-entered fields."""
    fieldnames = [
        "tier",
        "track",
        "primary_track",
        "paper_id",
        "sequence",
        "status",
        "evidence_level",
        "year",
        "venue",
        "title",
        "overview_path",
        "started_on",
        "completed_on",
        "problem_and_assumptions",
        "observation_state_action_control",
        "embodiment_task_data_metrics",
        "failure_modes",
        "research_relevance",
        "next_action",
        "personal_notes",
    ]
    preserved: dict[str, dict[str, str]] = {}
    if STATUS.exists():
        with STATUS.open(newline="") as file:
            for old_row in csv.DictReader(file):
                preserved[old_row.get("overview_path", "")] = old_row

    curated = [
        row for row in rows if tier_by_path[row["path"]] in {"CORE", "NEXT"}
    ]
    tier_order = {"CORE": 0, "NEXT": 1}
    track_order = {
        track: index
        for index, track in enumerate([*CORE_GROUPS.keys(), *NEXT_GROUPS.keys()])
    }
    curated_rank: dict[str, int] = {}
    rank = 0
    for groups in (resolve_groups(rows, CORE_GROUPS), resolve_groups(rows, NEXT_GROUPS)):
        for papers in groups.values():
            for paper in papers:
                curated_rank[paper["path"]] = rank
                rank += 1
    curated.sort(
        key=lambda row: (
            tier_order[tier_by_path[row["path"]]],
            track_order[track_by_path[row["path"]]],
            curated_rank[row["path"]],
        )
    )

    sequence_by_tier = {"CORE": 0, "NEXT": 0}
    output_rows = []
    for row in curated:
        path = row["path"]
        tier = tier_by_path[path]
        sequence_by_tier[tier] += 1
        old = preserved.get(path, {})
        overview = ROOT / path.removeprefix("./")
        evidence_match = re.search(
            r"Evidence maturity: `([^`]+)`", overview.read_text(encoding="utf-8")
        )
        note_evidence = evidence_match.group(1) if evidence_match else ""
        if note_evidence not in {
            "CURATION_ONLY",
            "ABSTRACT_CHECKED",
            "FULL_TEXT_CHECKED",
            "EXPERIMENT_CHECKED",
        }:
            note_evidence = ""
        evidence = old.get("evidence_level") or note_evidence or "CURATION_ONLY"
        if (
            old.get("status", "UNREAD") == "UNREAD"
            and evidence == "CURATION_ONLY"
            and note_evidence in {"ABSTRACT_CHECKED", "FULL_TEXT_CHECKED", "EXPERIMENT_CHECKED"}
        ):
            evidence = note_evidence
        output = {field: old.get(field, "") for field in fieldnames}
        output.update(
            {
                "tier": tier,
                "track": track_by_path[path],
                "primary_track": primary_track_by_path.get(path) or "",
                "paper_id": paper_id_by_path.get(path) or "",
                "sequence": str(sequence_by_tier[tier]),
                "status": old.get("status") or "UNREAD",
                "evidence_level": evidence,
                "year": row["year"],
                "venue": row["venue"],
                "title": row["title"],
                "overview_path": path,
            }
        )
        output_rows.append(output)

    with STATUS.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)


def write_synthesis_queues() -> None:
    """Refresh generated paper queues without touching hand-written synthesis."""
    with STATUS.open(newline="") as file:
        status_rows = list(csv.DictReader(file))
    rows_by_track: dict[str, list[dict[str, str]]] = {}
    for row in status_rows:
        rows_by_track.setdefault(row["track"], []).append(row)

    start_marker = "<!-- READING_QUEUE:START -->"
    end_marker = "<!-- READING_QUEUE:END -->"
    for filename, tracks in SYNTHESIS_FILES.items():
        document = SYNTHESIS / filename
        text = document.read_text()
        if start_marker not in text or end_marker not in text:
            raise RuntimeError(f"Missing generated queue markers in {document}")
        queue = [start_marker, "", "## Assigned Reading Queue", ""]
        for track in tracks:
            papers = rows_by_track.get(track, [])
            queue.extend(
                [
                    f"### {track} — {len(papers)}",
                    "",
                    "| Tier | Paper | Year / Venue | Status | Evidence |",
                    "|---|---|---|---|---|",
                ]
            )
            for paper in papers:
                relative_path = "." + paper["overview_path"]
                queue.append(
                    f"| {paper['tier']} | [{paper['title']}]({relative_path}) | "
                    f"{paper['year']} / {paper['venue']} | `{paper['status']}` | `{paper['evidence_level']}` |"
                )
            queue.append("")
        queue.append(end_marker)
        prefix, remainder = text.split(start_marker, 1)
        _, suffix = remainder.split(end_marker, 1)
        document.write_text(prefix + "\n".join(queue) + suffix)


def main() -> None:
    rows = parse_registry()
    tier_by_path, track_by_path, primary_track_by_path = classify(rows)
    paper_id_by_path = manifest_paper_ids()
    write_status(rows, tier_by_path, track_by_path, primary_track_by_path, paper_id_by_path)
    write_index(rows, tier_by_path, track_by_path, primary_track_by_path, paper_id_by_path)
    write_plan(rows, tier_by_path)
    write_synthesis_queues()
    counts = {
        tier: sum(value == tier for value in tier_by_path.values())
        for tier in ("CORE", "NEXT", "REFERENCE", "ARCHIVE")
    }
    print(counts)


if __name__ == "__main__":
    main()
