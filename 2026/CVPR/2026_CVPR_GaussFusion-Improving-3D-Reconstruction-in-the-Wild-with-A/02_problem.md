# Problem - GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_GaussFusion_Improving_3D_Reconstruction_in_the_Wild_with_A_Geometry-Informed_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_GaussFusion_Improving_3D_Reconstruction_in_the_Wild_with_A_Geometry-Informed_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): To address these limitations, several methods [3, 32, 34, 41, 46, 49, 56, 66, 70] have explored leveraging generative priors to enhance 3D reconstruction by generating dense novel-view images.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We present GaussFusion, a novel approach for improving 3D Gaussian splatting (3DGS) reconstructions in the wild through geometry-informed video generation.
- **p. 1 / Abstract - extractive PDF cue:** GaussFusion mitigates common 3DGS artifacts, including floaters, flickering, and blur caused by camera pose errors, incomplete coverage, and noisy geometry initialization.
- **p. 1 / Abstract - extractive PDF cue:** Unlike prior RGB-based approaches limited to a single reconstruction pipeline, our method introduces a geometryinformed video-to-video generator that refines 3DGS renderings across both optimization-based and ...
- **p. 1 / Abstract - extractive PDF cue:** Given an existing reconstruction, we render a Gaussian primitives video buffer encoding depth, normals, opacity, and covariance, which the generator refines to produce temporally coherent, ...
- **p. 1 / Abstract - extractive PDF cue:** We further introduce an artifact synthesis pipeline that simulates diverse degradation patterns, ensuring robustness and generalization.
- **p. 1 / 1. Introduction - extractive PDF cue:** To address these limitations, several methods [3, 32, 34, 41, 46, 49, 56, 66, 70] have explored leveraging generative priors to enhance 3D reconstruction by ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Similarly, MVSplat360 [7] refines feed-forward reconstructions but fails to generalize to optimization-based pipelines, as it is tightly coupled to a specific feed-forward model [6].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To address these limitations, several methods [3, 32, 34, 41, 46, 49, 56, 66, 70] have explored leveraging generative priors to enhance ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | (2) Feed-Forward 3DGS Reconstruction Models learn to directly predict a complete set of 3D Gaussian parameters from a small set of posed/unposed ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Feed-Forward, DGS, Reconstruction, Models, learn, directly, predict, complete, Gaussian, parameters | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Finally, merge, generated, novel, views, original, inputs, optimize | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Feed-Forward, DGS, Reconstruction, Models, learn, directly, predict, complete, Gaussian, parameters | p. 3 (3.1. Preliminaries), p. 3 (3.1. Preliminaries), p. 5 (3.4. 3D Reconstruction Updating) |
| Decision / output variable | geometry/map/query r; body terms: main, contributions, follows, geometry-informed, video-to-video, generation, model, GaussFusion | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminaries) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Finally, merge, generated, novel, views, original, inputs, optimize | p. 5 (3.4. 3D Reconstruction Updating) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.4. 3D Reconstruction Updating), p. 5 (3.4. 3D Reconstruction Updating) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (5.1. Results), p. 7 (5.1. Results), p. 8 (5.2. Ablation Studies) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** Similarly, MVSplat360 [7] refines feed-forward reconstructions but fails to generalize to optimization-based pipelines, as it is tightly coupled to a specific feed-forward model [6].
- **p. 1 / 1. Introduction - extractive PDF cue:** However, despite these advances, current methods still suffer from artifacts in sparseview and under-captured scenarios, and degrade significantly at novel views far from training views ...
- **p. 2 / 1. Introduction - extractive PDF cue:** This raises a key question: How can we train a single high-quality reconstruction refinement model that generalizes across different 3DGS paradigms?

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminaries), p. 1 (1. Introduction), p. 1 (1. Introduction)): Our main contributions are as follows: • A geometry-informed video-to-video generation model, GaussFusion, conditioned on 3DGS geometric renders, effective for artifact removal across diverse reconstruction pipelines. • A comprehensive ...

- **p. 2 / 1. Introduction - extractive PDF cue:** We present GaussFusion, a video-to-video generative model for robust 3D reconstruction that features as key component the GP-Buffer, a pixel-aligned video representation that encodes multi-modal ...
- **p. 3 / 3.1. Preliminaries - extractive PDF cue:** The contribution γi is the product of the learned opacity αi and the 2D Gaussian function evaluated at the pixel center u with projected mean ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Photorealistic 3D reconstruction and novel-view synthesis are fundamental problems in computer vision, with applications in virtual reality, autonomous driving, and robotics.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, despite these advances, current methods still suffer from artifacts in sparseview and under-captured scenarios, and degrade significantly at novel views far from training views ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | We discuss our limitations and future work in Supp. | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1. GaussFusion Overview. Given multi-view images as input, we first obtain an initial 3D Gaussian splatting (3DGS) ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 2. GaussFusion Video Generator Architecture. Our model refines video latents using geometry-aware conditioning derived from 3D Gaussian ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | 4), which combines optimization- and feed-forward degradations while injecting pose and coverage diversity. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3.1. Preliminaries), p. 3 (3.1. Preliminaries), p. 5 (3.4. 3D Reconstruction Updating), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3.1. Preliminaries), p. 3 (3.1. Preliminaries), p. 5 (3.4. 3D Reconstruction Updating), p. 2 (1. Introduction), objective p. 5 (3.4. 3D Reconstruction Updating).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
