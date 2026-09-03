# 3D Open-Vocabulary Panoptic Segmentation with 2D-3D Vision-Language Distillation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5642_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision, semantic
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5642_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these methods are only possible due to the vast amounts of paired image-text data available, making it difficult to train similar models for 3D data.를 문제로 두고, Our contributions are summarized as follows: - We present the first approach for 3D open-vocabulary panoptic segmentation in autonomous driving. - We propose two novel loss functions, object-level distillation loss and voxellevel ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: - We present the first approach for 3D open-vocabulary panoptic segmentation in autonomous driving. - We propose two novel ...
- **p. 6 / 3 Method - extractive body cue:** To take advantage of the benefits of separating things queries and stuff queries, we propose to predict the base stuff classes with a fixed set ...
- **p. 8 / 3 Method - extractive body cue:** Combining LO with LV enables segmenting novel things and novel stuff objects simultaneously.
- **p. 4 / 3 Method - extractive body cue:** The overview of our method is presented in Fig.
- **p. 5 / 3 Method - extractive body cue:** The architecture of our method is shown in Fig.
- **p. 11 / 4 Experiments - extractive body cue:** We show that this is due to lack of supervision of the whole scene as P3Former achieves similar performance when only trained on base categories.
- **p. 13 / Figure/Table caption - extractive body cue:** Table 5: Performance on a different split. We compare the performance with a split with 5 novel classes (B11/N5). The novel things classes are bicycle, ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Impact of each component. We evaluate the impact of each component using the base/novel split in Tab. 1. We observe that each component ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these methods are only possible due to the vast amounts of paired image-text data available, making it difficult to train similar models for 3D data.를 문제로 두고, Our contributions are summarized as follows: - We present the first approach for 3D open-vocabulary panoptic segmentation in autonomous driving. - We propose two novel loss functions, object-level distillation loss and voxellevel ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method), p. 7 (3 Method), p. 4 (3 Method), p. 5 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
