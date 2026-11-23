# RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: Chan Hee Song, Valts Blukis, Jonathan Tremblay, Stephen Tyree, Yu Su, Stan Birchfield
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: VLM, spatial reasoning, Robotics
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RoboSpatial은 실제 실내·탁상 장면의 3D 스캔과 2D 영상을 짝지어 로봇이 서로 다른 기준 좌표계에서 공간 관계를 학습하게 한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Spatial understanding is a crucial capability that enables robots to perceive their surroundings, reason about their environment, and interact with it meaningfully.
- **p. 1 / Abstract - extractive body cue:** In modern robotics, these capabilities are increasingly provided by vision-language models.
- **p. 1 / Abstract - extractive body cue:** However, these models face significant challenges in spatial reasoning tasks, as their training data are based on general-purpose image datasets that often lack sophisticated spatial ...
- **p. 1 / Abstract - extractive body cue:** For example, datasets frequently do not capture reference frame comprehension, yet effective spatial reasoning requires understanding whether to reason from ego-, world- , or object-centric ...
- **p. 1 / Abstract - extractive body cue:** To address this issue, we introduce ROBOSPATIAL, a large-scale dataset for spatial understanding in robotics.
- **p. 1–2 / 1. Introduction - 원문 대조 요지:** 장면에 보이는 것을 설명하는 능력만으로는 실제 상호작용에 필요한 공간 관계를 판단하기 어렵다.
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, a critical limitation of existing VLM training datasets is their inability to capture reference frame understanding (ref. frame) - the way we interpret spatial ...

## Core Idea

- **p. 4 / 3.2. Dataset Generation - extractive body cue:** The output is a spatial reasoning dataset D, where each entry di = hIi, qi, ai, lii consists of an image Ii, a question qi, ...
- **p. 1 / 1. Introduction - extractive body cue:** This illustration demonstrates how a model trained on ROBOSPATIAL enables human-aligned spatial reasoning within the correct reference frame, supporting task grounding, planning, and detection for ...
- **p. 4 / 3.1. Spatial Relationships - extractive body cue:** Configuration enables robots to understand and interpret the relative positioning of objects, which is crucial for directing navigation, manipulation, and interaction within complex environments.
- **p. 5 / 3.2. Dataset Generation - extractive body cue:** The simulation allows for translation and in-plane rotation of the object.
- **p. 5 / 3.2.3. Question-Answer Generation - extractive body cue:** To ensure that models learn from visual grounding rather than linguistic priors, we use deterministic templates that avoid ambiguity and minimize reliance on commonsense.
- **p. 4 / 3.2. Dataset Generation - extractive body cue:** Stage 1: 3D Spatial Relation Extraction The first stage involves extracting spatial relationships between objects or between objects and free space, based on 3D geometry.
- **p. 5 / 3.2.3. Question-Answer Generation - extractive body cue:** This supervision helps models more accurately resolve references during spatial reasoning and is included during training.
- **p. 6 / Model - extractive body cue:** As a result, reported scores represent a conservative estimate of each model's spatial understanding.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The pipeline takes as input a scene dataset Ds that contains RGB images, camera poses (both extrinsic and intrinsic parameters), and oriented 3D bounding box annotations with semantic object labels. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.2. Dataset Generation), p. 4 (3.2. Dataset Generation) |
| State/latent | pipeline, takes, input, scene, dataset, contains, RGB, images, camera, poses, extrinsic, intrinsic | geometry, map, object/relationship state | p. 4 (3.2. Dataset Generation), p. 4 (3.2. Dataset Generation), p. 1 (1. Introduction) |
| Output/action | The output is a spatial reasoning dataset D, where each entry di = hIi, qi, ai, lii consists of an image Ii, a question qi, an answer ai, and a reference frame ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.2. Dataset Generation), p. 1 (1. Introduction), p. 5 (3.2.3. Question-Answer Generation) |
| Objective/outcome | For each spatial configuration task, we evaluate all visible object pairs that appear uniquely in the image, avoiding duplicate instances to minimize ambiguity. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.2. Dataset Generation), p. 5 (3.2. Dataset Generation), p. 5 (3.2.3. Question-Answer Generation) |

