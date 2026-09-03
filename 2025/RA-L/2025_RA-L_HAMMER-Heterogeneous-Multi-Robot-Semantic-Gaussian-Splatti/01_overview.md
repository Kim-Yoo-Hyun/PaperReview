# HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2501.14147.
> PDF retrieval source: https://arxiv.org/pdf/2501.14147. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Robotics, Gaussian Splatting, semantic
- Official paper: https://arxiv.org/abs/2501.14147
- Full-text retrieval: https://arxiv.org/pdf/2501.14147
- Code/Project: https://hammer-project.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Multi-robot mapping is useful for rapidly exploring new environments, but when combined with traditional 3D reconstruction methods, can be difficult to scale efficiently, especially for teams of heterogeneous robots that have a ...를 문제로 두고, A server-based architecture allows our method to be used with existing robot and edge device hardware without highpowered GPUs, while leveraging typical communication infrastructure (e.g.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian Splatting offers expressive scene reconstruction and can model a broad range of visual, geometric, and semantic information.
- **p. 1 / Abstract - extractive body cue:** However, efficient real-time map reconstruction with data streamed from multiple robots and devices remains a challenge.
- **p. 1 / Abstract - extractive body cue:** To that end, we propose HAMMER, a server-based multi-robot Gaussian Splatting method that leverages ROS communication infrastructure to generate 3D, metric-semantic maps from asynchronous robot ...
- **p. 1 / Abstract - extractive body cue:** HAMMER consists of (i) a one-time frame alignment module that transforms local SLAM poses and image data into a global frame and requires no prior ...
- **p. 1 / Abstract - extractive body cue:** HAMMER handles mixed perception modes, adjusts automatically for variations in image pre-processing among different devices, and distills CLIP semantic codes into the 3D scene for ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Multi-robot mapping is useful for rapidly exploring new environments, but when combined with traditional 3D reconstruction methods, can be difficult to scale efficiently, especially for ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Alternatively, 3DGS is a promising representation for multi-robot mapping because of its scalability to large environments [8], modeling fidelity, and generalization to a broad range ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** A server-based architecture allows our method to be used with existing robot and edge device hardware without highpowered GPUs, while leveraging typical communication infrastructure (e.g.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose HAMMER, Heterogeneous Asynchronous Multi-robot Mapping of Environmental Radiance.
- **p. 1 / I. INTRODUCTION - extractive body cue:** HAMMER enables a server communicating with a team of robots to construct a joint 3DGS map of an unknown environment.
- **p. 2 / I. INTRODUCTION - extractive body cue:** A shared map enables these robots to have comprehensive spatial awareness compared to their own local maps.
- **p. 3 / III. METHOD - extractive body cue:** If the fraction of matched features exceeds a fixed ratio ξ = 0.25 then the image pair is accepted as a potential inter-robot correspondence.
- **p. 3 / III. METHOD - extractive body cue:** To perform SfM, we use the COLMAP backend [18] with SuperPoint features and the SuperGlue matcher [28], which have exhibited robustness in aligning images from ...
- **p. 4 / III. METHOD - extractive body cue:** 1) Representation: 3DGS models the opacity and color of the environment using explicit Gaussian primitives, which are optimized based on a differentiable, tile-based rasterization process ...
- **p. 4 / III. METHOD - extractive body cue:** The point cloud is then directly used to supervise the feature field.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | During runtime, HAMMER rejects alignments where the localized SfM fails to estimate poses for all 2W input images or alignments that have high translation (0.1m in the map frame) or rotation errors ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (III. METHOD), p. 2 (III. METHOD) |
| State/latent | During, runtime, HAMMER, rejects, alignments, where, localized, SfM, fails, estimate, poses, input | geometry, map, object/relationship state | p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD) |
| Output/action | Each robot produces color images, geometric information (e.g. depth images or point clouds), and camera pose estimates in SE(3) with respect to an arbitrary local coordinate frame T i. | point map, pose, scene graph, affordance 또는 query result | p. 2 (III. METHOD), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION) |
| Objective/outcome | Equation (1) optimizes the scaling, rotation, and translation (s, R, t) between the two frames with a small regularization term on the rotation to address degenerate data. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** A server-based architecture allows our method to be used with existing robot and edge device hardware without highpowered GPUs, while leveraging typical communication infrastructure (e.g.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose HAMMER, Heterogeneous Asynchronous Multi-robot Mapping of Environmental Radiance.
- **p. 1 / I. INTRODUCTION - extractive body cue:** HAMMER enables a server communicating with a team of robots to construct a joint 3DGS map of an unknown environment.
- **p. 2 / I. INTRODUCTION - extractive body cue:** A shared map enables these robots to have comprehensive spatial awareness compared to their own local maps.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** HAMMER dramatically outperforms Di-NeRF* which fails to converge to accurate inter-robot alignments.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** HAMMER outperforms both baselines on all averaged metrics, and does so at least 25× faster than CPSLAM and 16× faster than MAGiC-SLAM.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Map quality over time for HAMMER and baselines in two scenes. HAMMER outperforms Di-NeRF*, demonstrating the necessity of accurate robot alignment. It also ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** First, we compare HAMMER to state-of-the-art baselines [13], [14] by assessing their reconstruction accuracy on the ReplicaMultiAgent dataset [14], [15].

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Embodiment/environment | However, ReplicaMultiAgent only contains scenes from simulated environments, and lacks heterogeneous robots/sensing devices and challenging real-world scene conditions (e.g. motion blur, diverse lighting). | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | Because both MAGiC-SLAM and CP-SLAM are not realtime capable, do not have publicly available code for integration with hardware/ROS, and do not support heterogeneous devices, we cannot compare these methods to HAMMER ... | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Metric | First, we compare HAMMER to state-of-the-art baselines [13], [14] by assessing their reconstruction accuracy on the ReplicaMultiAgent dataset [14], [15]. | definition, denominator, direction and uncertainty | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption) |
| Baseline/ablation | Fig. 5: Map quality over time for HAMMER and baselines in two scenes. HAMMER outperforms Di-NeRF*, demonstrating the necessity of accurate robot alignment. It also outperforms Individuals, highlighting the benefits of collaboration. ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images.
- **p. 5 / III. METHOD - extractive body cue:** 3) Pose Refinement: Although the alignment module produces robust estimates of the local-to-world transforms, it cannot account for gradual drift or other temporal noise.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** HAMMER dramatically outperforms Di-NeRF* which fails to converge to accurate inter-robot alignments.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Multi-robot mapping is useful for rapidly exploring new environments, but when combined with traditional 3D reconstruction methods, can be difficult to scale efficiently, especially for teams of heterogeneous robots that have a ...를 문제로 두고, A server-based architecture allows our method to be used with existing robot and edge device hardware without highpowered GPUs, while leveraging typical communication infrastructure (e.g.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Multi-robot mapping is useful for rapidly exploring new environments, but when combined with traditional 3D reconstruction methods, can be difficult to scale efficiently, especially for teams of heterogeneous robots that ... (p. 1, I. INTRODUCTION).
- **Actual contribution:** In this work, we propose HAMMER, Heterogeneous Asynchronous Multi-robot Mapping of Environmental Radiance. (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** Therefore, to showcase the generalizability of HAMMER and its real-time deployment in real-world environments, we also assess its performance in two different hardware trials with data collected using real robots. (p. 5, IV. EXPERIMENTS).
- **Explicit failure boundary:** 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images. (p. 6, IV. EXPERIMENTS).
