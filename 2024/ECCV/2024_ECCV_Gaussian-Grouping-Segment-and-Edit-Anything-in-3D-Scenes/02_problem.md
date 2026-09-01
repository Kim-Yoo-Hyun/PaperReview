# Problem - Gaussian Grouping: Segment and Edit Anything in 3D Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4195_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04195.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 4 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction)): Most of these methods cannot generalize to open-world scenarios.

## PDF Body Digest

- **p. 2 / 1 Introduction - extractive PDF cue:** Open-world 3D scene understanding is an essential challenge, with far-reaching implications for robotics, AR / VR, and autonomous driving.
- **p. 2 / 1 Introduction - extractive PDF cue:** Given a set of posed RGB images, our goal is to learn an effective 3D representation that jointly reconstructs and segments anything in the 3D ...
- **p. 2 / 1 Introduction - extractive PDF cue:** The representation should easily support a wide range of downstream scene editing applications.
- **p. 2 / 1 Introduction - extractive PDF cue:** For example, in Figure 1, the 3D object of the scene can be easily removed or inpainted, and the scene can be recomposed by exchanging ...
- **p. 2 / 1 Introduction - extractive PDF cue:** While there has been remarkable progress in 2D scene understanding brought by SAM and its variants [13,16,63], their extension to 3D has been constrained.
- **p. 4 / 1 Introduction - extractive PDF cue:** Most of these methods cannot generalize to open-world scenarios.
- **p. 2 / 1 Introduction - extractive PDF cue:** Further, it is hard to directly adjust NeRF-based approaches for the downstream local editing tasks [18], because the learned neural networks, such as MLPs, cannot ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Most of these methods cannot generalize to open-world scenarios. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | We then detail the input data pre-processing steps and further describe the proposed Gaussian Grouping in Section 3.2. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | then, detail, input, data, pre-processing, steps, further, describe, Gaussian, Grouping | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Existing, methods, rely, manually-labeled, datasets, costly, limited, scope | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: then, detail, input, data, pre-processing, steps, further, describe, Gaussian, Grouping | p. 5 (3 Method), p. 5 (3 Method), p. 2 (1 Introduction) |
| Decision / output variable | geometry/map/query r; body terms: knowledge, first, Gaussian-based, tackle, open-world, scene, understanding, where | p. 4 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Projection, Camera, View, Gradient, Regularization, Loss, Multi-view, Captures | p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** Open-world 3D scene understanding is an essential challenge, with far-reaching implications for robotics, AR / VR, and autonomous driving.
- **p. 2 / 1 Introduction - extractive PDF cue:** Further, it is hard to directly adjust NeRF-based approaches for the downstream local editing tasks [18], because the learned neural networks, such as MLPs, cannot ...
- **p. 4 / 1 Introduction - extractive PDF cue:** However, none of the existing Gaussian Splatting works enables object / stufflevel or semantic understanding of the 3D scene.

## What the Paper Changes

PDF contribution framing (p. 4 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Method)): To our knowledge, we propose the first Gaussian-based method to tackle open-world 3D scene understanding, where we show the advantages compared to existing NeRF-based approaches [15,18,43] in segmentation quality, efficiency ...

- **p. 2 / 1 Introduction - extractive PDF cue:** We propose Gaussian Grouping, which represents the whole 3D scene with a set of grouped 3D Gaussians.
- **p. 2 / 1 Introduction - extractive PDF cue:** By inputting multi-view captures and the corresponding automatically generated masks by SAM, our method learns a discrete and grouped 3D representation for reconstructing and segmenting ...
- **p. 3 / 1 Introduction - extractive PDF cue:** We introduce Gaussian Grouping, the first 3D Gaussian Splatting-based segmentation framework that lifts knowledge of SAM to 3D scene anything zero-shot segmentation without the need ...
- **p. 5 / 3 Method - extractive PDF cue:** We design our method based on the recent 3D Gaussian Splatting [14], and extend it from pure 3D reconstruction to fine-grained scene understanding.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | Fig. 5: Robustness to input masks errors on Mip-NeRF 360 [1]. In the 2nd and 3rd columns (middle ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Model Gaussian Splatting Gaussian Grouping K=0 K=1 k=2 K=5 K=10 PSNR 30.32 30.51 30.62 30.61 30.72 30.62 RAcc ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | This is due to Gaussians inside the bear being occluded during training and cannot be supervised sufficiently. | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Limitation Due to the lack of dynamic modeling and time-dependent updating, Gaussian Grouping is currently limited to the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (3 Method), p. 5 (3 Method), p. 2 (1 Introduction), p. 6 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 4 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), interface p. 5 (3 Method), p. 5 (3 Method), p. 2 (1 Introduction), p. 6 (3 Method), objective p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
