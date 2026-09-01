# Learning Quadrupedal Locomotion over Challenging Terrain

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2010.11251.
> PDF retrieval source: https://arxiv.org/pdf/2010.11251. Reading tracker status/evidence was not changed.

- Year/Venue: 2020 / Science Robotics
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, quadruped locomotion, Reinforcement Learning, rough terrain
- Official paper: https://arxiv.org/abs/2010.11251
- Full-text retrieval: https://arxiv.org/pdf/2010.11251
- Code/Project: https://leggedrobotics.github.io/rl-blindloco/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 While animals instinctively solve this complex control problem, it is an open challenge in robotics.를 문제로 두고, Here we present a radically robust controller for blind quadrupedal locomotion on challenging terrain.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Legged locomotion can dramatically expand the reach of robotics.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Much of the dry landmass on Earth remains impassible to wheeled and tracked machines, the stability of which can be severely compromised on challenging terrain.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Quadrupedal animals, on the other hand, can access some of the most remote parts of our planet.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** They can choose safe footholds within their kinematic reach and rapidly change their kinematic state in response to the environment.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Legged robots have the potential to traverse any terrain that their animal counterparts can.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** While animals instinctively solve this complex control problem, it is an open challenge in robotics.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Under such conditions, existing published controllers manifest frequent foot slippage, loss of balance, and ultimately catastrophic failure.

## Core Idea

- **p. 3 / 1. INTRODUCTION - extractive body cue:** Here we present a radically robust controller for blind quadrupedal locomotion on challenging terrain.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Our methodology and results open new frontiers for legged robotics and suggest that the extraordinary complexity of the physical world can be tamed without brittle ...
- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** An overview of our method is given in Fig.
- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** One difference of our methodology from that of Chen et al.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Model-free reinforcement learning (RL) has recently emerged as an alternative approach in the development of legged locomotion skills [12-14].
- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** The model computes a latent embedding ¯lt that represents the current state, and an action ¯at.
- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** The student model is a temporal convolutional network (TCN) [22] that receives a sequence of N proprioceptive observations as input.
- **p. 7 / 4. MATERIALS AND METHODS - extractive body cue:** Research Article ETH Zurich and Intel 7 terrain traversability for the policy height map Automatic terrain curriculum

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The model computes a latent embedding ¯lt that represents the current state, and an action ¯at. | proprioception, terrain/perception observation과 velocity command | p. 6 (4. MATERIALS AND METHODS), p. 6 (4. MATERIALS AND METHODS) |
| State/latent | model, computes, latent, embedding, represents, current, state, action, student, temporal, convolutional, network | body/contact state, foothold 또는 behavior mode | p. 6 (4. MATERIALS AND METHODS), p. 6 (4. MATERIALS AND METHODS), p. 7 (4. MATERIALS AND METHODS) |
| Output/action | The student model is a temporal convolutional network (TCN) [22] that receives a sequence of N proprioceptive observations as input. | joint target, torque, footstep 또는 locomotion action | p. 6 (4. MATERIALS AND METHODS), p. 7 (4. MATERIALS AND METHODS), p. 3 (1. INTRODUCTION) |
| Objective/outcome | The training objective rewards locomotion in prescribed directions. | velocity/progress, stability, energy와 terrain generalization | p. 6 (4. MATERIALS AND METHODS), p. 6 (4. MATERIALS AND METHODS) |

## Main Claims and Actual Contribution

- **p. 3 / 1. INTRODUCTION - extractive body cue:** Here we present a radically robust controller for blind quadrupedal locomotion on challenging terrain.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Our methodology and results open new frontiers for legged robotics and suggest that the extraordinary complexity of the physical world can be tamed without brittle ...
- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** An overview of our method is given in Fig.
- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** One difference of our methodology from that of Chen et al.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Model-free reinforcement learning (RL) has recently emerged as an alternative approach in the development of legged locomotion skills [12-14].
- **p. 4 / 2. RESULTS - extractive body cue:** (E) Success rates for different step heights.
- **p. 4 / 2. RESULTS - extractive body cue:** The success rate is evaluated over 10 trials for each condition.
- **p. 5 / 2. RESULTS - extractive body cue:** The success rates are given in Fig.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 4 (2. RESULTS), p. 4 (2. RESULTS) |
| Embodiment/environment | The objective of the competition is to develop robotic systems that rapidly map, navigate, and search complex underground environments, including tunnels, urban underground, and cave networks. | hardware/simulator version and reset protocol | p. 5 (2. RESULTS), p. 3 (2. RESULTS) |
| Dataset/benchmark | We have deployed the trained locomotion controller on two generations of ANYmal robots: ANYmal-B (Fig. | role, split, size and leakage | p. 5 (2. RESULTS), p. 3 (2. RESULTS), p. 3 (2. RESULTS), p. 4 (2. RESULTS) |
| Metric | Research Article ETH Zurich and Intel 4 B A command C command 10 kg payload D Baseline 0.2 m/s Ours w/ payload Baseline 0.6 m/s Baseline 0.2 m/s with payload Ours E ... | definition, denominator, direction and uncertainty | p. 4 (2. RESULTS), p. 4 (Figure/Table caption), p. 10 (Figure/Table caption) |
| Baseline/ablation | We have compared the presented controller to a state-of-the-art baseline [1, 26] in the forest environment. | fair input/data/compute/action matching | p. 5 (2. RESULTS), p. 5 (2. RESULTS), p. 4 (2. RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 3. DISCUSSION - extractive body cue:** We see a number of limitations and opportunities for future work.
- **p. 5 / 2. RESULTS - extractive body cue:** Support surfaces are unstable and the robot's feet frequently slip.
- **p. 5 / 2. RESULTS - extractive body cue:** The baseline's catastrophic failures are not factored into these measurements: when the baseline fails, it is reset by a human operator in a more stable ...
- **p. 6 / 3. DISCUSSION - extractive body cue:** This is a significant advantage in that the controller makes few assumptions on the sensor suite and is not susceptible to failure when exteroception breaks ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. A number of specific deployments. (A-F) Zero-shot gener- alization to slippery and deforming terrain. (G) Steep descent during the DARPA Subterranean Challenge. The ...
- **p. 4 / 2. RESULTS - extractive body cue:** (A) Locomotion over unstable debris.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. Overview of the presented approach. (A) Two-stage training process. First, a teacher policy is trained using reinforcement learning in simulation. It has access ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 While animals instinctively solve this complex control problem, it is an open challenge in robotics.를 문제로 두고, Here we present a radically robust controller for blind quadrupedal locomotion on challenging terrain.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 6 (4. MATERIALS AND METHODS), p. 6 (4. MATERIALS AND METHODS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
