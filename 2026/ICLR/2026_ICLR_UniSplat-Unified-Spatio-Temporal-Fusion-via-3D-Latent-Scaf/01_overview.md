# UniSplat: Unified Spatio-Temporal Fusion via 3D Latent Scaffolds for Dynamic Driving Scene Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=Ng2VDbKD4r.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247830. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, sensor fusion, LiDAR, 3D Vision
- Official paper: https://openreview.net/forum?id=Ng2VDbKD4r
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/247830
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 EvolSplat (Miao et al., 2025) integrates multi-frame geometric information from front-view monocular sequences using 3D-CNN, but ignores semantic fusion and lacks mechanisms for dynamic handling.를 문제로 두고, In summary, our main contributions are as follows: • We introduce UniSplat, a novel feed-forward framework for dynamic scene reconstruction from multi-camera videos via a unified 3D latent scaffold. • We design ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Feed-forward 3D reconstruction for autonomous driving has advanced rapidly, yet existing methods struggle with the joint challenges of sparse, non-overlapping camera views and complex scene ...
- **p. 1 / ABSTRACT - extractive body cue:** We present UniSplat, a general feed-forward framework that learns robust dynamic scene reconstruction through unified latent spatio-temporal fusion.
- **p. 1 / ABSTRACT - extractive body cue:** UniSplat constructs a 3D latent scaffold, a structured representation that captures geometric and semantic scene context by leveraging pretrained foundation models.
- **p. 1 / ABSTRACT - extractive body cue:** To effectively integrate information across spatial views and temporal frames, we introduce an efficient fusion mechanism that operates directly within the 3D scaffold, enabling consistent ...
- **p. 1 / ABSTRACT - extractive body cue:** To ensure complete and detailed reconstructions, we design a dual-branch decoder that generates dynamic-aware Gaussians from the fused scaffold by combining point-anchored refinement with voxel-based ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** EvolSplat (Miao et al., 2025) integrates multi-frame geometric information from front-view monocular sequences using 3D-CNN, but ignores semantic fusion and lacks mechanisms for dynamic handling.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these challenges, we propose UniSplat, a general feed-forward framework for dynamic scene modeling from multi-camera videos.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our main contributions are as follows: • We introduce UniSplat, a novel feed-forward framework for dynamic scene reconstruction from multi-camera videos via a ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these challenges, we propose UniSplat, a general feed-forward framework for dynamic scene modeling from multi-camera videos.
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** To supervise the dynamic attributes of the Gaussians in Gt, we introduce a dynamics rendering mechanism that renders dynamic masks using the standard differentiable 15
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To enable faster inference, feed-forward reconstruction methods have emerged to synthesize novel views in a single forward pass (Xu et al., 2025; Chen et al., ...
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For a fair comparison, evaluation is performed by resizing our model's outputs to 224 × 400, aligning with the baseline's resolution before metric computation.
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For MVSplat, we initialize the model using its official weights pre-trained on RealEstate10K (Zhou et al., 2018).
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** The model is trained in a streaming manner using clips of 20 frames for 20 epochs, with an initial learning rate of 1.5 × 10-4 ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Experimental results demonstrate that our approach achieves state-of-the-art performance across both datasets in input-view reconstruction and novelview synthesis. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| State/latent | Experimental, demonstrate, achieves, state-of-the-art, performance, across, datasets, input-view, reconstruction, novelview, synthesis, Despite | geometry, map, object/relationship state | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/action | Despite these advances, robust reconstruction in urban driving scenarios remains challenging, particularly in maintaining a unified latent representation that evolves smoothly over time, handling partial observations, occlusions, and dy ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 16 (A.1 IMPLEMENTATION DETAILS) |
| Objective/outcome | To address the severe class imbalance in the dynamic segmentation loss, we incorporate a negative sampling strategy that randomly selects 50,000 negative pixels per sample for loss computation. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 15 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.1 IMPLEMENTATION DETAILS) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our main contributions are as follows: • We introduce UniSplat, a novel feed-forward framework for dynamic scene reconstruction from multi-camera videos via a ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these challenges, we propose UniSplat, a general feed-forward framework for dynamic scene modeling from multi-camera videos.
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** To supervise the dynamic attributes of the Gaussians in Gt, we introduce a dynamics rendering mechanism that renders dynamic masks using the standard differentiable 15
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To enable faster inference, feed-forward reconstruction methods have emerged to synthesize novel views in a single forward pass (Xu et al., 2025; Chen et al., ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** As shown in 1st and 2nd rows, the incorporation of spatial scaffold fusion, which aggregates spatial information in 3D space, improves performance by +0.36dB in ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** UniSplat consistently outperforms all baselines across every metric for both input view reconstruction and novel view synthesis.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We also report an variant (denoted by †), in which per-camera scales are set to optimal values derived from LiDAR pointmap, leading to additional improvements.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** This approach achieves a lower PSNR of 24.72dB, likely due to its limited ability to model dynamic elements and restricted temporal context.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Embodiment/environment | We conduct experiments on two large-scale autonomous driving benchmarks: Waymo Open (Sun et al., 2020) and nuScenes (Caesar et al., 2020) datasets. | hardware/simulator version and reset protocol | p. 6 (4 EXPERIMENTS), p. 16 (A.2 EFFICIENCY ANALYSIS) |
| Dataset/benchmark | We adopt image resolutions of 350 × 518 for the Waymo dataset and 224 × 406 for the nuScenes dataset. | role, split, size and leakage | p. 6 (4 EXPERIMENTS), p. 16 (A.2 EFFICIENCY ANALYSIS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Metric | Using only point-anchored Gaussians results in a performance degradation of 0.46 in PSNR, 0.02 in SSIM, and an increase of 0.08 in LPIPS error, underscoring the critical role of voxel-generated Gaussians in ... | definition, denominator, direction and uncertainty | p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Baseline/ablation | UniSplat consistently outperforms all baselines across every metric for both input view reconstruction and novel view synthesis. | fair input/data/compute/action matching | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 16 / A.3 MORE QUALITATIVE RESULTS - extractive body cue:** The third row illustrates a failure case in which a moving pedestrian is misclassified as static.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The voxel-only variant is excluded from comparison as it fails catastrophically at long-range rendering (Wei et al., 2025), yielding consistently poor performance across all metrics.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Specifically, replacing the default model with MoGe-2 (Wang et al., 2025e), a recently introduced open-domain geometry estimation method, yields consistent performance, which indicates that our ...
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Training is conducted with a batch size of 16 on 8 H20 GPUs for 40,000 iterations, as further training empirically degrades performance.
- **p. 17 / A.3 MORE QUALITATIVE RESULTS - extractive body cue:** The final dual-branch decoder effectively combines these complementary strengths, recovering sharp details while maintaining robust structural integrity in novel views.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 EvolSplat (Miao et al., 2025) integrates multi-frame geometric information from front-view monocular sequences using 3D-CNN, but ignores semantic fusion and lacks mechanisms for dynamic handling.를 문제로 두고, In summary, our main contributions are as follows: • We introduce UniSplat, a novel feed-forward framework for dynamic scene reconstruction from multi-camera videos via a unified 3D latent scaffold. • We design ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 15 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.1 IMPLEMENTATION DETAILS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
