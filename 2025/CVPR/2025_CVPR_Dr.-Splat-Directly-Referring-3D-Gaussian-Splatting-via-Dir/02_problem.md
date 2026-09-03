# Problem - Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): Despite its promise, such rendering-based distillation methods [30, 34] share two limitations.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Splat, a novel approach for openvocabulary 3D scene understanding leveraging 3D Gaussian Splatting.
- **p. 1 / Abstract - extractive body cue:** Unlike existing language-embedded 3DGS methods, which rely on a rendering process, our method directly associates language-aligned CLIP embeddings with 3D Gaussians for holistic 3D scene ...
- **p. 1 / Abstract - extractive body cue:** The key of our method is a language feature registration technique where CLIP embeddings are assigned to the dominant Gaussians intersected by each pixel-ray.
- **p. 1 / Abstract - extractive body cue:** Moreover, we integrate Product Quantization (PQ) trained on general large-scale image data to compactly represent embeddings without per-scene optimization.
- **p. 1 / Abstract - extractive body cue:** Experiments demonstrate that our approach significantly outperforms existing approaches in 3D perception benchmarks, such as openvocabulary 3D semantic segmentation, 3D object localization, and 3D object ...
- **p. 1 / 1. Introduction - extractive body cue:** Despite its promise, such rendering-based distillation methods [30, 34] share two limitations.
- **p. 1 / 1. Introduction - extractive body cue:** This gap This CVPR paper is the Open Access version, provided by the Computer Vision Foundation.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Despite its promise, such rendering-based distillation methods [30, 34] share two limitations. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | After training 3D Gaussians Φours with our feature registration process and PQ, we describe the details of an inference mode that facilitates ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | After, training, Gaussians, ours, feature, registration, process, describe, details, inference | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | athbf, thbf, T_i, mathbf, cdot, tilde, alpha, label | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: After, training, Gaussians, ours, feature, registration, process, describe, details, inference | p. 6 (3.3. Text-query based 3D localization), p. 2 (1. Introduction), p. 4 (3.1. Feature registration process) |
| Decision / output variable | geometry/map/query r; body terms: Splat, direct, registration, referencing, language-aligned, features, Gaussians, bypassing | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Dr. Splat) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: centroid, indices, jiL, optimized, minimizing, mink, quantize, given | p. 4 (3.1. Feature registration process), p. 4 (3.1. Feature registration process), p. 6 (3.2. Product-Quantized CLIP embeddings) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.1. Feature registration process), p. 5 (3.2. Product-Quantized CLIP embeddings), p. 1 (1. Introduction) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (Figure/Table caption), p. 7 (4.2. 3D object localization), p. 7 (4.2. 3D object localization) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** This gap This CVPR paper is the Open Access version, provided by the Computer Vision Foundation.
- **p. 2 / 1. Introduction - extractive body cue:** By preserving the richness of embeddings while reducing memory usage, PQ is integral to our framework's high scalability and its ability to perform 3D perception ...
- **p. 2 / 1. Introduction - extractive body cue:** Splat clearly distinguishable from prior works, facilitating a seamless integration of representative embeddings from 2D vision language models into the 3D spatial structure without compromising ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Dr. Splat), p. 4 (3.1. Feature registration process), p. 1 (1. Introduction)): Splat, direct registration and referencing of language-aligned features in 3D Gaussians, bypassing intermediate rendering and preserving feature accuracy. • We introduce the PQ encoding method for compact feature representation, reducin ...

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We propose Dr.
- **p. 3 / 3. Dr. Splat - extractive body cue:** Then, we introduce Product Quantization (PQ) into our framework to efficiently store Gaussian-registered language embeddings, Sec.
- **p. 4 / 3.1. Feature registration process - extractive body cue:** The proposed process can be interpreted as an inverse volume rendering without gradient-based optimization, which enables our method to be faster than the prior methods ...
- **p. 1 / 1. Introduction - extractive body cue:** Our method directly links language features to 3D Gaussians, enabling efficient and complete spatial coverage.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | For LangSplat-m, the activations often shows random 3D Gaussians or fail to localize entirely (e.g., see "coffee mug"), ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 6. Limitations of point-based IoU measurement. This figure shows the effect of removing the top and bottom ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Table 1. 3D object selection results on the LeRF-OVS dataset [17]. To measure 3D object selection performance, we ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Figure 7. Qualitative results of 3D object localization. We visualize 3D localization activations (yellow) for "chair" and "desk" ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (3.3. Text-query based 3D localization), p. 2 (1. Introduction), p. 4 (3.1. Feature registration process), p. 4 (3.1. Feature registration process). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 6 (3.3. Text-query based 3D localization), p. 2 (1. Introduction), p. 4 (3.1. Feature registration process), p. 4 (3.1. Feature registration process), objective p. 4 (3.1. Feature registration process), p. 4 (3.1. Feature registration process), p. 6 (3.2. Product-Quantized CLIP embeddings).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
