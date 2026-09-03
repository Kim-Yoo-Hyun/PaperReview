# nuScenes: A Multimodal Dataset for Autonomous Driving

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1903.11027.
> PDF retrieval source: https://arxiv.org/pdf/1903.11027. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, LiDAR, sensor fusion, Dataset
- Official paper: https://arxiv.org/abs/1903.11027
- Full-text retrieval: https://arxiv.org/pdf/1903.11027
- Code/Project: https://www.nuscenes.org/nuscenes
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 From the complexities of the multimodal 3D detection challenge, and the limitations of current AV datasets, a large-scale multimodal dataset with 360◦coverage across all vision and range sensors collected from diverse situations ...를 문제로 두고, Our second contribution is new detection and tracking metrics aimed at the AV application.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robust detection and tracking of objects is crucial for the deployment of autonomous vehicle technology.
- **p. 1 / Abstract - extractive body cue:** Image based benchmark datasets have driven development in computer vision tasks such as object detection, tracking and segmentation of agents in the environment.
- **p. 1 / Abstract - extractive body cue:** Most autonomous vehicles, however, carry a combination of cameras and range sensors such as lidar and radar.
- **p. 1 / Abstract - extractive body cue:** As machine learning based methods for detection and tracking become more prevalent, there is a need to train and evaluate such methods on datasets containing ...
- **p. 1 / Abstract - extractive body cue:** In this work we present nuTonomy scenes (nuScenes), the first dataset to carry the full autonomous vehicle sensor suite: 6 cameras, 5 radars and 1 ...
- **p. 2 / 1.1. Contributions - extractive body cue:** From the complexities of the multimodal 3D detection challenge, and the limitations of current AV datasets, a large-scale multimodal dataset with 360◦coverage across all vision ...
- **p. 1 / 1. Introduction - extractive body cue:** Since the three sensor types have different failure modes during difficult conditions, the joint treatment of sensor data is essential for agent detection and tracking.

## Core Idea

- **p. 2 / 1.1. Contributions - extractive body cue:** Our second contribution is new detection and tracking metrics aimed at the AV application.
- **p. 2 / 1.1. Contributions - extractive body cue:** It enables research on multiple tasks such as object detection, tracking and behavior modeling in a range of conditions.
- **p. 1 / Abstract - extractive body cue:** In this work we present nuTonomy scenes (nuScenes), the first dataset to carry the full autonomous vehicle sensor suite: 6 cameras, 5 radars and 1 ...
- **p. 1 / 1. Introduction - extractive body cue:** At the bottom we show the human written scene description.
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore the reflectance of lidar is an important feature [40, 51].
- **p. 1 / 1. Introduction - extractive body cue:** Such algorithms rely increasingly on machine learning, which drives the need for benchmark datasets.
- **p. 2 / 1. Introduction - extractive body cue:** Still, to the best of our knowledge, no other 3D dataset provides attribute annotations, such as pedestrian pose or vehicle state.
- **p. 3 / 1.2. Related datasets - extractive body cue:** It provides 200k 3D boxes over 22 scenes which helped advance the state-of-the-art in 3D object detection.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Still, to the best of our knowledge, no other 3D dataset provides attribute annotations, such as pedestrian pose or vehicle state. | standardized observation, action, task state와 evaluation split | p. 2 (1. Introduction), p. 2 (1.1. Contributions) |
| State/latent | Still, best, knowledge, other, dataset, provides, attribute, annotations, pedestrian, pose, vehicle, state | benchmark state/goal와 method decision | p. 2 (1. Introduction), p. 2 (1.1. Contributions), p. 3 (1.2. Related datasets) |
| Output/action | Third, we publish the devkit, evaluation code, taxonomy, annotator instructions, and database schema for industrywide standardization. | policy/controller trajectory 또는 measured result | p. 2 (1.1. Contributions), p. 3 (1.2. Related datasets), p. 1 (1. Introduction) |
| Objective/outcome | Operating points where recall or precision is less than 10% are removed in order to minimize the impact of noise commonly seen in low precision and recall regions. | success metric, robustness, generalization과 reproducibility | p. 5 (3.1. Detection), p. 1 (1. Introduction), p. 4 (2. The nuScenes dataset) |

