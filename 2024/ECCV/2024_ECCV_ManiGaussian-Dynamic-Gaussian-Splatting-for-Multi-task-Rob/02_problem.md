# Problem - ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5194_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05194.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): To address the challenges, previous arts have made great progress in general manipulation policy learning, which can be divided into two categories including perceptive methods and generative methods.

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** Designing autonomous agents for language-conditioned manipulation tasks [2, 11, 28, 30, 57, 58, 60, 61, 75] has been highly desired in the pursuit of artificial ...
- **p. 1 / 1 Introduction - extractive body cue:** In realistic deployment, intelligent robots are usually required to deal with unseen scenarios in novel tasks.
- **p. 1 / 1 Introduction - extractive body cue:** Therefore, comprehending complex 3D structures in the deployment scenes is necessary for the robots to achieve high task success rates across diverse manipulation tasks. ⋆B ...
- **p. 2 / 1 Introduction - extractive body cue:** Lu et al.  Previous ManiGaussian Initial state ... "Stack two rose blocks" 𝒕 𝒕 𝒕+ 𝟏 ...
- **p. 2 / 1 Introduction - extractive body cue:** Representation Gaussian Point Human Instruction Fig.
- **p. 2 / 1 Introduction - extractive body cue:** To address the challenges, previous arts have made great progress in general manipulation policy learning, which can be divided into two categories including perceptive methods ...
- **p. 2 / 1 Introduction - extractive body cue:** However, the perceptive methods heavily rely on multi-view or gripper-mounted cameras to cover the whole workbench to deal with the occlusion problem within unstructured environments, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To address the challenges, previous arts have made great progress in general manipulation policy learning, which can be divided into two categories ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | To learn the manipulation policy effectively, expert demonstrations as offline datasets are provided for imitation learning, where the sample triplets contain the ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | learn, manipulation, policy, effectively, expert, demonstrations, offline, datasets, provided, imitation | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | More, specifically, Gaussian, world, model, contains, representation, network | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: learn, manipulation, policy, effectively, expert, demonstrations, offline, datasets, provided, imitation | p. 5 (3 Approach), p. 5 (3 Approach), p. 8 (3 Approach) |
| Decision / output variable | geometry/map/query r; body terms: contributions, summarized, follows, dynamic, Gaussian, Splatting, framework, learn | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: employ, multi-modal, transformer, PerceiverIO, infer, selection, probability, different | p. 8 (3 Approach), p. 9 (3 Approach), p. 6 (3 Approach), p. 8 (3 Approach), p. 9 (3 Approach) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 Approach), p. 8 (3 Approach), p. 5 (3 Approach) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 11 (4 Experiments), p. 12 (4 Experiments), p. 10 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** However, the perceptive methods heavily rely on multi-view or gripper-mounted cameras to cover the whole workbench to deal with the occlusion problem within unstructured environments, ...
- **p. 3 / 1 Introduction - extractive body cue:** Therefore, our framework can acquire informative supervision in interactive environments by reconstructing the future scene according to the current scene and the robot actions, where ...

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Approach)): Our contributions can be summarized as follows: - We propose a dynamic Gaussian Splatting framework to learn the scenelevel spatiotemporal dynamics in general robotic manipulation tasks, so that the robotic ...

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose a ManiGaussian method that leverages a dynamic Gassuain Splatting framework for multi-task robotic manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** Different from conventional methods which only focus on semantic representation, our method mines the scene-level spatiotemporal dynamics via future scene reconstruction.
- **p. 3 / 1 Introduction - extractive body cue:** We evaluate our ManiGaussian method on the RLBench dataset [26] with 10 tasks and 166 variants, where our method outperforms the state-of-the-art multi-task robotic manipulation ...
- **p. 5 / 3 Approach - extractive body cue:** In this section, we first briefly introduce preliminaries on the problem formulation (Section 3.1), and then we present an overview of our pipeline (Section 3.2).

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 14 | The limitations stem from the necessity of multiple view supervision with camera calibration for the Gaussian Splatting framework. | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Fig. 1: Consider the human instruction "stack two rose blocks", where the task is con- sidered successful if ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | First, based on the front view observation where the gripper shape cannot be seen, our ManiGaussian offers superior ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | We evaluated 25 episodes in the testing set for each task to avoid result bias from noise. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (3 Approach), p. 5 (3 Approach), p. 8 (3 Approach), p. 8 (3 Approach). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 5 (3 Approach), p. 5 (3 Approach), p. 8 (3 Approach), p. 8 (3 Approach), objective p. 8 (3 Approach), p. 9 (3 Approach), p. 6 (3 Approach), p. 8 (3 Approach), p. 9 (3 Approach).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
