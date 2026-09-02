# LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2007.00258.
> PDF retrieval source: https://arxiv.org/pdf/2007.00258. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics, state estimation, LiDAR-inertial odometry, SLAM, factor graph, mapping
- Official paper: https://arxiv.org/abs/2007.00258
- Full-text retrieval: https://arxiv.org/pdf/2007.00258
- Code/Project: https://github.com/TixiaoShan/LIO-SAM
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Despite its success, LOAM presents some limitations - by saving its data in a global voxel map, it is often difficult to perform loop closure detection and incorporate other absolute measurements, e.g., ...를 문제로 두고, Scan-matching at a local scale instead of a global scale significantly improves the real-time performance of the system, as does the selective introduction of keyframes, and an efficient sliding window approach that ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We propose a framework for tightly-coupled lidar inertial odometry via smoothing and mapping, LIO-SAM, that achieves highly accurate, real-time mobile robot trajectory estimation and map-building.
- **p. 1 / Abstract - extractive body cue:** LIO-SAM formulates lidar-inertial odometry atop a factor graph, allowing a multitude of relative and absolute measurements, including loop closures, to be incorporated from different sources ...
- **p. 1 / Abstract - extractive body cue:** The estimated motion from inertial measurement unit (IMU) pre-integration de-skews point clouds and produces an initial guess for lidar odometry optimization.
- **p. 1 / Abstract - extractive body cue:** The obtained lidar odometry solution is used to estimate the bias of the IMU.
- **p. 1 / Abstract - extractive body cue:** To ensure high performance in real-time, we marginalize old lidar scans for pose optimization, rather than matching lidar scans to a global map.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Despite its success, LOAM presents some limitations - by saving its data in a global voxel map, it is often difficult to perform loop closure ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a framework for tightly-coupled lidar inertial odometry via smoothing and mapping, LIOSAM, to address the aforementioned problems.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Scan-matching at a local scale instead of a global scale significantly improves the real-time performance of the system, as does the selective introduction of keyframes, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a framework for tightly-coupled lidar inertial odometry via smoothing and mapping, LIOSAM, to address the aforementioned problems.
- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We introduce four types of factors along with one variable type for factor graph construction.
- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We use a factor graph to model this problem, as it is better suited to perform inference when compared with Bayes nets.
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Since we extract two types of features in the previous feature extraction step, Mi is composed of two subvoxel maps that are denoted Me i, ...
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Lidar Odometry Factor When a new lidar scan arrives, we first perform feature extraction.
- **p. 1 / Abstract - extractive body cue:** We propose a framework for tightly-coupled lidar inertial odometry via smoothing and mapping, LIO-SAM, that achieves highly accurate, real-time mobile robot trajectory estimation and map-building.
- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We seek to estimate the state of the robot and its trajectory using the observations of these sensors.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We seek to estimate the state of the robot and its trajectory using the observations of these sensors. | camera/depth stream, pose, map와 language goal | p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (I. INTRODUCTION) |
| State/latent | seek, estimate, state, robot, trajectory, observations, sensors, estimation, localization, mapping, fundamental, prerequisites | robot pose, free-space/semantic map와 local goal | p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (I. INTRODUCTION), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA) |
| Output/action | State estimation, localization and mapping are fundamental prerequisites for a successful intelligent mobile robot, required for feedback control, obstacle avoidance, and planning, among many other capabilities. | collision-free trajectory 또는 velocity command | p. 1 (I. INTRODUCTION), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (I. INTRODUCTION) |
| Objective/outcome | Note that without loss of generality, the proposed system can also incorporate measurements from other sensors, such as elevation from an altimeter or heading from a compass. | goal reach, safety, localization error와 replanning latency | p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 4 (III. LIDAR INERTIAL ODOMETRY VIA) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Scan-matching at a local scale instead of a global scale significantly improves the real-time performance of the system, as does the selective introduction of keyframes, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a framework for tightly-coupled lidar inertial odometry via smoothing and mapping, LIOSAM, to address the aforementioned problems.
- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We introduce four types of factors along with one variable type for factor graph construction.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without failure compared with ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** LIOM outperforms LOAM in this test.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Finally, LIO-SAM outperforms both methods and produces a map that is consistent with the available Google Earth imagery.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** As is shown in Table III, LIO-GPS and LIO-SAM achieve similar RMSE error with respect to the GPS ground truth.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** 4: Mapping results of LOAM, LIOM, and LIO-SAM using the Walking dataset.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Embodiment/environment | Similar to the problems encountered in the Park dataset, LIO-GPS is unable to close the loop when returning to the robot's initial position because of the drift in altitude, which further motivates ... | hardware/simulator version and reset protocol | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Dataset/benchmark | For validation, we collected 5 different datasets across various scales, platforms and environments. | role, split, size and leakage | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Metric | The relative translational error of all methods when the robot returns to the start is shown in Table II. | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Baseline/ablation | The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without failure compared with the results when the data playback speed ... | fair input/data/compute/action matching | p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Results of various methods using the Campus dataset that is gathered on the MIT campus. The red dot indicates the start and end ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** The results of LIOM are not shown due to its failure to initialize properly and produce meaningful results.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without failure compared with ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Mapping results of LOAM and LIO-SAM in the Rotation test. LIOM fails to produce meaningful results.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Campus Dataset TABLE II: End-to-end translation error (meters) Dataset LOAM LIOM LIO-odom LIO-GPS LIO-SAM Campus 192.43 Fail 9.44 6.87 0.12 Park 121.74 34.60 36.36 2.93 ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Due to these challenges, LOAM, LIOM, and LIO-odom all fail to produce meaningful results in this test.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Despite its success, LOAM presents some limitations - by saving its data in a global voxel map, it is often difficult to perform loop closure detection and incorporate other absolute measurements, e.g., ...를 문제로 두고, Scan-matching at a local scale instead of a global scale significantly improves the real-time performance of the system, as does the selective introduction of keyframes, and an efficient sliding window approach that ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
