# VINS-Mono: A Robust and Versatile Monocular Visual-Inertial State Estimator

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1708.03852.
> PDF retrieval source: https://arxiv.org/pdf/1708.03852. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / T-RO
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics, state estimation, visual-inertial odometry, SLAM, sensor fusion, flight control
- Official paper: https://arxiv.org/abs/1708.03852
- Full-text retrieval: https://arxiv.org/pdf/1708.03852
- Code/Project: https://github.com/HKUST-Aerial-Robotics/VINS-Mono
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 This implies that monocular VINS estimators cannot start from a stationary condition, but rather launch from an unknown moving state.를 문제로 두고, 2 To address all these issues, we propose VINS-Mono, a robust and versatile monocular visual-inertial state estimator.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A monocular visual-inertial system (VINS), consisting of a camera and a low-cost inertial measurement unit (IMU), forms the minimum sensor suite for metric six degreesof-freedom ...
- **p. 1 / Abstract - extractive body cue:** However, the lack of direct distance measurement poses significant challenges in terms of IMU processing, estimator initialization, extrinsic calibration, and nonlinear optimization.
- **p. 1 / Abstract - extractive body cue:** In this work, we present VINSMono: a robust and versatile monocular visual-inertial state estimator.
- **p. 1 / Abstract - extractive body cue:** Our approach starts with a robust procedure for estimator initialization and failure recovery.
- **p. 1 / Abstract - extractive body cue:** A tightly-coupled, nonlinear optimization-based method is used to obtain high accuracy visual-inertial odometry by fusing pre-integrated IMU measurements and feature observations.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This implies that monocular VINS estimators cannot start from a stationary condition, but rather launch from an unknown moving state.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Also recognizing the fact that visual-inertial systems are highly nonlinear, we see significant challenges in terms of estimator initialization.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** 2 To address all these issues, we propose VINS-Mono, a robust and versatile monocular visual-inertial state estimator.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables navigation tasks that require metric state estimates.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This enables robust and accurate relocalization with minimum computation overhead.
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** This enables immediate use of the most optimized pose graph for relocalization whenever it becomes available.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Finally, in order to eliminate long-term drift within an acceptable processing window, a complete system that includes visual-inertial odometry, loop detection, relocalization, and global optimization ...
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** To this end, we ignore estimating the drift-free roll and pitch states, and only perform 4-DOF pose graph optimization.
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** Pose graph optimization and relocalization (Sect.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Outdoor experimental results of the proposed monocular visual-inertial state estimator. | camera/depth stream, pose, map와 language goal | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| State/latent | Outdoor, experimental, monocular, visual-inertial, state, estimator, address, issues, VINS-Mono, robust, versatile, summarize | robot pose, free-space/semantic map와 local goal | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/action | 2 To address all these issues, we propose VINS-Mono, a robust and versatile monocular visual-inertial state estimator. | collision-free trajectory 또는 velocity command | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION) |
| Objective/outcome | The whole graph of sequential edges and loop closure edges are optimized by minimizing the following cost function: min p,ψ    X (i,j)∈S ∥ri,j∥2 + X (i,j)∈L ρ(∥ri,j∥2)   ... | goal reach, safety, localization error와 replanning latency | p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** 2 To address all these issues, we propose VINS-Mono, a robust and versatile monocular visual-inertial state estimator.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables navigation tasks that require metric state estimates.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This enables robust and accurate relocalization with minimum computation overhead.
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** This enables immediate use of the most optimized pose graph for relocalization whenever it becomes available.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Finally, in order to eliminate long-term drift within an acceptable processing window, a complete system that includes visual-inertial odometry, loop detection, relocalization, and global optimization ...
- **p. 14 / IX. EXPERIMENTAL RESULTS - extractive body cue:** In this large-scale test, We set the keyframe database size to 2000 in order to provide sufficient loop information and achieve real-time performance.
- **p. 12 / IX. EXPERIMENTAL RESULTS - extractive body cue:** However, VINS-Mono outperforms OKVIS at the system level.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. A block diagram illustrating the full pipeline of the proposed monocular visual-inertial state estimator. order to avoid repeated IMU re-integration This technique was ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 14 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS) |
| Embodiment/environment | We then test our system in the indoor environment to evaluate the performance in repetitive scenes. | hardware/simulator version and reset protocol | p. 11 (IX. EXPERIMENTAL RESULTS), p. 11 (IX. EXPERIMENTAL RESULTS) |
| Dataset/benchmark | The robot follows the trajectory four times. | role, split, size and leakage | p. 11 (IX. EXPERIMENTAL RESULTS), p. 11 (IX. EXPERIMENTAL RESULTS), p. 15 (IX. EXPERIMENTAL RESULTS), p. 15 (IX. EXPERIMENTAL RESULTS) |
| Metric | The x, y, z error versus time, and the translation error versus distance are shown in Fig. | definition, denominator, direction and uncertainty | p. 12 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS), p. 13 (IX. EXPERIMENTAL RESULTS) |
| Baseline/ablation | In the first experiment, we compare the proposed algorithm with another state-of-the-art algorithm on public datasets. | fair input/data/compute/action matching | p. 11 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 15 / IX. EXPERIMENTAL RESULTS - extractive body cue:** Final drift is 0.18m. estimator crash caused by unstable feature tracking or active failure detection and recovery.
- **p. 16 / X. CONCLUSION AND FUTURE WORK - extractive body cue:** Our approach features both state-ofthe-art and novel solutions to IMU pre-integration, estimator initialization and failure recovery, online extrinsic calibration, tightly-coupled visual-inertial odometry, relocalization, and efficient ...
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** We cannot see the shape of stairs in the red block.
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** When we went up stairs, OKVIS shows unstable feature tracking, resulting in bad estimation.
- **p. 16 / X. CONCLUSION AND FUTURE WORK - extractive body cue:** In this paper, we propose a robust and versatile monocular visual-inertial estimator.
- **p. 12 / IX. EXPERIMENTAL RESULTS - extractive body cue:** Our system is complete with robust initialization and loop closure.
- **p. 14 / IX. EXPERIMENTAL RESULTS - extractive body cue:** Application II: Mobile Device We port VINS-Mono to mobile devices and present a simple AR application to showcase its accuracy and robustness.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 This implies that monocular VINS estimators cannot start from a stationary condition, but rather launch from an unknown moving state.를 문제로 두고, 2 To address all these issues, we propose VINS-Mono, a robust and versatile monocular visual-inertial state estimator.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), p. 14 (IX. EXPERIMENTAL RESULTS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
