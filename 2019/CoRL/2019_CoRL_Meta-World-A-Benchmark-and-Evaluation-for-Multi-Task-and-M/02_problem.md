# Problem - Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v100/yu20a.html; PDF retrieval source: https://proceedings.mlr.press/v100/yu20a.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction)): We provide an evaluation protocol with evaluation modes of varying difficulty, and observe that current methods only show success in the easiest modes.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Meta-reinforcement learning algorithms can enable robots to acquire new skills much more quickly, by leveraging prior experience to learn how to learn.
- **p. 1 / Abstract - extractive PDF cue:** However, much of the current research on meta-reinforcement learning focuses on task distributions that are very narrow.
- **p. 1 / Abstract - extractive PDF cue:** For example, a commonly used meta-reinforcement learning benchmark uses different running velocities for a simulated robot as different tasks.
- **p. 1 / Abstract - extractive PDF cue:** When policies are meta-trained on such narrow task distributions, they cannot possibly generalize to more quickly acquire entirely new tasks.
- **p. 1 / Abstract - extractive PDF cue:** Therefore, if the aim of these methods is enable faster acquisition of entirely new behaviors, we must evaluate them on task distributions that are sufficiently ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We provide an evaluation protocol with evaluation modes of varying difficulty, and observe that current methods only show success in the easiest modes.
- **p. 2 / 1 Introduction - extractive PDF cue:** Our empirical evaluation of existing methods on this benchmark reveals that, despite some impressive progress in multi-task and meta-reinforcement learning over the past few years, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We provide an evaluation protocol with evaluation modes of varying difficulty, and observe that current methods only show success in the easiest ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | We evaluate 6 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks. | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | evaluate, state-of-the-art, meta-reinforcement, learning, multi-task, algorithms, tasks, While, reinforcement, achieved | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | contend, multi-task, meta, reinforcement, learning, methods, efficiently, learn | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: evaluate, state-of-the-art, meta-reinforcement, learning, multi-task, algorithms, tasks, While, reinforcement, achieved | p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Decision / output variable | method trajectory/action; body terms: present, benchmark, simulated, manipulation, tasks, everyday, objects, contained | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: While, methods, have, made, progress, development, classes, approaches | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Success / guarantee | comparable score and protocol validity | p. 13 (Figure/Table caption), p. 8 (Figure/Table caption), p. 11 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** Our empirical evaluation of existing methods on this benchmark reveals that, despite some impressive progress in multi-task and meta-reinforcement learning over the past few years, ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Recent works in meta-learning and multi-task reinforcement learning have shown promise for addressing this gap.
- **p. 1 / 1 Introduction - extractive PDF cue:** Recent advances in machine learning have provided unparalleled generalization capabilities in domains such as images [6] and speech [7], suggesting that this should be possible; ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract)): To this end, we present a benchmark of simulated manipulation tasks with everyday objects, all of which are contained in a shared, table-top environment with a simulated Sawyer arm.

- **p. 1 / 1 Introduction - extractive PDF cue:** Multi-task RL methods aim to learn a single policy that can solve multiple tasks more efficiently than learning the tasks individually, while meta-learning methods train ...
- **p. 2 / 1 Introduction - extractive PDF cue:** For example, one popular evaluation of metalearning involves choosing different running directions for simulated legged robots [10], which then enables fast adaptation to new directions.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we propose an open-source simulated benchmark for meta-reinforcement learning and multitask learning consisting of 50 distinct robotic manipulation tasks.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | When policies are meta-trained on such narrow task distributions, they cannot possibly generalize to more quickly acquire entirely ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Our experiments show that current meta-RL methods in fact cannot yet generalize effectively to entirely new tasks and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | This opens the door for future developments in multi-task and meta reinforcement learning: instead of focusing on further ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), interface p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
