# Evaluation - Waymo Open Dataset: An Autonomous Driving Dataset

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1912.04838; PDF retrieval source: https://arxiv.org/pdf/1912.04838. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5.4. Dataset Size), p. 7 (5.2. Baselines for Multi-Object Tracking), p. 7 (5.1. Baselines for Object Detection), p. 8 (5.3. Domain Gap), p. 3 (3.1. Sensor Specifications), p. 4 (3.4. Sensor Data)): For methods that work well on small datasets such as PointPillars [16], more data can achieve better results without requiring data augmentation: we trained the same PointPillars model [16] from ...

## Evaluation Body Digest

- **p. 5 / 3.5. Dataset Analysis - extractive PDF cue:** The dataset has scenes selected from both suburban and urban areas, from different times of the day.
- **p. 5 / 3.5. Dataset Analysis - extractive PDF cue:** In addition to the urban/suburban and time of day diversity, scenes in the dataset are selected from many different parts within the cities.
- **p. 7 / 5.3. Domain Gap - extractive PDF cue:** The majority of the scenes in our dataset were recorded in three distinct cities (Table 4), namely San Francisco, Phoenix, Mountain View.
- **p. 7 / 5.3. Domain Gap - extractive PDF cue:** We filter the training and validation datasets to only contain frames from a specific geographic subset referred to as SF (San Francisco), SUB (MTV + ...
- **p. 8 / 5.4. Dataset Size - extractive PDF cue:** For methods that work well on small datasets such as PointPillars [16], more data can achieve better results without requiring data augmentation: we trained the ...
- **p. 6 / 5. Experiments - extractive PDF cue:** The same method can be applied to other object types in the dataset.
- **p. 8 / 5.4. Dataset Size - extractive PDF cue:** The AP/APH at LEVEL 2 difficulty on the Validation set of Vehicles and Pedestrians as the dataset size grows.
- **p. 3 / 3.2. Coordinate Systems - extractive PDF cue:** Transform among close frames is very accurate in this dataset.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 3. Waymo Open Dataset (p. 2); 3.5. Dataset Analysis (p. 5); 5. Experiments (p. 6); 5.4. Dataset Size (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.4. Dataset Size | BENCHMARK / DATASET | For methods that work well on small datasets such as PointPillars [16], more data can achieve better results without requiring data augmentation: we trained ... | p. 8 (5.4. Dataset Size) |
| 5.2. Baselines for Multi-Object Tracking | BENCHMARK / DATASET | The resulting Tracktor model achieved a MOTA of 34.8 at LEVEL 1 and 28.3 at LEVEL 2 when tracking vehicles. | p. 7 (5.2. Baselines for Multi-Object Tracking) |
| 5.1. Baselines for Object Detection | BENCHMARK / DATASET | To achieve good heading prediction, we used a different rotation loss formulation, using a smooth-L1 loss of the heading residual error, wrapping the result ... | p. 7 (5.1. Baselines for Object Detection) |
| 5.3. Domain Gap | BENCHMARK / DATASET | When evaluating on SUB, training on either SF or SUB yield similar APH, while training on all data yields a 7+ APH improvement. | p. 8 (5.3. Domain Gap) |
| 3.1. Sensor Specifications | BENCHMARK / DATASET | The image sizes reflect the results of both cropping and downsampling the original sensor data. | p. 3 (3.1. Sensor Specifications) |

## Dataset / Benchmark Role

- **p. 5 / 3.5. Dataset Analysis - extractive PDF cue:** The dataset has scenes selected from both suburban and urban areas, from different times of the day.
- **p. 5 / 3.5. Dataset Analysis - extractive PDF cue:** In addition to the urban/suburban and time of day diversity, scenes in the dataset are selected from many different parts within the cities.
- **p. 7 / 5.3. Domain Gap - extractive PDF cue:** The majority of the scenes in our dataset were recorded in three distinct cities (Table 4), namely San Francisco, Phoenix, Mountain View.
- **p. 7 / 5.3. Domain Gap - extractive PDF cue:** We filter the training and validation datasets to only contain frames from a specific geographic subset referred to as SF (San Francisco), SUB (MTV + ...
- **p. 8 / 5.4. Dataset Size - extractive PDF cue:** For methods that work well on small datasets such as PointPillars [16], more data can achieve better results without requiring data augmentation: we trained the ...
- **p. 6 / 5. Experiments - extractive PDF cue:** The same method can be applied to other object types in the dataset.
- **p. 8 / 5.4. Dataset Size - extractive PDF cue:** The AP/APH at LEVEL 2 difficulty on the Validation set of Vehicles and Pedestrians as the dataset size grows.
- **p. 3 / 3.2. Coordinate Systems - extractive PDF cue:** Transform among close frames is very accurate in this dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison of some popular datasets. The Argo Dataset refers to their Tracking dataset only, not the Motion Forecasting dataset. 3D labels projected to ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Table 2. LiDAR Data Specifications for Front (F), Right (R), Side- Left (SL), Side-Right (SR), and Top (TOP) sensors. The vertical field of view (VFOV) ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 3. Camera Specifications for Front (F), Front-Left (FL), Front- Right (FR), Side-Left (SL), Side-Right (SR) cameras. The image sizes reflect the results of both ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1. Sensor layout and coordinate systems. ning mode can vary from scene to scene. All camera images are downsampled and cropped from the raw ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. LiDAR label example. Yellow = vehicle. Red = pedes- trian. Blue = sign. Pink = cyclist. axes depends on the LiDAR. The camera ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Camera LiDAR synchronization accuracy in milliseconds. The number in x-axis is in milli-seconds. The y-axis denotes the percentage of data frames.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. A range image example. It is cropped to only show the front 90◦. The first three rows are range, intensity, and elongation from ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. An example image overlaid with LiDAR point projections. PHX MTV SF Day Night Dawn Train

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset has scenes selected from both suburban and urban areas, from different times of the day. | embodiment, simulator version and control stack | p. 5 (3.5. Dataset Analysis), p. 5 (3.5. Dataset Analysis) |
| Task/environment | In addition to the urban/suburban and time of day diversity, scenes in the dataset are selected from many different parts within the cities. | reset, timeout, object/scene variation | p. 5 (3.5. Dataset Analysis), p. 7 (5.3. Domain Gap) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 5 (4.1. Object Detection), p. 2 (1. Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 2 (1. Introduction), p. 5 (3.4. Sensor Data) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We ignore detections with lower than a 0.2 class score, and set a minimum threshold of 0.5 IoU for a track and a detect ... | definition/direction/unit from same section | p. 7 (5.2. Baselines for Multi-Object Tracking) |
| To achieve good heading prediction, we used a different rotation loss formulation, using a smooth-L1 loss of the heading residual error, wrapping the result ... | definition/direction/unit from same section | p. 7 (5.1. Baselines for Object Detection) |
| We use 0.7 IoU for vehicles and 0.5 IoU for pedestrians when computing metrics for all tasks. | definition/direction/unit from same section | p. 6 (5. Experiments) |
| IoU thresholds: Vehicle 0.7, Pedestrian 0.5. | definition/direction/unit from same section | p. 8 (5.3. Domain Gap) |
| The synchronization error is bounded in [-6ms, 7ms] with 99.7% confidence, [-6ms, 8ms] with 99.9995% confidence. | definition/direction/unit from same section | p. 4 (3.4. Sensor Data) |
| Figure 6. Parallelogram cover of all level 13 S2 cells touched by all ego poses in San Francisco, Mountain View, and Phoenix. AP = ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Camera LiDAR synchronization accuracy in milliseconds. | definition/direction/unit from same section | p. 4 (3.4. Sensor Data) |
| Training just on SF when evaluating on SF yields a 2.4 APH improvement as compared to training on the larger combined dataset, while training ... | definition/direction/unit from same section | p. 8 (5.3. Domain Gap) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Baseline multi-object tracking metrics for vehicles and pedestrians. reduction of 7.6 when training on SUB and evaluating on SF compared with training on SF ... | comparison identity and matched condition | p. 8 (5.3. Domain Gap) |
| We provide baselines on our datasets based on recent approaches for detection and tracking for vehicles and pedestrians. | comparison identity and matched condition | p. 6 (5. Experiments) |
| 3D LiDAR Detection To establish a 3D Object Detection baseline, we reimplemented PointPillars [16], which is a simple and efficient LiDAR-based 3D detector that ... | comparison identity and matched condition | p. 6 (5.1. Baselines for Object Detection) |
| 3D Tracking We provide an online 3D multi-object tracking baseline following the common tracking-by-detection paradigm, leaning heavily on the above PointPillars [16] models. | comparison identity and matched condition | p. 7 (5.2. Baselines for Multi-Object Tracking) |
| For the 3D LiDARbased vehicle object detector, we observed an APH reduction of 8.0 when training on SF and evaluating on SUB compared with ... | comparison identity and matched condition | p. 7 (5.3. Domain Gap) |
| 3D object detection baseline LEVEL 2 APH results for domain shift on 3D vehicles and pedestrians on the Validation set. | comparison identity and matched condition | p. 8 (5.3. Domain Gap) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We first ignore all 3D labels without any LiDAR points. | component/input/data sensitivity | p. 7 (5.1. Baselines for Object Detection) |
| For methods that work well on small datasets such as PointPillars [16], more data can achieve better results without requiring data augmentation: we trained ... | component/input/data sensitivity | p. 8 (5.4. Dataset Size) |
| We pre-trained the model on the COCO Dataset [17] before fine-tuning the model on our dataset. | component/input/data sensitivity | p. 7 (5.1. Baselines for Object Detection) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In an effort to help align the research community's contributions with real-world selfdriving problems, we introduce a new large-scale, high quality, diverse dataset. | For methods that work well on small datasets such as PointPillars [16], more data can achieve better results without requiring data augmentation: we trained ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5.4. Dataset Size), p. 7 (5.2. Baselines for Multi-Object Tracking), p. 7 (5.1. Baselines for Object Detection), p. 8 (5.3. Domain Gap), p. 3 (3.1. Sensor Specifications), p. 4 (3.4. Sensor Data) |
| Primary metric/result | The resulting Tracktor model achieved a MOTA of 34.8 at LEVEL 1 and 28.3 at LEVEL 2 when tracking vehicles. | numeric claim only at cited anchor | p. 7 (5.2. Baselines for Multi-Object Tracking) |

- Numeric sentences retained from the body:
- **p. 4 / 3.4. Sensor Data - extractive PDF cue:** The synchronization accuracy is computed as camera center time -frame start timecamera center offset/360◦∗0.1s (4) The camera center time is the exposure time of the ...
- **p. 4 / 3.4. Sensor Data - extractive PDF cue:** The synchronization error is bounded in [-6ms, 7ms] with 99.7% confidence, [-6ms, 8ms] with 99.9995% confidence.
- **p. 7 / 5.2. Baselines for Multi-Object Tracking - extractive PDF cue:** Our tracked state consists of a 10 parameter state tm t = {cx, cy, cz, w, l, h, α, vx, vy, vz} with a constant ...
- **p. 1 / Abstract - extractive PDF cue:** Our new dataset consists of 1150 scenes that each span 20 seconds, consisting of well synchronized and calibrated high quality LiDAR and camera data captured ...
- **p. 1 / Abstract - extractive PDF cue:** It is 15x more diverse than the largest camera+LiDAR dataset available based on our proposed geographical coverage metric.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our dataset currently consists of 1000 scenes for training and validation, and 150 scenes for testing, where each scene spans 20 s.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our experiments suggest that a highly elongated low-intensity return is a strong indicator for a spurious object, while low intensity alone is not a ... | p. 4 (3.4. Sensor Data) |
| body limitation/failure cue | This result does not hold when evaluating on SF. | p. 8 (5.3. Domain Gap) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We then run the detector on all 5 camera images, and aggregate the results for evaluation. | p. 7 (5.1. Baselines for Object Detection) |
| We recorded all the sensor data of our dataset using an industrial-strength sensor suite consisting of multiple highresolution cameras and multiple high-quality LiDAR sensors. | p. 1 (1. Introduction) |
| The label is encoded as (cx, cy, l, w) with a unique tracking ID, where cx and cy represent the center pixel of the ... | p. 3 (3.3. Ground Truth Labels) |
| All of the coordinate systems follow the right hand rule, and the dataset contains all information needed to transform data between any two frames ... | p. 3 (3.2. Coordinate Systems) |
| LiDAR data is encoded in this dataset as range images, one for each LiDAR return; data for the first two returns is provided. | p. 4 (3.4. Sensor Data) |
| We emphasize that all LiDAR and all camera groundtruth labels were manually created by highly experienced human annotators using industrial-strength labeling tools. | p. 4 (3.3. Ground Truth Labels) |
| It computes precision and recall based on the matching result. | p. 5 (4.1. Object Detection) |
| The metrics implementation takes a set of predictions with scores normalized to [0, 1], and samples a fixed number of score thresholds uniformly in ... | p. 5 (4.1. Object Detection) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / 3.4. Sensor Data - extractive PDF cue:** Our experiments suggest that a highly elongated low-intensity return is a strong indicator for a spurious object, while low intensity alone is not a sufficient ...
- **p. 8 / 5.3. Domain Gap - extractive PDF cue:** This result does not hold when evaluating on SF.

- **PDF anchors reviewed:** datasets p. 5 (3.5. Dataset Analysis), p. 5 (3.5. Dataset Analysis), p. 7 (5.3. Domain Gap), p. 7 (5.3. Domain Gap), p. 8 (5.4. Dataset Size), p. 6 (5. Experiments), metrics p. 7 (5.2. Baselines for Multi-Object Tracking), p. 7 (5.1. Baselines for Object Detection), p. 6 (5. Experiments), p. 8 (5.3. Domain Gap), p. 4 (3.4. Sensor Data), p. 6 (Figure/Table caption), baselines p. 8 (5.3. Domain Gap), p. 6 (5. Experiments), p. 6 (5.1. Baselines for Object Detection), p. 7 (5.2. Baselines for Multi-Object Tracking), p. 7 (5.3. Domain Gap), p. 8 (5.3. Domain Gap), results p. 8 (5.4. Dataset Size), p. 7 (5.2. Baselines for Multi-Object Tracking), p. 7 (5.1. Baselines for Object Detection), p. 8 (5.3. Domain Gap), p. 3 (3.1. Sensor Specifications), p. 4 (3.4. Sensor Data).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
