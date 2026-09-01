# Problem - Scene-LLM: Extending Language Model for 3D Visual Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Fu_Scene-LLM_Extending_Language_Model_for_3D_Visual_Reasoning_WACV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Fu_Scene-LLM_Extending_Language_Model_for_3D_Visual_Reasoning_WACV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): Current models [15, 19, 42] typically focus on one of these aspects or process them with separate models, hindering their effectiveness in tasks like interactive indoor planning that require both.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** This paper introduces Scene-LLM, a 3D-visuallanguage model that enhances embodied agents' abilities in interactive 3D indoor environments by integrating the reasoning strengths of Large Language ...
- **p. 1 / Abstract - extractive PDF cue:** Scene-LLM adopts a unified 3D visual feature representation, that incorporates dense spatial information and supports scene state updates.
- **p. 1 / Abstract - extractive PDF cue:** The model employs a projection layer to efficiently project these features in the pre-trained textual embedding space, enabling effective interpretation of 3D visual information.
- **p. 1 / Abstract - extractive PDF cue:** Unique to our approach is the integration of both scene-level and egocentric 3D information with a compact hybrid representation.
- **p. 1 / Abstract - extractive PDF cue:** This combination is pivotal for interactive 1*Work done as an intern at Meta AI.
- **p. 2 / 1. Introduction - extractive PDF cue:** Current models [15, 19, 42] typically focus on one of these aspects or process them with separate models, hindering their effectiveness in tasks like interactive ...
- **p. 2 / 1. Introduction - extractive PDF cue:** While existing visuallanguage models (VLMs) [5, 15, 34] have made strides in 2D visual-language understanding, their limited grasp of persistent 3D spatial information often renders ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Current models [15, 19, 42] typically focus on one of these aspects or process them with separate models, hindering their effectiveness in ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | At the egocentric step, 3D frame data and a egocentric instruction are first input to Scene-LLM to describe the current state. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | egocentric, step, frame, data, instruction, first, input, Scene-LLM, describe, current | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | notation, denotes, textual, inputs, include, step-by-step, instructions, data | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: egocentric, step, frame, data, instruction, first, input, Scene-LLM, describe, current | p. 5 (4.3. Inference), p. 5 (4.3. Inference), p. 7 (C VoteNet+MCAN [78]) |
| Decision / output variable | geometry/map/query r; body terms: summary, primary, contributions, introduce, Scene-LLM, D-VLM, connecting, visual | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Then, scene, feature, updated, Equation, Scene-LLM, adopts, unified | p. 5 (4.3. Inference), p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.1. 3D Visual Feature), p. 5 (4.3. Inference) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1. Introduction), p. 4 (4.1. 3D Visual Feature), p. 5 (4.3. Inference) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (5. Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** While existing visuallanguage models (VLMs) [5, 15, 34] have made strides in 2D visual-language understanding, their limited grasp of persistent 3D spatial information often renders ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract), p. 3 (3. 3D-Visual-Language Data Generation), p. 4 (4.1. 3D Visual Feature)): In summary, our primary contributions are: • We introduce Scene-LLM, a 3D-VLM that connecting 3D visual information with LLM and sets new stateof-the-art on 3D-VQA and interactive planning benchmarks; • ...

- **p. 2 / 1. Introduction - extractive PDF cue:** To overcome this, we propose integrating both types of 3D visual information to an unified visual feature in Scene-LLM.
- **p. 1 / Abstract - extractive PDF cue:** Unique to our approach is the integration of both scene-level and egocentric 3D information with a compact hybrid representation.
- **p. 3 / 3. 3D-Visual-Language Data Generation - extractive PDF cue:** Our dataset comprises about 9, 000 indoor scenes from three sources: real indoor scans [14], single rooms from the Habitat-Matterport 3D dataset (hm3d) [53], and ...
- **p. 4 / 4.1. 3D Visual Feature - extractive PDF cue:** This consistency allows both 3D visual information being processed by the same projector layer, reducing computation complexity.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Scene-LLM faces limitations such as LLM input token length, challenges in processing dynamic scenes without a state detector, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | A: To enhance safety, consider laying down anti-slip mats by the sink and in any zones where spills ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | While Q-Former is a robust downsampling technique, it exhibits slightly lower performance compared to direct spatial down-sampling in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | It measures the ability to create precise and robust plans from a high-level goal in 3D interactive environments ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (4.3. Inference), p. 5 (4.3. Inference), p. 7 (C VoteNet+MCAN [78]), p. 4 (3.1. Frame Data Generation). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 5 (4.3. Inference), p. 5 (4.3. Inference), p. 7 (C VoteNet+MCAN [78]), p. 4 (3.1. Frame Data Generation), objective p. 5 (4.3. Inference), p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.1. 3D Visual Feature), p. 5 (4.3. Inference).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
