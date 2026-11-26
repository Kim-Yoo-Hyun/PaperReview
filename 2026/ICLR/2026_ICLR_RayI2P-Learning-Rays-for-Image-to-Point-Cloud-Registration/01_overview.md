# RayI2P: Learning Rays for Image-to-Point Cloud Registration

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/49f42aafbcce59b2665640cb9f3d794f-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247078. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Xinjun Li, Wenfei Yang, Zhixin Cheng, Jiacheng Deng, Fei Wang, Chen Qian, Tianzhu Zhang
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: geometry, point cloud, 3D Vision, 3D Registration
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/49f42aafbcce59b2665640cb9f3d794f-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/49f42aafbcce59b2665640cb9f3d794f-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

RayI2P는 영상 패치에서 장면으로 향하는 광선 묶음을 예측하고 이를 이용해 영상과 점군 사이의 카메라 자세를 추정한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/49f42aafbcce59b2665640cb9f3d794f-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Image-to-point cloud registration aims to estimate the 6-DoF camera pose of a query image relative to a 3D point cloud map.
- **p. 1 / ABSTRACT - extractive body cue:** Existing methods fall into two categories: matching-free methods regress pose directly using geometric priors, but lack fine-grained supervision and struggle with precise alignment; matching-based methods ...
- **p. 1 / ABSTRACT - extractive body cue:** To address these issues, we propose a novel ray-based registration framework that first predicts patch-wise 3D ray bundles connecting image patches to the 3D scene ...
- **p. 1 / ABSTRACT - extractive body cue:** This formulation naturally resolves projection ambiguity, provides scaleconsistent geometry encoding, and enables fine-grained supervision for accurate pose estimation.
- **p. 1 / ABSTRACT - extractive body cue:** Experiments on KITTI and nuScenes show that our approach achieves state-of-the-art registration accuracy, outperforming existing methods.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** This modality gap makes it inherently difficult to design shared feature representations and establish reliable 2D-3D correspondences.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, as illustrated in Figure 1(a), this frustum-based optimization only provides coarse supervision, and the resulting poses are often inaccurate due to the lack of ...

## Core Idea

- **p. 3 / 1 INTRODUCTION - extractive body cue:** The main contributions are summarized as follows: (1) We propose a novel ray-based paradigm for image-to-point cloud registration, which effectively addresses the core limitations of ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To realize this idea, we propose a novel ray-based framework for image-to-point cloud registration as shown in Figure 1(c).
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (2) Extensive experiments on KITTI and nuScenes demonstrate that our method achieves state-of-the-art performance in cross-modal registration accuracy, validating the effectiveness of our ray-based representation.
- **p. 4 / 3 METHOD - extractive body cue:** 3.1 OVERVIEW Given an image I ∈RH×W ×3 and a point cloud P ∈RN×3 from the same scene, our goal is to determine the camera ...
- **p. 4 / 3 METHOD - extractive body cue:** In this paper, we propose a ray-based imageto-point cloud registration method composed of two main stages: a ray prediction module to infer consistent 3D rays ...
- **p. 5 / 3 METHOD - extractive body cue:** We then apply a transformer-based fusion module (Vaswani et al., 2017) consisting of multiple self and cross attention layers, executed in an alternate fashion for ...
- **p. 5 / 3 METHOD - extractive body cue:** To encourage each image patch to attend more to geometrically relevant 3D points, we propose a focus loss that guides the attention distribution in cross ...
- **p. 6 / 3 METHOD - extractive body cue:** To address this, we propose a learnable ray-guided pose regression module that estimates the camera pose from fused patch features Ff, predicted patch rays r, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The output feature map is downsampled by a factor of 8 relative to the input image, yielding a resolution of 20 × 64 for KITTI and 20 × 40 for nuScenes. | RGB-D, image set, point cloud, depth와 camera pose | p. 16 (A.6 MORE IMPLEMENTATION DETAILS), p. 5 (3 METHOD) |
| State/latent | output, feature, downsampled, factor, relative, input, image, yielding, resolution, KITTI, nuScenes, Through | geometry, map, object/relationship state | p. 16 (A.6 MORE IMPLEMENTATION DETAILS), p. 5 (3 METHOD), p. 4 (3 METHOD) |
| Output/action | Through L rounds of alternate interaction, the patch features are progressively refined with both global image context and geometry-aware cues from the point cloud, enabling the network to reason about each patch's ... | point map, pose, scene graph, affordance 또는 query result | p. 5 (3 METHOD), p. 4 (3 METHOD), p. 1 (1 INTRODUCTION) |
| Objective/outcome | The overall loss consists of three terms: a ray regression loss Lray, a camera pose loss Lcam, and a focus loss Lfoc introduced in Equation 7. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD) |

