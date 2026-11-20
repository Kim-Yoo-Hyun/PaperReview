# Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Lv_Gau-Occ_Geometry-Completed_Gaussians_for_Multi-Modal_3D_Occupancy_Prediction_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Lv_Gau-Occ_Geometry-Completed_Gaussians_for_Multi-Modal_3D_Occupancy_Prediction_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Chengxin Lv, Yihui Li, Hongyu Yang, YunHong Wang
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Lv_Gau-Occ_Geometry-Completed_Gaussians_for_Multi-Modal_3D_Occupancy_Prediction_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Lv_Gau-Occ_Geometry-Completed_Gaussians_for_Multi-Modal_3D_Occupancy_Prediction_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Gau-Occ는 희소 라이다와 다중 시점 영상에서 3D 공간의 점유 상태와 의미 범주를 예측한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D semantic occupancy prediction is crucial for autonomous driving.
- **p. 1 / Abstract - extractive body cue:** While multi-modal fusion improves accuracy over vision-only methods, it typically relies on computationally expensive dense voxel or BEV tensors.
- **p. 1 / Abstract - extractive body cue:** We present Gau-Occ, a multi-modal framework that bypasses dense volumetric processing by modeling the scene as a compact collection of semantic 3D Gaussians.
- **p. 1 / Abstract - extractive body cue:** To ensure geometric completeness, we propose a LiDAR Completion Diffuser (LCD) that recovers missing structures from sparse LiDAR to initialize robust Gaussian anchors.
- **p. 1 / Abstract - extractive body cue:** Furthermore, we introduce Gaussian Anchor Fusion (GAF), which efficiently integrates multi-view image semantics via geometry-aligned 2D sampling and cross-modal alignment.
- **p. 1 / 1. Introduction - extractive body cue:** This limitation often leads to incomplete occupancy estimates and coarse free-space predictions in complex driving scenes.
- **p. 1 / 1. Introduction - extractive body cue:** To address these limitations, recent works integrate active depth sensors such as LiDAR or radar with multi-view RGB [19, 34, 42], exploiting complementary geometric and ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • We propose Gau-Occ, a compact Gaussian-based framework that unifies LiDAR and multi-view images for 3D semantic occupancy prediction. • ...
- **p. 1 / 1. Introduction - extractive body cue:** We propose Gau-Occ, a framework that leverages learnable semantic Gaussian anchors for efficient scene representation.
- **p. 2 / 1. Introduction - extractive body cue:** Second, we propose the Gaussian Anchor Fusion (GAF) module, which aligns multi-view image semantics with a LiDAR-anchored 3D structural prior.
- **p. 3 / 3.2. LiDAR Completion Diffuser (LCD) - extractive body cue:** We propose the LiDAR Completion Diffuser (LCD), a local diffusion model that reconstructs dense, geometrically consistent point clouds from sparse scans.
- **p. 4 / 3.4. Gaussian Anchor Fusion (GAF) - extractive body cue:** To unify precise LiDAR geometry with rich image semantics, we propose Gaussian Anchor Fusion (GAF), a geometry-conditioned multi-modal fusion module that extracts, samples, and aggregates ...
- **p. 3 / 3.1. 3D Semantic Gaussian Scene Representation - extractive body cue:** Each Gaussian then anchors multi-view image features via our Gaussian Anchor Fusion (GAF), producing geometry-aligned multi-modal representations.
- **p. 2 / 3. Proposed Approach - extractive body cue:** We propose Gau-Occ, a compact representation of 3D scenes using semantic Gaussians that jointly encode LiDAR geometry and multi-view semantics.
- **p. 2 / 3. Proposed Approach - extractive body cue:** The completed points are then voxelized into sparse features that initialize density-aware Gaussians.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given a sparse LiDAR point cloud P = {Pi ∈R3}NP i=1 and multi-view images I = {Ij ∈R3×H×W }NI j=1, the task is to predict a voxelized semantic occupancy grid O ∈R/C/×X×Y ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (3.1. 3D Semantic Gaussian Scene Representation), p. 4 (3.2. LiDAR Completion Diffuser (LCD)) |
| State/latent | Given, sparse, LiDAR, point, cloud, multi-view, images, task, predict, voxelized, semantic, occupancy | geometry, map, object/relationship state | p. 2 (3.1. 3D Semantic Gaussian Scene Representation), p. 4 (3.2. LiDAR Completion Diffuser (LCD)), p. 3 (3.2. LiDAR Completion Diffuser (LCD)) |
| Output/action | The denoising network ˆϵθ learns to predict the injected noise conditioned on the sparse input P: Ldiff = | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.2. LiDAR Completion Diffuser (LCD)), p. 3 (3.2. LiDAR Completion Diffuser (LCD)), p. 2 (1. Introduction) |
| Objective/outcome | Following [14], we optimize the model with a joint objective LCE + LLov, combining cross-entropy and Lov´aszSoftmax losses to enhance segmentation accuracy and class balance. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3.1. 3D Semantic Gaussian Scene Representation), p. 3 (3.2. LiDAR Completion Diffuser (LCD)), p. 2 (3. Proposed Approach) |

