# Method - Waymo Open Dataset: An Autonomous Driving Dataset

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1912.04838; PDF retrieval source: https://arxiv.org/pdf/1912.04838. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Sensor Data), p. 5 (3.4. Sensor Data)): Our dataset currently consists of 1000 scenes for training and validation, and 150 scenes for testing, where each scene spans 20 s.

## Method Body Digest

- **p. 2 / 1. Introduction - extractive body cue:** Our dataset currently consists of 1000 scenes for training and validation, and 150 scenes for testing, where each scene spans 20 s.
- **p. 2 / 1. Introduction - extractive body cue:** This is the first dataset with such low-level, synchronized information available, making it easier to conduct research on LiDAR input representations other than the popular ...
- **p. 5 / 3.4. Sensor Data - extractive body cue:** See Figure 5 for an example output of the projection algorithm.
- **p. 5 / 3.4. Sensor Data - extractive body cue:** The algorithm is efficient and can be used in real time as it usually converges in 2 or 3 iterations.
- **p. 5 / 3.4. Sensor Data - extractive body cue:** We minimize the difference between t and ˜t by solving a single variable (t) convex quadratic optimization.
- **p. 3 / 3.2. Coordinate Systems - extractive body cue:** A point (x, y, z) in the LiDAR Cartesian coordinate system can be uniquely transformed to a (range, azimuth, inclination) tuple in the LiDAR Spherical ...
- **p. 5 / 4.1. Object Detection - extractive body cue:** For each score threshold sampled, it does a Hungarian matching between the predictions with score above the threshold and ground truths to maximize the overall ...
- **p. 1 / 1. Introduction - extractive body cue:** The availability of public large-scale datasets and benchmarks has greatly accelerated progress in machine perception tasks, including image classification, object detection, object tracking, semantic segmentation ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** In an effort to help align the research community's contributions with real-world selfdriving problems, we introduce a new large-scale, high quality, diverse dataset.
- **p. 1 / 1. Introduction - extractive body cue:** To further accelerate the development of autonomous driving technology, we present the largest and most diverse multimodal autonomous driving dataset to date, comprising of images ...
- **p. 2 / 1. Introduction - extractive body cue:** We present benchmark results of several state-of-the-art 2D-and 3D object detection and tracking methods on the dataset.

## Source Evidence Cues

