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


# Project-specific reading order for the I-02/RP-2 failure-to-recovery study.
# This is not a fourth tier: it is a dependency-based view over CORE/NEXT/
# REFERENCE papers and is intentionally broader than the 100–150 paper
# intensive-reading operating guide.
RP2_PRIORITY_GROUPS = OrderedDict(
    [
        (
            "P0 — Concept prerequisites",
            [
                ("=Planning and Acting in Partially Observable Stochastic Domains", "MDP/POMDP, belief state, finite-memory policy"),
                ("A Reduction of Imitation Learning", "covariate shift and learner-induced failure states"),
                ("Proximal Policy Optimization Algorithms", "policy optimization and trust-region intuition"),
                ("Trust Region Policy Optimization", "stable constrained policy updates"),
                ("Recovery RL:", "task policy, recovery policy, safety critic"),
                ("Failure Prediction with Statistical Guarantees", "runtime monitoring and statistical failure prediction"),
                ("Control Barrier Function Based", "safe set, constraint violation, irreversible event"),
                ("Robots That Ask For Help", "uncertainty-aligned human escalation"),
                ("PDDLStream:", "symbolic–continuous task-and-motion replanning"),
                ("Relay Policy Learning", "long-horizon skill decomposition and relaying"),
            ],
        ),
        (
            "P1 — Direct detector, recovery, and selector baselines",
            [
                ("Can We Detect Failures Without Failure Data?", "uncertainty-aware detector without failure-data dependence"),
                ("SAFE: Multitask", "VLA latent failure score and conformal alert threshold"),
                ("FLARE:", "binary Retry/Reset recovery dispatcher"),
                ("Can VLMs Diagnose and Recover", "fault taxonomy, diagnosis, rollback recovery"),
                ("Temporal Difference Calibration", "sequential success-confidence calibration"),
                ("AHA: A Vision-Language-Model", "VLM failure detection and reasoning alternative"),
                ("Counterfactual VLA", "self-reflection and test-time recovery comparison"),
                ("SafeVLA:", "constrained VLA safety alignment"),
            ],
        ),
        (
            "P2 — Benchmark and metric semantics",
            [
                ("Benchmarking Knowledge Transfer for Lifelong Robot Learning", "LIBERO fixed states and goal predicates"),
                ("CALVIN:", "language-conditioned long-horizon sequence evaluation"),
                ("AtomicVLA:", "termination semantics and post-failure continuation"),
                ("FurnitureBench:", "phase/skill progress beyond final success"),
                ("LIBERO-Safety:", "physical and semantic safety perturbations"),
                ("VLA-Arena:", "safety, distractor, extrapolation, long-horizon stress axes"),
                ("BEHAVIOR-1K:", "large-scale embodied long-horizon evaluation context"),
                ("RLBench:", "task suite and simulator design comparison"),
            ],
        ),
        (
            "P3 — Frozen VLA and implementation branch",
            [
                ("OpenVLA", "recommended open frozen policy base for the first pilot"),
                ("Octo: An Open", "generalist policy and action conditioning alternative"),
                ("RT-1:", "robot policy/action-token lineage"),
                ("RT-2:", "language-to-action VLA lineage"),
                ("π0: A Vision-Language-Action Flow Model", "current flow-based VLA alternative"),
                ("π0.5", "open-world VLA extension"),
                ("Decision Transformer:", "trajectory-conditioned sequence modeling"),
                ("Implicit Q-Learning", "chosen-action or partial-feedback sensitivity; not the primary all-option estimator"),
                ("Conservative Q-Learning", "support-mismatch baseline for later policy reuse; not the primary all-option estimator"),
                ("Implicit Behavioral Cloning", "multimodal behavior-cloning alternative"),
                ("Q-Transformer:", "autoregressive action-value modeling extension"),
            ],
        ),
        (
            "P4 — Optional extensions and transfer checks",
            [
                ("Long-VLA:", "long-horizon VLA context"),
                ("PALM:", "progress-aware policy state"),
                ("Learning to Be Uncertain", "horizon-calibrated uncertainty context"),
                ("WorldGym", "world-model policy evaluation alternative"),
                ("WMPO", "imagined policy improvement and calibration context"),
                ("Memory Retrieval in Visuomotor Policies", "memory/retrieval effects on long-horizon execution"),
                ("Inner Monologue:", "language-mediated replanning and feedback"),
                ("SayPlan", "scene-graph task planning extension"),
                ("MimicPlay:", "long-horizon imitation and play data"),
                ("MimicGen", "demonstration augmentation if recovery data is scarce"),
                ("Data Scaling Laws", "data coverage and failure-data curation context"),
            ],
        ),
    ]
)


