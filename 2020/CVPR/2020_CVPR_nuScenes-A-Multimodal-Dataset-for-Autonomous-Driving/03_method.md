# Method - nuScenes: A Multimodal Dataset for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1903.11027; PDF retrieval source: https://arxiv.org/pdf/1903.11027. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1.1. Contributions), p. 2 (1. Introduction), p. 3 (1.2. Related datasets), p. 3 (2. The nuScenes dataset)): Furthermore the reflectance of lidar is an important feature [40, 51].

## Method Body Digest

- **p. 1 / 1. Introduction - extractive body cue:** Furthermore the reflectance of lidar is an important feature [40, 51].
- **p. 1 / 1. Introduction - extractive body cue:** Such algorithms rely increasingly on machine learning, which drives the need for benchmark datasets.
- **p. 2 / 1.1. Contributions - extractive body cue:** It enables research on multiple tasks such as object detection, tracking and behavior modeling in a range of conditions.
- **p. 2 / 1. Introduction - extractive body cue:** Still, to the best of our knowledge, no other 3D dataset provides attribute annotations, such as pedestrian pose or vehicle state.
- **p. 3 / 1.2. Related datasets - extractive body cue:** It provides 200k 3D boxes over 22 scenes which helped advance the state-of-the-art in 3D object detection.
- **p. 3 / 2. The nuScenes dataset - extractive body cue:** From a large body of training data we manually select 84 logs with 15h of driving data (242km travelled at an av4In preliminary analysis we ...
- **p. 4 / 2. The nuScenes dataset - extractive body cue:** We perform motion compensation using the localization algorithm described below.
- **p. 5 / 3.1. Detection - extractive body cue:** Operating points where recall or precision is less than 10% are removed in order to minimize the impact of noise commonly seen in low precision ...

## Design Rationale

- **p. 2 / 1.1. Contributions - extractive body cue:** Our second contribution is new detection and tracking metrics aimed at the AV application.
- **p. 2 / 1.1. Contributions - extractive body cue:** It enables research on multiple tasks such as object detection, tracking and behavior modeling in a range of conditions.
- **p. 1 / Abstract - extractive body cue:** In this work we present nuTonomy scenes (nuScenes), the first dataset to carry the full autonomous vehicle sensor suite: 6 cameras, 5 radars and 1 ...

## Source Evidence Cues

- **p. 1 / 1. Introduction - extractive body cue:** Furthermore the reflectance of lidar is an important feature [40, 51].
- **p. 1 / 1. Introduction - extractive body cue:** Such algorithms rely increasingly on machine learning, which drives the need for benchmark datasets.
- **p. 2 / 1.1. Contributions - extractive body cue:** It enables research on multiple tasks such as object detection, tracking and behavior modeling in a range of conditions.
- **p. 2 / 1. Introduction - extractive body cue:** Still, to the best of our knowledge, no other 3D dataset provides attribute annotations, such as pedestrian pose or vehicle state.
- **p. 3 / 1.2. Related datasets - extractive body cue:** It provides 200k 3D boxes over 22 scenes which helped advance the state-of-the-art in 3D object detection.
- **p. 3 / 2. The nuScenes dataset - extractive body cue:** From a large body of training data we manually select 84 logs with 15h of driving data (242km travelled at an av4In preliminary analysis we ...
- **p. 4 / 2. The nuScenes dataset - extractive body cue:** We perform motion compensation using the localization algorithm described below.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Furthermore the reflectance of lidar is an important feature [40, 51]. | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | Such algorithms rely increasingly on machine learning, which drives the need for benchmark datasets. | p. 1 (1. Introduction), p. 2 (1.1. Contributions) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | It enables research on multiple tasks such as object detection, tracking and behavior modeling in a range of conditions. | p. 2 (1.1. Contributions), p. 2 (1. Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.1. Detection - extractive body cue:** Operating points where recall or precision is less than 10% are removed in order to minimize the impact of noise commonly seen in low precision ...
- **p. 1 / 1. Introduction - extractive body cue:** However, the returns are even sparser than lidar and less precise in terms of localization.
- **p. 4 / 2. The nuScenes dataset - extractive body cue:** 0.2◦heading, 0.1◦roll/pitch, 20mm RTK positioning, 1000Hz update rate Table 2.
- **p. 5 / 2. The nuScenes dataset - extractive body cue:** At the same time they contain up to 40 radar returns at 10m and 10 at 50m.
- **p. 6 / 3.2. Tracking - extractive body cue:** In the updated formulation sMOTAr[77]6, MOTA is therefore augmented by a term to adjust for the respective recall: sMOTAr = max  0, 1 -IDS ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 6 (3.2. Tracking), p. 4 (2. The nuScenes dataset), p. 6 (3.1. Detection).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Still, best, knowledge, other, dataset, provides, attribute, annotations, pedestrian, pose, vehicle, state, Third, publish | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | Still, best, knowledge, other, dataset, provides, attribute, annotations, pedestrian, pose | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | second, contribution, detection, tracking, metrics, aimed, application, enables, research, multiple | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | Operating, points, where, recall, precision, less, removed, order, minimize, impact | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** Still, to the best of our knowledge, no other 3D dataset provides attribute annotations, such as pedestrian pose or vehicle state.
- **p. 2 / 1.1. Contributions - extractive body cue:** Third, we publish the devkit, evaluation code, taxonomy, annotator instructions, and database schema for industrywide standardization.
- **p. 3 / 1.2. Related datasets - extractive body cue:** It provides 200k 3D boxes over 22 scenes which helped advance the state-of-the-art in 3D object detection.
- **p. 1 / 1. Introduction - extractive body cue:** Radar sensors achieve a range of 200300m and measure the object velocity through the Doppler effect.
- **p. 1 / Abstract - extractive body cue:** As machine learning based methods for detection and tracking become more prevalent, there is a need to train and evaluate such methods on datasets containing ...
- **p. 3 / 1.2. Related datasets - extractive body cue:** KITTI [32] was the pioneering multimodal dataset providing dense pointclouds from a lidar sensor as well as front-facing stereo images and GPS/IMU data.
- **p. 4 / 2. The nuScenes dataset - extractive body cue:** Sensor data in nuScenes. erage of 16km/h).
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | We take advantage of temporal data available in nuScenes by accumulating lidar sweeps for a richer pointcloud as input. | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Aside from the advantage of richer pointclouds, this also provides temporal information, which helps the network in localization and enables velocity prediction. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | Sensor Details 6x Camera RGB, 12Hz capture frequency, 1/1.8" CMOS sensor, 1600 × 900 resolution, auto exposure, JPEG compressed 1x Lidar Spinning, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 2. The nuScenes dataset - extractive body cue:** From a large body of training data we manually select 84 logs with 15h of driving data (242km travelled at an av4In preliminary analysis we ...
- **p. 7 / 4.2. Analysis - extractive body cue:** For this ablation study we train PointPillars with 6x fewer epochs and a one cycle optimizer schedule [71] to cut down the training time.
- **p. 7 / 4.1. Baselines - extractive body cue:** From the detection challenge, we pick the best performing lidar method (Megvii [90]), the fastest reported method at inference time (PointPillars [51]), as well as ...
- **p. 2 / 1.1. Contributions - extractive body cue:** All data, code, and information is made available online3.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Furthermore, reflectance, lidar, important, feature, algorithms, rely, increasingly, machine, learning, drives, need, benchmark, datasets, enables, research, multiple, tasks, object, detection.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | In this section we present object detection and tracking experiments on the nuScenes dataset, analyze their characteristics and suggest avenues for future ... | p. 6 (4. Experiments), p. 3 (1.2. Related datasets) |
| Baseline harness | submissions, MonoDIS [70] was the best, significantly outperforming our image baseline and even some lidar based methods. | p. 7 (4.1. Baselines), p. 6 (4.1. Baselines) |
| Metric / failure reporting | submissions, MonoDIS [70] was the best, significantly outperforming our image baseline and even some lidar based methods. | p. 7 (4.1. Baselines), p. 7 (4.2. Analysis) |

## Failure and Ablation Link

- **p. 7 / 4.2. Analysis - extractive body cue:** For this ablation study we train PointPillars with 6x fewer epochs and a one cycle optimizer schedule [71] to cut down the training time.
- **p. 3 / Dataset - extractive body cue:** The top part of the table indicates datasets without range data.
- **p. 3 / 1.2. Related datasets - extractive body cue:** Other notable multimodal datasets include [15] providing driving behavior labels, [43] providing place categorization labels and [6, 55] providing raw data without semantic labels.
- **p. 8 / 4.2. Analysis - extractive body cue:** No pretraining means weights are initialized randomly using a uniform distribution as in [38].
- **p. 8 / 4.2. Analysis - extractive body cue:** ImageNet [21] pretraining [47] uses a backbone that was first trained to accurately classify images.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 16. PointPillars [51] detection performance vs. semantic prior map location on the val set. For the best lidar network (10 li- dar sweeps with ...
- **p. 8 / 5. Conclusion - extractive body cue:** Future work will add image-level and pointlevel semantic labels and a benchmark for trajectory prediction [63].

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1.1. Contributions), p. 2 (1. Introduction), p. 3 (1.2. Related datasets), p. 3 (2. The nuScenes dataset), objective p. 5 (3.1. Detection), p. 1 (1. Introduction), p. 4 (2. The nuScenes dataset), p. 5 (2. The nuScenes dataset), p. 6 (3.2. Tracking), temporal p. 6 (4.1. Baselines), p. 7 (4.2. Analysis), p. 7 (4.2. Analysis), p. 4 (2. The nuScenes dataset), p. 1 (Abstract), p. 2 (1.1. Contributions).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
