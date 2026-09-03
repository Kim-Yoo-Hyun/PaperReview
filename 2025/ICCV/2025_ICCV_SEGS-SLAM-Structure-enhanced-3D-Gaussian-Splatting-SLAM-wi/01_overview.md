# SEGS-SLAM: Structure-enhanced 3D Gaussian Splatting SLAM with Appearance Embedding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wen_SEGS-SLAM_Structure-enhanced_3D_Gaussian_Splatting_SLAM_with_Appearance_Embedding_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wen_SEGS-SLAM_Structure-enhanced_3D_Gaussian_Splatting_SLAM_with_Appearance_Embedding_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, geometry, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Wen_SEGS-SLAM_Structure-enhanced_3D_Gaussian_Splatting_SLAM_with_Appearance_Embedding_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Wen_SEGS-SLAM_Structure-enhanced_3D_Gaussian_Splatting_SLAM_with_Appearance_Embedding_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, AE has a notable limitation: its training involves each ground-truth image from the test set.를 문제로 두고, Second, we propose Appearancefrom-Motion embedding (AfME), which takes poses as input and eliminates the need for training on the left half of each ground-truth image in the test set.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian splatting (3D-GS) has recently revolutionized novel view synthesis in the simultaneous localization and mapping (SLAM) problem.
- **p. 1 / Abstract - extractive body cue:** However, most existing algorithms fail to fully capture the underlying structure, resulting in structural inconsistency.
- **p. 1 / Abstract - extractive body cue:** Additionally, they struggle with abrupt appearance variations, leading to inconsistent visual quality.
- **p. 1 / Abstract - extractive body cue:** To address these problems, we propose SEGS-SLAM, a structure-enhanced 3D Gaussian Splatting SLAM, which achieves high-quality photorealistic mapping.
- **p. 1 / Abstract - extractive body cue:** Our main contributions are two-fold.
- **p. 2 / 1. Introduction - extractive body cue:** However, AE has a notable limitation: its training involves each ground-truth image from the test set.
- **p. 2 / 1. Introduction - extractive body cue:** To address the above limitations, this paper presents SEGS-SLAM, a novel 3D Gaussian Splatting SLAM system.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Second, we propose Appearancefrom-Motion embedding (AfME), which takes poses as input and eliminates the need for training on the left half of each ground-truth image ...
- **p. 2 / 1. Introduction - extractive body cue:** Motivated by this, we propose a structure-enhanced photorealistic mapping (SEPM) framework, which initializes anchor points using ORB-SLAM3 [3] point cloud, significantly enhancing the utilization of ...
- **p. 1 / Abstract - extractive body cue:** To address these problems, we propose SEGS-SLAM, a structure-enhanced 3D Gaussian Splatting SLAM, which achieves high-quality photorealistic mapping.
- **p. 1 / Abstract - extractive body cue:** Second, we propose Appearance-from-Motion embedding (AfME), enabling 3D Gaussians to better model image appearance variations across different camera poses.
- **p. 4 / 4. SEGS-SLAM - extractive body cue:** Visualization of the Photo-SLAM's 3D Gaussians and of our method's anchor points using only SEPM after 30k iterations.
- **p. 4 / 4.2. Appearance-from-Motion Embedding - extractive body cue:** To address this issue, we propose Appearance-from-Motion embedding (AfME), which employs a lightweight Multilayer Perceptron (MLP) Mθa to learn a shared appearance representation.
- **p. 4 / 4.1. Structure-Enhanced Photorealistic Mapping - extractive body cue:** Based on this observation, we propose incrementally voxelizing the point cloud Pk of each keyframe to construct anchor points, as follows: Vk = {⌊Pk ϵ ...
- **p. 1 / 1. Introduction - extractive body cue:** However, most SLAM algorithms based on 3D-GS have neglected the latent structure in the scene, which constrains their rendering quality.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Based on this observation, we propose incrementally voxelizing the point cloud Pk of each keyframe to construct anchor points, as follows: Vk = {⌊Pk ϵ ⌉} · ϵ, (6) where Vk ∈RN×3 ... | camera/depth stream, pose, map와 language goal | p. 4 (4.1. Structure-Enhanced Photorealistic Mapping), p. 2 (1. Introduction) |
| State/latent | observation, incrementally, voxelizing, point, cloud, keyframe, construct, anchor, points, follows, where, denotes | robot pose, free-space/semantic map와 local goal | p. 4 (4.1. Structure-Enhanced Photorealistic Mapping), p. 2 (1. Introduction), p. 4 (2.1 Test on the right half of each) |
| Output/action | Second, we propose Appearancefrom-Motion embedding (AfME), which takes poses as input and eliminates the need for training on the left half of each ground-truth image in the test set. | collision-free trajectory 또는 velocity command | p. 2 (1. Introduction), p. 4 (2.1 Test on the right half of each), p. 5 (4.2. Appearance-from-Motion Embedding) |
| Objective/outcome | The optimization of the learnable parameters, the MLP Mα, Mc, Mq, Ms, and Mθa, are achieved by minimizing the L1 loss L1, SSIM term [40] LSSIM, frequency regularization Lhf, and volume regularization ... | goal reach, safety, localization error와 replanning latency | p. 5 (4.4. Losses Design), p. 3 (3.2. Localization and Geometry Mapping), p. 4 (4. SEGS-SLAM) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Second, we propose Appearancefrom-Motion embedding (AfME), which takes poses as input and eliminates the need for training on the left half of each ground-truth image ...
- **p. 2 / 1. Introduction - extractive body cue:** Motivated by this, we propose a structure-enhanced photorealistic mapping (SEPM) framework, which initializes anchor points using ORB-SLAM3 [3] point cloud, significantly enhancing the utilization of ...
- **p. 1 / Abstract - extractive body cue:** To address these problems, we propose SEGS-SLAM, a structure-enhanced 3D Gaussian Splatting SLAM, which achieves high-quality photorealistic mapping.
- **p. 1 / Abstract - extractive body cue:** Second, we propose Appearance-from-Motion embedding (AfME), enabling 3D Gaussians to better model image appearance variations across different camera poses.
- **p. 4 / 4. SEGS-SLAM - extractive body cue:** Visualization of the Photo-SLAM's 3D Gaussians and of our method's anchor points using only SEPM after 30k iterations.
- **p. 7 / 5.2. Results Analysis - extractive body cue:** The best results are marked as best score , second best score and third best score . '-' denotes that the system does not provide ...
- **p. 6 / 5.2. Results Analysis - extractive body cue:** 1, where SEGS-SLAM significantly outperforms comparison methods, achieving the highest average rendering quality on both TUM RGB-D and Replica datasets.
- **p. 7 / 5.2. Results Analysis - extractive body cue:** Notably, SEGS-SLAM continues to significantly outperform comparison methods on the TUM RGB-D dataset.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (5.2. Results Analysis), p. 6 (5.2. Results Analysis) |
| Embodiment/environment | The top scene is office2 from the Replica datasets, and the bottom is fr3/office from TUM RGB-D datasets. | hardware/simulator version and reset protocol | p. 6 (5.1. Experiment Setup), p. 6 (5.2. Results Analysis) |
| Dataset/benchmark | The top scene is room1 from the Replica dataset, and the bottom is V201 from the EuRoC MAV dataset. | role, split, size and leakage | p. 6 (5.1. Experiment Setup), p. 6 (5.2. Results Analysis), p. 7 (5.2. Results Analysis), p. 8 (5.3. Ablation Studies) |
| Metric | The best results are marked as best score , second best score and third best score . '-' denotes that the system does not provide valid results. based on 3D-GS, achieves the ... | definition, denominator, direction and uncertainty | p. 7 (5.2. Results Analysis), p. 2 (3. Extensive evaluations on various public datasets demon), p. 6 (5.2. Results Analysis) |
| Baseline/ablation | Quantitative evaluation of our method compared to SOTA methods for RGB-D camera on Replica and TUM RGB-D datasets. | fair input/data/compute/action matching | p. 6 (5.1. Experiment Setup), p. 6 (5.2. Results Analysis), p. 7 (5.2. Results Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5.4. Limitations - extractive body cue:** One limitation of our method is that a poorly structured point cloud leads to a decline in photorealistic mapping quality.
- **p. 6 / 5.1. Experiment Setup - extractive body cue:** GS-SLAM∗denotes the result of GS-SLAM is taken from [42], all others are obtained in our experiments. '-' denotes the system does not provide valid results.
- **p. 7 / 5.2. Results Analysis - extractive body cue:** The best results are marked as best score , second best score and third best score . '-' denotes that the system does not provide ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, AE has a notable limitation: its training involves each ground-truth image from the test set.를 문제로 두고, Second, we propose Appearancefrom-Motion embedding (AfME), which takes poses as input and eliminates the need for training on the left half of each ground-truth image in the test set.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (Abstract), p. 2 (1. Introduction), p. 4 (4.2. Appearance-from-Motion Embedding) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
