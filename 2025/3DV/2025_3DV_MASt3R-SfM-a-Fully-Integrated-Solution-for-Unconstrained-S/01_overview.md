# MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/3dv66043.2025.00008.
> PDF retrieval source: https://openreview.net/attachment?id=5uw1GRBFoT&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: Bardienus Pieter Duisterhof, Lojze Zust, Philippe Weinzaepfel, Vincent Leroy, Yohann Cabon, Jerome Revaud
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: geometry, 3D Vision, matching, 3D reconstruction, camera pose
- Official paper: https://api.crossref.org/works/10.1109/3dv66043.2025.00008
- Full-text retrieval: https://arxiv.org/pdf/2409.19152.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

MASt3R-SfM은 영상 쌍에서 예측한 국소 3차원 구조와 대응을 전역 좌표계로 정렬해 순서가 없는 사진 모음도 재구성한다. [PDF 1쪽](https://arxiv.org/pdf/2409.19152v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Structure-from-Motion (SfM), a task aiming at jointly recovering camera poses and 3D geometry of a scene given a set of images, remains a hard problem ...
- **p. 1 / Abstract - extractive body cue:** The traditional solution for SfM consists of a complex pipeline of minimal solvers which tends to propagate errors and fails when images do not sufficiently ...
- **p. 1 / Abstract - extractive body cue:** Recent methods have attempted to revisit this paradigm, but we empirically show that they fall short of fixing these core issues.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose instead to build upon a recently released foundation model for 3D vision that can robustly produce local 3D reconstructions and ...
- **p. 1 / Abstract - extractive body cue:** We introduce a low-memory approach to accurately align these local reconstructions in a global coordinate system.
- **p. 1 / 1. Introduction - extractive body cue:** These changes must, however, be put into perspective, as they do not fundamentally challenge the overall structure of the traditional pipeline.
- **p. 1 / 1. Introduction - extractive body cue:** The presence of outliers, such as wrong pixel matches, poses additional challenges and compels existing methods to repeatedly resort to hypothesis formulation and verification at ...

## Core Idea

- **p. 4 / 4. Proposed Method - extractive body cue:** We present a novel large-scale 3D reconstruction approach consisting of four steps outlined in fig.
- **p. 2 / 1. Introduction - extractive body cue:** To achieve linear complexity in the number of images, we show as second contribution how the encoder from MASt3R can be exploited for large-scale image ...
- **p. 2 / 1. Introduction - extractive body cue:** First, we propose MASt3R-SfM, a full-fledged SfM pipeline able to process unconstrained image collections.
- **p. 4 / 4.1. Scene graph - extractive body cue:** While any off-the-shelf image retriever can in theory do, we propose to leverage MASt3R's encoder Enc(·).
- **p. 6 / 4.4. Refinement - extractive body cue:** We propose instead to form pseudo-tracks by creating anchor points and rigidly tying together every pixel with their closest anchor point.
- **p. 4 / 4.1. Scene graph - extractive body cue:** In a nutshell, we consider the output 𝐹of the encoder as a bag of local features, apply feature whitening, quantize them according to a codebook ...
- **p. 5 / 4.2. Local reconstruction - extractive body cue:** Since the encoder features {𝐹𝑛}𝑛=1..𝑁have already been extracted and cached during scene graph construction (section 4.1), we only need to run the ViT decoder Dec(), ...
- **p. 5 / 4.2. Local reconstruction - extractive body cue:** (1) From it, we then recover the canonical depthmap ˜𝑍𝑛= ˜𝑋𝑛 :,:,3 and the focal length using Weiszfeld algorithm [64]: 𝑓∗= arg min 𝑓 ∑︁ ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The proposed method builds on the recently introduced MASt3R model which, given two input images 𝐼𝑛, 𝐼𝑚∈ ℝ𝐻×𝑊×3, performs joint local 3D reconstruction and pixelwise matching [27]. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3. Preliminaries), p. 2 (1. Introduction) |
| State/latent | builds, recently, introduced, MASt3R, model, given, input, images, performs, joint, local, reconstruction | geometry, map, object/relationship state | p. 3 (3. Preliminaries), p. 2 (1. Introduction), p. 3 (3. Preliminaries) |
| Output/action | In this work, we propose MASt3R-SfM, a fullyintegrated SfM pipeline that can handle completely unconstrained input image collections, i.e. ranging from a single view to large-scale scenes, possibly without any camera motion ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 4 (4.1. Scene graph) |
| Objective/outcome | Global optimization proceeds with gradient descent of a matching loss in 3D space, followed by refinement in terms of 2D reprojection error. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (4. Proposed Method), p. 4 (4. Proposed Method), p. 5 (4.3. Coarse alignment) |

