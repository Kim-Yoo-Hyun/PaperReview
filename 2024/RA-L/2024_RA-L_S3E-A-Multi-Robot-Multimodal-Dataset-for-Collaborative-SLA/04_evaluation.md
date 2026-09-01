# Evaluation - S3E: A Multi-Robot Multimodal Dataset for Collaborative SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2210.13723; PDF retrieval source: https://arxiv.org/pdf/2210.13723. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET), p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET)): However, in areas with limited overlap, reducing drift remained a challenge. - The incorporation of UWB measurements in CoLRIO significantly improved localization robustness and accuracy, as demonstrated in Table VII, ...

## Evaluation Body Digest

- **p. 3 / III. S3E DATASET - extractive PDF cue:** The dataset features two mobile robot platform versions: ∙S3Ev1.0: Designed for indoor use with a compact design for exceptional maneuverability in tight spaces. ∙S3Ev2.0: Enhanced ...
- **p. 4 / III. S3E DATASET - extractive PDF cue:** Dataset Analysis To test collaborative mission scenarios and trajectory paradigms, we conducted data collection at Sun Yat-sen University's Guangzhou East Campus using three tele-operated robots ...
- **p. 4 / III. S3E DATASET - extractive PDF cue:** To thoroughly assess the accuracy and robustness of CSLAM algorithms in complex, real-world scenarios, our dataset encompasses a diverse range of environments, each presenting unique ...
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** FENG et al.: S3E: A MULTI-ROBOT MULTIMODAL DATASET FOR COLLABORATIVE SLAM 7 Table VII: ATE [𝑚] for C-SLAM in the S3Ev2.0 outdoor environment with UWB ...
- **p. 6 / III. S3E DATASET - extractive PDF cue:** Dataset Format Our research utilizes the ROS2 [14] bag format for sensor data storage, a standard in robotics known for efficient data management and playback.
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Results Our experimental evaluation of the S3E dataset provides valuable insights into the performance of various state-of-theart SLAM methodologies under diverse real-world conditions.
- **p. 5 / III. S3E DATASET - extractive PDF cue:** The dataset covers a range of challenging environments that C-SLAM algorithms may encounter, including dynamic objects, long operation times, perceptual aliasing, indoor settings, and significant ...
- **p. 3 / III. S3E DATASET - extractive PDF cue:** Ground Truth To create accurate ground truth tracks for our dataset, we use a three-pronged approach: For outdoor environments with good GNSS signal reception, a ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** III. S3E DATASET (p. 3); IV. EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | BENCHMARK / DATASET | However, in areas with limited overlap, reducing drift remained a challenge. - The incorporation of UWB measurements in CoLRIO significantly improved localization robustness and ... | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | BENCHMARK / DATASET | The results, summarized in Table V and Table VI , reveal the absolute trajectory error (ATE) for both single-agent and collaborative SLAM (C-SLAM) systems ... | p. 7 (IV. EXPERIMENTS) |
| III. S3E DATASET | BENCHMARK / DATASET | The dataset features two mobile robot platform versions: ∙S3Ev1.0: Designed for indoor use with a compact design for exceptional maneuverability in tight spaces. ∙S3Ev2.0: ... | p. 3 (III. S3E DATASET) |
| III. S3E DATASET | BENCHMARK / DATASET | Realtime data sharing improves accuracy, but the similarity of observations can make it challenging to detect and adapt to rapid environmental changes. | p. 4 (III. S3E DATASET) |
| III. S3E DATASET | BENCHMARK / DATASET | Ground Truth To create accurate ground truth tracks for our dataset, we use a three-pronged approach: For outdoor environments with good GNSS signal reception, ... | p. 3 (III. S3E DATASET) |

## Dataset / Benchmark Role