## Main Claims and Actual Contribution

- 영상 패치별 광선과 점군의 공간 관계를 학습하고 미분 가능한 회귀 모듈로 상대 자세를 구한다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/49f42aafbcce59b2665640cb9f3d794f-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/49f42aafbcce59b2665640cb9f3d794f-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/49f42aafbcce59b2665640cb9f3d794f-Paper-Conference.pdf#page=5)
- KITTI와 nuScenes에서 정합 오차·효율을 비교하고 광선 기반 자세 회귀의 구성요소를 점검했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/49f42aafbcce59b2665640cb9f3d794f-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/49f42aafbcce59b2665640cb9f3d794f-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/49f42aafbcce59b2665640cb9f3d794f-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Embodiment/environment | 4.2 DATASETS We conduct experiments on two mostly used benchmarks: KITTI and nuScenes. | hardware/simulator version and reset protocol | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Dataset/benchmark | While classical pose solver (Row 4) achieves reasonable results, it is less stable than learning-based formulation, with notably larger mean and variance in rotation errors on the nuScenes dataset. | role, split, size and leakage | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Metric | 4.3 EVALUATION METRICS To assess registration performance, we follow the protocol from VP2P-match (Zhou et al., 2023), reporting three key metrics: average Relative Translation Error (RTE), average Relative Rotation Error (RRE), and ... | definition, denominator, direction and uncertainty | p. 7 (4 EXPERIMENTS), p. 14 (A.1 EVALUATION METRICS), p. 7 (4 EXPERIMENTS) |
| Baseline/ablation | 4.4 COMPARISON WITH STATE-OF-THE-ART METHODS Baselines. | fair input/data/compute/action matching | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 16 / A.5.2 FAILURE CASES UNDER COMPLETELY INCORRECT OVERLAP PREDICTION - extractive body cue:** This failure mode, although observed only in rare extreme cases, reveals a fundamental limitation of the current framework: when the predicted overlap region is entirely ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 5: Visual comparison between classical pose solver and our proposed ray-guided pose re- gression module. Classical pose solver suffers from unstable predictions under noisy ...
- **p. 9 / 5 CONCLUSION - extractive body cue:** In this paper, we present a novel ray-based framework for image-to-point cloud registration that overcomes key limitations of both matching-based and matching-free approaches.
- **p. 15 / A.5 LIMITATIONS AND FUTURE WORK - extractive body cue:** While our method achieves competitive performance on challenging outdoor datasets, it still exhibits certain limitation primarily associated with the reliance on overlap prediction, which is ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 7: Failure Cases Under Completely Incorrect Overlap Prediction. Visualization of a rare but critical failure mode where the predicted overlapping region contains no part ...
- **p. 16 / A.5.2 FAILURE CASES UNDER COMPLETELY INCORRECT OVERLAP PREDICTION - extractive body cue:** Under this condition, the cross attention mechanism is misled and lacks access to any informative cues, resulting in failed ray-level reasoning across the modalities.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Unlike CorrI2P (Ren et al., 2022), which filters out high-error samples before computing averages, we retain all test pairs during evaluation to better reflect real-world ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (3 METHOD)이다.
