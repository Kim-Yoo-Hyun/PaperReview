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
STATUS_HISTORY = RESEARCH / "READING_STATUS_HISTORY.csv"
SYNTHESIS = ROOT / "synthesis"


CORE_GROUPS = OrderedDict(
    [
        (
            "RL, IL, and policy learning foundations",
            [
                "=Learning to Predict by the Methods of Temporal Differences",
                "=Policy Gradient Methods for Reinforcement Learning with Function Approximation",
                "=Proximal Policy Optimization Algorithms",
                "=Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor",
                "=Offline Reinforcement Learning with Implicit Q-Learning",
                "=Conservative Q-Learning for Offline Reinforcement Learning",
                "=A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning",
                "=What Matters in Learning from Offline Human Demonstrations for Robot Manipulation",
                "=Denoising Diffusion Probabilistic Models",
                "=Flow Matching for Generative Modeling",
                "=Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
                "=Diffusion Policy Policy Optimization",
                "=Flow Q-Learning",
                "=Efficient Online Reinforcement Learning with Offline Data",
                "=SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning",
                "=Precise and dexterous robotic manipulation via human-in-the-loop reinforcement learning",
                "=RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning",
                "=DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset",
                "=LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning",
                "=Habitat: A Platform for Embodied AI Research",
            ],
        ),
        (
            "VLA and generalist robot policies",
            [
                "=Learning Transferable Visual Models From Natural Language Supervision",
                "=RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control",
                "=Open X-Embodiment: Robotic Learning Datasets and RT-X Models",
                "=Octo: An Open-Source Generalist Robot Policy",
                "=OpenVLA: An Open-Source Vision-Language-Action Model",
                "=Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
                "=π0: A Vision-Language-Action Flow Model for General Robot Control",
                "=FAST: Efficient Action Tokenization for Vision-Language-Action Models",
                "=π0.5: a Vision-Language-Action Model with Open-World Generalization",
                "=ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy",
                "=Do As I Can, Not As I Say: Grounding Language in Robotic Affordances",
                "=NaVILA: Legged Robot Vision-Language-Action Model for Navigation",
                "=CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks",
            ],
        ),
        (
            "Manipulation, contact, tactile, and dexterity",
            [
                "=Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware",
                "=3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations",
            ],
        ),
        (
            "Planning, control, and whole-body foundations",
            [
                "=Planning and Acting in Partially Observable Stochastic Domains",
                "=Impedance Control: An Approach to Manipulation: Part I—Theory",
                "=MuJoCo: A Physics Engine for Model-Based Control",
                "=NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration",
            ],
        ),
        (
            "Robotics-enabling 3D perception",
            [
                "=ConceptFusion: Open-set Multimodal 3D Mapping",
                "=RVT: Robotic View Transformer for 3D Object Manipulation",
                "=VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation",
                "=Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments",
            ],
        ),
        (
            "Locomotion, mobile manipulation, and humanoid systems",
            [
                "=ViNT: A Foundation Model for Visual Navigation",
                "=Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation",
            ],
        ),
        (
            "Safety and robot world models",
            [
                "=TD-MPC2: Scalable, Robust World Models for Continuous Control",
                "=Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones",
            ],
        ),
    ]
)


