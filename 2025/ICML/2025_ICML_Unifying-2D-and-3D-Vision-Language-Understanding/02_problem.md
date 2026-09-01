# Problem - Unifying 2D and 3D Vision-Language Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=FcTeo26AfZ; PDF retrieval source: https://openreview.net/pdf/6306d082de46d27c14c27436e4597009a5c8371a.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): Given these challenges, is scaling 3D training data the only viable path to bridging this gap, or are there alternative strategies for making 3D models more effective?

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Progress in 3D vision-language learning has been hindered by the scarcity of large-scale 3D datasets.
- **p. 1 / Abstract - extractive PDF cue:** We introduce UniVLG, a unified architecture for 2D and 3D vision-language understanding that bridges the gap between existing 2D-centric models and the rich 3D sensory ...
- **p. 1 / Abstract - extractive PDF cue:** Our approach initializes most model weights from pre-trained 2D models and trains on both 2D and 3D vision-language data.
- **p. 1 / Abstract - extractive PDF cue:** We propose a novel language-conditioned mask decoder shared across 2D and 3D modalities to ground objects effectively in both RGB and RGBD images, outperforming box-based ...
- **p. 1 / Abstract - extractive PDF cue:** To further reduce the domain gap between 2D and 3D, we incorporate 2D-to-3D lifting strategies, enabling UniVLG to utilize 2D data to enhance 3D performance.
- **p. 1 / 1. Introduction - extractive PDF cue:** Given these challenges, is scaling 3D training data the only viable path to bridging this gap, or are there alternative strategies for making 3D models ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The key limitation, however, is dataset availability: while 2D datasets are vast and well-curated, 3D datasets remain scarce and expensive to annotate (Dai et al., ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Given these challenges, is scaling 3D training data the only viable path to bridging this gap, or are there alternative strategies for ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | (D) Example task inputs/outputs for UniVLG. on both visual features and language instructions to ground objects mentioned in the language input. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Example, task, inputs/outputs, UniVLG, visual, features, language, instructions, ground, objects | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Unlike, models, operate, directly, point, clouds, UniVLG, processes | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Example, task, inputs/outputs, UniVLG, visual, features, language, instructions, ground, objects | p. 2 (1. Introduction), p. 3 (3. Method), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: summary, contributions, Unified, D-3D, Visual, Grounding, model, consume | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.1. Supervision Objective) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: incorporate, loss, additional, cost, Hungarian, matching, final, Box | p. 5 (3.1. Supervision Objective), p. 3 (3. Method), p. 5 (3.1. Supervision Objective), p. 4 (3. Method), p. 4 (3. Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3. Method), p. 4 (3. Method), p. 4 (3. Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4.1. Evaluation on 3D Referential Grounding), p. 6 (4.1. Evaluation on 3D Referential Grounding), p. 6 (4. Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** The key limitation, however, is dataset availability: while 2D datasets are vast and well-curated, 3D datasets remain scarce and expensive to annotate (Dai et al., ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We find that when trained exclusively on 3D data, UniVLG achieves state-of-the-art performance across all established benchmarks, outperforming prior methods in comparable settings by more ...
- **p. 2 / 1. Introduction - extractive PDF cue:** UniVLG directly uses sensor point clouds without any mesh pre-processing of the RGB-D input and without relying on ground-truth bounding box proposals, typically used in ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.1. Supervision Objective), p. 3 (3. Method), p. 4 (3. Method)): In summary, our contributions are: • Unified 2D-3D Visual Grounding: We propose a model that can consume and benefit from both 2D and 3D vision-language data. • State-of-the-Art Performance: UniVLG ...

- **p. 1 / 1. Introduction - extractive PDF cue:** In this paper, we introduce UniVLG, a unified 2D-3D visionlanguage model designed to improve 3D understanding by leveraging large-scale 2D data and pre-trained 2D models.
- **p. 5 / 3.1. Supervision Objective - extractive PDF cue:** To address this, we introduce a novel box loss.
- **p. 3 / 3. Method - extractive PDF cue:** The output consists of segmentation masks for each object mentioned in the sentence, a corresponding text span that refers to each segmented object, and optionally, ...
- **p. 4 / 3. Method - extractive PDF cue:** Open-vocabulary mask decoders, such as those in ODIN (Jain et al., 2024) and X-Decoder (Zou et al., 2023), which extend Mask2Former's decoder to accept language ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | We identify three systematic failure modes in our model, illustrated in Figure-5 (see Appendix). | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Classes UniVLG 72.6 53.8 UniVLG w/o 2D-to-3D lifting 71.4 0.0 UniVLG (Upper-Bound) 69.7 84.2 Grounding failures as seen ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 20 | Figure 5. Systematic failure modes of UniVLG: Green boxes and masks are ground-truth, red masks and boxes are ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Our results show that co-training with 3D data does not degrade the performance of the version trained solely ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 3 (3. Method), p. 1 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 3 (3. Method), p. 1 (1. Introduction), p. 2 (1. Introduction), objective p. 5 (3.1. Supervision Objective), p. 3 (3. Method), p. 5 (3.1. Supervision Objective), p. 4 (3. Method), p. 4 (3. Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
