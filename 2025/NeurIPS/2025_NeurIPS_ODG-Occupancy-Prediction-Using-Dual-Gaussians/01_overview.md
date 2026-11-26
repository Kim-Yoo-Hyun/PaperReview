# ODG: Occupancy Prediction Using Dual Gaussians

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://neurips.cc/virtual/2025/poster/119271.
> PDF retrieval source: https://arxiv.org/pdf/2506.09417.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: Yunxiao Shi, Yinhao Zhu, Shizhong Han, Jisoo Jeong, Amin Ansari, Hong Cai, Fatih Porikli
- 저자 표기 근거는 게재 PDF의 표제면이다. 웹 서지는 Herbert Cai를 세 번째로, 게재 PDF는 Hong Cai를 여섯 번째로 표기한다. [게재본](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e14be0332c04c76742710e417cedb2a-Paper-Conference.pdf#page=1) · [학회 서지](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2e14be0332c04c76742710e417cedb2a-Abstract-Conference.html)
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Gaussian Splatting, LiDAR, semantic occupancy, 3D Vision
- Official paper: https://neurips.cc/virtual/2025/poster/119271
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/2e14be0332c04c76742710e417cedb2a-Abstract-Conference.html
- DOI: https://doi.org/10.52202/085713-1078
- Full-text retrieval: https://arxiv.org/pdf/2506.09417.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

ODG는 주행 장면의 정적 구조와 동적 물체에 서로 다른 희소 Gaussian 질의를 사용해 카메라 영상에서 3차원 의미 점유를 추정한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e14be0332c04c76742710e417cedb2a-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Occupancy prediction infers fine-grained 3D geometry and semantics from camera images of the surrounding environment, making it a critical perception task for autonomous driving.
- **p. 1 / Abstract - extractive body cue:** Existing methods either adopt dense grids as scene representation which is difficult to scale to high resolution, or learn the entire scene using a single ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we present ODG, a hierarchical dual sparse Gaussian representation to effectively capture complex scene dynamics.
- **p. 1 / Abstract - extractive body cue:** Building upon the observation that driving scenes can be universally decomposed into static and dynamic counterparts, we define dual Gaussian queries to better model the ...
- **p. 1 / Abstract - extractive body cue:** We utilize a hierarchical Gaussian transformer to predict the occupied voxel centers and semantic classes along with the Gaussian parameters.
- **p. 1 / 1 Introduction - extractive body cue:** Concise as box representation is, it cannot deal with out-of-vocabulary or irregularly-shaped objects (e.g. trash can on the side of road, excavator with arms deployed) ...
- **p. 1 / 1 Introduction - extractive body cue:** Such sparse representation avoids spending resource to model empty regions and improves scalability.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions can be summarized as follows: • Dual Gaussian Query Design: We propose a novel dual-query architecture comprising two distinct sets of Gaussian queries ...
- **p. 2 / 1 Introduction - extractive body cue:** To establish communication between queries, we propose a simple and effective attention scheme to achieve this.
- **p. 3 / 1 Introduction - extractive body cue:** In contrast, our method predicts Gaussians in a hierarchical coarse-to-fine fashion allowing a much larger number of Gaussians, effectively resulting in higher learning capacity.
- **p. 3 / 3 Method - extractive body cue:** Formally, 3D occupancy prediction can be defined as O = G(V), V = F(I), (1) where F(·) consists of an image backbone that extract multi-camera ...
- **p. 4 / 3 Method - extractive body cue:** For each layer Tℓ, it takes as input static Gaussian means Gs :µ,ℓ-1 and query features Qs ℓ-1 from the previous layer, and predict the ...
- **p. 5 / 3 Method - extractive body cue:** 3.4 Attention across Dynamic and Static Queries To enable effective interaction between dynamic Gaussian queries Qd and static Gaussian queries Qs, we first concatenate their ...
- **p. 5 / 3 Method - extractive body cue:** We then apply Self-Attention [50] to the combined features, allowing for rich information exchange cross both query types.
- **p. 3 / 3 Method - extractive body cue:** 3.3) and leverage attention to enable feature interaction between the dual queries (Sec.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A cross query attention is also introduced to establish effective interaction between queries, enhancing 3D occupancy prediction. • Hierarchical Coarse-to-Fine Refinement: We refine the Gaussian properties in a hierarchical coarse-to-fi ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 3 (3 Method) |
| State/latent | cross, query, attention, introduced, establish, effective, interaction, between, queries, enhancing, occupancy, prediction | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 3 (3 Method), p. 2 (1 Introduction) |
| Output/action | 3.1 Problem Definition Given an ego-vehicle at time T, the task of 3D occupancy prediction takes Nc multi-camera images (with k × Nc optional history frames where k ≥0), I = {It ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3 Method), p. 2 (1 Introduction), p. 3 (3 Method) |
| Objective/outcome | For rendered depth and semantic maps from Gaussians at all stages, we supervise depth with L1 loss and semantics with cross-entropy loss Lr = L X ℓ=1 L1( ˆDℓ, ¯D) + CE( ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3 Method), p. 3 (3 Method), p. 4 (3 Method) |

## Main Claims and Actual Contribution

- 계층적 트랜스포머로 점유 위치·범주·Gaussian 파라미터를 예측하고 렌더링된 깊이와 의미 지도로 픽셀 단위 감독을 추가한다. [PDF 3쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e14be0332c04c76742710e417cedb2a-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e14be0332c04c76742710e417cedb2a-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e14be0332c04c76742710e417cedb2a-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e14be0332c04c76742710e417cedb2a-Paper-Conference.pdf#page=6)
- Occ3D-nuScenes와 Occ3D-Waymo에서 점유 정확도를 비교하고 정적·동적 질의 및 렌더링 감독의 효과를 분석했다. [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e14be0332c04c76742710e417cedb2a-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e14be0332c04c76742710e417cedb2a-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e14be0332c04c76742710e417cedb2a-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Embodiment/environment | 4.1 Experiment Setup Datasets: We evaluate our model on the Occ3D benchmark [48] which bootstraps the nuScenes [6] and Waymo-Open [43] dataset.∗nuScenes consists of 1,000 scenes with a split of 700/150/150 for ... | hardware/simulator version and reset protocol | p. 6 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | Our extensive experiments on the Occ3D-nuScenes and Occ3D-Waymo benchmark demonstrates ODG sets new state-of-the-art results while maintaining highly competitive efficiency. | role, split, size and leakage | p. 6 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 6 (4 Experiments) |
| Metric | We set λ3d = 0.2 to balance box loss Lbox and occupancy loss Locc. | definition, denominator, direction and uncertainty | p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments) |
| Baseline/ablation | One can see that our method achieves new state-of-the-art results in terms of both mIoU and RayIoU, while maintaining competitive inference speed even when compared to latest efficient approaches. | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4 Experiments - extractive body cue:** However, as promising as ODG is, it does not come without limitations.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method), p. 3 (3 Method)이다.
