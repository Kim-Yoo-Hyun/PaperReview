# SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1255_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: Yang Miao, Francis Engelmann, Olga Vysotska, Federico Tombari, Marc Pollefeys, Daniel Barath
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Graph Reasoning
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1255_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf)

## Why This Paper Is Here

SceneGraphLoc은 질의 이미지가 어느 장면에 속하는지 찾기 위해 이미지의 국소 영역과 여러 3D 장면 그래프의 물체 노드를 대응시킨다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf#page=1) · [PDF 2쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf#page=2)

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Coarse visual localization, or place recognition, is a fundamental component in computer vision and robotics applications, defined as the task of identifying the approximate location ...
- **p. 2 / 1 Introduction - extractive body cue:** The training phase is represented by orange arrows, while blue arrows denote the inference phase.
- **p. 2 / 1 Introduction - extractive body cue:** During training, a query image and its associated 3D scene graph form a positive sample within a contrastive learning framework, where negative samples are generated ...
- **p. 2 / 1 Introduction - extractive body cue:** The objective is to learn the embeddings of both the graph and the image so that embeddings of the positive pair are drawn closer, whereas ...
- **p. 2 / 1 Introduction - extractive body cue:** In the inference phase, the task involves assigning the correct scene graph to a given query image from a selection of multiple graphs, achieved by ...
- **p. 2 / 1 Introduction - extractive body cue:** The challenge with current state-of-the-art image-based coarse localization methods, such as AnyLoc [55], is their dependency on extensive image databases, which are not only storage-heavy ...
- **p. 2 / 1 Introduction - extractive body cue:** This paper addresses the novel challenge of localizing a query image within a database that is represented not by conventional images but by the 3D ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** This method enables the creation of small, efficient databases and significantly accelerates the coarse localization process.
- **p. 3 / 1 Introduction - extractive body cue:** The primary contributions of this paper are as follows: 1.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We introduce the task of localizing an input image within a multi-modal reference map represented by a collection of 3D scene graphs.
- **p. 2 / 1 Introduction - extractive body cue:** This paper addresses the novel challenge of localizing a query image within a database that is represented not by conventional images but by the 3D ...
- **p. 3 / 1 Introduction - extractive body cue:** Introducing a novel problem: cross-modal localization of a query image within 3D scene graphs incorporating a mixture of modalities.
- **p. 2 / 1 Introduction - extractive body cue:** The training phase is represented by orange arrows, while blue arrows denote the inference phase.
- **p. 2 / 1 Introduction - extractive body cue:** The challenge with current state-of-the-art image-based coarse localization methods, such as AnyLoc [55], is their dependency on extensive image databases, which are not only storage-heavy ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** This strategy significantly outperforms other cross-modal methods, even without incorporating images into the map representation.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We introduce the task of localizing an input image within a multi-modal reference map represented by a collection of 3D scene graphs. | camera/depth stream, pose, map와 language goal | p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)) |
| State/latent | introduce, task, localizing, input, image, within, multi-modal, reference, represented, collection, scene, graphs | robot pose, free-space/semantic map와 local goal | p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)), p. 3 (1 Introduction) |
| Output/action | Given these modalities, the proposed method SceneGraphLoc learns a fixed-sized embedding for each node (i.e., representing object instances) in the scene graph, enabling effective matching with the objects visible in the input ... | collision-free trajectory 또는 velocity command | p. 1 (Body text (section not recovered)), p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | The objective is to learn the embeddings of both the graph and the image so that embeddings of the positive pair are drawn closer, whereas those of the negative pair are pushed ... | goal reach, safety, localization error와 replanning latency | p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- 물체의 점군·속성·관계와 선택적 영상 정보를 노드별 고정 길이 표현으로 만들어 영상 영역과 같은 공간에서 비교한다. [PDF 5쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf#page=5) · [PDF 6쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf#page=6) · [PDF 7쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf#page=7)
- 후보 장면 중 올바른 방을 검색하는 재현율과 지도 저장량을 측정하고, 그래프에 영상 특징을 포함했을 때의 차이를 보고했다. [PDF 10쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf#page=10) · [PDF 11쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf#page=11) · [PDF 12쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf#page=12)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Embodiment/environment | The 3RScan dataset [123] comprises 1335 annotated indoor scenes, representing 432 distinct rooms, with 1178 scenes (385 rooms) allocated for training and 157 (47 rooms) designated for validation. | hardware/simulator version and reset protocol | p. 11 (4 Experiments), p. 12 (4 Experiments) |
| Dataset/benchmark | SceneGraphLoc 13 Table 3: Average time (ms) of obtaining the query image embedding (teq) and of the retrieval from 10, 50, and all scenes from the 3RScan [123] and ScanNet [21] datasets. | role, split, size and leakage | p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 11 (4 Experiments) |
| Metric | To evaluate the accuracy of a method, we focus on the recall of scene selection. | definition, denominator, direction and uncertainty | p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Baseline/ablation | For comparison with state-of-the-art visual localization methods requiring large image databases, we included CVNet [63] and AnyLoc [55]. | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 10 (4 Experiments), p. 12 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 5 Conclusion - extractive body cue:** In conclusion, we introduce SceneGraphLoc, a novel method for solving the novel problem of localizing an input image within a 3D scene graph-based multi-modal reference ...
- **p. 14 / 5 Conclusion - extractive body cue:** This approach outperforms existing cross-modal methods by a large margin.
- **p. 14 / 5 Conclusion - extractive body cue:** It achieves comparable accuracy to state-of-the-art image-based techniques with significantly lower storage requirements and faster processing speeds.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (Body text (section not recovered))이다.
