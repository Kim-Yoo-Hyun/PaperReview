# Problem - ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): Existing 3D visual grounding (3DVG) methods [7, 12, 13, 36] face challenges in open-vocabulary grounding and reasoning, primarily due to reliance on 3D annotations [37, 39] and mask proposals [2, ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Open-vocabulary 3D visual grounding and reasoning aim to localize objects in a scene based on implicit language descriptions, even when they are occluded.
- **p. 1 / Abstract - extractive PDF cue:** This ability is crucial for tasks such as vision-language navigation and autonomous robotics.
- **p. 1 / Abstract - extractive PDF cue:** However, current methods struggle because they rely heavily on fine-tuning with 3D annotations and mask proposals, which limits their ability to handle diverse semantics and ...
- **p. 1 / Abstract - extractive PDF cue:** In this work, we propose ReasonGrounder, an LVLM-guided framework that uses hierarchical 3D feature Gaussian fields for adaptive grouping based on physical scale, enabling open-vocabulary ...
- **p. 1 / Abstract - extractive PDF cue:** ReasonGrounder interprets implicit instructions using large vision-language models (LVLM) and localizes occluded objects through 3D Gaussian splatting.
- **p. 2 / 1. Introduction - extractive PDF cue:** Existing 3D visual grounding (3DVG) methods [7, 12, 13, 36] face challenges in open-vocabulary grounding and reasoning, primarily due to reliance on 3D annotations [37, ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, challenges remain in interpreting user intent and handling occlusions during object localization.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Existing 3D visual grounding (3DVG) methods [7, 12, 13, 36] face challenges in open-vocabulary grounding and reasoning, primarily due to reliance on ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | LVLM aids in interpreting complex instructions and locating objects even when partially or fully occluded. • (4) Dataset Contributions: A new ReasoningGD ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | LVLM, aids, interpreting, complex, instructions, locating, objects, even, when, partially | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | achieve, open-vocabulary, visual, grounding, reasoning, proposes, ReasonGrounder, novel | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: LVLM, aids, interpreting, complex, instructions, locating, objects, even, when, partially | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: Furthermore, introduce, novel, ReasoningGD, dataset, containing, over, complex | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (Figure/Table caption), p. 5 (4. Experiments), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** However, challenges remain in interpreting user intent and handling occlusions during object localization.
- **p. 1 / 1. Introduction - extractive PDF cue:** In a given scene, the user observes from a perspective with occlusions and asks questions such as: "Can you localize the red, round, sweet fruit ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): Furthermore, we introduce a novel ReasoningGD dataset containing over 10K complex scenes and 263 object types, with a total of approximately 2 million annotations.

- **p. 2 / 1. Introduction - extractive PDF cue:** To achieve open-vocabulary 3D visual grounding and reasoning, this paper proposes ReasonGrounder, a novel LVLM-Guided Hierarchical Feature Splatting method that enables implicit instruction comprehension and ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1. Examples of open-vocabulary 3D visual grounding and reasoning. In a given scene, the user observes from ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | The dataset features multiple object instances with varying levels of occlusion, making it ideal for evaluating the ability ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Existing openvocabulary 3D visual grounding methods struggle with localizing complete objects in novel views with occlusion, limiting their ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 6 (Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 6 (Method), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
