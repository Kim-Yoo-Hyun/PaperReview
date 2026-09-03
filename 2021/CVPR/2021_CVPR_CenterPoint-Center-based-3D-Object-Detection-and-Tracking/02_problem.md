# Problem - CenterPoint: Center-based 3D Object Detection and Tracking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2006.11275; PDF retrieval source: https://arxiv.org/pdf/2006.11275. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 2 (1. Introduction)): However, during a safety-critical left turn (bottom), anchor-based methods have difficulty fitting axisaligned bounding boxes to rotated objects.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Three-dimensional objects are commonly represented as 3D boxes in a point-cloud.
- **p. 1 / Abstract - extractive body cue:** This representation mimics the well-studied image-based 2D bounding-box detection but comes with additional challenges.
- **p. 1 / Abstract - extractive body cue:** Objects in a 3D world do not follow any particular orientation, and box-based detectors have difficulties enumerating all orientations or fitting an axis-aligned bounding box ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we instead propose to represent, detect, and track 3D objects as points.
- **p. 1 / Abstract - extractive body cue:** Our framework, CenterPoint, first detects centers of objects using a keypoint detector and regresses to other attributes, including 3D size, 3D orientation, and velocity.
- **p. 1 / 1. Introduction - extractive body cue:** However, during a safety-critical left turn (bottom), anchor-based methods have difficulty fitting axisaligned bounding boxes to rotated objects.
- **p. 1 / 1. Introduction - extractive body cue:** Compared to the wellstudied 2D detection problem, 3D detection on point-clouds offers a series of interesting challenges: First, point-clouds are sparse, and most regions of ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, during a safety-critical left turn (bottom), anchor-based methods have difficulty fitting axisaligned bounding boxes to rotated objects. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | It takes an input image and predicts a w × h heatmap ˆY ∈[0, 1]w×h×K for each of K classes. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | takes, input, image, predicts, heatmap, classes, output, backbone, network, map-view | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | velocity, estimate, special, requires, input, map-views, current, previous | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: takes, input, image, predicts, heatmap, classes, output, backbone, network, map-view | p. 3 (3. Preliminaries), p. 3 (3. Preliminaries), p. 4 (4. CenterPoint) |
| Decision / output variable | geometry/map/query r; body terms: marked, differences, between, detection, made, transfer, ideas, Anchor-based | p. 1 (1. Introduction), p. 3 (3. Preliminaries), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: CenterPoint, combines, heatmap, regression, losses, common, objective, jointly | p. 4 (4. CenterPoint), p. 3 (3. Preliminaries), p. 4 (4. CenterPoint), p. 5 (4.1. Two-Stage CenterPoint), p. 3 (4. CenterPoint) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3. Preliminaries), p. 5 (4.1. Two-Stage CenterPoint), p. 2 (1. Introduction) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 4 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Compared to the wellstudied 2D detection problem, 3D detection on point-clouds offers a series of interesting challenges: First, point-clouds are sparse, and most regions of ...
- **p. 2 / 1. Introduction - extractive body cue:** Notably, in NeurIPS 2020 nuScenes 3D Detection challenge, CenterPoint is adopted in 3 of the top 4 winning entries.
- **p. 3 / 3. Preliminaries - extractive body cue:** As 3D bounding boxes come with various sizes and orientation, anchor-based 3D detectors have difficulty fitting an axis-aligned 2D box to a 3D object.
- **p. 2 / 1. Introduction - extractive body cue:** For 3D tracking, our model performs at 63.8 AMOTA outperforming the prior state-of-the-art by 8.8 AMOTA on nuScenes.

## What the Paper Changes

PDF body contribution framing (p. 1 (1. Introduction), p. 3 (3. Preliminaries), p. 2 (1. Introduction), p. 1 (Abstract), p. 3 (3. Preliminaries)): These marked differences between 2D and 3D detection made a transfer of ideas bea) Anchor-based t=1 c) Anchor-based t=2 b) Center-based t=1 d) Center-based t=2 Figure 1: We present a ...

- **p. 3 / 3. Preliminaries - extractive body cue:** We introduce a novel center-based detection head but rely on existing 3D backbones (VoxelNet or PointPillars).
- **p. 2 / 1. Introduction - extractive body cue:** Thirdly, point-based feature extraction enables us to design an effective two-stage refinement module that is much faster than previous approaches [44-46].
- **p. 1 / Abstract - extractive body cue:** Our framework, CenterPoint, first detects centers of objects using a keypoint detector and regresses to other attributes, including 3D size, 3D orientation, and velocity.
- **p. 3 / 3. Preliminaries - extractive body cue:** Each bounding box b = (u, v, d, w, l, h, α) consists of a center location (u, v, d), relative to the objects ground ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Notably, our tracking does not require a separate motion model and runs in a negligible time, 1ms on ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Two-stage refinement does not bring an improvement over the single-stage CenterPoint model on nuScenes in our experiments. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3. Preliminaries), p. 3 (3. Preliminaries), p. 4 (4. CenterPoint), p. 4 (4.1. Two-Stage CenterPoint). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 2 (1. Introduction), interface p. 3 (3. Preliminaries), p. 3 (3. Preliminaries), p. 4 (4. CenterPoint), p. 4 (4.1. Two-Stage CenterPoint), objective p. 4 (4. CenterPoint), p. 3 (3. Preliminaries), p. 4 (4. CenterPoint), p. 5 (4.1. Two-Stage CenterPoint), p. 3 (4. CenterPoint).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
