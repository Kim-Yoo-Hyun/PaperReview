# Problem - SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): Nevertheless, 3DGS-based methods for the AD setting [7, 43, 51] inherit the limitation of only being able to render camera data, overlooking the lidar modality.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Ensuring the safety of autonomous robots, such as selfdriving vehicles, requires extensive testing across diverse driving scenarios.
- **p. 1 / Abstract - extractive body cue:** Simulation is a key ingredient for conducting such testing in a cost-effective and scalable way.
- **p. 1 / Abstract - extractive body cue:** Neural rendering methods have gained popularity, as they can build simulation environments from collected logs in a data-driven manner.
- **p. 1 / Abstract - extractive body cue:** However, existing neural radiance field (NeRF) methods for sensor-realistic rendering of camera and lidar data suffer from low rendering speeds, limiting their applicability for large-scale ...
- **p. 1 / Abstract - extractive body cue:** While 3D Gaussian Splatting (3DGS) enables real-time rendering, current methods are limited to camera data and are unable to render lidar data essential for autonomous ...
- **p. 1 / 1. Introduction - extractive body cue:** Nevertheless, 3DGS-based methods for the AD setting [7, 43, 51] inherit the limitation of only being able to render camera data, overlooking the lidar modality.
- **p. 2 / 1. Introduction - extractive body cue:** Applying 3DGS to lidar sensors presents unique challenges due to their distinct characteristics.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Nevertheless, 3DGS-based methods for the AD setting [7, 43, 51] inherit the limitation of only being able to render camera data, overlooking ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | To summarize, our contributions are as follows: • We propose the first method for efficient lidar rendering using 3D Gaussians, introducing custom ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | summarize, contributions, follows, first, efficient, lidar, rendering, Gaussians, introducing, custom | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Projecting, lidar, points, images, depth, supervision, previous, DGS | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: summarize, contributions, follows, first, efficient, lidar, rendering, Gaussians, introducing, custom | p. 2 (1. Introduction), p. 3 (3. Method), p. 6 (3.4. Optimization and implementation) |
| Decision / output variable | geometry/map/query r; body terms: summarize, contributions, follows, first, efficient, lidar, rendering, Gaussians | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: LBCE, binary, cross-entropy, loss, predicted, drop, probability, where | p. 5 (3.4. Optimization and implementation), p. 5 (3.4. Optimization and implementation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3. Method), p. 4 (3.3. Lidar rendering), p. 6 (3.4. Optimization and implementation) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4.2. Lidar rendering), p. 8 (4.2. Lidar rendering), p. 8 (4.3. Ablations) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Applying 3DGS to lidar sensors presents unique challenges due to their distinct characteristics.
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these challenges, we introduce SplatAD, a novel view synthesis method that unifies camera and lidar rendering and is designed for real-time rendering of ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3.2. Camera rendering), p. 5 (3.3. Lidar rendering)): To summarize, our contributions are as follows: • We propose the first method for efficient lidar rendering using 3D Gaussians, introducing custom CUDA-accelerated algorithms for rasterizing sparse point clouds in ...

- **p. 2 / 1. Introduction - extractive body cue:** To overcome these challenges, we introduce SplatAD, a novel view synthesis method that unifies camera and lidar rendering and is designed for real-time rendering of ...
- **p. 3 / 3. Method - extractive body cue:** Our method projects 3D Gaussians with associated feature vectors onto the corresponding sensor modalities (camera and lidar) and employs sensor-specific tiling to match their distinct ...
- **p. 3 / 3.2. Camera rendering - extractive body cue:** While we retain 3DGS's high-level steps-projection and view frustum culling, tile-assignment, depth sorting, and tilebased rasterization-we introduce key adaptations to better model the unique characteristics ...
- **p. 5 / 3.3. Lidar rendering - extractive body cue:** done in our method by modifying the projection accordingly.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Limitations and future work: SplatAD is currently limited to modeling all dynamic actors as rigid. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Drawing inspiration from recent advances in human reconstruction [18, 20, 26] can provide inspiration how to overcome this ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | However, we note that using Inception-v3 features instead does not change the model ranking or our conclusions. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | To validate the robustness of our method, we evaluate it across multiple popular AD datasets, using the same ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 3 (3. Method), p. 6 (3.4. Optimization and implementation), p. 4 (3.3. Lidar rendering). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 3 (3. Method), p. 6 (3.4. Optimization and implementation), p. 4 (3.3. Lidar rendering), objective p. 5 (3.4. Optimization and implementation), p. 5 (3.4. Optimization and implementation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
