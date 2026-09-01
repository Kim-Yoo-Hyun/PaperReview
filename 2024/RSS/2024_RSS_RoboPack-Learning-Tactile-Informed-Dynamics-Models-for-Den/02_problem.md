# Problem - RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p130.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p130.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): At the same time, tasks such as dense packing present significant challenges due to severe occlusions among objects, creating partially observable scenarios where vision alone is insufficient to determine the ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Tactile feedback is critical for understanding the dynamics of both rigid and deformable objects in many manipulation tasks, such as non-prehensile manipulation and dense packing.
- **p. 1 / Abstract - extractive body cue:** We introduce an approach that combines visual and tactile sensing for robotic manipulation by learning a neural, tactile-informed dynamics model.
- **p. 1 / Abstract - extractive body cue:** Our proposed framework, RoboPack, employs a recurrent graph neural network to estimate object states, including particles and object-level latent physics information, from historical visuo-tactile observations ...
- **p. 1 / Abstract - extractive body cue:** Our tactile-informed dynamics model, learned from real-world data, can solve downstream robotics tasks with model-predictive control.
- **p. 1 / Abstract - extractive body cue:** We demonstrate our approach on a real robot equipped with a compliant SoftBubble tactile sensor on non-prehensile manipulation and dense packing tasks, where the robot ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** At the same time, tasks such as dense packing present significant challenges due to severe occlusions among objects, creating partially observable scenarios where vision alone ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** These tasks involve multi-object interactions with complex dynamics that cannot be determined from vision alone.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | At the same time, tasks such as dense packing present significant challenges due to severe occlusions among objects, creating partially observable scenarios ... | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | To formulate this problem, we define the observation space as O, the state space as S, and the action space as A. | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF |
| State / latent | formulate, problem, define, observation, space, state, action, Secondly, estimator, infers | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | State, Estimation, Latent, Physics, Vector, Inference, real-world, robotic | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: formulate, problem, define, observation, space, state, action, Secondly, estimator, infers | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Decision / output variable | contact-aware action/force; body terms: tackle, challenges, learn, dynamics, directly, real, physical, interaction | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD) |
| Objective / loss / cost | contact prediction/control error; cue terms: objective, find, sequence, actions, aH-1, minimize, cost, function | p. 5 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Success / guarantee | slip/contact success and safe interaction | p. 9 (V. EXPERIMENTS), p. 10 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** These tasks involve multi-object interactions with complex dynamics that cannot be determined from vision alone.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To tackle these challenges, in this work, we propose to 1) learn dynamics directly from real physical interaction data using powerful deep function approximators, 2) ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This process is natural for us humans but very challenging for current robotic systems.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 5 (III. METHOD)): To tackle these challenges, in this work, we propose to 1) learn dynamics directly from real physical interaction data using powerful deep function approximators, 2) equip our robotic system with ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** We find that our method can successfully leverage histories of visuo-tactile information to improve prediction, with models trained on just 30 minutes of real-world interaction ...
- **p. 4 / III. METHOD - extractive body cue:** For multi-object packing settings with significant occlusion, we introduce an objective that constrains tracked points to be near the corresponding object masks, providing more consistent ...
- **p. 5 / III. METHOD - extractive body cue:** In the following paragraphs, we describe how our method performs state estimation using history information and future prediction.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | The test objects are more complex than the training set visually, geometrically, and physically, to showcase the generalizability ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Each episode includes various attempts at packing an object into the box and includes pushing and deforming objects, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Metrics such as EMD and CD that emphasize global shape and distribution but are insensitive to subtle positional ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Due to heavy occlusions during task execution, the robot does not have access to meaningful visual feedback during ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), objective p. 5 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
