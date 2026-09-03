# Problem - 3D Question Answering via only 2D Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=IkhJApkJQ3; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/168051. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3. Preliminaries), p. 5 (3. Preliminaries), p. 4 (3. Preliminaries)): However, both approaches have significant limitations, either being inefficient or failing to capture critical views.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Large vision-language models (LVLMs) have significantly advanced numerous fields.
- **p. 1 / Abstract - extractive body cue:** In this work, we explore how to harness their potential to address 3D scene understanding tasks, using 3D question answering (3D-QA) as a representative example.
- **p. 1 / Abstract - extractive body cue:** Due to the limited training data in 3D, we do not train LVLMs but infer in a zero-shot manner.
- **p. 1 / Abstract - extractive body cue:** Specifically, we sample 2D views from a 3D point cloud and feed them into 2D models to answer a given question.
- **p. 1 / Abstract - extractive body cue:** When the 2D model is chosen, e.g., LLAVA-OV, the quality of sampled views matters the most.
- **p. 2 / 1. Introduction - extractive body cue:** However, both approaches have significant limitations, either being inefficient or failing to capture critical views.
- **p. 2 / 1. Introduction - extractive body cue:** To tackle the challenges, we introduce a new framework cdViews to select critical and diverse Views <Question>: What is the black couch facing? <Answer>: Coffee ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, both approaches have significant limitations, either being inefficient or failing to capture critical views. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | It takes the question embedding Q and the visual embedding set {Vi}N i=1 as input and outputs a binary label ˆSi (0 ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | takes, question, embedding, visual, input, outputs, binary, label, Since, LVLMs | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | respectively, uniform, sampling, image, retrieval, cdViews, select, views | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: takes, question, embedding, visual, input, outputs, binary, label, Since, LVLMs | p. 6 (3. Preliminaries), p. 3 (3. Preliminaries), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: cdViews, novel, automatically, selecting, critical, diverse, Views, D-QA | p. 1 (Abstract), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: mismatch, loss, optimize, parameters, viewSelector, score, supervised, corresponding | p. 2 (1. Introduction), p. 6 (3. Preliminaries), p. 6 (3. Preliminaries) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Preliminaries) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (5. Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** To tackle the challenges, we introduce a new framework cdViews to select critical and diverse Views <Question>: What is the black couch facing? <Answer>: Coffee ...
- **p. 5 / 3. Preliminaries - extractive body cue:** It relies on the semantic similarity between questions and views, which introduces two key limitations: 1) Missing Critical Views.
- **p. 5 / 3. Preliminaries - extractive body cue:** This limitation stems from the fundamental difference between object identification and relationship comprehension, and the latter requiring stronger understanding capabilities.
- **p. 4 / 3. Preliminaries - extractive body cue:** In the following, we first present a problem formulation for zero-shot 3D-QA, followed by experiments using two intuitive view selection methods: uniform sampling and image ...

## What the Paper Changes

PDF body contribution framing (p. 1 (Abstract), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries)): We propose cdViews, a novel approach to automatically selecting critical and diverse Views for 3D-QA. cdViews consists of two key components: viewSelector prioritizing critical views based on their potential to ...

- **p. 1 / 1. Introduction - extractive body cue:** All of these methods require computationally intensive 3D-language alignment using point cloud data for spatial reasoning. a4 is our method that leverages pre-trained LVLMs operating ...
- **p. 2 / 1. Introduction - extractive body cue:** (2) We introduce cdViews that integrates a viewSelector with a viewNMS to capture critical and diverse views.
- **p. 2 / 1. Introduction - extractive body cue:** To tackle the challenges, we introduce a new framework cdViews to select critical and diverse Views <Question>: What is the black couch facing? <Answer>: Coffee ...
- **p. 3 / 3. Preliminaries - extractive body cue:** Since 2D LVLMs are fundamentally designed to process 2D images as input, we propose cdViews to efficiently select the most informative 2D views of 3D ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | The reason is that the uniform sampling method ignores the question and the image retrieval method often fails ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (3. Preliminaries), p. 3 (3. Preliminaries), p. 1 (1. Introduction), p. 4 (3. Preliminaries). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3. Preliminaries), p. 5 (3. Preliminaries), p. 4 (3. Preliminaries), interface p. 6 (3. Preliminaries), p. 3 (3. Preliminaries), p. 1 (1. Introduction), p. 4 (3. Preliminaries), objective p. 2 (1. Introduction), p. 6 (3. Preliminaries), p. 6 (3. Preliminaries).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
