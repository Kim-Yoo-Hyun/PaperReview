# Problem - RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction)): These limitations highlight an ongoing challenge: bridging the gap between surface-level scene description and the deeper spatial comprehension necessary for intuitive interThis CVPR paper is the Open Access version, provided ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Spatial understanding is a crucial capability that enables robots to perceive their surroundings, reason about their environment, and interact with it meaningfully.
- **p. 1 / Abstract - extractive body cue:** In modern robotics, these capabilities are increasingly provided by vision-language models.
- **p. 1 / Abstract - extractive body cue:** However, these models face significant challenges in spatial reasoning tasks, as their training data are based on general-purpose image datasets that often lack sophisticated spatial ...
- **p. 1 / Abstract - extractive body cue:** For example, datasets frequently do not capture reference frame comprehension, yet effective spatial reasoning requires understanding whether to reason from ego-, world- , or object-centric ...
- **p. 1 / Abstract - extractive body cue:** To address this issue, we introduce ROBOSPATIAL, a large-scale dataset for spatial understanding in robotics.
- **p. 1 / 1. Introduction - extractive body cue:** These limitations highlight an ongoing challenge: bridging the gap between surface-level scene description and the deeper spatial comprehension necessary for intuitive interThis CVPR paper is ...
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, a critical limitation of existing VLM training datasets is their inability to capture reference frame understanding (ref. frame) - the way we interpret spatial ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | These limitations highlight an ongoing challenge: bridging the gap between surface-level scene description and the deeper spatial comprehension necessary for intuitive interThis ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The pipeline takes as input a scene dataset Ds that contains RGB images, camera poses (both extrinsic and intrinsic parameters), and oriented ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | pipeline, takes, input, scene, dataset, contains, RGB, images, camera, poses | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Furthermore, critical, limitation, existing, VLM, training, datasets, inability | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: pipeline, takes, input, scene, dataset, contains, RGB, images, camera, poses | p. 4 (3.2. Dataset Generation), p. 4 (3.2. Dataset Generation), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: output, spatial, reasoning, dataset, where, entry, hIi, consists | p. 4 (3.2. Dataset Generation), p. 1 (1. Introduction), p. 4 (3.1. Spatial Relationships) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: spatial, configuration, task, evaluate, visible, object, pairs, appear | p. 5 (3.2. Dataset Generation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Dataset Generation), p. 5 (3.2. Dataset Generation), p. 5 (3.2.3. Question-Answer Generation) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (4.3. Real Robot Experiments), p. 5 (4.1.2. Spatial Understanding Evaluation), p. 8 (4.3. Real Robot Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, a critical limitation of existing VLM training datasets is their inability to capture reference frame understanding (ref. frame) - the way we interpret spatial ...

## What the Paper Changes

PDF body contribution framing (p. 4 (3.2. Dataset Generation), p. 1 (1. Introduction), p. 4 (3.1. Spatial Relationships), p. 5 (3.2. Dataset Generation)): The output is a spatial reasoning dataset D, where each entry di = hIi, qi, ai, lii consists of an image Ii, a question qi, an answer ai, and a ...

- **p. 1 / 1. Introduction - extractive body cue:** This illustration demonstrates how a model trained on ROBOSPATIAL enables human-aligned spatial reasoning within the correct reference frame, supporting task grounding, planning, and detection for ...
- **p. 4 / 3.1. Spatial Relationships - extractive body cue:** Configuration enables robots to understand and interpret the relative positioning of objects, which is crucial for directing navigation, manipulation, and interaction within complex environments.
- **p. 5 / 3.2. Dataset Generation - extractive body cue:** The simulation allows for translation and in-plane rotation of the object.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | To mitigate failure cases arising from poor object grounding, we also include an auxiliary grounding dataset during training, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We also observe that spatial failures in 2D VLMs often stem from errors in projecting 2D predictions into ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Nonetheless, models trained on ROBOSPATIAL produce more accurate predictions, reducing these failure cases and showing the benefit of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Several recent efforts aim to address this by explicitly training VLMs on spatial reasoning tasks, yet many fall ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3.2. Dataset Generation), p. 4 (3.2. Dataset Generation), p. 1 (1. Introduction), p. 5 (3.2.3. Question-Answer Generation). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 4 (3.2. Dataset Generation), p. 4 (3.2. Dataset Generation), p. 1 (1. Introduction), p. 5 (3.2.3. Question-Answer Generation), objective p. 5 (3.2. Dataset Generation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** These limitations highlight an ongoing challenge: bridging the gap between surface-level scene description and the deeper spatial comprehension necessary for intuitive interThis CVPR paper is the Open Access version, provided ... (p. 1, 1. Introduction).
- **Formulation-changing contribution:** This illustration demonstrates how a model trained on ROBOSPATIAL enables human-aligned spatial reasoning within the correct reference frame, supporting task grounding, planning, and detection for manipulation tasks. (p. 1, 1. Introduction).
- **Assumption/failure evidence:** To mitigate failure cases arising from poor object grounding, we also include an auxiliary grounding dataset during training, which provides additional supervision for object reference resolution. (p. 5, 4.1. Setup).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
