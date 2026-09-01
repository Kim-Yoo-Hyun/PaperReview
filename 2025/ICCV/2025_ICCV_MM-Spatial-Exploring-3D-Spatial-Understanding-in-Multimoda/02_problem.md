# Problem - MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Daxberger_MM-Spatial_Exploring_3D_Spatial_Understanding_in_Multimodal_LLMs_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Daxberger_MM-Spatial_Exploring_3D_Spatial_Understanding_in_Multimodal_LLMs_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 1 (Abstract)): Multimodal large language models (MLLMs) excel at 2D visual understanding but remain limited in their ability to reason about 3D space.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Multimodal large language models (MLLMs) excel at 2D visual understanding but remain limited in their ability to reason about 3D space.
- **p. 1 / Abstract - extractive PDF cue:** In this work, we leverage large-scale high-quality 3D scene data with open-set annotations to introduce 1) a novel supervised fine-tuning dataset and 2) a new ...
- **p. 1 / Abstract - extractive PDF cue:** Our Cubify Anything VQA (CA-VQA) data covers diverse spatial tasks including spatial relationship prediction, metric size and distance estimation, and 3D grounding.
- **p. 1 / Abstract - extractive PDF cue:** We show that CA-VQA enables us to train MM-Spatial, a strong generalist MLLM that also achieves state-of-the-art performance on 3D spatial understanding benchmarks, including our ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Understanding object locations and spatial relationships in both 2D and 3D space is crucial for interpreting complex visual scenes.
- **p. 1 / 1. Introduction - extractive PDF cue:** To address these †Equal contribution.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Multimodal large language models (MLLMs) excel at 2D visual understanding but remain limited in their ability to reason about 3D space. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | MM-Spatial-3B achieves SOTA with both image-only input and tool-use monocular depth, outperforming SpatialRGPT-VILA-1.5-8B (which fully encodes depth). | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | MM-Spatial-3B, achieves, SOTA, image-only, input, tool-use, monocular, depth, outperforming, SpatialRGPT-VILA-1 | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | model, supports, multi-image, input, allowing, concatenate, multiple, views | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: MM-Spatial-3B, achieves, SOTA, image-only, input, tool-use, monocular, depth, outperforming, SpatialRGPT-VILA-1 | p. 8 (Model), p. 1 (1. Introduction), p. 4 (4.1. Model Architecture) |
| Decision / output variable | geometry/map/query r; body terms: address, Equal, contribution, MM-Spatial-3B, achieves, SOTA, image-only, input | p. 1 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (Figure/Table caption), p. 5 (5.1. Model Variants), p. 7 (5.4. CV-Bench Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive PDF cue:** In this work, we leverage large-scale high-quality 3D scene data with open-set annotations to introduce 1) a novel supervised fine-tuning dataset and 2) a new ...

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction)): To address these †Equal contribution.

- additional contribution cue 없음

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | CA-VQA is the first dataset that is based on high-quality 3D ground truth, includes depth maps (both from ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In future work, we aim to extend our scope to outdoor scenes to complement our high-quality indoor dataset. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | MM-Spatial-3B 8 substantially outperforms various (much larger) top opensource and commercial models 1 - 6 , incl. the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Table 6. SpatialRGPT-Bench Results. MM-Spatial-3B achieves SOTA with both image-only input and tool-use monocular depth, out- performing SpatialRGPT-VILA-1.5-8B ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 8 (Model), p. 1 (1. Introduction), p. 4 (4.1. Model Architecture), p. 4 (4.1. Model Architecture). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (Abstract), p. 1 (Abstract), interface p. 8 (Model), p. 1 (1. Introduction), p. 4 (4.1. Model Architecture), p. 4 (4.1. Model Architecture), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
