# Problem - ScanQA: 3D Question Answering for Spatial Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.10482; PDF retrieval source: https://arxiv.org/pdf/2112.10482. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): For example, 2D images lack an accurate sense of the relative directions and distances in the 3D scenes, i.e., the stereoscopic attribute-perception problem.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We propose a new 3D spatial understanding task for 3D question answering (3D-QA).
- **p. 1 / Abstract - extractive PDF cue:** In the 3D-QA task, models receive visual information from the entire 3D scene of a rich RGB-D indoor scan and answer given textual questions about ...
- **p. 1 / Abstract - extractive PDF cue:** Unlike the 2D-question answering of visual question answering, the conventional 2D-QA models suffer from problems with spatial understanding of object alignment and directions and fail ...
- **p. 1 / Abstract - extractive PDF cue:** We propose a baseline model for 3D-QA, called the ScanQA1, which learns a fused descriptor from 3D object proposals and encoded sentence embeddings.
- **p. 1 / Abstract - extractive PDF cue:** This learned descriptor correlates language expressions with the underlying geometric features of the 3D scan and facilitates the regression of 3D bounding boxes to determine ...
- **p. 1 / 1. Introduction - extractive PDF cue:** For example, 2D images lack an accurate sense of the relative directions and distances in the 3D scenes, i.e., the stereoscopic attribute-perception problem.
- **p. 1 / 1. Introduction - extractive PDF cue:** When multiple images are used in 2Dimage-based question answering models, such models often encounter difficulties in tracking and recognizing whether some objects are the same ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | For example, 2D images lack an accurate sense of the relative directions and distances in the 3D scenes, i.e., the stereoscopic attribute-perception ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The 3D-QA is formalized as follows: given inputs of the point cloud p ∈P and question q ∈Q about the 3D scene, ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | D-QA, formalized, follows, given, inputs, point, cloud, question, about, scene | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Given, point, cloud, RGB, frame, sequence, capture, indoor | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: D-QA, formalized, follows, given, inputs, point, cloud, question, about, scene | p. 4 (4. ScanQA Model), p. 4 (4. ScanQA Model), p. 5 (4. ScanQA Model) |
| Decision / output variable | geometry/map/query r; body terms: introduce, task, question, answering, modeling, present, overview, Fig | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: consider, multiple, answers, compute, final, scores, binary, cross-entropy | p. 5 (4. ScanQA Model), p. 5 (4. ScanQA Model) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4. ScanQA Model), p. 5 (4. ScanQA Model) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 13 (Figure/Table caption), p. 8 (5.4. Qualitative Analysis), p. 1 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** When multiple images are used in 2Dimage-based question answering models, such models often encounter difficulties in tracking and recognizing whether some objects are the same ...
- **p. 2 / 1. Introduction - extractive PDF cue:** are still limited in terms of dataset size and question variety because existing datasets often rely on template-based question-answer collections.
- **p. 2 / 1. Introduction - extractive PDF cue:** We assume that this is plausible when the model can use the preliminarily captured visual information from the 3D scene because of prior navigation in ...

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4. ScanQA Model), p. 5 (4. ScanQA Model)): We introduce the new task of question answering for 3D modeling.

- **p. 2 / 1. Introduction - extractive PDF cue:** We present the overview of the task in Fig.
- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we propose a 3D question answering (3DQA) task that uses 3D spatial information instead of 2D images to comprehend real-world information through ...
- **p. 4 / 4. ScanQA Model - extractive PDF cue:** We introduce the baseline model of ScanQA for the 3DQA task.
- **p. 5 / 4. ScanQA Model - extractive PDF cue:** This layer consists of object localization, object classification, and answer classification modules.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Table 5. Feature ablation results ground-truth answers. We also included sentence evalua- tion metrics frequently used for image ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (4. ScanQA Model), p. 4 (4. ScanQA Model), p. 5 (4. ScanQA Model), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (4. ScanQA Model), p. 4 (4. ScanQA Model), p. 5 (4. ScanQA Model), p. 1 (1. Introduction), objective p. 5 (4. ScanQA Model), p. 5 (4. ScanQA Model).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