## Main Claims and Actual Contribution

- 라이다의 빈 구조를 보완하고 그 결과를 의미 정보가 있는 3D 가우시안으로 표현한다.
- 가우시안 위치를 기준으로 여러 카메라의 특징을 융합해 공간 점유를 추정한다.

[원문 초록](https://openaccess.thecvf.com/content/CVPR2026/html/Lv_Gau-Occ_Geometry-Completed_Gaussians_for_Multi-Modal_3D_Occupancy_Prediction_CVPR_2026_paper.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (4.2. Quantitative Results), p. 5 (4.2. Quantitative Results) |
| Embodiment/environment | We evaluate Gau-Occ on three widely adopted benchmarks: SurroundOcc-nuScenes [2, 46], Occ3DnuScenes [40], and KITTI-360 [28]. | hardware/simulator version and reset protocol | p. 5 (4.1. Datasets and Metrics), p. 6 (4.2. Quantitative Results) |
| Dataset/benchmark | Qualitative results on the Occ3D-nuScenes validation set. | role, split, size and leakage | p. 5 (4.1. Datasets and Metrics), p. 6 (4.2. Quantitative Results), p. 7 (4.3. Qualitative Comparison), p. 8 (4.4. Ablation Study) |
| Metric | 7, replacing the completed point cloud P′ with the raw input P leads to notable performance drops in both IoU and mIoU. | definition, denominator, direction and uncertainty | p. 7 (4.4. Ablation Study), p. 5 (4.1. Datasets and Metrics), p. 5 (4.2. Quantitative Results) |
| Baseline/ablation | As shown, Gau-Occ outperforms the strongest LiDAR-only baseline, L2COcc [43], by +1.3 IoU and +0.6 mIoU. | fair input/data/compute/action matching | p. 6 (4.2. Quantitative Results), p. 6 (4.3. Qualitative Comparison), p. 5 (4.2. Quantitative Results) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 4.2. Quantitative Results - extractive body cue:** Gau-Occ also achieves clear gains on safety-critical classes such as bus, car, bicycle, and motorcycle, benefiting from precise Geo-VLAD resampling and geometry-aware FiLM modulation that ...
- **p. 6 / 4.3. Qualitative Comparison - extractive body cue:** On KITTI-360, under challenging singlecamera + LiDAR setting, Gau-Occ maps both large layouts and small instances accurately, demonstrating robustness to sparse viewpoints and effective use ...
- **p. 7 / 4.3. Qualitative Comparison - extractive body cue:** These observations support Gau-Occ's geometry-complete representation and its robust multi-modal aggregation pipeline.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** The full GAF configuration (Row 4) achieves optimal results, validating the necessity of both geometry-guided sampling and refinement in building a robust multi-modal representation.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Replacing GGS with geometry-agnostic sampling (Row 2) degrades long-range feature association, underscoring the importance of LiDARconditioned offsets in maintaining spatial and semantic conFigure 8.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.4. Gaussian Anchor Fusion (GAF)), p. 3 (3.1. 3D Semantic Gaussian Scene Representation), p. 2 (3. Proposed Approach)이다.
