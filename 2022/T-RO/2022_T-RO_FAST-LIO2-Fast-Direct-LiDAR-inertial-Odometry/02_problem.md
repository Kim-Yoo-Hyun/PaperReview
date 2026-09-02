# Problem - FAST-LIO2: Fast Direct LiDAR-inertial Odometry

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2107.06829; PDF retrieval source: https://arxiv.org/pdf/2107.06829. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

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
| Target problem | However, efficient and accurate LiDAR odometry and mapping are still challenging problems: 1) Current LiDAR sensors produce a large amount of 3D ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | To prevent the size of the map from going unbound, only map points in a large local region of length L around ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | prevent, size, going, unbound, only, points, large, local, region, length | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | operation, defined, continuous, kinematic, model, discretized, IMU, sampling | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: prevent, size, going, unbound, only, points, large, local, region, length | p. 6 (V. MAPPING), p. 1 (I. INTRODUCTION), p. 4 (IV. STATE ESTIMATION) |
| Decision / output variable | path/waypoint/velocity; body terms: More, specifically, contributions, follows, develop, incremental, tree, data | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Besides, efficient, nearest, neighbor, search, data, structure, supports | p. 5 (IV. STATE ESTIMATION), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. SYSTEM OVERVIEW), p. 5 (IV. STATE ESTIMATION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (I. INTRODUCTION), p. 8 (9 Algorithm End), p. 8 (24 End Function) |
| Success / guarantee | goal reach with collision-free execution | p. 10 (VI. BENCHMARK RESULTS), p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 10 (VI. BENCHMARK RESULTS) |

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

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (V. MAPPING), p. 1 (I. INTRODUCTION), p. 4 (IV. STATE ESTIMATION), p. 4 (III. SYSTEM OVERVIEW). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 6 (V. MAPPING), p. 1 (I. INTRODUCTION), p. 4 (IV. STATE ESTIMATION), p. 4 (III. SYSTEM OVERVIEW), objective p. 5 (IV. STATE ESTIMATION), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. SYSTEM OVERVIEW), p. 5 (IV. STATE ESTIMATION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
