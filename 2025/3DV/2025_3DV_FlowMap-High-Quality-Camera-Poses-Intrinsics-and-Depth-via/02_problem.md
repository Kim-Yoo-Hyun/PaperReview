# Problem - FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=QI6HrBseVF&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): However, conventional SfM has a major limitation: it is not differentiable with respect to its free variables (camera poses, camera intrinsics, and perpixel depths).

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** Reconstructing a 3D scene from video is one of the most fundamental problems in vision and has been studied for over five decades.
- **p. 1 / 1 Introduction - extractive body cue:** Today, essentially all state-ofthe-art approaches are built on top of Structure-from-Motion (SfM) methods like COLMAP [58].
- **p. 1 / 1 Introduction - extractive body cue:** These approaches extract sparse correspondences across frames, match them, discard outliers, and then optimize the correspondences' 3D positions alongside the camera parameters by minimizing reprojection ...
- **p. 1 / 1 Introduction - extractive body cue:** This framework has delivered excellent results which underlie many presentday vision applications, and so it is unsurprising that SfM systems have remained largely unchanged in ...
- **p. 1 / 1 Introduction - extractive body cue:** However, conventional SfM has a major limitation: it is not differentiable with respect to its free variables (camera poses, camera intrinsics, and perpixel depths).
- **p. 1 / 1 Introduction - extractive body cue:** This means that SfM acts as an isolated pre-processing step that cannot be embedded into end-to-end deep learning pipelines.
- **p. 2 / 1 Introduction - extractive body cue:** Unlike prior attempts at gradient-based optimization of cameras and 3D geometry [2, 35, 73], we do not treat depth, intrinsics, and camera poses as free ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, conventional SfM has a major limitation: it is not differentiable with respect to its free variables (camera poses, camera intrinsics, and ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 1: We present FlowMap, an end-to-end differentiable method that recovers poses, intrinsics, and depth maps of an input video. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | present, FlowMap, end-to-end, differentiable, recovers, poses, intrinsics, depth, maps, input | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | introduces, FlowMap, end-to-end, differentiable, solves, precise, camera, poses | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: present, FlowMap, end-to-end, differentiable, recovers, poses, intrinsics, depth, maps, input | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)) |
| Decision / output variable | geometry/map/query r; body terms: present, FlowMap, differentiable, surprisingly, simple, camera, geometry, estimation | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: performs, per-video, gradient-descent, minimization, simple, least-squares, objective, compares | p. 1 (Body text (section not recovered)), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 14 (Figure/Table caption), p. 12 (6 Results), p. 12 (6 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** This means that SfM acts as an isolated pre-processing step that cannot be embedded into end-to-end deep learning pipelines.
- **p. 2 / 1 Introduction - extractive body cue:** Unlike prior attempts at gradient-based optimization of cameras and 3D geometry [2, 35, 73], we do not treat depth, intrinsics, and camera poses as free ...
- **p. 2 / 1 Introduction - extractive body cue:** Rather, we introduce differentiable feed-forward estimates of each one: depth is parameterized via a neural network, pose is parameterized as the solution to a least-squares ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered))): In this paper, we present FlowMap, a differentiable and surprisingly simple camera and geometry estimation method whose outputs enable photorealistic novel view synthesis.

- **p. 2 / 1 Introduction - extractive body cue:** We show that this uniquely enables high-quality SfM via gradient descent while making FlowMap compatible with standard deep-learning pipelines.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We empirically show that camera parameters and dense depth recovered by our method enable photo-realistic novel view synthesis on 360◦trajectories using Gaussian Splatting.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Our method not only far outperforms prior gradient-descent based bundle adjustment methods, but surprisingly performs on par with COLMAP, the state-of-the-art SfM method, on the ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 14 | FlowMap has several limitations that suggest exciting directions for future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | However, on about 20 percent of scenes, this approach falls into a local minimum and reconstruction fails catastrophically. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | DROID-SLAM* COLMAP Ours ATE Failure Fig. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | We note that COLMAP failed to estimate poses for 36 scenes, possibly because we ran it at a ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)), objective p. 1 (Body text (section not recovered)), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
