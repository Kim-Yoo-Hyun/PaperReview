# Problem - SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): Noticing these limitations of conventional VLMs, many recent works still prioritize image-level semantic alignment over the understanding of spatial and geometric structures [17, 32, 37].

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Large vision-language models (VLMs) still struggle with reliable 3D spatial reasoning, a core capability for embodied and physical AI systems.
- **p. 1 / Abstract - extractive body cue:** This limitation arises from their inability to capture fine-grained 3D geometry and spatial relationships.
- **p. 1 / Abstract - extractive body cue:** While recent efforts have introduced multi-view geometry transformers into VLMs, they typically fuse only the deep-layer features from vision and geometry encoders, discarding rich hierarchical ...
- **p. 1 / Abstract - extractive body cue:** To overcome this, we propose SpatialStack, a general hierarchical fusion framework that progressively aligns vision, geometry, and language representations across the model hierarchy.
- **p. 1 / Abstract - extractive body cue:** Moving beyond conventional late-stage vision-geometry fusion, SpatialStack stacks and synchronizes multi-level geometric features with the language backbone, enabling the model to capture both local geometric ...
- **p. 2 / 1. Introduction - extractive body cue:** Noticing these limitations of conventional VLMs, many recent works still prioritize image-level semantic alignment over the understanding of spatial and geometric structures [17, 32, 37].
- **p. 2 / 1. Introduction - extractive body cue:** Bridging this gap requires unifying geometric awareness with vision-language reasoning within a single framework, which is a key step toward reliable spatial intelligence.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Noticing these limitations of conventional VLMs, many recent works still prioritize image-level semantic alignment over the understanding of spatial and geometric structures ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | An initial line of work sought to compensate for these weaknesses by integrating explicit geometric inputs (e.g., precomputed point clouds or depth ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | initial, line, sought, compensate, weaknesses, integrating, explicit, geometric, inputs, precomputed | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | models, infer, rich, geometric, attributes, depth, camera, pose | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: initial, line, sought, compensate, weaknesses, integrating, explicit, geometric, inputs, precomputed | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: summarize, contributions, follows, present, first, systematic, analysis, fusion | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 8 (Model) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (5.2. Evaluation), p. 6 (Figure/Table caption), p. 7 (5.1. Training) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Bridging this gap requires unifying geometric awareness with vision-language reasoning within a single framework, which is a key step toward reliable spatial intelligence.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 8 (Model)): We summarize our contributions as follows: • We present the first systematic analysis of how fusion layers across vision encoders, geometry encoders, and LLM decoders affect the granularity of spatial ...

- **p. 2 / 1. Introduction - extractive body cue:** Building on these insights, we introduce SpatialStack, a general hierarchical fusion framework that integrates multi-level geometric features into multimodal LLMs.
- **p. 8 / Model - extractive body cue:** 5 shows that our method maintains robust general capabilities while specializing in spatial-temporal tasks, confirming no catastrophic forgetting.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | We introduced SpatialStack, a hierarchical fusion framework bridging the gap between vision, geometry, and language for robust 3D ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Notably, despite lacking route-planning data during training, it still surpasses all open-source systems on this task, demonstrating robust ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Table 5. General Capabilities Evaluation. Our SpatialStack-5B maintains robust general multimodal and spatial-temporal reason- ing capabilities, demonstrating no ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
