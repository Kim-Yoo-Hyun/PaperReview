# Problem - OpenMask3D: Open-Vocabulary 3D Instance Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.13631; PDF retrieval source: https://arxiv.org/pdf/2306.13631. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction)): Hence, the second key problem with closed-vocabulary approaches is their inherent limitation to recognize only object classes that are predefined at training time.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We introduce the task of open-vocabulary 3D instance segmentation.
- **p. 1 / Abstract - extractive PDF cue:** Current approaches for 3D instance segmentation can typically only recognize object categories from a pre-defined closed set of classes that are annotated in the training ...
- **p. 1 / Abstract - extractive PDF cue:** This results in important limitations for real-world applications where one might need to perform tasks guided by novel, open-vocabulary queries related to a wide variety ...
- **p. 1 / Abstract - extractive PDF cue:** Recently, open-vocabulary 3D scene understanding methods have emerged to address this problem by learning queryable features for each point in the scene.
- **p. 1 / Abstract - extractive PDF cue:** While such a representation can be directly employed to perform semantic segmentation, existing methods cannot separate multiple object instances.
- **p. 2 / 1 Introduction - extractive PDF cue:** Hence, the second key problem with closed-vocabulary approaches is their inherent limitation to recognize only object classes that are predefined at training time.
- **p. 2 / 1 Introduction - extractive PDF cue:** In an attempt to address and overcome the limitations of a closed-vocabulary setting, there has been a growing interest in open-vocabulary approaches.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Hence, the second key problem with closed-vocabulary approaches is their inherent limitation to recognize only object classes that are predefined at training ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Our pipeline takes as input a collection of posed RGB-D images captured in an indoor scene, and the reconstructed point cloud representation ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | pipeline, takes, input, collection, posed, RGB-D, images, captured, indoor, scene | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Given, posed, RGB-D, images, captured, scene, along, reconstructed | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: pipeline, takes, input, collection, posed, RGB-D, images, captured, indoor, scene | p. 3 (3 Method), p. 6 (3 Method), p. 3 (3 Method) |
| Decision / output variable | path/waypoint/velocity; body terms: contributions, three-fold, introduce, open-vocabulary, instance, segmentation, task, object | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Method) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: experiment, perform, Hungarian, matching, between, predicted, masks, oracle | p. 9 (Model), p. 6 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 9 (Model) |
| Success / guarantee | goal reach with collision-free execution | p. 18 (Figure/Table caption), p. 6 (4 Experiments), p. 19 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** In an attempt to address and overcome the limitations of a closed-vocabulary setting, there has been a growing interest in open-vocabulary approaches.
- **p. 1 / 1 Introduction - extractive PDF cue:** We argue that there are two key problems with closed-vocabulary 3D instance segmentation.

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Method), p. 3 (3 Method), p. 4 (3 Method)): Our contributions are three-fold: • We introduce the open-vocabulary 3D instance segmentation task in which the object instances that are similar to a given text-query are identified. • We propose ...

- **p. 2 / 1 Introduction - extractive PDF cue:** Our approach is intrinsically different from the existing 3D open-vocabulary scene understanding approaches [24, 32, 52] as we propose an instance-based feature computation approach instead ...
- **p. 4 / 3 Method - extractive PDF cue:** Our pipeline consists of four subsequent steps: 1⃝Our approach takes as input posed RGB-D images of a 3D indoor scene along with its reconstructed point ...
- **p. 3 / 3 Method - extractive PDF cue:** The key novelty of our method is that it follows an instance-mask oriented approach, contrary to existing 3D open-vocabulary scene understanding models which typically compute ...
- **p. 4 / 3 Method - extractive PDF cue:** 3, the mask-feature computation module consists of several steps.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 18 | Figure 9: Output of SAM, using only 5 randomly sampled points (visualized as green dots) of the projected ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Table 1: 3D instance segmentation results on the ScanNet200 validation set. Metrics are respectively: AP averaged over an ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | Figure 7: Difference between the bounding boxes obtained by tightly cropping around the projected points from the 3D ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3 Method), p. 6 (3 Method), p. 3 (3 Method), p. 4 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), interface p. 3 (3 Method), p. 6 (3 Method), p. 3 (3 Method), p. 4 (3 Method), objective p. 9 (Model), p. 6 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
