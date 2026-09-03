# Evaluation - VINS-Mono: A Robust and Versatile Monocular Visual-Inertial State Estimator

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1708.03852; PDF retrieval source: https://arxiv.org/pdf/1708.03852. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 14 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS), p. 3 (Figure/Table caption), p. 11 (IX. EXPERIMENTAL RESULTS), p. 11 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS)): In this large-scale test, We set the keyframe database size to 2000 in order to provide sufficient loop information and achieve real-time performance.

## Evaluation Body Digest

- **p. 11 / IX. EXPERIMENTAL RESULTS - extractive body cue:** We then test our system in the indoor environment to evaluate the performance in repetitive scenes.
- **p. 11 / IX. EXPERIMENTAL RESULTS - extractive body cue:** For aerial robot application, we use VINS-Mono for position feedback to control a drone to follow a pre-defined trajectory.
- **p. 15 / IX. EXPERIMENTAL RESULTS - extractive body cue:** The robot follows the trajectory four times.
- **p. 15 / IX. EXPERIMENTAL RESULTS - extractive body cue:** (a) Aerial robot testbed (b) Testing environment and desired figure eight pattern Fig.
- **p. 12 / IX. EXPERIMENTAL RESULTS - extractive body cue:** VINS-Mono performs well in all EuRoC datasets, even in the most challenging sequence, V1 03 difficult, the one includes aggressive motion, texture-less area, and significant ...
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** The dataset covers the ground that is around 710m in length, 240m in width, and with 60m in height changes.
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** 2) Go around campus: This very large-scale dataset that goes around the whole HKUST campus was recorded with a handheld VI-Sensor4.
- **p. 14 / IX. EXPERIMENTAL RESULTS - extractive body cue:** We run this dataset with an Intel i7-4790 CPU running at 3.60GHz.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IX. EXPERIMENTAL RESULTS (p. 11).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IX. EXPERIMENTAL RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | In this large-scale test, We set the keyframe database size to 2000 in order to provide sufficient loop information and achieve real-time performance. | p. 14 (IX. EXPERIMENTAL RESULTS) |
| IX. EXPERIMENTAL RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | However, VINS-Mono outperforms OKVIS at the system level. | p. 12 (IX. EXPERIMENTAL RESULTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 2. A block diagram illustrating the full pipeline of the proposed monocular visual-inertial state estimator. order to avoid repeated IMU re-integration This technique ... | p. 3 (Figure/Table caption) |
| IX. EXPERIMENTAL RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We perform a numerical analysis to show the accuracy of our system. | p. 11 (IX. EXPERIMENTAL RESULTS) |
| IX. EXPERIMENTAL RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We then test our system in the indoor environment to evaluate the performance in repetitive scenes. | p. 11 (IX. EXPERIMENTAL RESULTS) |

## Dataset / Benchmark Role

- **p. 11 / IX. EXPERIMENTAL RESULTS - extractive body cue:** We then test our system in the indoor environment to evaluate the performance in repetitive scenes.
- **p. 11 / IX. EXPERIMENTAL RESULTS - extractive body cue:** For aerial robot application, we use VINS-Mono for position feedback to control a drone to follow a pre-defined trajectory.
- **p. 15 / IX. EXPERIMENTAL RESULTS - extractive body cue:** The robot follows the trajectory four times.
- **p. 15 / IX. EXPERIMENTAL RESULTS - extractive body cue:** (a) Aerial robot testbed (b) Testing environment and desired figure eight pattern Fig.
- **p. 12 / IX. EXPERIMENTAL RESULTS - extractive body cue:** VINS-Mono performs well in all EuRoC datasets, even in the most challenging sequence, V1 03 difficult, the one includes aggressive motion, texture-less area, and significant ...
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** The dataset covers the ground that is around 710m in length, 240m in width, and with 60m in height changes.
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** 2) Go around campus: This very large-scale dataset that goes around the whole HKUST campus was recorded with a handheld VI-Sensor4.
- **p. 14 / IX. EXPERIMENTAL RESULTS - extractive body cue:** We run this dataset with an Intel i7-4790 CPU running at 3.60GHz.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Outdoor experimental results of the proposed monocular visual-inertial state estimator. Data is collected by a hand-held monocular camera-IMU setup under normal walking condition. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. A block diagram illustrating the full pipeline of the proposed monocular visual-inertial state estimator. order to avoid repeated IMU re-integration This technique was ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. An illustration of the sliding window monocular VIO with relocalization. It is a tightly-coupled formulation with IMU, visual, and loop measurements. where, αbk ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. An illustration of the visual-inertial alignment process for estimator initialization. slightly, we use (12) to correct pre-integration results approx- imately instead of re-propagation. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Illustration of 2 DOF parameterization of gravity. Since the magnitude of gravity is known, g lies on a sphere with radius g ≈9.81m/s2. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6. An illustration of the visual residual on a unit sphere. ˆ¯P cj l is the unit vector for the observation of the lth ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7. An illustration of our marginalization strategy. If the second latest frame is a keyframe, we will keep it in the window, and marginalize ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8. An illustration of motion-only bundle adjustment for camera-rate outputs. sufficient parallax for feature triangulation, and maximize the probability of maintaining accelerometer measurements with ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We then test our system in the indoor environment to evaluate the performance in repetitive scenes. | embodiment, simulator version and control stack | p. 11 (IX. EXPERIMENTAL RESULTS), p. 11 (IX. EXPERIMENTAL RESULTS) |
| Task/environment | For aerial robot application, we use VINS-Mono for position feedback to control a drone to follow a pre-defined trajectory. | reset, timeout, object/scene variation | p. 11 (IX. EXPERIMENTAL RESULTS), p. 15 (IX. EXPERIMENTAL RESULTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The x, y, z error versus time, and the translation error versus distance are shown in Fig. | definition/direction/unit from same section | p. 12 (IX. EXPERIMENTAL RESULTS) |
| Trajectory in MH 05 difficult, compared with OKVIS.. distance [m] 0 10 20 30 40 50 60 70 80 90 100 Tranlation error [m] ... | definition/direction/unit from same section | p. 12 (IX. EXPERIMENTAL RESULTS) |
| The closed loop trajectory is aligned with Google Map to verify its accuracy, as shown in Fig. | definition/direction/unit from same section | p. 13 (IX. EXPERIMENTAL RESULTS) |
| Application II: Mobile Device We port VINS-Mono to mobile devices and present a simple AR application to showcase its accuracy and robustness. | definition/direction/unit from same section | p. 14 (IX. EXPERIMENTAL RESULTS) |
| We perform a numerical analysis to show the accuracy of our system. | definition/direction/unit from same section | p. 11 (IX. EXPERIMENTAL RESULTS) |
| Details of the translation and rotation as well as their corresponding errors are shown in Fig. | definition/direction/unit from same section | p. 14 (IX. EXPERIMENTAL RESULTS) |
| Position, orientation and their corresponding errors of loop closure-disabled VINS-Mono compared with OptiTrack. | definition/direction/unit from same section | p. 16 (IX. EXPERIMENTAL RESULTS) |
| A sudden in pitch error at the 60s is caused by aggressive breaking at the end of the designed trajectory, and possible time misalignment ... | definition/direction/unit from same section | p. 16 (IX. EXPERIMENTAL RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In the first experiment, we compare the proposed algorithm with another state-of-the-art algorithm on public datasets. | comparison identity and matched condition | p. 11 (IX. EXPERIMENTAL RESULTS) |
| However, VINS-Mono outperforms OKVIS at the system level. | comparison identity and matched condition | p. 12 (IX. EXPERIMENTAL RESULTS) |
| In these experiments, we compare VINS-Mono with OKVIS [16], a state-of-the-art VIO that works with monocular and stereo cameras. | comparison identity and matched condition | p. 12 (IX. EXPERIMENTAL RESULTS) |
| With loop correction. the final drift is bounded to [-0.032, 0.09, - 0.07]m, which is trivial compared to the total trajectory length. | comparison identity and matched condition | p. 13 (IX. EXPERIMENTAL RESULTS) |
| Compared with Google map, we can see our results are almost drift-free in this very long-duration test. | comparison identity and matched condition | p. 14 (IX. EXPERIMENTAL RESULTS) |
| Position, orientation and their corresponding errors of loop closure-disabled VINS-Mono compared with OptiTrack. | comparison identity and matched condition | p. 16 (IX. EXPERIMENTAL RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Since the movement is smooth without much yaw angle change in this sequence, only position drift occurs. | component/input/data sensitivity | p. 12 (IX. EXPERIMENTAL RESULTS) |
| (b) Trajectory of VINS-Mono without loop closure. | component/input/data sensitivity | p. 13 (IX. EXPERIMENTAL RESULTS) |
| 17(b) is the VIO-only result from proposed method without loop closure. | component/input/data sensitivity | p. 13 (IX. EXPERIMENTAL RESULTS) |
| Fig. 7. An illustration of our marginalization strategy. If the second latest frame is a keyframe, we will keep it in the window, and ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 2 To address all these issues, we propose VINS-Mono, a robust and versatile monocular visual-inertial state estimator. | In this large-scale test, We set the keyframe database size to 2000 in order to provide sufficient loop information and achieve real-time performance. | PDF body cue; verify exact table/figure and matched conditions | p. 14 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS), p. 3 (Figure/Table caption), p. 11 (IX. EXPERIMENTAL RESULTS), p. 11 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS) |
| Primary metric/result | However, VINS-Mono outperforms OKVIS at the system level. | numeric claim only at cited anchor | p. 12 (IX. EXPERIMENTAL RESULTS) |

- Numeric sentences retained from the body:
- **p. 11 / IX. EXPERIMENTAL RESULTS - extractive body cue:** The datasets are collected onboard a micro aerial vehicle, which contains stereo images (Aptina MT9V034 global shutter, WVGA monochrome, 20 FPS), synchronized IMU measurements (ADIS16448, ...
- **p. 12 / IX. EXPERIMENTAL RESULTS - extractive body cue:** 12 x [m] -2 0 2 4 6 8 10 12 14 y [m] -4 -2 0 2 4 6 8 Trajectory in MH_03_median VINS ...
- **p. 12 / IX. EXPERIMENTAL RESULTS - extractive body cue:** Trajectory in MH 03 median, compared with OKVIS. time [s] 0 20 40 60 80 100 120 140 x error [m] 0 0.5 1 Error ...
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** It contains one forward-looking global shutter camera (MatrixVision mvBlueFOXMLC200w) with 752×480 resolution.
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** We use the built-in IMU (ADXL278 and ADXRS290, 100Hz) for the DJI A3 flight controller.
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** It contains a monocular camera (20Hz) and an IMU (100Hz) inside the DJI A3 controller3.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Final drift is 0.18m. estimator crash caused by unstable feature tracking or active failure detection and recovery. | p. 15 (IX. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | Our approach features both state-ofthe-art and novel solutions to IMU pre-integration, estimator initialization and failure recovery, online extrinsic calibration, tightly-coupled visual-inertial odometry, relocalization, and ... | p. 16 (X. CONCLUSION AND FUTURE WORK) |
| body limitation/failure cue | We cannot see the shape of stairs in the red block. | p. 13 (IX. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | When we went up stairs, OKVIS shows unstable feature tracking, resulting in bad estimation. | p. 13 (IX. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | In this paper, we propose a robust and versatile monocular visual-inertial estimator. | p. 16 (X. CONCLUSION AND FUTURE WORK) |
| body limitation/failure cue | Our system is complete with robust initialization and loop closure. | p. 12 (IX. EXPERIMENTAL RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We run this dataset with an Intel i7-4790 CPU running at 3.60GHz. | p. 14 (IX. EXPERIMENTAL RESULTS) |
| A simple holder that we used to mount the Google Tango device (left) and the iPhone7 Plus (right) that runs our VINS-Mobile implementation. iment ... | p. 16 (IX. EXPERIMENTAL RESULTS) |
| The onboard computation resource is an Intel i7-5500U CPU running at 3.00 GHz. | p. 14 (IX. EXPERIMENTAL RESULTS) |
| Admittedly, Tango is more accurate than our implementation especially for local state estimates. | p. 15 (IX. EXPERIMENTAL RESULTS) |
| Pose Graph Management The size of the pose graph may grow unbounded when the travel distance increases, limiting the real-time performance of the system ... | p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 15 / IX. EXPERIMENTAL RESULTS - extractive body cue:** Final drift is 0.18m. estimator crash caused by unstable feature tracking or active failure detection and recovery.
- **p. 16 / X. CONCLUSION AND FUTURE WORK - extractive body cue:** Our approach features both state-ofthe-art and novel solutions to IMU pre-integration, estimator initialization and failure recovery, online extrinsic calibration, tightly-coupled visual-inertial odometry, relocalization, and efficient ...
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** We cannot see the shape of stairs in the red block.
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** When we went up stairs, OKVIS shows unstable feature tracking, resulting in bad estimation.
- **p. 16 / X. CONCLUSION AND FUTURE WORK - extractive body cue:** In this paper, we propose a robust and versatile monocular visual-inertial estimator.
- **p. 12 / IX. EXPERIMENTAL RESULTS - extractive body cue:** Our system is complete with robust initialization and loop closure.

- **Evidence anchors reviewed:** datasets p. 11 (IX. EXPERIMENTAL RESULTS), p. 11 (IX. EXPERIMENTAL RESULTS), p. 15 (IX. EXPERIMENTAL RESULTS), p. 15 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS), p. 13 (IX. EXPERIMENTAL RESULTS), metrics p. 12 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS), p. 13 (IX. EXPERIMENTAL RESULTS), p. 14 (IX. EXPERIMENTAL RESULTS), p. 11 (IX. EXPERIMENTAL RESULTS), p. 14 (IX. EXPERIMENTAL RESULTS), baselines p. 11 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS), p. 13 (IX. EXPERIMENTAL RESULTS), p. 14 (IX. EXPERIMENTAL RESULTS), p. 16 (IX. EXPERIMENTAL RESULTS), results p. 14 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS), p. 3 (Figure/Table caption), p. 11 (IX. EXPERIMENTAL RESULTS), p. 11 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