## Main Claims and Actual Contribution

- MASt3R 특징을 영상 검색에 재사용해 비교할 쌍을 줄이고 국소 점 지도를 메모리 부담이 작은 전역 정렬에 이용한다. [PDF 3쪽](https://arxiv.org/pdf/2409.19152v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2409.19152v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2409.19152v1#page=5)
- 여러 규모와 장면에서 카메라 등록·자세 정확도를 평가하고 일반 SfM 및 학습 기반 방법과 비교했다. [PDF 6쪽](https://arxiv.org/pdf/2409.19152v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2409.19152v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2409.19152v1#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (5.2. Comparison with the state of the art), p. 7 (5.2. Comparison with the state of the art) |
| Embodiment/environment | We point out that, not only these splits select a subset of scenes for each dataset (in details: 3 scenes from Mip-360, 7 from LLFF, 14 from T&T and 2 from CO3Dv2), ... | hardware/simulator version and reset protocol | p. 7 (5.2. Comparison with the state of the art), p. 6 (5.1. Experimental setup) |
| Dataset/benchmark | When reported at the dataset level, metrics are averaged over all scenes. | role, split, size and leakage | p. 7 (5.2. Comparison with the state of the art), p. 6 (5.1. Experimental setup), p. 6 (5.1. Experimental setup), p. 7 (5.2. Comparison with the state of the art) |
| Metric | We report standard visual localization accuracy metrics, i.e. the percentages of images successfully localized within error thresholds of (0.25m, 2°) / (0.5m, 5°) / (5m, 10°) and (0.25m, 2°) / (0.5m, 10°) ... | definition, denominator, direction and uncertainty | p. 8 (8.4 GB), p. 15 (Figure/Table caption), p. 6 (5.1. Experimental setup) |
| Baseline/ablation | Overall, we find that combining short-range (𝑘-NN) and long-range (keyframes) connections is important for Method Aachen-Day-Night↑ InLoc↑ Day Night DUC1 DUC2 Kapture [21]+R2D2 [41] 91.3/97.0/99.5 78.5/91.6/100 41.4/60.1/73.7 47.3/67.2/ ... | fair input/data/compute/action matching | p. 8 (8.4 GB), p. 6 (5. Experimental Results), p. 7 (5.2. Comparison with the state of the art) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 6. Conclusion - extractive body cue:** After analyzing the results, we observe that failures are due to the presence of outlier (false) matches between similar-looking structures.
- **p. 12 / 6. Conclusion - extractive body cue:** MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion 7154 false matches (30° azimut, 0° elevation) (240° azimut, 0° elevation) 6659 false matches (60° azimut, 30° elevation) ...
- **p. 10 / 6. Conclusion - extractive body cue:** In such cases, the triangulation step from traditional SfM pipeline becomes ill-defined and notoriously fails.
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 6: In all failure cases that we have manually reviewed, the root cause of failure was the presence of wrong matches (outliers) between similar-looking ...
- **p. 9 / 6. Conclusion - extractive body cue:** Thanks to the strong priors encoded in the underlying MASt3R foundation model upon which our approach is based, it can even deal with cases without ...
- **p. 7 / 5.2. Comparison with the state of the art - extractive body cue:** The fact that COLMAP and VGGSfM also perform relatively poorly indicates a high sensitivity to not having highly overlapping images, meaning that in the end ...
- **p. 9 / 8.4 GB - extractive body cue:** As expected, refinement, a strongly non-convex bundle-adjustment problem, cannot recover from a random initialization (𝜈1 = 0).

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.1. Scene graph), p. 5 (4.2. Local reconstruction)이다.
