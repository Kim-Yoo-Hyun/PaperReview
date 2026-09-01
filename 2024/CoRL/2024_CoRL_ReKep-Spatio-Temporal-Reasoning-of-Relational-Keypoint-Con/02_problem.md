# Problem - ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/huang25g.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/huang25g/huang25g.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): However, manual annotation is required per task, thus lacking scalability in open-world settings, which we aim to address in this work.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Representing robotic manipulation tasks as constraints that associate the robot and the environment is a promising way to encode desired robot behaviors.
- **p. 1 / Abstract - extractive body cue:** However, it remains unclear how to formulate the constraints such that they are 1) versatile to diverse tasks, 2) free of manual labeling, and 3) ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce Relational Keypoint Constraints (ReKep), a visually-grounded representation for constraints in robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** Specifically, ReKep is expressed as Python functions mapping a set of 3D keypoints in the environment to a numerical cost.
- **p. 1 / Abstract - extractive body cue:** We demonstrate that by representing a manipulation task as a sequence of Relational Keypoint Constraints, we can employ a hierarchical optimization procedure to solve for ...
- **p. 3 / 1 Introduction - extractive body cue:** However, manual annotation is required per task, thus lacking scalability in open-world settings, which we aim to address in this work.
- **p. 2 / 1 Introduction - extractive body cue:** However, effectively formulating these constraints for a large variety of real-world tasks presents significant challenges.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, manual annotation is required per task, thus lacking scalability in open-world settings, which we aim to address in this work. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | contributions, summarized, follows, formulate, manipulation, tasks, hierarchical, optimization, problem, Relational | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Constrained, Optimization, Solver, RGB-D, Observation, Optimized, Actions, subgoal_stage1_f1 | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: contributions, summarized, follows, formulate, manipulation, tasks, hierarchical, optimization, problem, Relational | p. 2 (1 Introduction), p. 3 (3 Method), p. 4 (3 Method) |
| Decision / output variable | action, pose, option or chunk a; body terms: contributions, summarized, follows, formulate, manipulation, tasks, hierarchical, optimization | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Method) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Namely, stage, optimization, shall, find, end-effector, pose, next | p. 3 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3 Method), p. 5 (3 Method), p. 5 (3 Method) |
| Success / guarantee | instruction-conditioned task success | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** However, effectively formulating these constraints for a large variety of real-world tasks presents significant challenges.
- **p. 2 / 1 Introduction - extractive body cue:** While representing constraints using relative poses between robots and objects is a direct and widely-used approach [1], rigid-body transformations do not depict geometric details, require ...
- **p. 3 / 1 Introduction - extractive body cue:** Self-supervised vision models (e.g., DINO [5, 118]), on the other hand, provide fine-grained pixellevel features useful for various vision and robotic tasks [31, 119-124], but ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Method), p. 1 (1 Introduction), p. 6 (3 Method)): Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline to automatically specify keypoints and ...

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose Relational Keypoint Constraints (ReKep).
- **p. 4 / 3 Method - extractive body cue:** 2, which consists of three stages: grasp, align, and pour.
- **p. 1 / 1 Introduction - extractive body cue:** 1: the robot must grasp at the handle, keep the cup upright while transporting *Denotes equal contribution.
- **p. 6 / 3 Method - extractive body cue:** This enables VLM to reason about 3D rotations with arithmetic operations in 3D Cartesian space, effectively circumventing the need for dealing with alternative 3D rotation ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | The optimization module, on the other hand, does not contribute as much to the failures despite given limited ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | Figure 7: Stationary Dual-Arm Platform. A.2 Wheeled Single-Arm Platform One of our investigated platform is a Franka arm ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 27 | Herein we present additional limitations of the existing system. | reported limitation/failure wording; scope must be verified |
| body cue at p. 27 | Bimanual Coordination: Although we demonstrate the application of ReKep to bimanual manipulation, we also identify several important limitations ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 Introduction), p. 3 (3 Method), p. 4 (3 Method), p. 22 (A.6 Querying Vision-Language Model). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 2 (1 Introduction), p. 3 (3 Method), p. 4 (3 Method), p. 22 (A.6 Querying Vision-Language Model), objective p. 3 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
