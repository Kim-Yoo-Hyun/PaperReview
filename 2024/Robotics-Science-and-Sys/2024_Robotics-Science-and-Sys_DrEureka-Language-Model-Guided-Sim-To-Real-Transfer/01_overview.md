# DrEureka: Language Model Guided Sim-To-Real Transfer

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p094.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p094.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / Robotics: Science and Systems
- Authors: Yecheng Jason Ma, William Liang, Hung-Ju Wang, Yuke Zhu, Linxi “Jim” Fan, Osbert Bastani, Dinesh Jayaraman
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, sim-to-real, Reinforcement Learning, Large Language Model, NVIDIA
- Official paper: https://www.roboticsproceedings.org/rss20/p094.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p094.html
- Code/Project: https://eureka-research.github.io/dr-eureka/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

DrEureka는 강화학습 보상과 시뮬레이션 물성의 무작위화 범위를 언어모델로 설계해 실제 로봇으로 정책을 전이한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss20/p094.pdf#page=1)

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

- 보상 조건을 만족하는 물성 범위를 추정하고 그 정보를 바탕으로 실제 전이에 사용할 도메인 무작위화 분포를 제안한다. [PDF 3쪽](https://www.roboticsproceedings.org/rss20/p094.pdf#page=3) · [PDF 5쪽](https://www.roboticsproceedings.org/rss20/p094.pdf#page=5)
- 사족보행과 손안 큐브 회전의 전이를 비교하고 실제 사족 로봇이 공 위에서 균형을 유지하며 걷는 과제를 시험했다. [PDF 6쪽](https://www.roboticsproceedings.org/rss20/p094.pdf#page=6) · [PDF 8쪽](https://www.roboticsproceedings.org/rss20/p094.pdf#page=8)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM SETTING), p. 4 (IV. METHOD)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** These characteristics of designing DR parameters make it an ideal problem for LLMs to tackle because of their strong grasp of physical knowledge [1, 18] and effectiveness in generating hypotheses, ... (p. 1, I. INTRODUCTION).
- **Actual contribution:** In this work, we propose DrEureka (Domain Randomization Eureka), a novel algorithm that leverages LLMs to automate reward design and domain randomization parameter configuration simultaneously for sim-to-real transfer. (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** Note that while CEM and BayRn tackle the same problem, their iterative procedure is conceptually different from DrEureka, which trains all policies in parallel; thus, this comparison favors the baselines ... (p. 6, V. EXPERIMENTAL SETUP).
- **Explicit failure boundary:** While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are several areas of improvement to the current implementation: • Lack of visual ... (p. 9, VIII. LIMITATIONS).

## 원문과 공개 자료

- RSS 게재본에 병기된 Linxi “Jim” Fan의 이름을 반영했다. [표제면](https://www.roboticsproceedings.org/rss20/p094.pdf#page=1)
- 가중치 · DrEureka 사족 전진 보행 정책의 저장 가중치 · forward_locomotion/runs/forward_locomotion/dr_eureka_best/checkpoints/ac_weights_last.pt [배포 파일](https://raw.githubusercontent.com/eureka-research/DrEureka/1d4e00700423170717654516f4ef4b24cb0f3a84/forward_locomotion/runs/forward_locomotion/dr_eureka_best/checkpoints/ac_weights_last.pt)
- 코드 · 보상 및 도메인 무작위화 설계 구현 · dr_eureka/dr_eureka.py [배포 파일](https://raw.githubusercontent.com/eureka-research/DrEureka/1d4e00700423170717654516f4ef4b24cb0f3a84/dr_eureka/dr_eureka.py)
- 데이터 · 전진 보행 실험의 저장 학습 지표로 범위를 한정 · forward_locomotion/runs/forward_locomotion/dr_eureka_best/metrics.pkl [배포 파일](https://raw.githubusercontent.com/eureka-research/DrEureka/1d4e00700423170717654516f4ef4b24cb0f3a84/forward_locomotion/runs/forward_locomotion/dr_eureka_best/metrics.pkl)
