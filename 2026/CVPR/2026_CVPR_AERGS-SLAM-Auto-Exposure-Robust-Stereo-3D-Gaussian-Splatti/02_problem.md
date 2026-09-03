# Problem - AERGS-SLAM: Auto-Exposure-Robust Stereo 3D Gaussian Splatting SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): However, such methods suffer from a key limitation: This CVPR paper is the Open Access version, provided by the Computer Vision Foundation.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian splatting (3DGS) has emerged as a revolutionary scene representation in simultaneous localization and mapping (SLAM) research.
- **p. 1 / Abstract - extractive body cue:** However, existing research on 3DGS-based SLAM fails to accurately address the appearance variations induced by camera auto-exposure in prevalent real-world scenarios, resulting in reduced localization ...
- **p. 1 / Abstract - extractive body cue:** To address this issue, we propose a stereo auto-exposure-robust Gaussian splatting SLAM (AERGS-SLAM), a framework robust to such variations and enables both reliable localization and ...
- **p. 1 / Abstract - extractive body cue:** Our key contributions are two fold.
- **p. 1 / Abstract - extractive body cue:** Firstly, we propose a camera exposure network to model the camera exposure process, which we integrate with Gaussian splatting to achieve exposure-controlled novel view synthesis.
- **p. 1 / 1. Introduction - extractive body cue:** However, such methods suffer from a key limitation: This CVPR paper is the Open Access version, provided by the Computer Vision Foundation.
- **p. 2 / 1. Introduction - extractive body cue:** However, such coupled methods suffer from key limitations in localization robustness and real-time performance.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, such methods suffer from a key limitation: This CVPR paper is the Open Access version, provided by the Computer Vision Foundation. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Brightness adjustment is modeled as Vout = AVint, where Vint and Vout are the input and output brightness of a pixel, respectively, ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | Brightness, adjustment, modeled, Vout, AVint, where, Vint, input, output, pixel | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | However, capture, high-quality, images, cameras, automatically, regulate, light | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Brightness, adjustment, modeled, Vout, AVint, where, Vint, input, output, pixel | p. 6 (Method), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Decision / output variable | path/waypoint/velocity; body terms: summarize, main, contributions, follows, camera, exposure, network, recovers | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (Method) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Coarse-to-fine, optimization, strategy, effective, many, SLAM, methods, However | p. 5 (3.3.2. Coarse-To-Fine Optimization) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.3.2. Coarse-To-Fine Optimization), p. 5 (3.3.2. Coarse-To-Fine Optimization) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation), p. 8 (4.4. Ablation Studies) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** However, such coupled methods suffer from key limitations in localization robustness and real-time performance.
- **p. 2 / 1. Introduction - extractive body cue:** However, traditional handcrafted feature-based SLAM system lacks robustness to AE-induced illumination variations, leading to reduced localization accuracy and degraded appearance reconstruction quality in exposure-varying scenarios.
- **p. 1 / 1. Introduction - extractive body cue:** For instance, MonoGS [26] adjusts image brightness via two exposure parameters, yet it fails to model complex AE mechanisms.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (Method), p. 6 (Method), p. 5 (3.3.2. Coarse-To-Fine Optimization)): To summarize, the main contributions of this work are as follows: • We propose a camera exposure network that recovers the camera's CRF to map per-image radiance maps to RGB ...

- **p. 2 / 1. Introduction - extractive body cue:** To address these problems, we propose a stereo decoupled auto-exposure-robust Gaussian splatting SLAM (AERGS-SLAM).
- **p. 6 / Method - extractive body cue:** Then, we evaluate on our self-collected dataset, which consists of six sequences captured using a ZED 2i stereo camera.
- **p. 6 / Method - extractive body cue:** Given its demonstrated superior performance in handling complex real-world scenarios and stereo setups in recent literature [14, 37], DROID-SLAM provides a reliable benchmark for assessing ...
- **p. 5 / 3.3.2. Coarse-To-Fine Optimization - extractive body cue:** To mitigate this limitation, we propose a time-aware sliding window coarse-to-fine strategy.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Table 1. Quantitative results of localization (RMSE ↓). We color code eac column as best and second best. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Extensive experiments show the IRL module significantly improves localization accuracy and robustness. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | It adopts a decoupled pipeline enabling illumination-robust localization and auto-exposurerobust photorealistic mapping. | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Figure 2. Overview of the proposed AERGS-SLAM. Firstly, the localization thread performs illumination-robust localization using stereo images, generating ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (Method), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 6 (Method), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), objective p. 5 (3.3.2. Coarse-To-Fine Optimization).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
