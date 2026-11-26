# EAP-GS: Efficient Augmentation of Pointcloud for 3D Gaussian Splatting in Few-shot Scene Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: Dongrui Dai, Yuxiang Xing
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, point cloud, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

EAP-GS는 소수 영상으로 장면을 복원할 때 3D Gaussian Splatting의 초기 점 분포를 보완한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian splatting (3DGS) has shown impressive performance in 3D scene reconstruction.
- **p. 1 / Abstract - extractive body cue:** However, it suffers from severe degradation when the number of training views is limited, resulting in blur and floaters.
- **p. 1 / Abstract - extractive body cue:** Many works have been devoted to standardize the optimization process of 3DGS through regularization techniques.
- **p. 1 / Abstract - extractive body cue:** However, we identify that inadequate initialization is a critical issue overlooked by current studies.
- **p. 1 / Abstract - extractive body cue:** To address this, we propose EAP-GS, a method to enhance initialization for fast, accurate, and stable few-shot scene reconstruction.
- **p. 2 / 1. Introduction - extractive body cue:** In practice, a sufficient number of images are often difficult to obtain due to various limitations.
- **p. 2 / 1. Introduction - extractive body cue:** With a lack of coherence between Gaussians , their attributes can only be optimized individually via image supervision.

## Core Idea

- **p. 5 / 3.2. Attentional Pointcloud Augmentation - extractive body cue:** Therefore, we propose a pointcloud generation method specifically designed for 3DGS initialization, which significantly increases the number of initial points.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • A key insight that inadequate initialization can lead to poor performance in few-shot optimization, which is ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this, we propose an easy-to-implement attentional pointcloud augmentation technique to improve the accuracy of 3DGS reconstruction.
- **p. 4 / 3.2. Attentional Pointcloud Augmentation - extractive body cue:** The input to reconstruction stage consists of the n scene views I = {Ii ∈RH×W/i = 1, ..., n} and 16501
- **p. 4 / 3. Method - extractive body cue:** 3.2, we present an Attentional Pointcloud Augmentation technique to effectively increase the number of initial points and harmonize the overall pointcloud density distribution of the ...
- **p. 5 / 3.2. Attentional Pointcloud Augmentation - extractive body cue:** In this work, we implement our algorithm based on DetectorfreeSfM [11], which leverages a detector-free matcher to enhance feature extraction in texture-poor scenarios.
- **p. 4 / 3.1. Preliminary - extractive body cue:** The optimization process involves splatting 3D Gaussian into the image domain, sorting the N 2D Gaussians on the pixel by depth, and then calculating the ...
- **p. 5 / 3.2. Attentional Pointcloud Augmentation - extractive body cue:** Specifically, based on the pointcloud density distribution in the view Ii, we delineate an attention region Mi: \ ma t hbf {M} _i = \mathbf ...

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | 드문 여러 영상과 초기화에 쓰는 SfM 점 및 카메라 자세 |
| 표현 | 영상 상대 깊이와 평탄 정도로 보완한 초기 점 분포 |
| 출력 | 학습한 3D 가우시안 장면과 새 시점 렌더링 |
| 평가 | LLFF 등의 뷰 합성 품질 |

[방법 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.pdf#page=4) · [평가 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.pdf#page=7)

## Main Claims and Actual Contribution

- 기하 구조가 있으나 관측점이 드문 영역에 점을 보강한다.
- 실내외 장면에서 점 보강이 복원에 미치는 영향을 비교한다.

[원문 초록](https://openaccess.thecvf.com/content/CVPR2025/html/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.3. Ablation Studies), p. 2 (Figure/Table caption) |
| Embodiment/environment | We evaluated our method on all scenes of the LLFF [21] and Mip-NeRF360 dataset [1]. | hardware/simulator version and reset protocol | p. 6 (4.1. Dataset and Implementation Details), p. 6 (4.2. Experimental Results) |
| Dataset/benchmark | Quantitative results on LLFF and Mip-NeRF360 datasets. | role, split, size and leakage | p. 6 (4.1. Dataset and Implementation Details), p. 6 (4.2. Experimental Results), p. 7 (4.2. Experimental Results), p. 7 (4.2. Experimental Results) |
| Metric | Best score and second-best score are in red and orange respectively. | definition, denominator, direction and uncertainty | p. 7 (4.2. Experimental Results), p. 7 (4.2. Experimental Results), p. 8 (4.3. Ablation Studies) |
| Baseline/ablation | We configured COLMAP [28] with the same parameters as FSGS for the initialization of various baselines. | fair input/data/compute/action matching | p. 6 (4.1. Dataset and Implementation Details), p. 6 (4.1. Dataset and Implementation Details), p. 7 (4.3. Ablation Studies) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Discussion - extractive body cue:** Lacking a method to limit the error may be a limitation Figure 7.
- **p. 8 / 5. Discussion - extractive body cue:** This issue is primarily due to data incompleteness, and a potential approach to further enhance performance would be to incorporate prior knowledge or generative models ...
- **p. 7 / 4.2. Experimental Results - extractive body cue:** Similar results are obtained for unknown camera-poses though we did not report here because of space limitation.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 5 (3.2. Attentional Pointcloud Augmentation), p. 4 (3.1. Preliminary)이다.

## 검색 태그 근거

소수 영상의 SfM 점군을, 단안 상대 깊이와 공간 주파수에 따라 보완한다. 초기화에 쓰는 점과 깊이를 모두 영상에서 얻고 LLFF 등의 뷰 합성을 평가했다. [원문 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.pdf#page=4) · [원문 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.pdf#page=7)