- **p. 3 / III. S3E DATASET - extractive PDF cue:** The dataset features two mobile robot platform versions: ∙S3Ev1.0: Designed for indoor use with a compact design for exceptional maneuverability in tight spaces. ∙S3Ev2.0: Enhanced ...
- **p. 4 / III. S3E DATASET - extractive PDF cue:** Dataset Analysis To test collaborative mission scenarios and trajectory paradigms, we conducted data collection at Sun Yat-sen University's Guangzhou East Campus using three tele-operated robots ...
- **p. 4 / III. S3E DATASET - extractive PDF cue:** To thoroughly assess the accuracy and robustness of CSLAM algorithms in complex, real-world scenarios, our dataset encompasses a diverse range of environments, each presenting unique ...
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** FENG et al.: S3E: A MULTI-ROBOT MULTIMODAL DATASET FOR COLLABORATIVE SLAM 7 Table VII: ATE [𝑚] for C-SLAM in the S3Ev2.0 outdoor environment with UWB ...
- **p. 6 / III. S3E DATASET - extractive PDF cue:** Dataset Format Our research utilizes the ROS2 [14] bag format for sensor data storage, a standard in robotics known for efficient data management and playback.
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Results Our experimental evaluation of the S3E dataset provides valuable insights into the performance of various state-of-theart SLAM methodologies under diverse real-world conditions.
- **p. 5 / III. S3E DATASET - extractive PDF cue:** The dataset covers a range of challenging environments that C-SLAM algorithms may encounter, including dynamic objects, long operation times, perceptual aliasing, indoor settings, and significant ...
- **p. 3 / III. S3E DATASET - extractive PDF cue:** Ground Truth To create accurate ground truth tracks for our dataset, we use a three-pronged approach: For outdoor environments with good GNSS signal reception, a ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Mobile Platform Sensor Layout and Coordinate Systems. The left part details the sensor locations and the coordinate frames that define their spatial orientation ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Illustration of Trajectory Paradigms for C- SLAM. The distinct trajectory paradigms adopted by three agents, designated as Alpha, Bob, and Carol, to demonstrate ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Visualization of Outdoor Trajectory in the S3E Dataset. The outdoor trajectories captured in the S3E dataset by three tele-operated mobile platforms, designated as ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: S3E Dataset Organizational Structure. accurate positioning and mapping, especially in tunnels and corridors. Our dataset features unique areas like libraries and squares, adding ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Map in Laboratory_1 with CoRLIO.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: The qualitative results of outdoor environments.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset features two mobile robot platform versions: ∙S3Ev1.0: Designed for indoor use with a compact design for exceptional maneuverability in tight spaces. ∙S3Ev2.0: ... | embodiment, simulator version and control stack | p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET) |
| Task/environment | Dataset Analysis To test collaborative mission scenarios and trajectory paradigms, we conducted data collection at Sun Yat-sen University's Guangzhou East Campus using three tele-operated ... | reset, timeout, object/scene variation | p. 4 (III. S3E DATASET), p. 4 (III. S3E DATASET) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 1 (C OLLABORATIVE Simultaneous Localization and Map) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The results, summarized in Table V and Table VI , reveal the absolute trajectory error (ATE) for both single-agent and collaborative SLAM (C-SLAM) systems ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| However, in areas with limited overlap, reducing drift remained a challenge. - The incorporation of UWB measurements in CoLRIO significantly improved localization robustness and ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| In particular, we utilize the centermeteraccuracy GNSS and RTK for outdoor environments, achieving a precision of ±1cm, to record the ground truth trajectories. | definition/direction/unit from same section | p. 3 (III. S3E DATASET) |
| This includes the sensor types, their resolution, measurement range, accuracy, and any other pertinent technical details that define their contribution to the SLAM system's ... | definition/direction/unit from same section | p. 3 (III. S3E DATASET) |
| Long-distance and multi-cycle data assess stability, accuracy, and efficiency over extended operations. | definition/direction/unit from same section | p. 4 (III. S3E DATASET) |
| To thoroughly assess the accuracy and robustness of CSLAM algorithms in complex, real-world scenarios, our dataset encompasses a diverse range of environments, each presenting ... | definition/direction/unit from same section | p. 4 (III. S3E DATASET) |
| Ground Truth Format: The ground truth data, which is essential for evaluating the accuracy of C-SLAM algorithms, is provided as TXT files. | definition/direction/unit from same section | p. 6 (III. S3E DATASET) |
| Additionally, we have incorporated five collaborative SLAM (C-SLAM) systems into our study, which include COVINS [1], DiSCo-SLAM [2], Swarm-SLAM [19], DCL-SLAM [3], and CoLRIO ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For most of the baselines, we only modify the intrinsic and extrinsic of the sensors and use the left camera for evaluation. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Baselines We have implemented four single-agent SLAM systems, namely ORB-SLAM3 [15], VINS-Fusion [16], LIO-SAM [17], and LVI-SAM [18]. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| The results, summarized in Table V and Table VI , reveal the absolute trajectory error (ATE) for both single-agent and collaborative SLAM (C-SLAM) systems ... | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| In indoor environments without GNSS signals, like laboratories, a motion capture system with 17 high-frequency cameras is used to record track start and endpoints ... | comparison identity and matched condition | p. 3 (III. S3E DATASET) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The results, summarized in Table V and Table VI , reveal the absolute trajectory error (ATE) for both single-agent and collaborative SLAM (C-SLAM) systems ... | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |
| In indoor environments without GNSS signals, like laboratories, a motion capture system with 17 high-frequency cameras is used to record track start and endpoints ... | component/input/data sensitivity | p. 3 (III. S3E DATASET) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we introduce four trajectory prototypes designed to meet these principles and evaluate the adaptability of C-SLAM methodologies across diverse closure strategies ... | However, in areas with limited overlap, reducing drift remained a challenge. - The incorporation of UWB measurements in CoLRIO significantly improved localization robustness and ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET), p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET) |
| Primary metric/result | The results, summarized in Table V and Table VI , reveal the absolute trajectory error (ATE) for both single-agent and collaborative SLAM (C-SLAM) systems ... | numeric claim only at cited anchor | p. 7 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | If inter-loop closures detection fails, we mark it "Failed". | p. 6 (III. S3E DATASET) |
| body limitation/failure cue | Our experiments using this dataset have highlighted the improved robustness of C-SLAM systems, especially in handling inter-loop closures. | p. 7 (VI. CONCLUSION) |
| body limitation/failure cue | Sensor Configuration Our S3E dataset encompasses a multimodal array of sensors, each selected for its operational range and noise characteristics, and meticulously synchronized to ... | p. 3 (III. S3E DATASET) |
| body limitation/failure cue | Teaching Building and Tunnel: Poor lighting and similar geometric structures challenge robustness in maintaining | p. 4 (III. S3E DATASET) |
| body limitation/failure cue | Each paradigm is meticulously crafted to offer a robust framework for assessing C-SLAM algorithms across a multitude of real-world collaborative robotic applications. | p. 4 (III. S3E DATASET) |
| body limitation/failure cue | This diversity is crucial for evaluating C-SLAM performance, adaptability, and robustness, which are key for advancing collaborative robotic navigation and mapping technologies. | p. 5 (III. S3E DATASET) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Publicly available datasets are crucial for the SLAM research community for two main reasons: 1) Development Acceleration: Conducting specialized SLAM experiments involves significant investment ... | p. 1 (C OLLABORATIVE Simultaneous Localization and Map) |
| Despite progress, repeatability and benchmarking in C-SLAM research face challenges due to: 1) System Complexity: The complexity of C-SLAM systems, which integrate intricate software ... | p. 1 (C OLLABORATIVE Simultaneous Localization and Map) |
| The abbreviations used within the table are as follows: "Sw" denotes Software Synchronization, indicating that synchronization across sensors or systems is achieved through software ... | p. 2 (C OLLABORATIVE Simultaneous Localization and Map) |
| Our synchronization system is built around an Altera EP4CE10 FPGA board acting as the primary trigger device, with an Intel NUC11TNKv7 serving as the ... | p. 3 (III. S3E DATASET) |
| Considering transmission delays, all sensor readings are forwarded to the host computer, where they are timestamped upon arrival, organized, and packaged to ensure accurate ... | p. 3 (III. S3E DATASET) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / III. S3E DATASET - extractive PDF cue:** If inter-loop closures detection fails, we mark it "Failed".
- **p. 7 / VI. CONCLUSION - extractive PDF cue:** Our experiments using this dataset have highlighted the improved robustness of C-SLAM systems, especially in handling inter-loop closures.
- **p. 3 / III. S3E DATASET - extractive PDF cue:** Sensor Configuration Our S3E dataset encompasses a multimodal array of sensors, each selected for its operational range and noise characteristics, and meticulously synchronized to capture ...
- **p. 4 / III. S3E DATASET - extractive PDF cue:** Teaching Building and Tunnel: Poor lighting and similar geometric structures challenge robustness in maintaining
- **p. 4 / III. S3E DATASET - extractive PDF cue:** Each paradigm is meticulously crafted to offer a robust framework for assessing C-SLAM algorithms across a multitude of real-world collaborative robotic applications.
- **p. 5 / III. S3E DATASET - extractive PDF cue:** This diversity is crucial for evaluating C-SLAM performance, adaptability, and robustness, which are key for advancing collaborative robotic navigation and mapping technologies.

- **PDF anchors reviewed:** datasets p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET), p. 4 (III. S3E DATASET), p. 7 (IV. EXPERIMENTS), p. 6 (III. S3E DATASET), p. 7 (IV. EXPERIMENTS), metrics p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 3 (III. S3E DATASET), p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET), p. 4 (III. S3E DATASET), baselines p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 3 (III. S3E DATASET), results p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET), p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
