# Habitat 3.0: A Co-Habitat for Humans, Avatars, and Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/430894999584d0bd358611e2ecf00b15-Abstract-Conference.html.
> PDF retrieval source: https://proceedings.iclr.cc/paper_files/paper/2024/file/430894999584d0bd358611e2ecf00b15-Paper-Conference.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, simulation, human-robot interaction, social navigation, humanoid, mobile manipulation
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2024/hash/430894999584d0bd358611e2ecf00b15-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2024/file/430894999584d0bd358611e2ecf00b15-Paper-Conference.pdf
- Code/Project: https://aihabitat.org/habitat3
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-02 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Training and testing such social agents on hardware with real humans poses inherent challenges, including safety concerns, scalability limitations, substantial cost implications, and the complexity of establishing standardized benchmark ...를 문제로 두고, Social tasks - Aiming at reproducible and standardized benchmarking, we present two collaborative human-robot interaction tasks and a suite of baselines for each.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** We present Habitat 3.0: a simulation platform for studying collaborative humanrobot tasks in home environments.
- **p. 1 / ABSTRACT - extractive body cue:** Habitat 3.0 offers contributions across three dimensions: (1) Accurate humanoid1 simulation: addressing challenges in modeling complex deformable bodies and diversity in appearance and motion, all ...
- **p. 1 / ABSTRACT - extractive body cue:** (2) Human-in-the-loop infrastructure: enabling real human interaction with simulated robots via mouse/keyboard or a VR interface, facilitating evaluation of robot policies with human input.
- **p. 1 / ABSTRACT - extractive body cue:** (3) Collaborative tasks: studying two collaborative tasks, Social Navigation and Social Rearrangement.
- **p. 1 / ABSTRACT - extractive body cue:** Social Navigation investigates a robot's ability to locate and follow humanoid avatars in unseen environments, whereas Social Rearrangement addresses collaboration between a humanoid and robot ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Training and testing such social agents on hardware with real humans poses inherent challenges, including safety concerns, scalability limitations, substantial cost implications, and the complexity ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A simulation platform can overcome these challenges; however, the development of a collaborative human-robot simulation platform also comes with its own complexities.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Social tasks - Aiming at reproducible and standardized benchmarking, we present two collaborative human-robot interaction tasks and a suite of baselines for each.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce Habitat 3.0 - a simulator that supports both humanoid avatars and robots for the study of collaborative human-robot tasks in ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our framework is open-sourced, for more details see Appendix A.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We present the overall task success as well as the training reward for all approaches, averaged over 3 seeds.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The action space of the learned high-level policy consists of discrete selections from all possible combinations of skills and objects/receptacles allowed at each step.
- **p. 16 / A.1 SOCIAL NAVIGATION - extractive body cue:** We use a long short-term memory networks (LSTM) (Hochreiter & Schmidhuber, 1997) policy with ResNet18 as the visual backbone and two recurrent layers, resulting nearly ...
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We use 3 seeds for each model. overall task, +5 for completing any subgoal consisting of picking one of the target objects or placing an ...
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** When using learned skills, we use the same 2-layer policy architecture, except use learned navigation, and learned pick/place skills, which operate entirely using robot depth ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The policy uses a ResNet-18 (He et al., 2016) visual encoder to embed the 256 × 256 depth input image into a 512 dimension embedding. | standardized observation, action, task state와 evaluation split | p. 17 (A.2 SOCIAL REARRANGEMENT), p. 2 (1 INTRODUCTION) |
| State/latent | policy, uses, ResNet-18, visual, encoder, embed, depth, input, image, dimension, embedding, generate | benchmark state/goal와 method decision | p. 17 (A.2 SOCIAL REARRANGEMENT), p. 2 (1 INTRODUCTION), p. 17 (A.2 SOCIAL REARRANGEMENT) |
| Output/action | (2019)) to generate realistic body shapes and poses, (4) a library of avatars made from 12 base models with multiple gender representations, body shapes, and appearances, (5) a motion and behavior generation ... | policy/controller trajectory 또는 measured result | p. 2 (1 INTRODUCTION), p. 17 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT) |
| Objective/outcome | We use 2 PPO minibatches and 1 epoch per update, an entropy loss of 1e-4, and clip the gradient norm to 0.2. | success metric, robustness, generalization과 reproducibility | p. 17 (A.2 SOCIAL REARRANGEMENT), p. 17 (A.1 SOCIAL NAVIGATION), p. 16 (A.1 SOCIAL NAVIGATION) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Social tasks - Aiming at reproducible and standardized benchmarking, we present two collaborative human-robot interaction tasks and a suite of baselines for each.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce Habitat 3.0 - a simulator that supports both humanoid avatars and robots for the study of collaborative human-robot tasks in ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our framework is open-sourced, for more details see Appendix A.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We present the overall task success as well as the training reward for all approaches, averaged over 3 seeds.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The action space of the learned high-level policy consists of discrete selections from all possible combinations of skills and objects/receptacles allowed at each step.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Social Navigation. Overview of the Social Navigation task and sensors used (left). Baseline Results (right). The bottom rows show different variations of removing ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 9: Robot Embodiment. Spot robot in the simulation environment is designed to minimize the embodiment gaps to the robot in the physical world. We ...
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** This performance can potentially be improved by training the high-level policy with learned low-level skills in-the-loop, or by fine-tuning in this setting.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 25 (Figure/Table caption) |
| Embodiment/environment | In all episodes, to make sure that the robot learns to find the humanoid, the robot location is initialized at least 3m away from the humanoid. | hardware/simulator version and reset protocol | p. 16 (A.1 SOCIAL NAVIGATION), p. 17 (A.1 SOCIAL NAVIGATION) |
| Dataset/benchmark | We use 3 seeds for each model. overall task, +5 for completing any subgoal consisting of picking one of the target objects or placing an object at its goal, -0.005 penalty per ... | role, split, size and leakage | p. 16 (A.1 SOCIAL NAVIGATION), p. 17 (A.1 SOCIAL NAVIGATION), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 16 (A.1 SOCIAL NAVIGATION) |
| Metric | Figure 9: Robot Embodiment. Spot robot in the simulation environment is designed to minimize the embodiment gaps to the robot in the physical world. We measure the trained agents' performance when evaluated ... | definition, denominator, direction and uncertainty | p. 25 (Figure/Table caption), p. 16 (A.1 SOCIAL NAVIGATION), p. 16 (A.1 SOCIAL NAVIGATION) |
| Baseline/ablation | Figure 5: Social Navigation training curves. We plot the training average distance to the humanoid and reward for the social navigation baselines and ablations. We use 3 seeds for each model. path ... | fair input/data/compute/action matching | p. 17 (Figure/Table caption), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT) |

