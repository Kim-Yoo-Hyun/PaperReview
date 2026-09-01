# Problem - DroneSplat: 3D Gaussian Splatting for Robust 3D Reconstruction from In-the-Wild Drone Imagery

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Tang_DroneSplat_3D_Gaussian_Splatting_for_Robust_3D_Reconstruction_from_In-the-Wild_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_DroneSplat_3D_Gaussian_Splatting_for_Robust_3D_Reconstruction_from_In-the-Wild_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): However, despite incorporating geometric priors, InstantSplat lacks corresponding optimization in 3DGS, undermining the abundant priors.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Drones have become essential tools for reconstructing wild scenes due to their outstanding maneuverability.
- **p. 1 / Abstract - extractive PDF cue:** Recent advances in radiance field methods have achieved remarkable rendering quality, providing a new avenue for 3D reconstruction from drone imagery.
- **p. 1 / Abstract - extractive PDF cue:** However, dynamic distractors in wild environments challenge the static scene assumption in radiance fields, while limited view constraints hinder the accurate capture of underlying scene ...
- **p. 1 / Abstract - extractive PDF cue:** To address these challenges, we introduce DroneSplat, a novel framework designed for robust 3D reconstruction from in-the-wild drone imagery.
- **p. 1 / Abstract - extractive PDF cue:** Our method adaptively adjusts masking thresholds by integrating local-global segmentation heuristics with statistical approaches, enabling precise identification and elimination of dynamic distractors in static scenes.
- **p. 2 / 1. Introduction - extractive PDF cue:** However, despite incorporating geometric priors, InstantSplat lacks corresponding optimization in 3DGS, undermining the abundant priors.
- **p. 2 / 1. Introduction - extractive PDF cue:** However, applying NeRF or 3DGS to in-the-wild drone imagery presents several challenges for high-quality 3D reconstruction (Figure 2).

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, despite incorporating geometric priors, InstantSplat lacks corresponding optimization in 3DGS, undermining the abundant priors. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Given a few posed drone imagery of a wild scene, our goal is to identify and eliminate dynamic distractors. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Given, posed, drone, imagery, wild, scene, goal, identify, eliminate, dynamic | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | However, when, novel, view, significantly, differs, input, views | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Given, posed, drone, imagery, wild, scene, goal, identify, eliminate, dynamic | p. 4 (3.2. Adaptive Local-Global Masking), p. 5 (3.2. Adaptive Local-Global Masking), p. 7 (Method) |
| Decision / output variable | geometry/map/query r; body terms: address, challenges, introduce, DroneSplat, robust, gaussian, splatting, framework | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Adaptive Local-Global Masking) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: DGS, optimized, combination, D-SSIM, loss, computed, rendered, color | p. 3 (3.2. Adaptive Local-Global Masking), p. 3 (3.2. Adaptive Local-Global Masking), p. 5 (3.3. Voxel-guided Gaussian Splatting), p. 6 (3.3. Voxel-guided Gaussian Splatting), p. 6 (3.3. Voxel-guided Gaussian Splatting), p. 8 (Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.3. Voxel-guided Gaussian Splatting), p. 6 (3.3. Voxel-guided Gaussian Splatting), p. 8 (Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 1 (Figure/Table caption), p. 6 (4.2. Comparison), p. 6 (4.2. Comparison) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** However, applying NeRF or 3DGS to in-the-wild drone imagery presents several challenges for high-quality 3D reconstruction (Figure 2).
- **p. 1 / 1. Introduction - extractive PDF cue:** Capable of traversing obstacles like water and difficult terrain, drones enable extensive data acquisition from varied altitudes and angles.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Adaptive Local-Global Masking), p. 7 (Method), p. 1 (1. Introduction)): To address these challenges, we introduce DroneSplat, a robust 3D gaussian splatting framework tailored for inthe-wild drone imagery.

- **p. 2 / 1. Introduction - extractive PDF cue:** For the issue of viewpoint sparsity, our framework employs a multi-view stereo model to provide rich geometric priors by predicting dense 3D points.
- **p. 4 / 3.2. Adaptive Local-Global Masking - extractive PDF cue:** To establish an accurate and appropriate threshold across different scenarios and training stages, we propose an adaptive method to adjust threshold based on real-time residuals ...
- **p. 7 / Method - extractive PDF cue:** Our method outperforms baseline methods on scenes with various numbers of dynamic distractors, while Ours(COLMAP) leading the rest.
- **p. 1 / 1. Introduction - extractive PDF cue:** Recently, radiance field methods, such as NeRF [23] and 3D Gaussian Splatting (3DGS) [11], have shown remarkable potential in 3D representation and novel view synthesis.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | We present DroneSplat, a novel framework for robust 3D reconstruction from in-the-wild drone imagery. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Experimental evaluations across diverse datasets demonstrate the superiority and robustness of our approach over previous methods. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | While RobustNeRF and NeRF On-the-go successfully remove distractors, they fail to retain fine details. | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1. Given a set of drone imagery, our method effectively eliminates the impact of dynamic distractors on ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.2. Adaptive Local-Global Masking), p. 5 (3.2. Adaptive Local-Global Masking), p. 7 (Method), p. 8 (Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 4 (3.2. Adaptive Local-Global Masking), p. 5 (3.2. Adaptive Local-Global Masking), p. 7 (Method), p. 8 (Method), objective p. 3 (3.2. Adaptive Local-Global Masking), p. 3 (3.2. Adaptive Local-Global Masking), p. 5 (3.3. Voxel-guided Gaussian Splatting), p. 6 (3.3. Voxel-guided Gaussian Splatting), p. 6 (3.3. Voxel-guided Gaussian Splatting), p. 8 (Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
