# Problem - 3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=GThTiuXgDC; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114156. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): The IRAS task is designed to output an affordance mask region in response to complex, reasoning-based query text, overcoming the limitations of fixed affordance labels and the difficulty of understanding ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** 3D Affordance detection is a challenging problem with broad applications on various robotic tasks.
- **p. 1 / ABSTRACT - extractive body cue:** Existing methods typically formulate the detection paradigm as a label-based semantic segmentation task.
- **p. 1 / ABSTRACT - extractive body cue:** This paradigm relies on predefined labels and lacks the ability to comprehend complex natural language, resulting in limited generalization in open-world scene.
- **p. 1 / ABSTRACT - extractive body cue:** To address these limitations, we reformulate the traditional affordance detection paradigm into Instruction Reasoning Affordance Segmentation (IRAS) task.
- **p. 1 / ABSTRACT - extractive body cue:** This task is designed to output a affordance mask region given a query reasoning text, which avoids fixed categories of input labels.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The IRAS task is designed to output an affordance mask region in response to complex, reasoning-based query text, overcoming the limitations of fixed affordance labels ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, current affordance detection methods also heavily rely on the predefined labels and lack the ability to understand and reason over long contextual text.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The IRAS task is designed to output an affordance mask region in response to complex, reasoning-based query text, overcoming the limitations of ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Given a complex reasoning instruction query Qaff and a point cloud input Pcloud, we feed them into the multimodal point clouds LLM ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Given, complex, reasoning, instruction, query, Qaff, point, cloud, input, Pcloud | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Most, current, LLM, D-LLM, Hong, ShapeLLM, support, scenes | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Given, complex, reasoning, instruction, query, Qaff, point, cloud, input, Pcloud | p. 5 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD) |
| Decision / output variable | action, pose, option or chunk a; body terms: reforming, label-based, semantic, segmentation, task, traditional, affordance, detection | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD) |
| Objective / loss / cost | policy/action modeling objective; cue terms: overall, objective, weighted, losses, determined, mask, txtLtxt, maskLmask | p. 7 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 METHOD), p. 15 (A.4 TRAINING DETAILS), p. 5 (3 METHOD) |
| Success / guarantee | instruction-conditioned task success | p. 8 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, current affordance detection methods also heavily rely on the predefined labels and lack the ability to understand and reason over long contextual text.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD)): By reforming the label-based semantic segmentation task in the traditional affordance detection paradigm into a natural language-driven reasoning affordance segmentation task, our model enables more flexible and context-aware reasoning, ...

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Specifically, we introduce an additional token, <AFF>, into the original LLM vocabulary.
- **p. 3 / 3 METHOD - extractive body cue:** To address these limitations, we introduce a new paradigm formulated as an Instruction Reasoning Affordance Segmentation (IRAS) task as depicted in Fig.
- **p. 4 / 3 METHOD - extractive body cue:** Our framework, 3D AffordanceLLM, as illustrated in Fig.
- **p. 4 / 3 METHOD - extractive body cue:** To harness this capability for 3D affordance perception, we introduce the 3D AffordanceLLM Model, aiming to improve affordance detection in previously unseen contexts.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | 4.2.2 OUT-OF-DISTRIBUTION RESULTS The test in out-of-distribution (ood) datasets is essential to assess the generalization capability of the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Notably, the most substantial performance degradation with about 6% occurs in mIoU when the PC module is removed. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 3 (3 METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 5 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 3 (3 METHOD), objective p. 7 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
