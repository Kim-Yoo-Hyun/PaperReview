# 레지스트리 통계

- Generated: 2026-11-24 KST
- Source: [papers.json](../work/sources/papers.json)
- 분포와 검색 필드는 원장·등급표·읽기 이력에서 생성한다. 교정 후 오류율과 미확인 항목은 [원문 감사](./SOURCE_AUDIT.md)에서 확인한다.

## Snapshot

- Papers: **1252**
- Resources in the combined view: **684**
- Curated relation edges: **91**
- Papers with outgoing relations: **69**
- Papers participating in a relation: **109**
- Structured evaluation profiles: **1252**
- Reproducibility profiles: **1252**
- Lineage coverage profiles: **1252**
- Papers with explicit trial/seed cues: **260**
- Papers without DOI/arXiv/OpenReview identifier: **363**

## 연도와 발표처

| 등록 연도 | 편수 |
|---|---:|
| 2024 | 181 |
| 2025 | 411 |
| 2026 | 367 |
| 그 밖의 연도 | 293 |

| 발표처·공개처 | 편수 |
|---|---:|
| CVPR | 175 |
| RSS | 154 |
| ICLR | 136 |
| CoRL | 114 |
| NeurIPS | 100 |
| ICML | 100 |
| ICCV | 96 |
| ICRA | 71 |
| 그 밖의 발표처·공개처 | 306 |

프리프린트는 등록한 공개 연도를 따른다. 전체 연도·발표처·등급 조합은 [검색 색인](./REGISTRY_INDEX.csv)에서 확인할 수 있다.

## Tier

| Value | Count |
|---|---:|
| REFERENCE | 510 |
| NEXT | 450 |
| ARCHIVE | 242 |
| CORE | 50 |

## Evidence level

| Value | Count |
|---|---:|
| FULL_TEXT_CHECKED | 1056 |
| ABSTRACT_CHECKED | 196 |

## Reading status (intensive set)

| Value | Count |
|---|---:|
| UNREAD | 499 |
| READ | 1 |

## Reading status (inactive history; excluded from intensive denominator)

| Value | Count |
|---|---:|
| UNREAD | 43 |
| READ | 4 |

## Curation rationale status

| Value | Count |
|---|---:|
| recorded | 1252 |

## Curation roles

| Value | Count |
|---|---:|
| method | 984 |
| foundation | 124 |
| benchmark_or_dataset | 103 |
| system | 43 |

## Publication kind

| Value | Count |
|---|---:|
| conference | 1079 |
| journal | 97 |
| preprint | 70 |
| technical_report | 4 |
| workshop | 2 |

## Identifier status

| Value | Count |
|---|---:|
| identified | 889 |
| source_only | 363 |

## Primary source scope

| Value | Count |
|---|---:|
| paper_specific | 1252 |

## Code status

| Value | Count |
|---|---:|
| not_identified | 652 |
| released | 400 |
| project_only | 187 |
| not_released | 13 |

## Data status

| Value | Count |
|---|---:|
| not_identified | 1053 |
| released | 100 |
| not_applicable | 98 |
| not_released | 1 |

## Evaluation type

| Value | Count |
|---|---:|
| EMPIRICAL / REAL-ROBOT OR HARDWARE | 441 |
| not_recorded | 286 |
| EMPIRICAL / SOURCE-REPORTED EVALUATION | 266 |
| SYSTEM / EVALUATION SCOPE UNRESOLVED | 94 |
| EMPIRICAL / SIMULATION | 74 |
| BENCHMARK / DATASET | 65 |
| EMPIRICAL / REAL-ROBOT AND SIMULATION | 8 |
| EMPIRICAL / BENCHMARK OR DATASET | 5 |
| BENCHMARK / DATASET AND REAL-ROBOT COMPARISON | 4 |
| BENCHMARK / SIMULATION | 3 |
| BENCHMARK / DATASET WITH SIMULATION AND REAL-ROBOT COMPARISON | 2 |
| EMPIRICAL / SIMULATION / REAL-ROBOT OR HARDWARE | 2 |
| EMPIRICAL / BENCHMARK / REAL-ROBOT OR HARDWARE | 1 |
| EMPIRICAL / SIMULATION / REAL-ROBOT OR HARDWARE / BENCHMARK | 1 |

