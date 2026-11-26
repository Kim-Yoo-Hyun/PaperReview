# Open-Vocabulary Octree-Graph for 3D Scene Understanding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Zhigang Wang, Yifei Su, Chenhui Li, Dong Wang, Yan Huang, Xuelong Li, Bin Zhao
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, 3D Scene Graph, semantic
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.pdf
- Code/Project: https://github.com/yifeisu/OV-Octree-Graph
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Octree-Graph는 물체별 적응형 옥트리를 그래프 노드로, 물체 사이의 공간 관계를 간선으로 저장한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary 3D scene understanding is indispensable for embodied agents.
- **p. 1 / Abstract - extractive body cue:** Recent works leverage pretrained vision-language models (VLMs) for object segmentation and project them to point clouds to build 3D maps.
- **p. 1 / Abstract - extractive body cue:** Despite progress, a point cloud is a set of unordered coordinates that requires substantial storage space and does not directly convey occupancy information or spatial ...
- **p. 1 / Abstract - extractive body cue:** To address these issues, we propose Octree-Graph, a novel scene representation for open-vocabulary 3D scene understanding.
- **p. 1 / Abstract - extractive body cue:** Specifically, a Chronological Group-wise Segment Merging (CGSM) strategy and an Instance Feature Aggregation (IFA) algorithm are first designed to get 3D instances and corresponding semantic ...
- **p. 1 / 1. Introduction - extractive body cue:** Point clouds are unordered discrete coordinates that require considerable storage space, making existing methods inefficient to deploy on embodied agents with limited storage resources.
- **p. 1 / 1. Introduction - extractive body cue:** Moreover, point clouds lack explicit representation of occupancy information and spatial connectivity which are critical for downstream tasks, e.g., path planning and text-based object retrieval.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows. • We propose the Octree-Graph for open-vocabulary 3D scene understanding, which efficiently depicts objects' occupancies, semantics, and relations, benefiting ...
- **p. 2 / 1. Introduction - extractive body cue:** To alleviate these problems, we propose Octree-Graph as shown in Fig.
- **p. 3 / 3.3. Chronological Group-wise Segment Merging - extractive body cue:** To this end, we propose a Chronological Group-wise Segment Merging (CGSM) strategy with semantic-guided under-segment filtering and a dynamic threshold decay strategy.
- **p. 4 / 3.5. Octree-Graph Construction and Applications - extractive body cue:** The node Ni consists of correlated semantics ns i (e.g., captions and features), center nc i, and adaptive-octree no i .
- **p. 4 / 3.5. Octree-Graph Construction and Applications - extractive body cue:** Furthermore, we propose an adaptive-octree to depict the occupancy information of each object, which acts as a node of the Octree-Graph.
- **p. 4 / 3.4. Instance Feature Aggregation - extractive body cue:** Hence, we propose a weighted average method to fuse an instance's features for an optimal feature both representative and distinctive, as shown in Fig.
- **p. 3 / 3.1. Framework Overview - extractive body cue:** Then we dynamically aggregate the redundant semantics of each instance into a distinctive feature (§ 3.4).
- **p. 3 / 3.2. Segment Proposal and Comprehension - extractive body cue:** Next, each mi is fed into the visual encoder and caption generator to obtain the visual feature f v i and caption feature f c ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | First, given input images, 2D proposals are segmented via an off-the-shelf segmenter, and corresponding visual-language features are extracted by pretrained VLMs. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 4 (3.3. Chronological Group-wise Segment Merging) |
| State/latent | First, given, input, images, proposals, segmented, off-the-shelf, segmenter, corresponding, visual-language, features, extracted | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 4 (3.3. Chronological Group-wise Segment Merging), p. 1 (1. Introduction) |
| Output/action | Subsequently, we iteratively take the union {Mk-1, Gk} as input for the kth merging, until the final instance map M is constructed. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.3. Chronological Group-wise Segment Merging), p. 1 (1. Introduction), p. 4 (3.5. Octree-Graph Construction and Applications) |
| Objective/outcome | geometric accuracy, semantic consistency와 planning/manipulation utility | geometric accuracy, semantic consistency와 planning/manipulation utility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 시간 순서대로 관측한 분할 영역과 특징을 합쳐 3차원 인스턴스를 만들고 그 형상에 맞춰 점유 공간을 표현했다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.pdf#page=5)
- 열린 어휘의 3차원 의미 분할과 구성요소를 제거한 실험을 통해 장면 표현을 평가했다. [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 7 (4.4. Ablation Studies) |
| Embodiment/environment | For the path planning task, we employ the HM3DSem [46] dataset used in HOV-SG [44], where 8 scenes are selected for evaluation. | hardware/simulator version and reset protocol | p. 5 (4.2. Dataset and Evaluation Metrics), p. 5 (4.2. Dataset and Evaluation Metrics) |
| Dataset/benchmark | Text-based object retrieval results on the Sr3D dataset. | role, split, size and leakage | p. 5 (4.2. Dataset and Evaluation Metrics), p. 5 (4.2. Dataset and Evaluation Metrics), p. 6 (4.2. Dataset and Evaluation Metrics), p. 6 (4.3. Quantitative Comparison) |
| Metric | SR denotes success rate (%). s is the threshold within which the distance between the navigation endpoint and the destination is considered successful. isting methods across all metrics on both datasets, demonstrating ... | definition, denominator, direction and uncertainty | p. 6 (4.3. Quantitative Comparison), p. 5 (4.2. Dataset and Evaluation Metrics), p. 5 (4.2. Dataset and Evaluation Metrics) |
| Baseline/ablation | Compared to the existing SoTA 3D scene graph, HOV-SG [44], we achieve +8.9% mIoU and +11.0% mAcc on the Replica dataset. | fair input/data/compute/action matching | p. 6 (4.3. Quantitative Comparison), p. 8 (4.5. Qualitative Analysis), p. 6 (4.3. Quantitative Comparison) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.4. Ablation Studies - extractive body cue:** We also analyze the impact of hyper-parameter I, and the results in Rows 3-5 show that our method exhibits robustness to I ranging from 100 ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.5. Octree-Graph Construction and Applications), p. 4 (3.4. Instance Feature Aggregation)이다.