# These fast-moving 2026 papers stay outside the registry-backed tier system
# until their metadata admission is audited. They are still mandatory RP-2
# reading because they directly constrain the project's novelty boundary.
RP2_EXTERNAL_COLLISION_READING = [
    (
        "Learning Robust Execution with Agentic RL",
        "https://arxiv.org/html/2607.13818v1",
        "PREPRINT / FULL-TEXT-CHECKED",
        "strongest collision: a history-conditioned Execute/Retry/Repair/Reset manager trained with PPO on LIBERO",
    ),
    (
        "ActFovea",
        "https://arxiv.org/abs/2607.29169",
        "PREPRINT / FULL-TEXT-CHECKED",
        "verified observation recovery, bounded safe failure, and short-horizon/action-smoothing controls",
    ),
    (
        "ProbeAct",
        "https://arxiv.org/abs/2606.09740",
        "PREPRINT / FULL-TEXT-CHECKED",
        "hidden-state probing, a kinematic failure state machine, and training-free CBF correction",
    ),
    (
        "ViFailback",
        "https://openaccess.thecvf.com/content/CVPR2026/html/Zeng_Diagnose_Correct_and_Learn_from_Manipulation_Failures_via_Visual_Symbols_CVPR_2026_paper.html",
        "CVPR 2026 / FULL-TEXT-CHECKED",
        "diagnosis plus visual/text correction with real failure data",
    ),
    (
        "AgentChord",
        "https://roboticsconference.org/program/papers/180/",
        "RSS 2026 / SOURCE-VERIFIED",
        "precompiled recovery branches and low-latency orchestration",
    ),
    (
        "When to Act, Ask, or Learn",
        "https://roboticsconference.org/program/papers/142/",
        "RSS 2026 / SOURCE-VERIFIED",
        "calibrated act/clarify/intervene selection and selective autonomy",
    ),
    (
        "See, Plan, Rewind",
        "https://arxiv.org/abs/2603.09292",
        "PREPRINT / SOURCE-VERIFIED",
        "progress-aware subgoal rewind",
    ),
    (
        "FAR",
        "https://arxiv.org/abs/2607.01111",
        "PREPRINT / SOURCE-VERIFIED",
        "retry perturbation and failure-preference adaptation",
    ),
    (
        "Imagining Recovery / CoRe",
        "https://arxiv.org/abs/2608.14822",
        "PREPRINT / FULL-TEXT-CHECKED",
        "imagined continuation and state realignment; a different estimand from cloned same-onset branch outcomes",
    ),
    (
        "VLCP",
        "https://arxiv.org/abs/2608.16978",
        "PREPRINT / SOURCE-VERIFIED",
        "control-code abstraction and closed-loop replanning",
    ),
]


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
            ],
        ),
        (
            "VLA, cross-embodiment, and long-horizon planning",
            [
                "=A Generalist Agent",
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


def resolve_priority_groups(
    rows: list[dict[str, str]], groups: OrderedDict[str, list[tuple[str, str]]]
) -> OrderedDict[str, list[tuple[dict[str, str], str]]]:
    resolved: OrderedDict[str, list[tuple[dict[str, str], str]]] = OrderedDict()
    for group, entries in groups.items():
        papers: list[tuple[dict[str, str], str]] = []
        for query, rationale in entries:
            if query.startswith("="):
                hits = [row for row in rows if row["title"] == query[1:]]
            else:
                hits = [row for row in rows if query.lower() in row["title"].lower()]
            if len(hits) != 1:
                titles = [row["title"] for row in hits]
                raise RuntimeError(f"RP-2 query {query!r} resolved to {len(hits)} papers: {titles}")
            papers.append((hits[0], rationale))
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
    for track, papers in groups.items():
        lines.extend([f"### {track} — {len(papers)}", ""])
        for index, paper in enumerate(papers, 1):
            lines.append(
                f"{index}. [{paper['title']}]({'.' + paper['path']}) "
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
        "## How to Use This Plan",
        "",
        "이 문서는 별도 priority 목록과 robotics roadmap을 합친 유일한 장기 reading roadmap이다. 논문은 다음 폐루프에서 맡는 역할을 기준으로 읽는다.",
        "",
        "`observation → state/world model → task & motion decision → policy/control → contact → feedback/failure recovery`",
        "",
        "- **Robotics:** planning, control, learning, physical interaction, deployment가 주 연구축이다.",
        "- **VLA:** language 이해 자체보다 action representation, robot data, embodiment transfer, latency, memory, feedback, safety를 본다.",
        "- **3D Vision:** 독립 benchmark보다 manipulation, navigation, SLAM, spatial memory, active perception에 주는 downstream 효과를 본다.",
        "- **Humanoid:** 별도 축으로 분리하지 않고 locomotion, whole-body control, imitation, loco-manipulation 안에서 읽는다.",
        "",
        "### Default reading budget",
        "",
        "| Research track | Share | Focus |",
        "|---|---:|---|",
        "| Robot learning and control | 25% | RL/IL/offline RL, planning, optimal control, sim-to-real |",
        "| Manipulation and physical interaction | 25% | grasping, contact, tactile/force, dexterity, deformables, assembly |",
        "| VLA, world models, safety, and long horizon | 20% | generalist policies, predictive models, uncertainty, recovery, replanning |",
        "| Locomotion, whole-body, and mobile robotics | 15% | legged/humanoid control, loco-manipulation, navigation |",
        "| Robotics-enabling 3D Vision | 15% | geometry, SLAM, active perception, semantic/spatial memory |",
        "",
        "이 비율은 registry 구성 비율이 아니라 장기 읽기·비교·재현 시간의 기본값이다. 연구 주제가 정해지면 해당 track을 50% 이상으로 높일 수 있다.",
        "",
        "## Priority Criteria",
        "",
        "위에서 아래 순서로 판단하되 PDF 보유 여부는 고려하지 않는다.",
        "",
        "1. 실제 robot task와 closed-loop action/control에 직접 연결되는가",
        "2. 해당 분야의 foundation 또는 후속 연구의 핵심 prerequisite인가",
        "3. 해결하려는 연구 공백과 기존 접근의 한계가 명확한가",
        "4. contact, partial observability, uncertainty, safety, failure recovery를 실질적으로 다루는가",
        "5. real robot 또는 설득력 있는 physics evaluation이 있는가",
        "6. 평가 protocol, metric, baseline이 명확하고 재검증 가능한가",
        "7. 구현 난이도와 데이터·코드·하드웨어 접근성이 현실적인가",
        "8. embodiment, task, object, environment generalization을 검증하는가",
        "9. 최신 trend 중 후속 연구가 이어지는 핵심 flow를 형성하는가",
        "10. 현재 연구에서 반박·재사용·확장 가능한 contribution이 있는가",
        "",
        "## RP-2 / I-02 Priority Reading Sequence",
        "",
        "아래 순서는 전체 registry tier가 아니라 `Same-Onset Failure Recovery Arbitration` 연구를 시작할 때의 project-specific dependency다. broad high-level recovery selector는 Agentic RL이 이미 직접 다루므로, RP-2는 same-onset all-option supervision, vector budget, best-fixed regret가 실제로 필요한지부터 반증한다. 15편 hard cap을 두지 않으며, 각 논문은 event schema, detector, option contract, budget, estimator, benchmark 중 어느 결정을 바꾸는지 기록한다.",
        "",
    ]
    for priority, entries in resolve_priority_groups(rows, RP2_PRIORITY_GROUPS).items():
        lines.extend([f"### {priority} — {len(entries)} papers", ""])
        for index, (paper, rationale) in enumerate(entries, 1):
            lines.append(
                f"{index}. [{paper['title']}]({'.' + paper['path']}) "
                f"— {paper['year']} {paper['venue']}; {rationale}."
            )
        lines.append("")
        if priority.startswith("P1 —"):
            lines.extend([
                f"#### P1.5 — 2026 direct novelty-collision audit — {len(RP2_EXTERNAL_COLLISION_READING)} papers",
                "",
                "아래 자료는 registry tier와 별개인 필수 frontier audit다. 특히 Agentic RL을 재현 가능한 최우선 비교군으로 두고, `paper → policy-visible history → option set → decision timing → budget → supervision → outcome metric` 계약을 표로 남긴다.",
                "",
            ])
            for index, (title, url, status, rationale) in enumerate(RP2_EXTERNAL_COLLISION_READING, 1):
                lines.append(f"{index}. [{title}]({url}) — `{status}`; {rationale}.")
            lines.extend([
                "",
                "Implementation companion: [SAFE official code](https://github.com/vla-safe/SAFE), [SAFE OpenVLA fork](https://github.com/vla-safe/openvla), and the pinned manifests in [RP-2](./projects/RP-2_FAILURE_RECOVERY.md) define the detector/base-policy reproduction contract.",
                "",
            ])
    lines.extend([
        "## Tier Definitions",
        "",
        "| Tier | Papers | Use |",
        "|---|---:|---|",
        f"| CORE | {counts['CORE']} | 공통 기반과 주력 연구축. 순서대로 정독하고 비교 노트를 남긴다. |",
        f"| NEXT | {counts['NEXT']} | CORE 이후 트랙별로 정독한다. 연구 주제에 따라 내부 순서는 바꿀 수 있다. |",
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
        "## Long-Term Reading Sequence",
        "",
        "1. **Decision, mechanics, and control:** POMDP belief-state planning → Operational Space Control → PRM/RRT → CHOMP/TrajOpt → PDDLStream → whole-body/force control.",
        "2. **Policy learning:** DAgger/GAIL → RoboMimic/RLBench → TRPO/PPO/SAC → offline RL → DDPM/Flow Matching → Diffusion Policy and scalable robot data.",
        "3. **Physical interaction:** contact mechanics and grasping → tactile/force feedback → dexterous, deformable, tool, assembly tasks.",
        "4. **Generalist policies:** CLIP/PaLM-E/CLIPort → RT-1/RT-2 → Open X-Embodiment → Octo/OpenVLA/π0 → FAST/OpenVLA-OFT/π0.5.",
        "5. **Deployment:** World Models/Dreamer → DayDreamer/TD-MPC2 → FAIL-Detect/SAFE → safety filter and recovery.",
        "6. **Embodiment specialization:** locomotion, whole-body, mobile manipulation을 선택하고 필요한 3D perception을 역으로 연결한다.",
        "7. **Active spatial intelligence:** PointNet/3DGS/DUSt3R/VGGT → SLAM/semantic mapping → articulation, active perception, 3D-aware VLA.",
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
        "Batch exit artifact를 채우기 전에는 해당 계보를 `SYNTHESIZED`로 올리지 않는다. 세부 paper sequence는 아래 CORE/NEXT 목록의 순서를 따른다.",
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