## Evaluation setting

| Value | Count |
|---|---:|
| real_robot | 459 |
| not_recorded | 286 |
| source_reported | 266 |
| scope_unresolved | 94 |
| simulation | 90 |
| benchmark_or_dataset | 81 |

## Evaluation protocol status

| Value | Count |
|---|---:|
| trials_or_seeds=not_recorded | 992 |
| dataset_or_benchmark=reported | 961 |
| metrics=reported | 958 |
| baselines=reported | 949 |
| statistics=reported | 945 |
| split_or_generalization=reported | 925 |
| failure_cases=reported | 925 |
| ablations=reported | 920 |
| split_or_generalization=not_recorded | 327 |
| failure_cases=not_recorded | 327 |
| ablations=not_recorded | 304 |
| statistics=not_recorded | 298 |
| baselines=not_recorded | 294 |
| metrics=not_recorded | 293 |
| dataset_or_benchmark=not_recorded | 291 |
| trials_or_seeds=reported | 260 |
| ablations=not_reported | 28 |
| baselines=not_reported | 9 |
| statistics=not_reported | 9 |
| metrics=not_reported | 1 |

## Reproducibility profile

| Value | Count |
|---|---:|
| metadata_audited | 1252 |

## Checkpoint status

| Value | Count |
|---|---:|
| not_recorded | 1166 |
| reported | 86 |

## Configuration status

| Value | Count |
|---|---:|
| reported | 943 |
| not_recorded | 309 |

## Environment status

| Value | Count |
|---|---:|
| reported | 943 |
| not_recorded | 309 |

## Run-condition status

| Value | Count |
|---|---:|
| reported | 934 |
| not_recorded | 318 |

## Lineage coverage status

| Value | Count |
|---|---:|
| no_curated_edge_recorded | 888 |
| candidate_only | 255 |
| curated_edges | 109 |

## Relation type

| Value | Count |
|---|---:|
| extends | 40 |
| builds_on | 29 |
| baseline_for | 18 |
| uses_dataset | 4 |

## Relation confidence

| Value | Count |
|---|---:|
| verified | 43 |
| manual | 30 |
| inferred | 18 |

## Relation evidence scope

| Value | Count |
|---|---:|
| paper_body | 69 |
| title_lineage | 16 |
| official_project | 4 |
| official_abstract | 2 |

## Curated relation edges

The manifest is the source of truth; this table is a compact human-readable edge view.

