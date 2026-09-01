# Problem - FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=QI6HrBseVF&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): However, conventional SfM has a major limitation: it is not differentiable with respect to its free variables (camera poses, camera intrinsics, and perpixel depths).

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** Reconstructing a 3D scene from video is one of the most fundamental problems in vision and has been studied for over five decades.
- **p. 1 / 1 Introduction - extractive PDF cue:** Today, essentially all state-ofthe-art approaches are built on top of Structure-from-Motion (SfM) methods like COLMAP [58].
- **p. 1 / 1 Introduction - extractive PDF cue:** These approaches extract sparse correspondences across frames, match them, discard outliers, and then optimize the correspondences' 3D positions alongside the camera parameters by minimizing reprojection ...
- **p. 1 / 1 Introduction - extractive PDF cue:** This framework has delivered excellent results which underlie many presentday vision applications, and so it is unsurprising that SfM systems have remained largely unchanged in ...
- **p. 1 / 1 Introduction - extractive PDF cue:** However, conventional SfM has a major limitation: it is not differentiable with respect to its free variables (camera poses, camera intrinsics, and perpixel depths).
- **p. 1 / 1 Introduction - extractive PDF cue:** This means that SfM acts as an isolated pre-processing step that cannot be embedded into end-to-end deep learning pipelines.
- **p. 2 / 1 Introduction - extractive PDF cue:** Unlike prior attempts at gradient-based optimization of cameras and 3D geometry [2, 35, 73], we do not treat depth, intrinsics, and camera poses as free ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, conventional SfM has a major limitation: it is not differentiable with respect to its free variables (camera poses, camera intrinsics, and ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 1: We present FlowMap, an end-to-end differentiable method that recovers poses, intrinsics, and depth maps of an input video. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | present, FlowMap, end-to-end, differentiable, recovers, poses, intrinsics, depth, maps, input | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Today, essentially, state-ofthe-art, approaches, built, Structure-from-Motion, SfM, methods | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: present, FlowMap, end-to-end, differentiable, recovers, poses, intrinsics, depth, maps, input | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Decision / output variable | geometry/map/query r; body terms: present, FlowMap, differentiable, surprisingly, simple, camera, geometry, estimation | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: loss, minimized, only, gradient, descent, leading, high-quality, camera | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 14 (Figure/Table caption), p. 12 (6 Results), p. 12 (6 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive PDF cue:** This means that SfM acts as an isolated pre-processing step that cannot be embedded into end-to-end deep learning pipelines.
- **p. 2 / 1 Introduction - extractive PDF cue:** Unlike prior attempts at gradient-based optimization of cameras and 3D geometry [2, 35, 73], we do not treat depth, intrinsics, and camera poses as free ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Rather, we introduce differentiable feed-forward estimates of each one: depth is parameterized via a neural network, pose is parameterized as the solution to a least-squares ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): In this paper, we present FlowMap, a differentiable and surprisingly simple camera and geometry estimation method whose outputs enable photorealistic novel view synthesis.

- **p. 2 / 1 Introduction - extractive PDF cue:** We show that this uniquely enables high-quality SfM via gradient descent while making FlowMap compatible with standard deep-learning pipelines.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 14 | FlowMap has several limitations that suggest exciting directions for future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | However, on about 20 percent of scenes, this approach falls into a local minimum and reconstruction fails catastrophically. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | DROID-SLAM* COLMAP Ours ATE Failure Fig. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | We note that COLMAP failed to estimate poses for 36 scenes, possibly because we ran it at a ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), objective p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
