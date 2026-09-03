# Waymo Open Dataset: An Autonomous Driving Dataset

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1912.04838.
> PDF retrieval source: https://arxiv.org/pdf/1912.04838. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, LiDAR, sensor fusion, Dataset
- Official paper: https://arxiv.org/abs/1912.04838
- Full-text retrieval: https://arxiv.org/pdf/1912.04838
- Code/Project: https://waymo.com/open/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 We demonstrate that the differences in these geographies lead to a pronounced domain gap, enabling exciting research opportunities in the field of domain adaptation.를 문제로 두고, In an effort to help align the research community's contributions with real-world selfdriving problems, we introduce a new large-scale, high quality, diverse dataset.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The research community has increasing interest in autonomous driving research, despite the resource intensity of obtaining representative real world data.
- **p. 1 / Abstract - extractive body cue:** Existing selfdriving datasets are limited in the scale and variation of the environments they capture, even though generalization within and between operating regions is crucial ...
- **p. 1 / Abstract - extractive body cue:** In an effort to help align the research community's contributions with real-world selfdriving problems, we introduce a new large-scale, high quality, diverse dataset.
- **p. 1 / Abstract - extractive body cue:** Our new dataset consists of 1150 scenes that each span 20 seconds, consisting of well synchronized and calibrated high quality LiDAR and camera data captured ...
- **p. 1 / Abstract - extractive body cue:** It is 15x more diverse than the largest camera+LiDAR dataset available based on our proposed geographical coverage metric.
- **p. 1 / 1. Introduction - extractive body cue:** We demonstrate that the differences in these geographies lead to a pronounced domain gap, enabling exciting research opportunities in the field of domain adaptation.
- **p. 2 / 1. Introduction - extractive body cue:** Our dataset currently consists of 1000 scenes for training and validation, and 150 scenes for testing, where each scene spans 20 s.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** In an effort to help align the research community's contributions with real-world selfdriving problems, we introduce a new large-scale, high quality, diverse dataset.
- **p. 1 / 1. Introduction - extractive body cue:** To further accelerate the development of autonomous driving technology, we present the largest and most diverse multimodal autonomous driving dataset to date, comprising of images ...
- **p. 2 / 1. Introduction - extractive body cue:** We present benchmark results of several state-of-the-art 2D-and 3D object detection and tracking methods on the dataset.
- **p. 2 / 1. Introduction - extractive body cue:** Our dataset currently consists of 1000 scenes for training and validation, and 150 scenes for testing, where each scene spans 20 s.
- **p. 2 / 1. Introduction - extractive body cue:** This is the first dataset with such low-level, synchronized information available, making it easier to conduct research on LiDAR input representations other than the popular ...
- **p. 5 / 3.4. Sensor Data - extractive body cue:** See Figure 5 for an example output of the projection algorithm.
- **p. 5 / 3.4. Sensor Data - extractive body cue:** The algorithm is efficient and can be used in real time as it usually converges in 2 or 3 iterations.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Detection methods may use data from any of the LiDAR and camera sensors; they may also choose to leverage sensor inputs from preceding frames. | standardized observation, action, task state와 evaluation split | p. 5 (4.1. Object Detection), p. 2 (1. Introduction) |
| State/latent | Detection, methods, data, LiDAR, camera, sensors, they, choose, leverage, sensor, inputs, preceding | benchmark state/goal와 method decision | p. 5 (4.1. Object Detection), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | In addition to sensor features such as elongation, we provide each range image pixel with an accurate vehicle pose. | policy/controller trajectory 또는 measured result | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Sensor Data) |
| Objective/outcome | We minimize the difference between t and ˜t by solving a single variable (t) convex quadratic optimization. | success metric, robustness, generalization과 reproducibility | p. 5 (3.4. Sensor Data), p. 3 (3.2. Coordinate Systems), p. 5 (4.1. Object Detection) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** In an effort to help align the research community's contributions with real-world selfdriving problems, we introduce a new large-scale, high quality, diverse dataset.
- **p. 1 / 1. Introduction - extractive body cue:** To further accelerate the development of autonomous driving technology, we present the largest and most diverse multimodal autonomous driving dataset to date, comprising of images ...
- **p. 2 / 1. Introduction - extractive body cue:** We present benchmark results of several state-of-the-art 2D-and 3D object detection and tracking methods on the dataset.
- **p. 2 / 1. Introduction - extractive body cue:** Our dataset currently consists of 1000 scenes for training and validation, and 150 scenes for testing, where each scene spans 20 s.
- **p. 8 / 5.4. Dataset Size - extractive body cue:** For methods that work well on small datasets such as PointPillars [16], more data can achieve better results without requiring data augmentation: we trained the ...
- **p. 7 / 5.2. Baselines for Multi-Object Tracking - extractive body cue:** The resulting Tracktor model achieved a MOTA of 34.8 at LEVEL 1 and 28.3 at LEVEL 2 when tracking vehicles.
- **p. 7 / 5.1. Baselines for Object Detection - extractive body cue:** To achieve good heading prediction, we used a different rotation loss formulation, using a smooth-L1 loss of the heading residual error, wrapping the result between ...
- **p. 8 / 5.3. Domain Gap - extractive body cue:** When evaluating on SUB, training on either SF or SUB yield similar APH, while training on all data yields a 7+ APH improvement.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 8 (5.4. Dataset Size), p. 7 (5.2. Baselines for Multi-Object Tracking) |
| Embodiment/environment | The dataset has scenes selected from both suburban and urban areas, from different times of the day. | hardware/simulator version and reset protocol | p. 5 (3.5. Dataset Analysis), p. 5 (3.5. Dataset Analysis) |
| Dataset/benchmark | The majority of the scenes in our dataset were recorded in three distinct cities (Table 4), namely San Francisco, Phoenix, Mountain View. | role, split, size and leakage | p. 5 (3.5. Dataset Analysis), p. 5 (3.5. Dataset Analysis), p. 7 (5.3. Domain Gap), p. 7 (5.3. Domain Gap) |
| Metric | We ignore detections with lower than a 0.2 class score, and set a minimum threshold of 0.5 IoU for a track and a detect to be considered a match. | definition, denominator, direction and uncertainty | p. 7 (5.2. Baselines for Multi-Object Tracking), p. 7 (5.1. Baselines for Object Detection), p. 6 (5. Experiments) |
| Baseline/ablation | Baseline multi-object tracking metrics for vehicles and pedestrians. reduction of 7.6 when training on SUB and evaluating on SF compared with training on SF and evaluating on SF. | fair input/data/compute/action matching | p. 8 (5.3. Domain Gap), p. 6 (5. Experiments), p. 6 (5.1. Baselines for Object Detection) |

## Explicit Limitations and Failure Boundary

- **p. 4 / 3.4. Sensor Data - extractive body cue:** Our experiments suggest that a highly elongated low-intensity return is a strong indicator for a spurious object, while low intensity alone is not a sufficient ...
- **p. 8 / 5.3. Domain Gap - extractive body cue:** This result does not hold when evaluating on SF.

## Why Read It

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 We demonstrate that the differences in these geographies lead to a pronounced domain gap, enabling exciting research opportunities in the field of domain adaptation.를 문제로 두고, In an effort to help align the research community's contributions with real-world selfdriving problems, we introduce a new large-scale, high quality, diverse dataset.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Sensor Data), p. 5 (3.4. Sensor Data) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
