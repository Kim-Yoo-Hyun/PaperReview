# Problem - AGS-Mesh: Adaptive Gaussian Splatting and Meshing with Geometric Priors for Indoor Room Reconstruction Using Smartphones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=fTJrKaBKZk&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Gaussian Splatting), p. 1 (1. Introduction), p. 3 (3.1. Geometric Priors from Handheld Devices)): However, performance on room-scale reconstruction with data captured by a mobile device is still lacking.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Geometric priors are often used to enhance 3D reconstruction.
- **p. 1 / Abstract - extractive PDF cue:** With many smartphones featuring low-resolution depth sensors and the prevalence of off-the-shelf monocular geometry estimators, incorporating geometric priors as regularization signals has become common in ...
- **p. 1 / Abstract - extractive PDF cue:** However, the accuracy of depth estimates from mobile devices is typically poor for highly detailed geometry, and monocular estimators often suffer from poor multi-view consistency ...
- **p. 1 / Abstract - extractive PDF cue:** In this work, we propose an approach for joint surface depth and normal refinement of Gaussian Splatting methods for accurate 3D reconstruction of indoor scenes.
- **p. 1 / Abstract - extractive PDF cue:** We develop supervision strategies that adaptively filters low-quality depth and normal estimates by comparing the consistency of the priors during optimization.
- **p. 2 / 1. Introduction - extractive PDF cue:** However, performance on room-scale reconstruction with data captured by a mobile device is still lacking.
- **p. 2 / 1. Introduction - extractive PDF cue:** Low-texture surfaces and sparse, outward-facing captures, common in indoor room datasets [37, 55], pose challenges and ambiguities for purely photometric-based reconstruction.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, performance on room-scale reconstruction with data captured by a mobile device is still lacking. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | To achieve this, we employ a point cloud hint: we back-project our output depth maps from all training images into a point ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | achieve, employ, point, cloud, hint, back-project, output, depth, maps, training | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | first, predict, normal, estimates, pretrained, monocular, estimation, model | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: achieve, employ, point, cloud, hint, back-project, output, depth, maps, training | p. 6 (4.4. Mesh Extraction), p. 2 (1. Introduction), p. 4 (4. Method) |
| Decision / output variable | geometry/map/query r; body terms: summarize, contributions, following, statements, novel, regularization, strategy, indoor | p. 2 (1. Introduction), p. 4 (4. Method), p. 4 (4. Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: allow, gradients, normal, loss, during, optimization, directly, influence | p. 5 (4.2. Adaptive Normal Regularization), p. 5 (4.3. Optimization) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (4. Method), p. 6 (4.4. Mesh Extraction), p. 6 (4.4. Mesh Extraction) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (5. Experiments), p. 7 (Figure/Table caption), p. 7 (5.3. Ablation Studies) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** Low-texture surfaces and sparse, outward-facing captures, common in indoor room datasets [37, 55], pose challenges and ambiguities for purely photometric-based reconstruction.
- **p. 4 / 3.2. Gaussian Splatting - extractive PDF cue:** However, as noted in prior research [35], this is just an approximation for perpixel depth estimates.
- **p. 1 / 1. Introduction - extractive PDF cue:** Traditional approaches have addressed the problem by creating textured meshes that can be rendered using conventional graphics pipelines.
- **p. 3 / 3.1. Geometric Priors from Handheld Devices - extractive PDF cue:** Depth and Normal Priors from Monocular Networks.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 4 (4. Method), p. 4 (4. Method), p. 2 (1. Introduction), p. 5 (4.1. Regularization with Depth Normal Consistency)): We summarize our contributions with the following statements: • We propose a novel regularization strategy for indoor room reconstruction that adaptively filters geometric priors from mobile devices and off-the-shelf monocular ...

- **p. 4 / 4. Method - extractive PDF cue:** Our method consists of two adaptive supervision strategies for Gaussian Splatting-based methods that effectively combine supervision signals from geometric priors obtained from mobile devices and ...
- **p. 4 / 4. Method - extractive PDF cue:** Lastly, in Section 4.4, we propose a novel octree-based mesh extraction method that enhances surface quality and detail preservation compared to previous approaches.
- **p. 2 / 1. Introduction - extractive PDF cue:** Additionally, we propose an Adaptive Normal Regularization strategy (ANR) to refine normals by mitigating regularization in regions where monocular normal estimators struggle to provide accurate ...
- **p. 5 / 4.1. Regularization with Depth Normal Consistency - extractive PDF cue:** Furthermore, we propose an adaptive TSDF and octree-based Marching Cubes meshing strategy enabling the extraction of smoother and more geometrically detailed meshes.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Lastly, the DNC and ANR terms help preserve details for objects and reduce overall noise. | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | Figure 8. Qualitative visuals of our Depth Normal Consistency (DNR) and Adaptive Normal Regularization (ANR) terms. We visualize ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (4.4. Mesh Extraction), p. 2 (1. Introduction), p. 4 (4. Method), p. 4 (4. Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Gaussian Splatting), p. 1 (1. Introduction), p. 3 (3.1. Geometric Priors from Handheld Devices), interface p. 6 (4.4. Mesh Extraction), p. 2 (1. Introduction), p. 4 (4. Method), p. 4 (4. Method), objective p. 5 (4.2. Adaptive Normal Regularization), p. 5 (4.3. Optimization).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
