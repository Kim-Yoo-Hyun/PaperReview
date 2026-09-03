# Problem - QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=eZNdkwJYbN; PDF retrieval source: https://arxiv.org/pdf/2506.10977. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): Despite promising applications, 3D semantic occupancy prediction faces efficiency challenges due to its dense 3D predictions [4, 31].

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** 3D occupancy prediction is crucial for robust autonomous driving systems as it enables comprehensive perception of environmental structures and semantics.
- **p. 1 / Abstract - extractive body cue:** Most existing methods employ dense voxel-based scene representations, ignoring the sparsity of driving scenes and resulting in inefficiency.
- **p. 1 / Abstract - extractive body cue:** Recent works explore object-centric representations based on sparse Gaussians, but their ellipsoidal shape prior limits the modeling of diverse structures.
- **p. 1 / Abstract - extractive body cue:** In real-world driving scenes, objects exhibit rich geometries (e.g., cuboids, cylinders, and irregular shapes), necessitating excessive ellipsoidal Gaussians densely packed for accurate modeling, which leads ...
- **p. 1 / Abstract - extractive body cue:** To address this, we propose to use geometrically expressive superquadrics as scene primitives, enabling efficient representation of complex structures with fewer primitives through their inherent ...
- **p. 2 / 1 Introduction - extractive body cue:** Despite promising applications, 3D semantic occupancy prediction faces efficiency challenges due to its dense 3D predictions [4, 31].
- **p. 2 / 1 Introduction - extractive body cue:** Real-world driving scenarios contain objects with rich structural variations, which cannot be accurately represented by a few ellipsoidal Gaussian.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Despite promising applications, 3D semantic occupancy prediction faces efficiency challenges due to its dense 3D predictions [4, 31]. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Furthermore, surface-based methods rely on the explicit structure from point cloud inputs, whereas visual inputs introduce structural uncertainty, making deterministic modeling unstable. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Furthermore, surface-based, methods, rely, explicit, structure, point, cloud, inputs, whereas | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Formally, given, input, images, views, model, aims, predict | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Furthermore, surface-based, methods, rely, explicit, structure, point, cloud, inputs, whereas | p. 5 (6 Superquadrics), p. 3 (6 Superquadrics), p. 4 (6 Superquadrics) |
| Decision / output variable | geometry/map/query r; body terms: section, present, superquadric, representation, efficient, semantic, occupancy, prediction | p. 3 (6 Superquadrics), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: optimization, adopt, cross, entropy, loss, lovaszsoftmax, training, While | p. 3 (6 Superquadrics), p. 5 (6 Superquadrics), p. 6 (6 Superquadrics), p. 5 (6 Superquadrics), p. 6 (6 Superquadrics) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 3 (6 Superquadrics), p. 1 (Abstract) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 9 (Figure/Table caption), p. 7 (4 Experiments), p. 8 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Real-world driving scenarios contain objects with rich structural variations, which cannot be accurately represented by a few ellipsoidal Gaussian.

## What the Paper Changes

PDF body contribution framing (p. 3 (6 Superquadrics), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (12800 Gaussians)): 3 Proposed Approach In this section, we present our method based on the superquadric representation for efficient 3D semantic occupancy prediction.

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose an efficient and expressive object-centric 3D representation using superquadrics [1] as scene primitives.
- **p. 2 / 1 Introduction - extractive body cue:** Building on this representation, we introduce QuadricFormer, a superquadric-based framework for efficient 3D semantic occupancy prediction.
- **p. 1 / Abstract - extractive body cue:** To address this, we propose to use geometrically expressive superquadrics as scene primitives, enabling efficient representation of complex structures with fewer primitives through their inherent ...
- **p. 1 / 12800 Gaussians - extractive body cue:** 20.02 mIoU 1600 Superquadrics 20.12 mIoU GaussianFormer QuadricFormer Figure 1: Considering the ellipsoidal shape prior of Gaussians, we propose leveraging expressive superquadrics to build an ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | With random initialization, QuadricFormer cannot fully learn accurate superquadric positions, leaving some superquadrics in empty regions and reducing ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (6 Superquadrics), p. 3 (6 Superquadrics), p. 4 (6 Superquadrics), p. 5 (6 Superquadrics). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 5 (6 Superquadrics), p. 3 (6 Superquadrics), p. 4 (6 Superquadrics), p. 5 (6 Superquadrics), objective p. 3 (6 Superquadrics), p. 5 (6 Superquadrics), p. 6 (6 Superquadrics), p. 5 (6 Superquadrics), p. 6 (6 Superquadrics).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
