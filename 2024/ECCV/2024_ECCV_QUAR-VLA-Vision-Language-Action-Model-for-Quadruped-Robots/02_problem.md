# Problem - QUAR-VLA: Vision-Language-Action Model for Quadruped Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/808_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00808.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction)): However, such a task specification often relies on a single (coarse-grained) goal image instruction, making it difficult to apply in many real-world combination tasks, i.e. requiring combining multiple sub-instructions.

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** Quadruped robots, characterized by their excellent traversability on complex terrains and agile movements, have garnered significant attention in the field of robotics [14].
- **p. 1 / 1 Introduction - extractive PDF cue:** Researchers have extensively employed these robots to explore tasks encompassing autonomous navigation and manipulation [16,17,36]. ⋆Corresponding author
- **p. 2 / 1 Introduction - extractive PDF cue:** Ding et al. "Trot in place, with the front right leg move twice as fast as other legs" (a) QUAR-VA (b) QUAR-LA (c) QUAR-VLA Language ...
- **p. 2 / 1 Introduction - extractive PDF cue:** 1: Comparison of QUAR-VA, QUAR-LA, and QUAR-VLA.
- **p. 2 / 1 Introduction - extractive PDF cue:** QUAR-VA solely utilizes coarse-grained vision information, lacking explicit instructions for handling diverse tasks.
- **p. 2 / 1 Introduction - extractive PDF cue:** However, such a task specification often relies on a single (coarse-grained) goal image instruction, making it difficult to apply in many real-world combination tasks, i.e. ...
- **p. 2 / 1 Introduction - extractive PDF cue:** This task primarily encompasses two challenges.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, such a task specification often relies on a single (coarse-grained) goal image instruction, making it difficult to apply in many real-world ... | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | The policy QUART could be shown as follow: \begin {a li g ned} &\operat orname {QUART}(a_d/s, w) = p(a_d/t) \tau (t/s, w)\\ ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF |
| State / latent | policy, QUART, could, follow, begin, operat, orname, a_d/s, a_d/t, aligned | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | receives, visual, information, observation, outputs, action, representing, actual | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: policy, QUART, could, follow, begin, operat, orname, a_d/s, a_d/t, aligned | p. 8 (3 Method), p. 9 (3 Method), p. 9 (3 Method) |
| Decision / output variable | joint action/torque/footstep; body terms: extensive, evaluation, leads, performant, robotic, policies, enables, QUART | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: standard, categorical, cross-entropy, objective, causal, masking, utilized, prior | p. 5 (3 Method), p. 7 (3 Method), p. 9 (3 Method), p. 9 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (3 Method), p. 7 (3 Method), p. 9 (3 Method) |
| Success / guarantee | progress, balance and terrain robustness | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 13 (1. Comparison within VLM baselines. The experiment results reveal) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** This task primarily encompasses two challenges.
- **p. 3 / 1 Introduction - extractive PDF cue:** To address the simto-real gap caused by the data disparity, we construct a co-training pipeline to effectively distill the knowledge of simulation data for real-scene ...
- **p. 3 / 1 Introduction - extractive PDF cue:** To address these two problems, we collect a large-scale multi-task dataset QUAdruped Robot Dataset (QUARD).
- **p. 4 / 1 Introduction - extractive PDF cue:** 3) Our extensive evaluation shows that our approach leads to performant robotic policies and enables QUART to obtain a range of generalization capabilities.

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method)): Our extensive evaluation shows that our approach leads to performant robotic policies and enables QUART to obtain a range of generalization capabilities.

- **p. 2 / 1 Introduction - extractive PDF cue:** To enable quadruped robots to autonomously navigate and manipulate various tasks, in this paper, we propose a new paradigm: Vision-Language-Action tasks for QUAdruped Robots (QUAR-VLA), ...
- **p. 4 / 1 Introduction - extractive PDF cue:** 2) We present a large-scale multi-task dataset, QUARD, and a Vision-Language-Action model, QUART to solve the QUAR-VLA tasks.
- **p. 5 / 3 Method - extractive PDF cue:** Initially, we present the definition of our proposed QUAR-VLA in Section 3.1.
- **p. 5 / 3 Method - extractive PDF cue:** The policy is a mapping from images and instructions to actions, and can be written as µ : S × W →A, where the action ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 12 | This failure manifests in behaviors such as repetitive motion, misdirection, wrong terminate commands. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | When confronted with unseen instructions, the alighment between the existing language and the integration of vision and action ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | This observation suggests that while visual language models (VLMs) can grasp abstract principles of the world, directly applying ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | 5 Conclusion & Future Work This paper emphasizes the significance of deploying Vision-Language-Action models on quadruped robots. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 8 (3 Method), p. 9 (3 Method), p. 9 (3 Method), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), interface p. 8 (3 Method), p. 9 (3 Method), p. 9 (3 Method), p. 2 (1 Introduction), objective p. 5 (3 Method), p. 7 (3 Method), p. 9 (3 Method), p. 9 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
