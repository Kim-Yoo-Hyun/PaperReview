# Problem - RoboNet: Large-Scale Multi-Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v100/dasari20a.html; PDF retrieval source: https://proceedings.mlr.press/v100/dasari20a.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction)): However, when trained in a single environment, robot learning algorithms, including visual foresight and inverse models, do not generalize to large domain variations, such as different robot arms, grippers, viewpoints, ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Robot learning has emerged as a promising tool for taming the complexity and diversity of the real world.
- **p. 1 / Abstract - extractive PDF cue:** Methods based on high-capacity models, such as deep networks, hold the promise of providing effective generalization to a wide range of open-world environments.
- **p. 1 / Abstract - extractive PDF cue:** However, these same methods typically require large amounts of diverse training data to generalize effectively.
- **p. 1 / Abstract - extractive PDF cue:** In contrast, most robotic learning experiments are small-scale, single-domain, and single-robot.
- **p. 1 / Abstract - extractive PDF cue:** This leads to a frequent tension in robotic learning: how can we learn generalizable robotic controllers without having to collect impractically large amounts of data ...
- **p. 2 / 1 Introduction - extractive PDF cue:** However, when trained in a single environment, robot learning algorithms, including visual foresight and inverse models, do not generalize to large domain variations, such as ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We use RoboNet to study the viability of large-scale data-driven robot learning, as a means to attain broad generalization across robots and scenes. show that ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, when trained in a single environment, robot learning algorithms, including visual foresight and inverse models, do not generalize to large domain ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | Inspired by the breadth of the ImageNet dataset [8], we introduce RoboNet, a dataset containing roughly 162,000 trajectories with video and action ... | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF |
| State / latent | Inspired, breadth, ImageNet, dataset, introduce, RoboNet, containing, roughly, trajectories, video | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | Second, study, deep, inverse, models, trained, predict, action | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: Inspired, breadth, ImageNet, dataset, introduce, RoboNet, containing, roughly, trajectories, video | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Decision / output variable | normalized sample or downstream action; body terms: main, contributions, therefore, consist, RoboNet, dataset, experimental, evaluation | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | cross-domain transfer and task performance | p. 6 (Figure/Table caption), p. 13 (C Database Implementation Details), p. 6 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** We use RoboNet to study the viability of large-scale data-driven robot learning, as a means to attain broad generalization across robots and scenes. show that ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Such generalization may either be zero-shot, without any additional data from the target domain, or very fast, using only a modest amount of target domain ...
- **p. 1 / 1 Introduction - extractive PDF cue:** The key motivation for using machine learning in robotics is to build systems that can handle the diversity of open-world environments, which demand the ability ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 12 (C Database Implementation Details)): Our main contributions therefore consist of the RoboNet dataset, and an experimental evaluation that studies our framework for multi-robot, multi-domain model-based reinforcement learning based on extensions of the visual foresight ...

- **p. 1 / 1 Introduction - extractive PDF cue:** Instead, we propose the opposite - using dramatically larger and more varied datasets collected in the real world.
- **p. 1 / 1 Introduction - extractive PDF cue:** Inspired by the breadth of the ImageNet dataset [8], we introduce RoboNet, a dataset containing roughly 162,000 trajectories with video and action sequences recorded from ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We show that, when trained on RoboNet, we can acquire models that generalize in zero shot to novel objects, novel viewpoints, and novel table surfaces.
- **p. 12 / C Database Implementation Details - extractive PDF cue:** We provide code infrastructure that allows a user to filter certain subsets of attributes for training and testing.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Next, we discuss limitations of the dataset and evaluation, and additional directions for future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | While our results demonstrated a large degree of generalization, a number of important limitations remain, which we aim ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 13 (C Database Implementation Details). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), interface p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 13 (C Database Implementation Details), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
