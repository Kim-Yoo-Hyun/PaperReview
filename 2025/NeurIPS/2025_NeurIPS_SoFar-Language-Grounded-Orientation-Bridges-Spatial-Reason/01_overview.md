# SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (46 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=kmv7yg6QXv.
> PDF retrieval source: https://arxiv.org/pdf/2502.13143. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, 3D Vision
- Official paper: https://openreview.net/forum?id=kmv7yg6QXv
- Full-text retrieval: https://arxiv.org/pdf/2502.13143
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (46 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, translating a specific language description into a desired orientation is challenging for existing VLMs.를 문제로 두고, We propose PointSO, a generalizable cross-modal 3D Transformer [114, 26, 89, 91] for semantic orientation prediction.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** While spatial reasoning has made progress in object localization relationships, it often overlooks object orientation-a key factor in 6-DoF fine-grained manipulation.
- **p. 1 / Abstract - extractive body cue:** Traditional pose representations rely on pre-defined frames or templates, limiting generalization and semantic grounding.
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce the concept of semantic orientation, which defines object orientations using natural language in a reference-frame-free manner (e.g., the "plug-in" direction ...
- **p. 1 / Abstract - extractive body cue:** To support this, we construct OrienText300K, a large-scale dataset of 3D objects annotated with semantic orientations, and develop PointSO, a general model for zero-shot semantic ...
- **p. 1 / Abstract - extractive body cue:** By integrating semantic orientation into VLM agents, our SOFAR framework enables 6-DoF spatial reasoning and generates robotic actions.
- **p. 2 / 1 Introduction - extractive body cue:** However, translating a specific language description into a desired orientation is challenging for existing VLMs.
- **p. 4 / 1 Introduction - extractive body cue:** Data Annotation As mentioned in the introduction, VLMs struggle to produce accurate object orientation values, which presents a significant challenge for data generation.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We propose PointSO, a generalizable cross-modal 3D Transformer [114, 26, 89, 91] for semantic orientation prediction.
- **p. 2 / 1 Introduction - extractive body cue:** In addition, we introduce Open6DOR V2, a large-scale benchmark for 6-DoF object rearrangement in simulation, which supports both open-loop and closed-loop control.
- **p. 3 / 1 Introduction - extractive body cue:** Finally, we present two new benchmarks, Open6DOR V2 and 6-DoF SpatialBench, to evaluate 6-DoF rearrangement and spatial reasoning.
- **p. 3 / 1 Introduction - extractive body cue:** To support this, we introduce OrienText300K, a curated dataset of 3D models annotated with diverse language-guided orientation labels.
- **p. 5 / 1 Introduction - extractive body cue:** This enriched spatial representation enables the VLM to perform accurate spatial reasoning by leveraging its visual and linguistic understanding.
- **p. 4 / 1 Introduction - extractive body cue:** For the 3D point clouds, we follow [26, 136, 89] to first sample Ns seed points using farthest point sampling (FPS) and then group inputs ...
- **p. 5 / 1 Introduction - extractive body cue:** Position & Orientation Information Extraction Given a language query Q, we first prompt a visionlanguage model FVLM to extract a task-relevant set of object phrases ...
- **p. 3 / 1 Introduction - extractive body cue:** In summary, we propose Semantic Orientation as a new representation that bridges spatial reasoning and robotic manipulation, enabling open-vocabulary, template-free orientation understanding for unseen objects.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | X Y Z Pose Estimation Category / Instance Template Needed Only axis, the relationship with instruction is unclear "Blow Wind" "Top" "Back" "Pick up" "Fan" "Front" Semantic Orientation Without any template Training ... | image/video, language instruction, proprioception과 history | p. 2 (Abstract), p. 4 (1 Introduction) |
| State/latent | Pose, Estimation, Category, Instance, Template, Needed, Only, axis, relationship, instruction, unclear, Blow | language-grounded task state와 action-policy context | p. 2 (Abstract), p. 4 (1 Introduction), p. 4 (1 Introduction) |
| Output/action | For the 3D point clouds, we follow [26, 136, 89] to first sample Ns seed points using farthest point sampling (FPS) and then group inputs with KNN for point feature embedding with ... | continuous action, pose 또는 action chunk | p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction) |
| Objective/outcome | The optimization is to minimize the negative cosine similarity Lcos(v, k) = 1 - v·k ∥v∥·∥k∥between predicted and the ground truth semantic orientations: min θSO X Xi∈DOrienText300K X ℓi j∈Li Lcos  ... | instruction following, task success, generalization과 latency | p. 4 (1 Introduction), p. 2 (1 Introduction), p. 6 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We propose PointSO, a generalizable cross-modal 3D Transformer [114, 26, 89, 91] for semantic orientation prediction.
- **p. 2 / 1 Introduction - extractive body cue:** In addition, we introduce Open6DOR V2, a large-scale benchmark for 6-DoF object rearrangement in simulation, which supports both open-loop and closed-loop control.
- **p. 3 / 1 Introduction - extractive body cue:** Finally, we present two new benchmarks, Open6DOR V2 and 6-DoF SpatialBench, to evaluate 6-DoF rearrangement and spatial reasoning.
- **p. 3 / 1 Introduction - extractive body cue:** To support this, we introduce OrienText300K, a curated dataset of 3D models annotated with diverse language-guided orientation labels.
- **p. 5 / 1 Introduction - extractive body cue:** This enriched spatial representation enables the VLM to perform accurate spatial reasoning by leveraging its visual and linguistic understanding.
- **p. 9 / 4 Experiments - extractive body cue:** SOFAR consistently outperforms other methods across both tracks, achieving over 18% improvement.
- **p. 8 / 4 Experiments - extractive body cue:** SOFAR achieves the best performance, demonstrating strong spatial understanding and zero-shot generalization.
- **p. 8 / 4 Experiments - extractive body cue:** We note that certain objects are intrinsically difficult to manipulate, suggesting the need for more robust policies incorporating prehensile grasping and adaptive strategies to improve ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Embodiment/environment | We migrate its scenes into a robosuite-based simulation environment [151], following the task interface defined by LIBERO [64], and name this new benchmark Open6DOR V2. | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | Our PointSO model, integrated within the SOFAR system, demonstrates strong performance in both simulated and real-world robotic manipulation tasks. | role, split, size and leakage | p. 8 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Metric | We present success rates for the "Variant Aggregation" and "Visual Matching" approaches. | definition, denominator, direction and uncertainty | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Baseline/ablation | 7, SOFAR consistently outperforms baselines across all tracks, especially on orientation and 6-DoF tasks, while maintaining low planning overhead. | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4 Experiments - extractive body cue:** 5 Limitations & Conclusions One notable limitation for decoupled systems like SOFAR is that the execution may fail due to a sub-module error, as shown ...
- **p. 8 / 4 Experiments - extractive body cue:** Furthermore, leveraging the error detection and re-planning capabilities of VLMs [48, 1], we can make multiple attempts following a single-step execution failure to approximately achieve ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 16: Failure case distribution analysis of our SOFAR. C
- **p. 6 / 1 Introduction - extractive body cue:** We employ OMPL [103] to generate a collision-free trajectory, initializing joint positions at the midpoint to ensure smooth and safe motion.
- **p. 7 / 4 Experiments - extractive body cue:** To evaluate the robustness of PointSO under such conditions, we introduce three types of input perturbations: random rotations, partial single-sided observations, and Gaussian noise.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Semantic Orientation evaluation of robustness. Single-View: randomly select a camera viewpoint within the unit sphere and generate a single FoV viewpoint in polar ...
- **p. 9 / 4 Experiments - extractive body cue:** Future works include integrating scalable data and more advanced models and exploring the potential of combining end-to-end and such decoupled methods, and expanding SOFAR to ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, translating a specific language description into a desired orientation is challenging for existing VLMs.를 문제로 두고, We propose PointSO, a generalizable cross-modal 3D Transformer [114, 26, 89, 91] for semantic orientation prediction.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
