# Uni3R: Unified 3D Reconstruction and Semantic Understanding via Generalizable Gaussian Splatting from Unposed Multi-View Images

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Xiangyu Sun, Haoyi Jiang, Liu Liu, Seungtae Nam, Gyeongjin Kang, Xinjie Wang, Wei Sui, Zhizhong Su, Wenyu Liu, Xinggang Wang, Eunbyung Park
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, geometry, semantic, alignment, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf)

## Why This Paper Is Here

Uni3R은 카메라 자세가 주어지지 않은 여러 영상을 받아 장면의 가우시안 기하·외관과 열린 어휘 의미 특징을 함께 예측한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Reconstructing and semantically interpreting 3D scenes from sparse 2D views remains a fundamental challenge in computer vision.
- **p. 1 / Abstract - extractive body cue:** Conventional methods often decouple semantic understanding from reconstruction or necessitate costly per-scene optimization, thereby restricting their scalability and generalizability.
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce Uni3R, a novel feed-forward framework that jointly reconstructs a unified 3D scene representation enriched with open-vocabulary semantics, directly from unposed ...
- **p. 1 / Abstract - extractive body cue:** Our approach leverages a Cross-View Transformer to robustly integrate information across arbitrary
- **p. 1 / Abstract - extractive body cue:** Intern at D-Robotics ‡Project leader §Corresponding author multi-view inputs, which then regresses a set of 3D Gaussian primitives endowed with semantic feature fields.
- **p. 2 / 1. Introduction - extractive body cue:** Recent efforts, including LangSplat [28] and Feature-3DGS [45], have incorporated semantic fields into 3D Gaussian Splatting, yet remain constrained by scene-specific optimization and lack scalability ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these limitations, we propose Uni3R, a novel, generalizable framework that synthesizes a unified 3D representation from arbitrary multi-view images for both highfidelity rendering ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We introduce Uni3R, a novel feed-forward architecture that unifies 3D reconstruction and semantic understanding.
- **p. 2 / 1. Introduction - extractive body cue:** To address these limitations, we propose Uni3R, a novel, generalizable framework that synthesizes a unified 3D representation from arbitrary multi-view images for both highfidelity rendering ...
- **p. 3 / 3. Method - extractive body cue:** This section details our methodology, beginning with the Feed-Forward 3D Gaussian Model in Sec.
- **p. 4 / 3.1.2. Cross-View Transformer Encoder - extractive body cue:** The Cross-View Transformer Encoder consists of a series of Transformer blocks that alternate between intra-frame and cross-frame attention.
- **p. 5 / 3.3. Training Objectives - extractive body cue:** Given that the predictions from VGGT are not uniformly reliable, especially in challenging regions such as reflective surfaces or areas with heavy occlusion, we introduce ...
- **p. 4 / 3.1.2. Cross-View Transformer Encoder - extractive body cue:** Uni3R employs a Cross-View Transformer Encoder, following VGGT, to extract and fuse features from all input images into a consistent, view-agnostic latent representation.
- **p. 5 / 3.3. Training Objectives - extractive body cue:** We then enforce alignment between the rendered semantic feature map ˆF (i)′ and the 2D CLIP-based features using a cosine similarity loss: \m a t ...
- **p. 6 / 3.3. Training Objectives - extractive body cue:** The final training objective is a weighted sum of the individual losses: \mat h cal { L}_{\tex t {total}} = \mathcal {L}_{\text {rgb}} + \lambda ...

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | 외부 자세를 주지 않은 다중 RGB와 카메라 내부 파라미터 |
| 표현 | 다중 뷰 토큰, 점 기하와 의미 특징 |
| 출력 | 3D 가우시안 및 렌더링한 기하·색·의미 |
| 평가 | 뷰 합성, 깊이와 의미 분할 정확도 |

[방법 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf#page=3) · [평가 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf#page=7)

## Main Claims and Actual Contribution

- 시점 간 특징을 결합하는 모델에서 가우시안 장면과 의미 특징을 함께 복원해 새 시점 렌더링과 언어 기반 인식을 지원한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf#page=5)
- 실내 장면과 다양한 뷰 합성 자료에서 영상 재구성과 의미 이해를 평가하고 두 목적을 함께 학습했을 때의 영향을 비교했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.2. Experiment Results), p. 6 (4.2. Experiment Results) |
| Embodiment/environment | We evaluate on 40 unseen ScanNet scenes, and further examine the model's zero-shot generalization on the MipNeRF360 [1] dataset. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | Quantitative comparisons of novel view synthesis on the RE10k [46] and ACID [22] dataset under 2-views setup. | role, split, size and leakage | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (0.724 17.28 13.31 ≈60min), p. 7 (0.724 17.28 13.31 ≈60min) |
| Metric | Table 7. Ablation Study on different modules. We evaluate the ablated variants of Uni3R, by recording their rendering quality, segmentation performance and geometric accuracy. Removing the semantic loss causes a severe collapse ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 6 (4.2. Experiment Results), p. 8 (4.3. Analysis and Ablations) |
| Baseline/ablation | Uni3R consistently outperforms all baselines under both 4-view and 8-view settings. | fair input/data/compute/action matching | p. 7 (0.724 17.28 13.31 ≈60min), p. 7 (0.724 17.28 13.31 ≈60min), p. 6 (4.1. Experimental Setup) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.2. Experiment Results - extractive body cue:** Thus, Uni3R not only mimics LSeg, but also leverages 3D consistency to produce a denoised, robust semantic prediction.
- **p. 8 / 4.3. Analysis and Ablations - extractive body cue:** When the geometric loss is removed, the model exhibits degraded 3D consistency (higher depth error and lower τ), validating its effectiveness in improving point cloud ...
- **p. 8 / 4.3. Analysis and Ablations - extractive body cue:** The scale-invariant constraint contributes to rendering stability across scenes with varying depth ranges, while the intrinsic embedding improves robustness by aligning scenes of varying scales ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 4 (3.1.2. Cross-View Transformer Encoder), p. 5 (3.3. Training Objectives), p. 6 (3.3. Training Objectives)이다.

## 검색 태그 근거

외부 자세를 주지 않은 여러 RGB 영상과 카메라 내부 파라미터로 가우시안 기하와 의미 특징을 예측한다. VGGT의 기하 및 CLIP 계열 의미 특징은 훈련 감독에 쓰고 분할에서 텍스트 질의를 사용한다. [원문 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf#page=3) · [원문 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf#page=7)
