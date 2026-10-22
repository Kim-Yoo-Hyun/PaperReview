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
                "=Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning",
                "=RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning",
                "=DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset",
                "=Benchmarking Knowledge Transfer for Lifelong Robot Learning",
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
            ],
        ),
        (
            "VLA, cross-embodiment, and long-horizon planning",
            [
                "=What Can RL Bring to VLA Generalization? An Empirical Study",
                "=SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
                "=RLux-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models",
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
                "=VIMA: General Robot Manipulation with Multimodal Prompts",
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
                "=UMPNet: Universal Manipulation Policy Network for Articulated Objects",
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
                "=VLMaps: Visual-Language Maps for Robot Navigation",
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
                "=World Models",
                "=DayDreamer: World Models for Physical Robot Learning",
                "=Control Barrier Function Based Quadratic Programs for Safety Critical Systems",
                "=DreamGen: Unlocking Generalization in Robot Learning through Video World Models",
                "=DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos",
                "=Learning Latent Dynamics for Planning from Pixels",
                "=Dream to Control: Learning Behaviors by Latent Imagination",
                "=Mastering Diverse Domains through World Models",
                "=PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation",
                "=Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets",
                "=FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation",
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
    "pr-0951": "Foundation bridge. PPO를 denoising policy의 RL fine-tuning으로 연결한다. Diffusion Policy → DPPO → RL-100 등 직접 policy 개선을 비교하는 prerequisite이므로 CORE를 검토할 이유가 있다. VLA 자체를 제안한 논문은 아니다.",
    "pr-0952": "Foundation bridge. Expressive flow policy와 Q-learning/one-step actor를 연결한다. IQL/CQL 이후 flow-action RL과 Q-chunking 계열의 구현·비교 기준으로 중요하다. 평가가 곧 실제 robot VLA 학습을 입증하는 것은 아니다.",
    "pr-0953": "Current trend. Chunk 단위의 exploration과 TD backup을 결합한다. ACT/FAST의 표현 관점에 RLPD/FQL의 학습 관점을 더하므로 장기 manipulation의 비교 baseline으로 필요하다.",
    "pr-0954": "Current trend. Critic과 actor의 chunk 길이를 분리한다. Q-chunking의 value propagation 이점과 짧은 action horizon의 반응성 사이의 설계 문제를 직접 다룬다. 실제 contact feedback 성능으로의 확장은 본문/실험 확인이 필요하다.",
    "pr-0955": "Current trend. Base policy weight를 고정하고 latent noise를 RL로 조정한다. ConRFT의 fine-tuning, RLDG의 distillation과 구분되는 adaptation baseline이며 generalist policy와 실제 robot 평가가 있다.",
    "pr-0956": "Benchmark / empirical study. Visual·semantic·execution generalization을 나누어 SFT와 RL을 비교한다. OpenVLA/OFT 이후 RL의 효과를 주장할 때 필요한 평가 기준이다. 해당 실험에서의 PPO 결과를 모든 VLA에 대한 우열로 일반화하지 않는다.",
    "pr-0957": "Current trend / system. OpenVLA-OFT에서 outcome reward와 scalable rollout/training을 다룬다. 현재 OFT → ConRFT 경로에 대규모 simulator RL의 비교 지점을 추가한다. Real-world 결과와 real-world online training의 범위는 구분해서 정독해야 한다.",
    "pr-0958": "Current trend / system. 여러 VLA·RL 알고리즘·시뮬레이터를 비교할 공통 interface와 resource allocation을 제공한다. SimpleVLA-RL 및 ConRFT 실험을 설계할 때 algorithm 효과와 시스템 throughput을 분리하는 데 유용하다. 공식 software에서는 RLinf-VLA라는 이름도 사용한다.",
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
    "pr-0971": "Current system. 실제 robot online RL에서 edge/cloud·buffer·weight synchronization을 구현할 때 SERL/HIL-SERL의 시스템 확장으로 읽는다. Simulator 중심 RLux-VLA와 역할이 다르다.",
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
    if INDEX.exists():
        with INDEX.open(newline="") as file:
            for old_row in csv.DictReader(file):
                if old_row.get("tier") in {"REFERENCE", "ARCHIVE"}:
                    existing_tiers[old_row.get("overview_path", "")] = old_row["tier"]

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
        "# VLA Reading Plan for Manipulation and Navigation",
        "",
        f"- Updated: {datetime.now(ZoneInfo('Asia/Seoul')).date().isoformat()} KST",
        "- Source registry: [PAPER.md](../PAPER.md)",
        "- Full tier index: [READING_TIERS.csv](./READING_TIERS.csv)",
        "- Reading tracker: [READING_STATUS.csv](./READING_STATUS.csv)",
        "- Inactive reading history: [READING_STATUS_HISTORY.csv](./READING_STATUS_HISTORY.csv)",
        f"- Intensive-reading set: **{counts['CORE'] + counts['NEXT']} papers** "
        f"(CORE {counts['CORE']} + NEXT {counts['NEXT']})",
        f"- Base tier review: {FOCUS_REVIEW_DATE}; incremental review: 2026-10-22. 후보별 비교 문헌 47편을 등록하고 NEXT 18 / REFERENCE 29편으로 배정했다. 기존 membership과 사용자 읽기 이력은 유지한다. 연구 초점은 VLA 기반 manipulation·navigation과 action-relevant 3D이며 RL은 선택 사항이다.",
        "",
        "## Research Scope and Reading Policy",
        "",
        "주 연구축은 VLA를 기반으로 다양한 로봇의 manipulation과 navigation을 다루는 것이다. RL은 연구 질문에 필요할 때 비교할 방법이다. "
        "관측·언어 지시·보상이 실제 행동과 일반화에 주는 효과, 로봇별 적응 비용과 기존 능력 보존을 함께 검토한다. "
        "3D vision은 policy state, spatial memory, affordance, localization, collision/contact reasoning이 실제 행동을 바꾸는 경우 우선한다.",
        "",
        "읽기 결과는 [7개 synthesis와 교차 질문 분류](../synthesis/README.md)에 연결한다. 행동 표현·시간/feedback·상태/기억·접촉/실행 가능성·적응/평가 신뢰도를 구분해 비교한다. "
        "후보별 현재 판정과 재개 조건은 [16개 주제 요약](../work/research_candidates/summaries/README.md), 활성 작업은 [TODO](../TODO.md)에서 관리한다. 후보 HOLD/NO-GO와 GPU 확보는 아래 tier membership이나 실제 읽기 상태를 자동으로 바꾸지 않는다.",
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
        "| VLA + RL manipulation | PPO + Diffusion Policy → DPPO; IQL/CQL + Flow Matching → FQL; RLPD/SERL → HIL-SERL; OFT → ConRFT ↔ RLDG | DSRL, RL-100, SimpleVLA-RL, RLux-VLA, USER, RL4VLA, DyGRO-VLA | direct RL vs latent steering vs RL-data distillation; demonstration·interaction·compute를 맞춘 비교표 |",
        "| Action representation and generalization | DAgger/RoboMimic → ACT/Diffusion Policy; DDPM/Flow Matching → Octo/OpenVLA/π0 → FAST/π0.5; DPPO/FQL | Q-chunking → DQC, SpatialVLA, reactive/force VLA | actor chunk·critic horizon·feedback rate·latency·action likelihood와 RL objective 표 |",
        "| Navigation and mobile manipulation | POMDP/Habitat/VLN-CE → ViNT/NoMaD; CLIP/ConceptFusion/VLFM → SayCan/NaVILA; Mobile ALOHA | NaVid → Uni-NaVid/StreamVLN, NavDP/LoGoPlanner, SocialNav, FeedTTA, GOAT, WMNav | goal type·memory·action granularity·collision·social compliance·SPL/success와 reward 접근 조건 표 |",
        "| Action-relevant 3D | RVT ↔ DP3; ConceptFusion ↔ VLFM | LoGoPlanner의 metric memory, PointWorld의 3D dynamics/MPC, VLMaps, PointVLA, Any3D-VLA | policy·data·compute를 고정한 RGB/3D 비교, pose/calibration 접근과 downstream failure |",
        "| Evaluation, contact and recovery | LIBERO/CALVIN/DROID/Habitat; MuJoCo/impedance → Recovery RL/TD-MPC2 | OGBench, RL4VLA, OopsieVerse, Tac2Real, RLBench, ManiSkill3, FurnitureBench, SAFE | task/split·reward·damage·reset·intervention 비용, recovery·OOD protocol |",
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
    # Keep user inputs when a paper leaves the intensive set; active entries
    # override history on re-entry. Never infer a reading status from a tier.
    for source in (STATUS_HISTORY, STATUS):
        if source.exists():
            with source.open(newline="") as file:
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
