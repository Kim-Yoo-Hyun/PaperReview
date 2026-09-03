# EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=Lf0W2gmNBg.
> PDF retrieval source: https://arxiv.org/pdf/2512.00771. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://openreview.net/forum?id=Lf0W2gmNBg
- Full-text retrieval: https://arxiv.org/pdf/2512.00771
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, in real-world applications such as autonomous driving in the wild, which often involve fast motion and rapidly changing illumination, RGB cameras-dependent on long exposure times for imaging-face significant challenges, includi ...를 문제로 두고, In this paper, we propose EAG3R, an event-augemented MonST3R framework to enhance pointmapbased 3D geometry estimation under dynamic and extremely low-light conditions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robust 3D geometry estimation from videos is critical for applications such as autonomous navigation, SLAM, and 3D scene reconstruction.
- **p. 1 / Abstract - extractive body cue:** Recent methods like DUSt3R demonstrate that regressing dense pointmaps from image pairs enables accurate and efficient pose-free reconstruction.
- **p. 1 / Abstract - extractive body cue:** However, existing RGB-only approaches struggle under real-world conditions involving dynamic objects and extreme illumination, due to the inherent limitations of conventional cameras.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose EAG3R, a novel geometry estimation framework that augments pointmap-based reconstruction with asynchronous event streams.
- **p. 1 / Abstract - extractive body cue:** Built upon the MonST3R backbone, EAG3R introduces two key innovations: (1) a retinex-inspired image enhancement module and a lightweight event adapter with SNR-aware fusion mechanism ...
- **p. 1 / 1 Introduction - extractive body cue:** However, in real-world applications such as autonomous driving in the wild, which often involve fast motion and rapidly changing illumination, RGB cameras-dependent on long exposure ...
- **p. 1 / 1 Introduction - extractive body cue:** Estimating geometry from videos or images is a fundamental problem in 3D vision, with broad applications in camera pose estimation, novel view synthesis, geometry reconstruction, ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose EAG3R, an event-augemented MonST3R framework to enhance pointmapbased 3D geometry estimation under dynamic and extremely low-light conditions.
- **p. 1 / 1 Introduction - extractive body cue:** Recent methods like DUSt3R [64] have shown that regressing dense pointmaps from image pairs using transformer-based foundation models enables accurate and efficient pose-free 3D reconstruction.
- **p. 2 / 1 Introduction - extractive body cue:** This unified representation enables efficient downstream tasks such as depth estimation and camera pose estimation, under challenging lighting conditions. and neural rendering [48, 25], but ...
- **p. 1 / 1 Introduction - extractive body cue:** Estimating geometry from videos or images is a fundamental problem in 3D vision, with broad applications in camera pose estimation, novel view synthesis, geometry reconstruction, ...
- **p. 19 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** These features provide high-confidence geometric constraints and enhance convergence in the optimization of camera pose and structure.
- **p. 19 / A.5.4 Feature Strategy for Global Optimization - extractive body cue:** To improve the stability of global optimization, the feature selection strategy in EAG3R focuses on Harris corners, which represent sparse yet highly stable points with ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | EAG3R Input low light video Input event stream Lalign Lflow Lsmooth Levent Pointmaps Variables of Optimization {X, P, K} Depth Camera Pose Camera Intrinsics Object Motion 4D Reconstruction Trajectories Figure 1: EAG3R ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| State/latent | EAG3R, Input, light, video, event, stream, Lalign, Lflow, Lsmooth, Levent, Pointmaps, Variables | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | Estimating geometry from videos or images is a fundamental problem in 3D vision, with broad applications in camera pose estimation, novel view synthesis, geometry reconstruction, and 3D perception. | point map, pose, scene graph, affordance 또는 query result | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Objective/outcome | These features provide high-confidence geometric constraints and enhance convergence in the optimization of camera pose and structure. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 19 (A.5.4 Feature Strategy for Global Optimization), p. 19 (A.5.4 Feature Strategy for Global Optimization), p. 20 (A.5.4 Feature Strategy for Global Optimization) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose EAG3R, an event-augemented MonST3R framework to enhance pointmapbased 3D geometry estimation under dynamic and extremely low-light conditions.
- **p. 1 / 1 Introduction - extractive body cue:** Recent methods like DUSt3R [64] have shown that regressing dense pointmaps from image pairs using transformer-based foundation models enables accurate and efficient pose-free 3D reconstruction.
- **p. 2 / 1 Introduction - extractive body cue:** This unified representation enables efficient downstream tasks such as depth estimation and camera pose estimation, under challenging lighting conditions. and neural rendering [48, 25], but ...
- **p. 1 / 1 Introduction - extractive body cue:** Estimating geometry from videos or images is a fundamental problem in 3D vision, with broad applications in camera pose estimation, novel view synthesis, geometry reconstruction, ...
- **p. 9 / 4 Experiments - extractive body cue:** Each addition improves performance, with the full EAG3R system achieving the best results.
- **p. 7 / 4 Experiments - extractive body cue:** Fine-tuning MonST3R improves its performance across 7
- **p. 7 / 4 Experiments - extractive body cue:** However, applying RetinexFormer, a widely used image enhancement network, as a preprocessing light-up step (denoted as (LightUp)) does not yield significant improvements and, in some ...
- **p. 8 / 4 Experiments - extractive body cue:** 2, RGB-only baselines such as DUSt3R fail under extreme low-light conditions, while MonST3R offers improved results.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (4 Experiments), p. 7 (4 Experiments) |
| Embodiment/environment | To assess the model's performance in high-dynamic-range (HDR) conditions, we evaluated EAG3R on the challenging M3ED robot dog dataset penno_plaza_lights split, which features rapid motion and severe illumination fluctuations. | hardware/simulator version and reset protocol | p. 21 (A.7 Generalization to More Datasets), p. 18 (A.4 Summary of Existing Event-RGB Datasets) |
| Dataset/benchmark | Dataset Low-light Dynamic RGB Depth Sensor GT Pose Platform Environment DSEC ✓ ✓ ✓ LiDAR-16 ✗ Car Outdoor UZH-FPV ✗ ✓ ✓ ✗ MoCap Drone Indoor/Outdoor DAVIS 240C ✗ ✓ ✓ ✗ ... | role, split, size and leakage | p. 21 (A.7 Generalization to More Datasets), p. 18 (A.4 Summary of Existing Event-RGB Datasets), p. 18 (A.4 Summary of Existing Event-RGB Datasets), p. 21 (A.7 Generalization to More Datasets) |
| Metric | We report results using standard metrics: Absolute Relative Error (Abs Rel ↓), Scale-invariant RMSE log (RMSE log ↓), and the threshold accuracy δ < 1.25 (↑), where lower is better for error ... | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 17 (A.2 Video Depth Estimation Results on MVSEC), p. 17 (A.2 Video Depth Estimation Results on MVSEC) |
| Baseline/ablation | Our method, EAG3R, outperforms all baselines across all three nighttime sequences, indicating both accurate and reliable depth predictions. | fair input/data/compute/action matching | p. 8 (4 Experiments), p. 20 (A.6 Runtime and Memory Analysis), p. 21 (A.7 Generalization to More Datasets) |

