# Problem - GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1912.13470; PDF retrieval source: https://arxiv.org/pdf/1912.13470. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): Secondly, it is difficult to obtain large-scale high quality training data [3].

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Object grasping is critical for many applications, which is also a challenging computer vision problem.
- **p. 1 / Abstract - extractive body cue:** However, for clustered scene, current researches suffer from the problems of insufficient training data and the lacking of evaluation benchmarks.
- **p. 1 / Abstract - extractive body cue:** In this work, we contribute a large-scale grasp pose detection dataset with an unified evaluation system.
- **p. 1 / Abstract - extractive body cue:** Our dataset contains 87,040 RGBD image with over 370 million grasp poses.
- **p. 1 / Abstract - extractive body cue:** Meanwhile, our evaluation system directly reports whether a grasping is successful or not by analytic computation, which is able to evaluate any kind of grasp ...
- **p. 1 / 1. Introduction - extractive body cue:** Secondly, it is difficult to obtain large-scale high quality training data [3].
- **p. 1 / 1. Introduction - extractive body cue:** The difference in evaluation metrics makes it difficult to compare these methods directly in an unified manner, while evaluating with real robots would dramatically increase ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Secondly, it is difficult to obtain large-scale high quality training data [3]. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | The key of grasping is to detect the grasp pose given visual inputs (image or point cloud) and has drawn many attentions ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | grasping, detect, grasp, pose, given, visual, inputs, image, point, cloud | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | View, Kinect4A, RealSense, D-Pose, DoF, Grasp, Poses, Rectangle-based | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: grasping, detect, grasp, pose, given, visual, inputs, image, point, cloud | p. 1 (1. Introduction), p. 4 (2 Cams), p. 3 (3.2. Data Collection) |
| Decision / output variable | method trajectory/action; body terms: methodology, building, dataset, Specifically, inspired, previous, literature, two-step | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (3.1. Overview) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: difference, evaluation, metrics, makes, difficult, compare, methods, directly | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (2 Cams) |
| Success / guarantee | comparable score and protocol validity | p. 5 (4.1. Ground-Truth Evaluation), p. 4 (3.4. Evaluation), p. 5 (3.4. Evaluation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** The difference in evaluation metrics makes it difficult to compare these methods directly in an unified manner, while evaluating with real robots would dramatically increase ...
- **p. 2 / 1. Introduction - extractive body cue:** Moreover, embedded with an online evaluation system, our benchmark is able to evaluate current mainstream grasping detection algorithms.

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (3.1. Overview), p. 3 (3.3. Data Annotation)): Our methodology for building the dataset.

- **p. 1 / 1. Introduction - extractive body cue:** Specifically, inspired by previous literature [24], we propose a two-step pipeline to generate tremendous grasp poses for a scene.
- **p. 2 / 3.1. Overview - extractive body cue:** To overcome these issues, we propose a large-scale dataset in clustered scenario with dense and rich annotations for grasp pose prediction named GraspNet.
- **p. 3 / 3.3. Data Annotation - extractive body cue:** Considering all the objects are known, we propose a two stage automated pipeline for grasp pose annotation, which is illustrated in Fig.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | The previous method that pre-computed ground truth for evaluating grasping, no matter collected by human annotation [11] or ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Such evaluation method does not assume the representation of the grasp pose, thus is general in practice. | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Collision detection is also conducted to avoid the collision between grasps and background or other object. where Pj ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | The 6D poses will then be propagated to the remaining frames by: Pj i = cam-1 i cam0Pj ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1. Introduction), p. 4 (2 Cams), p. 3 (3.2. Data Collection), p. 2 (3.1. Overview). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 1 (1. Introduction), p. 4 (2 Cams), p. 3 (3.2. Data Collection), p. 2 (3.1. Overview), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
