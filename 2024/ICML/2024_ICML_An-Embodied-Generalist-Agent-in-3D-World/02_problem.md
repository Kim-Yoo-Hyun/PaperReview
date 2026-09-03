# Problem - An Embodied Generalist Agent in 3D World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (39 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2311.12871; PDF retrieval source: https://arxiv.org/pdf/2311.12871. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction)): The development of such generalist agents encounters three primary challenges: the lack of suitable datasets, unified models, and effective learning strategies.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Leveraging massive knowledge from large language models (LLMs), recent machine learning models show notable successes in generalpurpose task solving in diverse domains such as computer ...
- **p. 1 / Abstract - extractive body cue:** However, several significant challenges remain: (i) most of these models rely on 2D images yet exhibit a limited capacity for 3D input; (ii) these models ...
- **p. 1 / Abstract - extractive body cue:** We argue these limitations significantly hinder current models from performing real-world tasks and approaching general intelligence.
- **p. 1 / Abstract - extractive body cue:** To this end, we introduce LEO, an embodied multimodal generalist agent that excels in perceiving, grounding, reasoning, planning, and acting in the 3D world.
- **p. 1 / Abstract - extractive body cue:** LEO is trained with a unified task interface, model architecture, and objective in two stages: (i) 3D vision-language (VL) alignment and (ii) 3D vision-language-action (VLA) ...
- **p. 1 / 1. Introduction - extractive body cue:** The development of such generalist agents encounters three primary challenges: the lack of suitable datasets, unified models, and effective learning strategies.
- **p. 1 / 1. Introduction - extractive body cue:** This limitation stands as an obstacle that prevents current models from solving realworld tasks and approaching general intelligence.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The development of such generalist agents encounters three primary challenges: the lack of suitable datasets, unified models, and effective learning strategies. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The leading design principles of LEO are two-fold: 1) It should handle the multi-modal input of egocentric 2D, global 3D, and textual ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | leading, design, principles, LEO, two-fold, should, handle, multi-modal, input, egocentric | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Upon, understanding, reasoning, anticipate, LEO, support, more, sophisticated | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: leading, design, principles, LEO, two-fold, should, handle, multi-modal, input, egocentric | p. 3 (2. Model), p. 4 (2.3. Training & Inference), p. 6 (4.2. Scene-grounded Dialogue and Planning) |
| Decision / output variable | geometry/map/query r; body terms: present, CLIPort, manipulation, object, navigation, Tabs, development, generalist | p. 7 (4.3. Embodied Action in 3D World), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: formulate, learning, objective, LEO, following, Brown, Raffel, prefix | p. 3 (2. Model), p. 3 (2.3. Training & Inference), p. 7 (4.3. Embodied Action in 3D World), p. 7 (4.3. Embodied Action in 3D World) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (2. Model), p. 7 (4.3. Embodied Action in 3D World), p. 7 (4.3. Embodied Action in 3D World) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (Figure/Table caption), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** This limitation stands as an obstacle that prevents current models from solving realworld tasks and approaching general intelligence.

## What the Paper Changes

PDF body contribution framing (p. 7 (4.3. Embodied Action in 3D World), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 7 (4.3. Embodied Action in 3D World)): We present the results of CLIPort manipulation and object navigation in Tabs.

- **p. 1 / 1. Introduction - extractive body cue:** The development of such generalist agents encounters three primary challenges: the lack of suitable datasets, unified models, and effective learning strategies.
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, large-scale unified pretraining and efficient finetuning are under-explored by previous 3D VL models, which are often designed with strong priors (Zhao et al., 2021; ...
- **p. 7 / 4.3. Embodied Action in 3D World - extractive body cue:** Underlined figures indicate zero-shot results on novel scenes (3RScan).

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Figure 1: The proposed embodied generalist agent LEO. It takes egocentric 2D images, 3D point clouds, and texts ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (2. Model), p. 4 (2.3. Training & Inference), p. 6 (4.2. Scene-grounded Dialogue and Planning), p. 3 (2.1. Tokenization). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 3 (2. Model), p. 4 (2.3. Training & Inference), p. 6 (4.2. Scene-grounded Dialogue and Planning), p. 3 (2.1. Tokenization), objective p. 3 (2. Model), p. 3 (2.3. Training & Inference), p. 7 (4.3. Embodied Action in 3D World), p. 7 (4.3. Embodied Action in 3D World).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
