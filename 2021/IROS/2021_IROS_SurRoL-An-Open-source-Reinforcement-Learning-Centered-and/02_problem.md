# Problem - SurRoL: An Open-source Reinforcement Learning Centered and dVRK Compatible Platform for Surgical Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/9635867; PDF retrieval source: https://arxiv.org/pdf/2108.13035. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Ten constructed surgical relevant tasks with difficulty levels and varying scenes are presented for learning-based algorithm evaluation (right).

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Autonomous surgical execution relieves tedious routines and surgeon's fatigue.
- **p. 1 / Abstract - extractive PDF cue:** Recent learning-based methods, especially reinforcement learning (RL) based methods, achieve promising performance for dexterous manipulation, which usually requires the simulation to collect data efficiently and ...
- **p. 1 / Abstract - extractive PDF cue:** The existing learning-based simulation platforms for medical robots suffer from limited scenarios and simplified physical interactions, which degrades the real-world performance of learned policies.
- **p. 1 / Abstract - extractive PDF cue:** In this work, we designed SurRoL, an RL-centered simulation platform for surgical robot learning compatible with the da Vinci Research Kit (dVRK).
- **p. 1 / Abstract - extractive PDF cue:** The designed SurRoL integrates a user-friendly RL library for algorithm development and a real-time physics engine, which is able to support more PSM/ECM scenarios and ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Ten constructed surgical relevant tasks with difficulty levels and varying scenes are presented for learning-based algorithm evaluation (right).
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** The modeled trained on such simulated settings may suffer from the reality gap and fail to transfer to the real world [14].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Ten constructed surgical relevant tasks with difficulty levels and varying scenes are presented for learning-based algorithm evaluation (right). | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | SurRoL builds on top of the open-source PyBullet because of its state-of-the-art physics simulation, wide adoption in the machine learning community, and ... | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF |
| State / latent | SurRoL, builds, open-source, PyBullet, because, state-of-the-art, physics, simulation, wide, adoption | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | SurRoL, provides, dVRK, compatible, simulation, environments, surgical, robot | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: SurRoL, builds, open-source, PyBullet, because, state-of-the-art, physics, simulation, wide, adoption | p. 2 (III. METHODS), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Decision / output variable | normalized sample or downstream action; body terms: main, contributions, summarized, follows, design, open-source, surgical, robot | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. METHODS) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | cross-domain transfer and task performance | p. 6 (Figure/Table caption), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** The modeled trained on such simulated settings may suffer from the reality gap and fail to transfer to the real world [14].
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, the existing learning-based platforms only support limited scenarios in the simulated environments [13], [14], detailed in Table I.

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. METHODS), p. 2 (I. INTRODUCTION)): Our main contributions are summarized as follows: • We design an open-source surgical robot learning simulation platform centered on reinforcement learning for surgical skills, which benefits low-cost data collection and ...

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Further, the designed SurRoL with carefully modeled assets can successfully deal with more realistic physical interactions.
- **p. 2 / III. METHODS - extractive PDF cue:** Finally, ten surgical learning-based tasks are built for algorithm development and evaluation.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** SurRoL provides dVRK compatible simulation environments for surgical robot learning (left), with Gym-like interfaces for reinforcement learning algorithm development and ranges of surgical contents with ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | By visually inspecting the training progress, we find that the agents can quickly learn to approach the object ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Meanwhile, the needle picking point is restricted to the jaw tip to avoid unsafe jaw collisions with the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Besides, we find some failure cases resulting from dynamics discrepancies between the simulation and the real world, also ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Fig. 7. Different levels of physical interaction. The object is attached to the jaw if the tip-object distance ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (III. METHODS), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 2 (III. METHODS), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
