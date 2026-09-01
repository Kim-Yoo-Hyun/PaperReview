# Problem - GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Yan_GS-SLAM_Dense_Visual_SLAM_with_3D_Gaussian_Splatting_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Yan_GS-SLAM_Dense_Visual_SLAM_with_3D_Gaussian_Splatting_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction)): In practical mapping and tracking steps, these methods only render a small set of pixels to reduce optimization time, which leads to the reconstructed dense maps lacking This CVPR paper ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** In this paper, we introduce GS-SLAM that first utilizes 3D Gaussian representation in the Simultaneous Localization and Mapping (SLAM) system.
- **p. 1 / Abstract - extractive PDF cue:** It facilitates a better balance between efficiency and accuracy.
- **p. 1 / Abstract - extractive PDF cue:** Compared to recent SLAM methods employing neural implicit representations, our method utilizes a real-time differentiable splatting rendering pipeline that offers significant speedup to map optimization ...
- **p. 1 / Abstract - extractive PDF cue:** Specifically, we propose an adaptive expansion strategy that adds new or deletes noisy 3D Gaussians in order to efficiently reconstruct new observed scene geometry and ...
- **p. 1 / Abstract - extractive PDF cue:** This strategy is essential to extend 3D Gaussian representation to reconstruct the whole scene rather than synthesize a static object in existing methods.
- **p. 1 / 1. Introduction - extractive PDF cue:** In practical mapping and tracking steps, these methods only render a small set of pixels to reduce optimization time, which leads to the reconstructed dense ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We enhance scene reconstruction by introducing an adaptive strategy for managing 3D Gaussian elements, which optimizes mapping by focusing on current observations and minimizes errors ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In practical mapping and tracking steps, these methods only render a small set of pixels to reduce optimization time, which leads to ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | apply the proposed adaptive expansion strategy to add new or delete noisy 3D Gaussians from the whole scene representations to render RGB-D ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | apply, adaptive, expansion, strategy, delete, noisy, Gaussians, whole, scene, representations | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Then, find, pixel, coordinate, where, intersects, image, plane | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: apply, adaptive, expansion, strategy, delete, noisy, Gaussians, whole, scene, representations | p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 3 (3. Methodology), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping) |
| Decision / output variable | path/waypoint/velocity; body terms: Overall, contributions, include, GS-SLAM, first, Gaussian, Splatting, DGS | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. 3D Gaussian Scene Representation) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: apply, adaptive, expansion, strategy, delete, noisy, Gaussians, whole | p. 4 (3.3. Tracking and Bundle Adjustment), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 3 (3. Methodology), p. 3 (3. Methodology), p. 5 (3.3. Tracking and Bundle Adjustment), p. 5 (3.3. Tracking and Bundle Adjustment) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.3. Tracking and Bundle Adjustment), p. 3 (3. Methodology), p. 5 (3.3. Tracking and Bundle Adjustment) |
| Success / guarantee | goal reach with collision-free execution | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Evaluation of Localization and Mapping) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** We enhance scene reconstruction by introducing an adaptive strategy for managing 3D Gaussian elements, which optimizes mapping by focusing on current observations and minimizes errors ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. 3D Gaussian Scene Representation)): Overall, our contributions include: • We propose GS-SLAM, the first 3D Gaussian Splatting(3DGS)-based dense RGB-D SLAM approach, which takes advantage of the fast splatting rendering technique to boost the mapping ...

- **p. 2 / 1. Introduction - extractive PDF cue:** To this end, we propose GS-SLAM, the first RGB-D dense SLAM system that first utilizes 3D Gaussian scene representation coupled with the splatting rendering technique ...
- **p. 3 / 3.1. 3D Gaussian Scene Representation - extractive PDF cue:** Our goal is to optimize a scene representation that captures the geometry and appearance of the scene, resulting in a detailed dense map and high-quality ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | We believe GS-SLAM has the potential to extend to larger scale with some improvements and will explore this ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Figure 2. Overview of the proposed method. We aim to use 3D Gaussians to represent the scene and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | We further evaluate the rendering performance using the peak signal-to-noise ratio (PSNR), SSIM [43], and LPIPS [52] by ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 3 (3. Methodology), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 5 (3.3. Tracking and Bundle Adjustment). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 3 (3. Methodology), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 5 (3.3. Tracking and Bundle Adjustment), objective p. 4 (3.3. Tracking and Bundle Adjustment), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 3 (3. Methodology), p. 3 (3. Methodology), p. 5 (3.3. Tracking and Bundle Adjustment), p. 5 (3.3. Tracking and Bundle Adjustment).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
