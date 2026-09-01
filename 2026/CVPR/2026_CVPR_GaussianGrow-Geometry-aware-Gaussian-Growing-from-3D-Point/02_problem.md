# Problem - GaussianGrow: Geometry-aware Gaussian Growing from 3D Point Clouds with Text Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_GaussianGrow_Geometry-aware_Gaussian_Growing_from_3D_Point_Clouds_with_Text_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_GaussianGrow_Geometry-aware_Gaussian_Growing_from_3D_Point_Clouds_with_Text_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): mains limited due to the lack of proper geometry priors.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** 3D Gaussian Splatting has demonstrated superior performance in rendering efficiency and quality, yet the generation of 3D Gaussians still remains a challenge without proper geometric ...
- **p. 1 / Abstract - extractive PDF cue:** Existing methods have explored predicting point maps as geometric references for inferring Gaussian primitives, while the unreliable estimated geometries may lead to poor generations.
- **p. 1 / Abstract - extractive PDF cue:** In this work, we introduce GaussianGrow, a novel approach that generates 3D Gaussians by learning to grow them from easily accessible 3D point clouds, naturally ...
- **p. 1 / Abstract - extractive PDF cue:** Specifically, we design a textguided Gaussian growing scheme that leverages a multiview diffusion model to synthesize consistent appearances from input point clouds for supervision.
- **p. 1 / Abstract - extractive PDF cue:** To mitigate artifacts caused by fusing neighboring views, we constrain novel views generated at non-preset camera poses identified in overlapping regions across different views.
- **p. 2 / 1. Introduction - extractive PDF cue:** mains limited due to the lack of proper geometry priors.
- **p. 2 / 1. Introduction - extractive PDF cue:** The overlapping regions across different generated views often cause artifacts due to challenges in fusing Gaussian primitives.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | mains limited due to the lack of proper geometry priors. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | UDF Field Multi-View Diffusion Stable Diffusion ControlNet "Black and Red Dragon" Depth Map Input Point Clouds Normal Maps Position Maps Primary View ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | UDF, Field, Multi-View, Diffusion, Stable, ControlNet, Black, Red, Dragon, Depth | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Visual, comparison, Objaverse, dataset, GaussianGrow, uses, point, clouds | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: UDF, Field, Multi-View, Diffusion, Stable, ControlNet, Black, Red, Dragon, Depth | p. 4 (3.2. Appearance Generation), p. 3 (3.1. Preliminary Preparation), p. 6 (3.3. Iterative Inpainting and Refinement) |
| Decision / output variable | geometry/map/query r; body terms: contributions, summarized, follows, GaussianGrow, novel, generates, Gaussians, learning | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: differentiable, formulation, enables, efficient, gradient, descent, optimization, learnable | p. 3 (3.1. Preliminary Preparation), p. 3 (3.1. Preliminary Preparation), p. 4 (3.2. Appearance Generation), p. 5 (3.3. Iterative Inpainting and Refinement), p. 5 (3.3. Iterative Inpainting and Refinement) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Preliminary Preparation), p. 4 (3.2. Appearance Generation), p. 4 (3.2. Appearance Generation) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.1. Text-Guided Visual Synthesis), p. 7 (4.2. Text-to-3D Generation), p. 7 (4.1. Text-Guided Visual Synthesis) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** The overlapping regions across different generated views often cause artifacts due to challenges in fusing Gaussian primitives.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 4 (3.2. Appearance Generation), p. 4 (3.2. Appearance Generation)): Our contributions can be summarized as follows: • We propose GaussianGrow, a novel approach that generates 3D Gaussians by learning to grow them from easily accessible 3D point clouds with ...

- **p. 2 / 1. Introduction - extractive PDF cue:** Bridging the gap between point cloud geometries and 3D Gaussian Splatting appearances, we introduce a novel perspective that rethinks Gaussian generation by growing 3D Gaussians ...
- **p. 3 / 3. Method - extractive PDF cue:** We present GaussianGrow, a novel generative model for 3D Gaussian Splatting by learning to grow 3D Gaussians from 3D point cloud geometries.
- **p. 4 / 3.2. Appearance Generation - extractive PDF cue:** Our method begins by identifying critical overlap regions where the inconsistencies are most pronounced.
- **p. 4 / 3.2. Appearance Generation - extractive PDF cue:** A spatial Gaussian inpainting strategy is also used to diffuse appearance from optimized Gaussians to the hard-to-observe ones. we propose a dense-view generation framework that ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Fig. 4. Spatial Inpainting. Due to noises and uneven density in the raw point cloud data, some points ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | To demonstrate robustness with real-world data, we also utilized the DeepFashion3D dataset 18974 | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | These scans present challenging characteristics including noise and varying point densities. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | 4, using only the six cardinal views leads to clear degradation across all metrics, while adding four views ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.2. Appearance Generation), p. 3 (3.1. Preliminary Preparation), p. 6 (3.3. Iterative Inpainting and Refinement), p. 3 (3. Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.2. Appearance Generation), p. 3 (3.1. Preliminary Preparation), p. 6 (3.3. Iterative Inpainting and Refinement), p. 3 (3. Method), objective p. 3 (3.1. Preliminary Preparation), p. 3 (3.1. Preliminary Preparation), p. 4 (3.2. Appearance Generation), p. 5 (3.3. Iterative Inpainting and Refinement), p. 5 (3.3. Iterative Inpainting and Refinement).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
