# Problem - CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Tian_CCL-LGS_Contrastive_Codebook_Learning_for_3D_Language_Gaussian_Splatting_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Tian_CCL-LGS_Contrastive_Codebook_Learning_for_3D_Language_Gaussian_Splatting_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): However, their reliance on exhaustive multi-scale rendering leads to inefficiency, and patch-based feature extraction often fails to capture precise object boundaries, resulting in scale misalignment and performance degradation.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Recent advances in 3D reconstruction techniques and vision-language models have fueled significant progress in 3D semantic understanding, a capability critical to robotics, autonomous driving, and ...
- **p. 1 / Abstract - extractive PDF cue:** However, methods that rely on 2D priors are prone to a critical challenge: cross-view semantic inconsistencies induced by occlusion, image blur, and view-dependent variations.
- **p. 1 / Abstract - extractive PDF cue:** These inconsistencies, when propagated via projection supervision, deteriorate the quality of 3D Gaussian semantic fields and introduce artifacts in the rendered outputs.
- **p. 1 / Abstract - extractive PDF cue:** To mitigate this limitation, we propose CCL-LGS, a novel framework that enforces view-consistent semantic supervision by integrating multi-view semantic cues.
- **p. 1 / Abstract - extractive PDF cue:** Specifically, our approach first employs a zero-shot tracker to
- **p. 2 / 1. Introduction - extractive PDF cue:** However, their reliance on exhaustive multi-scale rendering leads to inefficiency, and patch-based feature extraction often fails to capture precise object boundaries, resulting in scale misalignment ...
- **p. 2 / 1. Introduction - extractive PDF cue:** This makes it difficult to maintain semantic coherence across views and often leads to artifacts in the rendered novel views.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, their reliance on exhaustive multi-scale rendering leads to inefficiency, and patch-based feature extraction often fails to capture precise object boundaries, resulting ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | For each pixel v, its semantic feature Fi(v) can be expressed as: F_i ( v) = \t e xt {CLIP}(I_t \odot M_i(v)), ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | pixel, semantic, feature, expressed, F_i, CLIP, I_t, odot, M_i, label | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | However, some, methods, rely, multi-scale, patch, averaging, pixellevel | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: pixel, semantic, feature, expressed, F_i, CLIP, I_t, odot, M_i, label | p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 2 (1. Introduction), p. 3 (3.2. Two-Level Semantic Feature Extraction) |
| Decision / output variable | geometry/map/query r; body terms: main, contributions, summarized, follows, novel, framework, CCL-LGS, integrates | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: jointly, optimize, semantic, features, Gaussians, parameters, MLP, decoder | p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 5 (3.3. Contrastive Codebook Learning), p. 5 (3.3. Contrastive Codebook Learning) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 5 (3.3. Contrastive Codebook Learning) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4. Experiments), p. 6 (4.1. Experiments on LERF), p. 1 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** This makes it difficult to maintain semantic coherence across views and often leads to artifacts in the rendered novel views.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 5 (3.3. Contrastive Codebook Learning)): The main contributions of our work can be summarized as follows: • We propose a novel framework, CCL-LGS, which integrates view-consistent semantic supervision to enable the reconstruction of 3D Gaussian ...

- **p. 2 / 1. Introduction - extractive PDF cue:** Owing to its proficiency in 3D open-vocabulary scene understanding, our method could benefit a variety of downstream applications.
- **p. 3 / 3. Method - extractive PDF cue:** In this section, we present our proposed framework, CCLLGS, for view-consistent 3D semantic reconstruction.
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive PDF cue:** In our method, a uniform 32×32 point prompt is provided to SAM to generate three types of masks corresponding to the semantic scales of subparts, ...
- **p. 5 / 3.3. Contrastive Codebook Learning - extractive PDF cue:** To mitigate the limitations of directly using features derived from imperfect masks, we introduce a codebookbased contrastive learning approach.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Limitations remain due to inherent capabilities of SAM and SAM2, as imperfect masks still affect results. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Future work will refine masks for greater robustness. | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1. Quantitative comparison of our method and LangSplat under three challenging scenarios: Occlusion, Image Blur, and View- ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The dataset's real-world imaging conditions, including severe occlusions and motion blur, make it particularly suited for testing segmentation ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 2 (1. Introduction), p. 3 (3.2. Two-Level Semantic Feature Extraction), p. 4 (3.2. Two-Level Semantic Feature Extraction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 2 (1. Introduction), p. 3 (3.2. Two-Level Semantic Feature Extraction), p. 4 (3.2. Two-Level Semantic Feature Extraction), objective p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 5 (3.3. Contrastive Codebook Learning), p. 5 (3.3. Contrastive Codebook Learning).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
