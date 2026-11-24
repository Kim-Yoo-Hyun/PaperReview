# Uni3DL: A Unified Model for 3D Vision-Language Understanding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3330_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03330.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: Xiang Li, Jian Ding, Zhaoyang Chen, Mohamed Elhoseiny
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3330_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03330.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03330.pdf)

## Why This Paper Is Here

Uni3DL은 점군을 직접 인코딩한 뒤 분할·검출·언어 기반 위치 추정과 설명 생성을 한 모델에서 처리한다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03330.pdf#page=1) · [PDF 6쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03330.pdf#page=6)

## Problem and Motivation

- **p. 2 / 1 Introduction - extractive body cue:** 3D perception technology stands as a fundamental element in the automatic understanding and operation within the physical world.
- **p. 2 / 1 Introduction - extractive body cue:** It enhances various applications, including autonomous driving, robotic navigation, object manipulation, and virtual reality.
- **p. 2 / 1 Introduction - extractive body cue:** 3D perception encompasses a broad spectrum of vision and vision-language tasks, such as 3D instance segmentation [10,21,24,29,35,37,53, 66,70], semantic segmentation [30,45,47-49,60,67], visual grounding [5,25,73], object ...
- **p. 2 / 1 Introduction - extractive body cue:** Despite these successes, task-specific models in 3D perception often lack generalizability, constraining their effectiveness across diverse tasks.
- **p. 2 / 1 Introduction - extractive body cue:** In contrast, the broader scientific community, as exemplified by the grand unified theory (GUT) in physics [3,32], has consistently emphasized the importance of unification.
- **p. 2 / 1 Introduction - extractive body cue:** This difficulty primarily stems from the substantial architectural differences between 2D and 3D models, along with the limited availability of extensive 3D datasets for pre-training ...
- **p. 3 / 1 Introduction - extractive body cue:** Furthermore, many existing models require multi-view images rather than direct training on 3D point clouds.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions are summarized as: - We present Uni3DL, a unified model tailored for 3D vision and language comprehension.
- **p. 3 / 1 Introduction - extractive body cue:** Uni3DL starts with a 3D encoder to extract point features and a text encoder to extract text features, followed by a carefully designed query transformer ...
- **p. 11 / 11 Method - extractive body cue:** On the BLEU-1 [44] and ROUGE-L [36] scores, our method beats precious STOA methods by a large margin (more than 20%).
- **p. 13 / 11 Method - extractive body cue:** We show results of the baseline method trained from scratch and our finetuned model.
- **p. 2 / 1 Introduction - extractive body cue:** Nevertheless, these methods are mainly designed for 3D object classification.
- **p. 12 / 11 Method - extractive body cue:** Ablation experiments are conducted by training separate models from scratch for various tasks, including ScanNet (v2) semantic segmentation, S3DIS
- **p. 14 / 11 Method - extractive body cue:** Ours + alt. means our model with alternative training.
- **p. 11 / 11 Method - extractive body cue:** 4.5 3D Captioning From Table 3, our Uni3DL model outperforms existing methods in 3D captioning on the Cap3D Objaverse dataset.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Its versatile architecture allows for the processing of both point clouds and text inputs, generating diverse outputs including masks, classes, and texts. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | versatile, architecture, allows, processing, point, clouds, text, inputs, generating, diverse, outputs, including | geometry, map, object/relationship state | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 12 (11 Method) |
| Output/action | They achieve this by matching projected multiview images with text inputs. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 Introduction), p. 12 (11 Method), p. 12 (11 Method) |
| Objective/outcome | geometric accuracy, semantic consistency와 planning/manipulation utility | geometric accuracy, semantic consistency와 planning/manipulation utility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 질의 트랜스포머가 공통 의미 특징과 마스크를 계산하고 태스크 라우터가 각 과제에 필요한 출력 헤드를 선택한다. [PDF 6쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03330.pdf#page=6) · [PDF 7쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03330.pdf#page=7) · [PDF 8쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03330.pdf#page=8)
- 의미·인스턴스 분할, 물체 검출, 시각·언어 과제에서 공통 모델을 과제별 모델과 비교했다. [PDF 10쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03330.pdf#page=10) · [PDF 11쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03330.pdf#page=11) · [PDF 12쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03330.pdf#page=12)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 10 (4.1 Dataset), p. 11 (Figure/Table caption) |
| Embodiment/environment | Following the official benchmark, we use 1,201 scenes for training, 312 for validation. | hardware/simulator version and reset protocol | p. 9 (4.1 Dataset), p. 9 (4.1 Dataset) |
| Dataset/benchmark | S3DIS dataset contains 6 large-scale areas with 271 scenes, and 13 semantic categories are annotated. | role, split, size and leakage | p. 9 (4.1 Dataset), p. 9 (4.1 Dataset), p. 10 (4.1 Dataset), p. 10 (4.1 Dataset) |
| Metric | Our method achieves significantly better performance than TGNN method as indicated by instance-average IoU, and accuracy at the IoU thresholds of 0.25 and 0.5. | definition, denominator, direction and uncertainty | p. 10 (4.1 Dataset), p. 10 (4.1 Dataset), p. 11 (Figure/Table caption) |
| Baseline/ablation | Fig. 5: 3D captioning results on Cap3D Objaverse dataset. 4.7 Zero-Shot 3D Object Classification We evaluate the zero-shot 3D classification performance on the ModelNet10/40 dataset [61]. Experiments demonstrate that our Uni3DL model ... | fair input/data/compute/action matching | p. 12 (Figure/Table caption), p. 13 (Figure/Table caption), p. 9 (4.1 Dataset) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 5 Conclusion - extractive body cue:** We introduce Uni3DL, a unified model for generalized 3D vision and language understanding tasks.
- **p. 14 / 5 Conclusion - extractive body cue:** We design a query transformer to attentively align 3D features with latent and text queries.
- **p. 14 / 5 Conclusion - extractive body cue:** A task router module with multiple functional heads is designed to support diverse vision-language tasks, including 3D object classification, 3D semantic/instance segmentation, 3D object detection, ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (1 Introduction), p. 12 (11 Method), p. 14 (11 Method)이다.
