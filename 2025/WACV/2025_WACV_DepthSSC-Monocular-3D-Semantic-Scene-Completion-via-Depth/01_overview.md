# DepthSSC: Monocular 3D Semantic Scene Completion via Depth-Spatial Alignment and Voxel Adaptation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Yao_DepthSSC_Monocular_3D_Semantic_Scene_Completion_via_Depth-Spatial_Alignment_and_WACV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Yao_DepthSSC_Monocular_3D_Semantic_Scene_Completion_via_Depth-Spatial_Alignment_and_WACV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / WACV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic, alignment, depth, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/WACV2025/html/Yao_DepthSSC_Monocular_3D_Semantic_Scene_Completion_via_Depth-Spatial_Alignment_and_WACV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/WACV2025/papers/Yao_DepthSSC_Monocular_3D_Semantic_Scene_Completion_via_Depth-Spatial_Alignment_and_WACV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The limitations of these cameras, such as the lack of stereoscopic depth perception and restricted field of view, often lead to spatial distortions and deformations.를 문제로 두고, test set), surpassing the latest approaches. • We introduce the Spatially-Transformed Graph Fusion module, which facilitates the spatial transformation and feature fusion from voxels to graph structures, ensuring precise alignment of sp ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The task of 3D semantic scene completion using monocular cameras is gaining significant attention in the field of autonomous driving.
- **p. 1 / Abstract - extractive body cue:** This task aims to predict the occupancy status and semantic labels of each voxel in a 3D scene from partial image inputs.
- **p. 1 / Abstract - extractive body cue:** Despite numerous existing methods, many face challenges such as inaccurately predicting object shapes and misclassifying object boundaries.
- **p. 1 / Abstract - extractive body cue:** To address these issues, we propose DepthSSC, an advanced method for semantic scene completion using only monocular cameras.
- **p. 1 / Abstract - extractive body cue:** DepthSSC integrates the Spatial Transformation Graph Fusion (ST-GF) module with Geometric-Aware Voxelization (GAV), enabling dynamic adjustment of voxel resolution to accommodate the geometric complexity of ...
- **p. 1 / 1. Introduction - extractive body cue:** The limitations of these cameras, such as the lack of stereoscopic depth perception and restricted field of view, often lead to spatial distortions and deformations.
- **p. 2 / 1. Introduction - extractive body cue:** In light of these challenges, our work introduces DepthSSC, a novel method designed to address the limitations of monocular SSC.

## Core Idea

- **p. 2 / 44.89 IoU on the SemanticKITTI benchmark (hidden - extractive body cue:** test set), surpassing the latest approaches. • We introduce the Spatially-Transformed Graph Fusion module, which facilitates the spatial transformation and feature fusion from voxels to ...
- **p. 2 / 1. Introduction - extractive body cue:** Our key contributions are: • We propose DepthSSC, a new method that integrates spatial transformation with geometric awareness to address the issues of inaccurate depth ...
- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive body cue:** To address these spatial alignment issues, we propose the Spatially-Transformed Graph Fusion (ST-GF) module, as shown in Figure 3.
- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive body cue:** ASAN is a neural network that predicts this affine transformation matrix Θijk, which consists of rotation, scaling, and translation components.
- **p. 1 / 1. Introduction - extractive body cue:** S3cnet [4] and Scpnet [27], which leverage LiDAR-generated point clouds, are examples among various approaches that have been developed for 3D semantic scene completion.
- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive body cue:** The ST-GF module is designed with three primary objectives: (1) correcting geometric distortions by predicting a 3D affine transformation matrix Θijk, which allows flexible adjustments ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** The Deformable Self-Attention (DSA) mechanism refines voxel features by enabling interactions within the 3D space: DSA(F3D, F3D) = DA(f, p, F3D), (2) where f is ...
- **p. 3 / 3. Method - extractive body cue:** In this part, we first introduce the baseline model VoxFormer [15] in Section 3.1.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The final output Yt ∈RH×W ×Z×(M+1) represents the semantic segmentation map, where H×W ×Z is the output resolution and M +1 indicates M semantic classes plus one void class. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary) |
| State/latent | final, output, represents, semantic, segmentation, where, resolution, indicates, classes, plus, void, class | geometry, map, object/relationship state | p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 1 (1. Introduction) |
| Output/action | From an input RGB image It, 2D features F2Dt ∈ Rb×c×d are extracted using a convolutional neural network backbone, where b × c is the spatial resolution and d is the feature ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Preliminary), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | We substitute equation 5, equation 4, and Tijk into equation 3, and obtain: Θijk = " cθcϕsx (cθsϕsψ-sθcψ)sy (cθsϕcψ+sθsψ)sz tx sθcϕsx (sθsϕsψ+cθcψ)sy (sθsϕcψ-cθsψ)sz ty -sϕsx cϕsψsy cϕcψsz tz 0 0 0 1 ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 3 (3.1. Preliminary) |

