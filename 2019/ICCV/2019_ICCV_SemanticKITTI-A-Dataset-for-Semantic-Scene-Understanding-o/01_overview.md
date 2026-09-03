# SemanticKITTI: A Dataset for Semantic Scene Understanding of LiDAR Sequences

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1904.01416.
> PDF retrieval source: https://arxiv.org/pdf/1904.01416. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, LiDAR, semantic, Dataset
- Official paper: https://arxiv.org/abs/1904.01416
- Full-text retrieval: https://arxiv.org/pdf/1904.01416
- Code/Project: http://semantic-kitti.org/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Complementary sensor modalities enable to cope with deficits or failures of particular sensors.를 문제로 두고, In summary, our main contributions are: • We present a point-wise annotated dataset of point cloud sequences with an unprecedented number of classes and unseen level-of-detail for each scan. • We furthermore ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Semantic scene understanding is important for various applications.
- **p. 1 / Abstract - extractive body cue:** In particular, self-driving cars need a finegrained understanding of the surfaces and objects in their vicinity.
- **p. 1 / Abstract - extractive body cue:** Light detection and ranging (LiDAR) provides precise geometric information about the environment and is thus a part of the sensor suites of almost all self-driving ...
- **p. 1 / Abstract - extractive body cue:** Despite the relevance of semantic scene understanding for this application, there is a lack of a large dataset for this task which is based on ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce a large dataset to propel research on laser-based semantic segmentation.
- **p. 1 / 1. Introduction - extractive body cue:** Complementary sensor modalities enable to cope with deficits or failures of particular sensors.
- **p. 2 / 1. Introduction - extractive body cue:** To close this gap we propose SemanticKITTI, a large dataset showing unprecedented detail in point-wise annotation with 28 classes, which is suited for various tasks.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are: • We present a point-wise annotated dataset of point cloud sequences with an unprecedented number of classes and unseen ...
- **p. 2 / 1. Introduction - extractive body cue:** To close this gap we propose SemanticKITTI, a large dataset showing unprecedented detail in point-wise annotation with 28 classes, which is suited for various tasks.
- **p. 1 / 1. Introduction - extractive body cue:** They mainly fulfill three purposes: (i) they provide a basis to measure progress, since they allow to provide results that are reproducible and comparable, (ii) ...
- **p. 7 / Approach - extractive body cue:** We expect that new approaches could explicitly exploit the sequential information by using multiple input streams to the architecture or even recurrent neural networks to ...
- **p. 6 / Approach - extractive body cue:** Approach num. parameters train time inference time (million)  GPU hours epoch   seconds point cloud  PointNet 3 4 0.5 PointNet++ 6 16 ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In summary, our main contributions are: • We present a point-wise annotated dataset of point cloud sequences with an unprecedented number of classes and unseen level-of-detail for each scan. • We furthermore ... | standardized observation, action, task state와 evaluation split | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | summary, main, contributions, present, point-wise, annotated, dataset, point, cloud, sequences, unprecedented, number | benchmark state/goal와 method decision | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 7 (Approach) |
| Output/action | They mainly fulfill three purposes: (i) they provide a basis to measure progress, since they allow to provide results that are reproducible and comparable, (ii) they uncover shortcomings of the current state ... | policy/controller trajectory 또는 measured result | p. 1 (1. Introduction), p. 7 (Approach), p. 6 (Approach) |
| Objective/outcome | success metric, robustness, generalization과 reproducibility | success metric, robustness, generalization과 reproducibility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are: • We present a point-wise annotated dataset of point cloud sequences with an unprecedented number of classes and unseen ...
- **p. 2 / 1. Introduction - extractive body cue:** To close this gap we propose SemanticKITTI, a large dataset showing unprecedented detail in point-wise annotation with 28 classes, which is suited for various tasks.
- **p. 1 / 1. Introduction - extractive body cue:** They mainly fulfill three purposes: (i) they provide a basis to measure progress, since they allow to provide results that are reproducible and comparable, (ii) ...
- **p. 6 / 4.2. Multiple Scan Experiments - extractive body cue:** In this task, we allow methods to exploit information from a sequence of multiple past scans to improve the segmentation of the current scan.
- **p. 8 / 5. Evaluation of Semantic Scene Completion - extractive body cue:** This has minimal impact on the performance, but significantly speeds up the training time due to faster preprocessing [18].
- **p. 8 / 5. Evaluation of Semantic Scene Completion - extractive body cue:** However, the usage of the best semantic segmentation directly working on the point cloud slightly outperforms SSCNet on semantic scene completion (TS3D + DarkNet53Seg).
- **p. 4 / 3.1. Labeling Process - extractive body cue:** We provided regular feedback to the annotators to improve the quality and accuracy of labels.
- **p. 4 / 4.1. Single Scan Experiments - extractive body cue:** To assess the labeling performance, we rely on the commonly applied mean Jaccard Index or mean intersectionover-union (mIoU) metric [15] over all classes, given by ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 6 (4.2. Multiple Scan Experiments), p. 8 (5. Evaluation of Semantic Scene Completion) |
| Embodiment/environment | The dataset is publicly available through a benchmark website and we provide only the training set with ground truth labels and perform the test set evaluation online. | hardware/simulator version and reset protocol | p. 3 (3. The SemanticKITTI Dataset), p. 3 (3. The SemanticKITTI Dataset) |
| Dataset/benchmark | However, a dataset combining the scale of a synthetic dataset and usage of real-world data is still missing. | role, split, size and leakage | p. 3 (3. The SemanticKITTI Dataset), p. 3 (3. The SemanticKITTI Dataset), p. 7 (5. Evaluation of Semantic Scene Completion), p. 7 (5. Evaluation of Semantic Scene Completion) |
| Metric | [49] and compute the IoU for the task of scene completion, which only classifies a voxel as being occupied or empty, i.e., ignoring the semantic label, as well as mIoU (1) for ... | definition, denominator, direction and uncertainty | p. 7 (5. Evaluation of Semantic Scene Completion), p. 8 (5. Evaluation of Semantic Scene Completion), p. 6 (Figure/Table caption) |
| Baseline/ablation | However, the usage of the best semantic segmentation directly working on the point cloud slightly outperforms SSCNet on semantic scene completion (TS3D + DarkNet53Seg). | fair input/data/compute/action matching | p. 8 (5. Evaluation of Semantic Scene Completion), p. 8 (5. Evaluation of Semantic Scene Completion), p. 4 (3.1. Labeling Process) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion and Outlook - extractive body cue:** In future work, we plan to provide also instance-level annotation over the whole sequence, i.e., we want to distinguish different objects in a scan, but ...
- **p. 7 / 5. Evaluation of Semantic Scene Completion - extractive body cue:** Existing point cloud datasets cannot be used to address this task, as they do not allow for aggregating labeled point clouds that are sufficiently dense ...
- **p. 8 / 5. Evaluation of Semantic Scene Completion - extractive body cue:** Due to Completion Semantic Scene (IoU) Completion (mIoU) SSCNet [49] 29.83 9.53 TS3D [18] 29.81 9.54 TS3D [18] + DarkNet53Seg 24.99 10.19 TS3D [18] + ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 7: Qualitative results for the semantic scene completion approach TS3D + DarkNet53Seg + SATNet. Left: Input volume. Middle: Network prediction. Right: Ground truth. Due ...
- **p. 7 / 5. Evaluation of Semantic Scene Completion - extractive body cue:** In the case of our proposed dataset, the car carrying the LiDAR moves past 3D objects in the scene and thereby records their backsides, which ...

## Why Read It

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Complementary sensor modalities enable to cope with deficits or failures of particular sensors.를 문제로 두고, In summary, our main contributions are: • We present a point-wise annotated dataset of point cloud sequences with an unprecedented number of classes and unseen level-of-detail for each scan. • We furthermore ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 7 (Approach), p. 6 (Approach), p. 6 (4.2. Multiple Scan Experiments) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