## Explicit Limitations and Failure Boundary

- **p. 17 / A.1 SOCIAL NAVIGATION - extractive body cue:** Since the Spot robot has a long body shape and cannot be represented by a single cylinder, we use a 2-cylinder representation, placed in the ...
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** Hence the high-level policy is not robust to low-level execution failures.
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** These skills do not use privileged information, and hence are more prone to failures in the diverse set of scenes considered in our tasks.
- **p. 16 / A.1 SOCIAL NAVIGATION - extractive body cue:** During training, the episode terminates if there is a collision between the humanoid and the robot.
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 5: Social Navigation training curves. We plot the training average distance to the humanoid and reward for the social navigation baselines and ablations. We ...
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The final social rearrangement reward is as follows: rsocial-rearrange t = 10 · ⊮success + 5 · ⊮subgoal -5 · ⊮collision -0.005.
- **p. 23 / Figure/Table caption - extractive body cue:** Table 3: Social Rearrangement baseline results. in place does no part of the task, thus reducing the total number of collisions. In the ZSC setting, ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Training and testing such social agents on hardware with real humans poses inherent challenges, including safety concerns, scalability limitations, substantial cost implications, and the complexity of establishing standardized benchmark ...를 문제로 두고, Social tasks - Aiming at reproducible and standardized benchmarking, we present two collaborative human-robot interaction tasks and a suite of baselines for each.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 16 (A.1 SOCIAL NAVIGATION), p. 18 (A.2 SOCIAL REARRANGEMENT) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
