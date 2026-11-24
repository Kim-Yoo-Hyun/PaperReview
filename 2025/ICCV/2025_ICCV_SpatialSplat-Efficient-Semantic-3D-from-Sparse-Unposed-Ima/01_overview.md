# SpatialSplat: Efficient Semantic 3D from Sparse Unposed Images

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Yu Sheng, Jiajun Deng, Xinran Zhang, Yu Zhang, Bei Hua, Yanyong Zhang, Jianmin Ji
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Gaussian Splatting, geometry, semantic, alignment, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

SpatialSplat은 자세를 모르는 희소 영상에서 불필요하게 겹치는 Gaussian을 줄이면서 세밀한 의미 특징을 가진 3차원 장면을 예측한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A major breakthrough in 3D reconstruction is the feedforward paradigm to generate pixel-wise 3D points or Gaussian primitives from sparse, unposed images.
- **p. 1 / Abstract - extractive body cue:** To further incorporate semantics while avoiding the significant memory and storage costs of high-dimensional semantic features, existing methods extend this paradigm by associating each primitive ...
- **p. 1 / Abstract - extractive body cue:** However, these methods have two major limitations: (a) the naively compressed feature compromises expressiveness, affecting the model's ability to capture finegrained semantics, and (b) the ...
- **p. 1 / Abstract - extractive body cue:** To this end, we introduce SpatialSplat, a feedforward framework that produces redundancy-aware Gaussians and capitalizes on a dual-field semantic representation.
- **p. 1 / Abstract - extractive body cue:** Particularly, with the insight that primitives within the same instance exhibit high semantic consistency, we decompose the semantic representation into a coarse feature field that ...
- **p. 2 / 1. Introduction - extractive body cue:** Despite significant progress, these methods have two major limitations.
- **p. 2 / 1. Introduction - extractive body cue:** However, these methods typically rely on perscene optimization and complex multi-step preprocessing, limiting their ability to generalize across multiple scenes within a single model.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Additionally, we introduce a Selective Gaussian Mechanism (SGM) to eliminate redundancy in overlapping areas caused by pixelwise representations, along with a novel loss function that ...
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are threefold: • A novel feed-forward 3DGS framework that, to the best of our knowledge, is the first to simultaneously learn semantic and ...
- **p. 3 / 3. Method - extractive body cue:** In the following sections, we provide a detailed explanation of each component of our method.
- **p. 4 / 3.2. Selective Gaussian Mechanism - extractive body cue:** To address this, we propose a selective Gaussian mechanism that assigns each primitive an importance score to quantify its necessity for the scene representation.
- **p. 4 / 3.3. Dual-field Architecture - extractive body cue:** To mitigate this loss without increasing storage costs, we propose a dual-field architecture that decouples semantic representation into: 1) a fine-grained instance-aware radiance field, capturing ...
- **p. 3 / 3.1. 3D Geometry Prediction - extractive body cue:** The features from encoder are then passed to a ViT-based decoder, where cross-attention is applied to better capture spatial relationships and aggregate information across views.
- **p. 5 / 3.3. Dual-field Architecture - extractive body cue:** We minimize the loss between the rendered feature map at a novel view and the feature map ˆF S of the ground truth image extracted ...
- **p. 3 / 3.1. 3D Geometry Prediction - extractive body cue:** Both the encoder and decoder in our geometric prediction module are built on pure ViT structures, requiring no geometric priors as in previous methods [3, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The input image is patchified and flattened into image sequences, which along with the camera intrinsics processed by a linear layer, are fed into the encoder. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. 3D Geometry Prediction), p. 4 (3.1. 3D Geometry Prediction) |
| State/latent | input, image, patchified, flattened, sequences, along, camera, intrinsics, processed, linear, layer, encoder | geometry, map, object/relationship state | p. 3 (3.1. 3D Geometry Prediction), p. 4 (3.1. 3D Geometry Prediction), p. 3 (3.1. 3D Geometry Prediction) |
| Output/action | Experiments show that SpatialSplat effectively learns 3D priors from sparse unposed images without depth supervision, even while jointly learning multiple parameters and features. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.1. 3D Geometry Prediction), p. 3 (3.1. 3D Geometry Prediction), p. 4 (3.3. Dual-field Architecture) |
| Objective/outcome | Therefore, we optimize βi through photometric loss minimization. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.2. Selective Gaussian Mechanism), p. 4 (3.3. Dual-field Architecture), p. 5 (3.3. Dual-field Architecture) |

## Main Claims and Actual Contribution

- 거친 고차원 의미장과 세밀한 저차원 특징장을 분리하고 선택 모듈로 겹치는 프리미티브를 제거한다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.pdf#page=4)
- ScanNet과 새 도메인인 Replica에서 의미 성능을 평가하고 장면을 저장하는 파라미터 수를 함께 비교했다. [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.pdf#page=6) · [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.1. Experimental Setup), p. 6 (4.2. Results and Analysis) |
| Embodiment/environment | We filter out bad scenes and those with incomplete extrinsic parameters, resulting in a training dataset of approximately 1,500 scenes. | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Setup), p. 8 (25.58 MB) |
| Dataset/benchmark | For evaluation, we follow LSM and select 40 unseen scenes from ScanNet to assess our model's performance. | role, split, size and leakage | p. 5 (4.1. Experimental Setup), p. 8 (25.58 MB), p. 5 (4.1. Experimental Setup), p. 8 (25.58 MB) |
| Metric | For OVS, we evaluate performance using class-wise intersection over union (mIoU) and average pixel accuracy (mAcc). | definition, denominator, direction and uncertainty | p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 8 (4.2. Results and Analysis) |
| Baseline/ablation | 1, SpatialSplat outperforms all compared methods, even surpassing L-Seg, which provides semantic feature supervision GT LSM LSM Ours Ours Figure 6. | fair input/data/compute/action matching | p. 7 (4.2. Results and Analysis), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Results and Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** In challenging cases where LSM fails, such as the table legs in the first two rows and the corners in the last two rows, our ...
- **p. 8 / 4.3. Ablations and Analysis - extractive body cue:** The primary issue is that per-primitive semantic learning struggles to maintain accurate semantics and fails to preserve clear instance boundaries, as illustrated in Fig.
- **p. 8 / 25.58 MB - extractive body cue:** Furthermore, as our method does not rely on dense semantic supervision, we leverage a lightweight pretrained 2D model, significantly accelerating inference speed.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Out-of-distribution (OOD) comparison on Replica dataset.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 4 (3.3. Dual-field Architecture), p. 3 (3.1. 3D Geometry Prediction), p. 5 (3.3. Dual-field Architecture), p. 4 (3.2. Selective Gaussian Mechanism)이다.
