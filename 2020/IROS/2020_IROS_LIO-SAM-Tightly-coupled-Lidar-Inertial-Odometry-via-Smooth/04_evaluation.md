# Evaluation - LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2007.00258; PDF retrieval source: https://arxiv.org/pdf/2007.00258. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS)): The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without failure compared with the results when the data ...

## Evaluation Body Digest

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Similar to the problems encountered in the Park dataset, LIO-GPS is unable to close the loop when returning to the robot's initial position because of ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Benchmarking Results TABLE III: RMSE translation error w.r.t GPS Dataset LOAM LIOM LIO-odom LIO-GPS LIO-SAM Park 47.31 28.96 23.96 1.09 0.96 Since full GPS coverage ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** For validation, we collected 5 different datasets across various scales, platforms and environments.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** For instance, the Park dataset is collected in a feature-rich environment where the vegetation results in a large quantity of features, whereas the Amsterdam dataset ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** These datasets are referred to as Rotation, Walking, Campus, Park and Amsterdam, respectively.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The details of these datasets are shown in Table I.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The maximum translational and rotational speed encountered is this dataset is 1.8 m/s and 213.9 ◦/s respectively.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** 5: Results of various methods using the Campus dataset that is gathered on the MIT campus.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without failure compared ... | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | LIOM outperforms LOAM in this test. | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Finally, LIO-SAM outperforms both methods and produces a map that is consistent with the available Google Earth imagery. | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | As is shown in Table III, LIO-GPS and LIO-SAM achieve similar RMSE error with respect to the GPS ground truth. | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4: Mapping results of LOAM, LIOM, and LIO-SAM using the Walking dataset. | p. 6 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Similar to the problems encountered in the Park dataset, LIO-GPS is unable to close the loop when returning to the robot's initial position because of ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Benchmarking Results TABLE III: RMSE translation error w.r.t GPS Dataset LOAM LIOM LIO-odom LIO-GPS LIO-SAM Park 47.31 28.96 23.96 1.09 0.96 Since full GPS coverage ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** For validation, we collected 5 different datasets across various scales, platforms and environments.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** For instance, the Park dataset is collected in a feature-rich environment where the vegetation results in a large quantity of features, whereas the Amsterdam dataset ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** These datasets are referred to as Rotation, Walking, Campus, Park and Amsterdam, respectively.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The details of these datasets are shown in Table I.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The maximum translational and rotational speed encountered is this dataset is 1.8 m/s and 213.9 ◦/s respectively.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** 5: Results of various methods using the Campus dataset that is gathered on the MIT campus.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: The system structure of LIO-SAM. The system receives input from a 3D lidar, an IMU and optionally a GPS. Four types of factors ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Datasets are collected on 3 platforms: (a) a custom-built handheld device, (b) an unmanned ground vehicle - Clearpath Jackal, (c) an electric boat ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Mapping results of LOAM and LIO-SAM in the Rotation test. LIOM fails to produce meaningful results.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Mapping results of LOAM, LIOM, and LIO-SAM using the Walking dataset. The map of LOAM in (b) diverges multiple times when aggressive rotation ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Results of various methods using the Campus dataset that is gathered on the MIT campus. The red dot indicates the start and end ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Results of various methods using the Park dataset that is gathered in Pleasant Valley Park, New Jersey. The red dot indicates the start ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Map of LIO-SAM aligned with Google Earth. as opposed to the runtime in the Park test.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Similar to the problems encountered in the Park dataset, LIO-GPS is unable to close the loop when returning to the robot's initial position because ... | embodiment, simulator version and control stack | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Task/environment | Benchmarking Results TABLE III: RMSE translation error w.r.t GPS Dataset LOAM LIOM LIO-odom LIO-GPS LIO-SAM Park 47.31 28.96 23.96 1.09 0.96 Since full GPS ... | reset, timeout, object/scene variation | p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (I. INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The relative translational error of all methods when the robot returns to the start is shown in Table II. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Campus Dataset TABLE II: End-to-end translation error (meters) Dataset LOAM LIOM LIO-odom LIO-GPS LIO-SAM Campus 192.43 Fail 9.44 6.87 0.12 Park 121.74 34.60 36.36 ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Though the trajectories of LIO-GPS and LIO-SAM coincide in the horizontal plane, their relative translational errors are different (Table II). | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| This RMSE error does not take the error along the z axis into account. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| As is shown in Table III, LIO-GPS and LIO-SAM achieve similar RMSE error with respect to the GPS ground truth. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Due to its failure to produce meaningful results, the map of LIOM is not shown. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 2: Datasets are collected on 3 platforms: (a) a custom-built handheld device, (b) an unmanned ground vehicle - Clearpath Jackal, (c) an electric ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 7: Map of LIO-SAM aligned with Google Earth. as opposed to the runtime in the Park test. | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without failure compared ... | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| LIOM outperforms LOAM in this test. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| As is shown, the map of LIO-SAM preserves more fine structural details of the environment compared with the map of LOAM. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| As is shown, the trajectory of LOAM drifts significantly when compared with all other methods. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Fig. 4: Mapping results of LOAM, LIOM, and LIO-SAM using the Walking dataset. The map of LOAM in (b) diverges multiple times when aggressive ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| 200 -100 0 100 200 300 400 -500 -400 -300 -200 -100 0 LOAM LIO-odom LIO-GPS LIO-SAM GPS availability -20 -15 -10 -5 0 ... | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We note that only the CPU is used for computation, without parallel computing enabled. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Because LIOM uses the same initialization pipeline from [25], it inherits the same initialization sensitivity of visual-inertial SLAM and is not able to initialize ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Without the correction of GPS data, the trajectory of LIO-odom begins to visibly drift at the lower right corner of the map. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| LIO-SAM produces a map that is consistent with the Google Earth imagery, without using GPS. mapping area, GPS reception is rarely available and inaccurate ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without failure compared ... | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Scan-matching at a local scale instead of a global scale significantly improves the real-time performance of the system, as does the selective introduction of ... | The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without failure compared ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Primary metric/result | LIOM outperforms LOAM in this test. | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Amsterdam Dataset Finally, we mounted the sensor suite on a boat and cruised along the canals of Amsterdam for 3 hours.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In other words, some lidar frames are dropped if the runtime takes more than 100ms when the lidar rotation rate is 10Hz.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 5: Results of various methods using the Campus dataset that is gathered on the MIT campus. The red dot indicates the start and ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | The results of LIOM are not shown due to its failure to initialize properly and produce meaningful results. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without failure compared ... | p. 7 (IV. EXPERIMENTS) |
| body limitation/failure cue | Fig. 3: Mapping results of LOAM and LIO-SAM in the Rotation test. LIOM fails to produce meaningful results. | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Campus Dataset TABLE II: End-to-end translation error (meters) Dataset LOAM LIOM LIO-odom LIO-GPS LIO-SAM Campus 192.43 Fail 9.44 6.87 0.12 Park 121.74 34.60 36.36 ... | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | Due to these challenges, LOAM, LIOM, and LIO-odom all fail to produce meaningful results in this test. | p. 6 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our implementation of LIO-SAM is freely available on Github1. | p. 5 (IV. EXPERIMENTS) |
| In all the experiments, LOAM and LIOSAM are forced to run in real-time. | p. 5 (IV. EXPERIMENTS) |
| Additionally, LIOM only runs at 0.67× real-time, while the other methods run in real-time. | p. 6 (IV. EXPERIMENTS) |
| Throughout all tests, LOAM and LIO-SAM are forced to run in real-time. | p. 7 (IV. EXPERIMENTS) |
| In other words, some lidar frames are dropped if the runtime takes more than 100ms when the lidar rotation rate is 10Hz. | p. 7 (IV. EXPERIMENTS) |
| We then apply the IMU preintegration method proposed in [20] to obtain the relative body motion between two timesteps. | p. 3 (III. LIDAR INERTIAL ODOMETRY VIA) |
| The preintegrated measurements ∆vij, ∆pij, and ∆Rij between time i and j can be computed using: ∆vij = RT i (vj -vi -g∆tij) (7) ... | p. 3 (III. LIDAR INERTIAL ODOMETRY VIA) |
| 3) Relative transformation: The distance between a feature and its edge or planar patch correspondence can be computed using the following equations: dek = | p. 4 (III. LIDAR INERTIAL ODOMETRY VIA) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Results of various methods using the Campus dataset that is gathered on the MIT campus. The red dot indicates the start and end ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** The results of LIOM are not shown due to its failure to initialize properly and produce meaningful results.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without failure compared with ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Mapping results of LOAM and LIO-SAM in the Rotation test. LIOM fails to produce meaningful results.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Campus Dataset TABLE II: End-to-end translation error (meters) Dataset LOAM LIOM LIO-odom LIO-GPS LIO-SAM Campus 192.43 Fail 9.44 6.87 0.12 Park 121.74 34.60 36.36 2.93 ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Due to these challenges, LOAM, LIOM, and LIO-odom all fail to produce meaningful results in this test.

- **Evidence anchors reviewed:** datasets p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), metrics p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), baselines p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (Figure/Table caption), p. 7 (IV. EXPERIMENTS), results p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
