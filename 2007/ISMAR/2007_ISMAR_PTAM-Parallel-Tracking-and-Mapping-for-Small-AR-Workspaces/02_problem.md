# Problem - PTAM: Parallel Tracking and Mapping for Small AR Workspaces

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.robots.ox.ac.uk/~gk/PTAM/; PDF retrieval source: https://www.robots.ox.ac.uk/~gk/publications/KleinMurray2007ISMAR.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): Finally, in our hand-held camera scenario, we cannot rely on long 2D feature tracks being available to initialise features and we replace this with an epipolar feature search.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** This paper presents a method of estimating camera pose in an unknown scene.
- **p. 1 / ABSTRACT - extractive body cue:** While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track a hand-held camera ...
- **p. 1 / ABSTRACT - extractive body cue:** We propose to split tracking and mapping into two separate tasks, processed in parallel threads on a dual-core computer: one thread deals with the task ...
- **p. 1 / ABSTRACT - extractive body cue:** This allows the use of computationally expensive batch optimisation techniques not usually associated with real-time operation: The result is a system that produces detailed maps ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The majority of Augmented Reality (AR) systems operate with prior knowledge of the user's environment - i.e, some form of map.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Finally, in our hand-held camera scenario, we cannot rely on long 2D feature tracks being available to initialise features and we replace this with an ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Here, we argue that tracking a hand-held camera is more difficult than tracking a moving robot: firstly, a robot usually receives some form of odometry; ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Finally, in our hand-held camera scenario, we cannot rely on long 2D feature tracks being available to initialise features and we replace ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | For this reason, the tracking system estimates the quality of tracking at every frame, using the fraction of feature observations which have ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | reason, tracking, system, estimates, quality, every, frame, fraction, feature, observations | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | tracking, system, receives, images, hand-held, video, camera, maintains | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: reason, tracking, system, estimates, quality, every, frame, fraction, feature, observations | p. 4 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), p. 3 (1 INTRODUCTION) |
| Decision / output variable | path/waypoint/velocity; body terms: While, previously, been, attempted, adapting, SLAM, algorithms, developed | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: pose, update, computed, iteratively, minimising, robust, objective, function | p. 4 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), p. 1 (1 INTRODUCTION), p. 4 (3. A small number (50) of the coarsest-scale features are), p. 2 (1 INTRODUCTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), p. 2 (1 INTRODUCTION) |
| Success / guarantee | goal reach with collision-free execution | p. 8 (7 RESULTS), p. 8 (7 RESULTS), p. 6 (7 RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Here, we argue that tracking a hand-held camera is more difficult than tracking a moving robot: firstly, a robot usually receives some form of odometry; ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The majority of Augmented Reality (AR) systems operate with prior knowledge of the user's environment - i.e, some form of map.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The logical extension of extensible tracking is to track in scenes without any prior map, and this is the focus of this paper.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Map points are projected into the image according to the frame's prior pose estimate.

## What the Paper Changes

PDF body contribution framing (p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT)): While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track a hand-held camera in a small AR workspace.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The map consists of a collection of M point features located in a world coordinate frame W.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** While we adopt the stereo initialisation, and occasionally make use of local bundle updates, our method is different in that we attempt to build a ...
- **p. 1 / ABSTRACT - extractive body cue:** We propose to split tracking and mapping into two separate tasks, processed in parallel threads on a dual-core computer: one thread deals with the task ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | 8 LIMITATIONS AND FUTURE WORK This section describes some of the known issues with the system presented. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | AR applications are usable as soon as the map has been initialised from stereo; mapping proceeds in the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Figure 6: The system can easily track across multiple scales. Here, the map is initialised at the top-right ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | As the map grows beyond 100 keyframes, global bundle adjustment cannot keep up with exploration and is almost ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), p. 3 (1 INTRODUCTION), p. 4 (3. A small number (50) of the coarsest-scale features are). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), interface p. 4 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), p. 3 (1 INTRODUCTION), p. 4 (3. A small number (50) of the coarsest-scale features are), objective p. 4 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are), p. 1 (1 INTRODUCTION), p. 4 (3. A small number (50) of the coarsest-scale features are), p. 2 (1 INTRODUCTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
