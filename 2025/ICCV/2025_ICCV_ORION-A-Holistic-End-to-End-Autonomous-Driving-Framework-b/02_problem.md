# Problem - ORION: A Holistic End-to-End Autonomous Driving Framework by Vision-Language Instructed Action Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): Besides, limited by the intrinsic autoregressive mechanism of VLMs, the trajectories these method output lack diversity [54], which is inconsistent with the natural uncertainty of human planning [9].

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** End-to-end (E2E) autonomous driving methods still struggle to make correct decisions in interactive closed-loop evaluation due to limited causal reasoning capability.
- **p. 1 / Abstract - extractive PDF cue:** Current methods attempt to leverage the powerful understanding and reasoning abilities of Vision-Language Models (VLMs) to resolve this dilemma.
- **p. 1 / Abstract - extractive PDF cue:** However, the problem is still open that few VLMs for E2E methods perform well in the closed-loop evaluation due to the gap between the semantic ...
- **p. 1 / Abstract - extractive PDF cue:** To tackle this issue, we propose ORION, a hOlistic E2E autonomous dRiving framework by vIsion-language instructed actiON generation.
- **p. 1 / Abstract - extractive PDF cue:** ORION uniquely combines a QT-Former to aggregate long-term history context, a Large Language Model (LLM) for driving scenario reasoning, and a generative planner for precision ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Besides, limited by the intrinsic autoregressive mechanism of VLMs, the trajectories these method output lack diversity [54], which is inconsistent with the natural uncertainty of ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Nevertheless, these methods lack the common sense to complete complex causal reasoning.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Besides, limited by the intrinsic autoregressive mechanism of VLMs, the trajectories these method output lack diversity [54], which is inconsistent with the ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 2, the user instruction Xq, including scene description, history information review, scene analysis, and action reasoning, is first encoded into language tokens ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | user, instruction, including, scene, description, history, information, review, analysis, action | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Other, methods, endeavor, bridge, utilizing, VLM, output, meta-action | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: user, instruction, including, scene, description, history, information, review, analysis, action | p. 4 (3.2. Large Language Model), p. 5 (3.3. Generative Planner), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: tackle, problem, hOlistic, E2E, autonomous, dRiving, framework, vIsion-language | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. QT-Former) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: total, loss, QTFormer, Lqt, Ldet, Ltra, weight, follows | p. 5 (3.4. Training Objectives), p. 5 (3.4. Training Objectives), p. 4 (3.1. QT-Former), p. 4 (3.1. QT-Former) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.4. Training Objectives), p. 4 (3.3. Generative Planner), p. 4 (3.1. QT-Former) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (4.3. Main Results), p. 7 (4.5. Ablation Study) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** Nevertheless, these methods lack the common sense to complete complex causal reasoning.
- **p. 2 / 1. Introduction - extractive PDF cue:** Other methods endeavor to bridge the gap via utilizing VLM output meta-action (e.g., turn left) to assist classic E2E methods [27, 41], as shown in ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. QT-Former), p. 4 (3.3. Generative Planner), p. 4 (3.2. Large Language Model)): To tackle this problem, we propose a hOlistic E2E autonomous dRiving framework by vIsion-language instructed actiON generation, termed ORION.

- **p. 2 / 1. Introduction - extractive PDF cue:** Instead, motivated by OmniDrive [61], which extracts features through Q-Former-styled architecture, we introduce QT-Former, a query-based temporal module.
- **p. 3 / 3.1. QT-Former - extractive PDF cue:** To compress and extract multi-view image features Fm derived from the vision encoder while achieving long-term information modeling, we introduce QT-Former, a querybased temporal module, ...
- **p. 4 / 3.3. Generative Planner - extractive PDF cue:** Inspired by the generative domain, we introduce a generative planner to bridge the gap between the reasoning and action space.
- **p. 4 / 3.2. Large Language Model - extractive PDF cue:** The LLM is pivotal to our framework because the highquality reasoning of the current driving scenario is necessary to instruct the generator to generate a ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | For open-loop evaluation, we use the L2 distance error and the collision rate. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | On the other hand, our model falls behind DriveAdapter in Merging and Give Way, which shows that ORION ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The plain text paradigm performs the worst (42.23 DS, 13.14% SR, and 15.39% mean ability), indicating the limitations ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The model cannot obtain both reasoning and planning capabilities with single-task training. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.2. Large Language Model), p. 5 (3.3. Generative Planner), p. 2 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.2. Large Language Model), p. 5 (3.3. Generative Planner), p. 2 (1. Introduction), p. 2 (1. Introduction), objective p. 5 (3.4. Training Objectives), p. 5 (3.4. Training Objectives), p. 4 (3.1. QT-Former), p. 4 (3.1. QT-Former).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
