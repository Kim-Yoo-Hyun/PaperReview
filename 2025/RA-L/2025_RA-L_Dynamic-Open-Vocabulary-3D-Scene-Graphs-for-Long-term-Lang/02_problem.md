# Problem - Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.11989; PDF retrieval source: https://arxiv.org/pdf/2410.11989. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): This limitation restricts their applicability in real-world scenarios where adaptability is crucial.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Enabling mobile robots to perform long-term tasks in dynamic real-world environments is a formidable challenge, especially when the environment changes frequently due to humanrobot interactions ...
- **p. 1 / Abstract - extractive body cue:** Traditional methods typically assume static scenes, which limits their applicability in the continuously changing real world.
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, we present DovSG, a novel mobile manipulation framework that leverages dynamic open-vocabulary 3D scene graphs and a language-guided task planning module ...
- **p. 1 / Abstract - extractive body cue:** DovSG takes RGB-D sequences as input and utilizes vision-language models (VLMs) for object detection to obtain high-level object semantic features.
- **p. 1 / Abstract - extractive body cue:** Based on the segmented Manuscript received: October 16, 2024; Revised January 2, 2025; Accepted February 4, 2025.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This limitation restricts their applicability in real-world scenarios where adaptability is crucial.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address the challenge of scene perception, our perception module integrates advanced tools such as RecognizeAnything [6], Grounding DINO [7], Segment Anything-2 [8], and CLIP ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This limitation restricts their applicability in real-world scenarios where adaptability is crucial. | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | YAN et al.: DYNAMIC OPEN-VOCABULARY 3D SCENE GRAPHS FOR LONG-TERM LANGUAGE-GUIDED MOBILE MANIPULATION 5 and color information, we process each new observation ... | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF |
| State / latent | YAN, DYNAMIC, OPEN-VOCABULARY, SCENE, GRAPHS, LONG-TERM, LANGUAGE-GUIDED, MOBILE, MANIPULATION, color | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | Update, low-level, memory, After, above, step, local, scene | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: YAN, DYNAMIC, OPEN-VOCABULARY, SCENE, GRAPHS, LONG-TERM, LANGUAGE-GUIDED, MOBILE, MANIPULATION, color | p. 5 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD) |
| Decision / output variable | base plus arm/gripper action; body terms: contributions, follows, novel, robotic, framework, integrates, dynamic, open-vocabulary | p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 2 (III. METHOD) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: Open-vocabuary, Segmentation, maximize, object, recognition, scene, first, apply | p. 2 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), p. 6 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (III. METHOD), p. 2 (III. METHOD), p. 4 (III. METHOD) |
| Success / guarantee | task completion and recovery | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** To address the challenge of scene perception, our perception module integrates advanced tools such as RecognizeAnything [6], Grounding DINO [7], Segment Anything-2 [8], and CLIP ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate ...

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 2 (III. METHOD), p. 1 (I. INTRODUCTION), p. 4 (III. METHOD)): Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate long-term task execution in dynamic ...

- **p. 4 / III. METHOD - extractive body cue:** We propose an efficient method that leverages new RGB-D observations to update the volumetric representation accordingly.
- **p. 2 / III. METHOD - extractive body cue:** DovSG enables mobile robots to perform long-term tasks in indoor environments by constructing dynamic 3D scene graphs and using large language models for task planning.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we enhance robotic capabilities by introducing a novel and practical robotic framework, the DovSG system.
- **p. 4 / III. METHOD - extractive body cue:** To address this issue, we have designed a simple memory update module that can quickly perform local updates to the memory based on new RGB-D ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | 2) Mobile control: Once the target location is determined, we use the A* [34] algorithm to generate a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | A buffer of 0.1 is added to account for potential collisions. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | In the first row, we cropped the point cloud input into anyGrasp within a certain range around the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 5 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD), objective p. 2 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), p. 6 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
