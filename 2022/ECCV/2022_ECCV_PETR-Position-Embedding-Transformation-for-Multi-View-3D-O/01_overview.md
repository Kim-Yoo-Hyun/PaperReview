# PETR: Position Embedding Transformation for Multi-View 3D Object Detection

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2203.05625.
> PDF retrieval source: https://arxiv.org/pdf/2203.05625. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / ECCV
- Authors: Yingfei Liu, Tiancai Wang, Xiangyu Zhang, Jian Sun
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://arxiv.org/abs/2203.05625
- Full-text retrieval: https://arxiv.org/pdf/2203.05625
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136870523.pdf)

## Why This Paper Is Here

PETR는 여러 카메라의 2D 특징에 카메라 기하로 계산한 3D 위치 정보를 넣어 물체 질의가 3D 경계 상자를 직접 예측하게 한다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136870523.pdf#page=1) · [PDF 5쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136870523.pdf#page=5)

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** 3D object detection from multi-view images is appealing due to its low cost in autonomous driving system.
- **p. 1 / 1 Introduction - extractive body cue:** Previous works [6,33,49,34,48] mainly solved this problem from the perspective of monocular object detection.
- **p. 1 / 1 Introduction - extractive body cue:** Recently, DETR [4] has gained remarkable attention due to its contribution on end-to-end object detection.
- **p. 1 / 1 Introduction - extractive body cue:** In DETR [4], each object query represents an object and interacts with the 2D features in transformer decoder to produce the predictions (see Fig.
- **p. 1 / 1 Introduction - extractive body cue:** Simply extended from DETR [4] framework, DETR3D [51] provides an intuitive solution for end-to-end 3D object detection.
- **p. 1 / 1 Introduction - extractive body cue:** However, such 2D-to-3D transformation in DETR3D [51] may introduce several problems.
- **p. 1 / 1 Introduction - extractive body cue:** Second, only the image feature at the projected point will be collected, which fails to perform the representation learning from global view.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** To summarize, our contributions are: - We propose a simple and elegant framework, termed PETR, for multi-view 3D object detection.
- **p. 1 / 1 Introduction - extractive body cue:** Recently, DETR [4] has gained remarkable attention due to its contribution on end-to-end object detection.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we aim to develop a simple and elegant framework based on DETR [4] for 3D object detection.
- **p. 5 / 3 Method - extractive body cue:** Object queries, generated from query generator, are updated through the interaction with 3D position-aware features in transformer decoder.
- **p. 7 / 3 Method - extractive body cue:** In each decoder layer, object queries interact with 3D position-aware features through the multi-head attention and feed-forward network.
- **p. 5 / 3 Method - extractive body cue:** Then 2D image features and 3D coordinates are injected to proposed 3D position encoder to generate the 3D position-aware features.
- **p. 6 / 3 Method - extractive body cue:** Given the 2D features F 2d and 3D coordinates P 3d, the P 3d is first feed into a multi-layer perception (MLP) network and transformed ...
- **p. 6 / 3 Method - extractive body cue:** Finally, we flatten the 3D position-aware features as the key component of transformer decoder.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given the images I = {Ii ∈R3×HI×WI, i = 1, 2, . . . , N} from N views, the images are input to the backbone network (e.g. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3 Method), p. 5 (3 Method) |
| State/latent | Given, images, views, input, backbone, network, multi-view, image, features, convolution, layer, dimension | geometry, map, object/relationship state | p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method) |
| Output/action | The multi-view images are input to the backbone network (e.g. | point map, pose, scene graph, affordance 또는 query result | p. 5 (3 Method), p. 6 (3 Method), p. 2 (1 Introduction) |
| Objective/outcome | 3.5 Head and Loss The detection head mainly includes two branches for classification and regression. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method) |

## Main Claims and Actual Contribution

- 영상 특징 격자의 각 광선을 깊이 방향으로 이산화하고 3D 좌표를 위치 임베딩으로 바꿔 멀티뷰 특징에 결합한다. [PDF 5쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136870523.pdf#page=5) · [PDF 6쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136870523.pdf#page=6) · [PDF 7쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136870523.pdf#page=7)
- nuScenes의 카메라 기반 3D 검출에서 검출 지표를 비교하고 3D 위치 임베딩과 멀티뷰 특징의 효과를 분석했다. [PDF 9쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136870523.pdf#page=9) · [PDF 10쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136870523.pdf#page=10) · [PDF 11쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136870523.pdf#page=11)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Embodiment/environment | 4.1 Datasets and Metrics We validate our method on nuScenes benchmark [3]. | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Dataset/benchmark | 2 shows the performance comparison on nuScenes test set. | role, split, size and leakage | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Metric | Consistent with official evaluation metrics, we report nuScenes Detection Score (NDS) and mean Average Precision (mAP), along with mean Average Translation Error (mATE), mean Average Scale Error (mASE), mean Average Orientation Error(mA ... | definition, denominator, direction and uncertainty | p. 8 (4 Experiments), p. 13 (4 Experiments), p. 9 (4 Experiments) |
| Baseline/ablation | It achieves state-of-the-art performance and can serve as a strong baseline for future research. | fair input/data/compute/action matching | p. 14 (4 Experiments), p. 12 (4 Experiments), p. 9 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 4 Experiments - extractive body cue:** Finally, we provide some failure cases (see Fig.
- **p. 14 / 4 Experiments - extractive body cue:** We mark the failure cases by red and green circles.
- **p. 12 / 4 Experiments - extractive body cue:** The global feature of object query fail to make the model converge. "Fix-BEV" is the fixed anchor points are generated with the number of 39×39 ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 5 (3 Method), p. 7 (3 Method), p. 6 (3 Method)이다.
