# ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1912.08830.
> PDF retrieval source: https://arxiv.org/pdf/1912.08830. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D visual grounding, RGB-D, semantic
- Official paper: https://arxiv.org/abs/1912.08830
- Full-text retrieval: https://arxiv.org/pdf/1912.08830
- Code/Project: https://daveredrum.github.io/ScanRefer/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these methods and datasets are restricted to 2D images, where object localization fails to capture the true 3D extent of an object (see Fig.를 문제로 두고, Our architecture consists of two main modules: 1) detection & encoding; 2) fusion & localization (Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 6 / 5 Method - extractive body cue:** Our architecture consists of two main modules: 1) detection & encoding; 2) fusion & localization (Fig.
- **p. 7 / 5 Method - extractive body cue:** 5.2 Network Architecture Our method takes as input the preprocessed point cloud P′ and the word embedding sequence W representing the input description and outputs ...
- **p. 8 / 5 Method - extractive body cue:** Conceptually, our localization pipeline consists of the following four stages: detection, encoding, fusion and localization.
- **p. 8 / 5 Method - extractive body cue:** Next, the proposal module takes in the point clusters and processes those clusters to predict the objectness mask Dobjn ∈RM×1 and the axis-aligned bounding boxes ...
- **p. 2 / 1 Introduction - extractive body cue:** Flickr30K Entities [47] have enabled the development of various methods for visual grounding in 2D [23, 22, 39].
- **p. 14 / 6 Experiments - extractive body cue:** The additional 3D information improves performance.
- **p. 14 / 6 Experiments - extractive body cue:** Our architecture trained with geometry, multi-view features, and normals (xyz+multiview+ normals+lobjcls) achieves the best performance among all ablations.
- **p. 11 / Figure/Table caption - extractive body cue:** Table 4: Comparison of localization results obtained by our ScanRefer and base- line models. We measure percentage of predictions whose IoU with the ground truth ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 14 (6 Experiments), p. 14 (6 Experiments) |
| Embodiment/environment | 4: Description lengths Number of descriptions 51,583 Number of scenes 800 Number of objects 11,046 Number of objects per scene 13.81 Number of descriptions per scene 64.48 Number of descriptions per object ... | hardware/simulator version and reset protocol | p. 5 (4 Dataset), p. 9 (6 Experiments) |
| Dataset/benchmark | 4.2 Dataset Statistics We collected 51,583 descriptions for 800 ScanNet scenes2. | role, split, size and leakage | p. 5 (4 Dataset), p. 9 (6 Experiments), p. 6 (4 Dataset), p. 4 (3 dataset) |
| Metric | To evaluate the performance of our method, we measure the thresholded accuracy where the positive predictions have higher intersection over union (IoU) with the ground truths than the thresholds. | definition, denominator, direction and uncertainty | p. 10 (6 Experiments), p. 12 (Figure/Table caption), p. 10 (6 Experiments) |
| Baseline/ablation | We outperform all baselines by a significant margin. | fair input/data/compute/action matching | p. 11 (6 Experiments), p. 11 (6 Experiments), p. 12 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 13 / 6 Experiments - extractive body cue:** In contrast, even provided with a pool of ground truth proposals, OracleRefer sometimes still fails to predict correct bounding boxes, while One-stage is limited by ...
- **p. 12 / 6 Experiments - extractive body cue:** We show examples where our method produced good predictions (blue block) as well as failure cases (orange block).
- **p. 13 / 6 Experiments - extractive body cue:** Some failure cases of our method are displayed in the orange block in Fig.
- **p. 33 / Figure/Table caption - extractive body cue:** Fig. 17: Additional qualitative analysis in the "unique" scenarios where there is only one object from a certain category. Our method is capable of localizing ...
- **p. 34 / Figure/Table caption - extractive body cue:** Fig. 18: Additional qualitative analysis for the "multiple" subset where there are multiple objects with the same category as the target objects. While our methods ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We introduce the task of object localization in 3D scenes using natural language. Given as input a 3D scene and a natural language ...
- **p. 28 / B.1 Fusion Module - extractive body cue:** As expected, models with the language-based object classifier (rows [g-k]) does not results in better object detection compared to models without such a module (rows ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these methods and datasets are restricted to 2D images, where object localization fails to capture the true 3D extent of an object (see Fig.를 문제로 두고, Our architecture consists of two main modules: 1) detection & encoding; 2) fusion & localization (Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 7 (5 Method), p. 7 (5 Method), p. 9 (5 Method), p. 6 (5 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
