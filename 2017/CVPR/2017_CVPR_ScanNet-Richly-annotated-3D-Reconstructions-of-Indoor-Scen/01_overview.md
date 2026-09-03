# ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1702.04405.
> PDF retrieval source: https://arxiv.org/pdf/1702.04405. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2017 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Dataset, semantic, 3D reconstruction
- Official paper: https://arxiv.org/abs/1702.04405
- Full-text retrieval: https://arxiv.org/pdf/1702.04405
- Code/Project: http://www.scan-net.org/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Typically, 3D deep learning methods use synthetic data to mitigate this lack of real-world data [91, 6].를 문제로 두고, In this paper, we introduce ScanNet, a dataset of richlyannotated RGB-D scans of real-world environments containing 2.5M RGB-D images in 1513 scans acquired in 707 distinct spaces.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A key requirement for leveraging supervised deep learning methods is the availability of large, labeled datasets.
- **p. 1 / Abstract - extractive body cue:** Unfortunately, in the context of RGB-D scene understanding, very little data is available - current datasets cover a small range of scene views and have ...
- **p. 1 / Abstract - extractive body cue:** To address this issue, we introduce ScanNet, an RGB-D video dataset containing 2.5M views in 1513 scenes annotated with 3D camera poses, surface reconstructions, and ...
- **p. 1 / Abstract - extractive body cue:** To collect this data, we designed an easy-to-use and scalable RGB-D capture system that includes automated surface reconstruction and crowdsourced semantic annotation.
- **p. 1 / Abstract - extractive body cue:** We show that using this data helps achieve state-of-the-art performance on several 3D scene understanding tasks, including 3D object classification, semantic voxel labeling, and CAD ...
- **p. 1 / 1. Introduction - extractive body cue:** Typically, 3D deep learning methods use synthetic data to mitigate this lack of real-world data [91, 6].
- **p. 1 / 1. Introduction - extractive body cue:** Thus, many of the current RGB-D datasets [74, 92, 77, 32] are orders of magnitude smaller than their 2D counterparts.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we introduce ScanNet, a dataset of richlyannotated RGB-D scans of real-world environments containing 2.5M RGB-D images in 1513 scans acquired in 707 ...
- **p. 1 / 1. Introduction - extractive body cue:** In the collection of this dataset, we have considered two main research questions: 1) how can we design a framework that allows many people to ...
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** This allows us to select the floor plane based on the scan bounding box and the normal most similar to the IMU up vector direction.
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** We chose the BundleFusion system [12] as it was designed and evaluated for similar sensor setups as ours, and provides real-time speed while being reasonably ...
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** BundleFusion produces accurate pose alignments which we then use to perform volumetric integration through VoxelHashing [62] and extract a high resolution surface mesh using the ...
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** There is a large variety of algorithms targeting this scenario [59, 88, 7, 62, 37, 89, 42, 9, 90, 38, 12].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For each input scan, we first run BundleFusion [12] at a voxel resolution of 1 cm3. | standardized observation, action, task state와 evaluation split | p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction) |
| State/latent | input, scan, first, BundleFusion, voxel, resolution, chose, system, designed, evaluated, similar, sensor | benchmark state/goal와 method decision | p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction), p. 1 (1. Introduction) |
| Output/action | We chose the BundleFusion system [12] as it was designed and evaluated for similar sensor setups as ours, and provides real-time speed while being reasonably robust given handheld RGBD video data. | policy/controller trajectory 또는 measured result | p. 4 (3.2. Surface Reconstruction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | This annotation is in progress at ≈35%, with gray regions indicating unannotated surfaces. | success metric, robustness, generalization과 reproducibility | p. 4 (3.2. Surface Reconstruction) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we introduce ScanNet, a dataset of richlyannotated RGB-D scans of real-world environments containing 2.5M RGB-D images in 1513 scans acquired in 707 ...
- **p. 1 / 1. Introduction - extractive body cue:** In the collection of this dataset, we have considered two main research questions: 1) how can we design a framework that allows many people to ...
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** This allows us to select the floor plane based on the scan bounding box and the normal most similar to the IMU up vector direction.
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** We chose the BundleFusion system [12] as it was designed and evaluated for similar sensor setups as ours, and provides real-time speed while being reasonably ...
- **p. 7 / 5.1. 3D Object Classification - extractive body cue:** On the other hand, training on ScanNet translates well to testing on SceneNN; as a result, the test results on SceneNN are significantly improved by ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 15. Comparison of calibration results. In the top row, we show results of calibration on a flat wall. As the distance increases the distortion ...
- **p. 2 / Dataset - extractive body cue:** We also provide CAD model placements for a subset of the scans. • A design for efficient 3D data capture and annotation suitable for novice ...
- **p. 3 / 3.1. RGB-D Scanning - extractive body cue:** We find that this calibration procedure is easy for users and results in improved data and consequently enhanced reconstruction quality.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (5.1. 3D Object Classification), p. 20 (Figure/Table caption) |
| Embodiment/environment | Our main goal driving the design of our framework was to allow untrained users to capture semantically labeled surfaces of indoor scenes with commodity hardware. | hardware/simulator version and reset protocol | p. 3 (3. Dataset Acquisition Framework), p. 5 (4. ScanNet Dataset) |
| Dataset/benchmark | We use these tasks to demonstrate that ScanNet enables the use of deep learning methods for 3D scene understanding tasks with supervised training, and compare performance to that using data from other ... | role, split, size and leakage | p. 3 (3. Dataset Acquisition Framework), p. 5 (4. ScanNet Dataset), p. 6 (5. Tasks and Benchmarks), p. 6 (5.1. 3D Object Classification) |
| Metric | Percentages indicate average instance accuracy of retrieved model to query region. | definition, denominator, direction and uncertainty | p. 7 (5.1. 3D Object Classification), p. 7 (5.1. 3D Object Classification), p. 8 (5.2. Semantic Voxel Labeling) |
| Baseline/ablation | Summary statistics for ScanNet compared to the most similar existing dataset (SceneNN [32]). | fair input/data/compute/action matching | p. 5 (3.3. Semantic Annotation), p. 6 (5.1. 3D Object Classification), p. 7 (5.2. Semantic Voxel Labeling) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Example reconstructed spaces in ScanNet annotated with instance-level object category labels through our crowdsourced annotation framework. ciently providing (dense) annotations in 3D is ...
- **p. 8 / 6. Conclusion - extractive body cue:** We demonstrated that the richlyannotated scan data collected so far in ScanNet is useful in achieving state-of-the-art performance on several 3D scene understanding tasks; we ...
- **p. 3 / 3.1. RGB-D Scanning - extractive body cue:** This feature was critical for providing intuition to users who are not familiar with the constraints and limitations of 3D reconstruction algorithms.
- **p. 5 / 3.3. Semantic Annotation - extractive body cue:** The main limitation of this interface is due to the mismatch between the corpus of available CAD models and the objects observed in the ScanNet ...
- **p. 5 / 3.3. Semantic Annotation - extractive body cue:** A promising way to alleviate this limitation is to algorithmically suggest candidate retrieved and aligned CAD models such that workers can perform an easier verification ...
- **p. 6 / 5.1. 3D Object Classification - extractive body cue:** When training data is synthetic and test is performed on real data, there is also a significant discrepancy of test performance, as data characteristics, such ...
- **p. 6 / 5.1. 3D Object Classification - extractive body cue:** Note that the number of instances does not include the rotation augmentation. ing, research has developed approaches to classify objects using only geometric data with ...

## Why Read It

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Typically, 3D deep learning methods use synthetic data to mitigate this lack of real-world data [91, 6].를 문제로 두고, In this paper, we introduce ScanNet, a dataset of richlyannotated RGB-D scans of real-world environments containing 2.5M RGB-D images in 1513 scans acquired in 707 distinct spaces.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction), p. 7 (5.1. 3D Object Classification), p. 20 (Figure/Table caption) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
