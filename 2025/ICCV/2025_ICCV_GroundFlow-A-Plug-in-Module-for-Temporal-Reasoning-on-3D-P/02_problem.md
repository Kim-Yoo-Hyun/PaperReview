# Problem - GroundFlow: A Plug-in Module for Temporal Reasoning on 3D Point Cloud Sequential Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Lin_GroundFlow_A_Plug-in_Module_for_Temporal_Reasoning_on_3D_Point_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Lin_GroundFlow_A_Plug-in_Module_for_Temporal_Reasoning_on_3D_Point_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction)): While 3D LLMs achieve state-of-the-art results in various 3D tasks, they still face significant difficulty adapting to the complex SG3D problem [52].

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Sequential grounding in 3D point clouds (SG3D) refers to locating sequences of objects by following text instructions for a daily activity with detailed steps.
- **p. 1 / Abstract - extractive PDF cue:** Current 3D visual grounding (3DVG) methods treat text instructions with multiple steps as a whole, without extracting useful temporal information from each step.
- **p. 1 / Abstract - extractive PDF cue:** However, the instructions in SG3D often contain pronouns such as "it", "here" and "the same" to make language expressions concise.
- **p. 1 / Abstract - extractive PDF cue:** This requires grounding methods to understand the context and retrieve relevant information from previous steps to correctly locate object sequences.
- **p. 1 / Abstract - extractive PDF cue:** Due to the lack of an effective module for collecting related historical information, state-of-theart 3DVG methods face significant challenges in adapting to the SG3D task.
- **p. 2 / 1. Introduction - extractive PDF cue:** While 3D LLMs achieve state-of-the-art results in various 3D tasks, they still face significant difficulty adapting to the complex SG3D problem [52].
- **p. 2 / 1. Introduction - extractive PDF cue:** The main reason for the huge performance gap between the two tasks is that current 3DVG methods are not designed to reason over historical information.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While 3D LLMs achieve state-of-the-art results in various 3D tasks, they still face significant difficulty adapting to the complex SG3D problem [52]. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | As shown, GroundFlow module's output ˆJt will be treated as input in the next step t + 1. studied task that requires ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | GroundFlow, module, output, will, treated, input, next, step, studied, task | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Figure, DVG, methods, typically, process, text, instructions, single | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: GroundFlow, module, output, will, treated, input, next, step, studied, task | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: summary, make, following, contributions, GroundFlow, module, recurrent, framework | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Training Objective) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: defined, Equation, loss, compares, predicted, object, score, ground | p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4.4. Ablation Study), p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (4.3. Comparison on SG3D Benchmark) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** The main reason for the huge performance gap between the two tasks is that current 3DVG methods are not designed to reason over historical information.
- **p. 1 / 1. Introduction - extractive PDF cue:** S3 : Sit on the black office chair under that same desk to enjoy your drink O2 : Cup O3 : Chair_2 Chair_1 Grounding Sequences ...
- **p. 1 / 1. Introduction - extractive PDF cue:** An example of SG3D task (above) and a comparison between previous visual grounding framework (bottom left) and our recurrent framework (bottom right) integrated with GroundFlow ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Training Objective)): In summary, we make the following contributions: • We propose the GroundFlow module with a recurrent framework, which can be integrated into previous 3DVG baselines and introduce important temporal reasoning ...

- **p. 2 / 1. Introduction - extractive PDF cue:** In addition, we propose GroundFlow module, which can be built on top of the existing 3DVG methods to perform temporal fusion with previous step embeddings, ...
- **p. 5 / 3.3. Training Objective - extractive PDF cue:** Detailed illustration of Memory component in GroundFlow, which enables the module to extract relevant information of both short-term ( ˆJt-1) and long-term ( ˆJm) effectively.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Their degraded performance is particularly reflected in their overall task accuracy, with three of the models are falling ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | This advantage could stem from the limitations of existing methods: LSTM or GRU tends to forget longterm information. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Since previous step embeddings do not attend to this lost information, it cannot be carried forward to subsequent ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | It is shown that PQ3D fails to correctly choose the target "Telephone", while PQ3D+GroundFlow makes the correct predictions ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), objective p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
