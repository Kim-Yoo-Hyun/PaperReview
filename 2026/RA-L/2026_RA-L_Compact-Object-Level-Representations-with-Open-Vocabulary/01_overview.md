# Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2606.24767.
> PDF retrieval source: https://arxiv.org/pdf/2606.24767. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic
- Official paper: https://arxiv.org/abs/2606.24767
- Full-text retrieval: https://arxiv.org/pdf/2606.24767
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 A dedicated pose optimization strategy tailored to the object-level paradigm is still lacking.를 문제로 두고, Overall, our contributions can be summarized as follows: • We introduce a multi-modal landmark association module that combines open-vocabulary object descriptors with a global scene graph, enabling robust class-agnostic object matching ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / I. INTRODUCTION - extractive body cue:** Overall, our contributions can be summarized as follows: • We introduce a multi-modal landmark association module that combines open-vocabulary object descriptors with a global scene ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We construct an objectoriented map suite that consists of a global scene graph, openvocabulary object descriptors, object geometry, and reference frames.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In response to these challenges, we propose OpenReLoc, a semantic-aware, memory-efficient, and scalable camera relocalization framework based on object-level representations with open-vocabulary understanding.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Third, to improve object-level pose optimization accuracy, we propose a dual-path 2D ICP (Iterative Closest Pixel) loss to align observed and actually projected pixel areas ...
- **p. 3 / III. METHOD - extractive body cue:** In this section, we introduce an object-oriented mapping workflow and the principles behind each module.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** V, it can be seen that our method can still outperform GoReloc in both success rate and accuracy.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Open-vocabulary Object Matching. Open-vocabulary object-level mapping allows us to recognize diverse objects. methods achieve comparable efficiency. The relocalization module typically serves as an ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In this section, we describe our experimental setup and validate that our system can achieve significant improvements in relocalization performance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 A dedicated pose optimization strategy tailored to the object-level paradigm is still lacking.를 문제로 두고, Overall, our contributions can be summarized as follows: • We introduce a multi-modal landmark association module that combines open-vocabulary object descriptors with a global scene graph, enabling robust class-agnostic object matching ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 5 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
