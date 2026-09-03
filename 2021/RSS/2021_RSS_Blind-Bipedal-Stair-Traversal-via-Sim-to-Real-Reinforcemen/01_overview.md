# Blind Bipedal Stair Traversal via Sim-to-Real Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss17/p061.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss17/p061.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, bipedal locomotion, Reinforcement Learning, sim-to-real, proprioception
- Official paper: https://www.roboticsproceedings.org/rss17/p061.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss17/p061.pdf
- Code/Project: https://www.roboticsproceedings.org/rss17/p061.html
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 On stair-like environments, this is especially apparent due to the difficulty of recovery from missteps with only two legs.를 문제로 두고, We present a training pipeline which produces policies capable of blindly ascending and descending stairs in the real world.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Accurate and precise terrain estimation is a difficult problem for robot locomotion in real-world environments.
- **p. 1 / Abstract - extractive body cue:** Thus, it is useful to have systems that do not depend on accurate estimation to the point of fragility.
- **p. 1 / Abstract - extractive body cue:** In this paper, we explore the limits of such an approach by investigating the problem of traversing stair-like terrain without any external perception or terrain ...
- **p. 1 / Abstract - extractive body cue:** For such blind bipedal platforms, the problem appears difficult (even for humans) due to the surprise elevation changes.
- **p. 1 / Abstract - extractive body cue:** Our main contribution is to show that sim-to-real reinforcement learning (RL) can achieve robust locomotion over stair-like terrain on the bipedal robot Cassie using only ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** On stair-like environments, this is especially apparent due to the difficulty of recovery from missteps with only two legs.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Further, integrating a state-ofthe-art computer vision system into a high-speed controller is technically difficult, especially on a computationally limited platform like a mobile robot.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** We present a training pipeline which produces policies capable of blindly ascending and descending stairs in the real world.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we show that robust proprioceptive bipedal control for complex stair-like terrain can be learned via an existing RL framework with surprisingly little ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These policies learn proprioceptive reflexes to reject significant disturbances in ground height, resulting in highly robust behavior to many realworld environments. start location or the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Learning on this distribution allows for blind locomotion up and down unknown stairs as well as handling more general stair-like terrain characteristics, e.g. logs, curbs, ...
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Intuitively, this allows the controller to choose an appropriate stepping frequency for a particular gait, command, and terrain.
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** For sim-to-real training of the policy, we use Proximal Policy Optimization (PPO) [20], a model-free deep RL algorithm.
- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Training is done completely in a simulation environment, with dynamics randomization (see below), and the resulting policy is then used in the realworld.
- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Action Space The output action at of the control policy at each time step (running at 40Hz) is an 11 dimensional vector with the first ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | State Space The state st that is input to the control policy at each time step includes three main components. | proprioception, terrain/perception observation과 velocity command | p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION) |
| State/latent | State, Space, input, control, policy, time, step, includes, three, main, components, general | body/contact state, foothold 또는 behavior mode | p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION) |
| Output/action | In the general RL setting, at each discrete time step t the robot control policy π receives the current state st and returns an action at, which is applied and results in ... | joint target, torque, footstep 또는 locomotion action | p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION) |
| Objective/outcome | The RL optimization objective considered in this work is to learn a policy through interaction with the environment that maximizes the expected cumulative discounted reward over a finite-horizon T. | velocity/progress, stability, energy와 terrain generalization | p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** We present a training pipeline which produces policies capable of blindly ascending and descending stairs in the real world.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we show that robust proprioceptive bipedal control for complex stair-like terrain can be learned via an existing RL framework with surprisingly little ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These policies learn proprioceptive reflexes to reject significant disturbances in ground height, resulting in highly robust behavior to many realworld environments. start location or the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Learning on this distribution allows for blind locomotion up and down unknown stairs as well as handling more general stair-like terrain characteristics, e.g. logs, curbs, ...
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Intuitively, this allows the controller to choose an appropriate stepping frequency for a particular gait, command, and terrain.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, and can reliably ascend and descend stairs ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and 1.5 ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: The ground reaction forces and cumulative impulses of a Stair LSTM policy when it encounters varying ground height. The peak vertical force (A) ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 4 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Embodiment/environment | Each policy was trained until 300 million timesteps were sampled from the virtual environment, simulated with MuJoCo [22]. | hardware/simulator version and reset protocol | p. 4 (IV. RESULTS) |
| Dataset/benchmark | Each policy was trained until 300 million timesteps were sampled from the virtual environment, simulated with MuJoCo [22]. | role, split, size and leakage | p. 4 (IV. RESULTS) |
| Metric | Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, and can reliably ascend and descend stairs of typical dimensions found in human environments. ... | definition, denominator, direction and uncertainty | p. 4 (Figure/Table caption), p. 5 (Figure/Table caption), p. 4 (IV. RESULTS) |
| Baseline/ablation | We also trained a group of policies without stair terrain randomization, and denote these Flat Ground LSTM, to investigate the importance of the terrain randomization introduced in this work. | fair input/data/compute/action matching | p. 4 (IV. RESULTS), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / V. CONCLUSION - extractive body cue:** In future work, it will be interesting to investigate how vision can be most effectively used to improve the efficiency and/or performance of a blind ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and 1.5 ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: In this work, we investigate the limits of blind bipedal locomo- tion. We present a training pipeline which produces policies capable of blindly ...
- **p. 7 / V. CONCLUSION - extractive body cue:** In this work, we have motivated the desirability of a highly robust but blind walking controller, and demonstrated that such a blind bipedal walking controller ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: In order to ensure robustness over a variety of possible stair- like terrain, we randomize a number of parameters when generating stairs at ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, and can reliably ascend and descend stairs ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 On stair-like environments, this is especially apparent due to the difficulty of recovery from missteps with only two legs.를 문제로 두고, We present a training pipeline which produces policies capable of blindly ascending and descending stairs in the real world.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
