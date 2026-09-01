# Method - PTAM: Parallel Tracking and Mapping for Small AR Workspaces

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.robots.ox.ac.uk/~gk/PTAM/; PDF retrieval source: https://www.robots.ox.ac.uk/~gk/publications/KleinMurray2007ISMAR.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3. A small number (50) of the coarsest-scale features are), p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 3 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are)): If the fraction falls below an even lower threshold for more than a few frames (during which the motion model might successfully bridge untrackable frames) then tracking is considered lost, ...

## Method Body Digest

- **p. 4 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** If the fraction falls below an even lower threshold for more than a few frames (during which the motion model might successfully bridge untrackable frames) ...
- **p. 1 / ABSTRACT - extractive PDF cue:** While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track a hand-held camera ...
- **p. 1 / ABSTRACT - extractive PDF cue:** We propose to split tracking and mapping into two separate tasks, processed in parallel threads on a dual-core computer: one thread deals with the task ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** The map consists of a collection of M point features located in a world coordinate frame W.
- **p. 3 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** We use a decaying velocity model; this is similar to a simple alpha-beta constant velocity model, but lacking any new measurements, the estimated camera slows ...
- **p. 5 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** Bundle adjustment iteratively adjusts the map so as to minimise the robust objective function: ˘ {µ2..µN}, {p′ 1..p′ M} ¯ = argmin {{µ},{p}} N X ...
- **p. 4 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** For this reason, the tracking system estimates the quality of tracking at every frame, using the fraction of feature observations which have been successful.
- **p. 4 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** The pose update is computed iteratively by minimising a robust objective function of the reprojection error: µ′ = argmin µ X j∈S Obj „/ej/ σj ...

## Design Rationale

- **p. 1 / ABSTRACT - extractive PDF cue:** While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track a hand-held camera ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** The map consists of a collection of M point features located in a world coordinate frame W.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** While we adopt the stereo initialisation, and occasionally make use of local bundle updates, our method is different in that we attempt to build a ...

## Source Evidence Cues

