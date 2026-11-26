# 3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1910.02527.
> PDF retrieval source: https://arxiv.org/pdf/1910.02527. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / ICCV
- Authors: Iro Armeni, Zhi-Yang He, JunYoung Gwak, Amir R. Zamir, Martin Fischer, Jitendra Malik, Silvio Savarese
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Scene Graph, semantic, geometry, Graph Reasoning
- Official paper: https://arxiv.org/abs/1910.02527
- Full-text retrieval: https://arxiv.org/pdf/1910.02527
- Code/Project: https://3dscenegraph.stanford.edu/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content_ICCV_2019/papers/Armeni_3D_Scene_Graph_A_Structure_for_Unified_Semantics_3D_Space_ICCV_2019_paper.pdf)

## Why This Paper Is Here

3D Scene Graph는 실내 스캔을 건물·방·물체·카메라의 관계와 속성으로 구성해 장면에 대한 구조화된 질의를 지원한다. [PDF 1쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Armeni_3D_Scene_Graph_A_Structure_for_Unified_Semantics_3D_Space_ICCV_2019_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Armeni_3D_Scene_Graph_A_Structure_for_Unified_Semantics_3D_Space_ICCV_2019_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A comprehensive semantic understanding of a scene is important for many applications - but in what space should diverse semantic information (e.g., objects, scene categories, ...
- **p. 1 / Abstract - extractive body cue:** Aspiring to have one unified structure that hosts diverse types of semantics, we follow the Scene Graph paradigm in 3D, generating a 3D Scene Graph.
- **p. 1 / Abstract - extractive body cue:** Given a 3D mesh and registered panoramic images, we construct a graph that spans the entire building and includes semantics on objects (e.g., class, material, ...
- **p. 1 / Abstract - extractive body cue:** However, this process is prohibitively labor heavy if done manually.
- **p. 1 / Abstract - extractive body cue:** To alleviate this we devise a semi-automatic framework that employs existing detection methods and enhances them using two main constraints: I. framing of query images ...
- **p. 2 / 1. Introduction - extractive body cue:** This gives free computation for various attributes and relationships. • We propose a two-step robustification approach to optimizing semantic recognition using imperfect existing detectors, which ...

## Core Idea

- **p. 4 / 3. 3D Scene Graph Structure - extractive body cue:** The input to our method is the typical output of 3D scanners and consists of 3D mesh models, registered RGB panoramas and the corresponding camera ...
- **p. 2 / 1. Introduction - extractive body cue:** This gives free computation for various attributes and relationships. • We propose a two-step robustification approach to optimizing semantic recognition using imperfect existing detectors, which ...
- **p. 1 / 1. Introduction - extractive body cue:** 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera.
- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this paper can be summarized as: • We extend the scene graph idea in [27] to 3D space and ground semantic information ...
- **p. 3 / C S1 - extractive body cue:** The Gibson database [44], consists of several hundreds of 3D mesh models with registered panoramic images.
- **p. 4 / 4. Constructing the 3D Scene Graph - extractive body cue:** In our experiments (Section 5), we used the best reported performing Mask RCNN network [18] and got results only for detections with a confidence score ...
- **p. 2 / 1. Introduction - extractive body cue:** To construct the 3D Scene Graph, we combine stateof-the-art algorithms in a mainly automatic approach to semantic recognition.
- **p. 1 / Abstract - extractive body cue:** To alleviate this we devise a semi-automatic framework that employs existing detection methods and enhances them using two main constraints: I. framing of query images ...

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | 표면 메시와 정합된 RGB 파노라마 |
| 표현 | 건물·방·물체·카메라 계층과 관계 |
| 출력 | 3D 장면의 구조화된 주석 |
| 평가 | 실내 장면 주석과 그래프 질의 |

[원문 4쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Armeni_3D_Scene_Graph_A_Structure_for_Unified_Semantics_3D_Space_ICCV_2019_paper.pdf#page=4) · [원문 8쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Armeni_3D_Scene_Graph_A_Structure_for_Unified_Semantics_3D_Space_ICCV_2019_paper.pdf#page=8)

## Main Claims and Actual Contribution

- 건물에서 개별 물체와 관측 카메라까지 잇는 계층을 정의하고 공간 관계 및 관측 속성을 그래프에 표현한다. [PDF 3쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Armeni_3D_Scene_Graph_A_Structure_for_Unified_Semantics_3D_Space_ICCV_2019_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Armeni_3D_Scene_Graph_A_Structure_for_Unified_Semantics_3D_Space_ICCV_2019_paper.pdf#page=4)
- 여러 뷰의 예측을 3차원에 모으고 사람이 결과를 검수하는 방식으로 주석을 구축해 실제 스캔에서의 활용 예를 제시했다. [PDF 4쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Armeni_3D_Scene_Graph_A_Structure_for_Unified_Semantics_3D_Space_ICCV_2019_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Armeni_3D_Scene_Graph_A_Structure_for_Unified_Semantics_3D_Space_ICCV_2019_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Armeni_3D_Scene_Graph_A_Structure_for_Unified_Semantics_3D_Space_ICCV_2019_paper.pdf#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (5.2. Evaluation of Automated Pipeline), p. 6 (5.2. Evaluation of Automated Pipeline) |
| Embodiment/environment | The semantic categories used come from the COCO dataset [33] for objects, MINC [8] for materials, and DTD [12] for textures. | hardware/simulator version and reset protocol | p. 6 (5.1. Dataset Statistics), p. 6 (5.2. Evaluation of Automated Pipeline) |
| Dataset/benchmark | To this end, we perform another set of experiments using BlitzNet [15], a network with faster inference but worse reported performance on the COCO dataset (AP 34.1). | role, split, size and leakage | p. 6 (5.1. Dataset Statistics), p. 6 (5.2. Evaluation of Automated Pipeline), p. 7 (5.2. Evaluation of Automated Pipeline), p. 8 (5.3. 2D Scene Graph Prediction) |
| Metric | This suggests that the robustification mechanisms can provide similar value in increasing the performance of standard detectors and correct errors, regardless of initial predictions. | definition, denominator, direction and uncertainty | p. 7 (5.2. Evaluation of Automated Pipeline), p. 8 (5.3. 2D Scene Graph Prediction), p. 7 (5.2. Evaluation of Automated Pipeline) |
| Baseline/ablation | Baselines: We compare the following approaches in 2D: • Mask R-CNN [18]: We run Mask R-CNN on 6 rectilinear images sampled on the panorama with no overlap. | fair input/data/compute/action matching | p. 6 (5.2. Evaluation of Automated Pipeline), p. 7 (5.2. Evaluation of Automated Pipeline), p. 7 (5.2. Evaluation of Automated Pipeline) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Semantic statistics for bed: (a) Number of object instances in buildings. (b) Distribution of its surface coverage. (c) Nearest object instance in 3D ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera. Elements are nodes in the graph and have ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Framing: Examples of sampled rectilinear images using the framing robustification mechanism are shown in the dashed colored boxes. Detections (b) on individual frames ...
- **p. 6 / 5.2. Evaluation of Automated Pipeline - extractive body cue:** The panorama results are obtained after applying both robustification mechanisms.
- **p. 7 / 5.2. Evaluation of Automated Pipeline - extractive body cue:** We want to further understand the behavior of the two robustification mechanisms when using a less accurate detector.
- **p. 7 / 5.2. Evaluation of Automated Pipeline - extractive body cue:** This suggests that the robustification mechanisms can provide similar value in increasing the performance of standard detectors and correct errors, regardless of initial predictions.
- **p. 8 / 5.3. 2D Scene Graph Prediction - extractive body cue:** We focus on relationship classification and provide results on: (a) spatial order and (b) relative volume classification, as well as on (c) amodal mask segmentation ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (C S1), p. 4 (4. Constructing the 3D Scene Graph), p. 4 (3. 3D Scene Graph Structure), p. 1 (Abstract)이다.

## 검색 태그 근거

실내의 3D 메시와 정합한 RGB 파노라마를 바탕으로 건물·방·물체·카메라의 속성과 관계를 구성한다. 확인한 과제는 그래프 기반 장면 주석과 예시 질의다. [원문 4쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Armeni_3D_Scene_Graph_A_Structure_for_Unified_Semantics_3D_Space_ICCV_2019_paper.pdf#page=4) · [원문 8쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Armeni_3D_Scene_Graph_A_Structure_for_Unified_Semantics_3D_Space_ICCV_2019_paper.pdf#page=8)
