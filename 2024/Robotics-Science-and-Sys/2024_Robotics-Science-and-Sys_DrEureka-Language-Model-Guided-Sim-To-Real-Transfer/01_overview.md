# DrEureka: Language Model Guided Sim-To-Real Transfer

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p094.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p094.html. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / Robotics: Science and Systems
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, sim-to-real, Reinforcement Learning, Large Language Model, NVIDIA
- Official paper: https://www.roboticsproceedings.org/rss20/p094.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p094.html
- Code/Project: https://eureka-research.github.io/dr-eureka/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 Directly synthesizing robot policies from LLMs is difficult because it does not explicitly reason through the physics of the environment, however, when a simulator is available, we can combine the impressive world ...를 문제로 두고, In this work, we propose DrEureka (Domain Randomization Eureka), a novel algorithm that leverages LLMs to automate reward design and domain randomization parameter configuration simultaneously for sim-to-real transfer.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Transferring policies learned in simulation to the real world is a promising strategy for acquiring robot skills at scale.
- **p. 1 / Abstract - extractive body cue:** However, sim-to-real approaches typically rely on manual design and tuning of the task reward function as well as the simulation physics parameters, rendering the process ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we investigate using Large Language Models (LLMs) to automate and accelerate sim-to-real design.
- **p. 1 / Abstract - extractive body cue:** Our LLM-guided sim-to-real approach, DrEureka, requires only the physics simulation for the target task and automatically constructs suitable reward functions and domain randomization distributions to ...
- **p. 1 / Abstract - extractive body cue:** We first demonstrate that our approach can discover sim-to-real configurations that are competitive with existing human-designed ones on quadruped locomotion and dexterous manipulation tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Directly synthesizing robot policies from LLMs is difficult because it does not explicitly reason through the physics of the environment, however, when a simulator is ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These characteristics of designing DR parameters make it an ideal problem for LLMs to tackle because of their strong grasp of physical knowledge [1, 18] ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose DrEureka (Domain Randomization Eureka), a novel algorithm that leverages LLMs to automate reward design and domain randomization parameter configuration simultaneously ...
- **p. 4 / IV. METHOD - extractive body cue:** Instead, we propose to directly exploit the strong instructionfollowing capability of instruction-tuned LLMs [62] and prompt the LLM to explicitly consider including safety terms for ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We evaluate DrEureka on quadruped and dexterous manipulator platforms, demonstrating that our method is general
- **p. 3 / IV. METHOD - extractive body cue:** In this section, we introduce DrEureka, which uses LLMs to automate two important bottlenecks in sim-to-real design: reward design and domain randomization.
- **p. 4 / IV. METHOD - extractive body cue:** We introduce a simple reward aware physics prior (RAPP) mechanism to restrict the base ranges for the LLM.
- **p. 4 / IV. METHOD - extractive body cue:** Algorithm 2 Reward Aware Physics Prior (RAPP) 1: Require: Reinforcement learning policy πinitial, simulator S, success criteria F, domain randomization parameters P and their respective ...
- **p. 3 / IV. METHOD - extractive body cue:** In Eureka, the LLM first takes the task description ltask and a summary of the environment state and action spaces (provided by environment code M) ...
- **p. 3 / IV. METHOD - extractive body cue:** At a high level, DrEureka first uses the LLM to generate a reward function that is both effective at the task and safe (Section IV-A ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A sim-to-real algorithm Algo for reward design and domain randomization takes M and task specification ltask as inputs, and outputs a reward function R and a distribution over transition functions, T : ... | multi-view observation, language/task label과 action trajectory | p. 3 (III. PROBLEM SETTING), p. 3 (IV. METHOD) |
| State/latent | sim-to-real, algorithm, Algo, reward, design, domain, randomization, takes, task, specification, ltask, inputs | shared representation, embodiment/task identity와 data distribution | p. 3 (III. PROBLEM SETTING), p. 3 (IV. METHOD), p. 4 (IV. METHOD) |
| Output/action | In Eureka, the LLM first takes the task description ltask and a summary of the environment state and action spaces (provided by environment code M) as input, and then samples several reward ... | dataset sample 또는 learned policy action | p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD) |
| Objective/outcome | These scores as well as other training statistics (e.g., values of the reward components during training) are provided as feedback to the LLM to iteratively evolve better reward functions that maximize F. | coverage, cross-embodiment transfer, data efficiency와 task success | p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 3 (IV. METHOD) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose DrEureka (Domain Randomization Eureka), a novel algorithm that leverages LLMs to automate reward design and domain randomization parameter configuration simultaneously ...
- **p. 4 / IV. METHOD - extractive body cue:** Instead, we propose to directly exploit the strong instructionfollowing capability of instruction-tuned LLMs [62] and prompt the LLM to explicitly consider including safety terms for ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We evaluate DrEureka on quadruped and dexterous manipulator platforms, demonstrating that our method is general
- **p. 3 / IV. METHOD - extractive body cue:** In this section, we introduce DrEureka, which uses LLMs to automate two important bottlenecks in sim-to-real design: reward design and domain randomization.
- **p. 4 / IV. METHOD - extractive body cue:** We introduce a simple reward aware physics prior (RAPP) mechanism to restrict the base ranges for the LLM.
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** The task of forward locomotion is to walk forward at 2 meters-per-second on flat terrains; while it is possible for the robot to walk forward ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** DrEureka's average and best policies outperform Human-Designed and a prior reward-design baseline.
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** Additionally, we consider two classes of DrEureka ablations that probe (1) whether some fixed DR configuration can generally outperform DrEureka samples, and (2) the importance ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP) |
| Embodiment/environment | We use the simulation environment as well as the real-world controller from Margolis et al. | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP) |
| Dataset/benchmark | To verify that a policy outputted by a reward-design algorithm itself is not effective for real-world deployment, we also compare against Eureka [9], which designs rewards using LLMs without safety consideration and ... | role, split, size and leakage | p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP) |
| Metric | Fig. 8: Forward locomotion training curves for 16 DR configurations. All runs are trained with the same reward function. B3. LLM Reward Reflection The following is an example of reward reflection on ... | definition, denominator, direction and uncertainty | p. 21 (Figure/Table caption), p. 6 (V. EXPERIMENTAL SETUP), p. 2 (Figure/Table caption) |
| Baseline/ablation | Forward locomotion specifically uses a teacher-student variant of PPO in which the teacher Sim-to-real Configuration Forward Velocity (m/s) Meters Traveled (m) Human-Designed [25] 1.32 ± 0.44 4.17 ± 1.57 Eureka [9] 0.0 ... | fair input/data/compute/action matching | p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP) |