## Explicit Limitations and Failure Boundary

- **p. 22 / A.9 Limitations - extractive body cue:** In particular, we attempted to train our model using synthetic events generated by V2E [20], but observed that the low fidelity of these generated events ...
- **p. 9 / 5 Conclusion - extractive body cue:** We discuss limitations and broader impact in the appendix.
- **p. 21 / A.9 Limitations - extractive body cue:** Despite the strong empirical performance of EAG3R, several limitations remain: Limited dataset availability.
- **p. 21 / A.9 Limitations - extractive body cue:** To address this, our future work aims to curate a diverse dataset featuring high-quality, real-world event-RGB pairs across varied lighting and motion scenarios.
- **p. 7 / 4 Experiments - extractive body cue:** However, applying RetinexFormer, a widely used image enhancement network, as a preprocessing light-up step (denoted as (LightUp)) does not yield significant improvements and, in some ...
- **p. 9 / 5 Conclusion - extractive body cue:** We presented EAG3R, a event-augmented framework for robust 3D geometry estimation under dynamic and low-light conditions.
- **p. 22 / A.9 Limitations - extractive body cue:** Metric Night1 Night2 Night3 Abs Rel ↓ δ < 1.25 ↑ RMSE log ↓ Abs Rel ↓ δ < 1.25 ↑ RMSE log ↓ Abs ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, in real-world applications such as autonomous driving in the wild, which often involve fast motion and rapidly changing illumination, RGB cameras-dependent on long exposure times for imaging-face significant challenges, includi ...를 문제로 두고, In this paper, we propose EAG3R, an event-augemented MonST3R framework to enhance pointmapbased 3D geometry estimation under dynamic and extremely low-light conditions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 19 (A.5.4 Feature Strategy for Global Optimization), p. 19 (A.5.4 Feature Strategy for Global Optimization), p. 9 (4 Experiments) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
