# Problem - From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=fzmittHfq3; PDF retrieval source: https://openreview.net/pdf/d6aae457099a5d9e50bba1a6bbc48d8756a15c91.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction)): This discrepancy results in a critical gap: current VLAs lack reliable 3D spatial understanding, leading to persistent challenges in generalization and adaptability.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Existing vision-language-action (VLA) models act in 3D real-world but are typically built on 2D encoders, leaving a spatial reasoning gap that limits generalization and adaptability.
- **p. 1 / Abstract - extractive body cue:** Recent 3D integration techniques for VLAs either require specialized sensors and transfer poorly across modalities, or inject weak cues that lack geometry and degrade vision-language ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce FALCON (From Spatial to Action), a novel paradigm that injects rich 3D spatial tokens into the action head.
- **p. 1 / Abstract - extractive body cue:** FALCON leverages spatial foundation models to deliver strong geometric priors from RGB alone, and includes an Embodied Spatial Model that can optionally fuse depth, or ...
- **p. 1 / Abstract - extractive body cue:** To preserve language reasoning, spatial tokens are consumed by a Spatial-Enhanced Action Head rather than being concatenated into the vision-language backbone.
- **p. 2 / 1 Introduction - extractive body cue:** This discrepancy results in a critical gap: current VLAs lack reliable 3D spatial understanding, leading to persistent challenges in generalization and adaptability.
- **p. 2 / 1 Introduction - extractive body cue:** These limitations now form a major bottleneck in developing reliable generalist robot policies.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This discrepancy results in a critical gap: current VLAs lack reliable 3D spatial understanding, leading to persistent challenges in generalization and adaptability. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 3.1 Problem Definition We study the problem of task-oriented robot control, where a robot must interpret visual observations Ot = {I1 t ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Problem, Definition, study, task-oriented, robot, control, where, must, interpret, visual | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | learnable, action, token, tact, appended, corresponding, output, hidden | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Problem, Definition, study, task-oriented, robot, control, where, must, interpret, visual | p. 4 (3 Methodology), p. 5 (3 Methodology), p. 4 (3 Methodology) |
| Decision / output variable | geometry/map/query r; body terms: FALCON, Spatial, Action, novel, paradigm, integrates, richer, more | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Training, Objective, During, process, FALCON, action, sequence, generation | p. 5 (3 Methodology), p. 5 (3 Methodology), p. 6 (3 Methodology), p. 6 (3 Methodology) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3 Methodology), p. 6 (3 Methodology), p. 6 (3 Methodology) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** These limitations now form a major bottleneck in developing reliable generalist robot policies.
- **p. 3 / 1 Introduction - extractive body cue:** To overcome limitation (3) of alignment challenges, we draw inspiration from the brain's division of labor.
- **p. 3 / 1 Introduction - extractive body cue:** For limitation (2) of poor modality transferability, we introduce an Embodied Spatial Model that can optionally integrate extra 3D modalities (e.g., depth, poses).

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (3 Methodology), p. 4 (3 Methodology)): We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection scheme.

- **p. 2 / 1 Introduction - extractive body cue:** Overall Benchmark Bridge Calvin (Zero-shot) Google Robot Calvin Real-World Real-World (Few-Shot) Figure 1 We propose FALCON, a vision-language-action model that achieves robust 3D spatial understanding ...
- **p. 3 / 1 Introduction - extractive body cue:** For limitation (2) of poor modality transferability, we introduce an Embodied Spatial Model that can optionally integrate extra 3D modalities (e.g., depth, poses).
- **p. 4 / 3 Methodology - extractive body cue:** We introduce a lightweight fusion mechanism that aligns and combines these complementary representations (see Sec.
- **p. 4 / 3 Methodology - extractive body cue:** To this end, we propose FALCON, a generalist robot policy that overcomes limitations of prior VLAs by integrating rich geometric priors from spatial foundation models ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | In this work, we introduce FALCON, a vision-language-action model that augments generalist robot policies with robust 3D spatial ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Experiments across both simulation and real-world tasks show that FALCON consistently surpasses existing VLA methods, achieving state-of-the-art performance ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | For real-world tasks, we design settings that span from simple interactions (e.g., lifting a yellow pepper) to long-horizon, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3 Methodology), p. 5 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), interface p. 4 (3 Methodology), p. 5 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), objective p. 5 (3 Methodology), p. 5 (3 Methodology), p. 6 (3 Methodology), p. 6 (3 Methodology).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (27 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** These limitations now form a major bottleneck in developing reliable generalist robot policies. (p. 2, 1 Introduction).
- **Formulation-changing contribution:** We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection scheme. (p. 2, 1 Introduction).
- **Assumption/failure evidence:** For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure. (p. 9, 4 Experiments).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
