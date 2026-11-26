# Problem - FAST-LIO2: Fast Direct LiDAR-inertial Odometry

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2107.06829; PDF retrieval source: https://arxiv.org/pdf/2107.06829. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): However, efficient and accurate LiDAR odometry and mapping are still challenging problems: 1) Current LiDAR sensors produce a large amount of 3D points from hundreds of thousands to millions per ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** This paper presents FAST-LIO2: a fast, robust, and versatile LiDAR-inertial odometry framework.
- **p. 1 / Abstract - extractive body cue:** Building on a highly efficient tightly-coupled iterated Kalman filter, FASTLIO2 has two key novelties that allow fast, robust, and accurate LiDAR navigation (and mapping).
- **p. 1 / Abstract - extractive body cue:** The first one is directly registering raw points to the map (and subsequently update the map, i.e., mapping) without extracting features.
- **p. 1 / Abstract - extractive body cue:** This enables the exploitation of subtle features in the environment and hence increases the accuracy.
- **p. 1 / Abstract - extractive body cue:** The elimination of a hand-engineered feature extraction module also makes it naturally adaptable to emerging LiDARs of different scanning patterns; The second main novelty is ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, efficient and accurate LiDAR odometry and mapping are still challenging problems: 1) Current LiDAR sensors produce a large amount of 3D points from hundreds ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** On the other hand, real-time dense mapping [5]-[8] based on visual sensors at high resolution and accuracy with only the robot onboard computation resources is ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, efficient and accurate LiDAR odometry and mapping are still challenging problems: 1) Current LiDAR sensors produce a large amount of 3D ... | 실제 이동 플랫폼의 LiDAR–관성 오도메트리와 지도 작성 | body wording is the source claim |
| Observation / input | To prevent the size of the map from going unbound, only map points in a large local region of length L around ... | 원시 LiDAR 스캔과 IMU 가속도·각속도 | exact sensor/frame/preprocessing from PDF body |
| State / latent | prevent, size, going, unbound, only, points, large, local, region, length | 관성 상태와 로컬 점군 지도 | notation and tensor shape require body check |
| Output / action | operation, defined, continuous, kinematic, model, discretized, IMU, sampling | 추정한 자세·위치와 갱신된 점군 지도 | exact unit/frame/decoder require body check |
| Target outcome | 궤적 추정 정확도와 스캔당 처리 시간 | 궤적 오차와 스캔당 추정·지도 갱신 시간 | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | 원시 LiDAR·IMU 측정과 이전 관성 상태; body terms: prevent, size, going, unbound, only, points, large, local, region, length | p. 6 (V. MAPPING), p. 1 (I. INTRODUCTION), p. 4 (IV. STATE ESTIMATION) |
| Decision / output variable | 관성 상태 추정치와 점군 지도; body terms: More, specifically, contributions, follows, develop, incremental, tree, data | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract) |
| Objective / loss / cost | 점–평면 측정 잔차와 관성 사전 추정의 결합; cue terms: Besides, efficient, nearest, neighbor, search, data, structure, supports | p. 5 (IV. STATE ESTIMATION), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. SYSTEM OVERVIEW), p. 5 (IV. STATE ESTIMATION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (I. INTRODUCTION), p. 8 (9 Algorithm End), p. 8 (24 End Function) |
| Success / guarantee | 궤적 추정 정확도와 스캔당 처리 시간 | p. 10 (VI. BENCHMARK RESULTS), p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 10 (VI. BENCHMARK RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** On the other hand, real-time dense mapping [5]-[8] based on visual sensors at high resolution and accuracy with only the robot onboard computation resources is ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Experiments on 18 sequences of various sizes show that ikdTree achieves superior performance against existing dynamic data structures (octree, R∗-tree, nanoflann k-d tree) in the ...

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 4 (IV. STATE ESTIMATION), p. 1 (Abstract)): More specifically, our contributions are as follows: 1) We develop an incremental k-d tree data structure, ikd-Tree, to represent a large dense point cloud map efficiently.

- **p. 2 / I. INTRODUCTION - extractive body cue:** 2) Allowed by the increased computation efficiency of ikd-Tree, we directly register raw points to the map, which enables more accurate and reliable scan registration ...
- **p. 1 / Abstract - extractive body cue:** The elimination of a hand-engineered feature extraction module also makes it naturally adaptable to emerging LiDARs of different scanning patterns; The second main novelty is ...
- **p. 4 / IV. STATE ESTIMATION - extractive body cue:** Kinematic Model We first derive the system model, which consists of a state transition model and a measurement model.
- **p. 1 / Abstract - extractive body cue:** This enables the exploitation of subtle features in the environment and hence increases the accuracy.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 13 | LIO-SAM shows good performance in its own sequences liosam 2 and liosam 3 but cannot keep it on ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | It should be noted that the LILI-OM also supports solid-state LiDAR, but it fails in this data since ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 15 | As can be seen, the averaging mapping time per scan for FAST-LIO exceeds 10 ms hence cannot be ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Since FAST-LIO2 does not extract features, it is naturally adaptable to this new LiDAR. | reported limitation/failure wording; scope must be verified |

## Position in the Robotics Loop

로봇의 관측을 자세·위치 및 로컬 지도로 바꾸는 상태 추정 단계다. 그림 1과 IV–V절에서 실제 출력과 지도 갱신을 확인할 수 있다.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 6 (V. MAPPING), p. 1 (I. INTRODUCTION), p. 4 (IV. STATE ESTIMATION), p. 4 (III. SYSTEM OVERVIEW), objective p. 5 (IV. STATE ESTIMATION), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. SYSTEM OVERVIEW), p. 5 (IV. STATE ESTIMATION).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)
