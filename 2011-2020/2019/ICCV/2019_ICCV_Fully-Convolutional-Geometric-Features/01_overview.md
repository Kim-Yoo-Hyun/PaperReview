# Fully Convolutional Geometric Features

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content_ICCV_2019/html/Choy_Fully_Convolutional_Geometric_Features_ICCV_2019_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content_ICCV_2019/papers/Choy_Fully_Convolutional_Geometric_Features_ICCV_2019_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / ICCV
- Authors: Christopher Choy, Jaesik Park, Vladlen Koltun
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, registration, 3D geometry, representation
- Official paper: https://openaccess.thecvf.com/content_ICCV_2019/html/Choy_Fully_Convolutional_Geometric_Features_ICCV_2019_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content_ICCV_2019/papers/Choy_Fully_Convolutional_Geometric_Features_ICCV_2019_paper.pdf
- Code/Project: https://github.com/chrischoy/FCGF
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

FCGF는 점군 전체에 3D 완전 합성곱을 적용해 정합에 사용할 조밀한 기하 특징을 계산한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Extracting geometric features from 3D scans or point clouds is the first step in applications such as registration, reconstruction, and tracking.
- **p. 1 / Abstract - extractive body cue:** State-of-the-art methods require computing low-level features as input or extracting patch-based features with limited receptive field.
- **p. 1 / Abstract - extractive body cue:** In this work, we present fully-convolutional geometric features, computed in a single pass by a 3D fully-convolutional network.
- **p. 1 / Abstract - extractive body cue:** We also present new metric learning losses that dramatically improve performance.
- **p. 1 / Abstract - extractive body cue:** Fully-convolutional geometric features are compact, capture broad spatial context, and scale to large scenes.
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, current pipelines limit spatial context by focusing on patches with restricted spatial extent.
- **p. 1 / 1. Introduction - extractive body cue:** The gray region shows the Pareto frontier of the prior methods. patches for feature learning is akin to extracting small 2D patches around each pixel ...

## Core Idea

- **p. 3 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive body cue:** In this section, we propose metric learning losses for fully-convolutional feature learning.
- **p. 1 / 1. Introduction - extractive body cue:** Our approach is the most accurate and the fastest.
- **p. 2 / 1. Introduction - extractive body cue:** Our approach does not require low-level preprocessing or 3D patches as input, and can rapidly generate high-resolution features with state-ofthe-art discriminative power.
- **p. 2 / 1. Introduction - extractive body cue:** Our approach achieves state-of-the-art performance on the 3DMatch benchmark [36], while being nine times faster than the fastest learning-based method and 290 times faster than ...
- **p. 8 / 6.7. Runtime - extractive body cue:** On average, our approach takes about 0.36 seconds to extract features for a single fragment on 3DMatch with 2.5cm voxel size.
- **p. 7 / 6.4. Hardest-contrastive and Hardest-triplet Losses - extractive body cue:** We used L2 normalization to project features to the surface of a hypersphere and pass the gradient from the loss through the normalization layer to ...
- **p. 7 / 6.4. Hardest-contrastive and Hardest-triplet Losses - extractive body cue:** For the contrastive loss, we use both normalized (denoted norm.) and unnormalized features.
- **p. 3 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive body cue:** Then, we use the pairwise loss for the mined quadruplet (fi, fj, f - i , f - j ) and form the fully8960

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our approach does not require low-level preprocessing or 3D patches as input, and can rapidly generate high-resolution features with state-ofthe-art discriminative power. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 4 (5. Implementation) |
| State/latent | does, require, low-level, preprocessing, patches, input, rapidly, generate, high-resolution, features, state-ofthe-art, discriminative | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 4 (5. Implementation), p. 8 (6.7. Runtime) |
| Output/action | As the input to the network requires unique coordinates C and corresponding features F, we first downsample the input point cloud using a fast GPU-based voxel downsampling function. | point map, pose, scene graph, affordance 또는 query result | p. 4 (5. Implementation), p. 8 (6.7. Runtime), p. 1 (1. Introduction) |
| Objective/outcome | We used L2 normalization to project features to the surface of a hypersphere and pass the gradient from the loss through the normalization layer to train the network with normalization. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses) |

## Main Claims and Actual Contribution

- 개별 패치마다 네트워크를 따로 실행하는 계산을 줄인다.
- 특징 대응을 이용하는 3D 정합에서 성능을 비교한다.

[저자 원문](https://openaccess.thecvf.com/content_ICCV_2019/html/Choy_Fully_Convolutional_Geometric_Features_ICCV_2019_paper.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 4 (6. Experiments), p. 8 (Figure/Table caption) |
| Embodiment/environment | This training set contains 11 sequences, which we split into train/val/test sets as follows: sequence 0 to 5 for training, sequence 7 to 8 for 8961 | hardware/simulator version and reset protocol | p. 4 (6.1. Datasets and Training), p. 4 (6.1. Datasets and Training) |
| Dataset/benchmark | For the outdoor dataset, we use the Relative Translation Error and the Relative Rotation Error. | role, split, size and leakage | p. 4 (6.1. Datasets and Training), p. 4 (6.1. Datasets and Training), p. 5 (6.2. Evaluation Metrics), p. 5 (6.2. Evaluation Metrics) |
| Metric | Table 6: Results on the KITTI dataset. Relative Trans- lation Error (RTE) and Relative Rotation Error (RRE) af- ter RANSAC on FCGF trained with the hardest-contrastive loss with various downsampling voxel sizes. ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 4 (6. Experiments), p. 5 (6.2. Evaluation Metrics) |
| Baseline/ablation | We show that FCGF outperform all state-of-the-art methods in both accuracy and speed, and analyze the proposed hardestcontrastive and hardest-triplet losses. | fair input/data/compute/action matching | p. 4 (6. Experiments), p. 5 (6.3. 3D Match Benchmark), p. 5 (6.3. 3D Match Benchmark) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 7. Conclusion - extractive body cue:** An interesting avenue for future work is to extend the FCGF methodology to end-to-end registration.
- **p. 4 / 5. Implementation - extractive body cue:** Next, we find the hardest negatives for all positive pairs and filter out the hardest negatives that fall within the vicinity of positive pairs by ...
- **p. 4 / 5. Implementation - extractive body cue:** First, we create a matrix P that contains the indices of positive pairs (i, j) as well as an additional matrix Pdt that contains all ...
- **p. 5 / 6.1. Datasets and Training - extractive body cue:** If ICP fails or the number of overlapping voxels is less than 1k, we removed the pair from the dataset.
- **p. 5 / 6.2. Evaluation Metrics - extractive body cue:** However, it does not measure the quality of feature when used within a reconstruction system.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses)이다.