## Main Claims and Actual Contribution

- **p. 2 / 1.1. Contributions - extractive body cue:** Our second contribution is new detection and tracking metrics aimed at the AV application.
- **p. 2 / 1.1. Contributions - extractive body cue:** It enables research on multiple tasks such as object detection, tracking and behavior modeling in a range of conditions.
- **p. 1 / Abstract - extractive body cue:** In this work we present nuTonomy scenes (nuScenes), the first dataset to carry the full autonomous vehicle sensor suite: 6 cameras, 5 radars and 1 ...
- **p. 1 / 1. Introduction - extractive body cue:** At the bottom we show the human written scene description.
- **p. 7 / 4.1. Baselines - extractive body cue:** submissions, MonoDIS [70] was the best, significantly outperforming our image baseline and even some lidar based methods.
- **p. 7 / 4.2. Analysis - extractive body cue:** Multiple lidar sweeps improve performance.
- **p. 8 / 4.2. Analysis - extractive body cue:** An important question for AVs is which sensors are required to achieve the best detection performance.
- **p. 8 / 4.2. Analysis - extractive body cue:** Weng and Kitani [77] presented a simple baseline that achieved stateof-the-art 3d tracking results using powerful detections on KITTI.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (4.1. Baselines), p. 7 (4.2. Analysis) |
| Embodiment/environment | In this section we present object detection and tracking experiments on the nuScenes dataset, analyze their characteristics and suggest avenues for future research. | hardware/simulator version and reset protocol | p. 6 (4. Experiments), p. 3 (1.2. Related datasets) |
| Dataset/benchmark | (‡) The current Waymo Open dataset size is comparable to nuScenes, but at a 5x higher annotation frequency. | role, split, size and leakage | p. 6 (4. Experiments), p. 3 (1.2. Related datasets), p. 3 (Dataset), p. 5 (2. The nuScenes dataset) |
| Metric | Table 7. Detailed detection performance for PointPillars [51] (top) and MonoDIS [70] (bottom) on the test set. AP: average precision averaged over distance thresholds (%), ATE: average translation error (m), ASE: average ... | definition, denominator, direction and uncertainty | p. 15 (Figure/Table caption), p. 8 (4.2. Analysis), p. 7 (4.2. Analysis) |
| Baseline/ablation | submissions, MonoDIS [70] was the best, significantly outperforming our image baseline and even some lidar based methods. | fair input/data/compute/action matching | p. 7 (4.1. Baselines), p. 6 (4.1. Baselines), p. 7 (4.1. Baselines) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Future work will add image-level and pointlevel semantic labels and a benchmark for trajectory prediction [63].
- **p. 3 / 2. The nuScenes dataset - extractive body cue:** From a large body of training data we manually select 84 logs with 15h of driving data (242km travelled at an av4In preliminary analysis we ...
- **p. 4 / 2. The nuScenes dataset - extractive body cue:** This method is very robust and we achieve localization errors of ≤10cm.
- **p. 7 / 4.2. Analysis - extractive body cue:** As expected, when using IOU matching, small objects like pedestrians and bicycles fail to achieve above 0 AP, making ordering impossible (Figure 7).

## Why Read It

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 From the complexities of the multimodal 3D detection challenge, and the limitations of current AV datasets, a large-scale multimodal dataset with 360◦coverage across all vision and range sensors collected from diverse situations ...를 문제로 두고, Our second contribution is new detection and tracking metrics aimed at the AV application.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1.1. Contributions), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1.1. Contributions), p. 1 (1. Introduction), p. 1 (1. Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
