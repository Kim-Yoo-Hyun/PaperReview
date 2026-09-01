# Problem - Learning Latent Plans from Play

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v100/lynch20a.html; PDF retrieval source: https://arxiv.org/pdf/1903.01973. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): This presents a challenge for conventional methods-if a slight variation of a skill is needed, e.g. opening a drawer by grasping the handle from the top down rather than bottom ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Acquiring a diverse repertoire of general-purpose skills remains an open challenge for robotics.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose self-supervising control on top of human teleoperated play data as a way to scale up skill learning.
- **p. 1 / Abstract - extractive body cue:** Play has two properties that make it attractive compared to conventional task demonstrations.
- **p. 1 / Abstract - extractive body cue:** Play is cheap, as it can be collected in large quantities quickly without task segmenting, labeling, or resetting to an initial state.
- **p. 1 / Abstract - extractive body cue:** Play is naturally rich, covering ∼4x more interaction space than task demonstrations for the same amount of collection time.
- **p. 1 / 1 Introduction - extractive body cue:** This presents a challenge for conventional methods-if a slight variation of a skill is needed, e.g. opening a drawer by grasping the handle from the ...
- **p. 1 / 1 Introduction - extractive body cue:** Additionally, using reinforcement learning in complex settings such as robotics requires overcoming significant exploration challenges, typically addressed by introducing manual scripting primitives to an unsupervised ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This presents a challenge for conventional methods-if a slight variation of a skill is needed, e.g. opening a drawer by grasping the ... | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | Algorithm 2 Training Play-LMP 1: Input: Play data D : {(s1, a1), · · · , (sT , aT )} 2: Randomly ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF |
| State / latent | Algorithm, Training, Play-LMP, Input, Play, data, Randomly, initialize, model, parameters | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | Goals, image, experiments, only, output, visual, embedder, treated | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: Algorithm, Training, Play-LMP, Input, Play, data, Randomly, initialize, model, parameters | p. 12 (A.1 Theoretical Motivation), p. 2 (1 Introduction), p. 12 (A.2 Architecture Details) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: alternative, means, obtaining, task-agnostic, control-self-supervising, unlabeled, teleoperated, play | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 12 (A.2 Architecture Details) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: updated, version, Mujoco, HAPTIX, system, collect, teleoperation, demonstration | p. 15 (A.3.4 Training Data) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 15 (A.3.4 Training Data) |
| Success / guarantee | closed-loop task success and robustness | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** Additionally, using reinforcement learning in complex settings such as robotics requires overcoming significant exploration challenges, typically addressed by introducing manual scripting primitives to an unsupervised ...
- **p. 2 / 1 Introduction - extractive body cue:** Unfortunately, it is difficult to obtain datasets with this sort of coverage (Fig.
- **p. 2 / 1 Introduction - extractive body cue:** To generalize to the widest variety of tasks at test time (indexed by the pair (sc, sg)), it stands that the agent should see the ...
- **p. 3 / 1 Introduction - extractive body cue:** (a) The ideal coverage is dense and broad over all regions of the space, providing statistical support for all pairs of (current state, goal state).

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 3 (1 Introduction), p. 12 (A.2 Architecture Details), p. 1 (1 Introduction), p. 12 (A.2 Architecture Details)): In this work, we propose an alternative means of obtaining task-agnostic control-self-supervising on top of unlabeled teleoperated play data: continuous logs of low-level observations and actions collected while a human ...

- **p. 3 / 1 Introduction - extractive body cue:** 3, we propose two self-supervised methods for learning task-agnostic control from play: Play-GCBC and Play-LMP.
- **p. 12 / A.2 Architecture Details - extractive body cue:** Action space Our 8-DOF agent's action space state consists of: 3 cartesian coordinates for the position of its end effector, 3 Euler angles representing its ...
- **p. 1 / 1 Introduction - extractive body cue:** Unfortunately, designing reward functions for robotic skills is very challenging, especially when learning from raw observations, typically requiring manually-designed perception systems.
- **p. 12 / A.2 Architecture Details - extractive body cue:** 9 we show the layers with their sizes and depths of different sub-networks used in the model: the vision network, plan recognition network, plan proposal ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 16 | Figure 13: Naturally emerging retrying behavior: example run of Play-LMP policy on "grasp upright" task (grasping an object ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | The question of out-of-distribution generalization-say, playing in the living room and generalizing to the kitchen-is left to future ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Emergent Retrying: We find qualitative evidence that play-supervised models, unlike models trained solely on expert demonstrations, make multiple ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Future work includes exploring whether generalization is possible to novel objects or novel environments, as well as exploring ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 12 (A.1 Theoretical Motivation), p. 2 (1 Introduction), p. 12 (A.2 Architecture Details), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 12 (A.1 Theoretical Motivation), p. 2 (1 Introduction), p. 12 (A.2 Architecture Details), p. 2 (1 Introduction), objective p. 15 (A.3.4 Training Data).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
