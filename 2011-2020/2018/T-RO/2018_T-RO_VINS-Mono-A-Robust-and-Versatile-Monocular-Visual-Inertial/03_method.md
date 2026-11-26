# Method - VINS-Mono: A Robust and Versatile Monocular Visual-Inertial State Estimator

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1708.03852; PDF retrieval source: https://arxiv.org/pdf/1708.03852. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION)): To this end, we ignore estimating the drift-free roll and pitch states, and only perform 4-DOF pose graph optimization.

## Method Body Digest

- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** To this end, we ignore estimating the drift-free roll and pitch states, and only perform 4-DOF pose graph optimization.
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** Pose graph optimization and relocalization (Sect.
- **네 자유도 자세 그래프.** 식 (29)는 위치와 요각을 변수로 순차 간선의 제곱 잔차와 루프 폐쇄 간선에 Huber 함수를 적용한 제곱 잔차를 합해 최소화한다. [PDF 11쪽](https://arxiv.org/pdf/1708.03852v1#page=11)
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** All keyframes with loop closure constraints will be kept, while other keyframes that are either too close or have very similar orientations to its neighbors ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Outdoor experimental results of the proposed monocular visual-inertial state estimator.
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2 To address all these issues, we propose VINS-Mono, a robust and versatile monocular visual-inertial state estimator.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables navigation tasks that require metric state estimates.
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** After relocalization, the local sliding window shifts and aligns with past poses.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** 2 To address all these issues, we propose VINS-Mono, a robust and versatile monocular visual-inertial state estimator.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables navigation tasks that require metric state estimates.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This enables robust and accurate relocalization with minimum computation overhead.

## Source Evidence Cues

- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** To this end, we ignore estimating the drift-free roll and pitch states, and only perform 4-DOF pose graph optimization.
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** Pose graph optimization and relocalization (Sect.
- **Detected method headings:** none reliably recovered

## Pipeline

단안 영상 특징과 IMU 각속도·가속도 → 슬라이딩 윈도의 포즈·속도·관성 편향 → 추정 궤적과 비행 제어기에 보내는 상태. [방법·평가의 원문 근거](./01_overview.md#observation-state-and-output-interface)

## Objective / Update Rule

- **네 자유도 자세 그래프.** 식 (29)는 위치와 요각을 변수로 순차 간선의 제곱 잔차와 루프 폐쇄 간선에 Huber 함수를 적용한 제곱 잔차를 합해 최소화한다. [PDF 11쪽](https://arxiv.org/pdf/1708.03852v1#page=11)
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** All keyframes with loop closure constraints will be kept, while other keyframes that are either too close or have very similar orientations to its neighbors ...
- **Formal bridge:** 단안 영상 특징과 IMU 각속도·가속도 → 슬라이딩 윈도의 포즈·속도·관성 편향 → 추정 궤적과 비행 제어기에 보내는 상태.
- **Equation/algorithm anchors:** p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Outdoor, experimental, monocular, visual-inertial, state, estimator, address, issues, VINS-Mono, robust, versatile, summarize, contributions, follow | 단안 영상 특징과 IMU 각속도·가속도 | body cue; exact tensor/frame verify |
| State/latent | Outdoor, experimental, monocular, visual-inertial, state, estimator, address, issues, VINS-Mono, robust | 슬라이딩 윈도의 포즈·속도·관성 편향 | body cue; notation verify |
| Action/output | address, issues, VINS-Mono, robust, versatile, monocular, visual-inertial, state, estimator, enables | 추정 궤적과 비행 제어기에 보내는 상태 | body cue; unit/decoder verify |
| Objective/constraint | whole, graph, sequential, edges, loop, closure, optimized, minimizing, following, cost | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** Outdoor experimental results of the proposed monocular visual-inertial state estimator.
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2 To address all these issues, we propose VINS-Mono, a robust and versatile monocular visual-inertial state estimator.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To this end, we summarize our contributions as follow: • A robust initialization procedure that is able to bootstrap the system from unknown initial states. ...
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** To this end, we ignore estimating the drift-free roll and pitch states, and only perform 4-DOF pose graph optimization.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables navigation tasks that require metric state estimates.
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** After relocalization, the local sliding window shifts and aligns with past poses.
- **Normalized interface:** observation=단안 영상 특징과 IMU 각속도·가속도; state=슬라이딩 윈도의 포즈·속도·관성 편향; output/action=추정 궤적과 비행 제어기에 보내는 상태.

## Temporal and Runtime Contract

| Contract | PDF body cue | Unresolved detail |
|---|---|---|
| Horizon | The datasets are collected onboard a micro aerial vehicle, which contains stereo images (Aptina MT9V034 global shutter, WVGA monochrome, 20 FPS), synchronized ... | episode/sequence/action-chunk boundary |
| Rate / latency | In this large-scale test, We set the keyframe database size to 2000 in order to provide sufficient loop information and achieve real-time ... | Hz/fps, inference time and control rate |
| Memory | not recovered | window and reset |
| Compute | The datasets are collected onboard a micro aerial vehicle, which contains stereo images (Aptina MT9V034 global shutter, WVGA monochrome, 20 FPS), synchronized ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

## Method-Specific Formal Details

- **Body-defined terms:** ignore, estimating, drift-free, roll, pitch, states, only, perform, DOF, pose, graph, optimization, relocalization, Sect, whole, sequential, edges, loop, closure, optimized.
- **Relevant PDF headings:** not reliably recovered.

## Evaluation Link

| 평가 근거 | 원문에서 추출한 내용 | 원문 위치 |
|---|---|---|
| 원문 대조 | We then test our system in the indoor environment to evaluate the performance in repetitive scenes. | p. 11 (IX. EXPERIMENTAL RESULTS), p. 11 (IX. EXPERIMENTAL RESULTS) |
| 원문 대조 | In the first experiment, we compare the proposed algorithm with another state-of-the-art algorithm on public datasets. | p. 11 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS) |
| 원문 대조 | In this large-scale test, We set the keyframe database size to 2000 in order to provide sufficient loop information and achieve real-time ... | p. 14 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS) |

## Failure and Ablation Link

- **p. 12 / IX. EXPERIMENTAL RESULTS - extractive body cue:** Since the movement is smooth without much yaw angle change in this sequence, only position drift occurs.
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** (b) Trajectory of VINS-Mono without loop closure.
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** 17(b) is the VIO-only result from proposed method without loop closure.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7. An illustration of our marginalization strategy. If the second latest frame is a keyframe, we will keep it in the window, and marginalize ...
- **p. 15 / IX. EXPERIMENTAL RESULTS - extractive body cue:** Final drift is 0.18m. estimator crash caused by unstable feature tracking or active failure detection and recovery.
- **p. 16 / X. CONCLUSION AND FUTURE WORK - extractive body cue:** Our approach features both state-ofthe-art and novel solutions to IMU pre-integration, estimator initialization and failure recovery, online extrinsic calibration, tightly-coupled visual-inertial odometry, relocalization, and efficient ...
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** We cannot see the shape of stairs in the red block.

## Reproduction Checklist

[공통 검토 기준](../../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), objective p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), temporal p. 11 (IX. EXPERIMENTAL RESULTS), p. 14 (IX. EXPERIMENTAL RESULTS), p. 2 (II. RELATED WORK), p. 2 (I. INTRODUCTION), p. 12 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS).
