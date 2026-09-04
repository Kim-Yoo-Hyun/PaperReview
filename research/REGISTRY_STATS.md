# Registry Statistics

- Generated: 2026-09-04 KST
- Source: [papers.json](../work/sources/papers.json)
- This is a generated diagnostic view; edit the manifest, tracker, or tier generator instead.

## Snapshot

- Papers: **950**
- Resources in the combined view: **439**
- Curated relation edges: **49**
- Papers with outgoing relations: **40**
- Papers participating in a relation: **60**
- Structured evaluation profiles: **950**
- Reproducibility profiles: **950**
- Lineage coverage profiles: **950**
- Papers with explicit trial/seed cues: **248**
- Papers without DOI/arXiv/OpenReview identifier: **343**

## Tier

| Value | Count |
|---|---:|
| REFERENCE | 397 |
| ARCHIVE | 242 |
| NEXT | 234 |
| CORE | 77 |

## Evidence level

| Value | Count |
|---|---:|
| FULL_TEXT_CHECKED | 950 |

## Reading status (intensive set)

| Value | Count |
|---|---:|
| UNREAD | 306 |
| READ | 5 |

## Curation rationale status

| Value | Count |
|---|---:|
| recorded | 950 |

## Curation roles

| Value | Count |
|---|---:|
| method | 750 |
| foundation | 110 |
| benchmark_or_dataset | 68 |
| system | 22 |

## Publication kind

| Value | Count |
|---|---:|
| conference | 858 |
| journal | 63 |
| preprint | 24 |
| technical_report | 4 |
| workshop | 1 |

## Identifier status

| Value | Count |
|---|---:|
| identified | 607 |
| source_only | 343 |

## Primary source scope

| Value | Count |
|---|---:|
| paper_specific | 907 |
| venue_index | 43 |

## Code status

| Value | Count |
|---|---:|
| not_identified | 537 |
| project_only | 277 |
| released | 110 |
| not_released | 26 |

## Data status

| Value | Count |
|---|---:|
| not_identified | 783 |
| not_applicable | 102 |
| released | 63 |
| not_released | 2 |

## Evaluation type

| Value | Count |
|---|---:|
| EMPIRICAL / REAL-ROBOT OR HARDWARE | 448 |
| EMPIRICAL / SOURCE-REPORTED EVALUATION | 274 |
| SYSTEM / EVALUATION SCOPE UNRESOLVED | 95 |
| BENCHMARK / DATASET | 69 |
| EMPIRICAL / SIMULATION | 64 |

## Evaluation setting

| Value | Count |
|---|---:|
| real_robot | 448 |
| source_reported | 274 |
| scope_unresolved | 95 |
| benchmark_or_dataset | 69 |
| simulation | 64 |

## Evaluation protocol status

| Value | Count |
|---|---:|
| dataset_or_benchmark=reported | 949 |
| metrics=reported | 949 |
| statistics=reported | 941 |
| baselines=reported | 940 |
| split_or_generalization=reported | 928 |
| failure_cases=reported | 928 |
| ablations=reported | 921 |
| trials_or_seeds=not_recorded | 702 |
| trials_or_seeds=reported | 248 |
| ablations=not_reported | 29 |
| split_or_generalization=not_recorded | 22 |
| failure_cases=not_recorded | 22 |
| baselines=not_reported | 10 |
| statistics=not_reported | 9 |
| dataset_or_benchmark=not_recorded | 1 |
| metrics=not_reported | 1 |

## Reproducibility profile

| Value | Count |
|---|---:|
| metadata_audited | 950 |

## Checkpoint status

| Value | Count |
|---|---:|
| not_recorded | 943 |
| reported | 7 |

## Configuration status

| Value | Count |
|---|---:|
| reported | 950 |

## Environment status

| Value | Count |
|---|---:|
| reported | 950 |

## Run-condition status

| Value | Count |
|---|---:|
| reported | 941 |
| not_recorded | 9 |

## Lineage coverage status

| Value | Count |
|---|---:|
| no_curated_edge_recorded | 622 |
| candidate_only | 268 |
| curated_edges | 60 |

## Relation type

| Value | Count |
|---|---:|
| extends | 26 |
| builds_on | 13 |
| baseline_for | 6 |
| uses_dataset | 4 |

## Relation confidence

| Value | Count |
|---|---:|
| verified | 26 |
| inferred | 18 |
| manual | 5 |

## Relation evidence scope

| Value | Count |
|---|---:|
| paper_body | 28 |
| title_lineage | 16 |
| official_project | 3 |
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

## Note evidence gaps

| Note | Missing evidence header |
|---|---:|

## Interpretation

- `reading_status` is user-controlled and is intentionally independent from `evidence_level`.
- Facets are curation cues for filtering; exact task, split, metric, and failure claims remain in the paper notes.
- Evaluation profiles expose body-derived section cues and raw trial/seed evidence; they do not replace paper-specific protocol verification.
- `benchmark_catalog.json` and `metric_catalog.json` remain cue-only navigation inputs; benchmark and metric cue lists in each profile retain that label.
- Reproducibility profiles distinguish manifest links from explicit note cues; a code/project URL does not prove executable reproduction.
- Lineage profiles cover every registry paper. Curated relations remain selective; queue adjacency and legacy-summary matches are non-relational candidates, not citation facts.
- Relation edges are directed curation links, not an exhaustive citation graph: a method points to a predecessor/data dependency, while a baseline points to the evaluated paper. Managed edges retain a basis, source, confidence, evidence scope, and review date.

