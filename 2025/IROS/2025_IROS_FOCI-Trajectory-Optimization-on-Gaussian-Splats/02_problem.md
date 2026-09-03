# Problem - FOCI: Trajectory Optimization on Gaussian Splats

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2505.08510; PDF retrieval source: https://arxiv.org/pdf/2505.08510. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): To overcome these challenges, we propose FOCI, a trajectory optimization algorithm that leverages the overlap integral - the spatial integral over the multiplication of two functions - as a proxy ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian Splatting (3DGS) has recently gained popularity as a faster alternative to Neural Radiance Fields (NeRFs) in 3D reconstruction and view synthesis methods.
- **p. 1 / Abstract - extractive body cue:** Leveraging the spatial information encoded in 3DGS, this work proposes FOCI (Field Overlap Collision Integral), an algorithm that is able to optimize trajectories directly on ...
- **p. 1 / Abstract - extractive body cue:** FOCI leverages a novel and interpretable collision formulation for 3DGS using the notion of the overlap integral between Gaussians.
- **p. 1 / Abstract - extractive body cue:** Contrary to other approaches, which represent the robot with conservative bounding boxes that underestimate the traversability of the environment, we propose to represent the environment ...
- **p. 1 / Abstract - extractive body cue:** This not only has desirable computational properties, but also allows for orientation-aware planning, allowing the robot to pass through very tight and narrow spaces.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To overcome these challenges, we propose FOCI, a trajectory optimization algorithm that leverages the overlap integral - the spatial integral over the multiplication of two ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Although some steps have been taken in this direction [3], [4], [5], the huge number of Gaussians a scene can have, together with the specific ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To overcome these challenges, we propose FOCI, a trajectory optimization algorithm that leverages the overlap integral - the spatial integral over the ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Since each spline segment lies within the convex hull of its control points, it is enough to constrain the norm of the ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Since, spline, segment, lies, within, convex, hull, control, points, enough | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Instead, full, pose, only, position, angle, optimized, Spline | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Since, spline, segment, lies, within, convex, hull, control, points, enough | p. 4 (III. METHOD), p. 6 (Method), p. 3 (III. METHOD) |
| Decision / output variable | geometry/map/query r; body terms: algorithm, enables, robot, perform, trajectory, optimization, directly, Gaussians | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: minimize, weighted, obstacle, cost, jerk, along, trajectory, distance | p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. METHOD), p. 6 (Method), p. 6 (Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (A. Trajectory Evaluation), p. 5 (A. Trajectory Evaluation), p. 6 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Although some steps have been taken in this direction [3], [4], [5], the huge number of Gaussians a scene can have, together with the specific ...

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 6 (Method)): In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians.

- **p. 2 / I. INTRODUCTION - extractive body cue:** The contributions of this work are therefore summarized as follows: • A novel collision measure between Gaussian Splats based on the overlap integral between Gaussians. ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To overcome these challenges, we propose FOCI, a trajectory optimization algorithm that leverages the overlap integral - the spatial integral over the multiplication of two ...
- **p. 3 / III. METHOD - extractive body cue:** Our methodology can be split into three parts: 1) trajectory representation to create an initial spline, 2) collision measure and 3) optimization loop.
- **p. 6 / Method - extractive body cue:** Runtime We evaluate the performance of our method by comparing the runtimes of the Casadi optimization on a single CPU core, multiple CPU cores, and ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | This means that when computing the overlap integral over the environment, flat regions with text or patterns have ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | As Figure 2b shows, the planning algorithm effectively leverages the asymmetry of ANYmal to pass through the narrow ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | 2) General Trajectory Planning Through 3DGS: Figure 3 shows that we can plan collision-free trajectories through splats that ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (III. METHOD), p. 6 (Method), p. 3 (III. METHOD), p. 3 (III. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 4 (III. METHOD), p. 6 (Method), p. 3 (III. METHOD), p. 3 (III. METHOD), objective p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Although some steps have been taken in this direction [3], [4], [5], the huge number of Gaussians a scene can have, together with the specific formulation of an explicit collision ... (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians. (p. 1, I. INTRODUCTION).
- **Assumption/failure evidence:** 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points. (p. 7, V. LIMITATIONS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
