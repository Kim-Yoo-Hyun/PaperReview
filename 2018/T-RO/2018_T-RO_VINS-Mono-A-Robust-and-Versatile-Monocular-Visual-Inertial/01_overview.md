# VINS-Mono: A Robust and Versatile Monocular Visual-Inertial State Estimator

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1708.03852.
> PDF retrieval source: https://arxiv.org/pdf/1708.03852. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / T-RO
- Authors: Tong Qin, Peiliang Li, Shaojie Shen
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics, state estimation, visual-inertial odometry, SLAM, sensor fusion, flight control
- Official paper: https://arxiv.org/abs/1708.03852
- Full-text retrieval: https://arxiv.org/pdf/1708.03852
- Code/Project: https://github.com/HKUST-Aerial-Robotics/VINS-Mono
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://arxiv.org/pdf/1708.03852v1) 기준이다.

## Why This Paper Is Here

VINS-Mono는 단안 영상 특징과 관성 센서 측정을 결합해 이동체의 미터 단위 자세·위치를 추정하고 재방문 정보를 이용해 누적 오차를 줄인다. [PDF 1쪽](https://arxiv.org/pdf/1708.03852v1#page=1)

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
| Objective/outcome | 순차 간선의 제곱 잔차와 루프 폐쇄 간선의 강건 비용을 합해 키프레임의 위치와 요각을 최적화한다. | 전역 궤적의 정합과 드리프트 | 식 (29) [PDF 11쪽](https://arxiv.org/pdf/1708.03852v1#page=11) |

## Main Claims and Actual Contribution

- 관성 측정을 사전적분하고 영상과 관성의 초기 정렬을 거쳐 슬라이딩 윈도에서 상태를 함께 최적화한다. [PDF 4쪽](https://arxiv.org/pdf/1708.03852v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/1708.03852v1#page=5) · [PDF 7쪽](https://arxiv.org/pdf/1708.03852v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/1708.03852v1#page=8)
- 재지역화로 얻은 루프 제약과 순차 제약을 네 자유도의 자세 그래프에 결합하고 궤적 추정 결과를 비교했다. [PDF 10쪽](https://arxiv.org/pdf/1708.03852v1#page=10) · [PDF 11쪽](https://arxiv.org/pdf/1708.03852v1#page=11) · [PDF 12쪽](https://arxiv.org/pdf/1708.03852v1#page=12)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), p. 14 (IX. EXPERIMENTAL RESULTS)이다.
