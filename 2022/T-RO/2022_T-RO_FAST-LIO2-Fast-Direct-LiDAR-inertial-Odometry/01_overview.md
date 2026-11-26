# FAST-LIO2: Fast Direct LiDAR-inertial Odometry

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2107.06829.
> PDF retrieval source: https://arxiv.org/pdf/2107.06829. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / T-RO
- Authors: Wei Xu, Yixi Cai, Dongjiao He, Jiarong Lin, Fu Zhang
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics, state estimation, LiDAR-inertial odometry, SLAM, direct registration, real-time
- Official paper: https://arxiv.org/abs/2107.06829
- Full-text retrieval: https://arxiv.org/pdf/2107.06829
- Code/Project: https://github.com/hku-mars/FAST_LIO
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://arxiv.org/pdf/2107.06829v1) 기준이다.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

FAST-LIO2는 라이다 원시 점을 국소 지도에 직접 정합하고 관성 측정과 함께 필터링해 실시간 위치·자세를 추정한다. [PDF 1쪽](https://arxiv.org/pdf/2107.06829v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper presents FAST-LIO2: a fast, robust, and versatile LiDAR-inertial odometry framework.
- **p. 1 / Abstract - extractive body cue:** Building on a highly efficient tightly-coupled iterated Kalman filter, FASTLIO2 has two key novelties that allow fast, robust, and accurate LiDAR navigation (and mapping).
- **p. 1 / Abstract - extractive body cue:** The first one is directly registering raw points to the map (and subsequently update the map, i.e., mapping) without extracting features.
- **p. 1 / Abstract - extractive body cue:** This enables the exploitation of subtle features in the environment and hence increases the accuracy.
- **p. 1 / Abstract - extractive body cue:** The elimination of a hand-engineered feature extraction module also makes it naturally adaptable to emerging LiDARs of different scanning patterns; The second main novelty is ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, efficient and accurate LiDAR odometry and mapping are still challenging problems: 1) Current LiDAR sensors produce a large amount of 3D points from hundreds ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** On the other hand, real-time dense mapping [5]-[8] based on visual sensors at high resolution and accuracy with only the robot onboard computation resources is ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** More specifically, our contributions are as follows: 1) We develop an incremental k-d tree data structure, ikd-Tree, to represent a large dense point cloud map ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2) Allowed by the increased computation efficiency of ikd-Tree, we directly register raw points to the map, which enables more accurate and reliable scan registration ...
- **p. 1 / Abstract - extractive body cue:** The elimination of a hand-engineered feature extraction module also makes it naturally adaptable to emerging LiDARs of different scanning patterns; The second main novelty is ...
- **p. 4 / IV. STATE ESTIMATION - extractive body cue:** Kinematic Model We first derive the system model, which consists of a state transition model and a measurement model.
- **p. 1 / Abstract - extractive body cue:** This enables the exploitation of subtle features in the environment and hence increases the accuracy.
- **p. 7 / V. MAPPING - extractive body cue:** For a given point p in {G¯pj} from the state estimation module (see Algorithm 1) and downsample resolution l, the algorithm partitions the space evenly ...
- **원문 대조:** 첫 IMU frame을 전역 좌표계 G로 두며, LiDAR–IMU 외부 파라미터를 회전과 병진의 쌍 I_T_L=(I_R_L, I_p_L)로 나타낸다. ([PDF p. 4](https://arxiv.org/pdf/2107.06829#page=4), §IV-A.1 State Transition Model).
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, the performance of the feature extraction module is easily influenced by the environment.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To prevent the size of the map from going unbound, only map points in a large local region of length L around the LiDAR current position are maintained Algorithm 1: State Estimation ... | 원시 LiDAR 스캔과 IMU 가속도·각속도 | p. 6 (V. MAPPING), p. 1 (I. INTRODUCTION) |
| State/latent | prevent, size, going, unbound, only, points, large, local, region, length, around, LiDAR | 관성 상태와 로컬 점군 지도 | p. 6 (V. MAPPING), p. 1 (I. INTRODUCTION), p. 4 (IV. STATE ESTIMATION) |
| Output/action | The localization provides state feedback for the robot onboard controllers, while the dense 3D map provides necessary information about the environment (i.e., free space and obstacles) for trajectory planning. | 추정한 자세·위치와 갱신된 점군 지도 | p. 1 (I. INTRODUCTION), p. 4 (IV. STATE ESTIMATION), p. 4 (III. SYSTEM OVERVIEW) |
| Objective/outcome | Besides efficient nearest neighbor search, the new data structure supports incremental map update (i.e., point insertion, on-tree downsampling, points delete) and dynamic re-balancing at minimal computation cost. | 궤적 오차와 스캔당 추정·지도 갱신 시간 | p. 2 (I. INTRODUCTION), p. 5 (IV. STATE ESTIMATION), p. 1 (I. INTRODUCTION) |

## Main Claims and Actual Contribution

- 반복 칼만 필터에 점과 지도 사이의 거리 잔차를 넣어 별도 기하 특징 추출 없이 상태를 갱신한다. [PDF 4쪽](https://arxiv.org/pdf/2107.06829v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2107.06829v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2107.06829v1#page=6)
- 점 삽입·삭제와 재균형을 지원하는 증분 k-d 트리로 지도를 유지하고 저장 구조 비용 및 주행 순서열의 위치 오차를 평가했다. [PDF 7쪽](https://arxiv.org/pdf/2107.06829v1#page=7) · [PDF 9쪽](https://arxiv.org/pdf/2107.06829v1#page=9) · [PDF 10쪽](https://arxiv.org/pdf/2107.06829v1#page=10) · [PDF 12쪽](https://arxiv.org/pdf/2107.06829v1#page=12)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 10 (VI. BENCHMARK RESULTS) |
| Embodiment/environment | 11 TABLE II THE DATASETS FOR BENCHMARK LiDAR IMU Type Line Type Rate lili Solid-state - 6-axis | hardware/simulator version and reset protocol | p. 11 (VI. BENCHMARK RESULTS), p. 14 (VII. REAL-WORLD EXPERIMENTS) |
| Dataset/benchmark | Private Dataset 1) Detail Evaluation of Processing Time: In order to validate the real-time performance of FAST-LIO2, we use the handheld platform to collect a sequence at 100 Hz scan rate in ... | role, split, size and leakage | p. 11 (VI. BENCHMARK RESULTS), p. 14 (VII. REAL-WORLD EXPERIMENTS), p. 14 (VII. REAL-WORLD EXPERIMENTS), p. 16 (VII. REAL-WORLD EXPERIMENTS) |
| Metric | In this section, extensive experiments in terms of accuracy, robustness, and computational efficiency are conducted on various open datasets. | definition, denominator, direction and uncertainty | p. 10 (VI. BENCHMARK RESULTS), p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 10 (VI. BENCHMARK RESULTS) |
| Baseline/ablation | For example, our prior work [63] demonstrated the application of FAST-LIO2 on an autonomous UAV avoiding dynamic small objects (down to 9 mm) in complex indoor and outdoor environments. | fair input/data/compute/action matching | p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 12 (Figure/Table caption), p. 4 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 13 / 100 Hz - extractive body cue:** LIO-SAM shows good performance in its own sequences liosam 2 and liosam 3 but cannot keep it on other sequences such as ulhk.
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** It should be noted that the LILI-OM also supports solid-state LiDAR, but it fails in this data since its feature extraction module produces too few ...
- **p. 15 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** As can be seen, the averaging mapping time per scan for FAST-LIO exceeds 10 ms hence cannot be processed in real-time for this large scene.
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** Since FAST-LIO2 does not extract features, it is naturally adaptable to this new LiDAR.
- **p. 16 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** The occasional timeout usually does not affect a subsequent controller since the IMU propagated state estimate could be used during this short period.
- **p. 10 / VI. BENCHMARK RESULTS - extractive body cue:** In this section, extensive experiments in terms of accuracy, robustness, and computational efficiency are conducted on various open datasets.
- **p. 13 / 100 Hz - extractive body cue:** The LINS performs worse than LIO-SAM in liosam and ulhk datasets and failed in liosam 2 (garden sequence from [30]) because the two sequences are ...

## 검색 태그 근거

원시 LiDAR 점을 로컬 지도에 직접 정합하고 IMU로 전파한 상태를 반복 칼만 필터로 갱신한다. 항공·지상 이동 자료에서 궤적 오차와 처리 시간을 평가한다. 장애물 회피는 추정치를 활용한 선행 응용으로 인용한다. [원문 4쪽](https://arxiv.org/pdf/2107.06829v1#page=4) · [원문 14쪽](https://arxiv.org/pdf/2107.06829v1#page=14)

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (IV. STATE ESTIMATION), p. 7 (V. MAPPING)이다.