NEXT_GROUPS = OrderedDict(
    [
        (
            "RL, IL, offline learning, and robot data",
            [
                "=Reinforcement Learning with Action Chunking",
                "=Decoupled Q-Chunking",
                "=Steering Your Diffusion Policy with Latent Space Reinforcement Learning",
                "=Performant robotic manipulation with real-world reinforcement learning",
                "=OGBench: Benchmarking Offline Goal-Conditioned RL",
                "=USER: A Unified and Extensible System for Online Real-World Policy Learning in Embodied AI",
                "=Trust Region Policy Optimization",
                "=Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World",
                "=Implicit Behavioral Cloning",
                "=Decision Transformer: Reinforcement Learning via Sequence Modeling",
                "=Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions",
                "=Behavior Transformers: Cloning k modes with one stone",
                "=R3M: A Universal Visual Representation for Robot Manipulation",
                "=Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?",
                "=Maximum a Posteriori Policy Optimisation",
                "=MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale",
                "=Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning",
                "=Eureka: Human-Level Reward Design via Coding Large Language Models",
                "=DrEureka: Language Model Guided Sim-To-Real Transfer",
                "=Continuous Control with Deep Reinforcement Learning",
                "=Addressing Function Approximation Error in Actor-Critic Methods",
                "=Hindsight Experience Replay",
                "=Constrained Policy Optimization",
                "=MOPO: Model-based Offline Policy Optimization",
                "=A Minimalist Approach to Offline Reinforcement Learning",
                "=Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations",
                "=Learning Latent Plans from Play",
                "=Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning",
                "=RLBench: The Robot Learning Benchmark & Learning Environment",
                "=MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations",
                "=Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots",
                "=Robot Fine-Tuning Made Easy: Pre-Training Rewards and Policies for Autonomous Real-World Reinforcement Learning",
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
                "=MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation",
                "=Diffusion Meets DAgger: Supercharging Eye-in-hand Imitation Learning",
                "=Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation",
                "=Any-point Trajectory Modeling for Policy Learning",
                "=Evaluating Real-World Robot Manipulation Policies in Simulation",
                "=MimicPlay: Long-Horizon Imitation Learning by Watching Human Play",
                "=Test-Time Adaptation for Online Vision-Language Navigation with Feedback-based Reinforcement Learning",
                "=Studying the Interplay Between the Actor and Critic Representations in Reinforcement Learning",
                "=SPRINT: Scalable Policy Pre-Training via Language Instruction Relabeling",
                "=Autonomous Improvement of Instruction Following Skills via Foundation Models",
                "=ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning",
            ],
        ),
        (
            "VLA, cross-embodiment, and long-horizon planning",
            [
                "=What Can RL Bring to VLA Generalization? An Empirical Study",
                "=SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
                "=RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models",
                "=A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots",
                "=Learning from Hindsight for VLA Reinforcement Learning",
                "=CAST: Counterfactual Labels Improve Instruction Following in Vision-Language-Action Models",
                "=NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation",
                "=StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling",
                "=SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation",
                "=DyGRO-VLA: Cross-Task Scaling of Vision–Language–Action Models via Dynamic Grouped Residual Optimization",
                "=CLIPort: What and Where Pathways for Robotic Manipulation",
                "=PaLM-E: An Embodied Multimodal Language Model",
                "=RT-1: Robotics Transformer for Real-World Control at Scale",
                "=VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models",
                "=A Generalist Agent",
                "=AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents",
                "=RT-H: Action Hierarchies Using Language",
                "=Gemini Robotics: Bringing AI into the Physical World",
                "=NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots",
                "=BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning",
                "=Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation",
                "=VIMA: Robot Manipulation with Multimodal Prompts",
                "=Inner Monologue: Embodied Reasoning through Planning with Language Models",
                "=SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning",
                "=XSkill: Cross Embodiment Skill Discovery",
                "=Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers",
                "=AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots",
                "=PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation",
                "=ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation",
                "=Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action",
                "=Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning",
                "=Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds",
                "=MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning",
                "=AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention",
                "=VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models",
                "=SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models",
                "=From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors",
                "=Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks",
                "=Learning to Act Anywhere with Task-centric Latent Actions",
                "=CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision",
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
            "Contact-rich, deformable, force, and dexterous manipulation",
            [
                "=Tac2Real: Reliable and GPU Visuotactile Simulation for Online Reinforcement Learning and Zero-Shot Real-World Deployment",
                "=GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping",
                "=Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes",
                "=Factory: Fast Contact for Robotic Assembly",
                "=RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing",
                "=Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation",
                "=Universal Manipulation Policy Network for Articulated Objects",
                "=Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation",
                "=GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping",
                "=ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation",
                "=Gaussian Splatting Visual MPC for Granular Media Manipulation",
                "=Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects",
                "=DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation",
                "=DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality",
                "=Control-Limited Differential Dynamic Programming",
                "=In-Hand Manipulation via Motion Cones",
                "=Towards Tight Convex Relaxations for Contact-Rich Manipulation",
                "=Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization",
                "=Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation",
                "=SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation",
                "=DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools",
                "=Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation",
                "=Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation",
                "=IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality",
                "=Binding Touch to Everything: Learning Unified Multimodal Tactile Representations",
                "=DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo",
                "=G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation",
                "=Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation",
                "=AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models",
                "=ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation",
                "=Dexterous World Models",
                "=EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation",
                "=Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language",
                "=TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment",
                "=DexterityGen: Foundation Controller for Unprecedented Dexterity",
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
                "=Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching",
            ],
        ),
        (
            "Planning, control, simulation, and TAMP extensions",
            [
                "=NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance",
                "=Rapidly-Exploring Random Trees: A New Tool for Path Planning",
                "=Information Theoretic MPC for Model-Based Reinforcement Learning",
                "=PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning",
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
            ],
        ),
        (
            "Active and embodied 3D Vision",
            [
                "=LoGoPlanner: Localization Grounded Navigation Policy with Metric-aware Visual Geometry",
                "=Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments",
                "=PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation",
                "=DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras",
                "=Where2Act: From Pixels to Actions for Articulated 3D Objects",
                "=FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects",
                "=Ditto: Building Digital Twins of Articulated Objects from Interaction",
                "=Visual Language Maps for Robot Navigation",
                "=SUGAR: Pre-training 3D Visual Representations for Robotics",
                "=Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps",
                "=RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics",
                "=PointVLA: Injecting the 3D World into Vision-Language-Action Models",
                "=Vysics: Object Reconstruction Under Occlusion by Fusing Vision and Contact-Rich Physics",
                "=Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery",
                "=Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects",
                "=Clio: Real-time Task-Driven Open-Set 3D Scene Graphs",
                "=HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting",
                "=VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting",
                "=RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics",
                "=Volumetric Environment Representation for Vision-Language Navigation",
                "=IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation",
                "=Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation",
            ],
        ),
        (
            "Locomotion, whole-body control, mobile manipulation, and humanoids",
            [
                "=RMA: Rapid Motor Adaptation for Legged Robots",
                "=RoboPanoptes: The All-Seeing Robot with Whole-body Dexterity",
                "=Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics",
                "=Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation",
                "=Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation",
                "=Demonstrating MOSART: Opening Articulated Structures in the Real World",
                "=HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit",
                "=SPIN: Simultaneous Perception, Interaction and Navigation",
                "=GOAT: GO to Any Thing",
                "=Habitat 2.0: Training Home Assistants to Rearrange their Habitat",
            ],
        ),
        (
            "World models, uncertainty, failure detection, and recovery",
            [
                "=VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model",
                "=Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models",
                "=Self-Improving Robot Policy with Compositional World Model",
                "=PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation",
                "=OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation",
                "=Recurrent World Models Facilitate Policy Evolution",
                "=DayDreamer: World Models for Physical Robot Learning",
                "=Control Barrier Function Based Quadratic Programs for Safety Critical Systems",
                "=DreamGen: Unlocking Generalization in Robot Learning through Video World Models",
                "=DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos",
                "=Learning Latent Dynamics for Planning from Pixels",
                "=Dream to Control: Learning Behaviors by Latent Imagination",
                "=Mastering diverse control tasks through world models",
                "=PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation",
                "=Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets",
                "=FlowDreamer: A RGB-D World Model With Flow-Based Motion Representations for Robot Manipulation",
                "=Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies",
                "=SAFE: Multitask Failure Detection for Vision-Language-Action Models",
                "=WorldGym: World Model as An Environment for Policy Evaluation",
                "=WMPO: World Model-based Policy Optimization for Vision-Language-Action Models",
                "=FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation",
                "=Can VLMs Diagnose and Recover from VLA Manipulation Faults?",
                "=Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models",
                "=Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control",
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
    ]
)


# Incremental admission review: 2026-10-21; existing membership is preserved.
NEXT_GROUPS["VLA, cross-embodiment, and long-horizon planning"].extend([
    "=DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation",
    "=How Should Vision-Language-Action Models Use Proprioceptive State?",
    "=Self-Adaptive VLA for Robust Robot Deployment",
    "=ReViP: Mitigating False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance",
    "=CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts",
    "=CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts",
    "=When would Vision-Proprioception Policies Fail in Robotic Manipulation?"
])
NEXT_GROUPS["Contact-rich, deformable, force, and dexterous manipulation"].extend([
    "=Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models"
])
NEXT_GROUPS["Locomotion, whole-body control, mobile manipulation, and humanoids"].extend([
    "=MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation",
    "=WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control"
])
NEXT_GROUPS["World models, uncertainty, failure detection, and recovery"].extend([
    "=LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models"
])

# Incremental candidate/baseline admission: 2026-10-22. Existing membership stays intact.
NEXT_GROUPS['VLA, cross-embodiment, and long-horizon planning'].extend([
    '=Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning',
    '=Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting',
    '=LAP: Language-Action Pre-training Enables Zero-Shot Cross-Embodiment Transfer',
    '=Adaptive Action Chunking at Inference-time for Vision-Language-Action Models',
    '=Memory Anchors for Continual Robot Learning',
    '=Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization',
    '=Can Vision-Language-Action Models Learn from Real-World Data Continually without Forgetting?',
    '=SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies',
    '=Real-Time Execution of Action Chunking Flow Policies',
    '=Learning High-Frequency Continuous Action Chunks in Latent Space',
    '=CounterAlign: Counterfactual Supervision for Vision-Language-Action Models',
])
NEXT_GROUPS['RL, IL, offline learning, and robot data'].extend([
    '=SAIL: Faster-than-Demonstration Execution of Imitation Learning Policies',
    '=AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World',
    '=Is Your Imitation Learning Policy Better than Mine? Policy Comparison with Near-Optimal Stopping',
    '=Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison',
    '=RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents',
])
NEXT_GROUPS['World models, uncertainty, failure detection, and recovery'].extend([
    '=Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons',
    '=RoboReward: General-Purpose Vision-Language Reward Models for Robotics',
])

# User-directed scope review; these are curation judgments, not paper claims.
FOCUS_REVIEW_DATE = "2026-10-19"
# Incremental reviews must not restamp the earlier cohort's evidence dates.
FOCUS_REVIEW_DATES = dict.fromkeys(
    (f"pr-{number:04d}" for number in range(991, 1038)), "2026-10-22"
)

# Official abstract/project checks inform priority only; they do not upgrade
# reading evidence or claim a new full-text review.
FOCUS_SOURCE_CHECKS = {
    "pr-0951": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/c0749c39aaff9e9e4c91f7118bf21b1e-Abstract-Conference.html",
    "pr-0952": "https://proceedings.mlr.press/v267/park25f.html",
    "pr-0953": "https://proceedings.neurips.cc/paper_files/paper/2025/hash/50348e8f9aef984abe0ea1ec2a326f78-Abstract-Conference.html",
    "pr-0954": "https://openreview.net/pdf/bde79a617f6c016e2c51c7771416933c0646102c.pdf",
    "pr-0955": "https://proceedings.mlr.press/v305/wagenmaker25a.html",
    "pr-0956": "https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html",
    "pr-0957": "https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html",
    "pr-0958": "https://www.roboticsproceedings.org/rss22/p089.html",
    "pr-0959": "https://doi.org/10.1126/scirobotics.aed6267",
    "pr-0960": "https://proceedings.mlr.press/v306/guo26i.html",
    "pr-0961": "https://proceedings.mlr.press/v306/zhang26ez.html",
    "pr-0962": "https://roboticsproceedings.org/rss22/p012.html",
    "pr-0963": "https://roboticsproceedings.org/rss20/p079.html",
    "pr-0964": "https://arxiv.org/abs/2505.08712",
    "pr-0965": "https://arxiv.org/abs/2507.05240",
    "pr-0966": "https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html",
    "pr-0967": "https://arxiv.org/abs/2512.19629",
    "pr-0968": "https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.pdf",
    "pr-0969": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/ecd92623ac899357312aaa8915853699-Abstract-Conference.html",
    "pr-0970": "https://www.roboticsproceedings.org/rss22/p098.html",
    "pr-0971": "https://roboticsproceedings.org/rss22/p037.html",
    "pr-0972": "https://proceedings.mlr.press/v306/lin26af.html",
    "pr-0973": "https://arxiv.org/abs/2603.28475",
    "pr-0974": "https://arxiv.org/abs/2603.25685",
    "pr-0568": "https://arxiv.org/abs/2310.07896",
    "pr-0540": "https://arxiv.org/abs/2312.03275",
    "pr-0749": "https://www.roboticsproceedings.org/rss21/p012.html",
    "pr-0948": "https://proceedings.neurips.cc/paper_files/paper/2021/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html",
    "pr-0566": "https://tonyzhaozh.github.io/aloha/",
    "pr-0732": "https://droid-dataset.github.io/",
    "pr-0874": "https://github.com/rail-berkeley/serl",
    "pr-0622": "https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html",
    "pr-0539": "https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html",
    "pr-0041": "https://arxiv.org/abs/2112.03227",
    "pr-0885": "https://www.roboticsproceedings.org/rss21/p019.html",
    "pr-0886": "https://www.roboticsproceedings.org/rss21/p028.html",
    "pr-0750": "https://www.roboticsproceedings.org/rss21/p017.html",
    "pr-0884": "https://www.roboticsproceedings.org/rss21/p018.html",
    "pr-0925": "https://proceedings.mlr.press/v202/ball23a.html",
    "pr-0914": "https://hil-serl.github.io/",
    "pr-0500": "https://openaccess.thecvf.com/content_ICCV_2019/html/Savva_Habitat_A_Platform_for_Embodied_AI_Research_ICCV_2019_paper.html",
    "pr-0541": "https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/6018_ECCV_2020_paper.php",
    "pr-0927": "https://proceedings.mlr.press/v229/shah23a.html",
    "pr-0926": "https://www.roboticsproceedings.org/rss20/p067.html",
    "pr-0136": "https://proceedings.mlr.press/v267/kim25ad.html",
    "pr-0042": "https://arxiv.org/abs/2306.03310",
    "pr-0020": "https://say-can.github.io/",
}

FOCUS_PRIORITY_RATIONALES = {
    "pr-1113": "직접 선행. 실패의 보조 언어 목표와 원 지시를 공동 학습하는 LfH는 hindsight 재사용 자체의 신규성을 제한한다. 원 과제 전이를 위한 복수 valid-label 선택을 연구하기 전에 비교해야 한다. arXiv v2 기준이며 main-conference 채택은 미확인이다.",
    "pr-1114": "언어 재라벨·skill chaining의 offline policy pretraining 선행. HER/goal-conditioned 학습에서 VLA hindsight 후학습으로 이어지는 차이와 추가 자료 효과를 구별하기 위해 읽는다.",
    "pr-1115": "자율 경험 수집·VLM 평가·image-goal 학습을 결합한 실제 로봇 시스템. 단일 VLA RL과 분해된 정책의 정보/감독/상호작용 예산을 비교하는 기준이다.",
    "pr-1116": "Flow Matching과 policy gradient를 연결하는 online RL 방법. DPPO/FQL 이후 생성 경로 likelihood·학습 noise·적은 생성 step을 비교할 때 필요하다. 후속 VLA repository 기능을 원 논문 결과와 구별한다.",
    "pr-1117": "VLA 언어 추종을 위한 counterfactual instruction/action 증강. 실제 실패의 참인 hindsight 목표와 실행되지 않은 합성 행동 자료의 기여를 구분하는 직접 대조다. 공식 main venue 미확인 preprint다.",
    "pr-0951": "Foundation bridge. PPO를 denoising policy의 RL fine-tuning으로 연결한다. Diffusion Policy → DPPO → RL-100 등 직접 policy 개선을 비교하는 prerequisite이므로 CORE를 검토할 이유가 있다. VLA 자체를 제안한 논문은 아니다.",
    "pr-0952": "Foundation bridge. Expressive flow policy와 Q-learning/one-step actor를 연결한다. IQL/CQL 이후 flow-action RL과 Q-chunking 계열의 구현·비교 기준으로 중요하다. 평가가 곧 실제 robot VLA 학습을 입증하는 것은 아니다.",
    "pr-0953": "Current trend. Chunk 단위의 exploration과 TD backup을 결합한다. ACT/FAST의 표현 관점에 RLPD/FQL의 학습 관점을 더하므로 장기 manipulation의 비교 baseline으로 필요하다.",
    "pr-0954": "Current trend. Critic과 actor의 chunk 길이를 분리한다. Q-chunking의 value propagation 이점과 짧은 action horizon의 반응성 사이의 설계 문제를 직접 다룬다. 실제 contact feedback 성능으로의 확장은 본문/실험 확인이 필요하다.",
    "pr-0955": "Current trend. Base policy weight를 고정하고 latent noise를 RL로 조정한다. ConRFT의 fine-tuning, RLDG의 distillation과 구분되는 adaptation baseline이며 generalist policy와 실제 robot 평가가 있다.",
    "pr-0956": "Benchmark / empirical study. Visual·semantic·execution generalization을 나누어 SFT와 RL을 비교한다. OpenVLA/OFT 이후 RL의 효과를 주장할 때 필요한 평가 기준이다. 해당 실험에서의 PPO 결과를 모든 VLA에 대한 우열로 일반화하지 않는다.",
    "pr-0957": "Current trend / system. OpenVLA-OFT에서 outcome reward와 scalable rollout/training을 다룬다. 현재 OFT → ConRFT 경로에 대규모 simulator RL의 비교 지점을 추가한다. Real-world 결과와 real-world online training의 범위는 구분해서 정독해야 한다.",
    "pr-0958": "Current trend / system. 여러 VLA·RL 알고리즘·시뮬레이터를 비교할 공통 interface와 resource allocation을 제공한다. SimpleVLA-RL 및 ConRFT 실험을 설계할 때 algorithm 효과와 시스템 throughput을 분리하는 데 유용하다. 공식 RSS title은 RLinf-VLA다.",
    "pr-0959": "Current trend / real-robot system. Diffusion policy에서 imitation→offline/online RL과 빠른 실행을 연결한다. HIL-SERL/DPPO와 비교해 실제 interaction 비용·latency·복구를 읽을 가치가 크다. 제목/이름의 “100”을 모든 환경에서의 무실패 보장으로 해석하지 않는다.",
    "pr-0960": "Current trend. 실제 rollout으로 world model의 failure coverage를 개선하고 synthetic rollout으로 policy를 개선하는 반복 구조다. 이미 등록된 Ctrl-World/WMPO와 연결해 model bias와 real-data budget을 비교한다. Abstract만으로 특정 RL optimizer를 단정하지 않는다.",
    "pr-0961": "Current trend. Multi-view consistency와 chunk-level branched rollout으로 world-model RL의 오차 누적을 다룬다. WMPO/WorldGym을 읽을 때 직접 비교해야 할 누락 논문이다.",
    "pr-0962": "Current trend. Multi-view dynamics와 progress value를 분리하여 imagined rollout의 advantage를 만든다. VLA-MBPO/WMPO와 reward/value 신뢰도 및 real-robot transfer를 비교할 가치가 있다.",
    "pr-0963": "Foundation lineage. RGB video history에서 next action을 출력하는 navigation VLM이다. Uni-NaVid/StreamVLN을 비교할 때 선행 interface를 보충한다. **NaVILA 및 Uni-NaVid와 다른 논문**이다.",
    "pr-0964": "Current trend. Simulation training에서 real-world cross-embodiment local navigation으로 이어지는 경로를 보충한다. NoMaD/ViNT의 local policy와 비교할 대상이며, 논문 자체를 language-conditioned VLA RL로 부르지는 않는다.",
    "pr-0965": "Current trend. Fast action context와 slow history memory를 결합한다. NaVid/Uni-NaVid 이후 긴 video history를 제한된 inference budget으로 처리하는 비교 대상이다. RL 자체의 논문으로 분류하지 않는다.",
    "pr-0966": "Current trend / dataset. Semantic reasoning과 trajectory generation에 socially compliant reward를 연결한다. NaVILA/VLFM의 task success 중심 비교에 행동 제약을 더한다. 기존 **SocialNav-SUB는 별도 benchmark**다.",
    "pr-0967": "Current trend / enabling 3D. Metric-aware geometry와 history 기반 state estimation을 trajectory planning에 연결한다. 일반 reconstruction보다 현재 navigation 목표에 직접적이다. Controller가 실제 사용하는 pose·calibration·simulator GT의 범위는 본문/배포 코드 확인이 필요하다.",
    "pr-0968": "Current trend / action-relevant 3D. State와 action을 3D point flow로 표현하고 예측을 manipulation MPC에 연결한다. DP3/3D-VLA 이후 explicit geometry와 world model을 비교할 직접적인 연결이다. 본문 평가의 보장 범위와 calibration 의존성은 추가 확인 대상이다.",
    "pr-0969": "Benchmark. Stitching·장기 horizon·pixel input 등의 능력을 구분하는 기준이다. FQL/Q-chunking/DQC 결과를 이해하는 prerequisite이며 LIBERO/CALVIN과 평가 목적을 구분한다. Language-conditioned real-robot benchmark는 아니다.",
    "pr-0970": "Benchmark. Task success와 물리적 damage를 분리하고 damage-aware IL/RL 및 VLA 평가를 지원한다. 기존 safety/recovery 흐름에 contact·thermal·fluid damage라는 구체적인 평가 축을 보충한다.",
    "pr-0971": "Current system. 실제 robot online RL에서 edge/cloud·buffer·weight synchronization을 구현할 때 SERL/HIL-SERL의 시스템 확장으로 읽는다. Simulator 중심 RLinf-VLA와 역할이 다르다.",
    "pr-0972": "Current trend. RL fine-tuning 중 task-specific overfitting을 줄이는 것이 연구 질문일 때 RL4VLA/ConRFT와 비교한다. 새 architecture라는 이유만으로 CORE로 올리지는 않는다.",
    "pr-0973": "Current trend / simulator. Tactile feedback을 이용하는 insertion·contact RL을 선택할 때 relevant하다. HIL-SERL 등 실제 interaction 학습과 simulation fidelity/transfer를 비교한다. Peg insertion 결과를 범용 dexterity로 확대하지 않는다.",
    "pr-0835": "TD bootstrapping은 SAC·IQL·RLPD의 value target과 offline/online 오차를 이해하는 공통 기반이다.",
    "pr-0838": "Policy-gradient objective와 gradient estimator는 PPO 및 VLA의 reward-driven 정책 갱신을 비교하는 기반이다.",
    "pr-0524": "PPO의 clipped policy update는 on-policy VLA RL과 navigation policy optimization의 대표 비교 기준이다.",
    "pr-0620": "Entropy-regularized off-policy actor-critic은 SERL·HIL-SERL 계열의 sample-efficient manipulation RL을 이해하는 기반이다.",
    "pr-0624": "Dataset action support 안에서 value와 policy를 학습하는 IQL은 VLA의 offline initialization과 online 개선을 구분하는 기준이다.",
    "pr-0622": "Offline 데이터 밖 action의 value 과대평가를 다루는 CQL은 IQL·VLA RL의 보수성과 탐색 trade-off를 비교하는 기반이다.",
    "pr-0522": "DAgger의 distribution shift와 data aggregation은 VLA closed-loop 실패 및 intervention 기반 RL 개선을 해석하는 기반이다.",
    "pr-0747": "RoboMimic의 demonstration·observation·평가 설계는 VLA/RL 방법 비교에서 데이터 품질과 정책 효과를 분리하는 기준이다.",
    "pr-0008": "DDPM의 denoising objective는 Diffusion Policy와 이후 diffusion-action RL의 정책 분포를 이해하는 기반이다.",
    "pr-0745": "Flow Matching의 vector-field 학습은 π0 계열 continuous action 생성과 RL 적응의 policy parameterization을 이해하는 기반이다.",
    "pr-0019": "Diffusion Policy는 VLA의 개선이 language pretraining·action generation·RL 중 어디서 생기는지 비교할 대표 visuomotor IL baseline이다.",
    "pr-0925": "RLPD의 offline/online replay 결합은 SERL·HIL-SERL에서 demonstration을 활용하는 실제 robot RL 학습 경로의 선행 기반이다.",
    "pr-0874": "SERL은 actor/learner·reward·robot interface를 연결해 HIL-SERL과 VLA RL의 실제 학습 비용을 평가할 공개 시스템 기준이다.",
    "pr-0914": "HIL-SERL은 demonstration·human intervention·reward classifier를 결합한 real-robot RL의 대표 실행 기준이며 ConRFT·RLDG 비교에 필요하다.",
    "pr-0886": "RLDG는 specialist RL로 얻은 데이터를 generalist에 증류하는 경로를 제시해 ConRFT의 직접 VLA RL 미세조정과 구분할 핵심 비교 기준이다.",
    "pr-0732": "DROID는 실제 환경의 조작 데이터 다양성과 수집 조건을 제공하여 VLA 사전학습·fine-tuning의 데이터 가정을 판단하는 기준이다.",
    "pr-0042": "LIBERO는 OpenVLA-OFT와 VLA RL의 task suite·transfer 평가를 이해하고 baseline을 공정하게 비교하기 위한 benchmark 기반이다.",
    "pr-0500": "Habitat는 navigation의 task·sensor·simulator·generalization protocol을 제공하여 VLN-CE와 navigation RL 평가를 해석하는 기반이다.",
    "pr-0005": "CLIP의 image-language alignment는 VLA backbone과 VLFM·ConceptFusion의 semantic grounding을 이해하는 공통 기반이다.",
    "pr-0022": "RT-2는 pretrained VLM에서 robot action으로의 전이를 정식화해 OpenVLA 및 이후 VLA의 action-token 설계를 이해하는 기반이다.",
    "pr-0024": "Open X-Embodiment는 Octo·OpenVLA의 heterogeneous robot-data와 embodiment transfer 가정을 이해하는 데이터 기반이다.",
    "pr-0052": "Octo는 공개 generalist policy의 diffusion action·cross-embodiment adaptation을 제공해 VLA 및 RL 개선의 baseline이 된다.",
    "pr-0051": "OpenVLA는 공개 VLA 학습·fine-tuning 경로를 제공하며 OFT와 후속 VLA RL의 backbone 기준이다.",
    "pr-0750": "OpenVLA-OFT는 action chunking·parallel decoding·continuous action의 강한 supervised baseline으로 RL의 추가 이득을 분리하는 데 필요하다.",
    "pr-0746": "π0는 VLM과 flow-based action expert를 결합해 이후 flow VLA와 RL 정책 갱신의 action interface를 이해하는 기반이다.",
    "pr-0749": "FAST는 action tokenization과 고주파 action chunk 압축을 분리해 continuous-flow와 autoregressive VLA의 비용을 비교하는 기준이다.",
    "pr-0061": "π0.5는 open-world generalization과 이질적 데이터 결합의 대표 시스템으로 RL 개선을 새로운 환경·task transfer와 함께 평가할 기준이다.",
    "pr-0885": "ConRFT는 offline BC/Q 학습에서 online human-intervention VLA RL로 이어지는 직접 fine-tuning 경로를 제공하는 연구축의 핵심 비교 기준이다.",
    "pr-0020": "SayCan은 language task proposal과 learned affordance/value를 결합해 VLA+RL의 hierarchical manipulation·navigation 의사결정을 이해하는 기반이다.",
    "pr-0884": "NaVILA는 VLA의 중간 수준 spatial command와 visual locomotion RL을 연결해 navigation에서 reasoning/control interface를 비교하는 대표 시스템이다.",
    "pr-0041": "CALVIN은 language-conditioned long-horizon manipulation의 연속 skill 성공과 일반화를 평가해 LIBERO와 다른 실패 누적을 비교하는 기준이다.",
    "pr-0566": "ACT는 action chunk와 temporal aggregation을 사용하는 조작 IL 기준으로 OFT·flow VLA·RL 개선의 action-interface 효과를 분리한다.",
    "pr-0926": "DP3는 sparse point-cloud representation을 action diffusion에 연결해 3D 입력이 조작 일반화에 주는 효과를 직접 비교하는 기준이다.",
    "pr-0821": "POMDP의 belief와 partial observability는 navigation memory·VLA history·recovery의 상태 가정을 명시하는 기반이다.",
    "pr-0825": "Impedance control은 contact-rich policy의 action이 low-level compliance와 어떻게 연결되는지 판단하고 RL 성능과 controller 효과를 구분하는 기반이다.",
    "pr-0831": "MuJoCo는 조작 RL benchmark의 접촉 dynamics와 simulator 가정을 이해해 reward·success·sim-to-real 비교를 해석하는 기반이다.",
    "pr-0568": "NoMaD는 goal-conditioned diffusion과 exploration을 결합해 ViNT 이후 navigation action generation의 비교 기준을 제공한다.",
    "pr-0030": "ConceptFusion은 open-set semantic 3D memory가 object navigation과 language-grounded robot action으로 이어지는 representation 기준이다.",
    "pr-0037": "RVT는 3D scene을 multi-view action representation으로 연결해 DP3·spatial VLA와 비교할 manipulation 기준이다.",
    "pr-0540": "VLFM은 semantic value map과 frontier exploration을 연결해 learned navigation VLA/RL과 비교할 modular object-navigation 기준이다.",
    "pr-0541": "VLN-CE는 graph waypoint를 넘어 low-level action을 실행하는 continuous navigation formulation으로 NaVILA와 VLN RL의 평가 가정을 구분한다.",
    "pr-0927": "ViNT는 다양한 robot navigation 데이터의 goal-conditioned pretraining을 제공해 NoMaD와 navigation VLA의 transfer를 이해하는 기반이다.",
    "pr-0574": "Mobile ALOHA는 base와 bimanual arm을 함께 다루는 데이터·policy interface를 제공해 navigation과 manipulation의 결합 범위를 판단하는 기준이다.",
    "pr-0684": "TD-MPC2는 latent dynamics·value·planning을 함께 사용하는 model-based RL 기준으로 VLA+world-model 개선의 비용과 효과를 비교한다.",
    "pr-0677": "Recovery RL은 task policy와 recovery policy의 역할을 분리해 VLA/RL의 실패 후 복구 및 안전한 online 학습을 비교하는 기반이다.",
    "pr-0552": "RRT는 learned navigation·manipulation과 motion-planning baseline을 비교하는 선택적 선행으로 유지한다.",
    "pr-0833": "MPPI는 VLA action과 model-based local control을 결합할 때 필요한 전문화로 둔다.",
    "pr-0748": "PDDLStream은 SayCan 이후 symbolic/TAMP 대안을 검토하는 계획 branch로 둔다.",
    "pr-0615": "TRPO는 PPO의 trust-region 계보를 더 깊게 이해할 때 읽는 선택적 기반으로 둔다.",
    "pr-0561": "Domain Randomization은 VLA/RL sim-to-real 실험을 설계할 때 읽는 직접 관련 전문화로 둔다.",
    "pr-0636": "IBC는 action energy optimization과 diffusion/flow policy를 비교하는 선택적 baseline으로 둔다.",
    "pr-0018": "Decision Transformer는 sequence-modeling과 value/policy optimization의 차이를 비교할 때 읽는다.",
    "pr-0625": "Q-Transformer는 autoregressive action과 offline Q-learning을 연결하는 VLA+RL 전문화로 유지한다.",
    "pr-0645": "GraspNet은 grasp perception을 task input이나 benchmark로 쓰는 manipulation branch에서 읽는다.",
    "pr-0646": "Contact-GraspNet은 6-DoF grasp proposal을 사용하는 modular manipulation baseline으로 유지한다.",
    "pr-0736": "Factory는 contact-rich assembly를 sim-to-real RL 실험으로 선택할 때 읽는다.",
    "pr-0649": "RoboPack은 tactile dynamics를 policy feedback에 추가하는 manipulation 전문화로 유지한다.",
    "pr-0502": "CLIPort는 semantic grounding과 spatial action을 분리하는 VLA/3D manipulation의 선택적 비교 기준이다.",
    "pr-0023": "PaLM-E는 embodied multimodal reasoning 계보로 보존하고 직접 action/RL interface 논문 이후에 읽는다.",
    "pr-0021": "RT-1은 RT-2·OpenVLA의 robot-data/action-token 계보를 확인할 때 읽는 기반으로 둔다.",
    "pr-0038": "VoxPoser는 VLA 직접 정책과 language-conditioned 3D planning을 비교하는 전문화로 유지한다.",
    "pr-0678": "World Models 원전은 latent world-model 계보를 확인할 때 읽고 실제 robot/control 비교는 TD-MPC2와 후속 연구에 우선한다.",
    "pr-0682": "DayDreamer는 실제 robot model-based RL branch에서 학습 예산과 dynamics 사용을 비교한다.",
    "pr-0675": "CBF는 safety filter의 가정과 보장을 연구하는 branch에서 읽으며 VLA/RL 전체의 선행 의무에서는 분리한다.",
    "pr-0564": "RMA는 NaVILA 등 legged navigation의 저수준 adaptation을 깊게 다룰 때 읽는다.",
    "pr-0012": "PointNet은 DP3 등 point-cloud policy encoder를 구현·비교할 때 필요한 선택적 representation 기반이다.",
    "pr-0017": "DROID-SLAM은 navigation의 localization 품질이 policy 성능을 제한하는 실험에서 읽는다.",
    "pr-0136": "FeedTTA는 episodic success/failure feedback을 이용한 online VLN adaptation으로 manipulation VLA RL과 navigation RL의 reward·stability 차이를 비교한다.",
    "pr-0948": "Habitat 2.0는 navigation에서 object rearrangement/mobile manipulation으로 확장할 때 필요한 task·simulator 기준이다.",
    "pr-0539": "R2R은 VLN instruction grounding과 graph-navigation 평가의 원형으로 VLN-CE·NaVILA의 설정 차이를 비교할 때 읽는다.",

}

FOCUS_REFERENCE_RATIONALES = {
    "pr-0974": "PersistWorld는 world-model visual fidelity를 RL로 개선한다. 실제 policy success의 개선 근거를 별도 확인하기 전에는 Ctrl-World/WMPO 구현 시 참조하는 REFERENCE로 둔다.",
    "pr-0823": "Kalman filtering은 필요할 때 state-estimation 가정을 확인할 기반이며 현재 VLA/RL policy 학습의 필수 정독 선행은 아니다.",
    "pr-0822": "A*는 navigation search baseline으로 보존하되 learned navigation policy·RL adaptation의 공통 필수 선행에서 분리한다.",
    "pr-0550": "Operational-space control은 torque/Cartesian controller를 직접 설계할 때 참조하며 정책 수준 VLA/RL의 공통 읽기 부담에서 분리한다.",
    "pr-0824": "Hybrid position/force control은 force-controlled contact task를 정할 때 참조하고 현재 contact interface 공통 기반은 impedance로 대표한다.",
    "pr-0551": "PRM은 sampling-based motion planning을 직접 비교할 때 참조하며 learned policy와 navigation adaptation의 공통 선행에서 분리한다.",
    "pr-0555": "CHOMP는 trajectory optimizer를 설계·baseline으로 사용하는 경우에 읽는 전문 계획 방법이다.",
    "pr-0558": "TrajOpt는 collision-constrained optimization이 필요한 경우 참조하며 현재 VLA/RL 기본 경로에는 두지 않는다.",
    "pr-0666": "Rigid-contact whole-body dynamics가 주 기여이므로 현재 arm/mobile navigation 정책 연구에는 필요시 참조한다.",
    "pr-0667": "Humanoid hierarchical QP controller 설계가 주 기여이므로 현재 VLA/RL manipulation·navigation의 공통 선행에서 분리한다.",
    "pr-0668": "Quadruped whole-body NMPC는 해당 low-level controller를 연구할 때 참조한다.",
    "pr-0836": "Q-learning 원전은 TD·SAC·IQL·CQL을 읽다 tabular update의 정의가 필요할 때 조회한다.",
    "pr-0837": "REINFORCE 원전은 estimator 유도를 확인할 때 조회하고 공통 policy-gradient 기반은 function approximation 논문으로 대표한다.",
    "pr-0830": "PILCO의 Gaussian-process policy search는 model-based RL 역사·data efficiency 비교용으로 보존한다.",
    "pr-0560": "Guided Policy Search는 trajectory-centric supervision을 직접 비교할 때 참조하며 VLA/RL adaptation 기본 경로에서 분리한다.",
    "pr-0523": "Adversarial imitation objective는 inverse-reward 연구를 선택할 때 참조하며 현재 reward-based VLA 개선의 필수 선행은 아니다.",
    "pr-0827": "Analytic optimal grasp 원전은 grasp-quality/contact mechanics를 직접 설계할 때 읽는다.",
    "pr-0848": "GelSight hardware 원전은 tactile sensing을 실험에 도입할 때 참조한다.",
    "pr-0642": "Contact-invariant trajectory optimization은 specialized contact planner 비교가 필요할 때 읽는다.",
    "pr-0647": "Quasi-dynamic contact-model planning은 model-based contact optimization을 구현할 때 참조한다.",
    "pr-0648": "Extrinsic tactile contact-mode control은 해당 sensor/control regime를 선택할 때 읽는다.",
    "pr-0585": "Human-reference dexterous tracking은 현재 language-conditioned arm/navigation policy보다 별도 embodiment 전문화에 가깝다.",
    "pr-0828": "ZMP preview walking은 biped gait controller 설계용 foundation으로 보존한다.",
    "pr-0851": "Physics-based character motion prior는 human motion imitation을 선택할 때 참조한다.",
    "pr-0656": "Quadruped terrain locomotion은 저수준 보행 성능이 핵심인 별도 전문화이므로 on-demand로 이동한다.",
    "pr-0661": "Parkour의 agile locomotion은 language-goal navigation/RL adaptation과 구분해 전문 참조로 보존한다.",
    "pr-0599": "Humanoid whole-body benchmark는 해당 embodiment의 실험을 선택할 때 참조한다.",
    "pr-0602": "Human-to-humanoid whole-body teleoperation은 현재 arm/mobile policy 연구의 공통 baseline에서 분리한다.",
    "pr-0826": "ICP는 localization/registration 알고리즘을 직접 다룰 때 참조하며 현재 policy 평가의 필수 원전은 아니다.",
    "pr-0011": "3D Gaussian Splatting 원전은 rendering/map representation을 구현할 때 참조하고 CORE에는 action으로 연결된 3D 방법을 둔다.",
    "pr-0046": "DUSt3R는 geometric reconstruction backbone을 선택할 때 참조하고 CORE에는 robot-policy downstream이 직접 비교되는 방법을 둔다.",
    "pr-0852": "Perpetual Humanoid Control for Real-time Simulated Avatars의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0867": "MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0868": "HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0872": "SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0595": "DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0654": "Sim-to-Real: Learning Agile Locomotion For Quadruped Robots의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0655": "Learning Quadrupedal Locomotion over Challenging Terrain의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0662": "Extreme Parkour with Legged Robots의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0658": "Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0601": "HumanPlus: Humanoid Shadowing and Imitation from Humans의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0607": "ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0606": "LangWBC: Language-Directed Humanoid Whole-Body Control via End-to-End Learning의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0611": "HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0613": "VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0604": "AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0743": "Flying Hand: End-Effector-Centric Framework for Versatile Aerial Manipulation Teleoperation and Policy Learning의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",
    "pr-0603": "WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts의 주요 비교 대상은 전신 motion tracking·보행 또는 특수 embodiment 제어이므로, 현재 VLA+RL arm/mobile navigation 경로에서는 필요시 참조한다.",


}

# 2026-10-21 admission rationales; no retrospective change to older reviews.
FOCUS_PRIORITY_RATIONALES.update({
    "pr-0975": "NaVILA·MoTo와 함께 VLA와 기하학적 실행 가능성의 경계를 비교하는 NEXT다.",
    "pr-0977": "OpenVLA 이후 language-conditioned 행동 여부를 확인할 직접 비교군이므로 NEXT다.",
    "pr-0978": "VLA의 이득이 task specification 차이인지 가릴 강한 non-VLA baseline이므로 NEXT다.",
    "pr-0979": "D1에서 state 사용과 history 효과를 먼저 입증할 NEXT prerequisite다.",
    "pr-0980": "D1의 hardware-cause adaptation과 가장 가까운 NEXT 비교군이다.",
    "pr-0981": "D1에서 단순 vision 강화나 stage feedback을 새 기여로 재주장하지 않게 하는 NEXT다.",
    "pr-0982": "D1의 modality robustness와 직접 겹치는 NEXT다. 카메라 복원 CoRe-VLA와 다른 논문이다.",
    "pr-0983": "D1 camera-shift 보정의 직접 NEXT baseline이다. Conditional Routing CoRE-VLA와 별도 identity다.",
    "pr-0984": "D1의 fault taxonomy와 policy/controller 경계 진단에 필요한 NEXT benchmark다.",
    "pr-0987": "NaVILA 이후 VLA와 low-level RL의 역할을 비교할 NEXT다.",
    "pr-0989": "D1에서 modality dominance를 새 발견으로 주장하지 않도록 추가한 직접 NEXT다."
})
FOCUS_REFERENCE_RATIONALES.update({
    "pr-0976": "D2의 도구·접촉 표현을 비교할 REFERENCE다. End-to-end VLA로 분류하지 않는다.",
    "pr-0985": "D3의 일반 task interruption 주장을 제한하는 REFERENCE다.",
    "pr-0986": "D3의 concurrency 자체를 기여로 주장하지 않게 하는 REFERENCE다.",
    "pr-0988": "D3 양팔 role reasoning의 중복을 피할 REFERENCE다. IROS 2026은 저자 표기이며 공식 채택 미확인이다.",
    "pr-0990": "Top-tier 선정 논문은 아니지만 D1의 stream diagnosis·correction 주장과 직접 겹쳐 REFERENCE로 등록한다."
})

FOCUS_PRIORITY_RATIONALES.update({
    'pr-0991': 'E1에서 복잡한 replay selector 전에 확인할 강한 단순 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-0992': '의미 능력 보존이라는 넓은 방향의 직접 선행이며 action interface 비교에도 필요하다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-0993': 'Cross-embodiment VLA interface를 비교할 최신 직접 선행이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-0994': 'E2의 adaptive horizon 주장에 대한 직접 baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-0995': 'E1의 action-conflict replay와 가장 가까운 직접 비교군이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-0996': 'E1에서 정상 action 정렬·mixture 자체의 설명력을 먼저 제거할 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-0997': 'E1의 실환경 단순 baseline과 compute-matched 비교에 필요한 연구다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-1000': 'E1/E2에서 정상적인 state-effect 표현과 dynamics adapter의 강한 대안이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-1002': '초기 지연 후보와 E2가 반드시 비교할 표준 실행 baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-1003': 'E2에서 retiming·tracking·feedback 이득을 분해할 핵심 IL baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-1004': 'E2에서 고주파 표현과 controller 변경을 분리할 직접 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-1021': 'C4/C6의 reward·progress·평가 신호를 비교할 핵심 최신 baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-1022': 'C4의 독립 outcome과 reward model 차이를 정할 직접 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-1025': 'C5/C6의 reset ledger와 반복 평가를 설계할 핵심 system 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-1027': 'C6의 trial budget·통계적 중단에 대한 표준 직접 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-1028': 'C6의 progress-aware 선택을 신규 통계 방법으로 재주장하지 않도록 하는 최신 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-1033': 'C2와 새로운 VLA 탐색에서 지시 준수 개선의 직접 baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
    'pr-1034': 'C2/D3의 instruction switch와 성공 지표를 검증할 핵심 benchmark다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.',
})
FOCUS_REFERENCE_RATIONALES.update({
    'pr-0998': 'E1에서 물리 action 충돌을 단순 expert 분리와 구별할 직접 REFERENCE다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-0999': 'E2에서 연속 행동 곡선 자체를 신규 기여로 재주장하지 않기 위한 REFERENCE다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1001': 'E2의 adaptive time compression과 직접 겹치는 REFERENCE다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1005': 'E2의 fresh feedback correction·delay/horizon 분리가 이미 존재함을 보여준다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1006': 'E2 진단에서도 state-dependent 안정성을 새 발견으로 주장하지 않도록 하는 REFERENCE다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1007': 'D2의 운반 결과를 고려한 파지 주장이 이미 다뤄졌음을 보여준다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1008': 'D2에서 grasp/place 변경과 전체 경로 reasoning의 기하학 baseline이다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1009': 'D2의 파지 후 geometry 고려라는 넓은 기여와 직접 충돌한다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1010': 'D2/D3에서 persistent planning·shield 결합의 신규성 경계를 정한다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1011': 'D2에서 downstream outcome·failure attribution을 새 방법으로 주장하지 않게 한다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1012': 'D2에서 후속 실행 가능성을 reward에 넣는 좁은 RL 주장도 제한한다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1013': 'D3에서 rollback이 세계 상태를 되돌린다는 잘못된 가정을 피할 직접 비교군이다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1014': 'D3에서 단순 switching 방법과 추가 도구 정보의 효과를 구분할 기준이다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1015': 'C5/D3의 비가역성·reset 질문에 필요한 RL 선행이다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1016': 'D3의 multi-level replanning이 이미 존재하는 workshop 비교군이다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1017': 'E1에서 loss/gradient interference를 신규 원리로 재주장하지 않게 하는 foundation이다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1018': 'C4에서 query 선택·reward refinement의 오래된 직접 선행이다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1019': 'C4의 decision-relevant reward audit 주장의 직접 foundation이다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1020': 'C4에서 progress reward 품질과 정책 효과를 분리할 비교군이다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1023': 'C5의 continuing/deployed 평가와 human intervention 기준을 제공한다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1024': 'C5의 reset-induced state distribution 자체가 신규 문제가 아님을 보여준다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1026': 'C6에서 OPE+능동 online 평가라는 넓은 방법의 직접 선행이다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1029': 'C6의 task-aware cost-aware 평가 배분에 대한 직접 REFERENCE다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1030': 'C1/D1의 능동 관측·관측 정렬 주장과 직접 충돌한다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1031': 'C1의 시선 조절과 action-relevant 관측에 대한 직접 REFERENCE다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1032': 'C1/RP-2의 관측/개입 가치 진단에 대한 직접 evaluation 기준이다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1035': 'C2의 수행 방식 지시 주장이 겹치는 직접 선행이며 KineVLA와 동일 identity다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1036': 'C3에서 실행 동치 action의 확률 질량을 합치는 원리의 foundation이다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
    'pr-1037': 'C3의 action equivalence 주장을 제한하는 가장 직접적인 이론 계보다. REFERENCE: 해당 후보의 한계·대안 점검 때 참조하며 집중 읽기에는 추가하지 않는다.',
})
FOCUS_SOURCE_CHECKS.update({
    'pr-0991': 'https://proceedings.mlr.press/v306/liu26bu.html',
    'pr-0992': 'https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html',
    'pr-0993': 'https://www.roboticsproceedings.org/rss22/p203.html',
    'pr-0994': 'https://arxiv.org/abs/2604.04161',
    'pr-0995': 'https://openreview.net/forum?id=dSbtHPqFj9',
    'pr-0996': 'https://arxiv.org/abs/2602.09722',
    'pr-0997': 'https://arxiv.org/abs/2605.26820',
    'pr-0998': 'https://arxiv.org/abs/2512.05693',
    'pr-0999': 'https://arxiv.org/abs/2610.05230',
    'pr-1000': 'https://arxiv.org/abs/2606.24049',
    'pr-1001': 'https://arxiv.org/abs/2610.25961',
    'pr-1002': 'https://papers.nips.cc/paper_files/paper/2025/hash/300ccb2187dedd4edcc07f7e76d8e553-Abstract-Conference.html',
    'pr-1003': 'https://proceedings.mlr.press/v305/arachchige25a.html',
    'pr-1004': 'https://proceedings.mlr.press/v306/wang26lj.html',
    'pr-1005': 'https://arxiv.org/abs/2509.23224',
    'pr-1006': 'https://arxiv.org/abs/2610.01626',
    'pr-1007': 'https://doi.org/10.1109/LRA.2026.3653338',
    'pr-1008': 'https://doi.org/10.1109/LRA.2025.3562005',
    'pr-1009': 'https://arxiv.org/abs/2610.01083',
    'pr-1010': 'https://arxiv.org/abs/2610.21453',
    'pr-1011': 'https://arxiv.org/abs/2606.03385',
    'pr-1012': 'https://arxiv.org/abs/2607.16506',
    'pr-1013': 'https://arxiv.org/abs/2609.26313',
    'pr-1014': 'https://openreview.net/forum?id=sF3YZbbTNX',
    'pr-1015': 'https://proceedings.neurips.cc/paper_files/paper/2025/hash/56d748a1d7128158681280be7668e0d3-Abstract-Conference.html',
    'pr-1016': 'https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/html/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.html',
    'pr-1017': 'https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html',
    'pr-1018': 'https://proceedings.mlr.press/v119/reddy20a.html',
    'pr-1019': 'https://proceedings.neurips.cc/paper/2021/hash/1fa6269f58898f0e809575c9a48747ef-Abstract.html',
    'pr-1020': 'https://openaccess.thecvf.com/content/ICCV2025/html/Ayalew_PROGRESSOR_A_Perceptually_Guided_Reward_Estimator_with_Self-Supervised_Online_Refinement_ICCV_2025_paper.html',
    'pr-1021': 'https://www.roboticsproceedings.org/rss22/p140.html',
    'pr-1022': 'https://arxiv.org/abs/2601.00675',
    'pr-1023': 'https://openreview.net/forum?id=nkaba3ND7B5',
    'pr-1024': 'https://proceedings.mlr.press/v162/sharma22a.html',
    'pr-1025': 'https://proceedings.mlr.press/v305/zhou25a.html',
    'pr-1026': 'https://papers.nips.cc/paper_files/paper/2021/hash/cec2346566ba8ecd04bfd992fd193fb3-Abstract.html',
    'pr-1027': 'https://roboticsproceedings.org/rss21/p077.html',
    'pr-1028': 'https://roboticsproceedings.org/rss22/p076.html',
    'pr-1029': 'https://proceedings.mlr.press/v305/anwar25a.html',
    'pr-1030': 'https://arxiv.org/abs/2610.23378',
    'pr-1031': 'https://arxiv.org/abs/2610.03710',
    'pr-1032': 'https://arxiv.org/abs/2610.13516',
    'pr-1033': 'https://openreview.net/forum?id=AY4totylcx',
    'pr-1034': 'https://openreview.net/forum?id=A9AQjk3dAt',
    'pr-1035': 'https://arxiv.org/abs/2603.17524',
    'pr-1036': 'https://proceedings.mlr.press/v80/fujita18a.html',
    'pr-1037': 'https://openreview.net/forum?id=HkgqFiAcFm',
})

# Incremental registry refresh, 2026-10-25: preserve all earlier memberships.
NEXT_GROUPS["RL, IL, offline learning, and robot data"].extend([
    "=What Matters in Learning from Large-Scale Datasets for Robot Manipulation",
    "=DataMIL: Selecting Data for Robot Imitation Learning with Datamodels"
])
NEXT_GROUPS["VLA, cross-embodiment, and long-horizon planning"].extend([
    "=Mechanistic Interpretability for Steering Vision-Language-Action Models",
    "=LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models",
    "=THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation",
    "=RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies",
    "=Beyond Sight: Finetuning Generalist Robot Policies with Heterogeneous Sensors via Language Grounding"
])
NEXT_GROUPS["World models, uncertainty, failure detection, and recovery"].extend([
    "=Simple Masked Training Strategies Yield Control Policies That Are Robust to Sensor Failure",
    "=Scaling Robot Policy Evaluation via Discrete Diffusion World Model",
    "=Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling"
])
FOCUS_PRIORITY_RATIONALES.update({
    "pr-1038": "단순 시각·공간 정렬로 설명되는 이득을 제거하기 위한 DataMIL·GAP-N1의 비교 기준이다.",
    "pr-1039": "현재 proxy→target 데이터 전이 질문에서 반드시 대조할 performance-aware 선택 방법이다.",
    "pr-1043": "Instruction 대응이나 VLA 행동 교정을 연구할 때 fine-tuning 없는 직접 baseline이다.",
    "pr-1044": "새 multimodal VLA adaptation 전에 대조할 단순 sensor-dropout 기준이다.",
    "pr-1045": "기본 성공률과 일반화 성능을 구분하는 현재 VLA 평가의 직접 기준이다.",
    "pr-1046": "LIBERO 계열에 한정하지 않고 manipulation 일반화를 점검할 benchmark 계보다.",
    "pr-1047": "현재 GAP-N1–N3의 직접 benchmark이며 memory 필요성과 단순 정보 누설을 구분하는 기준이다.",
    "pr-1048": "World-model 평가를 연구할 때 시각 품질과 행동별 순위 신뢰도를 구분할 직접 비교군이다.",
    "pr-1049": "GAP-P 계열에서 uncertainty 추가 자체를 새로운 navigation 기여로 삼지 않게 하는 직접 선행이다.",
    "pr-1053": "새 sensor 결합을 연구할 때 naive finetuning·masked training과 함께 대조할 직접 기준이다."
})
FOCUS_REFERENCE_RATIONALES.update({
    "pr-1040": "학습 전 subset 선택과 실행 중 retrieval의 효과를 분리할 직접 대안이다.",
    "pr-1041": "Proxy scoring과 target 확인 자체를 새 VLA 기여로 재주장하지 않게 하는 GAP-N1의 직접 선행이다.",
    "pr-1042": "GAP-N1에서 관측 정보 효과와 optimizer 설정 효과를 분리하는 필수 방법론 참조다.",
    "pr-1050": "물성·boundary 식별과 task-oriented probing을 구별하는 GAP-DE의 직접 선행이다.",
    "pr-1051": "물성 adaptation을 신규 방법으로 반복하지 않기 위한 GAP-DE의 모델 기반 대안이다.",
    "pr-1052": "Semantic representation을 실제 contact/action에 연결하는 비교용 3D/affordance 지원 연구다.",
    "pr-1054": "지시 교란 평가와 구현된 task의 유효성을 함께 점검할 비교 benchmark다.",
    "pr-1055": "THE COLOSSEUM의 후속 평가 자산이며 다양한 로봇을 다루는 사용자 연구축과 직접 연결된다."
})
FOCUS_SOURCE_CHECKS.update({
    "pr-1038": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/16466b6c95c5924784486ac5a3feeb65-Abstract-Conference.html",
    "pr-1039": "https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html",
    "pr-1040": "https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c2ecd140ebe227a531edc9a0c3b69d4-Abstract-Conference.html",
    "pr-1041": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/412360d2dd428c26f34918c8d682cf7e-Abstract-Conference.html",
    "pr-1042": "https://proceedings.iclr.cc/paper_files/paper/2026/hash/c7d04ce5e71efdfc7a4a78f7161238a9-Abstract-Conference.html",
    "pr-1043": "https://proceedings.mlr.press/v305/haon25a.html",
    "pr-1044": "https://proceedings.mlr.press/v270/skand25a.html",
    "pr-1045": "https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html",
    "pr-1046": "https://roboticsproceedings.org/rss20/p133.html",
    "pr-1047": "https://proceedings.mlr.press/v306/dai26c.html",
    "pr-1048": "https://proceedings.mlr.press/v306/li26hi.html",
    "pr-1049": "https://proceedings.mlr.press/v305/yao25a.html",
    "pr-1050": "https://www.roboticsproceedings.org/rss20/p007.html",
    "pr-1051": "https://roboticsproceedings.org/rss20/p010.html",
    "pr-1052": "https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5748_ECCV_2024_paper.php",
    "pr-1053": "https://arxiv.org/abs/2501.04693",
    "pr-1054": "https://arxiv.org/abs/2510.03827",
    "pr-1055": "https://arxiv.org/abs/2605.27759"
})
FOCUS_REVIEW_DATES.update(dict.fromkeys((f"pr-{n:04d}" for n in range(1038, 1056)), "2026-10-25"))

# Top-tier Robotics/AI supplement, 2026-10-25; no prior membership removed.
NEXT_GROUPS["VLA, cross-embodiment, and long-horizon planning"].extend([
    "=RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies",
    "=A Taxonomy for Evaluating Generalist Robot Manipulation Policies",
    "=Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation",
    "=Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs"
])
NEXT_GROUPS["Contact-rich, deformable, force, and dexterous manipulation"].extend([
    "=FMB: A functional manipulation benchmark for generalizable robotic learning",
    "=Learning Visuotactile Estimation and Control for Non-prehensile Manipulation under Occlusions"
])
NEXT_GROUPS["RL, IL, offline learning, and robot data"].extend([
    "=ReMix: Optimizing Data Mixtures for Large Scale Imitation Learning",
    "=DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning",
    "=TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction",
    "=Equivariant diffusion policy for sample-efficient robotic manipulation"
])
NEXT_GROUPS["Locomotion, whole-body control, mobile manipulation, and humanoids"].extend([
    "=TidyBot++: An Open-Source Holonomic Mobile Manipulator for Robot Learning"
])
NEXT_GROUPS["Active and embodied 3D Vision"].extend([
    "=PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos"
])
FOCUS_PRIORITY_RATIONALES.update({
    "pr-1056": "LIBERO-Plus·THE COLOSSEUM의 고정 benchmark와 구별되는 실환경 평가 기준을 보완한다.",
    "pr-1057": "VLA 일반화 주장을 시각 변화·언어 이해·행동 변화로 분해할 평가 formulation이다.",
    "pr-1058": "범용 pick-and-place 성능과 접촉 조립 능력을 구분할 benchmark를 보완한다.",
    "pr-1059": "DataMIL의 subset 선택과 domain-level mixture 최적화를 구분하는 필수 비교군이다.",
    "pr-1060": "여러 embodiment의 데이터를 늘릴 때 실제 시연과 합성 trajectory의 역할을 비교할 자산이다.",
    "pr-1061": "새 RL/VLA 적응 기여를 주장하기 전에 인간 개입·residual 학습으로 설명되는 이득을 대조한다.",
    "pr-1062": "VLA의 video prior가 action supervision을 어떻게 보완하는지 비교할 직접 선행이다.",
    "pr-1063": "NaVILA·NoMaD와 비교할 계층형 VLA navigation 및 환경 사전정보 기준이다.",
    "pr-1064": "다양한 로봇 연구에서 policy 성능과 base의 운동학적 자유도 차이를 구분할 플랫폼 기준이다.",
    "pr-1065": "3D 외관 재구성과 행동에 유용한 물성 모델을 구별할 직접 연결 연구다.",
    "pr-1066": "일반화 이득이 더 큰 VLA보다 대칭성 같은 inductive bias로 설명되는지 대조할 기준이다.",
    "pr-1068": "접촉 VLA의 센서 이득과 상태 추정·feedback controller 이득을 분리할 직접 대안이다."
})
FOCUS_REFERENCE_RATIONALES.update({
    "pr-1067": "언어 기반 skill 조합과 전문가가 명시한 물리적 요구·종료 조건을 비교할 참조다.",
    "pr-1069": "명시적 video model 사용과 정책에 내재한 예측 능력을 구별하는 AI 이론 참조다.",
    "pr-1070": "VLA world model의 시각 품질·정책 순위와 환경 이해를 구분할 평가 방법론이다.",
    "pr-1071": "로봇 시연의 숨은 정보 문제를 단순 모델 불확실성과 혼동하지 않게 하는 방법론 참조다.",
    "pr-1072": "VLA history 추가를 새 해결책으로 주장하기 전에 정보 비대칭과 도구변수 조건을 점검할 선행이다."
})
FOCUS_SOURCE_CHECKS.update({
    "pr-1056": "https://proceedings.mlr.press/v305/atreya25a.html",
    "pr-1057": "https://api.crossref.org/works/10.1109/LRA.2026.3656785",
    "pr-1058": "https://journals.sagepub.com/doi/full/10.1177/02783649241276017",
    "pr-1059": "https://proceedings.mlr.press/v270/hejna25a.html",
    "pr-1060": "https://api.crossref.org/works/10.1109/ICRA55743.2025.11127809",
    "pr-1061": "https://proceedings.mlr.press/v270/jiang25a.html",
    "pr-1062": "https://proceedings.mlr.press/v305/bharadhwaj25a.html",
    "pr-1063": "https://proceedings.mlr.press/v270/xu25b.html",
    "pr-1064": "https://proceedings.mlr.press/v270/wu25a.html",
    "pr-1065": "https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html",
    "pr-1066": "https://journals.sagepub.com/doi/10.1177/02783649261424445",
    "pr-1067": "https://www.nature.com/articles/s42256-025-01045-3",
    "pr-1068": "https://proceedings.mlr.press/v270/ferrandis25a.html",
    "pr-1069": "https://proceedings.mlr.press/v267/richens25a.html",
    "pr-1070": "https://proceedings.mlr.press/v306/warrier26a.html",
    "pr-1071": "https://proceedings.iclr.cc/paper_files/paper/2024/hash/0b9ff9baa226af39f86045ecdc173672-Abstract-Conference.html",
    "pr-1072": "https://proceedings.iclr.cc/paper_files/paper/2026/hash/4415e8cb0741bc0beb79b316f0856108-Abstract-Conference.html"
})
FOCUS_REVIEW_DATES.update(dict.fromkeys((f"pr-{n:04d}" for n in range(1056, 1073)), "2026-10-25"))
FOCUS_SOURCE_CHECKS["pr-0914"] = "https://www.science.org/doi/10.1126/scirobotics.ads5033"
FOCUS_REVIEW_DATES["pr-0914"] = "2026-10-25"

# Active HANDOFF prerequisites, 2026-10-28; preserve all earlier membership.
NEXT_GROUPS["Locomotion, whole-body control, mobile manipulation, and humanoids"].append("=Mobi-π: Mobilizing Your Robot Learning Policy")
NEXT_GROUPS["VLA, cross-embodiment, and long-horizon planning"].append("=Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks")
FOCUS_PRIORITY_RATIONALES.update({
    "pr-1073": "Mobile ALOHA의 whole-body 데이터와 MoTo의 이동–조작 연결을 보완하며, HANDOFF의 정책별 도착 조건을 비교할 직접 선행이다.",
    "pr-1074": "현재 HANDOFF P0의 직접적인 benchmark/source prerequisite다. 전체 task 성공률과 독립 skill 능력의 차이를 읽을 NEXT로 추가하되 preprint status를 유지한다.",
})
FOCUS_SOURCE_CHECKS.update({
    "pr-1073": "https://proceedings.mlr.press/v305/yang25b.html",
    "pr-1074": "https://arxiv.org/abs/2608.30536",
})
FOCUS_REVIEW_DATES.update({"pr-1073": "2026-10-28", "pr-1074": "2026-10-28"})

# Active instruction revision prerequisites, 2026-10-31.
NEXT_GROUPS["VLA, cross-embodiment, and long-horizon planning"].extend([
    "=ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies",
    "=Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies",
    "=Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models",
])
FOCUS_PRIORITY_RATIONALES.update({
    "pr-1075": "현재 부분 지시 수정 후보의 기본 switching 선행이자 최소 실행의 직접 prerequisite다. 단순 task switch나 행동 큐 교체를 신규 기여로 삼지 않도록 NEXT에 추가한다.",
    "pr-1076": "전환 실패를 의미 기억 오류로 오인하지 않기 위한 직접 경쟁 설명이다. 새 목표의 물리적 실행 가능성과 언어 해석을 분리할 NEXT로 추가하며 preprint status를 유지한다.",
    "pr-1077": "현재 제약 유지·철회 후보에서 지시 반응, 목표 성공, 제약 준수를 분리할 직접 진단 선행이다. 평가 정의 자체를 새 기여로 과장하지 않기 위한 NEXT이며 preprint로 둔다.",
})
FOCUS_SOURCE_CHECKS.update({
    "pr-1075": "https://roboticsproceedings.org/rss22/p143.html",
    "pr-1076": "https://arxiv.org/abs/2609.30913",
    "pr-1077": "https://arxiv.org/abs/2610.21251",
})
FOCUS_REVIEW_DATES.update(dict.fromkeys(("pr-1075", "pr-1076", "pr-1077"), "2026-10-31"))


# Active object-set/counting prerequisites, 2026-11-01; preserve prior membership.
NEXT_GROUPS["VLA, cross-embodiment, and long-horizon planning"].extend([
    "=ClevrSkills: Compositional Language And Visual Reasoning in Robotics",
    "=Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models",
])
NEXT_GROUPS["RL, IL, offline learning, and robot data"].extend([
    "=Diagnosing Compositional Generalization in Sequential Robot Tasks",
])
FOCUS_PRIORITY_RATIONALES.update({
    "pr-1078": "VIMA·VLABench와 함께 집합/수량 후보의 기존 조합 task와 평가 predicate를 이해할 NEXT benchmark다. 여러 물체 처리·나열 표현 자체를 새 기여로 삼지 않도록 등록한다.",
    "pr-1079": "집합·수량 후보의 가장 직접적인 counting/직접 지시 비교 선행이다. 알려진 공간 grounding 실패를 새 공백으로 과장하지 않도록 NEXT에 등록하며 preprint 경계를 유지한다.",
    "pr-1080": "DataMIL·ReMix의 데이터 선택 흐름과 SET의 단순 분해를 연결할 instruction-coverage 선행이다. 분해 자체를 신규 기여로 주장하지 않고 학습 support를 따질 NEXT로 등록한다.",
})
FOCUS_SOURCE_CHECKS.update({
    "pr-1078": "https://proceedings.neurips.cc/paper_files/paper/2024/hash/439539557e9ba0d04055773ff1f3241c-Abstract-Datasets_and_Benchmarks_Track.html",
    "pr-1079": "https://arxiv.org/abs/2610.12696",
    "pr-1080": "https://arxiv.org/abs/2607.29687",
})
FOCUS_REVIEW_DATES.update(dict.fromkeys(("pr-1078", "pr-1079", "pr-1080"), "2026-11-01"))

# 2026-11-02 official top-tier supplement; 9 NEXT / 1 REFERENCE.
NEXT_GROUPS["VLA, cross-embodiment, and long-horizon planning"].extend([
    "=RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models",
    "=Scaling up Memory for Robotic Control via Experience Retrieval",
    "=LIBERO-X: Robustness Litmus for Vision-Language-Action Models",
    "=Learning Native Continuation for Action Chunking Flow Policies",
    "=Stable Language Guidance for Vision–Language–Action Models",
])
NEXT_GROUPS["RL, IL, offline learning, and robot data"].extend([
    "=A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation",
    "=Emergence of Human to Robot Transfer in Vision-Language-Action Models",
    "=Dejavu: Towards Experience Feedback Learning for Embodied Intelligence",
])
NEXT_GROUPS["Locomotion, whole-body control, mobile manipulation, and humanoids"].extend([
    "=SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding",
])
FOCUS_PRIORITY_RATIONALES.update({
    "pr-1081": "OpenVLA·π0 계열의 후학습과 시연 검색을 잇는 직접 선행이다. 현재 bank 확장 질문에서 이미 알려진 ICL 능력·검색 이득을 신규성으로 재주장하지 않도록 NEXT로 등록한다.",
    "pr-1082": "MemoryVLA와 계층 정책의 관계를 구체화하는 NEXT다. 외부 시연 검색과 실행 중 기억을 구분하고 SET의 counting 선행을 보완한다.",
    "pr-1083": "LIBERO·LIBERO-Plus·VLABench 이후 복합 shift와 목표 다양성을 비교할 NEXT benchmark다. 같은 scene의 다른 goal을 다루는 연구에서 기존 평가 범위를 확인하는 데 필요하다.",
    "pr-1084": "Open X-Embodiment·DataMIL·ReMix 이후 데이터 양과 종류의 효과를 분리하는 NEXT 실증 기준이다. 새로운 아키텍처보다 데이터 구성이라는 단순 대안을 먼저 검토하게 한다.",
    "pr-1085": "Open X-Embodiment와 사람 영상 기반 로봇 학습을 잇는 NEXT 데이터 조건 연구다. Cross-embodiment 전이를 보편적 성질로 가정하지 않도록 비교 기준을 추가한다.",
    "pr-1086": "ACT·Diffusion Policy와 RTC 이후 action interface를 이해할 NEXT다. Chunk queue나 지연으로 생긴 차이를 새로운 지시 이해/검색 효과로 혼동하지 않게 한다.",
    "pr-1087": "Residual RL과 retrieval의 직접 결합이므로 NEXT에 추가한다. Bank 성장·frozen backbone이라는 조합 자체를 새 연구 공백으로 주장하지 않도록 현재 후보의 선행 경계를 보완한다.",
    "pr-1088": "VoxPoser·Mobile ALOHA와 구조적 3D grounding을 잇는 NEXT다. 다양한 로봇을 다룬다는 목표에서 의미 표현과 embodiment별 제어의 경계를 비교한다.",
    "pr-1089": "지시 수정·집합 지시·시연 검색 후보가 공유하는 언어 민감성의 NEXT 직접 대안이다. 같은 의미의 표현 차이를 새로운 task conflict로 해석하지 않도록 등록한다.",
})
FOCUS_SOURCE_CHECKS.update({
    "pr-1081": "https://proceedings.mlr.press/v305/sridhar25a.html",
    "pr-1082": "https://proceedings.iclr.cc/paper_files/paper/2026/hash/9da515b1ad19d032a7398f00f5ff9b0c-Abstract-Conference.html",
    "pr-1083": "https://roboticsproceedings.org/rss22/p097.html",
    "pr-1084": "https://roboticsproceedings.org/rss22/p007.html",
    "pr-1085": "https://roboticsproceedings.org/rss22/p072.html",
    "pr-1086": "https://roboticsproceedings.org/rss22/p058.html",
    "pr-1087": "https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.html",
    "pr-1088": "https://ieeexplore.ieee.org/document/11568510/",
    "pr-1089": "https://aclanthology.org/2026.acl-long.190/",
})
FOCUS_REVIEW_DATES.update(dict.fromkeys(("pr-1081", "pr-1082", "pr-1083", "pr-1084", "pr-1085", "pr-1086", "pr-1087", "pr-1088", "pr-1089"), "2026-11-02"))


# 2026-11-03 direct residual RL prerequisites; 7 NEXT, Q-filter foundation REFERENCE.
NEXT_GROUPS["VLA, cross-embodiment, and long-horizon planning"].extend([
    "=Self-Improving Vision-Language-Action Models with Data Generation via Residual RL",
    "=Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement",
    "=EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models",
])
NEXT_GROUPS["RL, IL, offline learning, and robot data"].extend([
    "=EXPO: Stable Reinforcement Learning with Expressive Policies",
    "=Policy Decorator: Model-Agnostic Online Refinement for Large Policy Model",
    "=Accelerating Residual Reinforcement Learning With Uncertainty Estimation",
    "=From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning",
])
FOCUS_PRIORITY_RATIONALES.update({
    "pr-1091": "VLA의 residual 개선→데이터 생성→base 갱신을 잇는 직접 선행이다. 현재 후보에서 이 루프 자체를 새 기여로 주장하지 않도록 NEXT에 추가한다.",
    "pr-1092": "Object-centric residual의 전이를 이미 다룬 직접 충돌 선행이다. 다양한 로봇·base 갱신 전이와 sim-to-real 전이를 구분할 NEXT다.",
    "pr-1093": "Residual/editor와 value 선택을 결합한 강한 직접 baseline이다. Q 선택·base 모방·editor RL이라는 조합 자체의 신규성 주장을 막는 NEXT다.",
    "pr-1094": "현재 VLA+RL 후보의 가장 가까운 공동 적응 baseline이다. 독립 base 갱신과 editor 공동 학습을 구별할 NEXT다.",
    "pr-1095": "Frozen large policy+bounded residual의 핵심 비교 선행이다. 현재 후보의 scalar gain·탐색 schedule이라는 단순 대안을 놓치지 않도록 NEXT에 추가한다.",
    "pr-1096": "현재 후보의 critic mismatch 대안을 검토할 직접 선행이다. 합성 행동 critic을 새 알고리즘으로 재주장하지 않도록 NEXT에 등록한다.",
    "pr-1098": "Frozen prior+residual+선택적 모방의 최신 직접 선행이다. 현재 후보의 규칙 조합만으로 독립 방법 기여를 주장하지 않도록 NEXT에 추가한다.",
})
FOCUS_SOURCE_CHECKS.update({
    "pr-1091": "https://iclr.cc/virtual/2026/poster/10008318",
    "pr-1092": "https://www.corl.org/program/accepted-papers",
    "pr-1093": "https://proceedings.iclr.cc/paper_files/paper/2026/hash/d56a652ad743308b24b6c4d0e6411dd7-Abstract-Conference.html",
    "pr-1094": "https://www.corl.org/program/accepted-papers",
    "pr-1095": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c361d4117d598d4bb6568b407e9ac9-Abstract-Conference.html",
    "pr-1096": "https://api.crossref.org/works/10.1109/LRA.2025.3636808",
    "pr-1098": "https://proceedings.mlr.press/v306/sun26al.html",
})
FOCUS_REVIEW_DATES.update({
    "pr-1091": "2026-11-03",
    "pr-1092": "2026-11-03",
    "pr-1093": "2026-11-03",
    "pr-1094": "2026-11-03",
    "pr-1095": "2026-11-03",
    "pr-1096": "2026-11-03",
    "pr-1098": "2026-11-03",
})

# Publication update retains paper identity and reading inputs.
FOCUS_REFERENCE_RATIONALES["pr-1097"] = "선택적 Q 기반 imitation의 직접 기원으로 REFERENCE에 추가한다. 2024–2026 최신 동향 수에는 포함하지 않으며 기존 SAC/DDPG 기반 읽기 흐름을 보완한다."
FOCUS_SOURCE_CHECKS["pr-1097"] = "https://api.crossref.org/works/10.1109/ICRA.2018.8463162"
FOCUS_REVIEW_DATES["pr-1097"] = "2026-11-03"
FOCUS_SOURCE_CHECKS["pr-1080"] = "https://www.corl.org/program/accepted-papers"
FOCUS_REVIEW_DATES["pr-1080"] = "2026-11-03"

# 2026-11-05 integrated review: current six topics and two exploratory questions.
NEXT_GROUPS["VLA, cross-embodiment, and long-horizon planning"].extend([
    "=Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models",
    "=Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models",
    "=Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models",
    "=RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models",
    "=CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy",
    "=Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning",
    "=RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation",
    "=When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models",
    "=Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?",
])
NEXT_GROUPS["RL, IL, offline learning, and robot data"].extend([
    "=Latent Theory of Mind: A Decentralized Diffusion Architecture for Cooperative Manipulation",
])
NEXT_GROUPS["World models, uncertainty, failure detection, and recovery"].extend([
    "=DRILL: Training World Models to Improve Policies, Not Predict Pixels",
])
FOCUS_PRIORITY_RATIONALES.update({
    "pr-1099": "REVISION·FEEDBACK·residual 보정의 직접 충돌 선행. 변화에 반응하고 nuisance에 불변이라는 broad proposal의 재발명을 막는다.",
    "pr-1100": "FEEDBACK의 출발 근거이자 과장 방지 선행. Activation replay 결과와 자연 정책의 closed-loop 행동을 구별하는 NEXT.",
    "pr-1101": "FEEDBACK에서 attribution 자체를 새 기여로 주장하지 않도록 하는 직접 진단 baseline.",
    "pr-1102": "FEEDBACK에서 단순 Jacobian 억제·강건 RL을 새 방법으로 제안하지 않도록 하는 직접 비교.",
    "pr-1103": "CROSSPLAY의 decentralized 협력·상대 행동 모델링은 이미 존재함을 보여 주는 CoRL 직접 선행.",
    "pr-1104": "CROSSPLAY에서 여러 embodiment·local-only 협력 자체를 새 기여로 주장하지 않도록 하는 직접 선행.",
    "pr-1105": "CROSSPLAY에서 VLA+MARL 결합 자체의 신규성을 배제하는 가장 가까운 RL 선행.",
    "pr-1106": "World-model utility라는 broad gap의 직접 충돌을 registry에 남겨 같은 제안을 반복하지 않도록 한다.",
    "pr-1107": "RETRIEVAL 후보의 semantic retrieval·execution 결합이라는 넓은 주장이 이미 존재함을 확인하는 ICML 직접 선행.",
    "pr-1108": "RETRIEVAL의 가장 직접적인 진단 선행으로, 단순 cross-task interference 발견만으로 기여를 주장하지 않게 한다.",
    "pr-1109": "CODEC1의 broad motivation과 prefix/replanning confound를 가장 직접적으로 제한하는 선행.",
})
FOCUS_REFERENCE_RATIONALES.update({
    "pr-1110": "FEEDBACK의 표현/행동 연결 진단 도구로 REFERENCE에 보존한다. 기존 mechanistic NEXT와 중복되는 도구 축이며 현재 학습 메커니즘의 직접 검증은 아니다.",
})
FOCUS_SOURCE_CHECKS.update({
    "pr-1099": "https://neurips.cc/Downloads/2026",
    "pr-1100": "https://neurips.cc/Downloads/2026",
    "pr-1101": "https://proceedings.mlr.press/v306/zhang26gz.html",
    "pr-1102": "https://arxiv.org/abs/2511.01331",
    "pr-1103": "https://proceedings.mlr.press/v305/he25a.html",
    "pr-1104": "https://arxiv.org/abs/2606.12352",
    "pr-1105": "https://arxiv.org/abs/2609.36588",
    "pr-1106": "https://neurips.cc/Downloads/2026",
    "pr-1107": "https://proceedings.mlr.press/v306/jang26c.html",
    "pr-1108": "https://arxiv.org/abs/2610.05492",
    "pr-1109": "https://arxiv.org/abs/2610.09170",
    "pr-1110": "https://aclanthology.org/2026.emnlp-main.2076/",
})
FOCUS_REVIEW_DATES.update({
    "pr-1099": "2026-11-05",
    "pr-1100": "2026-11-05",
    "pr-1101": "2026-11-05",
    "pr-1102": "2026-11-05",
    "pr-1103": "2026-11-05",
    "pr-1104": "2026-11-05",
    "pr-1105": "2026-11-05",
    "pr-1106": "2026-11-05",
    "pr-1107": "2026-11-05",
    "pr-1108": "2026-11-05",
    "pr-1109": "2026-11-05",
    "pr-1110": "2026-11-05",
})

# 2026-11-08 REG-R12: official 2024–2026 proceedings supplement.
NEXT_GROUPS['RL, IL, offline learning, and robot data'].extend(['=PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies', '=MolmoSpaces: Large-Scale Open Ecosystem for Robot Manipulation and Navigation', '=When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning', '=Long-Context Robot Imitation Learning by Focusing on Key History Frames', '=TMRL: Diffusion Timestep-Modulated Pretraining Enables Exploration for Efficient Policy Finetuning', '=ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations', '=CoMo: Learning Continuous Latent Motion from Internet Videos for Scalable Robot Learning', '=General Process Reward Modeling for Robotic Reinforcement Learning', '=Lifelong Autonomous Improvement of Navigation Foundation Models in the Wild', '=Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance', '=DEAS: DEtached value learning with Action Sequence for Scalable Offline RL', '=PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models'])
NEXT_GROUPS['VLA, cross-embodiment, and long-horizon planning'].extend(['=LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation', '=Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement', '=Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning', '=LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion', '=ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models', '=SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models', '=Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild', '=RehearseVLA: Simulated Post-Training for VLAs with Physically-Consistent World Model', '=Contrast Sets for Evaluating Language-Guided Robot Policies', '=Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning', '=MM-ACT: Learn from Multimodal Parallel Generation to Act', '=EvoVLA: Self-evolving Vision-Language-Action Model', '=Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration', '=VLA-R1: Enhancing Reasoning in Vision-Language-Action Models', '=MobileVLA-R1: Reinforcing Vision-Language-Action for Mobile Robots', '=Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment', '=GRAD-NAV++: Vision-Language Model Enabled Visual Drone Navigation With Gaussian Radiance Fields and Differentiable Dynamics'])
NEXT_GROUPS['Contact-rich, deformable, force, and dexterous manipulation'].extend(['=Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation', '=Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning'])
NEXT_GROUPS['Planning, control, simulation, and TAMP extensions'].extend(['=KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning'])
NEXT_GROUPS['Locomotion, whole-body control, mobile manipulation, and humanoids'].extend(['=MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation'])
FOCUS_PRIORITY_RATIONALES.update({
    'pr-1118': 'SIMPLER·RoboCasa의 점수를 실제 개선으로 해석하기 전 필요한 평가 타당성 비교다.',
    'pr-1119': '조작에서 설계한 VLA+RL 목적함수가 항법의 긴 시간축에도 유효한지 비교할 직접 선행이다.',
    'pr-1120': 'RL 자체의 기여를 주장할 때 반드시 비교할 자율 데이터 선택·모방 대안이다.',
    'pr-1121': '환경 return 최적화와 참조 행동 기반 RLVR을 구별하기 위한 직접 비교다.',
    'pr-1122': '현재 후보의 한 benchmark 의존을 줄일 추가 환경·데이터 자원이다.',
    'pr-1124': 'Unified VLA의 접촉 기여가 분리된 고주파 힘 제어보다 나은지 판단할 비교 기준이다.',
    'pr-1125': 'BC prior 보존을 새 unified objective 없이 달성하는 강한 대안이다.',
    'pr-1126': 'VLA의 실패가 언어 표현 문제인지 물리적 의사결정 문제인지 진단할 자원이다.',
    'pr-1127': 'VLA memory를 늘리는 것과 필요한 정보만 남기는 것의 차이를 검증할 직접 선행이다.',
    'pr-1128': 'VLA 내부 학습을 제안할 때 비교해야 할 사전학습 coverage·탐색 조절 대안이다.',
    'pr-1129': '단일 모델의 행동·세계 예측 공유를 새 기여로 제안하기 전에 비교할 핵심 구조다.',
    'pr-1130': '새 VLA-RL 보상이나 실패 재사용이 기존 언어 보상 일반화와 어떻게 다른지 비교할 선행이다.',
    'pr-1131': 'RL이 반드시 필요한지를 판단할 저데이터 SFT·표현 적응 비교다.',
    'pr-1133': 'HINDSIGHT의 실패 재사용이 이미 존재하는 self-reference reward shaping과 다른지 검토할 직접 선행이다.',
    'pr-1134': 'Unified VLA-RL의 action representation 기여를 판단할 사전학습 비교 기준이다.',
    'pr-1135': '행동 공간의 통합이 discrete/continuous 선택 자체의 효과인지 분리할 비교다.',
    'pr-1136': 'VLA+RL 보상 설계와 HINDSIGHT의 대안 설명을 검토할 직접 선행이다.',
    'pr-1137': 'VLAW 등과 함께 imagined rollout으로 실제 interaction을 대체하는 직접 비교 기준이다.',
    'pr-1138': 'VLA+RL을 manipulation과 navigation에 통합할 때 성공 조건을 구체화하는 benchmark다.',
    'pr-1140': 'VLA+RL의 지속 학습을 manipulation에 한정하지 않고 실제 항법 운영 조건과 비교할 기준이다.',
    'pr-1141': 'VLA+RL 개선이 언어 민감도까지 바꾸는지 적은 실행으로 진단할 평가 설계의 선행이다.',
    'pr-1143': '단일 정책을 RL로 갱신하는 방법이 추론 후보 선택보다 필요한 이유를 검증할 직접 대조군이다.',
    'pr-1144': 'Chunk-aware actor-critic과 공유 표현 연구에서 반드시 넘어야 하는 직접 offline RL 선행이다.',
    'pr-1146': 'VLA-RL의 탐색 개선이 정책 방법보다 reset coverage에서 오는지 분리할 중요한 대조군이다.',
    'pr-1148': 'Hindsight 재사용과 foundation reward 결합이 이미 연구되었음을 보여 주는 비교 선행이다.',
    'pr-1151': 'RL reasoning의 이득을 긴 텍스트 출력 없이 행동에 전달하는 대안으로 비교한다.',
    'pr-1152': '하나의 VLA 내부 통합을 설계할 architecture 선행이며 RL objective 통합 효과로 해석하지 않는다.',
    'pr-1154': 'VLA+RL 보상 개선에서 이미 다룬 near-miss 구분과 실제 물리 완료의 선행이다.',
    'pr-1155': 'RL 이후 성공률이 언어 grounding을 보장하지 않는다는 직접 평가·간단 대안이다.',
    'pr-1156': 'VLA의 RL이 환경 return이 아닌 검증 가능한 중간 출력 보상일 때의 직접 비교 기준이다.',
    'pr-1157': 'Manipulation 외에 단일 VLA 후학습을 검토할 모바일 로봇 선행이다.',
    'pr-1158': '정책 RL 갱신의 필요성을 검증할 강한 추론 계산량·검증 대안이다.',
    'pr-1161': '언어·시각·행동과 differentiable RL을 결합한 직접 항법 선행이다. 기존 GRaD-Nav의 언어 조건부 확장이라 별도 등록한다.',
})
FOCUS_REFERENCE_RATIONALES.update({
    'pr-1123': '새 VLA-RL 구조의 필요성을 판단할 때 참고할 강한 off-policy 학습 baseline이다.',
    'pr-1132': '항법 VLA-RL에 인간 선호 보상을 붙일 때 참고할 구체적 reward-learning 대안이다.',
    'pr-1139': '행동 표현을 통합하는 연구에서 object motion과 robot motion의 차이를 보존할 대안이다.',
    'pr-1142': '단일 VLA 내부 RL이 계층형 분해보다 어떤 비용·일반화 이점을 주는지 비교하는 시스템 대안이다.',
    'pr-1145': 'Diffusion RL 안정화의 알고리즘 대안으로 참고하며 로봇 조작 효과는 별도 검증한다.',
    'pr-1147': 'Cross-embodiment VLA-RL의 필요성을 검증할 기하 prior+동역학 적응 기준이다.',
    'pr-1149': '시각 VLA에 촉각을 넣기 전에 입력 유용성과 표현 학습을 분리할 진단 자원이다.',
    'pr-1150': 'VLA policy RL과 world model RL을 구분하며 예측 개선이 행동에 전달되는지 물을 비교 자료다.',
    'pr-1153': '적응을 RL update 없이 해결하는 비교 대안으로 등록한다.',
    'pr-1159': 'VLA-RL 성능 병목이 reward보다 공간 지각에 있을 때 비교할 표현 대안이다.',
    'pr-1160': '정책 내부 표현·미래 예측이 항법에 주는 효과를 RL 기여와 분리할 기준이다.',
})
FOCUS_SOURCE_CHECKS.update({
    'pr-1118': 'https://roboticsproceedings.org/rss22/p062.html',
    'pr-1119': 'https://roboticsproceedings.org/rss22/p068.html',
    'pr-1120': 'https://roboticsproceedings.org/rss22/p079.html',
    'pr-1121': 'https://roboticsproceedings.org/rss22/p086.html',
    'pr-1122': 'https://roboticsproceedings.org/rss22/p091.html',
    'pr-1123': 'https://roboticsproceedings.org/rss22/p099.html',
    'pr-1124': 'https://roboticsproceedings.org/rss22/p128.html',
    'pr-1125': 'https://roboticsproceedings.org/rss22/p153.html',
    'pr-1126': 'https://roboticsproceedings.org/rss22/p184.html',
    'pr-1127': 'https://roboticsproceedings.org/rss22/p201.html',
    'pr-1128': 'https://roboticsproceedings.org/rss22/p208.html',
    'pr-1129': 'https://roboticsproceedings.org/rss22/p210.html',
    'pr-1130': 'https://proceedings.mlr.press/v305/zhang25a.html',
    'pr-1131': 'https://proceedings.mlr.press/v305/li25c.html',
    'pr-1132': 'https://proceedings.mlr.press/v305/seneviratne25a.html',
    'pr-1133': 'https://openaccess.thecvf.com/content/CVPR2026/html/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.html',
    'pr-1134': 'https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild_CVPR_2026_paper.html',
    'pr-1135': 'https://openaccess.thecvf.com/content/CVPR2026/html/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.html',
    'pr-1136': 'https://openaccess.thecvf.com/content/CVPR2026/html/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.html',
    'pr-1137': 'https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html',
    'pr-1138': 'https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.html',
    'pr-1139': 'https://openaccess.thecvf.com/content/ICCV2025/html/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.html',
    'pr-1140': 'https://proceedings.mlr.press/v270/stachowicz25a.html',
    'pr-1141': 'https://proceedings.mlr.press/v270/anwar25a.html',
    'pr-1142': 'https://proceedings.mlr.press/v270/zhou25a.html',
    'pr-1143': 'https://proceedings.mlr.press/v270/nakamoto25a.html',
    'pr-1144': 'https://proceedings.iclr.cc/paper_files/paper/2026/hash/68b7f71467c83d5d32275c5acbf6b588-Abstract-Conference.html',
    'pr-1145': 'https://proceedings.iclr.cc/paper_files/paper/2026/hash/64a0192102e1421a2b2c15ae0bdb9f3a-Abstract-Conference.html',
    'pr-1146': 'https://proceedings.iclr.cc/paper_files/paper/2026/hash/8e3e3488623d64c493a7f11cf1f2e49f-Abstract-Conference.html',
    'pr-1147': 'https://proceedings.iclr.cc/paper_files/paper/2026/hash/514bdfb12b318ad02c6f28dc68f2feea-Abstract-Conference.html',
    'pr-1148': 'https://proceedings.neurips.cc/paper_files/paper/2025/hash/e0d760e4495abf701b97c8acda111372-Abstract-Conference.html',
    'pr-1149': 'https://proceedings.neurips.cc/paper_files/paper/2025/hash/bc09efb501c801ed92e181e26a885c2d-Abstract-Conference.html',
    'pr-1150': 'https://proceedings.neurips.cc/paper_files/paper/2025/hash/b63a24a1832bd14fa945c71f535c0095-Abstract-Conference.html',
    'pr-1151': 'https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Fast-ThinkAct_Efficient_Vision-Language-Action_Reasoning_via_Verbalizable_Latent_Planning_CVPR_2026_paper.html',
    'pr-1152': 'https://openaccess.thecvf.com/content/CVPR2026/html/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.html',
    'pr-1153': 'https://link.springer.com/chapter/10.1007/978-3-032-37531-5_16',
    'pr-1154': 'https://link.springer.com/chapter/10.1007/978-3-032-37023-5_14',
    'pr-1155': 'https://link.springer.com/chapter/10.1007/978-3-032-37152-2_3',
    'pr-1156': 'https://eccv.ecva.net/Conferences/2026/AcceptedPapers',
    'pr-1157': 'https://eccv.ecva.net/Conferences/2026/AcceptedPapers',
    'pr-1158': 'https://eccv.ecva.net/Conferences/2026/AcceptedPapers',
    'pr-1159': 'https://ieeexplore.ieee.org/document/11661761/',
    'pr-1160': 'https://ieeexplore.ieee.org/document/11673313/',
    'pr-1161': 'https://ieeexplore.ieee.org/document/11297793/',
})
FOCUS_REVIEW_DATES.update(dict.fromkeys(['pr-1118', 'pr-1119', 'pr-1120', 'pr-1121', 'pr-1122', 'pr-1123', 'pr-1124', 'pr-1125', 'pr-1126', 'pr-1127', 'pr-1128', 'pr-1129', 'pr-1130', 'pr-1131', 'pr-1132', 'pr-1133', 'pr-1134', 'pr-1135', 'pr-1136', 'pr-1137', 'pr-1138', 'pr-1139', 'pr-1140', 'pr-1141', 'pr-1142', 'pr-1143', 'pr-1144', 'pr-1145', 'pr-1146', 'pr-1147', 'pr-1148', 'pr-1149', 'pr-1150', 'pr-1151', 'pr-1152', 'pr-1153', 'pr-1154', 'pr-1155', 'pr-1156', 'pr-1157', 'pr-1158', 'pr-1159', 'pr-1160', 'pr-1161'], "2026-11-08"))

# 2026-11-09 REG-R13: contact-adaptation prerequisites; abstract evidence only.
NEXT_GROUPS['VLA, cross-embodiment, and long-horizon planning'].extend(['=TacCoRL: Integrating Tactile Feedback into VLA via Simulation', '=CompVLA: A Variable Compliance Vision-Language-Action Model for Contact-rich Manipulation', '=TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation', '=ForceRFT: Refining VLA Actions through Force-Guided Residual Reinforcement Learning', '=Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation', '=πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models'])
NEXT_GROUPS['Contact-rich, deformable, force, and dexterous manipulation'].extend(['=FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation Under Uncertainty', '=ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation'])
FOCUS_PRIORITY_RATIONALES.update({'pr-1162': '촉각 추가와 단일 VLA RL 자체가 이미 선행임을 확인할 직접 비교다.', 'pr-1163': '강성 출력을 VLA에 추가하는 것 자체의 신규성을 배제할 직접 선행이다.', 'pr-1164': '접촉 VLA의 online RL과 사람 개입 credit 처리가 이미 다뤄졌음을 확인할 비교다.', 'pr-1165': 'RL 이득이 성공 데이터 선택·추가 imitation으로 설명되는지 판단할 직접 선행이다.', 'pr-1166': 'VLA의 추가 복잡도 전에 넘어야 할 비-VLA 접촉 RL 기준선이다.', 'pr-1167': '접촉 일반화 질문을 구체적인 물리 변화와 재현 자산으로 정의할 benchmark다.', 'pr-1168': 'Action–wrench 예측·가치·RL 결합 자체의 중복을 점검할 직접 경쟁 선행이다.', 'pr-1171': '현재 π₀ Flow-SDE/PPO backend의 likelihood·탐색 정의를 이해할 직접 prerequisite다.'})
FOCUS_REFERENCE_RATIONALES.update({'pr-1169': '동작·강성 공동 RL 자체가 새롭지 않음을 보이는 controller 비교 자료다.', 'pr-1170': '단일 VLA RL 이전에 비교할 학습 없는 context/force 기반 controller 대안이다.'})
FOCUS_SOURCE_CHECKS.update({'pr-1162': 'https://arxiv.org/abs/2606.11743', 'pr-1163': 'https://arxiv.org/abs/2609.23614', 'pr-1164': 'https://arxiv.org/abs/2606.09337', 'pr-1165': 'https://arxiv.org/abs/2609.22840', 'pr-1166': 'https://api.crossref.org/works/10.1109/LRA.2025.3551637', 'pr-1167': 'https://arxiv.org/abs/2610.24512', 'pr-1168': 'https://arxiv.org/abs/2609.01596', 'pr-1169': 'https://arxiv.org/abs/2609.13516', 'pr-1170': 'https://arxiv.org/abs/2601.15541', 'pr-1171': 'https://arxiv.org/abs/2510.25889'})
FOCUS_REVIEW_DATES.update(dict.fromkeys(['pr-1162', 'pr-1163', 'pr-1164', 'pr-1165', 'pr-1166', 'pr-1167', 'pr-1168', 'pr-1169', 'pr-1170', 'pr-1171'], "2026-11-09"))

# 2026-11-12 REG-R14: register cited retention/timing/memory prerequisites; abstract evidence.
NEXT_GROUPS['RL, IL, offline learning, and robot data'].extend(["=RL's Razor: Why Online Reinforcement Learning Forgets Less"])
NEXT_GROUPS['VLA, cross-embodiment, and long-horizon planning'].extend(['=Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training', '=TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models', '=When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs', '=Trajectory-Level Continuous Action Representation for Robotic Manipulation', "=Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies"])
FOCUS_PRIORITY_RATIONALES.update({'pr-1172': 'RL이 지시 능력을 잃는다는 가정을 먼저 반박할 직접 선행이며 KL 진단의 기준이다.', 'pr-1173': '단순히 지시 보존·semantic freezing을 도입하는 것을 새 연구 기여로 주장하지 않도록 한다.', 'pr-1174': '단일 VLA 내부의 의미 보존과 모듈별 RL 갱신에 관한 직접 경쟁 선행이다.', 'pr-1175': 'LANGRET의 공개 장면·지시쌍·평가기 source이며 기존 counterfactual benchmark와의 중복을 드러낸다.', 'pr-1176': '제어 간격·물리 시간 조건부 행동 표현 자체를 새 공백으로 오인하지 않게 하는 기준이다.', 'pr-1179': '기억의 시간 편향 진단과 사건 기반 index가 이미 선행임을 반영할 직접 반대 근거다.'})
FOCUS_REFERENCE_RATIONALES.update({'pr-1177': '제어 주기 학습 전에 넘어야 할 학습 없는 실행 대안이며 예비 timing 질문의 비교 자료다.', 'pr-1178': '행동 이력 memory의 강한 비교 자료이며 결과 기반 기억이라는 질문의 기존 대안을 구체화한다.'})
FOCUS_SOURCE_CHECKS.update({'pr-1172': 'https://proceedings.iclr.cc/paper_files/paper/2026/hash/618c95f4557c15b253fb0e6f548ea0c0-Abstract-Conference.html', 'pr-1173': 'https://arxiv.org/abs/2604.23121', 'pr-1174': 'https://arxiv.org/abs/2608.07314', 'pr-1175': 'https://arxiv.org/abs/2602.17659', 'pr-1176': 'https://link.springer.com/chapter/10.1007/978-3-032-37369-4_24', 'pr-1177': 'https://arxiv.org/abs/2611.01390', 'pr-1178': 'https://arxiv.org/abs/2609.37307', 'pr-1179': 'https://arxiv.org/abs/2611.14488'})
FOCUS_REVIEW_DATES.update(dict.fromkeys(['pr-1172', 'pr-1173', 'pr-1174', 'pr-1175', 'pr-1176', 'pr-1177', 'pr-1178', 'pr-1179'], "2026-11-12"))

# 2026-11-12 REG-R15: foundational missing links and current VLA/robotics prerequisites.
_rl_foundations = CORE_GROUPS["RL, IL, and policy learning foundations"]
_rl_foundations.insert(
    _rl_foundations.index("=Proximal Policy Optimization Algorithms"),
    "=High-Dimensional Continuous Control Using Generalized Advantage Estimation",
)
_rl_foundations[1:1] = [
    "=Policy invariance under reward transformations: Theory and application to reward shaping",
    "=Universal Value Function Approximators",
]
NEXT_GROUPS["RL, IL, offline learning, and robot data"].extend(["=Successor Features for Transfer in Reinforcement Learning","=AWAC: Accelerating Online Reinforcement Learning with Offline Datasets","=DART: Noise Injection for Robust Imitation Learning","=Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning","=HIQL: Offline Goal-Conditioned RL with Latent States as Actions","=Is Value Learning Really the Main Bottleneck in Offline RL?","=Horizon Reduction Makes RL Scalable"])
NEXT_GROUPS["VLA, cross-embodiment, and long-horizon planning"].extend(["=Act2Goal: From World Model To General Goal-conditioned Policy","=AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation","=WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning","=Reinforcement Learning for Real-Time Vision-Language-Action Policies","=RoboAlign: Learning Test-Time Reasoning for Language-Action Alignment in Vision-Language-Action Models","=STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models"])
NEXT_GROUPS["World models, uncertainty, failure detection, and recovery"].extend(["=Causal World Modeling for Robot Control","=Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation"])
NEXT_GROUPS["Contact-rich, deformable, force, and dexterous manipulation"].extend(["=Tune to Learn: How Controller Gains Shape Robot Policy Learning"])
FOCUS_PRIORITY_RATIONALES.update({"pr-1180":"PPO 기반 VLA RL에서 advantage·bootstrap·시간 단위가 학습에 미치는 영향을 해석하기 위한 공통 원전이므로 CORE다.","pr-1181":"VLM progress·단계 보상·접촉 보상으로 목표를 변경하는지 판단할 공통 이론 원전이므로 CORE다.","pr-1182":"HER·HIQL·목표 조건부 critic과 단일 VLA의 지시별 가치 표현을 이해하는 원전이므로 CORE다.","pr-1183":"보상 전이와 로봇 동역학 전이를 혼동하지 않게 하는 명확한 이론·로봇 비교 기준이다.","pr-1184":"RL 이득이 성공 선택이나 weighted imitation으로 설명되는지 비교할 핵심 baseline이다.","pr-1186":"복구 성공을 RL 고유 이득으로 해석하기 전 넘어야 할 강한 데이터 수집·모방 대안이다.","pr-1190":"초기 성능 손실을 semantic forgetting으로만 설명하지 않게 하는 critic calibration baseline이다.","pr-1191":"공유 가치함수와 계층 정책을 단일 actor 공동 학습과 구별하고 장기 credit 문제의 강한 대안으로 비교한다.","pr-1192":"단일 VLA critic 개선 후보가 actor 학습·coverage 효과를 놓치지 않도록 하는 핵심 원인 분석이다.","pr-1193":"Chunk 길이·목표 분해와 데이터 scaling의 효과를 분리할 최신 기준 연구다.","pr-1195":"Hindsight 목표 변경·world model·단일 정책 연결의 직접 선행이며 언어 VLA와 시각 목표 정책의 경계를 드러낸다.","pr-1196":"Architecture 통합과 RL 공동 갱신을 구별할 world-action 비교 대상으로 보완한다.","pr-1197":"접촉 VLA RL의 이득을 baseline gain 튜닝과 분리해야 함을 보이는 직접 선행이다.","pr-1198":"실험 rollout 종료와 실제 실패를 구별하고 가치 진단의 target을 정할 최신 기준이다.","pr-1199":"RL 기반 시간 적응과 비교할 학습된 계산 절감 baseline이며 지연·feedback·성능의 비용 분리를 돕는다.","pr-1200":"공유 표현·가치 공동 학습 후보의 직접 경쟁 선행이므로 단순 world-model 보조 loss를 신규 기여로 재제안하지 않게 한다.","pr-1201":"지연·feedback 공백의 직접 선행이자 단일 정책 선호와 별도로 보존할 강한 editor pipeline baseline이다.","pr-1202":"VLM의 RL 정렬과 배포 VLA의 직접 RL 갱신을 구분할 선행으로 단일 정책 연구의 기여 경계를 보완한다.","pr-1203":"단계별 credit·보상 shaping 자체가 기존 방법임을 반영하고 원 보상 보존·추가 supervision을 비교하는 직접 선행이다."})
FOCUS_REFERENCE_RATIONALES.update({"pr-1185":"TRPO·MPO·KL 제약의 개념 계보를 보완할 원전이며 현재 공통 정독은 GAE/PPO를 우선한다.","pr-1187":"가변 chunk·재계획·중단을 해석할 기본 formulation을 보완하며 계층형 주제로 전환하라는 의미는 아니다.","pr-1188":"로봇 문제의 제약에서 연구 질문을 세우기 위한 기반 survey로 최신 VLA 방법의 전제 점검에 필요하다.","pr-1189":"CQL·IQL·Cal-QL의 데이터 조건과 결과를 읽기 위한 표준 benchmark의 누락을 보완한다.","pr-1194":"석사 연구 후보의 구현 부담과 로봇 행동 기여를 평가할 최신 survey로 2013 원전과 함께 사용한다."})
FOCUS_SOURCE_CHECKS.update({"pr-1180":"https://arxiv.org/abs/1506.02438","pr-1181":"https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf","pr-1182":"https://proceedings.mlr.press/v37/schaul15.html","pr-1183":"https://proceedings.neurips.cc/paper/2017/hash/350db081a661525235354dd3e19b8c05-Abstract.html","pr-1184":"https://arxiv.org/abs/2006.09359","pr-1185":"https://ojs.aaai.org/index.php/AAAI/article/view/7727","pr-1186":"https://proceedings.mlr.press/v78/laskey17a.html","pr-1187":"https://www.sciencedirect.com/science/article/pii/S0004370299000521","pr-1188":"https://journals.sagepub.com/doi/abs/10.1177/0278364913495721","pr-1189":"https://arxiv.org/abs/2004.07219","pr-1190":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html","pr-1191":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/6d7c4a0727e089ed6cdd3151cbe8d8ba-Abstract-Conference.html","pr-1192":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/8ffb4e3118280a66b192b6f06e0e2596-Abstract-Conference.html","pr-1193":"https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c66099070429b9b49ad8bb19c740c22-Abstract-Conference.html","pr-1194":"https://www.annualreviews.org/content/journals/10.1146/annurev-control-030323-022510","pr-1195":"https://www.roboticsproceedings.org/rss22/p015.html","pr-1196":"https://www.roboticsproceedings.org/rss22/p016.html","pr-1197":"https://www.roboticsproceedings.org/rss22/p139.html","pr-1198":"https://www.roboticsproceedings.org/rss22/p154.html","pr-1199":"https://ijcai.org/proceedings/2026/228","pr-1200":"https://arxiv.org/abs/2607.29613","pr-1201":"https://arxiv.org/abs/2609.18207","pr-1202":"https://arxiv.org/abs/2603.21341","pr-1203":"https://arxiv.org/abs/2512.05107"})
FOCUS_REVIEW_DATES.update(dict.fromkeys(["pr-1180","pr-1181","pr-1182","pr-1183","pr-1184","pr-1185","pr-1186","pr-1187","pr-1188","pr-1189","pr-1190","pr-1191","pr-1192","pr-1193","pr-1194","pr-1195","pr-1196","pr-1197","pr-1198","pr-1199","pr-1200","pr-1201","pr-1202","pr-1203"], "2026-11-12"))

# 2026-11-16 REG-R16: requested Psi-Zero and its direct data prerequisites.
NEXT_GROUPS["VLA, cross-embodiment, and long-horizon planning"].append(
    "=Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation"
)
NEXT_GROUPS["RL, IL, offline learning, and robot data"].extend([
    "=EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video",
    "=Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation",
])
FOCUS_PRIORITY_RATIONALES.update({
    "pr-1204": "Human-video 표현 학습·humanoid action expert·RL 하위 제어의 역할을 분리할 직접 비교 논문이다. VLA 가중치의 reward 공동 갱신과 혼동하지 않는다.",
    "pr-1205": "Ψ₀ 사전학습의 인간 데이터 전제이며 hand prediction과 robot closed-loop 성공을 구분할 핵심 데이터 기준이다.",
    "pr-1206": "Ψ₀의 로봇 데이터 전제와 G1/H1 action schema를 비교하는 데 필요하며 전체 corpus와 모델 사용 subset을 구분한다.",
})
FOCUS_SOURCE_CHECKS.update({
    "pr-1204": "https://www.roboticsproceedings.org/rss22/p021.html",
    "pr-1205": "https://iclr.cc/Downloads/2026",
    "pr-1206": "https://arxiv.org/abs/2510.08807",
})
FOCUS_REVIEW_DATES.update(dict.fromkeys(["pr-1204", "pr-1205", "pr-1206"], "2026-11-16"))

# 2026-11-18 REG-R17: direct active-perception, geometry and exploration prerequisites.
NEXT_GROUPS['Active and embodied 3D Vision'].extend([
    '=FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects',
    '=Active 6D pose estimation for textureless objects using multi-view RGB frames',
    '=RFMPose: Generative Category-level Object Pose Estimation via Riemannian Flow Matching',
    '=Robo3R: Enhancing Robotic Manipulation with Accurate Feed-Forward 3D Reconstruction',
    '=Robotic task success evaluation under multi-modal non-parametric object pose uncertainty',
    '=ActivePose: Active 6D Object Pose Estimation and Tracking for Robotic Manipulation',
    '=Imagine then Verify: Affordance-Targeted Active Perception for Task-Oriented Grasping in Cluttered Scenes',
])
NEXT_GROUPS['RL, IL, offline learning, and robot data'].extend([
    '=Learning to Look: Seeking Information for Decision Making via Policy Factorization',
    '=Real-World Reinforcement Learning of Active Perception Behaviors',
    '=Colored Noise in PPO: Improved Exploration and Performance through Correlated Action Sampling',
    '=SOE: Sample-Efficient Robot Policy Self-Improvement via On-Manifold Exploration',
])
NEXT_GROUPS['VLA, cross-embodiment, and long-horizon planning'].extend([
    '=Universal Pose Pretraining for Generalizable Vision-Language-Action Policies',
    '=GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation',
    '=ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver',
    '=StructRL: Structured Action-Space Exploration for Flow-Based VLAs',
    '=SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics',
    '=Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation',
])
NEXT_GROUPS['Contact-rich, deformable, force, and dexterous manipulation'].extend([
    '=Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation',
    '=Guiding real-world reinforcement learning for in-contact manipulation tasks with Shared Control Templates',
])
FOCUS_REFERENCE_RATIONALES.pop("pr-1030", None)
FOCUS_PRIORITY_RATIONALES.update({'pr-1207': '현재 능동 관측 후보의 pose baseline이며 CAD/reference·score·좌표 가정을 판단하는 직접 NEXT다.', 'pr-1208': '행동 불확실성 기반 관측 전환이 이미 존재함을 확인할 필수 직접 선행이다.', 'pr-1209': 'Pose 정확도 중심 NBV와 task 성공 중심 관측 중단을 비교할 journal 기준이다.', 'pr-1211': '유한 pose 가설 생성과 score 해석을 비교하는 직접 NEXT다.', 'pr-1212': 'Pose 표현을 VLA에 넣는 것만으로 새 기여를 주장하지 않도록 하는 직접 선행이다.', 'pr-1213': 'TASK-GEOMETRY가 일반 재구성 정확도 개선의 반복인지 판단할 직접 비교다.', 'pr-1214': '3D reconstruction auxiliary loss 자체가 새 기여가 아님을 보여 주는 직접 VLA 비교다.', 'pr-1215': 'TASK-GEOMETRY의 이득이 단순 target attention/영역 supervision 때문인지 비교할 선행이다.', 'pr-1216': '관계 기반 탐색 후보에서 geometry representation 이득과 exploration 변경의 이득을 구별하는 직접 비교다.', 'pr-1217': 'VLA+RL로 관측 행동을 만든다는 넓은 주장을 제한하는 핵심 실세계 기준이다.', 'pr-1218': '복잡한 관계 noise 학습 전에 비교해야 할 단순 시간 상관 탐색 baseline이다.', 'pr-1219': '관계/geometry로 탐색을 제한한다는 원리를 이미 제시한 직접 선행이다.', 'pr-1220': '불확실성이 남아도 성공하면 행동한다는 원리를 신규성에서 제외하게 하는 직접 비교다.', 'pr-1221': '관계 기반 RL 탐색의 noise 위치·시간 구조·재채점 설계와 직접 충돌하는 최신 선행이다.', 'pr-1222': '관계 조건 탐색이 일반 latent/on-manifold 탐색보다 필요한지 확인할 직접 baseline이다.', 'pr-1223': 'Pose estimation+active perception 조합이 이미 구현됐음을 보여 주는 직접 선행이다.', 'pr-1224': 'Task-aware NBV와 verification 기반 중단이 이미 있는 점을 반영할 직접 비교다.', 'pr-0805': 'Camera와 manipulation action의 decoupled 공동 학습·active benchmark가 현재 능동 관측 후보의 직접 비교이므로 REFERENCE에서 NEXT로 승격한다.', 'pr-1030': '관측 종료 상태에 맞춘 continuation adaptation은 현재 pose-active 비교의 필수 통제이며 REFERENCE에서 NEXT로 승격한다.'})
FOCUS_REFERENCE_RATIONALES.update({'pr-1210': 'CAD 완전성 전제를 완화하는 geometry 대안으로 보존하되 첫 active-pose 비교의 필수 정독에서는 REFERENCE로 둔다.'})
FOCUS_SOURCE_CHECKS.update({'pr-1207': 'https://openaccess.thecvf.com/content/CVPR2024/html/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.html', 'pr-1208': 'https://proceedings.mlr.press/v270/dass25a.html', 'pr-1209': 'https://journals.sagepub.com/doi/10.1177/02783649251411922', 'pr-1210': 'https://openaccess.thecvf.com/content/CVPR2025/html/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.html', 'pr-1211': 'https://proceedings.neurips.cc/paper_files/paper/2025/hash/618c0a236e7aace748d09bc8fbed3e4d-Abstract-Conference.html', 'pr-1212': 'https://roboticsproceedings.org/rss22/p145.html', 'pr-1213': 'https://roboticsproceedings.org/rss22/p056.html', 'pr-1214': 'https://openaccess.thecvf.com/content/CVPR2026/html/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.html', 'pr-1215': 'https://ojs.aaai.org/index.php/AAAI/article/view/38921', 'pr-1216': 'https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf', 'pr-1217': 'https://papers.neurips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html', 'pr-1218': 'https://ojs.aaai.org/index.php/AAAI/article/view/29139', 'pr-1219': 'https://link.springer.com/article/10.1007/s10514-024-10164-6', 'pr-1220': 'https://www.emerald.com/ir/article-abstract/52/5/651/1254840/Robotic-task-success-evaluation-under-multi-modal?redirectedFrom=PDF', 'pr-1221': 'https://arxiv.org/abs/2608.15139', 'pr-1222': 'https://arxiv.org/abs/2509.19292', 'pr-1223': 'https://arxiv.org/abs/2509.11364', 'pr-1224': 'https://arxiv.org/abs/2609.23504', 'pr-0805': 'https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html', 'pr-1030': 'https://arxiv.org/abs/2610.23378'})
FOCUS_REVIEW_DATES.update(dict.fromkeys(['pr-1207', 'pr-1208', 'pr-1209', 'pr-1210', 'pr-1211', 'pr-1212', 'pr-1213', 'pr-1214', 'pr-1215', 'pr-1216', 'pr-1217', 'pr-1218', 'pr-1219', 'pr-1220', 'pr-1221', 'pr-1222', 'pr-1223', 'pr-1224', 'pr-0805', 'pr-1030'], "2026-11-18"))

# 2026-11-18 REG-R18: direct task-geometry collisions; user reading status stays UNREAD.
NEXT_GROUPS['Active and embodied 3D Vision'].append(
    "=Estimate, Don't Imitate: Reusing Differentiable State-Based Policies for Visuomotor Control"
)
NEXT_GROUPS['VLA, cross-embodiment, and long-horizon planning'].extend([
    '=Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models',
    '=PRISM: Precision Forcing for Generalist Vision-Language-Action Policies',
])
FOCUS_PRIORITY_RATIONALES.update({
    'pr-1225': 'Frozen expert의 action-consistency 추정 학습은 현재 geometry 후보가 넘어야 할 직접 비교다.',
    'pr-1226': 'Geometry 결합과 재구성 품질–VLA 성능 분석의 ECCV 기준으로, 단순 상관 분석의 신규성 한계를 확인한다.',
    'pr-1227': '정밀도 요구에 따른 flow supervision·표현 학습이 이미 존재하므로 task-aware geometry의 잔여 기여를 비교한다.',
})
FOCUS_SOURCE_CHECKS.update({
    'pr-1225': 'https://arxiv.org/abs/2609.34018',
    'pr-1226': 'https://link.springer.com/chapter/10.1007/978-3-032-37271-0_2',
    'pr-1227': 'https://arxiv.org/abs/2610.14704',
})
FOCUS_REVIEW_DATES.update(dict.fromkeys(['pr-1225', 'pr-1226', 'pr-1227'], '2026-11-18'))

# Gapfill admission, reviewed 2026-11-19.
NEXT_GROUPS['VLA, cross-embodiment, and long-horizon planning'].extend([
    '=DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution',
    '=Improving Vision-Language-Action Model with Online Reinforcement Learning',
    '=MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models',
    '=MEM: Multi-Scale Embodied Memory for Vision Language Action Models',
    '=RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models',
])
NEXT_GROUPS['Contact-rich, deformable, force, and dexterous manipulation'].extend([
    '=T-Rex: Tactile-Reactive Dexterous Manipulation',
    '=Contact-Grounded Policy: Dexterous Visuotactile Policy with Generative Contact Grounding',
    '=KineDex: Learning Tactile-Informed Visuomotor Policies via Kinesthetic Teaching for Dexterous Manipulation',
    '=VTDexManip: A Dataset and Benchmark for Visual-tactile Pretraining and Dexterous Manipulation with Reinforcement Learning',
    '=ViTacFormer: Learning Cross-Modal Representation for Visuo-Tactile Dexterous Manipulation',
    '=Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning',
    '=PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation',
])
NEXT_GROUPS['Locomotion, whole-body control, mobile manipulation, and humanoids'].extend([
    '=Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning',
    '=CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks',
    '=HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning',
    '=HuG: Learning Humanoid Whole-Body Affordance-Aware Grasping with Active Perception',
])
NEXT_GROUPS['Active and embodied 3D Vision'].extend([
    '=Vision in Action: Learning Active Perception from Human Demonstrations',
    '=Active Perception for Grasp Detection via Neural Graspness Field',
    '=UniTac2Pose: A Unified Approach Learned in Simulation for Category-level Visuotactile In-hand Pose Estimation',
    '=ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation',
    '=ActiveMimic: Egocentric Video Pretraining with Active Perception',
])
NEXT_GROUPS['World models, uncertainty, failure detection, and recovery'].extend([
    '=Back to the Familiar Future: Failure Recovery for VLA Policies via Pre-Imagined Milestone Selection',
    '=VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models',
])
FOCUS_PRIORITY_RATIONALES.update({
    'pr-1228': '계산 예산에 따라 같은 VLA의 실행 깊이를 바꾸는 비교 기준이다.',
    'pr-1229': '온라인 RL을 VLA에 직접 적용하는 방식과 RL·감독학습을 교대하는 방식을 대조할 기준이다.',
    'pr-1230': '사족 로봇에서 VLA를 행동 가치 함수로 학습하는 경로를 대표한다.',
    'pr-1231': '단기 영상 이력과 장기 의미 이력이 서로 다른 행동 오류를 해결하는지 시험할 기준이다.',
    'pr-1232': '추가 학습 없이 행동 후보를 더 뽑는 효과와 학습한 검증기가 주는 이득을 분리할 기준이다.',
    'pr-1233': '접촉 중 빠른 촉각 반응을 학습할 시연 자료와 서로 다른 주기의 VLA 구조를 함께 제시한다.',
    'pr-1234': '촉각을 정책의 추가 입력으로 쓰는 경우와 미래 접촉을 실행 제어 목표로 만드는 경우를 직접 비교한다.',
    'pr-1235': '잡음 제거 세계 모델과 보행 RL을 실제 불규칙 지형에 전이한 대표 제어 사례다.',
    'pr-1236': '전신 시연을 수집할 때 제어기와 실제 위치의 차이를 폐루프로 보정하는 시스템 기준이다.',
    'pr-1237': '카메라 움직임을 학습한 양팔 정책과 고정 카메라 정책을 실물에서 비교한 능동 인식의 직접 선행이다.',
    'pr-1238': '복구가 가능한 시점에서 미래 시각 목표만 바꾸는 대조군을 제공한다.',
    'pr-1239': '실패 감지의 정확도와 알림 시간을 함께 평가하는 지표와 VLA용 감지 기준을 제공한다.',
    'pr-1240': '전신 계획으로 이동 조작 시연을 만드는 기법과 휴머노이드용 시뮬레이션 벤치마크를 함께 제공한다.',
    'pr-1241': '재구성 품질 대신 파지 목표에 대한 불확실성으로 카메라 시점을 고르는 기준이다.',
    'pr-1242': '접촉력 시연을 수집하고 힘을 제어하는 정책까지 연결하는 촉각 모방학습의 기준이다.',
    'pr-1243': '새 물체의 손안 자세·추적·불확실성을 같은 촉각 추정기에서 평가하는 비교 기준이다.',
    'pr-1244': '손안 물체의 자세와 물체가 환경에 닿는 위치를 함께 추정하는 접촉 상태 기준이다.',
    'pr-1245': '희소 이진 촉각의 기여를 같은 RL 과제에서 비교할 수 있는 데이터셋과 벤치마크다.',
    'pr-1246': '행동과 미래 촉각의 공동 예측을 장시간 실물 다지 조작에서 대조할 기준이다.',
    'pr-1247': '시각이 없는 다지 파지에서 촉각 접촉 보정과 RL 전문가 증류를 검토할 기준이다.',
    'pr-1248': '실물의 특권 관측을 학습 때만 사용해 촉각 상태 추정기를 증류하는 전이 기준이다.',
    'pr-1249': '카메라 탐색과 파지 가능성 판단에 전신 균형 제약을 결합한 실기 휴머노이드 기준이다.',
    'pr-1250': '사람의 머리 움직임을 관측 행동으로 학습하고 실제 로봇으로 전이하는 직접 선행이다.',
})
FOCUS_SOURCE_CHECKS.update({
    'pr-1228': 'https://proceedings.neurips.cc/paper_files/paper/2024/hash/67b0e7c7c2a5780aeefe3b79caac106e-Abstract-Conference.html',
    'pr-1229': 'https://api.crossref.org/works/10.1109/icra55743.2025.11127299',
    'pr-1230': 'https://api.crossref.org/works/10.1109/icra55743.2025.11128601',
    'pr-1231': 'https://arxiv.org/abs/2603.03596',
    'pr-1232': 'https://proceedings.mlr.press/v305/kwok25a.html',
    'pr-1233': 'https://arxiv.org/abs/2606.17055',
    'pr-1234': 'https://roboticsproceedings.org/rss22/p005.html',
    'pr-1235': 'https://roboticsproceedings.org/rss20/p058.html',
    'pr-1236': 'https://proceedings.mlr.press/v305/li25h.html',
    'pr-1237': 'https://proceedings.mlr.press/v305/xiong25a.html',
    'pr-1238': 'https://arxiv.org/abs/2606.09258',
    'pr-1239': 'https://arxiv.org/abs/2606.21386',
    'pr-1240': 'https://arxiv.org/abs/2605.27724',
    'pr-1241': 'https://proceedings.neurips.cc/paper_files/paper/2024/hash/4364fef031fdf7bfd9d1c9c56b287084-Abstract-Conference.html',
    'pr-1242': 'https://proceedings.mlr.press/v305/zhang25l.html',
    'pr-1243': 'https://proceedings.mlr.press/v305/wu25d.html',
    'pr-1244': 'https://roboticsproceedings.org/rss21/p054.html',
    'pr-1245': 'https://proceedings.iclr.cc/paper_files/paper/2025/hash/e19b6f65791e350347bcff8a3955cb5b-Abstract-Conference.html',
    'pr-1246': 'https://roboticsproceedings.org/rss22/p129.html',
    'pr-1247': 'https://arxiv.org/abs/2606.11767',
    'pr-1248': 'https://arxiv.org/abs/2603.04531',
    'pr-1249': 'https://arxiv.org/abs/2611.01659',
    'pr-1250': 'https://arxiv.org/abs/2606.06194',
})
FOCUS_REVIEW_DATES.update(dict.fromkeys((f"pr-{n:04d}" for n in range(1228, 1251)), "2026-11-19"))

FOCUS_REFERENCE_RATIONALES.update({
    "pr-1251": "시연자 요청과 적용 명령을 시각별로 분리할 수 있는 실제 공유 제어 데이터셋이다. 시연 재수집의 필요성과 원격조작 로그의 정보 손실을 판별할 때 조회한다.",
    "pr-1252": "사람과 RL 잔차 정책이 함께 모은 시연을 직접 원격조작과 비교한 실물 조립 기준선이다. 공유 제어 시연의 학습 가치와 재수집 비용을 평가할 때 조회한다.",
})
FOCUS_SOURCE_CHECKS.update({
    "pr-1251": "https://journals.sagepub.com/doi/10.1177/02783649211050677",
    "pr-1252": "https://www.corl.org/program/accepted-papers",
})
FOCUS_REVIEW_DATES.update(dict.fromkeys(("pr-1251", "pr-1252"), "2026-11-20"))

SYNTHESIS_FILES = OrderedDict(
    [
        (
            "01_control.md",
            [
                "Planning, control, and whole-body foundations",
                "Planning, control, simulation, and TAMP extensions",
            ],
        ),
        (
            "02_learning.md",
            [
                "RL, IL, and policy learning foundations",
                "RL, IL, offline learning, and robot data",
            ],
        ),
        (
            "03_manipulation.md",
            [
                "Manipulation, contact, tactile, and dexterity",
                "Contact-rich, deformable, force, and dexterous manipulation",
            ],
        ),
        (
            "04_vla.md",
            [
                "VLA and generalist robot policies",
                "VLA, cross-embodiment, and long-horizon planning",
            ],
        ),
        (
            "05_safety.md",
            [
                "Safety and robot world models",
                "World models, uncertainty, failure detection, and recovery",
            ],
        ),
        (
            "06_mobility.md",
            [
                "Locomotion, mobile manipulation, and humanoid systems",
                "Locomotion, whole-body control, mobile manipulation, and humanoids",
            ],
        ),
        (
            "07_perception.md",
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
        "pr-0516",  # Preserve the existing CFG reference decision through the 2026-10-31 path repair
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
    focus_ids = set(FOCUS_PRIORITY_RATIONALES) | set(FOCUS_REFERENCE_RATIONALES) | set(FOCUS_SOURCE_CHECKS)
    if focus_ids - known_manifest_ids:
        raise RuntimeError(f"Unknown focus-review paper IDs: {sorted(focus_ids - known_manifest_ids)}")
    for papers in core_groups.values():
        for paper in papers:
            if manifest_ids.get(paper["path"]) not in FOCUS_PRIORITY_RATIONALES:
                raise RuntimeError(f"CORE paper needs a dependency rationale: {paper['title']}")
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
    existing_tiers_by_id: dict[str, str] = {}
    if INDEX.exists():
        with INDEX.open(newline="") as file:
            for old_row in csv.DictReader(file):
                if old_row.get("tier") in {"REFERENCE", "ARCHIVE"}:
                    existing_tiers[old_row.get("overview_path", "")] = old_row["tier"]
                    if old_row.get("paper_id"):
                        existing_tiers_by_id[old_row["paper_id"]] = old_row["tier"]

    for row in rows:
        path = row["path"]
        if path in tier_by_path:
            continue
        if manifest_ids.get(path) in FOCUS_REFERENCE_RATIONALES:
            tier_by_path[path] = "REFERENCE"
            track_by_path[path] = "Focus review: on-demand reference"
            primary_track_by_path[path] = manifest_tracks.get(path)
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
        existing_tier = existing_tiers.get(path) or existing_tiers_by_id.get(manifest_ids.get(path))
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
    ids = manifest_paper_ids()
    sequence = 0
    for track, papers in groups.items():
        lines.extend([f"### {track} — {len(papers)}", ""])
        for paper in papers:
            sequence += 1
            lines.append(
                f"{sequence}. [{paper['title']}]({'.' + paper['path']}) "
                f"— {paper['year']} {paper['venue']}."
            )
            rationale = FOCUS_PRIORITY_RATIONALES.get(ids.get(paper["path"]))
            if rationale:
                lines.append(f"   - 선정 이유: {rationale}")
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
        "# 읽기 계획",
        "",
        f"- Updated: {datetime.now(ZoneInfo('Asia/Seoul')).date().isoformat()} KST",
        "- Source registry: [PAPER.md](../PAPER.md)",
        "- Full tier index: [READING_TIERS.csv](./READING_TIERS.csv)",
        "- Reading tracker: [READING_STATUS.csv](./READING_STATUS.csv)",
        "- Inactive reading history: [READING_STATUS_HISTORY.csv](./READING_STATUS_HISTORY.csv)",
        f"- Intensive-reading set: **{counts['CORE'] + counts['NEXT']} papers** "
        f"(CORE {counts['CORE']} + NEXT {counts['NEXT']})",
        f"- Base tier review: {FOCUS_REVIEW_DATE}. 최근 등록·게재 갱신은 [레지스트리 변경](../work/update/REGISTRY.md)을 따른다. 개별 membership은 이 생성기의 CORE/NEXT group으로 관리하고 사용자 읽기 이력은 보존한다.",
        "",
        "## Research Scope and Reading Policy",
        "",
        "주 연구축은 VLA를 기반으로 다양한 로봇의 manipulation과 navigation을 다루는 것이다. 현재 새 탐색은 VLA + RL 결합이며, 기존 비-RL 후보의 문헌과 판단도 보존한다. "
        "관측·언어 지시·보상이 실제 행동과 일반화에 주는 효과, 로봇별 적응 비용과 기존 능력 보존을 함께 검토한다. "
        "3D vision은 policy state, spatial memory, affordance, localization, collision/contact reasoning이 실제 행동을 바꾸는 경우 우선한다.",
        "",
        "읽기 결과는 [7개 synthesis와 교차 질문 분류](../synthesis/README.md)에 연결한다. 행동 표현·시간/feedback·상태/기억·접촉/실행 가능성·적응/평가 신뢰도를 구분해 비교한다. "
        "현재 후보는 [연구 후보](../work/research_topics/README.md), 이전 판단은 [종료·보류 결과](../work/research_topics/RESULTS.md), 다음 실행은 [TODO](../TODO.md)에서 관리한다. 연구 후보의 판단과 논문 읽기 상태는 별도로 갱신한다.",
        "",
        "`observation/history → state/belief/3D memory → language/task/skill decision → VLA/policy/control → contact/failure feedback → adaptation/recovery (RL optional)`",
        "",
        f"1. **CORE {counts['CORE']}편:** 목표 연구의 재사용 가능한 foundation, 대표 policy/RL interface, 데이터·평가 기준이다. 각 논문의 선정 이유를 아래에 기록한다.",
        f"2. **NEXT {counts['NEXT']}편:** 해당 branch의 선행 개념을 확인한 뒤 읽는 전문화·frontier다. CORE 전체 완독을 기다릴 필요는 없다.",
        f"3. **REFERENCE {counts['REFERENCE']}편:** controller, sensor, embodiment, reconstruction 방법을 실제로 사용할 때 조회한다.",
        f"4. **ARCHIVE {counts['ARCHIVE']}편:** 현재 범위 밖의 검색·역사 자료로 보존한다.",
        "",
        "### 운영 원칙",
        "",
        "- 연도만으로 승격·강등하지 않는다. TD, policy gradient, PPO, SAC, POMDP, impedance는 최신 방법의 objective와 interface를 이해하는 데 필요한 범위로 유지한다.",
        "- CORE의 번호는 탐색과 기본 진행 순서다. 아래 dependency batch에서 필요한 선행을 확인하면 해당 NEXT를 병행한다.",
        "- Manipulation의 direct VLA RL, RL-generated data distillation, navigation의 hierarchical VLA/RL control을 서로 다른 개선 경로로 비교한다.",
        "- 동일 플랫폼의 fleet, pretraining-seen/RL-held-out robot, target adaptation, unseen-embodiment zero-shot을 구분한다. RL 전이는 동일 데이터 SFT·후학습 전 base policy와 비교한다.",
        "- Locomotion은 navigation controller·mobile manipulation과 직접 연결될 때 우선하며, humanoid motion tracking이나 순수 보행 전문화는 필요시 참조한다.",
        "- 7개 primary track과 연도/venue 폴더 구조를 유지한다. Navigation은 관련 track의 task/interface로 연결하고 중복 등록하지 않는다.",
        "- 선정 이유는 연구자의 curation 판단이다. abstract/project 재확인은 본문 정독이나 reading status 승격을 뜻하지 않는다.",
        "",
        "## Priority Criteria",
        "",
        "1. VLA/generalist policy의 reward-driven 개선 또는 manipulation/navigation 실행에 직접 필요한가",
        "2. action representation, policy gradient/value objective, offline-to-online data, controller interface를 이해할 기준인가",
        "3. 여러 후속 연구에서 재사용할 foundation, 공개 system, 데이터 또는 benchmark인가",
        "4. 3D representation의 효과가 perception 점수와 함께 downstream behavior로 평가되는가",
        "5. demonstration·interaction·compute·inference budget을 맞춘 비교가 가능한가",
        "6. partial observability, long horizon, reward error, contact, recovery를 구체적으로 평가하는가",
        "7. 최신 논문은 기존 기준의 어떤 한계를 검증하거나 바꾸는가",
        "",
        "## Tier Definitions",
        "",
        "| Tier | Papers | Use |",
        "|---|---:|---|",
        f"| CORE | {counts['CORE']} | VLA 기반 manipulation/navigation의 기반·대표 interface·평가 좌표계 |",
        f"| NEXT | {counts['NEXT']} | 해당 CORE prerequisite 이후 읽는 직접 관련 전문화·frontier |",
        f"| REFERENCE | {counts['REFERENCE']} | 특정 구현·sensor·embodiment가 요구할 때 읽는 기반과 대안 |",
        f"| ARCHIVE | {counts['ARCHIVE']} | 현재 범위 밖의 검색·역사 자료 |",
        "",
        "CORE는 최신 논문 모음이나 고정 quota가 아니다. 중요성과 dependency가 바뀌면 규모도 바뀐다.",
        "",
        "## Completion Rule",
        "",
        "논문 하나를 정독한 뒤 문제·가정, observation/state/action/control interface, "
        "embodiment/task/data/metric/failure, 재사용·반박할 지점을 tracker와 해당 synthesis에 기록한다. "
        "노트의 존재와 source evidence는 사용자의 읽기 상태와 별개다.",
        "",
        "## Dependency-Based Reading Batches",
        "",
        "단일 canonical plan 안의 비교 경로다. 화살표는 개념적 prerequisite이며 직접 citation을 뜻하지 않는다. "
        "각 경로의 선행을 확인한 뒤 frontier와 baseline을 함께 읽는다.",
        "",
        "| Branch | Foundation and comparison spine | NEXT extension | Exit artifact |",
        "|---|---|---|---|",
        "| VLA + RL manipulation | TD/GAE → PPO + Diffusion Policy → DPPO; IQL/CQL → AWAC/Cal-QL ↔ FQL; RLPD/SERL → HIL-SERL; OFT → ConRFT ↔ RLDG | SimpleVLA-RL, RL4VLA, WCM, RoboAlign, STARE-VLA; Real-Time EXPO-FT는 별도 editor 구조의 대안 | advantage/critic·actor 갱신 대상·배포 구조, demonstration·interaction·compute를 맞춘 비교표 |",
        "| Reward, goals and temporal abstraction | Potential-based reward shaping; UVFA → HER ↔ Successor Features; options/semi-MDP | HIQL, Is Value Learning Really the Main Bottleneck in Offline RL?, Horizon Reduction, Act2Goal | 목표·전이 동역학·종료/할인 가정, value 오차와 policy extraction·horizon 병목을 분리한 표 |",
        "| Action representation and generalization | DAgger/RoboMimic → ACT/Diffusion Policy; DDPM/Flow Matching → Octo/OpenVLA/π0 → FAST/π0.5; DPPO/FQL | Q-chunking → DQC, SpatialVLA, reactive/force VLA | actor chunk·critic horizon·feedback rate·latency·action likelihood와 RL objective 표 |",
        "| Navigation and mobile manipulation | POMDP/Habitat/VLN-CE → ViNT/NoMaD; CLIP/ConceptFusion/VLFM → SayCan/NaVILA; Mobile ALOHA | NaVid → Uni-NaVid/StreamVLN, NavDP/LoGoPlanner, SocialNav, FeedTTA, GOAT, WMNav | goal type·memory·action granularity·collision·social compliance·SPL/success와 reward 접근 조건 표 |",
        "| Action-relevant 3D | RVT ↔ DP3; ConceptFusion ↔ VLFM | LoGoPlanner의 metric memory, PointWorld의 3D dynamics/MPC, VLMaps, PointVLA, Any3D-VLA | policy·data·compute를 고정한 RGB/3D 비교, pose/calibration 접근과 downstream failure |",
        "| Evaluation, contact and recovery | LIBERO/CALVIN/DROID/Habitat; DAgger → DART; MuJoCo/impedance → Recovery RL/TD-MPC2 | D4RL ↔ OGBench, Tune to Learn, Discounted Liveness OPE, OopsieVerse, Tac2Real, RLBench, ManiSkill3, FurnitureBench, SAFE | task/split·reward·gain·damage·reset·intervention 비용, recovery·truncation·OOD protocol |",
        "| World-model policy improvement | TD-MPC2 → Ctrl-World/WMPO/WorldGym | VLAW ↔ VLA-MBPO ↔ RISE; PointWorld의 MPC와 비교; PersistWorld는 prediction-fidelity 참조 | fixed real-data budget, imagined vs real success, failure coverage와 model bias의 분리 |",
        "",
        "Batch 산출물과 source location을 확인한 뒤에만 synthesis evidence로 사용한다. Benchmark 간 성공률을 같은 난이도의 점수로 합치지 않는다.",
        "",
        "## Research Lenses Across Tracks",
        "",
        "- VLA RL과 from-scratch RL, supervised fine-tuning, RL-generated-data distillation을 분리한다.",
        "- Offline demonstration과 online interaction 양, human intervention, reset, reward annotation 비용을 함께 기록한다.",
        "- Navigation의 instruction/goal grounding과 low-level execution을 분리하고 privileged state·map·oracle success 접근을 명시한다.",
        "- 3D 입력의 이득은 action success·collision·sample efficiency·latency와 연결한다.",
        "- 최신 2024–2026 연구도 장기 foundation으로 단정하지 않는다. 공개 interface와 평가 근거가 부족하면 NEXT 또는 REFERENCE로 유지한다.",
        "- Task success 외에 disturbance, long horizon, contact failure, forgetting, recovery를 비교한다.",
        "",
    ]
    lines.extend(plan_section("CORE", core_groups))
    lines.extend([
        "해당 branch의 CORE prerequisite를 확인한 뒤 아래 NEXT를 병행한다. 모든 CORE를 먼저 완독할 필요는 없다.",
        "",
    ])
    lines.extend(plan_section("NEXT", next_groups))
    lines.extend([
        "## REFERENCE — On-Demand Reading",
        "",
        "기존 foundation의 가치를 낮춘 분류가 아니다. 일반 search/control, tactile hardware, "
        "whole-body locomotion, generic reconstruction은 선택한 실험의 요구에 따라 다시 읽는다. "
        "현재 tier에서 빠진 기존 읽기 상태와 개인 분석은 history CSV에 보존하며 재승격 시 복원한다.",
        "",
        "## ARCHIVE — Search Only",
        "",
        "현재 연구 범위 밖의 논문도 registry와 표준 노트에서 검색할 수 있다. "
        "이번 재분류는 논문 수·PDF 보유 여부·venue quota를 기준으로 하지 않는다.",
        "",
    ])
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
    # A case-only filesystem repair must not discard reading inputs. Restrict
    # this migration to a unique current path with the same stable paper ID;
    # arbitrary missing paths still fail below.
    paths_by_case: dict[str, list[str]] = {}
    for path in paper_id_by_path:
        paths_by_case.setdefault(path.casefold(), []).append(path)
    # Keep user inputs when a paper leaves the intensive set; active entries
    # override history on re-entry. Never infer a reading status from a tier.
    for source in (STATUS_HISTORY, STATUS):
        if source.exists():
            with source.open(newline="") as file:
                for old_row in csv.DictReader(file):
                    path = old_row.get("overview_path", "")
                    if path not in paper_id_by_path:
                        matches = paths_by_case.get(path.casefold(), [])
                        if len(matches) == 1 and old_row.get("paper_id") and old_row["paper_id"] == paper_id_by_path[matches[0]]:
                            path = matches[0]
                    preserved[path] = old_row

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
        overview = ROOT / urllib.parse.unquote(path.removeprefix("./"))
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

    active_paths = {row["overview_path"] for row in output_rows}
    registry_by_path = {row["path"]: row for row in rows}
    history_rows = []
    for path, old in sorted(preserved.items()):
        if path in active_paths:
            continue
        if path not in registry_by_path:
            raise RuntimeError(f"Reading history path is missing from registry: {path}")
        row = registry_by_path[path]
        saved = {field: old.get(field, "") for field in fieldnames}
        saved.update({
            "tier": tier_by_path[path], "track": track_by_path[path],
            "primary_track": primary_track_by_path.get(path) or "",
            "paper_id": paper_id_by_path.get(path) or "", "sequence": "",
            "year": row["year"], "venue": row["venue"], "title": row["title"],
            "overview_path": path,
        })
        history_rows.append(saved)
    with STATUS_HISTORY.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(history_rows)

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