| From paper | Relation | To paper | Confidence | Evidence scope |
|---|---|---|---|---|
| `pr-0011` 3D Gaussian Splatting for Real-Time Radiance Field Rendering | `builds_on` | `pr-0010` NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis | `inferred` | `paper_body` |
| `pr-0013` PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space | `extends` | `pr-0012` PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation | `verified` | `official_abstract` |
| `pr-0016` ORB-SLAM: A Versatile and Accurate Monocular SLAM System | `builds_on` | `pr-0525` Parallel Tracking and Mapping for Small AR Workspaces | `verified` | `paper_body` |
| `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `baseline_for` | `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `verified` | `paper_body` |
| `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `baseline_for` | `pr-0577` Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching | `verified` | `paper_body` |
| `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `baseline_for` | `pr-0751` Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation | `verified` | `paper_body` |
| `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `baseline_for` | `pr-0897` CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity | `verified` | `paper_body` |
| `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `baseline_for` | `pr-0924` FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation | `verified` | `paper_body` |
| `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `builds_on` | `pr-0008` Denoising Diffusion Probabilistic Models | `verified` | `paper_body` |
| `pr-0022` RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | `extends` | `pr-0021` RT-1: Robotics Transformer for Real-World Control at Scale | `inferred` | `title_lineage` |
| `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `baseline_for` | `pr-0085` MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation | `verified` | `paper_body` |
| `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `baseline_for` | `pr-0278` PD-VLA: Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding | `verified` | `paper_body` |
| `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `baseline_for` | `pr-0746` π0: A Vision-Language-Action Flow Model for General Robot Control | `verified` | `paper_body` |
| `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `baseline_for` | `pr-0773` CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models | `verified` | `paper_body` |
| `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `baseline_for` | `pr-0804` ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models | `verified` | `paper_body` |
| `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `baseline_for` | `pr-0880` SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | `verified` | `paper_body` |
| `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `baseline_for` | `pr-0915` SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | `verified` | `paper_body` |
| `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `baseline_for` | `pr-0957` SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | `verified` | `paper_body` |
| `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `builds_on` | `pr-0006` DINOv2: Learning Robust Visual Features without Supervision | `verified` | `paper_body` |
| `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `builds_on` | `pr-0022` RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | `verified` | `paper_body` |
| `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `uses_dataset` | `pr-0024` Open X-Embodiment: Robotic Learning Datasets and RT-X Models | `manual` | `paper_body` |
| `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `uses_dataset` | `pr-0732` DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset | `verified` | `paper_body` |
| `pr-0052` Octo: An Open-Source Generalist Robot Policy | `baseline_for` | `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `verified` | `paper_body` |
| `pr-0052` Octo: An Open-Source Generalist Robot Policy | `uses_dataset` | `pr-0024` Open X-Embodiment: Robotic Learning Datasets and RT-X Models | `manual` | `paper_body` |
| `pr-0061` π0.5: a Vision-Language-Action Model with Open-World Generalization | `baseline_for` | `pr-1233` T-Rex: Tactile-Reactive Dexterous Manipulation | `manual` | `paper_body` |
| `pr-0061` π0.5: a Vision-Language-Action Model with Open-World Generalization | `extends` | `pr-0746` π0: A Vision-Language-Action Flow Model for General Robot Control | `manual` | `title_lineage` |
| `pr-0075` TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies | `extends` | `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `verified` | `paper_body` |
| `pr-0084` ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY | `extends` | `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `verified` | `paper_body` |
| `pr-0137` SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space | `extends` | `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `verified` | `paper_body` |
| `pr-0524` Proximal Policy Optimization Algorithms | `baseline_for` | `pr-1229` Improving Vision-Language-Action Model with Online Reinforcement Learning | `manual` | `paper_body` |
| `pr-0524` Proximal Policy Optimization Algorithms | `extends` | `pr-0615` Trust Region Policy Optimization | `verified` | `official_abstract` |
| `pr-0577` Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching | `builds_on` | `pr-0745` Flow Matching for Generative Modeling | `verified` | `paper_body` |
| `pr-0615` Trust Region Policy Optimization | `builds_on` | `pr-0838` Policy Gradient Methods for Reinforcement Learning with Function Approximation | `inferred` | `paper_body` |
| `pr-0618` Constrained Policy Optimization | `extends` | `pr-0615` Trust Region Policy Optimization | `verified` | `paper_body` |
| `pr-0696` SAFE: Multitask Failure Detection for Vision-Language-Action Models | `baseline_for` | `pr-1239` VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models | `manual` | `paper_body` |
| `pr-0746` π0: A Vision-Language-Action Flow Model for General Robot Control | `builds_on` | `pr-0745` Flow Matching for Generative Modeling | `verified` | `paper_body` |
| `pr-0746` π0: A Vision-Language-Action Flow Model for General Robot Control | `uses_dataset` | `pr-0024` Open X-Embodiment: Robotic Learning Datasets and RT-X Models | `verified` | `paper_body` |
| `pr-0748` PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning | `extends` | `pr-0834` FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning | `inferred` | `title_lineage` |
| `pr-0749` FAST: Efficient Action Tokenization for Vision-Language-Action Models | `builds_on` | `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `verified` | `paper_body` |
| `pr-0750` Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | `extends` | `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `verified` | `paper_body` |
| `pr-0751` Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation | `extends` | `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `verified` | `paper_body` |
| `pr-0762` Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation | `extends` | `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `inferred` | `paper_body` |
| `pr-0838` Policy Gradient Methods for Reinforcement Learning with Function Approximation | `builds_on` | `pr-0837` Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning | `verified` | `paper_body` |
| `pr-0844` Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning | `builds_on` | `pr-0831` MuJoCo: A Physics Engine for Model-Based Control | `inferred` | `title_lineage` |
| `pr-0846` robosuite: A Modular Simulation Framework and Benchmark for Robot Learning | `builds_on` | `pr-0831` MuJoCo: A Physics Engine for Model-Based Control | `inferred` | `title_lineage` |
| `pr-0847` ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations | `builds_on` | `pr-0950` SAPIEN: A SimulAted Part-Based Interactive ENvironment | `inferred` | `title_lineage` |
| `pr-0849` DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation | `extends` | `pr-0848` GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force | `inferred` | `title_lineage` |
| `pr-0850` TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors | `builds_on` | `pr-0849` DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation | `verified` | `paper_body` |
| `pr-0852` Perpetual Humanoid Control for Real-time Simulated Avatars | `builds_on` | `pr-0851` AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control | `verified` | `paper_body` |
| `pr-0862` Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments | `extends` | `pr-0861` Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning | `inferred` | `title_lineage` |
| `pr-0863` Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning | `extends` | `pr-0861` Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning | `verified` | `official_project` |
| `pr-0863` Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning | `extends` | `pr-0862` Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments | `inferred` | `title_lineage` |
| `pr-0867` MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting | `extends` | `pr-0852` Perpetual Humanoid Control for Real-time Simulated Avatars | `inferred` | `title_lineage` |
| `pr-0868` HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots | `extends` | `pr-0867` MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting | `inferred` | `title_lineage` |
| `pr-0871` DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos | `extends` | `pr-0870` DreamGen: Unlocking Generalization in Robot Learning through Video World Models | `inferred` | `title_lineage` |
| `pr-0872` SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control | `extends` | `pr-0868` HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots | `inferred` | `title_lineage` |
| `pr-0887` Demonstrating GPU Parallelized Robot Simulation and Rendering for Generalizable Embodied AI with ManiSkill3 | `extends` | `pr-0847` ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations | `inferred` | `title_lineage` |
| `pr-0917` GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots | `extends` | `pr-0869` NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots | `manual` | `official_project` |
| `pr-0918` GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots | `extends` | `pr-0917` GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots | `manual` | `official_project` |
| `pr-0924` FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation | `builds_on` | `pr-0745` Flow Matching for Generative Modeling | `verified` | `paper_body` |
| `pr-0926` 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations | `baseline_for` | `pr-0084` ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY | `verified` | `paper_body` |
| `pr-0926` 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations | `extends` | `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `verified` | `paper_body` |
| `pr-0930` Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation | `extends` | `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `verified` | `paper_body` |
| `pr-0931` Diffusion Meets DAgger: Supercharging Eye-in-hand Imitation Learning | `extends` | `pr-0522` A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning | `verified` | `paper_body` |
| `pr-0948` Habitat 2.0: Training Home Assistants to Rearrange their Habitat | `extends` | `pr-0500` Habitat: A Platform for Embodied AI Research | `inferred` | `title_lineage` |
| `pr-0949` Habitat 3.0: A Co-Habitat for Humans, Avatars, and Robots | `extends` | `pr-0948` Habitat 2.0: Training Home Assistants to Rearrange their Habitat | `inferred` | `title_lineage` |
| `pr-0957` SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | `builds_on` | `pr-0750` Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | `verified` | `paper_body` |
| `pr-1143` Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance | `builds_on` | `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `verified` | `paper_body` |
| `pr-1161` GRAD-NAV++: Vision-Language Model Enabled Visual Drone Navigation With Gaussian Radiance Fields and Differentiable Dynamics | `extends` | `pr-0290` GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics | `manual` | `official_project` |
| `pr-1203` STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models | `extends` | `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `verified` | `paper_body` |
| `pr-1228` DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution | `extends` | `pr-0935` Vision-Language Foundation Models as Effective Robot Imitators | `manual` | `paper_body` |
| `pr-1230` MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models | `extends` | `pr-0625` Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions | `manual` | `paper_body` |
| `pr-1231` MEM: Multi-Scale Embodied Memory for Vision Language Action Models | `builds_on` | `pr-0061` π0.5: a Vision-Language-Action Model with Open-World Generalization | `manual` | `paper_body` |
| `pr-1232` RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models | `builds_on` | `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `manual` | `paper_body` |
| `pr-1234` Contact-Grounded Policy: Dexterous Visuotactile Policy with Generative Contact Grounding | `extends` | `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `manual` | `paper_body` |
| `pr-1235` Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning | `builds_on` | `pr-0524` Proximal Policy Optimization Algorithms | `manual` | `paper_body` |
| `pr-1236` CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks | `extends` | `pr-0602` OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning | `manual` | `paper_body` |
| `pr-1237` Vision in Action: Learning Active Perception from Human Demonstrations | `extends` | `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `manual` | `paper_body` |
| `pr-1238` Back to the Familiar Future: Failure Recovery for VLA Policies via Pre-Imagined Milestone Selection | `extends` | `pr-0042` LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | `manual` | `paper_body` |
| `pr-1240` HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning | `extends` | `pr-0637` MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations | `manual` | `paper_body` |
| `pr-1241` Active Perception for Grasp Detection via Neural Graspness Field | `extends` | `pr-0645` GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping | `manual` | `paper_body` |
| `pr-1242` KineDex: Learning Tactile-Informed Visuomotor Policies via Kinesthetic Teaching for Dexterous Manipulation | `extends` | `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `manual` | `paper_body` |
| `pr-1243` UniTac2Pose: A Unified Approach Learned in Simulation for Category-level Visuotactile In-hand Pose Estimation | `builds_on` | `pr-0484` Score-Based Generative Modeling through Stochastic Differential Equations | `manual` | `paper_body` |
| `pr-1244` ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation | `builds_on` | `pr-0848` GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force | `manual` | `paper_body` |
| `pr-1245` VTDexManip: A Dataset and Benchmark for Visual-tactile Pretraining and Dexterous Manipulation with Reinforcement Learning | `builds_on` | `pr-0524` Proximal Policy Optimization Algorithms | `manual` | `paper_body` |
| `pr-1246` ViTacFormer: Learning Cross-Modal Representation for Visuo-Tactile Dexterous Manipulation | `extends` | `pr-0566` Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware | `manual` | `paper_body` |
| `pr-1247` Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning | `builds_on` | `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `manual` | `paper_body` |
| `pr-1248` PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation | `builds_on` | `pr-0522` A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning | `manual` | `paper_body` |
| `pr-1249` HuG: Learning Humanoid Whole-Body Affordance-Aware Grasping with Active Perception | `builds_on` | `pr-0872` SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control | `manual` | `paper_body` |
| `pr-1250` ActiveMimic: Egocentric Video Pretraining with Active Perception | `builds_on` | `pr-0056` VGGT: Visual Geometry Grounded Transformer | `manual` | `paper_body` |
| `pr-1252` Efficient and Reliable Teleoperation through Real-to-Sim-to-Real Shared Autonomy | `builds_on` | `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `manual` | `paper_body` |

## Note evidence gaps

| Note | Missing evidence header |
|---|---:|

## Interpretation

- `reading_status` is user-controlled and is intentionally independent from `evidence_level`.
- Facets are curation cues for filtering; exact task, split, metric, and failure claims remain in the paper notes.
- Evaluation profiles expose note-derived cues within each paper's recorded evidence scope. Abstract/project-only notes are not full-text protocol checks; profile coverage does not imply verified experiments.
- `benchmark_catalog.json` and `metric_catalog.json` remain cue-only navigation inputs; benchmark and metric cue lists in each profile retain that label.
- Reproducibility profiles distinguish manifest links from explicit note cues; a code/project URL does not prove executable reproduction.
- Lineage profiles cover every registry paper. Curated relations remain selective; queue adjacency and legacy-summary matches are non-relational candidates, not citation facts.
- Relation edges are directed curation links, not an exhaustive citation graph: a method points to a predecessor/data dependency, while a baseline points to the evaluated paper. Managed edges retain a basis, source, confidence, evidence scope, and review date.

