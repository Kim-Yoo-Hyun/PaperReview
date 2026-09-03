# Problem - SC-OmniGS: Self-Calibrating Omnidirectional Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=7idCpuEAiR; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/113436. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): Given the lack of camera models accounting for the distortion of 360-degree images and the limitations of existing self-calibration approaches, there is an urgent need for a framework that calibrates ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** 360-degree cameras streamline data collection for radiance field 3D reconstruction by capturing comprehensive scene data.
- **p. 1 / ABSTRACT - extractive body cue:** However, traditional radiance field methods do not address the specific challenges inherent to 360-degree images.
- **p. 1 / ABSTRACT - extractive body cue:** We present SC-OmniGS, a novel self-calibrating omnidirectional Gaussian splatting system for fast and accurate omnidirectional radiance field reconstruction using 360-degree images.
- **p. 1 / ABSTRACT - extractive body cue:** Rather than converting 360-degree images to cube maps and performing perspective image calibration, we treat 360-degree images as a whole sphere and derive a mathematical ...
- **p. 1 / ABSTRACT - extractive body cue:** Furthermore, we introduce a differentiable omnidirectional camera model in order to rectify the distortion of real-world data for performance enhancement.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Given the lack of camera models accounting for the distortion of 360-degree images and the limitations of existing self-calibration approaches, there is an urgent need ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Existing methods for recovering 3D information from 360-degree images, including structure-from-motion (SfM) systems (Moulon et al., 2013; Huang & Yeung, 2022), rely on an idealized ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Given the lack of camera models accounting for the distortion of 360-degree images and the limitations of existing self-calibration approaches, there is ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | To rectify distortion patterns in the input image, we propose a differentiable omnidirectional camera model comprising a learnable 3D spherical grid to ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | rectify, distortion, patterns, input, image, differentiable, omnidirectional, camera, model, comprising | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | thus, obtain, undistorted, omnidirectional, images, re-sampling, input, learned | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: rectify, distortion, patterns, input, image, differentiable, omnidirectional, camera, model, comprising | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Decision / output variable | geometry/map/query r; body terms: summarize, main, contributions, include, first, system, self-calibrating, omnidirectional | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Overall, omnidirectional, camera, intrinsic, model, extrinsic, poses, Gaussians | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 10 (5 EXPERIMENTS), p. 16 (Figure/Table caption), p. 8 (5 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Existing methods for recovering 3D information from 360-degree images, including structure-from-motion (SfM) systems (Moulon et al., 2013; Huang & Yeung, 2022), rely on an idealized ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** It can achieve rapid radiance field reconstruction with no pose prior and render high-fidelity novel views. on SfM, some approaches (Lin et al., 2021; Jeong ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT)): To summarize, the main contributions of this work include: • We proposed the first system for self-calibrating omnidirectional radiance fields, which jointly optimizes 3D Gaussians, omnidirectional camera poses, and camera ...

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose SC-OmniGS, a novel system that self-calibrates the omnidirectional camera model and poses along with omnidirectional radiance field reconstruction.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** It can also facilitate other applications such as GS-based omnidirectional SLAM. • We introduced a novel differentiable omnidirectional camera model that effectively tackles the complex ...
- **p. 1 / ABSTRACT - extractive body cue:** We present SC-OmniGS, a novel self-calibrating omnidirectional Gaussian splatting system for fast and accurate omnidirectional radiance field reconstruction using 360-degree images.
- **p. 1 / ABSTRACT - extractive body cue:** Furthermore, we introduce a differentiable omnidirectional camera model in order to rectify the distortion of real-world data for performance enhancement.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | However, we cannot apply a similar modification to 3D-GS based methods. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | With the differentiable omnidirectional camera model and Gaussian splatting procedure, our approach jointly optimizes 3D Gaussians, omnidirectional camera ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Our camera calibration demonstrates greater robustness to translation errors with only minor degradation compared to rotation errors. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | OmniBlender dataset provides noise-free camera poses and depth maps. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), objective p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
