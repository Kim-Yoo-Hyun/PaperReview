# Learning Latent Plans from Play

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v100/lynch20a.html.
> PDF retrieval source: https://arxiv.org/pdf/1903.01973. Reading tracker status/evidence was not changed.

- Year/Venue: 2020 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Imitation Learning, learning from play, latent plans
- Official paper: https://proceedings.mlr.press/v100/lynch20a.html
- Full-text retrieval: https://arxiv.org/pdf/1903.01973
- Code/Project: https://learning-from-play.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 This presents a challenge for conventional methods-if a slight variation of a skill is needed, e.g. opening a drawer by grasping the handle from the top down rather than bottom up, an ...를 문제로 두고, In this work, we propose an alternative means of obtaining task-agnostic control-self-supervising on top of unlabeled teleoperated play data: continuous logs of low-level observations and actions collected while a human teleoperates the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Acquiring a diverse repertoire of general-purpose skills remains an open challenge for robotics.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose self-supervising control on top of human teleoperated play data as a way to scale up skill learning.
- **p. 1 / Abstract - extractive body cue:** Play has two properties that make it attractive compared to conventional task demonstrations.
- **p. 1 / Abstract - extractive body cue:** Play is cheap, as it can be collected in large quantities quickly without task segmenting, labeling, or resetting to an initial state.
- **p. 1 / Abstract - extractive body cue:** Play is naturally rich, covering ∼4x more interaction space than task demonstrations for the same amount of collection time.
- **p. 1 / 1 Introduction - extractive body cue:** This presents a challenge for conventional methods-if a slight variation of a skill is needed, e.g. opening a drawer by grasping the handle from the ...
- **p. 1 / 1 Introduction - extractive body cue:** Additionally, using reinforcement learning in complex settings such as robotics requires overcoming significant exploration challenges, typically addressed by introducing manual scripting primitives to an unsupervised ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose an alternative means of obtaining task-agnostic control-self-supervising on top of unlabeled teleoperated play data: continuous logs of low-level observations and ...
- **p. 3 / 1 Introduction - extractive body cue:** 3, we propose two self-supervised methods for learning task-agnostic control from play: Play-GCBC and Play-LMP.
- **p. 12 / A.2 Architecture Details - extractive body cue:** Action space Our 8-DOF agent's action space state consists of: 3 cartesian coordinates for the position of its end effector, 3 Euler angles representing its ...
- **p. 1 / 1 Introduction - extractive body cue:** Unfortunately, designing reward functions for robotic skills is very challenging, especially when learning from raw observations, typically requiring manually-designed perception systems.
- **p. 12 / A.2 Architecture Details - extractive body cue:** 9 we show the layers with their sizes and depths of different sub-networks used in the model: the vision network, plan recognition network, plan proposal ...
- **p. 17 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** Our state models were trained on a smaller dataset, up to 180 minutes of play (see Fig 8). "Random": we collected a random exploration dataset ...
- **p. 15 / A.3.4 Training Data - extractive body cue:** We model an 8-dof continuous action space representing agent end effector position, rotation, and gripper control.
- **p. 15 / A.3.4 Training Data - extractive body cue:** Tasks are specified to goal-conditioned models by resetting the environment to the initial state of the demonstration, and feeding in the final state as the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Algorithm 2 Training Play-LMP 1: Input: Play data D : {(s1, a1), · · · , (sT , aT )} 2: Randomly initialize model parameters θ = {θV , θCG, θπLMP , ... | observation history와 expert trajectory/action | p. 12 (A.1 Theoretical Motivation), p. 2 (1 Introduction) |
| State/latent | Algorithm, Training, Play-LMP, Input, Play, data, Randomly, initialize, model, parameters, LMP, while | behavior policy와 temporal action context | p. 12 (A.1 Theoretical Motivation), p. 2 (1 Introduction), p. 12 (A.2 Architecture Details) |
| Output/action | (a) Training: 1) sample a random window of experience from a memory of play data; 2) train to recognize and organize a repertoire of behaviors executed during play in a latent plan ... | predicted action 또는 action chunk | p. 2 (1 Introduction), p. 12 (A.2 Architecture Details), p. 2 (1 Introduction) |
| Objective/outcome | An updated version of the Mujoco HAPTIX system is used to collect teleoperation demonstration data [39]. | imitation error, task success, robustness와 compounding error | p. 15 (A.3.4 Training Data) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose an alternative means of obtaining task-agnostic control-self-supervising on top of unlabeled teleoperated play data: continuous logs of low-level observations and ...
- **p. 3 / 1 Introduction - extractive body cue:** 3, we propose two self-supervised methods for learning task-agnostic control from play: Play-GCBC and Play-LMP.
- **p. 12 / A.2 Architecture Details - extractive body cue:** Action space Our 8-DOF agent's action space state consists of: 3 cartesian coordinates for the position of its end effector, 3 Euler angles representing its ...
- **p. 1 / 1 Introduction - extractive body cue:** Unfortunately, designing reward functions for robotic skills is very challenging, especially when learning from raw observations, typically requiring manually-designed perception systems.
- **p. 12 / A.2 Architecture Details - extractive body cue:** 9 we show the layers with their sizes and depths of different sub-networks used in the model: the vision network, plan recognition network, plan proposal ...
- **p. 7 / 4 Experiments - extractive body cue:** 3) Does decoupling latent plan inference and plan decoding into independent problems, as is done in Play-LMP, improve performance over goal-conditioned Behavioral Cloning (Play-GCBC), (which ...
- **p. 7 / 4 Experiments - extractive body cue:** 10 5 0 5 10 15 20 25 Improvement of Play-LMP over Play-GCBC (absolute accuracy % points) rotate left close sliding grasp upright sweep right ...
- **p. 8 / 4 Experiments - extractive body cue:** Additionally, we find that the decoupling happening in Play-LMP compared to Play-GCBC is beneficial and yields systematic improvements in performance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Embodiment/environment | To compare our play-supervised models to a conventional scenario, we collect a training set of 100 expert demonstrations per task in the environment, and train one behavioral cloning policy (BC, details in ... | hardware/simulator version and reset protocol | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | 4 we embed 512 randomly selected windows from the play dataset as well as all validation task demonstrations, using the Φ plan recognition model. | role, split, size and leakage | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 17 (A.4.3 Coverage Analysis of Interaction Space) |
| Metric | 0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 Perturbation amount (meters) 0 20 40 60 80 100 18 tasks average accuracy % Play-LMP (ours) Play-GCBC (ours) BC (b) Robustness to variations. | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Baseline/ablation | (a) Play-LMP consistently outperforms the baselines, whether trained on groundtruth states or directly on pixels. | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 16 / Figure/Table caption - extractive body cue:** Figure 13: Naturally emerging retrying behavior: example run of Play-LMP policy on "grasp upright" task (grasping an object in upright position). The agent fails initially, ...
- **p. 17 / A.5 Limitations - extractive body cue:** The question of out-of-distribution generalization-say, playing in the living room and generalizing to the kitchen-is left to future work.
- **p. 8 / 4 Experiments - extractive body cue:** Emergent Retrying: We find qualitative evidence that play-supervised models, unlike models trained solely on expert demonstrations, make multiple attempts to retry the task after initial ...
- **p. 8 / 5 Conclusion - extractive body cue:** Future work includes exploring whether generalization is possible to novel objects or novel environments, as well as exploring the effects of imbalance in play data ...
- **p. 17 / A.5 Limitations - extractive body cue:** We hope to explore this in future work.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 14: Naturally emerging retrying behavior: example run of Play-LMP policy on "close sliding" task (sliding door left to right). The policy is aiming the ...
- **p. 7 / 4 Experiments - extractive body cue:** (b) models trained on play data are more robust to perturbations to the initial position.

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 This presents a challenge for conventional methods-if a slight variation of a skill is needed, e.g. opening a drawer by grasping the handle from the top down rather than bottom up, an ...를 문제로 두고, In this work, we propose an alternative means of obtaining task-agnostic control-self-supervising on top of unlabeled teleoperated play data: continuous logs of low-level observations and actions collected while a human teleoperates the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 12 (A.2 Architecture Details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
