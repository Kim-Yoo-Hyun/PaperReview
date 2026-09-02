# Method - VINS-Mono: A Robust and Versatile Monocular Visual-Inertial State Estimator

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1708.03852; PDF retrieval source: https://arxiv.org/pdf/1708.03852. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION)): To this end, we ignore estimating the drift-free roll and pitch states, and only perform 4-DOF pose graph optimization.

## Method Body Digest

- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** To this end, we ignore estimating the drift-free roll and pitch states, and only perform 4-DOF pose graph optimization.
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** Pose graph optimization and relocalization (Sect.
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** The whole graph of sequential edges and loop closure edges are optimized by minimizing the following cost function: min p,ψ    X (i,j)∈S ...
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

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | To this end, we ignore estimating the drift-free roll and pitch states, and only perform 4-DOF pose graph optimization. | p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Pose graph optimization and relocalization (Sect. | p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | To this end, we ignore estimating the drift-free roll and pitch states, and only perform 4-DOF pose graph optimization. | p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** The whole graph of sequential edges and loop closure edges are optimized by minimizing the following cost function: min p,ψ    X (i,j)∈S ...
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** All keyframes with loop closure constraints will be kept, while other keyframes that are either too close or have very similar orientations to its neighbors ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Outdoor, experimental, monocular, visual-inertial, state, estimator, address, issues, VINS-Mono, robust, versatile, summarize, contributions, follow | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Outdoor, experimental, monocular, visual-inertial, state, estimator, address, issues, VINS-Mono, robust | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | address, issues, VINS-Mono, robust, versatile, monocular, visual-inertial, state, estimator, enables | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | whole, graph, sequential, edges, loop, closure, optimized, minimizing, following, cost | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** Outdoor experimental results of the proposed monocular visual-inertial state estimator.
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2 To address all these issues, we propose VINS-Mono, a robust and versatile monocular visual-inertial state estimator.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To this end, we summarize our contributions as follow: • A robust initialization procedure that is able to bootstrap the system from unknown initial states. ...
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** To this end, we ignore estimating the drift-free roll and pitch states, and only perform 4-DOF pose graph optimization.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables navigation tasks that require metric state estimates.
- **p. 11 / VIII. GLOBAL POSE GRAPH OPTIMIZATION - extractive body cue:** After relocalization, the local sliding window shifts and aligns with past poses.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | The datasets are collected onboard a micro aerial vehicle, which contains stereo images (Aptina MT9V034 global shutter, WVGA monochrome, 20 FPS), synchronized ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | In this large-scale test, We set the keyframe database size to 2000 in order to provide sufficient loop information and achieve real-time ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | The datasets are collected onboard a micro aerial vehicle, which contains stereo images (Aptina MT9V034 global shutter, WVGA monochrome, 20 FPS), synchronized ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** ignore, estimating, drift-free, roll, pitch, states, only, perform, DOF, pose, graph, optimization, relocalization, Sect, whole, sequential, edges, loop, closure, optimized.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We then test our system in the indoor environment to evaluate the performance in repetitive scenes. | p. 11 (IX. EXPERIMENTAL RESULTS), p. 11 (IX. EXPERIMENTAL RESULTS) |
| Global / local decision | In the first experiment, we compare the proposed algorithm with another state-of-the-art algorithm on public datasets. | p. 11 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS) |
| Motion execution / recovery | In this large-scale test, We set the keyframe database size to 2000 in order to provide sufficient loop information and achieve real-time ... | p. 14 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS) |

## Failure and Ablation Link

- **p. 12 / IX. EXPERIMENTAL RESULTS - extractive body cue:** Since the movement is smooth without much yaw angle change in this sequence, only position drift occurs.
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** (b) Trajectory of VINS-Mono without loop closure.
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** 17(b) is the VIO-only result from proposed method without loop closure.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7. An illustration of our marginalization strategy. If the second latest frame is a keyframe, we will keep it in the window, and marginalize ...
- **p. 15 / IX. EXPERIMENTAL RESULTS - extractive body cue:** Final drift is 0.18m. estimator crash caused by unstable feature tracking or active failure detection and recovery.
- **p. 16 / X. CONCLUSION AND FUTURE WORK - extractive body cue:** Our approach features both state-ofthe-art and novel solutions to IMU pre-integration, estimator initialization and failure recovery, online extrinsic calibration, tightly-coupled visual-inertial odometry, relocalization, and efficient ...
- **p. 13 / IX. EXPERIMENTAL RESULTS - extractive body cue:** We cannot see the shape of stairs in the red block.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), objective p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), p. 11 (VIII. GLOBAL POSE GRAPH OPTIMIZATION), temporal p. 11 (IX. EXPERIMENTAL RESULTS), p. 14 (IX. EXPERIMENTAL RESULTS), p. 2 (II. RELATED WORK), p. 2 (I. INTRODUCTION), p. 12 (IX. EXPERIMENTAL RESULTS), p. 12 (IX. EXPERIMENTAL RESULTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
