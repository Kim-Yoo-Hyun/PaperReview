# Eureka: Human-Level Reward Design via Coding Large Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (45 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/70c26937fbf3d4600b69a129031b66ec-Abstract-Conference.html.
> PDF retrieval source: https://openreview.net/forum?id=IEduRUO55F. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICLR
- Authors: Yecheng Jason Ma, William Liang, Guanzhi Wang, De-An Huang, Osbert Bastani, Dinesh Jayaraman, Yuke Zhu, Jim Fan, anima anandkumar
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Reinforcement Learning, Reward Design, Large Language Model, NVIDIA
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2024/hash/70c26937fbf3d4600b69a129031b66ec-Abstract-Conference.html
- Full-text retrieval: https://openreview.net/forum?id=IEduRUO55F
- Code/Project: https://eureka-research.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (45 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Eureka는 언어모델이 제안한 보상 코드를 강화학습 결과에 따라 반복 수정해 로봇 기술에 맞는 보상 함수를 찾는다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2024/file/70c26937fbf3d4600b69a129031b66ec-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Large Language Models (LLMs) have excelled as high-level semantic planners for sequential decision-making tasks.
- **p. 1 / ABSTRACT - extractive body cue:** However, harnessing them to learn complex lowlevel manipulation tasks, such as dexterous pen spinning, remains an open problem.
- **p. 1 / ABSTRACT - extractive body cue:** We bridge this fundamental gap and present EUREKA, a human-level reward design algorithm powered by LLMs.
- **p. 1 / ABSTRACT - extractive body cue:** EUREKA exploits the remarkable zero-shot generation, code-writing, and in-context improvement capabilities of state-of-theart LLMs, such as GPT-4, to perform evolutionary optimization over reward code.
- **p. 1 / ABSTRACT - extractive body cue:** The resulting rewards can then be used to acquire complex skills via reinforcement learning.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 2 PROBLEM SETTING AND DEFINITIONS The goal of reward design is to return a shaped reward function for a ground-truth reward function that may be ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Then, it iterates between reward sampling, GPU-accelerated reward evaluation, and reward reflection to progressively improve its reward outputs. domain expertise to construct task prompts or ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce Evolution-driven Universal REward Kit for Agent (EUREKA), a novel reward design algorithm powered by coding LLMs with the following contributions: 1.
- **p. 3 / 3 METHOD - extractive body cue:** EUREKA consists of three algorithmic components: 1) environment as context that enables zero-shot generation of executable rewards, 2) evolutionary search that iteratively proposes and refines ...
- **p. 3 / 3 METHOD - extractive body cue:** We propose directly feeding the raw environment source code (without the reward code, if exists) as context.
- **p. 5 / 3 METHOD - extractive body cue:** We propose reward reflection, an automated feedback that summarizes the policy training dynamics in texts.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Enables a new gradient-free in-context learning approach to reinforcement learning from human feedback (RLHF) that can generate more performant and human-aligned reward functions 2
- **p. 4 / 3 METHOD - extractive body cue:** In practice, to ensure that the environment code fits within the LLM's context window and does not leak simulation internals (so that we can expect ...
- **p. 3 / 3 METHOD - extractive body cue:** Given that any reward function is a function over the environment's state and action variables, the only requirement in the source code is that it ...
- **p. 5 / 3 METHOD - extractive body cue:** 3), reward reflection tracks the scalar values of all reward components and the task fitness function at intermediate policy checkpoints throughout training.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given that any reward function is a function over the environment's state and action variables, the only requirement in the source code is that it exposes these environment variables, which is easy ... | multi-view observation, language/task label과 action trajectory | p. 3 (3 METHOD), p. 4 (3 METHOD) |
| State/latent | Given, reward, function, over, environment, state, action, variables, only, requirement, source, code | shared representation, embodiment/task identity와 data distribution | p. 3 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD) |
| Output/action | In practice, to ensure that the environment code fits within the LLM's context window and does not leak simulation internals (so that we can expect the same prompt to generalize to new ... | dataset sample 또는 learned policy action | p. 4 (3 METHOD), p. 5 (3 METHOD), p. 3 (1 INTRODUCTION) |
| Objective/outcome | Algorithm 1 EUREKA 1: Require: Task description l, environment code M, coding LLM LLM, fitness function F, initial prompt prompt 2: Hyperparameters: search iteration N, iteration batch size K 3: for N ... | coverage, cross-embodiment transfer, data efficiency와 task success | p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD) |

