# Registry Statistics

- Generated: 2026-11-18 KST
- Source: [papers.json](../work/sources/papers.json)
- This is a generated diagnostic view; edit the manifest, tracker, or tier generator instead.

## Snapshot

- Papers: **1224**
- Resources in the combined view: **670**
- Curated relation edges: **50**
- Papers with outgoing relations: **41**
- Papers participating in a relation: **62**
- Structured evaluation profiles: **1224**
- Reproducibility profiles: **1224**
- Lineage coverage profiles: **1224**
- Papers with explicit trial/seed cues: **247**
- Papers without DOI/arXiv/OpenReview identifier: **366**

## Tier

| Value | Count |
|---|---:|
| REFERENCE | 508 |
| NEXT | 424 |
| ARCHIVE | 242 |
| CORE | 50 |

## Evidence level

| Value | Count |
|---|---:|
| FULL_TEXT_CHECKED | 968 |
| ABSTRACT_CHECKED | 256 |

## Reading status (intensive set)

| Value | Count |
|---|---:|
| UNREAD | 473 |
| READ | 1 |

## Reading status (inactive history; excluded from intensive denominator)

| Value | Count |
|---|---:|
| UNREAD | 43 |
| READ | 4 |

## Curation rationale status

| Value | Count |
|---|---:|
| recorded | 1224 |

## Curation roles

| Value | Count |
|---|---:|
| method | 963 |
| foundation | 124 |
| benchmark_or_dataset | 99 |
| system | 40 |

## Publication kind

| Value | Count |
|---|---:|
| conference | 1044 |
| journal | 87 |
| preprint | 86 |
| technical_report | 4 |
| workshop | 2 |
| other | 1 |

## Identifier status

| Value | Count |
|---|---:|
| identified | 858 |
| source_only | 366 |

## Primary source scope

| Value | Count |
|---|---:|
| paper_specific | 1181 |
| venue_index | 43 |

## Code status

| Value | Count |
|---|---:|
| not_identified | 621 |
| project_only | 314 |
| released | 250 |
| not_released | 39 |

## Data status

| Value | Count |
|---|---:|
| not_identified | 1050 |
| not_applicable | 103 |
| released | 69 |
| not_released | 2 |

## Evaluation type

| Value | Count |
|---|---:|
| EMPIRICAL / REAL-ROBOT OR HARDWARE | 447 |
| not_recorded | 275 |
| EMPIRICAL / SOURCE-REPORTED EVALUATION | 274 |
| SYSTEM / EVALUATION SCOPE UNRESOLVED | 95 |
| BENCHMARK / DATASET | 69 |
| EMPIRICAL / SIMULATION | 64 |

## Evaluation setting

| Value | Count |
|---|---:|
| real_robot | 447 |
| not_recorded | 275 |
| source_reported | 274 |
| scope_unresolved | 95 |
| benchmark_or_dataset | 69 |
| simulation | 64 |

## Evaluation protocol status

| Value | Count |
|---|---:|
| trials_or_seeds=not_recorded | 977 |
| dataset_or_benchmark=reported | 948 |
| metrics=reported | 948 |
| statistics=reported | 940 |
| baselines=reported | 939 |
| split_or_generalization=reported | 927 |
| failure_cases=reported | 927 |
| ablations=reported | 920 |
| split_or_generalization=not_recorded | 297 |
| failure_cases=not_recorded | 297 |
| dataset_or_benchmark=not_recorded | 276 |
| metrics=not_recorded | 275 |
| baselines=not_recorded | 275 |
| ablations=not_recorded | 275 |
| statistics=not_recorded | 275 |
| trials_or_seeds=reported | 247 |
| ablations=not_reported | 29 |
| baselines=not_reported | 10 |
| statistics=not_reported | 9 |
| metrics=not_reported | 1 |

## Reproducibility profile

| Value | Count |
|---|---:|
| metadata_audited | 1224 |

## Checkpoint status

| Value | Count |
|---|---:|
| not_recorded | 1214 |
| reported | 10 |

## Configuration status

| Value | Count |
|---|---:|
| reported | 949 |
| not_recorded | 275 |

## Environment status

| Value | Count |
|---|---:|
| reported | 949 |
| not_recorded | 275 |

## Run-condition status

| Value | Count |
|---|---:|
| reported | 940 |
| not_recorded | 284 |

## Lineage coverage status