## Explicit Limitations and Failure Boundary

- **p. 9 / VIII. LIMITATIONS - extractive body cue:** While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are several areas of improvement to the current ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** Sim-to-real Configuration Rotation (rad) Time-to-Fall (s) Human-Designed [25] 3.24 ± 1.66 20.00 ± 0.00 Our Method (Best) 9.39 ± 4.15 20.00 ± 0.00 Our Method ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Walking Globe sim and real environments. In lab settings, we loosely strap the robot horizontally to a center point to prevent robot from ...
- **p. 28 / Figure/Table caption - extractive body cue:** Fig. 13: DrEureka with safety instruction successfully learns transferable gait from simulation to real. In contrast, removing the safety instruction leads to behavior that exploits ...
- **p. 9 / VIII. LIMITATIONS - extractive body cue:** Incorporating vision-based inputs could potentially improve the robustness and generalizability of the learned policies in the real world, where visual cues play a critical role ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** This task is challenging because the policy only receives 16 joint angles and proprioceptive history, encoded via GRU [63], as observations and does not have ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** In the first class, we first compare to an ablation that does not train with domain randomization (No DR).

## Why Read It

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 Directly synthesizing robot policies from LLMs is difficult because it does not explicitly reason through the physics of the environment, however, when a simulator is available, we can combine the impressive world ...를 문제로 두고, In this work, we propose DrEureka (Domain Randomization Eureka), a novel algorithm that leverages LLMs to automate reward design and domain randomization parameter configuration simultaneously for sim-to-real transfer.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM SETTING), p. 4 (IV. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
