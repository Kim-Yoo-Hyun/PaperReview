# Problem - VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vkmi3jZtYG; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/168040. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): This obstacle makes 3DGS still hard to scale up to extremely large scenes in SLAM, remaining the challenge of improving the rendering quality, tracking accuracy, and scalability of 3DGS in ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Jointly estimating camera poses and mapping scenes from RGBD images is a fundamental task in simultaneous localization and mapping (SLAM).
- **p. 1 / Abstract - extractive body cue:** State-of-the-art methods employ 3D Gaussians to represent a scene, and render these Gaussians through splatting for higher efficiency and better rendering.
- **p. 1 / Abstract - extractive body cue:** However, these methods cannot scale up to extremely large scenes, due to the inefficient tracking and mapping strategies that need to optimize all 3D Gaussians ...
- **p. 1 / Abstract - extractive body cue:** To resolve this issue, we propose novel tracking and mapping strategies to work with a novel 3D representation, dubbed view-tied 3D Gaussians, for RGBD SLAM ...
- **p. 1 / Abstract - extractive body cue:** View-tied 3D Gaussians is a kind of simplified Gaussians, which is tied to depth pixels, without needing to learn locations, rotations, and multi-dimensional variances.
- **p. 1 / 1. Introduction - extractive body cue:** This obstacle makes 3DGS still hard to scale up to extremely large scenes in SLAM, remaining the challenge of improving the rendering quality, tracking accuracy, ...
- **p. 1 / 1. Introduction - extractive body cue:** To overcome this challenge, we propose an RGBD SLAM system with splatting view-tied 3D Gaussians.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This obstacle makes 3DGS still hard to scale up to extremely large scenes in SLAM, remaining the challenge of improving the rendering ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | We minimize the rendering errors with respect to observations, min {g}k ρ//Vi-V ′ i //1+τLS(Vi, V ′ i )+σUi//Di-D′ i//1, (2) where ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | minimize, rendering, errors, respect, observations, Vi-V, Ui//Di-D, i//1, where, SSIM | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | i-th, frame, RGB, depth, will, initialize, Gaussians, remove | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: minimize, rendering, errors, respect, observations, Vi-V, Ui//Di-D, i//1, where, SSIM | p. 5 (3.4. Mapping Scenes), p. 4 (3.3. Tracking Cameras), p. 3 (3.2. View-tied Gaussians) |
| Decision / output variable | path/waypoint/velocity; body terms: main, contributions, listed, below, view-tied, Gaussian, splatting, significantly | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: minimize, rendering, errors, respect, observations, Vi-V, Ui//Di-D, i//1 | p. 5 (3.5. Bundle Adjustment), p. 5 (3.4. Mapping Scenes), p. 4 (3.3. Tracking Cameras), p. 4 (3.3. Tracking Cameras) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Overview), p. 4 (3.3. Tracking Cameras), p. 4 (3.3. Tracking Cameras) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (4. Experiments and Analysis), p. 5 (4. Experiments and Analysis), p. 6 (4. Experiments and Analysis) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** To overcome this challenge, we propose an RGBD SLAM system with splatting view-tied 3D Gaussians.
- **p. 2 / 1. Introduction - extractive body cue:** Our tracking and mapping strategies remove the need of holding and optimizing all Gaussians in memory throughout the training, which improves the scalability of 3DGS ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.2. View-tied Gaussians), p. 3 (3.2. View-tied Gaussians)): Our main contributions are listed below. • We propose view-tied Gaussian splatting that significantly reduces storage but improves rendering quality with 3DGS in SLAM. • We introduce a novel RGBD ...

- **p. 1 / 1. Introduction - extractive body cue:** Our method introduces a novel point-based volume representation, dubbed view-tied 3D Gaussians, to represent the color and 1
- **p. 1 / 1. Introduction - extractive body cue:** To overcome this challenge, we propose an RGBD SLAM system with splatting view-tied 3D Gaussians.
- **p. 3 / 3.2. View-tied Gaussians - extractive body cue:** Our view-tied Gaussians aim to achieve memory efficiency in SLAM, which enables us to improve the rendering quality by using many more Gaussians to represent ...
- **p. 3 / 3.2. View-tied Gaussians - extractive body cue:** This not only enables us to use more Gaussians to represent local details, but also removes the need to maintain the appearance and geometry consistency ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | We cannot use a large number of Gaussians 8 | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | However, relying on data-driven priors, LoopSplat (Zhu et al., 2024) reported more accurate camera tracking in terms of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 23 | Table 22. Impact of depth noise and movability of Gaussians on the rendering performance in PSNR ↑, SSIM ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (3.4. Mapping Scenes), p. 4 (3.3. Tracking Cameras), p. 3 (3.2. View-tied Gaussians), p. 3 (3.2. View-tied Gaussians). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 5 (3.4. Mapping Scenes), p. 4 (3.3. Tracking Cameras), p. 3 (3.2. View-tied Gaussians), p. 3 (3.2. View-tied Gaussians), objective p. 5 (3.5. Bundle Adjustment), p. 5 (3.4. Mapping Scenes), p. 4 (3.3. Tracking Cameras), p. 4 (3.3. Tracking Cameras).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
