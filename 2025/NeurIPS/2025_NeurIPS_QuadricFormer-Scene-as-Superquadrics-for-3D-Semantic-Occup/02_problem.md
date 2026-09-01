# Problem - QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=eZNdkwJYbN; PDF retrieval source: https://openreview.net/pdf/cc6e0a2d054469a238a6da05b30dce8f439f11f3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): Despite promising applications, 3D semantic occupancy prediction faces efficiency challenges due to its dense 3D predictions [4, 38].

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** 3D occupancy prediction is crucial for robust autonomous driving systems as it enables comprehensive perception of environmental structures and semantics.
- **p. 1 / Abstract - extractive PDF cue:** Most existing methods employ dense voxel-based scene representations, ignoring the sparsity of driving scenes and resulting in inefficiency.
- **p. 1 / Abstract - extractive PDF cue:** Recent works explore object-centric representations based on sparse Gaussians, but their ellipsoidal shape prior limits the modeling of diverse structures.
- **p. 1 / Abstract - extractive PDF cue:** In real-world driving scenes, objects exhibit rich geometries (e.g., cuboids, cylinders, and irregular shapes), necessitating excessive ellipsoidal Gaussians densely packed for accurate modeling, which leads ...
- **p. 1 / Abstract - extractive PDF cue:** To address this, we propose to use geometrically expressive superquadrics as scene primitives, enabling efficient representation of complex structures with fewer primitives through their inherent ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Despite promising applications, 3D semantic occupancy prediction faces efficiency challenges due to its dense 3D predictions [4, 38].
- **p. 2 / 1 Introduction - extractive PDF cue:** Real-world driving scenarios contain objects with rich structural variations, which cannot be accurately represented by a few ellipsoidal Gaussian.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Despite promising applications, 3D semantic occupancy prediction faces efficiency challenges due to its dense 3D predictions [4, 38]. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Extensive experiments on the nuScenes and KITTI-360 dataset demonstrate that our QuadricFormer achieves state-of-the-art performance with superior efficiency. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Extensive, experiments, nuScenes, KITTI-360, dataset, demonstrate, QuadricFormer, achieves, state-of-the-art, performance | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | efficient, expressive, object-centric, representation, superquadrics, scene, primitives, Building | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Extensive, experiments, nuScenes, KITTI-360, dataset, demonstrate, QuadricFormer, achieves, state-of-the-art, performance | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Decision / output variable | geometry/map/query r; body terms: efficient, expressive, object-centric, representation, superquadrics, scene, primitives, Building | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 16 (C Additional Implementation Details) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** Real-world driving scenarios contain objects with rich structural variations, which cannot be accurately represented by a few ellipsoidal Gaussian.

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 16 (C Additional Implementation Details)): In this paper, we propose an efficient and expressive object-centric 3D representation using superquadrics [1] as scene primitives.

- **p. 2 / 1 Introduction - extractive PDF cue:** Building on this representation, we introduce QuadricFormer, a superquadric-based framework for efficient 3D semantic occupancy prediction.
- **p. 16 / C Additional Implementation Details - extractive PDF cue:** To address this, we introduce the prunning-and-splitting module: · We divide all superquadrics in Q into two groups based on the product of their scales: ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | With random initialization, QuadricFormer cannot fully learn accurate superquadric positions, leaving some superquadrics in empty regions and reducing ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 Introduction), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 2 (1 Introduction), p. 2 (1 Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
