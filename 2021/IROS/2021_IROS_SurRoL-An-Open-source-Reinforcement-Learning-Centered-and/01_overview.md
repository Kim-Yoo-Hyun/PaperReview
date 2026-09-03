# SurRoL: An Open-source Reinforcement Learning Centered and dVRK Compatible Platform for Surgical Robot Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ieeexplore.ieee.org/document/9635867.
> PDF retrieval source: https://arxiv.org/pdf/2108.13035. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, surgical robotics, Reinforcement Learning, simulation, sim-to-real, dexterous manipulation
- Official paper: https://ieeexplore.ieee.org/document/9635867
- Full-text retrieval: https://arxiv.org/pdf/2108.13035
- Code/Project: https://github.com/med-air/SurRoL
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 robot_data 문제를 이해하기 위해 읽는다. 본문은 Ten constructed surgical relevant tasks with difficulty levels and varying scenes are presented for learning-based algorithm evaluation (right).를 문제로 두고, Our main contributions are summarized as follows: • We design an open-source surgical robot learning simulation platform centered on reinforcement learning for surgical skills, which benefits low-cost data collection and accelerates the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Autonomous surgical execution relieves tedious routines and surgeon's fatigue.
- **p. 1 / Abstract - extractive body cue:** Recent learning-based methods, especially reinforcement learning (RL) based methods, achieve promising performance for dexterous manipulation, which usually requires the simulation to collect data efficiently and ...
- **p. 1 / Abstract - extractive body cue:** The existing learning-based simulation platforms for medical robots suffer from limited scenarios and simplified physical interactions, which degrades the real-world performance of learned policies.
- **p. 1 / Abstract - extractive body cue:** In this work, we designed SurRoL, an RL-centered simulation platform for surgical robot learning compatible with the da Vinci Research Kit (dVRK).
- **p. 1 / Abstract - extractive body cue:** The designed SurRoL integrates a user-friendly RL library for algorithm development and a real-time physics engine, which is able to support more PSM/ECM scenarios and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Ten constructed surgical relevant tasks with difficulty levels and varying scenes are presented for learning-based algorithm evaluation (right).
- **p. 1 / I. INTRODUCTION - extractive body cue:** The modeled trained on such simulated settings may suffer from the reality gap and fail to transfer to the real world [14].

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our main contributions are summarized as follows: • We design an open-source surgical robot learning simulation platform centered on reinforcement learning for surgical skills, which ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Further, the designed SurRoL with carefully modeled assets can successfully deal with more realistic physical interactions.
- **p. 2 / III. METHODS - extractive body cue:** Finally, ten surgical learning-based tasks are built for algorithm development and evaluation.
- **p. 2 / I. INTRODUCTION - extractive body cue:** SurRoL provides dVRK compatible simulation environments for surgical robot learning (left), with Gym-like interfaces for reinforcement learning algorithm development and ranges of surgical contents with ...
- **p. 2 / III. METHODS - extractive body cue:** SurRoL builds on top of the open-source PyBullet because of its state-of-the-art physics simulation, wide adoption in the machine learning community, and removal of the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | SurRoL builds on top of the open-source PyBullet because of its state-of-the-art physics simulation, wide adoption in the machine learning community, and removal of the commercial software limits, e.g., V-REP. | multi-view observation, language/task label과 action trajectory | p. 2 (III. METHODS), p. 1 (I. INTRODUCTION) |
| State/latent | SurRoL, builds, open-source, PyBullet, because, state-of-the-art, physics, simulation, wide, adoption, machine, learning | shared representation, embodiment/task identity와 data distribution | p. 2 (III. METHODS), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/action | Our main contributions are summarized as follows: • We design an open-source surgical robot learning simulation platform centered on reinforcement learning for surgical skills, which benefits low-cost data collection and accelerates the ... | dataset sample 또는 learned policy action | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective/outcome | coverage, cross-embodiment transfer, data efficiency와 task success | coverage, cross-embodiment transfer, data efficiency와 task success | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our main contributions are summarized as follows: • We design an open-source surgical robot learning simulation platform centered on reinforcement learning for surgical skills, which ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Further, the designed SurRoL with carefully modeled assets can successfully deal with more realistic physical interactions.
- **p. 2 / III. METHODS - extractive body cue:** Finally, ten surgical learning-based tasks are built for algorithm development and evaluation.
- **p. 2 / I. INTRODUCTION - extractive body cue:** SurRoL provides dVRK compatible simulation environments for surgical robot learning (left), with Gym-like interfaces for reinforcement learning algorithm development and ranges of surgical contents with ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** By contrast, the policy trained in the Interact manner with improved physics simulation is more robust to environment changes with a high success rate.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The success rates and episode returns are used as the evaluation metrics for goal-based and reward-based tasks, respectively, as in [32], [9], [10].
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** The mean success rate and standard deviation of three trained policies for the two manners are presented based on the evaluation of 200 episodes per ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Epoch 30 40 50 10 20 0.0 0.2 0.4 0.6 0.8 1.0 Success Rate BiPegTransfer with Variants (1) Approach (2) Pick (3) Lift (4) Handover ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Embodiment/environment | 1) Experiment Setup: In our RL environments, we set up the manipulation workspace for robots and objects to interact within. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Dataset/benchmark | The average success rates for goal-based tasks and episode returns for the reward-based task (ActiveTrack) are shown over three random seeds, with one epoch equalling 40 episodes. | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Metric | Fig. 5. Evaluation results for ten proposed tasks. The average success rates for goal-based tasks and episode returns for the reward-based task (ActiveTrack) are shown over three random seeds, with one epoch ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Baseline/ablation | 4) Evaluation Results: A summary of the evaluation results for RL baselines is shown in Fig. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTS), p. 3 (Figure/Table caption), p. 5 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** By visually inspecting the training progress, we find that the agents can quickly learn to approach the object such as the needle and attempt to ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Meanwhile, the needle picking point is restricted to the jaw tip to avoid unsafe jaw collisions with the holding surface.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Besides, we find some failure cases resulting from dynamics discrepancies between the simulation and the real world, also observed in [14].
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7. Different levels of physical interaction. The object is attached to the jaw if the tip-object distance is below a certain threshold with limited ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** However, in PSM settings, HER alone cannot solve all tasks within the given time horizon, mainly due to the tiny object and physically rich interaction ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Surprisingly, even with the correct grasping points, HER+DEMO fails to learn the picking action, which shows the extreme exploration difficulties during learning (Fig.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Examples of the demonstration. To demonstrate the proposed tasks and overcome the sample complexity, we provide the scripted policy for each and collect ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 robot_data 문제를 이해하기 위해 읽는다. 본문은 Ten constructed surgical relevant tasks with difficulty levels and varying scenes are presented for learning-based algorithm evaluation (right).를 문제로 두고, Our main contributions are summarized as follows: • We design an open-source surgical robot learning simulation platform centered on reinforcement learning for surgical skills, which benefits low-cost data collection and accelerates the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. METHODS), p. 2 (III. METHODS), p. 7 (IV. EXPERIMENTS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
