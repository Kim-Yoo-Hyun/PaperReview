# SemanticKITTI: A Dataset for Semantic Scene Understanding of LiDAR Sequences

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1904.01416.
> PDF retrieval source: https://arxiv.org/pdf/1904.01416. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / ICCV
- Authors: Jens Behley, Martin Garbade, Andres Milioto, Jan Quenzel, Sven Behnke, Cyrill Stachniss, Juergen Gall
- 저자 판본: ICCV 게재본에서 마지막 저자가 Juergen Gall로 인쇄된 것을 확인했다. CVF 웹 서지는 Jurgen Gall로 표기한다. [표제면](https://openaccess.thecvf.com/content_ICCV_2019/papers/Behley_SemanticKITTI_A_Dataset_for_Semantic_Scene_Understanding_of_LiDAR_Sequences_ICCV_2019_paper.pdf#page=1) · [학회 서지](https://openaccess.thecvf.com/content_ICCV_2019/html/Behley_SemanticKITTI_A_Dataset_for_Semantic_Scene_Understanding_of_LiDAR_Sequences_ICCV_2019_paper.html)
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, LiDAR, semantic, Dataset
- Official paper: https://arxiv.org/abs/1904.01416
- Full-text retrieval: https://arxiv.org/pdf/1904.01416
- Code/Project: http://semantic-kitti.org/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content_ICCV_2019/papers/Behley_SemanticKITTI_A_Dataset_for_Semantic_Scene_Understanding_of_LiDAR_Sequences_ICCV_2019_paper.pdf)

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 6. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

SemanticKITTI는 KITTI 주행 시퀀스의 360도 LiDAR 스캔에 점별 의미를 부여해 시간적 장면 이해를 평가한다. [PDF 1쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Behley_SemanticKITTI_A_Dataset_for_Semantic_Scene_Understanding_of_LiDAR_Sequences_ICCV_2019_paper.pdf#page=1) · [PDF 2쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Behley_SemanticKITTI_A_Dataset_for_Semantic_Scene_Understanding_of_LiDAR_Sequences_ICCV_2019_paper.pdf#page=2)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Semantic scene understanding is important for various applications.
- **p. 1 / Abstract - extractive body cue:** In particular, self-driving cars need a finegrained understanding of the surfaces and objects in their vicinity.
- **p. 1 / Abstract - extractive body cue:** Light detection and ranging (LiDAR) provides precise geometric information about the environment and is thus a part of the sensor suites of almost all self-driving ...
- **p. 1 / Abstract - extractive body cue:** Despite the relevance of semantic scene understanding for this application, there is a lack of a large dataset for this task which is based on ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce a large dataset to propel research on laser-based semantic segmentation.
- **p. 1 / 1. Introduction - extractive body cue:** Complementary sensor modalities enable to cope with deficits or failures of particular sensors.
- **p. 2 / 1. Introduction - extractive body cue:** To close this gap we propose SemanticKITTI, a large dataset showing unprecedented detail in point-wise annotation with 28 classes, which is suited for various tasks.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are: • We present a point-wise annotated dataset of point cloud sequences with an unprecedented number of classes and unseen ...
- **p. 2 / 1. Introduction - extractive body cue:** To close this gap we propose SemanticKITTI, a large dataset showing unprecedented detail in point-wise annotation with 28 classes, which is suited for various tasks.
- **p. 1 / 1. Introduction - extractive body cue:** They mainly fulfill three purposes: (i) they provide a basis to measure progress, since they allow to provide results that are reproducible and comparable, (ii) ...
- **p. 7 / Approach - extractive body cue:** We expect that new approaches could explicitly exploit the sequential information by using multiple input streams to the architecture or even recurrent neural networks to ...
- **PDF p. 6, Table 3 (DOC-QA2 원문 대조):** Table 3의 열은 parameters (million), training time (GPU hours/epoch), inference time (seconds/point cloud)다. 예를 들어 PointNet은 3/4/0.5, DarkNet53Seg는 50/3/0.1이다. 숫자만 분리해 동일 단위로 해석하지 않는다.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In summary, our main contributions are: • We present a point-wise annotated dataset of point cloud sequences with an unprecedented number of classes and unseen level-of-detail for each scan. • We furthermore ... | standardized observation, action, task state와 evaluation split | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | summary, main, contributions, present, point-wise, annotated, dataset, point, cloud, sequences, unprecedented, number | benchmark state/goal와 method decision | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 7 (Approach) |
| Output/action | They mainly fulfill three purposes: (i) they provide a basis to measure progress, since they allow to provide results that are reproducible and comparable, (ii) they uncover shortcomings of the current state ... | policy/controller trajectory 또는 measured result | p. 1 (1. Introduction), p. 7 (Approach), p. 6 (Approach) |
| Objective/outcome | success metric, robustness, generalization과 reproducibility | success metric, robustness, generalization과 reproducibility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 전체 주행 시퀀스의 점군에 의미와 물체 운동 상태를 주석하고 범주별 빈도와 가시성의 차이를 정리했다. [PDF 2쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Behley_SemanticKITTI_A_Dataset_for_Semantic_Scene_Understanding_of_LiDAR_Sequences_ICCV_2019_paper.pdf#page=2) · [PDF 3쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Behley_SemanticKITTI_A_Dataset_for_Semantic_Scene_Understanding_of_LiDAR_Sequences_ICCV_2019_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Behley_SemanticKITTI_A_Dataset_for_Semantic_Scene_Understanding_of_LiDAR_Sequences_ICCV_2019_paper.pdf#page=4)
- 단일 스캔 분할, 여러 과거 스캔을 이용한 분할과 의미 장면 완성을 서로 다른 과제로 정의하고 기준선을 제공했다. [PDF 5쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Behley_SemanticKITTI_A_Dataset_for_Semantic_Scene_Understanding_of_LiDAR_Sequences_ICCV_2019_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Behley_SemanticKITTI_A_Dataset_for_Semantic_Scene_Understanding_of_LiDAR_Sequences_ICCV_2019_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Behley_SemanticKITTI_A_Dataset_for_Semantic_Scene_Understanding_of_LiDAR_Sequences_ICCV_2019_paper.pdf#page=7)

## Evaluation Scope

SemanticKITTI는 28개 범주에 주석을 붙였다. 표 2의 단일 스캔 분할은 19개 평가 범주를 사용하고 00~10번 가운데 08번을 검증에, 11~21번을 시험에 쓴다. [PDF 2쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Behley_SemanticKITTI_A_Dataset_for_Semantic_Scene_Understanding_of_LiDAR_Sequences_ICCV_2019_paper.pdf#page=2) · [PDF 5쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Behley_SemanticKITTI_A_Dataset_for_Semantic_Scene_Understanding_of_LiDAR_Sequences_ICCV_2019_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Behley_SemanticKITTI_A_Dataset_for_Semantic_Scene_Understanding_of_LiDAR_Sequences_ICCV_2019_paper.pdf#page=6)

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion and Outlook - extractive body cue:** In future work, we plan to provide also instance-level annotation over the whole sequence, i.e., we want to distinguish different objects in a scan, but ...
- **p. 7 / 5. Evaluation of Semantic Scene Completion - extractive body cue:** Existing point cloud datasets cannot be used to address this task, as they do not allow for aggregating labeled point clouds that are sufficiently dense ...
- **p. 8 / 5. Evaluation of Semantic Scene Completion - extractive body cue:** Due to Completion Semantic Scene (IoU) Completion (mIoU) SSCNet [49] 29.83 9.53 TS3D [18] 29.81 9.54 TS3D [18] + DarkNet53Seg 24.99 10.19 TS3D [18] + ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 7: Qualitative results for the semantic scene completion approach TS3D + DarkNet53Seg + SATNet. Left: Input volume. Middle: Network prediction. Right: Ground truth. Due ...
- **p. 7 / 5. Evaluation of Semantic Scene Completion - extractive body cue:** In the case of our proposed dataset, the car carrying the LiDAR moves past 3D objects in the scene and thereby records their backsides, which ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 7 (Approach), p. 6 (Approach), p. 6 (4.2. Multiple Scan Experiments)이다.