- **p. 2 / 1. Introduction - extractive body cue:** Our dataset currently consists of 1000 scenes for training and validation, and 150 scenes for testing, where each scene spans 20 s.
- **p. 2 / 1. Introduction - extractive body cue:** This is the first dataset with such low-level, synchronized information available, making it easier to conduct research on LiDAR input representations other than the popular ...
- **p. 5 / 3.4. Sensor Data - extractive body cue:** See Figure 5 for an example output of the projection algorithm.
- **p. 5 / 3.4. Sensor Data - extractive body cue:** The algorithm is efficient and can be used in real time as it usually converges in 2 or 3 iterations.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Our dataset currently consists of 1000 scenes for training and validation, and 150 scenes for testing, where each scene spans 20 s. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | This is the first dataset with such low-level, synchronized information available, making it easier to conduct research on LiDAR input representations other ... | p. 2 (1. Introduction), p. 5 (3.4. Sensor Data) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | See Figure 5 for an example output of the projection algorithm. | p. 5 (3.4. Sensor Data), p. 5 (3.4. Sensor Data) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Sensor Data - extractive body cue:** We minimize the difference between t and ˜t by solving a single variable (t) convex quadratic optimization.
- **p. 3 / 3.2. Coordinate Systems - extractive body cue:** A point (x, y, z) in the LiDAR Cartesian coordinate system can be uniquely transformed to a (range, azimuth, inclination) tuple in the LiDAR Spherical ...
- **p. 5 / 4.1. Object Detection - extractive body cue:** For each score threshold sampled, it does a Hungarian matching between the predictions with score above the threshold and ground truths to maximize the overall ...
- **p. 1 / 1. Introduction - extractive body cue:** The availability of public large-scale datasets and benchmarks has greatly accelerated progress in machine perception tasks, including image classification, object detection, object tracking, semantic segmentation ...
- **p. 2 / 3.1. Sensor Specifications - extractive body cue:** We restrict the range of the LiDAR data, and provide data for the first two returns of each laser pulse.
- **p. 4 / 3.4. Sensor Data - extractive body cue:** Each range image pixel corresponds to a LiDAR return.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 3 (3.2. Coordinate Systems), p. 5 (4.1. Object Detection), p. 5 (4.1. Object Detection).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Detection, methods, data, LiDAR, camera, sensors, they, choose, leverage, sensor, inputs, preceding, frames, addition | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | Detection, methods, data, LiDAR, camera, sensors, they, choose, leverage, sensor | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | effort, help, align, research, community, contributions, real-world, selfdriving, problems, introduce | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | minimize, difference, between, solving, single, variable, convex, quadratic, optimization, point | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 4.1. Object Detection - extractive body cue:** Detection methods may use data from any of the LiDAR and camera sensors; they may also choose to leverage sensor inputs from preceding frames.
- **p. 2 / 1. Introduction - extractive body cue:** In addition to sensor features such as elongation, we provide each range image pixel with an accurate vehicle pose.
- **p. 2 / 1. Introduction - extractive body cue:** We present benchmark results of several state-of-the-art 2D-and 3D object detection and tracking methods on the dataset.
- **p. 5 / 3.4. Sensor Data - extractive body cue:** See Figure 5 for an example output of the projection algorithm.
- **p. 1 / 1. Introduction - extractive body cue:** Our proposed dataset contains a large number of highquality, manually annotated 3D ground truth bounding boxes for the LiDAR data, and 2D tightly fitting bounding ...
- **p. 1 / 1. Introduction - extractive body cue:** To further accelerate the development of autonomous driving technology, we present the largest and most diverse multimodal autonomous driving dataset to date, comprising of images ...
- **p. 3 / 3.2. Coordinate Systems - extractive body cue:** A Sensor frame is defined for each sensor.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | In this paradigm, tracking at each timestep t consists of running a detector to generate detections dn t = {d1 t, d2 ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | We trained the model on single frame of sensor data with all LiDARs included. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1. Introduction - extractive body cue:** Our dataset currently consists of 1000 scenes for training and validation, and 150 scenes for testing, where each scene spans 20 s.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** dataset, currently, consists, scenes, training, validation, testing, where, scene, spans, first, low-level, synchronized, information, available, making, easier, conduct, research, LiDAR.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | The dataset has scenes selected from both suburban and urban areas, from different times of the day. | p. 5 (3.5. Dataset Analysis), p. 5 (3.5. Dataset Analysis) |
| Baseline harness | Baseline multi-object tracking metrics for vehicles and pedestrians. reduction of 7.6 when training on SUB and evaluating on SF compared with training ... | p. 8 (5.3. Domain Gap), p. 6 (5. Experiments) |
| Metric / failure reporting | For methods that work well on small datasets such as PointPillars [16], more data can achieve better results without requiring data augmentation: ... | p. 8 (5.4. Dataset Size), p. 7 (5.2. Baselines for Multi-Object Tracking) |

## Failure and Ablation Link

- **p. 7 / 5.1. Baselines for Object Detection - extractive body cue:** We first ignore all 3D labels without any LiDAR points.
- **p. 8 / 5.4. Dataset Size - extractive body cue:** For methods that work well on small datasets such as PointPillars [16], more data can achieve better results without requiring data augmentation: we trained the ...
- **p. 7 / 5.1. Baselines for Object Detection - extractive body cue:** We pre-trained the model on the COCO Dataset [17] before fine-tuning the model on our dataset.
- **p. 4 / 3.4. Sensor Data - extractive body cue:** Our experiments suggest that a highly elongated low-intensity return is a strong indicator for a spurious object, while low intensity alone is not a sufficient ...
- **p. 8 / 5.3. Domain Gap - extractive body cue:** This result does not hold when evaluating on SF.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Sensor Data), p. 5 (3.4. Sensor Data), objective p. 5 (3.4. Sensor Data), p. 3 (3.2. Coordinate Systems), p. 5 (4.1. Object Detection), p. 1 (1. Introduction), p. 2 (3.1. Sensor Specifications), p. 4 (3.4. Sensor Data), temporal p. 7 (5.2. Baselines for Multi-Object Tracking), p. 6 (5.1. Baselines for Object Detection), p. 7 (5.1. Baselines for Object Detection), p. 8 (5.4. Dataset Size), p. 8 (5.4. Dataset Size), p. 3 (3.1. Sensor Specifications).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
