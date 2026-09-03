# PTAM: Parallel Tracking and Mapping for Small AR Workspaces

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=0.833); canonical paper source: https://www.robots.ox.ac.uk/~gk/PTAM/.
> PDF retrieval source: https://www.robots.ox.ac.uk/~gk/publications/KleinMurray2007ISMAR.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2007 / ISMAR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, SLAM, geometry, camera pose
- Official paper: https://www.robots.ox.ac.uk/~gk/PTAM/
- Full-text retrieval: https://www.robots.ox.ac.uk/~gk/publications/KleinMurray2007ISMAR.pdf
- Code/Project: https://www.robots.ox.ac.uk/~gk/PTAM/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=0.833)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Finally, in our hand-held camera scenario, we cannot rely on long 2D feature tracks being available to initialise features and we replace this with an epipolar feature search.를 문제로 두고, While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track a hand-held camera in a small AR workspace.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** This paper presents a method of estimating camera pose in an unknown scene.
- **p. 1 / ABSTRACT - extractive body cue:** While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track a hand-held camera ...
- **p. 1 / ABSTRACT - extractive body cue:** We propose to split tracking and mapping into two separate tasks, processed in parallel threads on a dual-core computer: one thread deals with the task ...
- **p. 1 / ABSTRACT - extractive body cue:** This allows the use of computationally expensive batch optimisation techniques not usually associated with real-time operation: The result is a system that produces detailed maps ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The majority of Augmented Reality (AR) systems operate with prior knowledge of the user's environment - i.e, some form of map.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Finally, in our hand-held camera scenario, we cannot rely on long 2D feature tracks being available to initialise features and we replace this with an ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Here, we argue that tracking a hand-held camera is more difficult than tracking a moving robot: firstly, a robot usually receives some form of odometry; ...

## Core Idea

- **p. 1 / ABSTRACT - extractive body cue:** While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track a hand-held camera ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The map consists of a collection of M point features located in a world coordinate frame W.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** While we adopt the stereo initialisation, and occasionally make use of local bundle updates, our method is different in that we attempt to build a ...
- **p. 1 / ABSTRACT - extractive body cue:** We propose to split tracking and mapping into two separate tasks, processed in parallel threads on a dual-core computer: one thread deals with the task ...
- **p. 4 / 3. A small number (50) of the coarsest-scale features are - extractive body cue:** If the fraction falls below an even lower threshold for more than a few frames (during which the motion model might successfully bridge untrackable frames) ...
- **p. 3 / 3. A small number (50) of the coarsest-scale features are - extractive body cue:** We use a decaying velocity model; this is similar to a simple alpha-beta constant velocity model, but lacking any new measurements, the estimated camera slows ...
- **p. 5 / 3. A small number (50) of the coarsest-scale features are - extractive body cue:** Bundle adjustment iteratively adjusts the map so as to minimise the robust objective function: ˘ {µ2..µN}, {p′ 1..p′ M} ¯ = argmin {{µ},{p}} N X ...
- **p. 4 / 3. A small number (50) of the coarsest-scale features are - extractive body cue:** For this reason, the tracking system estimates the quality of tracking at every frame, using the fraction of feature observations which have been successful.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For this reason, the tracking system estimates the quality of tracking at every frame, using the fraction of feature observations which have been successful. | camera/depth stream, pose, map와 language goal | p. 4 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are) |
| State/latent | reason, tracking, system, estimates, quality, every, frame, fraction, feature, observations, have, been | robot pose, free-space/semantic map와 local goal | p. 4 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), p. 3 (1 INTRODUCTION) |
| Output/action | Writing the current state of the map as {EK1W, ...EKN W} and {p1, ...pM}, each image measurement also has an associated reprojection error eji calculated as for equation (9). | collision-free trajectory 또는 velocity command | p. 5 (3. A small number (50) of the coarsest-scale features are), p. 3 (1 INTRODUCTION), p. 4 (3. A small number (50) of the coarsest-scale features are) |
| Objective/outcome | The pose update is computed iteratively by minimising a robust objective function of the reprojection error: µ′ = argmin µ X j∈S Obj „/ej/ σj , σT « (8) where ej is ... | goal reach, safety, localization error와 replanning latency | p. 4 (3. A small number (50) of the coarsest-scale features are), p. 1 (1 INTRODUCTION), p. 4 (3. A small number (50) of the coarsest-scale features are) |

## Main Claims and Actual Contribution

- **p. 1 / ABSTRACT - extractive body cue:** While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track a hand-held camera ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The map consists of a collection of M point features located in a world coordinate frame W.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** While we adopt the stereo initialisation, and occasionally make use of local bundle updates, our method is different in that we attempt to build a ...
- **p. 1 / ABSTRACT - extractive body cue:** We propose to split tracking and mapping into two separate tasks, processed in parallel threads on a dual-core computer: one thread deals with the task ...
- **p. 8 / 7 RESULTS - extractive body cue:** At the same time, the use of a larger number of features reduces visible tracking jitter and improves performance when some features are occluded or ...
- **p. 8 / 7 RESULTS - extractive body cue:** Frames are tracked in a relatively constant 20ms by our system, whereas EKF-SLAM scales quadratically from 3ms when the map is empty to 40ms at ...
- **p. 6 / 7 RESULTS - extractive body cue:** All results were obtained with identical tunable parameters.
- **p. 6 / 7 RESULTS - extractive body cue:** 7.1 Tracking performance on live video An example of the system's operation is provided in the accompanying video file1.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (7 RESULTS), p. 8 (7 RESULTS) |
| Embodiment/environment | This system requires fairly powerful computing hardware and this has so far limited live experiments to a single office; we expect that with some optimisations we will be able to run at ... | hardware/simulator version and reset protocol | p. 8 (7 RESULTS), p. 8 (7 RESULTS) |
| Dataset/benchmark | The camera then moves rapidly around the mapped scene. | role, split, size and leakage | p. 8 (7 RESULTS), p. 8 (7 RESULTS), p. 6 (7 RESULTS), p. 6 (7 RESULTS) |
| Metric | This game demonstrates tracking accuracy. | definition, denominator, direction and uncertainty | p. 8 (7 RESULTS), p. 8 (7 RESULTS), p. 6 (7 RESULTS) |
| Baseline/ablation | Compared with bundle adjustment, the processing time required for epipolar search and occasional data association refinement is small. | fair input/data/compute/action matching | p. 6 (7 RESULTS), p. 8 (7 RESULTS), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 7 RESULTS - extractive body cue:** 8 LIMITATIONS AND FUTURE WORK This section describes some of the known issues with the system presented.
- **p. 8 / 7 RESULTS - extractive body cue:** AR applications are usable as soon as the map has been initialised from stereo; mapping proceeds in the background in a manner transparent to the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: The system can easily track across multiple scales. Here, the map is initialised at the top-right scale; the user moves closer in and ...
- **p. 6 / 7 RESULTS - extractive body cue:** As the map grows beyond 100 keyframes, global bundle adjustment cannot keep up with exploration and is almost always aborted, converging only when the camera ...
- **p. 6 / 7 RESULTS - extractive body cue:** Timings of individual mapping steps are difficult to obtain, they vary wildly not only with map size but also scene structure (both global and local); ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Finally, in our hand-held camera scenario, we cannot rely on long 2D feature tracks being available to initialise features and we replace this with an epipolar feature search.를 문제로 두고, While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track a hand-held camera in a small AR workspace.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3. A small number (50) of the coarsest-scale features are) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
