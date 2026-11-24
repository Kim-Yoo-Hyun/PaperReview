# MR-COGraphs: Communication-efficient Multi-Robot Open-vocabulary Mapping System via 3D Scene Graphs

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2412.18381.
> PDF retrieval source: https://arxiv.org/pdf/2412.18381. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RA-L
- Authors: Qiuyi Gu, Zhaocheng Ye, Jincheng Yu, Jiahao Tang, Tinghao Yi, Yuhan Dong, Jian Wang, Jinqiang Cui, Xinlei Chen, Yu Wang
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics, 3D Vision, Graph Reasoning, semantic
- Official paper: https://arxiv.org/abs/2412.18381
- Venue verification: https://api.crossref.org/works/10.1109/LRA.2025.3561569
- Full-text retrieval: https://arxiv.org/pdf/2412.18381
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

MR-COGraphs는 여러 로봇이 물체 중심의 압축된 3차원 장면 그래프를 교환해 열린 어휘로 질의할 수 있는 공동 지도를 만든다. [PDF 1쪽](https://arxiv.org/pdf/2412.18381v2#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Collaborative perception in unknown environments is crucial for multi-robot systems.
- **p. 1 / Abstract - extractive body cue:** With the emergence of foundation models, robots can now not only perceive geometric information but also achieve open-vocabulary scene understanding.
- **p. 1 / Abstract - extractive body cue:** However, existing map representations that support open-vocabulary queries often involve large data volumes, which becomes a bottleneck for multi-robot transmission in communication-limited environments.
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we develop a method to construct a graph-structured 3D representation called COGraph, where nodes represent objects with semantic features and edges ...
- **p. 1 / Abstract - extractive body cue:** Before transmission, a data-driven feature encoder is applied to compress the feature dimensions of the COGraph.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, current open-vocabulary 3D map representations demand significant data storage [9][11], which becomes a communication bottleneck for multi-robot mapping systems.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This data explosion makes it difficult for multiple robots to share and update maps in real time.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** To fulfill the requirements above, we propose a Communication-efficient Multi-Robot Open-vocabulary 3D Scene Graphs-based Mapping (MR-COGraphs) System with the following contributions: • A data-efficient open-vocabulary ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 1, we propose a graph-structured open-vocabulary representation called COGraph (detailed in Section III-A).
- **p. 3 / III. METHOD - extractive body cue:** COGraphs Representation The proposed COGraph consists of the robot name, nodes, and edges.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Recent advances in visual foundation models (e.g., SAM [2]) and vision-language models (e.g., CLIP [3]) have enabled the development of open-vocabulary 3D map representations.
- **p. 3 / III. METHOD - extractive body cue:** 1, this section first outlines the map representation of the COGraph, followed by an introduction to the three key modules: 1) feature-object nodes and edges ...
- **p. 4 / III. METHOD - extractive body cue:** These features are then used to train the encoder and decoder, which are optimized to effectively compress and reconstruct high-dimensional features.
- **p. 4 / III. METHOD - extractive body cue:** 2) Training Process: We train the feature encoder and decoder using images from the ImageNet dataset [31], which contains over 80,000 images across 1,000 categories.
- **p. 5 / III. METHOD - extractive body cue:** Place recognition is then performed by iteratively calculating the feature similarity between each received node and nodes in the local COGraph.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3D back projection is conducted using FO images, depth images, and poses derived from SLAM. | camera/depth stream, pose, map와 language goal | p. 4 (III. METHOD), p. 4 (III. METHOD) |
| State/latent | back, projection, conducted, images, depth, poses, derived, SLAM, observation, conduct, further, experimental | robot pose, free-space/semantic map와 local goal | p. 4 (III. METHOD), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Output/action | Based on this observation, we conduct further experimental evaluations in Section IV-B. | collision-free trajectory 또는 velocity command | p. 4 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective/outcome | Comparison of the original and decoded features when the encoder and decoder are trained on household-related images from ImageNet. same way as existing image formats, and various lossless image compression methods can ... | goal reach, safety, localization error와 replanning latency | p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD) |

## Main Claims and Actual Contribution

- 물체와 공간적 이웃 관계를 그래프로 저장하고 노드의 의미 특징을 전송 전에 압축한 뒤 수신 측에서 복원한다. [PDF 3쪽](https://arxiv.org/pdf/2412.18381v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2412.18381v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2412.18381v2#page=5)
- 겹치는 장소를 찾아 로컬 그래프를 정렬하고 데이터 전송량, 지도 품질, 질의 성능을 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2412.18381v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2412.18381v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2412.18381v2#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Embodiment/environment | Map Merging Evaluation 1) Dataset: Since the Replica dataset lacks multi-room scenes suitable for collaborative mapping [22] (only apartment2 is available), we construct two additional simulation environments, Isaac Small and Isaac Larg ... | hardware/simulator version and reset protocol | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | It comprises 18 indoor environments, from which we select three representative scenes (room0, office2, and apartment2) due to their substantial size and rich semantic diversity. | role, split, size and leakage | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Metric | Compared to baseline methods, our approach not only maintains high accuracy and query success rates but also ensures realtime performance in the mapping system. | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Baseline/ablation | Compared to baseline methods, our approach not only maintains high accuracy and query success rates but also ensures realtime performance in the mapping system. | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** demonstrate that our feature compression process does not compromise the object finding rate and query success rate across the three evaluated scenes.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** 2) Metrics: Unlike multi-robot SLAM, our localization module relies on a ready-made SLAM algorithm, and the graph-structured map does not require high geometric precision.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Comparison of the original and decoded features when the encoder and decoder are trained on household-related images from ImageNet. same way as existing ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In this section, we 1) conduct experimental evaluations comparing our approach with state-of-the-art methods (Section IVA), 2) analyze the open-vocabulary capabilities and design insights of ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD)이다.
