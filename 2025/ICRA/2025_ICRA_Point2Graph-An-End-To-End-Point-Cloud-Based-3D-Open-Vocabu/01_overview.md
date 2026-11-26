# Point2Graph: An End-To-End Point Cloud-Based 3D Open-Vocabulary Scene Graph for Robot Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/icra55743.2025.11127471.
> PDF retrieval source: https://arxiv.org/pdf/2409.10350v1. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICRA
- Authors: Yifan Xu, Ziming Luo, Qianwei Wang, Vineet Kamat, Carol Menassa
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics, 3D Vision, Navigation, 3D Scene Graph, semantic
- Official paper: https://api.crossref.org/works/10.1109/icra55743.2025.11127471
- Full-text retrieval: https://arxiv.org/pdf/2409.10350v1
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

Point2Graph는 카메라 자세가 붙은 RGB-D 영상열 없이 장면 점군에서 방과 물체를 분할·분류해 개방 어휘 3차원 장면 그래프를 만든다. [PDF 1쪽](https://arxiv.org/pdf/2409.10350v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Current open-vocabulary scene graph generation algorithms highly rely on both 3D scene point cloud data and posed RGB-D images and thus have limited applications in ...
- **p. 1 / Abstract - extractive body cue:** To solve this problem, we propose Point2Graph, a novel end-to-end point cloud-based 3D open-vocabulary scene graph generation framework in which the requirement of posed RGB-D ...
- **p. 1 / Abstract - extractive body cue:** This hierarchical framework contains room and object detection/segmentation and openvocabulary classification.
- **p. 1 / Abstract - extractive body cue:** For the room layer, we leverage the advantage of merging the geometry-based border detection algorithm with the learning-based region detection to segment rooms and create ...
- **p. 1 / Abstract - extractive body cue:** In addition, we create an end-toend pipeline for the object layer to detect and classify 3D objects based solely on 3D point cloud data.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Lacking 3D-text pair data leads to poor performance in 3D object and room segmentation and classification.
- **p. 1 / I. INTRODUCTION - extractive body cue:** For example, the point clouds created from a Building Information Model (BIM) or LiDAR sensors often lack the RGB-D images and their pose data [13], ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Generally speaking, our framework consists of a room segmentation and classification module and an object detection and classification module.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Object-Level Detection and Classification After getting the segmentation result for each room, our approach mainly consists of two steps, where the first step deals with ...
- **p. 2 / III. METHODOLOGY - extractive body cue:** In this section, we present our design of Point2Graph, which builds a compact and enriched open-vocabulary 3D scene graph with solely 3D scene model input.
- **p. 4 / III. METHODOLOGY - extractive body cue:** 5: Overview of the 3D open-vocabulary detection pipeline: It consists of two stages: (1) detection and localization using class-agnostic bounding boxes and DBSCAN filtering for ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** Voronoi Navigation Graph In order to let a robot navigate in the area where our scene graph is built, we propose a navigation graph based ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** To obtain open-vocabulary features for each room, inspired by the approach in [8], we use the CLIP visual encoder to extract embeddings from the images.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Specifically, the model takes as input both the filtered 3D point cloud and a textual description and retrieves the appropriate object label by identifying the ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** A region detection module is then applied to segment the scene into individual rooms.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | First, the input point cloud is segmented into N slices along the z-axis, with each slice projected onto an occupancy grid map denoted as Gk, k = 1, ..., N. | camera/depth stream, pose, map와 language goal | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |
| State/latent | First, input, point, cloud, segmented, slices, along, z-axis, slice, projected, onto, occupancy | robot pose, free-space/semantic map와 local goal | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), p. 4 (III. METHODOLOGY) |
| Output/action | Compared with existing methods [8], [9], our proposed Point2Graph framework solely use the scene point cloud as input to generate open-vocabulary 3D scene graph. | collision-free trajectory 또는 velocity command | p. 1 (I. INTRODUCTION), p. 4 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |
| Objective/outcome | goal reach, safety, localization error와 replanning latency | goal reach, safety, localization error와 replanning latency | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 기하 경계와 학습 기반 영역 검출을 결합해 방을 나누고, 방과 물체의 관측을 의미 특징과 대응시켜 개방 어휘 이름을 부여한다. [PDF 3쪽](https://arxiv.org/pdf/2409.10350v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2409.10350v1#page=4)
- 실제 장면 데이터에서 방·물체의 분할 및 분류 성능을 비교해, 점군만 입력하는 조건에서 얼마나 정확한 장면 표현을 얻는지 측정했다. [PDF 5쪽](https://arxiv.org/pdf/2409.10350v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2409.10350v1#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS) |
| Embodiment/environment | Evaluation for Object Detection and Classification We conducted our experiments on the widely-used ScanNetv2 [45] indoor point cloud dataset, which consists of 312 validation scenes, each annotated with semantic and instance segmentation ... | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS) |
| Dataset/benchmark | The robot should interpret the human's query and search for the room and object location in the pre-built 3D scene graph hierarchically and navigate to the most relevant location. | role, split, size and leakage | p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS) |
| Metric | The "F1" score takes their harmonic mean of Precision and Recall. "mAP" measures the average accuracy of classification across all categories Method B/N AP50 AP25 use RGB-D PLA [41] 10/7 0.22 - ... | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS) |
| Baseline/ablation | We compared our method to RoomFormer [28], the current SOTA in learning-based algorithms, and the room segmentation techniques employed in HOV-SG [8], the SOTA in geometry-based algorithms. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / V. CONCLUSION - extractive body cue:** Nevertheless, Point2Graph has its limitations.
- **p. 6 / V. CONCLUSION - extractive body cue:** In conclusion, this work presents the Point2Graph framework, which addresses the limitations of current openvocabulary 3D scene graph generation methods by eliminating the need for ...
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** Our proposed "Snap-Lookup" pipeline, which incorporates room visual features into type inference, can differentiate between various types of rooms that contain the same objects-something text-only ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY)이다.
