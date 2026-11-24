# Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2606.24767.
> PDF retrieval source: https://arxiv.org/pdf/2606.24767. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / RA-L
- Authors: Zhaopeng Cui, Jiarui Hu, Jingbo Liu, Boming Zhao, Xiyue Guo, Boyin Feng, Haocheng Peng, Yujun Shen, Hujun Bao, Guofeng Zhang
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic
- Official paper: https://arxiv.org/abs/2606.24767
- Full-text retrieval: https://arxiv.org/pdf/2606.24767
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11578335)

## Why This Paper Is Here

OpenReLoc은 장면의 물체를 중심으로 표현한 열린 어휘 지도에 질의 관측을 대응시켜 카메라의 3D 자세를 복구한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11578335#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11578335#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Indoor visual relocalization plays a critical role in emerging spatial and embodied AI applications.
- **p. 1 / Abstract - extractive body cue:** However, prior research was predominantly devoted to low-level vision schemes, struggling to perceive scene semantics and compositions, which limits both interpretability and applicability.
- **p. 1 / Abstract - extractive body cue:** In this paper, we explore the issue of how to organize rich object information in a scene, including semantics, layout, and geometry, into a structured ...
- **p. 1 / Abstract - extractive body cue:** To this end, we propose OpenReLoc, a camera relocalization system designed to provide scene understanding and accurate pose estimation capabilities.
- **p. 1 / Abstract - extractive body cue:** Leveraging recent foundation models, we first introduce a multi-modal mechanism to integrate open-vocabulary semantic knowledge for effective 2D-3D object matching.
- **p. 1 / I. INTRODUCTION - extractive body cue:** A dedicated pose optimization strategy tailored to the object-level paradigm is still lacking.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Previous visual relocalization methods [1]-[4] mainly rely on low-level visual features, and thus suffer from limitations in robustness, compactness, and semantic awareness.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Overall, our contributions can be summarized as follows: • We introduce a multi-modal landmark association module that combines open-vocabulary object descriptors with a global scene ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We construct an objectoriented map suite that consists of a global scene graph, openvocabulary object descriptors, object geometry, and reference frames.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In response to these challenges, we propose OpenReLoc, a semantic-aware, memory-efficient, and scalable camera relocalization framework based on object-level representations with open-vocabulary understanding.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Third, to improve object-level pose optimization accuracy, we propose a dual-path 2D ICP (Iterative Closest Pixel) loss to align observed and actually projected pixel areas ...
- **p. 3 / III. METHOD - extractive body cue:** In this section, we introduce an object-oriented mapping workflow and the principles behind each module.
- **p. 5 / III. METHOD - extractive body cue:** To ensure more robust and accurate pose estimation, we use a Huber kernel H with a threshold δ on the 2D ICP loss to suppress ...
- **p. 3 / III. METHOD - extractive body cue:** Object-oriented Mapping (Sec III-A): Given a set of posed RGBD images from a scene, this step is to process these RGBD observations and build an ...
- **p. 4 / III. METHOD - extractive body cue:** Recent progress suggested that the advanced CLIP model can work as an effective object descriptor encoder [7].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Object-oriented Mapping (Sec III-A): Given a set of posed RGBD images from a scene, this step is to process these RGBD observations and build an object-centric 3D map suite, including 3D instance ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | Object-oriented, Mapping, Sec, III-A, Given, posed, RGBD, images, scene, step, process, observations | geometry, map, object/relationship state | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Output/action | Based on depth observations, we can reconstruct the scene mesh by TSDF-Fusion [20] and convert vertices into the scene point cloud P. | point map, pose, scene graph, affordance 또는 query result | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective/outcome | Benefiting from this loss, we can achieve stable pose optimization. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) |

## Main Claims and Actual Contribution

- 물체 간 기하 배치를 고려해 대응 후보를 만들고 서로 다른 두 정합 경로를 사용해 자세 후보를 정제한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11578335#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11578335#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11578335#page=5)
- 여러 장면에서 위치·회전 오차 허용 범위에 든 질의의 비율을 비교하고 물체 대응과 자세 정제의 영향을 평가했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11578335#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11578335#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11578335#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption) |
| Embodiment/environment | Experiments on these two datasets illustrate the capability of our system in handling complex real-world scenes, boosting the practicality of object-level camera relocalization. | hardware/simulator version and reset protocol | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | This table shows average metrics over multi-room/floor scenes of the Synthetic dataset. | role, split, size and leakage | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Metric | As such, it does not demand strict realtime performance but places greater emphasis on success rate and accuracy. | definition, denominator, direction and uncertainty | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Baseline/ablation | Therefore, our main comparison is to GoReloc [6], an open-source and SOTA object-level baseline, which shares the most relevant problem formulation with ours. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Open-vocabulary Object Matching. Open-vocabulary object-level mapping allows us to recognize diverse objects. methods achieve comparable efficiency. The relocalization module typically serves as an ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Such a distribution falls beyond the scope of closed-vocabulary methods, leading to their failure.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** IV show that ORB-SLAM2 experienced failure, succeeding on very few frames, despite achieving better accuracy.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** As a result, GoReloc fails to identify valid matching objects in many observations.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: OpenReLoc, an open-vocabulary visual relocalization system, can achieve robust and accurate relocalization performance on various indoor scenes, based on an object-level map. As ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 5 (III. METHOD)이다.
