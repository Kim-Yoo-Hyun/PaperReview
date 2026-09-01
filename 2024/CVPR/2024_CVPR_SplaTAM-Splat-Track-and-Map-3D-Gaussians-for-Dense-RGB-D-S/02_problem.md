# Problem - SplaTAM: Splat Track & Map 3D Gaussians for Dense RGB-D SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Keetha_SplaTAM_Splat_Track__Map_3D_Gaussians_for_Dense_RGB-D_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Keetha_SplaTAM_Splat_Track__Map_3D_Gaussians_for_Dense_RGB-D_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): However, this is difficult for implicit map representations, as the network is subject to global changes during gradient-based optimization for the unmapped space. • Explicit map: We can arbitrarily increase ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Dense simultaneous localization and mapping (SLAM) is crucial for robotics and augmented reality applications.
- **p. 1 / Abstract - extractive PDF cue:** However, current methods are often hampered by the nonvolumetric or implicit way they represent a scene.
- **p. 1 / Abstract - extractive PDF cue:** This work introduces SplaTAM, an approach that, for the first time, leverages explicit volumetric representations, i.e., 3D Gaussians, to enable high-fidelity reconstruction from a single ...
- **p. 1 / Abstract - extractive PDF cue:** SplaTAM employs a simple online tracking and mapping system tailored to the underlying Gaussian representation.
- **p. 1 / Abstract - extractive PDF cue:** It utilizes a silhouette mask to elegantly capture the presence of scene density.
- **p. 2 / 1. Introduction - extractive PDF cue:** However, this is difficult for implicit map representations, as the network is subject to global changes during gradient-based optimization for the unmapped space. • Explicit ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, current methods use implicit neural representations to model the volumetric radiance fields, which causes a number of issues in the SLAM setting - they ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, this is difficult for implicit map representations, as the network is subject to global changes during gradient-based optimization for the unmapped ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | We propose to similarly differentiably render depth: D( \ m a thb f {p}) = \ s um _{i = 1}^{n} d_i ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | similarly, differentiably, render, depth, mathbf, prod, compared, against, input, return | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | modeling, world, collection, Gaussians, rendered, highfidelity, color, depth | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: similarly, differentiably, render, depth, mathbf, prod, compared, against, input, return | p. 4 (3. Method), p. 4 (3. Method), p. 3 (3. Method) |
| Decision / output variable | path/waypoint/velocity; body terms: across, experiments, simulated, real, data, SplaTAM, achieves, state-of-the-art | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Method) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: camera, parameters, initialized, following, E_t, text, pose, then | p. 4 (3. Method), p. 4 (3. Method), p. 5 (3. Method), p. 3 (3. Method), p. 3 (3. Method), p. 5 (3. Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3. Method), p. 5 (3. Method), p. 3 (3. Method) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (5. Results & Discussion), p. 8 (5. Results & Discussion), p. 6 (5. Results & Discussion) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** However, current methods use implicit neural representations to model the volumetric radiance fields, which causes a number of issues in the SLAM setting - they ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Method), p. 3 (3. Method), p. 4 (3. Method)): We show across all our experiments on simulated and real data that our approach, SplaTAM, achieves state-of-the-art results compared to all previous approaches for camera pose estimation, map estimation, and ...

- **p. 2 / 1. Introduction - extractive PDF cue:** We introduce several simple modifications that make splatting even faster for SLAM, including the removal of view-dependent appearance and the use of isotropic Gaussians.
- **p. 4 / 3. Method - extractive PDF cue:** We propose to similarly differentiably render depth: D( \ m a thb f {p}) = \ s um _{i = 1}^{n} d_i f_i(\mathbf {p}) \prod ...
- **p. 3 / 3. Method - extractive PDF cue:** The core of our approach is the ability to render high-fidelity color, depth, and silhouette images from our underlying Gaussian Map 21359
- **p. 4 / 3. Method - extractive PDF cue:** This differentiable rendering allows us to directly calculate the gradients in the underlying scene representation (Gaussians) and camera parameters with respect to the error between ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Figure 3. Renderings on ScanNet++ [49]. Our method, SplaTAM, renders color & depth for the novel & train ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1. SplaTAM enables precise camera tracking and high-fidelity reconstruction for dense simultaneous localization and mapping (SLAM) in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | However, all current SLAM benchmarks don't have a hold-out set of images separate from the camera trajectory that ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | In contrast, Point-SLAM [30] fails at camera-pose tracking and overfits to the training views, and isn't able to ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3. Method), p. 4 (3. Method), p. 3 (3. Method), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3. Method), p. 4 (3. Method), p. 3 (3. Method), p. 2 (1. Introduction), objective p. 4 (3. Method), p. 4 (3. Method), p. 5 (3. Method), p. 3 (3. Method), p. 3 (3. Method), p. 5 (3. Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