## Main Claims and Actual Contribution

- 환경 코드로 여러 보상 함수를 생성하고 정책 학습에서 얻은 피드백으로 다음 보상 후보를 개선한다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2024/file/70c26937fbf3d4600b69a129031b66ec-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2024/file/70c26937fbf3d4600b69a129031b66ec-Paper-Conference.pdf#page=4)
- 서로 다른 로봇 형태의 시뮬레이션 과제에서 사람이 설계한 보상과 비교하고 Shadow Hand의 펜 돌리기도 학습했다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2024/file/70c26937fbf3d4600b69a129031b66ec-Paper-Conference.pdf#page=1)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 29 (Figure/Table caption), p. 2 (Figure/Table caption) |
| Embodiment/environment | In addition to coverage over robot form factors, we ensure depth in our evaluation by including all 20 tasks from the Bidexterous Manipulation (Dexterity) benchmark (Chen et al., 2022). | hardware/simulator version and reset protocol | p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS) |
| Dataset/benchmark | These are the original shaped reward functions provided in our benchmark tasks. | role, split, size and leakage | p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Metric | Figure 13: Raw success rates of all methods on the Dexterity benchmark. Reward Reflection Ablations. In Fig. 14, we provide a detailed per-task breakdown on the impact of removing reward reflection in ... | definition, denominator, direction and uncertainty | p. 29 (Figure/Table caption), p. 22 (Figure/Table caption), p. 29 (Figure/Table caption) |
| Baseline/ablation | Figure 4: EUREKA outperforms Human and L2R across all tasks. In particular, EUREKA realizes much greater gains on high-dimensional dexterity environments. about these tasks, making them ideal testbeds for assessing EUREKA's reward ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 28 (Figure/Table caption), p. 7 (4.3 RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.3 RESULTS - extractive body cue:** This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after 2 ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: EUREKA can zero-shot generate executable rewards and then flexibly improve them with many distinct types of free-form modification, such as (1) changing the ...
- **p. 7 / 4.3 RESULTS - extractive body cue:** Furthermore, we ablate GPT-4 with GPT-3.5 and find EUREKA degrades in performance but still matches or exceeds human-level on most Isaac tasks, indicating that its ...
- **p. 30 / Figure/Table caption - extractive body cue:** Figure 14: EUREKA without the reward reflection mechanism exhibits degraded performance. EUREKA with GPT-3.5. In Fig. 15, we compare the performance of EUREKA with GPT- ...
- **p. 30 / Figure/Table caption - extractive body cue:** Figure 15: Using GPT3.5 observes performance degradation in EUREKA but still remains comparable to GPT-4 on a majority of the tasks. Reward Correlation Experiments. To ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 5 (3 METHOD)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (45 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** 2 PROBLEM SETTING AND DEFINITIONS The goal of reward design is to return a shaped reward function for a ground-truth reward function that may be difficult to optimize directly (e.g., ... (p. 3, 1 INTRODUCTION).
- **Actual contribution:** We introduce Evolution-driven Universal REward Kit for Agent (EUREKA), a novel reward design algorithm powered by coding LLMs with the following contributions: 1. (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** Figure 10: EUREKA reward functions enjoy improved sample efficiency compared to various baseline reward functions on aggregate over 20 Dexterity tasks. Additional Evaluation Metrics. In Fig. 11, we present holistic ... (p. 28, Figure/Table caption).
- **Explicit failure boundary:** This skill requires the cooperation of two hands to ensure that the cap does not fall 1[dist > 0.03] CatchAbreast (422, 52) This class corresponds to the Catch Abreast task. (p. 19, B ENVIRONMENT DETAILS).
