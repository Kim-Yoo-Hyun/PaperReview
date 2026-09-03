# Evaluation - FAST-LIO2: Fast Direct LiDAR-inertial Odometry

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2107.06829; PDF retrieval source: https://arxiv.org/pdf/2107.06829. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 10 (VI. BENCHMARK RESULTS), p. 10 (VI. BENCHMARK RESULTS), p. 14 (VII. REAL-WORLD EXPERIMENTS), p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 17 (Figure/Table caption)): Notice that the considerably reduced processing time for FAST-LIO2 is achieved even at a much higher number of map points.

## Evaluation Body Digest

- **p. 11 / VI. BENCHMARK RESULTS - extractive body cue:** 11 TABLE II THE DATASETS FOR BENCHMARK LiDAR IMU Type Line Type Rate lili Solid-state - 6-axis
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** Platforms Besides the benchmark evaluation where the datasets are mainly collected on the ground, we also test our FAST-LIO2 in a variety of challenging data ...
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** Private Dataset 1) Detail Evaluation of Processing Time: In order to validate the real-time performance of FAST-LIO2, we use the handheld platform to collect a ...
- **p. 16 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** By providing high-accuracy odometry and a high-resolution 3D map of the environment at 100 Hz, FAST-LIO2 is very suitable for a robots' realtime control and ...
- **p. 10 / VI. BENCHMARK RESULTS - extractive body cue:** The data is recorded in the university campus and urban streets with structured scenes.
- **p. 10 / VI. BENCHMARK RESULTS - extractive body cue:** It contains different kinds of scenes, including structured buildings and forests on campus.
- **p. 15 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** 15 TABLE VI THE AVERAGE PROCESSING TIME PER SCAN BENCHMARK IN MILLISECONDS FAST-LIO2 (2000) FAST-LIO2 (1000) FAST-LIO2 (800) FAST-LIO2 (600) FAST-LIO2 (Feature) FAST-LIO2 (ARM) LILI-OM ...
- **p. 16 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** 2) Aggressive UAV Flight Experiment: In order to show the application of FAST-LIO2 in mobile robotic platforms, we deploy a small-scale quadrotor UAV carrying the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** VI. BENCHMARK RESULTS (p. 10); VII. REAL-WORLD EXPERIMENTS (p. 14).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| VII. REAL-WORLD EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notice that the considerably reduced processing time for FAST-LIO2 is achieved even at a much higher number of map points. | p. 16 (VII. REAL-WORLD EXPERIMENTS) |
| VI. BENCHMARK RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | VI-C, we compare the accuracy and processing time of FAST-LIO2 on 19 sequences. | p. 10 (VI. BENCHMARK RESULTS) |
| VI. BENCHMARK RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | In this section, extensive experiments in terms of accuracy, robustness, and computational efficiency are conducted on various open datasets. | p. 10 (VI. BENCHMARK RESULTS) |
| VII. REAL-WORLD EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Private Dataset 1) Detail Evaluation of Processing Time: In order to validate the real-time performance of FAST-LIO2, we use the handheld platform to collect ... | p. 14 (VII. REAL-WORLD EXPERIMENTS) |
| VII. REAL-WORLD EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The mapping results of FAST-LIO2 in the fast motion handheld experiment. controller [62] that takes state feedback from the FAST-LIO2. | p. 16 (VII. REAL-WORLD EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 11 / VI. BENCHMARK RESULTS - extractive body cue:** 11 TABLE II THE DATASETS FOR BENCHMARK LiDAR IMU Type Line Type Rate lili Solid-state - 6-axis
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** Platforms Besides the benchmark evaluation where the datasets are mainly collected on the ground, we also test our FAST-LIO2 in a variety of challenging data ...
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** Private Dataset 1) Detail Evaluation of Processing Time: In order to validate the real-time performance of FAST-LIO2, we use the handheld platform to collect a ...
- **p. 16 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** By providing high-accuracy odometry and a high-resolution 3D map of the environment at 100 Hz, FAST-LIO2 is very suitable for a robots' realtime control and ...
- **p. 10 / VI. BENCHMARK RESULTS - extractive body cue:** The data is recorded in the university campus and urban streets with structured scenes.
- **p. 10 / VI. BENCHMARK RESULTS - extractive body cue:** It contains different kinds of scenes, including structured buildings and forests on campus.
- **p. 15 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** 15 TABLE VI THE AVERAGE PROCESSING TIME PER SCAN BENCHMARK IN MILLISECONDS FAST-LIO2 (2000) FAST-LIO2 (1000) FAST-LIO2 (800) FAST-LIO2 (600) FAST-LIO2 (Feature) FAST-LIO2 (ARM) LILI-OM ...
- **p. 16 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** 2) Aggressive UAV Flight Experiment: In order to show the application of FAST-LIO2 in mobile robotic platforms, we deploy a small-scale quadrotor UAV carrying the ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 1. System overview of FAST-LIO2. with on-tree downsampling which is a common requirement in mapping, whereas downsampling must be done outside before inserting new ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2. The measurement model. 2) Measurement Model: LiDAR typically samples points one after another. The resultant points are therefore sampled at different poses when ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. 2D demonstration of map region management. In (a), the blue rectangle is the initial map region with length L. The red circle is ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4. Re-building an unbalanced sub-tree nodes (i.e., labeled as "deleted") on the sub-trees are removed to reduce tree size. Reducing the height and size ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 5. Data structure comparison over different tree size. with on-tree downsampling and kNN search of ikd-Tree is indeed proportional to log n, which is ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 6. Three different platforms: (a) 280 mm wheelbase small scale quadrotor UAV carrying a forward-looking Livox Avia LiDAR, (b) handheld platforms, (c) 750 mm ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 7. Large-scale scene experiment. FAST-LIO and FAST-LIO2 and are below 0.1 ms. The feature extraction of FAST-LIO is 0.9 ms per scan, which is ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 8. The processing time for each LiDAR scan of FAST-LIO and FAST- LIO2. other hand, the mapping time for FAST-LIO2 is well below the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 11 TABLE II THE DATASETS FOR BENCHMARK LiDAR IMU Type Line Type Rate lili Solid-state - 6-axis | embodiment, simulator version and control stack | p. 11 (VI. BENCHMARK RESULTS), p. 14 (VII. REAL-WORLD EXPERIMENTS) |
| Task/environment | Platforms Besides the benchmark evaluation where the datasets are mainly collected on the ground, we also test our FAST-LIO2 in a variety of challenging ... | reset, timeout, object/scene variation | p. 14 (VII. REAL-WORLD EXPERIMENTS), p. 14 (VII. REAL-WORLD EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 6 (V. MAPPING), p. 1 (I. INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (IV. STATE ESTIMATION), p. 4 (III. SYSTEM OVERVIEW) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In this section, extensive experiments in terms of accuracy, robustness, and computational efficiency are conducted on various open datasets. | definition/direction/unit from same section | p. 10 (VI. BENCHMARK RESULTS) |
| By providing high-accuracy odometry and a high-resolution 3D map of the environment at 100 Hz, FAST-LIO2 is very suitable for a robots' realtime control ... | definition/direction/unit from same section | p. 16 (VII. REAL-WORLD EXPERIMENTS) |
| VI-C, we compare the accuracy and processing time of FAST-LIO2 on 19 sequences. | definition/direction/unit from same section | p. 10 (VI. BENCHMARK RESULTS) |
| Private Dataset 1) Detail Evaluation of Processing Time: In order to validate the real-time performance of FAST-LIO2, we use the handheld platform to collect ... | definition/direction/unit from same section | p. 14 (VII. REAL-WORLD EXPERIMENTS) |
| 11 TABLE II THE DATASETS FOR BENCHMARK LiDAR IMU Type Line Type Rate lili Solid-state - 6-axis | definition/direction/unit from same section | p. 11 (VI. BENCHMARK RESULTS) |
| The map built by FAST-LIO2 in real-time is shown in Fig. | definition/direction/unit from same section | p. 14 (VII. REAL-WORLD EXPERIMENTS) |
| The time consumption and the number of map points at each scan are shown in Fig. | definition/direction/unit from same section | p. 15 (VII. REAL-WORLD EXPERIMENTS) |
| The difference between these two methods becomes drastic when looking at the mapping module, which includes map points retrieve and k-d tree building for ... | definition/direction/unit from same section | p. 15 (VII. REAL-WORLD EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For example, our prior work [63] demonstrated the application of FAST-LIO2 on an autonomous UAV avoiding dynamic small objects (down to 9 mm) in ... | comparison identity and matched condition | p. 16 (VII. REAL-WORLD EXPERIMENTS) |
| Fig. 5. Data structure comparison over different tree size. with on-tree downsampling and kNN search of ikd-Tree is indeed proportional to log n, which ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 1. System overview of FAST-LIO2. with on-tree downsampling which is a common requirement in mapping, whereas downsampling must be done outside before inserting ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Fig. 3. 2D demonstration of map region management. In (a), the blue rectangle is the initial map region with length L. The red circle ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Fig. 4. Re-building an unbalanced sub-tree nodes (i.e., labeled as "deleted") on the sub-trees are removed to reduce tree size. Reducing the height and ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| The detailed time consumption of individual components for processing a scan is shown in Table. | component/input/data sensitivity | p. 14 (VII. REAL-WORLD EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| More specifically, our contributions are as follows: 1) We develop an incremental k-d tree data structure, ikd-Tree, to represent a large dense point cloud ... | Notice that the considerably reduced processing time for FAST-LIO2 is achieved even at a much higher number of map points. | PDF body cue; verify exact table/figure and matched conditions | p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 10 (VI. BENCHMARK RESULTS), p. 10 (VI. BENCHMARK RESULTS), p. 14 (VII. REAL-WORLD EXPERIMENTS), p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 17 (Figure/Table caption) |
| Primary metric/result | VI-C, we compare the accuracy and processing time of FAST-LIO2 on 19 sequences. | numeric claim only at cited anchor | p. 10 (VI. BENCHMARK RESULTS) |

- Numeric sentences retained from the body:
- **p. 10 / VI. BENCHMARK RESULTS - extractive body cue:** The first dataset is from the work LILI-OM [17] and is collected by a solid-state 3D LiDAR Livox Horizon4, which has non-repetitive scan pattern and ...
- **p. 10 / VI. BENCHMARK RESULTS - extractive body cue:** The gyroscope and accelerometer measurements are sampled at 200 Hz by a 6-axis Xsens MTi-670 IMU.
- **p. 10 / VI. BENCHMARK RESULTS - extractive body cue:** The second dataset is from the work LIO-SAM [30] in MIT campus and contains several sequences collected by a VLP-16 LiDAR5 sampled at 10 Hz ...
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** Unless stated otherwise, the scan rate is set at 100 Hz, and the computation platform is the DJI manifold 2-C used in the previous section.
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** Private Dataset 1) Detail Evaluation of Processing Time: In order to validate the real-time performance of FAST-LIO2, we use the handheld platform to collect a ...
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** It should be noted that the LILI-OM also supports solid-state LiDAR, but it fails in this data since its feature extraction module produces too few ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | LIO-SAM shows good performance in its own sequences liosam 2 and liosam 3 but cannot keep it on other sequences such as ulhk. | p. 13 (100 Hz) |
| body limitation/failure cue | It should be noted that the LILI-OM also supports solid-state LiDAR, but it fails in this data since its feature extraction module produces too ... | p. 14 (VII. REAL-WORLD EXPERIMENTS) |
| body limitation/failure cue | As can be seen, the averaging mapping time per scan for FAST-LIO exceeds 10 ms hence cannot be processed in real-time for this large ... | p. 15 (VII. REAL-WORLD EXPERIMENTS) |
| body limitation/failure cue | Since FAST-LIO2 does not extract features, it is naturally adaptable to this new LiDAR. | p. 14 (VII. REAL-WORLD EXPERIMENTS) |
| body limitation/failure cue | The occasional timeout usually does not affect a subsequent controller since the IMU propagated state estimate could be used during this short period. | p. 16 (VII. REAL-WORLD EXPERIMENTS) |
| body limitation/failure cue | In this section, extensive experiments in terms of accuracy, robustness, and computational efficiency are conducted on various open datasets. | p. 10 (VI. BENCHMARK RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All three platforms carry the same DJI Manifold2C onboard computer. | p. 14 (VII. REAL-WORLD EXPERIMENTS) |
| For FAST-LIO2, we additionally test on the ARM (Khadas VIM3) onboard computer. | p. 14 (VII. REAL-WORLD EXPERIMENTS) |
| Our implementation of the system FAST-LIO2, and the data structure ikd-Tree are both open-sourced on Github2,3. | p. 1 (Abstract) |
| These features make the ikd-Tree very suitable for LiDAR odometry and mapping application, leading to 100 Hz odometry and mapping on computationallyconstrained platforms such ... | p. 2 (I. INTRODUCTION) |
| As a result, the ikd-Tree tracks all map points in a large cube area with a certain length (referred to as "map size" in ... | p. 4 (III. SYSTEM OVERVIEW) |
| It consists of two key steps: propagation upon each IMU measurement and iterated update upon each LiDAR scan, both step estimates the state naturally ... | p. 5 (IV. STATE ESTIMATION) |
| Since the IMU measurements are typically at a higher frequency than a LiDAR scan (e.g., 200Hz for IMU measurement and 10Hz ∼100Hz for LiDAR ... | p. 5 (IV. STATE ESTIMATION) |
| 1 Forward propagation to obtain state prediction bxk and its covariance bPk via (6); 2 Backward propagation to compensate motion [22]; 3 κ = ... | p. 6 (V. MAPPING) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 13 / 100 Hz - extractive body cue:** LIO-SAM shows good performance in its own sequences liosam 2 and liosam 3 but cannot keep it on other sequences such as ulhk.
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** It should be noted that the LILI-OM also supports solid-state LiDAR, but it fails in this data since its feature extraction module produces too few ...
- **p. 15 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** As can be seen, the averaging mapping time per scan for FAST-LIO exceeds 10 ms hence cannot be processed in real-time for this large scene.
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** Since FAST-LIO2 does not extract features, it is naturally adaptable to this new LiDAR.
- **p. 16 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** The occasional timeout usually does not affect a subsequent controller since the IMU propagated state estimate could be used during this short period.
- **p. 10 / VI. BENCHMARK RESULTS - extractive body cue:** In this section, extensive experiments in terms of accuracy, robustness, and computational efficiency are conducted on various open datasets.

- **Evidence anchors reviewed:** datasets p. 11 (VI. BENCHMARK RESULTS), p. 14 (VII. REAL-WORLD EXPERIMENTS), p. 14 (VII. REAL-WORLD EXPERIMENTS), p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 10 (VI. BENCHMARK RESULTS), p. 10 (VI. BENCHMARK RESULTS), metrics p. 10 (VI. BENCHMARK RESULTS), p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 10 (VI. BENCHMARK RESULTS), p. 14 (VII. REAL-WORLD EXPERIMENTS), p. 11 (VI. BENCHMARK RESULTS), p. 14 (VII. REAL-WORLD EXPERIMENTS), baselines p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 12 (Figure/Table caption), results p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 10 (VI. BENCHMARK RESULTS), p. 10 (VI. BENCHMARK RESULTS), p. 14 (VII. REAL-WORLD EXPERIMENTS), p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 17 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