- **p. 4 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** If the fraction falls below an even lower threshold for more than a few frames (during which the motion model might successfully bridge untrackable frames) ...
- **p. 1 / ABSTRACT - extractive PDF cue:** While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track a hand-held camera ...
- **p. 1 / ABSTRACT - extractive PDF cue:** We propose to split tracking and mapping into two separate tasks, processed in parallel threads on a dual-core computer: one thread deals with the task ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** The map consists of a collection of M point features located in a world coordinate frame W.
- **p. 3 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** We use a decaying velocity model; this is similar to a simple alpha-beta constant velocity model, but lacking any new measurements, the estimated camera slows ...
- **p. 5 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** Bundle adjustment iteratively adjusts the map so as to minimise the robust objective function: ˘ {µ2..µN}, {p′ 1..p′ M} ¯ = argmin {{µ},{p}} N X ...
- **p. 4 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** For this reason, the tracking system estimates the quality of tracking at every frame, using the fraction of feature observations which have been successful.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | If the fraction falls below an even lower threshold for more than a few frames (during which the motion model might successfully ... | p. 4 (3. A small number (50) of the coarsest-scale features are), p. 1 (ABSTRACT) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track ... | p. 1 (ABSTRACT), p. 1 (ABSTRACT) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We propose to split tracking and mapping into two separate tasks, processed in parallel threads on a dual-core computer: one thread deals ... | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** The pose update is computed iteratively by minimising a robust objective function of the reprojection error: µ′ = argmin µ X j∈S Obj „/ej/ σj ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** This is a challenging problem, and to simplify the task somewhat we have imposed some constraints on the scene to be tracked: it should be ...
- **p. 4 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** (9) Obj(·, σT ) is the Tukey biweight objective function [13] and σT a robust (median-based) estimate of the distribution's standard deviation derived from all ...
- **p. 5 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** However there is an important difference in the selection of parameters which are optimised, and the selection of measurements used for constraints.
- **p. 5 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** Writing the current state of the map as {EK1W, ...EKN W} and {p1, ...pM}, each image measurement also has an associated reprojection error eji calculated ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Section 5 will describe how this map is tracked, and Section 6 will describe how the map is built and updated.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), p. 1 (1 INTRODUCTION), p. 4 (3. A small number (50) of the coarsest-scale features are), p. 2 (1 INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | reason, tracking, system, estimates, quality, every, frame, fraction, feature, observations, have, been, successful, Writing | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | reason, tracking, system, estimates, quality, every, frame, fraction, feature, observations | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | While, previously, been, attempted, adapting, SLAM, algorithms, developed, robotic, exploration | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | pose, update, computed, iteratively, minimising, robust, objective, function, reprojection, error | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** For this reason, the tracking system estimates the quality of tracking at every frame, using the fraction of feature observations which have been successful.
- **p. 5 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** Writing the current state of the map as {EK1W, ...EKN W} and {p1, ...pM}, each image measurement also has an associated reprojection error eji calculated ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** The tracking system receives images from the hand-held video camera and maintains a real-time estimate of the camera pose relative to the built map.
- **p. 4 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** 5.4 Pose update Given a set S of successful patch observations, a camera pose update can be computed.
- **p. 5 / 3. A small number (50) of the coarsest-scale features are - extractive PDF cue:** Including user interaction, map initialisation takes around three seconds.
- **p. 1 / ABSTRACT - extractive PDF cue:** We propose to split tracking and mapping into two separate tasks, processed in parallel threads on a dual-core computer: one thread deals with the task ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Map points are projected into the image according to the frame's prior pose estimate.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | This allows the use of computationally expensive batch optimisation techniques not usually associated with real-time operation: The result is a system that ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | These new keyframes then need not be processed within strict real-time limits (although processing should be finished by the time the next ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | At the end of the sequence the map consists of 57 keyframes and 4997 point features: from finest level to coarsest level, ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** fraction, falls, below, even, lower, threshold, more, frames, during, motion, model, might, successfully, bridge, untrackable, then, tracking, considered, lost, recovery.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | This system requires fairly powerful computing hardware and this has so far limited live experiments to a single office; we expect that ... | p. 8 (7 RESULTS), p. 8 (7 RESULTS) |
| Global / local decision | Compared with bundle adjustment, the processing time required for epipolar search and occasional data association refinement is small. | p. 6 (7 RESULTS), p. 8 (7 RESULTS) |
| Motion execution / recovery | At the same time, the use of a larger number of features reduces visible tracking jitter and improves performance when some features ... | p. 8 (7 RESULTS), p. 8 (7 RESULTS) |

## Failure and Ablation Link

- **p. 6 / 7 RESULTS - extractive PDF cue:** This video represents the size of a typical working volume which the system can handle without great difficulty.
- **p. 8 / 7 RESULTS - extractive PDF cue:** 8 LIMITATIONS AND FUTURE WORK This section describes some of the known issues with the system presented.
- **p. 8 / 7 RESULTS - extractive PDF cue:** AR applications are usable as soon as the map has been initialised from stereo; mapping proceeds in the background in a manner transparent to the ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 6: The system can easily track across multiple scales. Here, the map is initialised at the top-right scale; the user moves closer in and ...
- **p. 6 / 7 RESULTS - extractive PDF cue:** As the map grows beyond 100 keyframes, global bundle adjustment cannot keep up with exploration and is almost always aborted, converging only when the camera ...
- **p. 6 / 7 RESULTS - extractive PDF cue:** Timings of individual mapping steps are difficult to obtain, they vary wildly not only with map size but also scene structure (both global and local); ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3. A small number (50) of the coarsest-scale features are), p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 3 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), objective p. 4 (3. A small number (50) of the coarsest-scale features are), p. 1 (1 INTRODUCTION), p. 4 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), p. 2 (1 INTRODUCTION), temporal p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 3 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), p. 6 (7 RESULTS), p. 6 (7 RESULTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
