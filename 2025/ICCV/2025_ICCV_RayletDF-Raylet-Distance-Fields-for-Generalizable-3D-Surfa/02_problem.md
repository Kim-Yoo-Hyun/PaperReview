# Problem - RayletDF: Raylet Distance Fields for Generalizable 3D Surface Reconstruction from Point Clouds or Gaussians

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wei_RayletDF_Raylet_Distance_Fields_for_Generalizable_3D_Surface_Reconstruction_from_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wei_RayletDF_Raylet_Distance_Fields_for_Generalizable_3D_Surface_Reconstruction_from_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): Nevertheless, due to the limitation of existing ray parametrizations such as Plucker and spherical coordinates, they are often limited to recovering object-level surfaces and require per-scene training, lacking the desired ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** In this paper, we present a generalizable method for 3D surface reconstruction from raw point clouds or pre-estimated 3D Gaussians by 3DGS from RGB images.
- **p. 1 / Abstract - extractive PDF cue:** Unlike existing coordinate-based methods which are often computationally intensive when rendering explicit surfaces, our proposed method, named RayletDF, introduces a new technique called raylet distance ...
- **p. 1 / Abstract - extractive PDF cue:** Our pipeline consists of three key modules: a raylet feature extractor, a raylet distance field predictor, and a multi-raylet blender.
- **p. 1 / Abstract - extractive PDF cue:** These components work together to extract fine-grained local geometric features, predict raylet distances, and aggregate multiple predictions to reconstruct precise surface points.
- **p. 1 / Abstract - extractive PDF cue:** We extensively evaluate our method on multiple public real-world datasets, demonstrating superior performance in surface reconstruction from point clouds or 3D Gaussians.
- **p. 1 / 1. Introduction - extractive PDF cue:** Nevertheless, due to the limitation of existing ray parametrizations such as Plucker and spherical coordinates, they are often limited to recovering object-level surfaces and require ...
- **p. 1 / 1. Introduction - extractive PDF cue:** However, it still falls short in rendering high-quality depth views, due to its failure in capturing fine-grained surface geometry, though various constraints such as depth ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Nevertheless, due to the limitation of existing ray parametrizations such as Plucker and spherical coordinates, they are often limited to recovering object-level ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Given a specific 3D scene P as input, if it is a raw point cloud, for a specific query ray r, we ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Given, specific, scene, input, point, cloud, query, sample, multiple, raylets | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | particular, pipeline, comprises, three, modules, raylet, feature, extractor | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Given, specific, scene, input, point, cloud, query, sample, multiple, raylets | p. 4 (3.5. Sampling Raylets for Training and Test), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: contributions, generic, pipeline, explicit, surface, reconstruction, either, point | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4.1. Evaluation on 3D Gaussians) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** However, it still falls short in rendering high-quality depth views, due to its failure in capturing fine-grained surface geometry, though various constraints such as depth ...
- **p. 2 / 1. Introduction - extractive PDF cue:** With this merit of raylets, we simply formulate the problem of generalizable 3D surface reconstruction into learning raylet distance fields from visual observations.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.5. Sampling Raylets for Training and Test)): Our contributions are: • We propose a generic pipeline for explicit 3D surface reconstruction from either point clouds or 3D Gaussians. • We introduce a new raylet distance field followed ...

- **p. 1 / 1. Introduction - extractive PDF cue:** Given RGB/D images and/or point clouds, a series of 3D representations has † Equal contribution * Corresponding author been developed to recover 3D geometry, including ...
- **p. 1 / 1. Introduction - extractive PDF cue:** In this paper, we present a generalizable 3D surface representation pipeline to accurately recover 3D geometry.
- **p. 4 / 3.5. Sampling Raylets for Training and Test - extractive PDF cue:** If the input 3D scene P is a set of 3D Gaussians recovered by 3DGS [30] from RGBs, we follow the technique [31, 74] to ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Figure 3. Overview of our proposed pipeline. The leftmost block shows the raylet feature extractor module, the middle ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Remarkably, thanks to the learned local raylet features, it exhibits excellent generalizability to new and unseen scenes in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | This validates the generalizability and robustness of our simple design. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.5. Sampling Raylets for Training and Test), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.5. Sampling Raylets for Training and Test), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
