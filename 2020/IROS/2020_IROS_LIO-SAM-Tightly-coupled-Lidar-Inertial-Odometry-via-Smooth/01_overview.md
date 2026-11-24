# LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2007.00258.
> PDF retrieval source: https://arxiv.org/pdf/2007.00258. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / IROS
- Authors: Tixiao Shan, Brendan Englot, Drew Meyers, Wei Wang, Carlo Ratti, Daniela Rus
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics, state estimation, LiDAR-inertial odometry, SLAM, factor graph, mapping
- Official paper: https://arxiv.org/abs/2007.00258
- Full-text retrieval: https://arxiv.org/pdf/2007.00258
- Code/Project: https://github.com/TixiaoShan/LIO-SAM
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://arxiv.org/pdf/2007.00258v3) 기준이다.

> DOC-QA3 (2026-10-23): [LIO-SAM의 지정 수식·공개 구현 대조](./03_method.md). Commit `0be1fbe6275fb8366d5b800af4fc8c76a885c869`의 정적 검토이며 paper-run 버전·실행 결과는 미확인. [결과와 경계](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/PAPER_CODE_FORMULA_REVIEW_2026-10-23.md).

## Why This Paper Is Here

LIO-SAM은 라이다와 관성 센서의 상대 운동, 루프 폐쇄 및 이용 가능한 절대 위치 관측을 요인 그래프로 결합해 궤적과 지도를 추정한다. [PDF 1쪽](https://arxiv.org/pdf/2007.00258v3#page=1)

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

- 관성 사전적분으로 스캔 왜곡을 보정하고 라이다 정합의 초깃값을 구하며 라이다 결과로 관성 센서의 편향을 갱신한다. [PDF 2쪽](https://arxiv.org/pdf/2007.00258v3#page=2) · [PDF 3쪽](https://arxiv.org/pdf/2007.00258v3#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2007.00258v3#page=4)
- 여러 플랫폼에서 모은 실외 순서열로 궤적·지도 품질을 비교하고 루프 폐쇄 및 위치 관측이 누적 오차에 미치는 영향을 보여준다. [PDF 5쪽](https://arxiv.org/pdf/2007.00258v3#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2007.00258v3#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2007.00258v3#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2007.00258v3#page=8)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (Abstract)이다.
