# Problem - VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): To address these challenges, we introduce VarSplat, an uncertainty-aware RGB-D SLAM system leveraging 3D Gaussian Splatting.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Simultaneous Localization and Mapping (SLAM) with 3D Gaussian Splatting (3DGS) enables fast, differentiable rendering and high-fidelity reconstruction across diverse realworld scenes.
- **p. 1 / Abstract - extractive PDF cue:** However, existing 3DGS-SLAM approaches handle measurement reliability implicitly, making pose estimation and global alignment susceptible to drift in lowtexture regions, transparent surfaces, or areas with ...
- **p. 1 / Abstract - extractive PDF cue:** To this end, we introduce VarSplat, an uncertainty-aware 3DGS-SLAM system that explicitly learns per-splat appearance variance.
- **p. 1 / Abstract - extractive PDF cue:** By using the law of total variance with alpha compositing, we then render differentiable per-pixel uncertainty map via efficient, singlepass rasterization.
- **p. 1 / Abstract - extractive PDF cue:** This map guides tracking, submap registration, and loop detection toward focusing on reliable regions and contributes to more stable optimization.
- **p. 2 / 1. Introduction - extractive PDF cue:** To address these challenges, we introduce VarSplat, an uncertainty-aware RGB-D SLAM system leveraging 3D Gaussian Splatting.
- **p. 2 / 1. Introduction - extractive PDF cue:** Despite these advances, a key limitation exists: measurement reliability is rarely modeled explicitly.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To address these challenges, we introduce VarSplat, an uncertainty-aware RGB-D SLAM system leveraging 3D Gaussian Splatting. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | VarSplat is an RGB-D SLAM approach that jointly estimates camera poses and incrementally updates 3D Gaussian Splatting (3DGS) map from input frames, ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | VarSplat, RGB-D, SLAM, jointly, estimates, camera, poses, incrementally, updates, Gaussian | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Given, current, estimate, keyframe, color, depth, images, differentiably | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: VarSplat, RGB-D, SLAM, jointly, estimates, camera, poses, incrementally, updates, Gaussian | p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.2. Mapping) |
| Decision / output variable | path/waypoint/velocity; body terms: summary, contributions, follows, introduce, VarSplat, RGB-D, DGS-SLAM, system | p. 2 (1. Introduction), p. 3 (3. Method), p. 2 (1. Introduction) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Therefore, optimizing, pure, photometric, loss, pose, refinement, lead | p. 5 (3.2. Mapping), p. 5 (3.3. Downstream Pose Estimation), p. 4 (3.2. Mapping), p. 4 (3.2. Mapping), p. 3 (3. Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Mapping), p. 3 (3.1. Per-pixel uncertainty rendering), p. 3 (3. Method) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (4.2. Quantitative Evaluation), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Quantitative Evaluation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** Despite these advances, a key limitation exists: measurement reliability is rarely modeled explicitly.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 3 (3. Method), p. 2 (1. Introduction), p. 4 (3.1. Per-pixel uncertainty rendering), p. 5 (3.3. Downstream Pose Estimation)): In summary, our contributions can be shown as follows: • We introduce VarSplat, an RGB-D 3DGS-SLAM system that learns per-splat appearance variance σ2 to render differentiable per-pixel uncertainty map V ...

- **p. 3 / 3. Method - extractive PDF cue:** To address these issues, we introduce a novel uncertainty quantification pipeline based on per-pixel uncertainty map rendering.
- **p. 2 / 1. Introduction - extractive PDF cue:** To address these challenges, we introduce VarSplat, an uncertainty-aware RGB-D SLAM system leveraging 3D Gaussian Splatting.
- **p. 4 / 3.1. Per-pixel uncertainty rendering - extractive PDF cue:** By sharing the same single-pass rasterization as color and depth, V enables efficient, online, in-the-loop reliability estimation.
- **p. 5 / 3.3. Downstream Pose Estimation - extractive PDF cue:** Ltrack = X λc  f wp⊙∥ˆI -I∥1  +(1-λc)∥ˆD-D∥1 (17) where 0 ≤λc ≤1 balances the contribution between photometric and geometric losses, and f ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Limitations and future works are provided in Supplementary Material. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | These results also show that using the per-pixel uncertainty map to regularize the photometric loss does not degrade ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Across four datasets, this integration achieves robust and competitive-to-superior performance. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | On ScanNet++, VarSplat improves ATE RMSE by about 18% over the second best method and ensures robustness in ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.2. Mapping), p. 4 (3.2. Mapping). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.2. Mapping), p. 4 (3.2. Mapping), objective p. 5 (3.2. Mapping), p. 5 (3.3. Downstream Pose Estimation), p. 4 (3.2. Mapping), p. 4 (3.2. Mapping), p. 3 (3. Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
