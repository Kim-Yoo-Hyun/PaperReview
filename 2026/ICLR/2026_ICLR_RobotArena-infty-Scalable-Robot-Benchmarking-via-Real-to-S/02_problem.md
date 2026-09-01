# Problem - RobotArena $\infty$: Scalable Robot Benchmarking via Real-to-Sim Translation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=OutljIofvS; PDF retrieval source: https://openreview.net/pdf/4355de50de1431de9a4ef52786c9b5f7f9f124fe.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): While recent years have witnessed substantial progress in developing more capable and general robot policies, their evaluation remains a persistent challenge and lacks standardization.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** The pursuit of robot generalists, instructable agents capable of performing diverse tasks across diverse environments, demands rigorous and scalable evaluation.
- **p. 1 / ABSTRACT - extractive PDF cue:** Yet real-world testing of robot policies remains fundamentally constrained: it is laborintensive, slow, unsafe at scale, and difficult to reproduce.
- **p. 1 / ABSTRACT - extractive PDF cue:** As policies expand in scope and complexity, these barriers only intensify, since defining "success" in robotics often hinges on nuanced human judgments of execution quality.
- **p. 1 / ABSTRACT - extractive PDF cue:** We introduce RobotArena ∞, a new benchmarking framework that overcomes these challenges by shifting VLA evaluation into large-scale simulated environments augmented with online human feedback.
- **p. 1 / ABSTRACT - extractive PDF cue:** Leveraging advances in vision-language models, 2D-to-3D generative modeling, and differentiable rendering, our approach automatically converts video demonstrations from widely used robot datasets into simulated counterparts.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** While recent years have witnessed substantial progress in developing more capable and general robot policies, their evaluation remains a persistent challenge and lacks standardization.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Notable examples include the Amazon Picking Challenge Correll et al.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While recent years have witnessed substantial progress in developing more capable and general robot policies, their evaluation remains a persistent challenge and ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | First, vision-language-action (VLA) models are highly sensitive to dataset differences: performance drops when they are tested in environments outside their training distribution, ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | First, vision-language-action, VLA, models, highly, sensitive, dataset, differences, performance, drops | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | introduce, RobotArena, benchmarking, framework, overcomes, challenges, shifting, VLA | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: First, vision-language-action, VLA, models, highly, sensitive, dataset, differences, performance, drops | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Decision / output variable | method trajectory/action; body terms: RobotArena, introduce, benchmarking, framework, scales, robot, evaluation, deploying | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: However, high, cost, organizers, participants, means, events, occur | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Success / guarantee | comparable score and protocol validity | p. 24 (Figure/Table caption), p. 22 (Figure/Table caption), p. 24 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Notable examples include the Amazon Picking Challenge Correll et al.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Second, even within the same environment, performance degrades under perturbations, showing that robustness to distribution shifts remains an open challenge.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Our benchmark is not without limitations.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We present key evaluation results that reveal how current robot policies generalize-or fail to-under distribution shifts.

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): RobotArena ∞: We introduce RobotArena ∞, a new benchmarking framework that scales robot evaluation by deploying policies in automatically constructed simulated environments and assessing them through automatic VLM score and ...

- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We present key evaluation results that reveal how current robot policies generalize-or fail to-under distribution shifts.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We introduce a fully automated reality-to-simulation translation pipeline built upon VLMs, 2D-to-3D generative models and differentiable rendering.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** (2024), a largescale, crowdsourced evaluation framework that benchmarks LLMs and VLMs through direct pairwise ∗Equal contribution
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** RobotArena ∞is inspired by prior efforts to design scalable robot benchmarks, particularly the seminal contributions of BEHAVIOR (Li et al., 2024) and SIMPLER (Li et ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Intuitively, this focuses evaluation on the terminal phase of execution, where task completion (or failure) is most evident. | reported limitation/failure wording; scope must be verified |
| body cue at p. 24 | Figure 19: Example VLM-generated task evaluation curves on perturbed environments. Top: A successful pick-and-place execution-after the object lift ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Our benchmark is not without limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | For example, in RH20TSim, RoboVLM (19.05%) achieves a substantially higher score than all other models, while X-VLA fails ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), interface p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
