# Problem - Towards CLIP-driven Language-free 3D Visual Grounding via 2D-3D Relational Enhancement and Consistency

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Towards_CLIP-driven_Language-free_3D_Visual_Grounding_via_2D-3D_Relational_Enhancement_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_Towards_CLIP-driven_Language-free_3D_Visual_Grounding_via_2D-3D_Relational_Enhancement_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): Although language-free training based on implicit feature substitution looks promising for various 2D visionlanguage tasks, it encounters several specific challenges when applied to 3D point clouds: (1) Insufficient 3Dlanguage alignment ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** 3D visual grounding plays a crucial role in scene understanding, with extensive applications in AR/VR.
- **p. 1 / Abstract - extractive body cue:** Despite the significant progress made in recent methods, the requirement of dense textual descriptions for each individual object, which is time-consuming and costly, hinders their ...
- **p. 1 / Abstract - extractive body cue:** To mitigate reliance on text annotations during training, researchers have explored language-free training paradigms in the 2D field via explicit text generation or implicit feature ...
- **p. 1 / Abstract - extractive body cue:** Nevertheless, unlike 2D images, the complexity of spatial relations in 3D, coupled with the absence of robust 3D visual language pre-trained models, makes it challenging ...
- **p. 1 / Abstract - extractive body cue:** To tackle the above issues, in this paper, we introduce a language-free training framework for 3D visual grounding.
- **p. 2 / 1. Introduction - extractive body cue:** Although language-free training based on implicit feature substitution looks promising for various 2D visionlanguage tasks, it encounters several specific challenges when applied to 3D point ...
- **p. 1 / 1. Introduction - extractive body cue:** However, training current 3DVG models demands sufficient detailed text descriptions of each object, which are time-consuming and costly to acquire.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Although language-free training based on implicit feature substitution looks promising for various 2D visionlanguage tasks, it encounters several specific challenges when applied ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | During training phase, the inputs consist of two parts: a point cloud P ∈RN×(3+F ) (with 3D coordinates and F-dimensional auxiliary features) ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | During, training, phase, inputs, consist, parts, point, cloud, coordinates, F-dimensional | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Different, training, process, inference, stage, input, point, cloud | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: During, training, phase, inputs, consist, parts, point, cloud, coordinates, F-dimensional | p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 5 (3.4. Training and Inference) |
| Decision / output variable | geometry/map/query r; body terms: Overall, contributions, summarized, follows, introduce, CLIP-driven, language-free, DVG | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overview) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: describe, methods, augmenting, pseudo-language, features, more, neighboring, relation | p. 3 (3. Methodology), p. 3 (3.1. Overview), p. 5 (3.4. Training and Inference), p. 5 (3.3. Relation Injection) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.4. Training and Inference), p. 5 (3.4. Training and Inference), p. 4 (3.3. Relation Injection) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.2. Implementation Details), p. 6 (Figure/Table caption), p. 5 (4.2. Implementation Details) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** However, training current 3DVG models demands sufficient detailed text descriptions of each object, which are time-consuming and costly to acquire.
- **p. 2 / 1. Introduction - extractive body cue:** However, existing methods tend to neglect the relation modeling during pseudo-language feature synthesis.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overview), p. 4 (3.1. Overview), p. 4 (3.3. Relation Injection)): Overall, our contributions can be summarized as follows: • We introduce a CLIP-driven language-free 3DVG framework, which requires no manually annotated texts to effectively achieve 3D visual grounding on point ...

- **p. 2 / 1. Introduction - extractive body cue:** To address the above issues, we propose a LanguageFree training method for 3D Visual Grounding, named 3DLFVG.
- **p. 3 / 3.1. Overview - extractive body cue:** The objective of our method is to train a model to localize specified objects without using any language queries during training, yet capable of identifying ...
- **p. 4 / 3.1. Overview - extractive body cue:** Since our method capitalizes on the image-text feature alignment provided by CLIP, and incorporates extra modules that enhance the features with relation-aware capabilities.
- **p. 4 / 3.3. Relation Injection - extractive body cue:** (2) Since there is no supervision of this relation during our training process, we introduce the proxy task of predicting the target object to achieve ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Extensive experiments conducted on mainstream datasets demonstrate the robustness and efficiency of our approach. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | It does not have a red chair near it. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Table 3. Ablation study on main components of our method. We report the "overall" results in terms of ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 5 (3.4. Training and Inference), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 5 (3.4. Training and Inference), p. 2 (1. Introduction), objective p. 3 (3. Methodology), p. 3 (3.1. Overview), p. 5 (3.4. Training and Inference), p. 5 (3.3. Relation Injection).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