## Main Claims and Actual Contribution

- 카메라·세계·물체 기준의 위치 관계를 구분해 같은 장면에서 공간 질의와 정답을 생성했다. [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.pdf#page=5)
- 공간 관계·물체 배치 가능성 예측을 비교하고, 실제 로봇에서 공간 지시에 맞춰 물체를 놓는 과제를 평가했다. [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 2 (Dataset), p. 8 (4.3. Real Robot Experiments) |
| Embodiment/environment | We make the data and code for generating the dataset from 3D annotated scenes publicly available1. • VLMs trained on ROBOSPATIAL demonstrate superior spatial reasoning, outperforming SOTA baselines on language-guided robot manipulation ... | hardware/simulator version and reset protocol | p. 3 (Dataset), p. 2 (Dataset) |
| Dataset/benchmark | These benchmarks rigorously test spatial reasoning skills in practical robotic tasks, including object rearrangement and contextual question answering in indoor environments, while also examining the models' capacity to generalize to no ... | role, split, size and leakage | p. 3 (Dataset), p. 2 (Dataset), p. 2 (Dataset), p. 5 (4.1. Setup) |
| Metric | Experiments show that LLaVA-NeXT fine-tuned on ROBOSPATIAL achieves the highest success rate across all models. | definition, denominator, direction and uncertainty | p. 8 (4.3. Real Robot Experiments), p. 5 (4.1.2. Spatial Understanding Evaluation), p. 8 (4.3. Real Robot Experiments) |
| Baseline/ablation | We evaluate the following VLMs: LLaVA-NeXT [35] and RoboPoint [62], both with and without ROBOSPATIAL training; and two strong baselines, Molmo [9] and GPT-4o [42]. | fair input/data/compute/action matching | p. 8 (4.3. Real Robot Experiments), p. 3 (Dataset), p. 2 (Dataset) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 4.1. Setup - extractive body cue:** To mitigate failure cases arising from poor object grounding, we also include an auxiliary grounding dataset during training, which provides additional supervision for object reference ...
- **p. 8 / 4.3. Real Robot Experiments - extractive body cue:** We also observe that spatial failures in 2D VLMs often stem from errors in projecting 2D predictions into 3D.
- **p. 8 / 4.3. Real Robot Experiments - extractive body cue:** Nonetheless, models trained on ROBOSPATIAL produce more accurate predictions, reducing these failure cases and showing the benefit of dataset-driven improvements.
- **p. 2 / Dataset - extractive body cue:** Several recent efforts aim to address this by explicitly training VLMs on spatial reasoning tasks, yet many fall short of the demands posed by embodied ...
- **p. 5 / 4.1.2. Spatial Understanding Evaluation - extractive body cue:** Questions fall into two categories: binary yes/no questions and coordinate prediction tasks.
- **p. 4 / 3.2. Dataset Generation - extractive body cue:** Although the method does not require point clouds or meshes, it relies on camera intrinsics and extrinsics to project between 2D and 3D and to ...
- **p. 2 / Dataset - extractive body cue:** This results, for example, in failing to predict whether the gray bowl can fit in front of the car in Figure 1.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 5 (3.2.3. Question-Answer Generation), p. 4 (3.2. Dataset Generation), p. 4 (3.1. Spatial Relationships)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** 장면에 보이는 것을 설명하는 능력만으로는 실제 상호작용에 필요한 공간 관계를 판단하기 어렵다. (PDF 1–2쪽).
- **Actual contribution:** This illustration demonstrates how a model trained on ROBOSPATIAL enables human-aligned spatial reasoning within the correct reference frame, supporting task grounding, planning, and detection for manipulation tasks. (p. 1, 1. Introduction).
- **Evaluation boundary:** Results demonstrate that models trained on ROBOSPATIAL exhibit significantly improved spatial reasoning capabilities, consistently outperforming baseline methods on the evaluation benchmark ROBOSPATIAL-Val, a held-out validation subset ... (p. 2, Dataset).
- **Explicit failure boundary:** To mitigate failure cases arising from poor object grounding, we also include an auxiliary grounding dataset during training, which provides additional supervision for object reference resolution. (p. 5, 4.1. Setup).
