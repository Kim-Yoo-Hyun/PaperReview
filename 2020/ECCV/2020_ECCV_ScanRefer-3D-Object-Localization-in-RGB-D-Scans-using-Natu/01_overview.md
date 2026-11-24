# ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1912.08830.
> PDF retrieval source: https://arxiv.org/pdf/1912.08830. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / ECCV
- Authors: Dave Zhenyu Chen, Angel X. Chang, Matthias Nießner
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D visual grounding, RGB-D, semantic
- Official paper: https://arxiv.org/abs/1912.08830
- Full-text retrieval: https://arxiv.org/pdf/1912.08830
- Code/Project: https://daveredrum.github.io/ScanRefer/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650205.pdf)

## Why This Paper Is Here

ScanRefer는 RGB-D로 스캔한 장면의 점군과 자연어 설명을 입력받아 설명에 해당하는 물체의 3차원 경계 상자를 예측한다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650205.pdf#page=1) · [PDF 4쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650205.pdf#page=4)

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** In recent years, there has been tremendous progress in both semantic understanding and localization of objects in 2D images from natural language (also known as ...
- **p. 2 / 1 Introduction - extractive body cue:** Flickr30K Entities [47] have enabled the development of various methods for visual grounding in 2D [23, 22, 39].
- **p. 2 / 1 Introduction - extractive body cue:** However, these methods and datasets are restricted to 2D images, where object localization fails to capture the true 3D extent of an object (see Fig.
- **p. 2 / 1 Introduction - extractive body cue:** This is a limitation for applications ranging from assistive robots to AR/VR agents where understanding the global 3D context and the physical size is important, ...
- **p. 2 / 1 Introduction - extractive body cue:** [31] looked at coreference in 3D, but was limited to single-view RGB-D images.

## Core Idea

- **p. 6 / 5 Method - extractive body cue:** Our architecture consists of two main modules: 1) detection & encoding; 2) fusion & localization (Fig.
- **p. 7 / 5 Method - extractive body cue:** 5.2 Network Architecture Our method takes as input the preprocessed point cloud P′ and the word embedding sequence W representing the input description and outputs ...
- **p. 8 / 5 Method - extractive body cue:** Conceptually, our localization pipeline consists of the following four stages: detection, encoding, fusion and localization.
- **p. 8 / 5 Method - extractive body cue:** Next, the proposal module takes in the point clusters and processes those clusters to predict the objectness mask Dobjn ∈RM×1 and the axis-aligned bounding boxes ...
- **p. 2 / 1 Introduction - extractive body cue:** Flickr30K Entities [47] have enabled the development of various methods for visual grounding in 2D [23, 22, 39].
- **p. 7 / 5 Method - extractive body cue:** 6: ScanRefer architecture: The PointNet++ [51] backbone takes as input a point cloud and aggregates it to high-level point feature maps, which are then clustered ...
- **p. 9 / 5 Method - extractive body cue:** 5.4 Training and Inference Training During training, the detection and encoding modules propose object candidates as point clusters, which are then fed into the fusion ...
- **p. 8 / 5 Method - extractive body cue:** Object detection loss We use the same detection loss Ldet as introduced in Qi et al.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The detection & encoding module encodes the input point cloud and description, and outputs the object proposals and the language embedding, which are fed into the fusion module to mask out invalid ... | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (5 Method), p. 7 (5 Method) |
| State/latent | detection, encoding, module, encodes, input, point, cloud, description, outputs, object, proposals, language | geometry, map, object/relationship state | p. 6 (5 Method), p. 7 (5 Method), p. 7 (5 Method) |
| Output/action | 5.2 Network Architecture Our method takes as input the preprocessed point cloud P′ and the word embedding sequence W representing the input description and outputs the 3D | point map, pose, scene graph, affordance 또는 query result | p. 7 (5 Method), p. 7 (5 Method), p. 8 (5 Method) |
| Objective/outcome | We then use a cross-entropy loss as the localization loss Lloc = -PM i=1 ti log(si). | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 8 (5 Method), p. 9 (5 Method), p. 7 (5 Method) |

## Main Claims and Actual Contribution

- ScanNet 장면 800개에 있는 물체 11,046개에 대해 사람이 작성한 지시 표현 51,583개를 수집했다. [PDF 3쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650205.pdf#page=3) · [PDF 5쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650205.pdf#page=5)
- 점군의 물체 후보 특징과 문장 임베딩을 결합해 후보별 대응 점수를 학습하고, 예측 상자와 정답 상자의 겹침으로 위치 추정을 평가했다. [PDF 7쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650205.pdf#page=7) · [PDF 8쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650205.pdf#page=8) · [PDF 11쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650205.pdf#page=11)

## Evaluation Scope

51,583개는 지시 표현의 수이고 11,046개는 지시된 물체의 수다. 표 4는 예측 상자가 정답 상자와 IoU 0.25 또는 0.5 기준을 넘긴 질의의 비율을 같은 범주 물체가 하나인 장면과 여럿인 장면으로 나누어 보고한다. [PDF 3쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650205.pdf#page=3) · [PDF 5쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650205.pdf#page=5) · [PDF 11쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650205.pdf#page=11)

## Explicit Limitations and Failure Boundary

- **p. 13 / 6 Experiments - extractive body cue:** In contrast, even provided with a pool of ground truth proposals, OracleRefer sometimes still fails to predict correct bounding boxes, while One-stage is limited by ...
- **p. 12 / 6 Experiments - extractive body cue:** We show examples where our method produced good predictions (blue block) as well as failure cases (orange block).
- **p. 13 / 6 Experiments - extractive body cue:** Some failure cases of our method are displayed in the orange block in Fig.
- **p. 33 / Figure/Table caption - extractive body cue:** Fig. 17: Additional qualitative analysis in the "unique" scenarios where there is only one object from a certain category. Our method is capable of localizing ...
- **p. 34 / Figure/Table caption - extractive body cue:** Fig. 18: Additional qualitative analysis for the "multiple" subset where there are multiple objects with the same category as the target objects. While our methods ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We introduce the task of object localization in 3D scenes using natural language. Given as input a 3D scene and a natural language ...
- **p. 28 / B.1 Fusion Module - extractive body cue:** As expected, models with the language-based object classifier (rows [g-k]) does not results in better object detection compared to models without such a module (rows ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 7 (5 Method), p. 9 (5 Method), p. 6 (5 Method)이다.
