# Problem - Human2LocoMan: Learning Versatile Quadrupedal Manipulation with Human Pretraining

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p122.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p122.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): However, the substantial embodiment gap between humans and quadrupedal robots poses challenges to both data collection and policy transfer.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Quadrupedal robots have demonstrated impressive locomotion capabilities in complex environments, but equipping them with autonomous versatile manipulation skills in a scalable way remains a significant ...
- **p. 1 / Abstract - extractive PDF cue:** In this work, we introduce a cross-embodiment imitation learning system for quadrupedal manipulation, leveraging data collected from both humans and LocoMan, a quadruped equipped with ...
- **p. 1 / Abstract - extractive PDF cue:** Specifically, we develop a teleoperation and data collection pipeline, which unifies and modularizes the observation and action spaces of the human and the robot.
- **p. 1 / Abstract - extractive PDF cue:** To effectively leverage the collected data, we propose an efficient modularized architecture that supports co-training and pretraining on structured modalityaligned data across different embodiments.
- **p. 1 / Abstract - extractive PDF cue:** Additionally, we construct the first manipulation dataset for the LocoMan robot, covering various household tasks in both unimanual and bimanual modes, supplemented by a corresponding ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** However, the substantial embodiment gap between humans and quadrupedal robots poses challenges to both data collection and policy transfer.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** While quadrupedal robots have demonstrated impressive locomotion capabilities in complex environments [1, 2, 3, 4, 5, 6, 7], and recent advances have extended their abilities ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, the substantial embodiment gap between humans and quadrupedal robots poses challenges to both data collection and policy transfer. | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | The trunk is an encoder-decoder Transformer, where the input sequence length and the output sequence length are both fixed, as the number ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF |
| State / latent | trunk, encoder-decoder, Transformer, where, input, sequence, length, output, fixed, number | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | tokenizers, encoders, embodiment-specific, observation, modalities, tokens, latent, space | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: trunk, encoder-decoder, Transformer, where, input, sequence, length, output, fixed, number | p. 6 (III. METHODOLOGY), p. 6 (III. METHODOLOGY), p. 5 (III. METHODOLOGY) |
| Decision / output variable | joint action/torque/footstep; body terms: summary, provides, following, contributions, Human2LocoMan, framework, enables, flexible | p. 2 (I. INTRODUCTION), p. 6 (III. METHODOLOGY), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: general, given, dataset, embodiment, aligned, action, modalities, total | p. 6 (III. METHODOLOGY), p. 6 (III. METHODOLOGY), p. 7 (III. METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (III. METHODOLOGY), p. 7 (III. METHODOLOGY), p. 5 (III. METHODOLOGY) |
| Success / guarantee | progress, balance and terrain robustness | p. 10 (Figure/Table caption), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** While quadrupedal robots have demonstrated impressive locomotion capabilities in complex environments [1, 2, 3, 4, 5, 6, 7], and recent advances have extended their abilities ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To structure the data and bridge the embodiment gap, we align motions of the human and the quadruped within a shared unified coordinate frame.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 6 (III. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY)): In summary, our paper provides the following contributions: • We propose Human2LocoMan, a framework that enables flexible and scalable collection of human demonstrations and teleoperated robot trajectories for learning versatile ...

- **p. 6 / III. METHODOLOGY - extractive PDF cue:** This design preserves modality-specific distributions unique to each embodiment and enables the model to explicitly account for distributional gaps across embodiments, which is core to ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To address these challenges, and drawing inspiration from the LocoMan platform [14]-a quadrupedal robot equipped with two leg-mounted loco-manipulators that offers a versatile foundation for ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** In this section, we present the design and implementation of our system, Human2LocoMan, which integrates teleoperation, data collection, and a Transformer-based architecture for cross-embodied learning.
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** The dataset consists of aligned vision, proprioception, and actions from the human and the robot.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | MXT-Scratch: MXT trained only on the LocoMan data. "L" denotes the larger training set (80 trajectories for SO-Uni, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Additionally, as depicted in Figure 8, MXT-Pretrained consistently achieves lower validation loss than MXT-Scratch, whereas the gap between ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | As shown in Figure 4, this task involves three pairs of shoes, with one pair being out-of-distribution (OOD). | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The policy is rolled out for 24 times with in-distribution (ID) objects and 12 times with out-of-distribution (OOD) ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (III. METHODOLOGY), p. 6 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 7 (III. METHODOLOGY). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 6 (III. METHODOLOGY), p. 6 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 7 (III. METHODOLOGY), objective p. 6 (III. METHODOLOGY), p. 6 (III. METHODOLOGY), p. 7 (III. METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
