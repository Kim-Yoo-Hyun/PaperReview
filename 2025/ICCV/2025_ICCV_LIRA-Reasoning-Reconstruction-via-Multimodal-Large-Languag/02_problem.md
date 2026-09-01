# Problem - LIRA: Reasoning Reconstruction via Multimodal Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): However, existing systems [15, 27, 46, 47] mainly rely on explicit instructions, such as explicitly indicating target objects or categories, to reconstruct instruction-relevant regions, while implicit instruction reasoning is more ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Existing language instruction-guided online 3D reconstruction systems mainly rely on explicit instructions or queryable maps, showing inadequate capability to handle implicit and complex instructions.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we first introduce a reasoning reconstruction task.
- **p. 1 / Abstract - extractive PDF cue:** This task inputs an implicit instruction involving complex reasoning and an RGB-D sequence, and outputs incremental 3D reconstruction of instances that conform to the instruction.
- **p. 1 / Abstract - extractive PDF cue:** To handle this task, we propose LIRA: Language Instructed Reconstruction Assistant.
- **p. 1 / Abstract - extractive PDF cue:** It leverages a multimodal large language model to actively reason about the implicit instruction and obtain instruction-relevant 2D candidate instances and their attributes.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, existing systems [15, 27, 46, 47] mainly rely on explicit instructions, such as explicitly indicating target objects or categories, to reconstruct instruction-relevant regions, while ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Particularly for implicit instructions involving complex reasoning, they are more difficult to handle.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, existing systems [15, 27, 46, 47] mainly rely on explicit instructions, such as explicitly indicating target objects or categories, to reconstruct ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Given an implicit and complex instruction L and posed RGB-D sequences as input, LIRA first incrementally performs geometric reconstruction, and leverages a ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Given, implicit, complex, instruction, posed, RGB-D, sequences, input, LIRA, first | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Online, reconstruction, guided, language, instructions, serves, task, embodied | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Given, implicit, complex, instruction, posed, RGB-D, sequences, input, LIRA, first | p. 3 (3. Method), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: summary, major, contributions, follows, introduce, reasoning, reconstruction, task | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: perceptual, information, progressively, constructed, global, containing, multiple, candidate | p. 4 (3.1.1. Incremental Geometric Reconstruction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 4 (3.1.1. Incremental Geometric Reconstruction), p. 7 (4.5. Runtime Analysis) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.2. Evaluation Metrics), p. 7 (Figure/Table caption), p. 7 (4.5. Runtime Analysis) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** Particularly for implicit instructions involving complex reasoning, they are more difficult to handle.
- **p. 2 / 1. Introduction - extractive PDF cue:** Since geometric reconstruction can be accurately obtained by systems such as Simultaneous Localization and Mapping (SLAM) [12, 16, 17, 55], the main challenge in reasoning ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The target instance based on the current map is within the red box.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): In summary, our major contributions are as follows: • We introduce the reasoning reconstruction task, which requires online 3D reconstruction guided by implicit and complex instructions.

- **p. 2 / 1. Introduction - extractive PDF cue:** To achieve higher-quality instance fusion, we propose TIFF, a Text-enhanced Instance Fusion module operating within a Fragment bounding volume (FBV), which is learning-based and fuses ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | One limitation is that LIRA exhibits relatively low performance in high-precision reconstruction. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Future work will consider further optimization in 3D space. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Erroneous projected pixels caused by occlusion are filtered out. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3. Method), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 1 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 3 (3. Method), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 1 (1. Introduction), p. 2 (1. Introduction), objective p. 4 (3.1.1. Incremental Geometric Reconstruction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
