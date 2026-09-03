# Helpful DoggyBot: Open-World Object Fetching using Legged Robots and Vision-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2410.00231.
> PDF retrieval source: https://arxiv.org/pdf/2410.00231. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics, Reinforcement Learning
- Official paper: https://arxiv.org/abs/2410.00231
- Full-text retrieval: https://arxiv.org/pdf/2410.00231
- Code/Project: https://helpful-doggybot.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 locomotion 문제를 이해하기 위해 읽는다. 본문은 In this paper, we present Helpful DoggyBot, a quadrupedal robot system that aims to overcome these limitations and enable helpful mobile manipulation skills that can understand human commands and generalize across different ...를 문제로 두고, The key contributions of our system include (1) a simple yet effective 1-DoF gripper design that enables object grasping for quadrupeds, (2) a general-purpose low-level controller trained in simulation that enables real-world ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Learning-based methods have achieved strong performance for quadrupedal locomotion.
- **p. 1 / Abstract - extractive body cue:** However, several challenges prevent quadrupeds from learning helpful indoor skills that require interaction with environments and humans: lack of end-effectors for manipulation, limited semantic understanding ...
- **p. 1 / Abstract - extractive body cue:** We present a system for quadrupedal mobile manipulation in indoor environments.
- **p. 1 / Abstract - extractive body cue:** It uses a front-mounted gripper for object manipulation, a lowlevel controller trained in simulation using egocentric depth for agile skills like climbing and whole-body tilting, ...
- **p. 1 / Abstract - extractive body cue:** We evaluate our system in two unseen environments without any real-world data collection or training.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Several key challenges have hindered progress in this direction.
- **p. 2 / I. INTRODUCTION - extractive body cue:** On the semantic perception and control front for solving useful tasks, instead of relying on collecting human demonstrations that is time-consuming or simulation that has ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** The key contributions of our system include (1) a simple yet effective 1-DoF gripper design that enables object grasping for quadrupeds, (2) a general-purpose low-level ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present Helpful DoggyBot, a quadrupedal robot system that aims to overcome these limitations and enable helpful mobile manipulation skills that can ...
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** Our online estimator architecture consists of a convolutional neural network (CNN) followed by a gated recurrent unit (GRU) to process the temporal sequence of depth ...
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** We introduce auxiliary rewards for maintaining balance, minimizing energy consumption, and smooth transitions between different locomotion modes (e.g., walking, climbing, and tilting).
- **p. 2 / I. INTRODUCTION - extractive body cue:** Notably, our system achieves this generalization without any real-world data collection or training, highlighting the potential of our approach for creating helpful quadrupedal assistants that ...
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** Phase 1: Training with Privileged Information We develop our agile visual whole-body control policy through a two-phase training process: In the first phase, we train ...
- **p. 4 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** We use a two-phase framework to train a depth-based policy as the low-evel whole-body controller.
- **p. 4 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** During deployment, we use VLMs for open-vocabulary detection, segmentation and tracking models to provide velocity commands and pitch commands for the controller. locomotion and precise ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The output of this estimator replaces the scandots input to the base policy learned in Phase 1. | proprioception, terrain/perception observation과 velocity command | p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER) |
| State/latent | output, estimator, replaces, scandots, input, base, policy, learned, Phase, VLM, Velocity, Commands | body/contact state, foothold 또는 behavior mode | p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER) |
| Output/action | VLM Velocity Commands VLM Pitch Commands Proprioception Exteroception Student Actions Deployment Training Depth Oracle Velocity Commands Phase 2 Depth Images Fig. | joint target, torque, footstep 또는 locomotion action | p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER) |
| Objective/outcome | We introduce auxiliary rewards for maintaining balance, minimizing energy consumption, and smooth transitions between different locomotion modes (e.g., walking, climbing, and tilting). | velocity/progress, stability, energy와 terrain generalization | p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** The key contributions of our system include (1) a simple yet effective 1-DoF gripper design that enables object grasping for quadrupeds, (2) a general-purpose low-level ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present Helpful DoggyBot, a quadrupedal robot system that aims to overcome these limitations and enable helpful mobile manipulation skills that can ...
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** Our online estimator architecture consists of a convolutional neural network (CNN) followed by a gated recurrent unit (GRU) to process the temporal sequence of depth ...
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** We introduce auxiliary rewards for maintaining balance, minimizing energy consumption, and smooth transitions between different locomotion modes (e.g., walking, climbing, and tilting).
- **p. 2 / I. INTRODUCTION - extractive body cue:** Notably, our system achieves this generalization without any real-world data collection or training, highlighting the potential of our approach for creating helpful quadrupedal assistants that ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** In the task involving navigating to a toy on a bed, our system achieved a 60% total first-attempt success rate, significantly outperforming the Go2 default ...
- **p. 5 / VI. EXPERIMENTS - extractive body cue:** In contrast, our approach achieves consistently higher performance, with nearperfect scores in most tasks, especially Climb Up and Climb Down, and outperforms all baselines.
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** Ours outperform all baselines in average time to completion, and close to teleoperation in success rates.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS) |
| Embodiment/environment | Illustrated in Figure 1, we select three objects and three environments that represent realistic real-world scenarios: • Bed + Toy: The robot needs to fetch a stuffed toy on a bed. | hardware/simulator version and reset protocol | p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Dataset/benchmark | Real-World Experiments Baselines and Tasks in Real World. | role, split, size and leakage | p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS) |
| Metric | We measure the success rates and average time to completion across 10 trials per setting. | definition, denominator, direction and uncertainty | p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS) |
| Baseline/ablation | In contrast, our approach achieves consistently higher performance, with nearperfect scores in most tasks, especially Climb Up and Climb Down, and outperforms all baselines. | fair input/data/compute/action matching | p. 5 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / VI. EXPERIMENTS - extractive body cue:** While our approach demonstrates progress, limitations include the gripper's restricted dexterity, reliance on ceiling-mounted cameras for navigation, and potential occlusion to the perception system.
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** Go2 default controller fails to climb up high obstacles like beds and sofas, whereas No Tracking only generates an open-loop trajectory of commands and fails ...
- **p. 5 / VI. EXPERIMENTS - extractive body cue:** This controller does not use exteroception. • Teleop: the commands are generated by an expert human operator through a remote controller, replacing VLMs. • No ...
- **p. 5 / V. ZERO-SHOT DEPLOYMENT USING VLMS - extractive body cue:** We find only small degradation in performance from the oracle policy using priviledged information in Phase 1.

## Why Read It

VLA and generalist robot policies의 locomotion 문제를 이해하기 위해 읽는다. 본문은 In this paper, we present Helpful DoggyBot, a quadrupedal robot system that aims to overcome these limitations and enable helpful mobile manipulation skills that can understand human commands and generalize across different ...를 문제로 두고, The key contributions of our system include (1) a simple yet effective 1-DoF gripper design that enables object grasping for quadrupeds, (2) a general-purpose low-level controller trained in simulation that enables real-world ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
