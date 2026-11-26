# 3D Open-Vocabulary Panoptic Segmentation with 2D-3D Vision-Language Distillation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5642_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: Zihao Xiao, Longlong Jing, Shangxuan Wu, Alex Zihao Zhu, Jingwei Ji, Chiyu Max Jiang, Wei-Chih Hung, Thomas Funkhouser, Weicheng Kuo, Anelia Angelova, Yin Zhou, Shiwei Sheng
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision, semantic, distillation
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5642_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf)

## Why This Paper Is Here

개방 어휘 3D 파놉틱 분할을 위해 라이다 특징과 동결한 CLIP의 영상 특징을 결합해 기존 범주와 새로운 범주를 하나의 헤드로 분류한다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf#page=1) · [PDF 4쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf#page=4)

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** 3D panoptic segmentation is a crucial task in computer vision with many realworld applications, most notably in autonomous driving.
- **p. 1 / 1 Introduction - extractive body cue:** It combines 3D semantic and instance segmentation to produce per-point predictions for two different types of objects: things (e.g., car) and stuff (e.g., road).
- **p. 1 / 1 Introduction - extractive body cue:** To date, there has been significant progress in 3D panoptic segmentation [27, 40, 42, 47, 52, 58].
- **p. 1 / 1 Introduction - extractive body cue:** Most recently, methods such as [47] produce panoptic segmentation predictions directly from point clouds by leveraging learned queries to represent objects and ∗Work done while ...
- **p. 2 / 1 Introduction - extractive body cue:** Transformer-based [45] architectures [2, 4] to perform the modeling.
- **p. 2 / 1 Introduction - extractive body cue:** However, these methods are only possible due to the vast amounts of paired image-text data available, making it difficult to train similar models for 3D ...
- **p. 2 / 1 Introduction - extractive body cue:** However, existing models only predict panoptic segmentation results for a closed-set of objects.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: - We present the first approach for 3D open-vocabulary panoptic segmentation in autonomous driving. - We propose two novel ...
- **p. 6 / 3 Method - extractive body cue:** To take advantage of the benefits of separating things queries and stuff queries, we propose to predict the base stuff classes with a fixed set ...
- **p. 8 / 3 Method - extractive body cue:** Combining LO with LV enables segmenting novel things and novel stuff objects simultaneously.
- **p. 4 / 3 Method - extractive body cue:** The overview of our method is presented in Fig.
- **p. 5 / 3 Method - extractive body cue:** The architecture of our method is shown in Fig.
- **p. 5 / 3 Method - extractive body cue:** In order to improve the open vocabulary capability of our model, we propose significant changes to the P3Former architecture, as well as two new loss ...
- **p. 7 / 3 Method - extractive body cue:** We propose an additional training loss which forces our predicted object-level class embeddings to be similar to the CLIP embeddings within their corresponding masks after ...
- **p. 4 / 3 Method - extractive body cue:** Then we provide detailed descriptions of the model architecture as well as the proposed loss functions.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The LiDAR encoder is a model which takes an unordered set of points as input and extracts per-point features. | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3 Method), p. 5 (3 Method) |
| State/latent | LiDAR, encoder, model, takes, unordered, points, input, extracts, per-point, features, mainly, consists | geometry, map, object/relationship state | p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method) |
| Output/action | 1 and mainly consists of multimodal feature fusion, a segmentation head, and input text embeddings for open-vocabulary classification. | point map, pose, scene graph, affordance 또는 query result | p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method) |
| Objective/outcome | 3.3 Loss Function Closed-set panoptic segmentation models [47] are typically optimized with objective functions consisting of a classification loss Lcls and a mask prediction loss Lmask. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 7 (3 Method), p. 7 (3 Method), p. 4 (3 Method) |

## Main Claims and Actual Contribution

- 물체 단위와 복셀 단위의 증류 손실을 따로 두어 영상 모델의 의미 정보를 3D 마스크에 전달한다. [PDF 4쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf#page=4) · [PDF 6쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf#page=6) · [PDF 7쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf#page=7)
- nuScenes와 SemanticKITTI에서 새 물체 및 배경 범주별 성능을 측정하고 두 증류 손실의 역할을 분석했다. [PDF 10쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf#page=10) · [PDF 11쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf#page=11) · [PDF 12쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf#page=12)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Embodiment/environment | The nuScenes dataset [4] is a public benchmark for autonomous driving. | hardware/simulator version and reset protocol | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Dataset/benchmark | Comparisons on the nuScenes and SemanticKITTI datasets are shown in Tab. | role, split, size and leakage | p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Metric | During inference, if there are multiple labels for one class, we derive the class score by getting the maximum scores among these labels. | definition, denominator, direction and uncertainty | p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments) |
| Baseline/ablation | 4.3 Main Results Since there are no existing methods for the 3D open-vocabulary panoptic segmentation task, we mainly compare with three methods to demonstrate the capability of our method: (1) the strong ... | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 10 (4 Experiments), p. 13 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 5 Conclusion - extractive body cue:** We experimentally verified that simply extending the 2D open-vocabulary segmentation method into 3D does not yield good performance, and demonstrated that our proposed model design ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 5 (3 Method), p. 7 (3 Method), p. 4 (3 Method)이다.

## 검색 태그 근거

훈련 때는 라이다 점에 대응하는 영상의 CLIP 특징을 복셀 및 물체 수준에서 증류한다. 점군으로 예측한 마스크와 특징으로 nuScenes와 SemanticKITTI의 파놉틱 분할을 평가했다. [원문 4쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf#page=4) · [원문 9쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf#page=9)
