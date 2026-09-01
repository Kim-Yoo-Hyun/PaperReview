# Problem - Fully Convolutional Geometric Features

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content_ICCV_2019/html/Choy_Fully_Convolutional_Geometric_Features_ICCV_2019_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content_ICCV_2019/papers/Choy_Fully_Convolutional_Geometric_Features_ICCV_2019_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): Furthermore, current pipelines limit spatial context by focusing on patches with restricted spatial extent.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Extracting geometric features from 3D scans or point clouds is the first step in applications such as registration, reconstruction, and tracking.
- **p. 1 / Abstract - extractive PDF cue:** State-of-the-art methods require computing low-level features as input or extracting patch-based features with limited receptive field.
- **p. 1 / Abstract - extractive PDF cue:** In this work, we present fully-convolutional geometric features, computed in a single pass by a 3D fully-convolutional network.
- **p. 1 / Abstract - extractive PDF cue:** We also present new metric learning losses that dramatically improve performance.
- **p. 1 / Abstract - extractive PDF cue:** Fully-convolutional geometric features are compact, capture broad spatial context, and scale to large scenes.
- **p. 1 / 1. Introduction - extractive PDF cue:** Furthermore, current pipelines limit spatial context by focusing on patches with restricted spatial extent.
- **p. 1 / 1. Introduction - extractive PDF cue:** The gray region shows the Pareto frontier of the prior methods. patches for feature learning is akin to extracting small 2D patches around each pixel ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Furthermore, current pipelines limit spatial context by focusing on patches with restricted spatial extent. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Our approach does not require low-level preprocessing or 3D patches as input, and can rapidly generate high-resolution features with state-ofthe-art discriminative power. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | does, require, low-level, preprocessing, patches, input, rapidly, generate, high-resolution, features | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | reported, times, include, data, preprocessing, feature, extraction, standard | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: does, require, low-level, preprocessing, patches, input, rapidly, generate, high-resolution, features | p. 2 (1. Introduction), p. 4 (5. Implementation), p. 8 (6.7. Runtime) |
| Decision / output variable | geometry/map/query r; body terms: analogy, extracting, Equal, contribution, section, metric, learning, losses | p. 1 (1. Introduction), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 1 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: normalization, project, features, surface, hypersphere, pass, gradient, loss | p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), p. 4 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 4 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 4 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (Figure/Table caption), p. 4 (6. Experiments), p. 5 (6.2. Evaluation Metrics) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** The gray region shows the Pareto frontier of the prior methods. patches for feature learning is akin to extracting small 2D patches around each pixel ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Our approach achieves state-of-the-art performance on the 3DMatch benchmark [36], while being nine times faster than the fastest learning-based method and 290 times faster than ...

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): If we use a 2D analogy, extracting 3D ∗Equal contribution.

- **p. 3 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** In this section, we propose metric learning losses for fully-convolutional feature learning.
- **p. 1 / 1. Introduction - extractive PDF cue:** Our approach is the most accurate and the fastest.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our approach does not require low-level preprocessing or 3D patches as input, and can rapidly generate high-resolution features with state-ofthe-art discriminative power.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our approach achieves state-of-the-art performance on the 3DMatch benchmark [36], while being nine times faster than the fastest learning-based method and 290 times faster than ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | An interesting avenue for future work is to extend the FCGF methodology to end-to-end registration. | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Next, we find the hardest negatives for all positive pairs and filter out the hardest negatives that fall ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | First, we create a matrix P that contains the indices of positive pairs (i, j) as well as ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | If ICP fails or the number of overlapping voxels is less than 1k, we removed the pair from ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 4 (5. Implementation), p. 8 (6.7. Runtime), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 4 (5. Implementation), p. 8 (6.7. Runtime), p. 1 (1. Introduction), objective p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), p. 4 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 4 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