| Value | Count |
|---|---:|
| no_curated_edge_recorded | 893 |
| candidate_only | 269 |
| curated_edges | 62 |

## Relation type

| Value | Count |
|---|---:|
| extends | 27 |
| builds_on | 13 |
| baseline_for | 6 |
| uses_dataset | 4 |

## Relation confidence

| Value | Count |
|---|---:|
| verified | 26 |
| inferred | 18 |
| manual | 6 |

## Relation evidence scope

| Value | Count |
|---|---:|
| paper_body | 28 |
| title_lineage | 16 |
| official_project | 4 |
| official_abstract | 2 |

## Curated relation edges

The manifest is the source of truth; this table is a compact human-readable edge view.

| From paper | Relation | To paper | Confidence | Evidence scope |
|---|---|---|---|---|
| `pr-0011` 3D Gaussian Splatting for Real-Time Radiance Field Rendering | `builds_on` | `pr-0010` NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis | `inferred` | `paper_body` |
| `pr-0013` PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space | `extends` | `pr-0012` PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation | `verified` | `official_abstract` |
| `pr-0016` ORB-SLAM: A Versatile and Accurate Monocular SLAM System | `builds_on` | `pr-0525` PTAM: Parallel Tracking and Mapping for Small AR Workspaces | `verified` | `paper_body` |
| `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `baseline_for` | `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `verified` | `paper_body` |
| `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `baseline_for` | `pr-0577` Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching | `verified` | `paper_body` |
| `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `baseline_for` | `pr-0751` Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation | `verified` | `paper_body` |
| `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `baseline_for` | `pr-0897` CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity | `verified` | `paper_body` |
| `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `baseline_for` | `pr-0924` FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation | `verified` | `paper_body` |
| `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `builds_on` | `pr-0008` Denoising Diffusion Probabilistic Models | `verified` | `paper_body` |
| `pr-0022` RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | `extends` | `pr-0021` RT-1: Robotics Transformer for Real-World Control at Scale | `inferred` | `title_lineage` |
| `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `uses_dataset` | `pr-0024` Open X-Embodiment: Robotic Learning Datasets and RT-X Models | `manual` | `paper_body` |
| `pr-0051` OpenVLA: An Open-Source Vision-Language-Action Model | `uses_dataset` | `pr-0732` DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset | `verified` | `paper_body` |
| `pr-0052` Octo: An Open-Source Generalist Robot Policy | `uses_dataset` | `pr-0024` Open X-Embodiment: Robotic Learning Datasets and RT-X Models | `manual` | `paper_body` |
| `pr-0061` π0.5: a Vision-Language-Action Model with Open-World Generalization | `extends` | `pr-0746` π0: A Vision-Language-Action Flow Model for General Robot Control | `manual` | `title_lineage` |
| `pr-0084` ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY | `extends` | `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `verified` | `paper_body` |
| `pr-0137` SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space | `extends` | `pr-0019` Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | `verified` | `paper_body` |
| `pr-0524` Proximal Policy Optimization Algorithms | `extends` | `pr-0615` Trust Region Policy Optimization | `verified` | `official_abstract` |
| `pr-0577` Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching | `builds_on` | `pr-0745` Flow Matching for Generative Modeling | `verified` | `paper_body` |
| `pr-0615` Trust Region Policy Optimization | `builds_on` | `pr-0838` Policy Gradient Methods for Reinforcement Learning with Function Approximation | `inferred` | `paper_body` |
| `pr-0618` Constrained Policy Optimization | `extends` | `pr-0615` Trust Region Policy Optimization | `verified` | `paper_body` |
| `pr-0746` π0: A Vision-Language-Action Flow Model for General Robot Control | `builds_on` | `pr-0745` Flow Matching for Generative Modeling | `verified` | `paper_body` |
| `pr-0746` π0: A Vision-Language-Action Flow Model for General Robot Control | `uses_dataset` | `pr-0024` Open X-Embodiment: Robotic Learning Datasets and RT-X Models | `verified` | `paper_body` |
| `pr-0748` PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning | `extends` | `pr-0834` FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning | `inferred` | `title_lineage` |
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
| `pr-1161` GRAD-NAV++: Vision-Language Model Enabled Visual Drone Navigation With Gaussian Radiance Fields and Differentiable Dynamics | `extends` | `pr-0290` GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics | `manual` | `official_project` |

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