## Main Claims and Actual Contribution

- **p. 2 / 44.89 IoU on the SemanticKITTI benchmark (hidden - extractive body cue:** test set), surpassing the latest approaches. • We introduce the Spatially-Transformed Graph Fusion module, which facilitates the spatial transformation and feature fusion from voxels to ...
- **p. 2 / 1. Introduction - extractive body cue:** Our key contributions are: • We propose DepthSSC, a new method that integrates spatial transformation with geometric awareness to address the issues of inaccurate depth ...
- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive body cue:** To address these spatial alignment issues, we propose the Spatially-Transformed Graph Fusion (ST-GF) module, as shown in Figure 3.
- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive body cue:** ASAN is a neural network that predicts this affine transformation matrix Θijk, which consists of rotation, scaling, and translation components.
- **p. 1 / 1. Introduction - extractive body cue:** S3cnet [4] and Scpnet [27], which leverage LiDAR-generated point clouds, are examples among various approaches that have been developed for 3D semantic scene completion.
- **p. 8 / 4.4. Robustness experiment - extractive body cue:** The addition of the dynamic resolution in GAV also contributes significantly to the final performance. ing intensities into the depth input, defined as N(0, σ2), ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Pipeline of the DepthSSC. The process begins with a backbone extracting 2D features from input images, followed by the projection of these 2D ...
- **p. 8 / 4.4. Robustness experiment - extractive body cue:** The best performance is highlighted in bold.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4.4. Robustness experiment), p. 3 (Figure/Table caption) |
| Embodiment/environment | test set), surpassing the latest approaches. • We introduce the Spatially-Transformed Graph Fusion module, which facilitates the spatial transformation and feature fusion from voxels to graph structures, ensuring precise alignment of sp ... | hardware/simulator version and reset protocol | p. 2 (44.89 IoU on the SemanticKITTI benchmark (hidden), p. 8 (4.4. Robustness experiment) |
| Dataset/benchmark | Methods VoxFormer-S MonoScene DepthSSC Range (m) 12.8m 25.6m 51.2m 12.8m 25.6m 51.2m 12.8m 25.6m 51.2m IoU (%) 55.45 46.36 38.76 54.65 44.70 37.87 59.37 49.47 40.85 Precision (%) 66.10 61.34 58.52 65.88 ... | role, split, size and leakage | p. 2 (44.89 IoU on the SemanticKITTI benchmark (hidden), p. 8 (4.4. Robustness experiment), p. 8 (4.4. Robustness experiment) |
| Metric | Methods VoxFormer-S MonoScene DepthSSC Range (m) 12.8m 25.6m 51.2m 12.8m 25.6m 51.2m 12.8m 25.6m 51.2m IoU (%) 55.45 46.36 38.76 54.65 44.70 37.87 59.37 49.47 40.85 Precision (%) 66.10 61.34 58.52 65.88 ... | definition, denominator, direction and uncertainty | p. 8 (4.4. Robustness experiment), p. 7 (4.4. Robustness experiment), p. 8 (4.4. Robustness experiment) |
| Baseline/ablation | Quantitative comparison against RGB-inferred baselines and the state-of-the-art monocular SSC method on SemanticKITTI [1] (hidden test set).The best results compared to the corresponding baselines are marked in blue. | fair input/data/compute/action matching | p. 8 (4.4. Robustness experiment), p. 8 (4.4. Robustness experiment), p. 8 (4.4. Robustness experiment) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** By integrating the Spatially-Transformed Graph Fusion (ST-GF) module and Geometrically-aware Voxelization, DepthSSC dynamically adjusts voxel resolutions based on the geometric complexity of 3D space, addressing ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Robustness evaluation under noisy depth inputs. This table shows the performance degradation in mIoU under increas- ing depth noise levels. Our ST-GF module ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Goal of Our Approach. Demonstrates DepthSSC's su- periority in handling complex 3D environments for semantic scene completion. Contrasted with VoxFormer, DepthSSC excels in ...
- **p. 7 / 4.4. Robustness experiment - extractive body cue:** To evaluate the robustness of the ST-GF module under depth input errors, we simulate errors in depth measurements by artificially introducing Gaussian noise with vary2160

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The limitations of these cameras, such as the lack of stereoscopic depth perception and restricted field of view, often lead to spatial distortions and deformations.를 문제로 두고, test set), surpassing the latest approaches. • We introduce the Spatially-Transformed Graph Fusion module, which facilitates the spatial transformation and feature fusion from voxels to graph structures, ensuring precise alignment of sp ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 4 (3.2. Spatially-Transformed Graph Fusion), p. 3 (3.1. Preliminary) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
