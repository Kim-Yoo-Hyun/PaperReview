# Eureka: Human-Level Reward Design via Coding Large Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (45 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=IEduRUO55F.
> PDF retrieval source: https://openreview.net/forum?id=IEduRUO55F. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Reinforcement Learning, Reward Design, Large Language Model, NVIDIA
- Official paper: https://openreview.net/forum?id=IEduRUO55F
- Full-text retrieval: https://openreview.net/forum?id=IEduRUO55F
- Code/Project: https://eureka-research.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (45 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 2 PROBLEM SETTING AND DEFINITIONS The goal of reward design is to return a shaped reward function for a ground-truth reward function that may be difficult to optimize directly (e.g., sparse rewards); ...를 문제로 두고, We introduce Evolution-driven Universal REward Kit for Agent (EUREKA), a novel reward design algorithm powered by coding LLMs with the following contributions: 1.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce Evolution-driven Universal REward Kit for Agent (EUREKA), a novel reward design algorithm powered by coding LLMs with the following contributions: 1.
- **p. 3 / 3 METHOD - extractive body cue:** EUREKA consists of three algorithmic components: 1) environment as context that enables zero-shot generation of executable rewards, 2) evolutionary search that iteratively proposes and refines ...
- **p. 3 / 3 METHOD - extractive body cue:** We propose directly feeding the raw environment source code (without the reward code, if exists) as context.
- **p. 5 / 3 METHOD - extractive body cue:** We propose reward reflection, an automated feedback that summarizes the policy training dynamics in texts.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Enables a new gradient-free in-context learning approach to reinforcement learning from human feedback (RLHF) that can generate more performant and human-aligned reward functions 2
- **p. 29 / Figure/Table caption - extractive body cue:** Figure 12: EUREKA reward functions' improvement over alternative reward functions are statistically significant. Dexterity Performance Breakdown. We present the raw success rates of EUREKA, L2R, ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: EUREKA takes unmodified environment source code and language task description as context to zero-shot generate executable reward functions from a coding LLM. Then, ...
- **p. 8 / 4.3 RESULTS - extractive body cue:** Furthermore, the fact that EUREKA can significantly improve over human rewards even when they are highly sub-optimal hints towards an interesting hypothesis: human designers are ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 29 (Figure/Table caption), p. 2 (Figure/Table caption) |
| Embodiment/environment | In addition to coverage over robot form factors, we ensure depth in our evaluation by including all 20 tasks from the Bidexterous Manipulation (Dexterity) benchmark (Chen et al., 2022). | hardware/simulator version and reset protocol | p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS) |
| Dataset/benchmark | These are the original shaped reward functions provided in our benchmark tasks. | role, split, size and leakage | p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Metric | Figure 13: Raw success rates of all methods on the Dexterity benchmark. Reward Reflection Ablations. In Fig. 14, we provide a detailed per-task breakdown on the impact of removing reward reflection in ... | definition, denominator, direction and uncertainty | p. 29 (Figure/Table caption), p. 22 (Figure/Table caption), p. 29 (Figure/Table caption) |
| Baseline/ablation | Figure 4: EUREKA outperforms Human and L2R across all tasks. In particular, EUREKA realizes much greater gains on high-dimensional dexterity environments. about these tasks, making them ideal testbeds for assessing EUREKA's reward ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 28 (Figure/Table caption), p. 6 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.3 RESULTS - extractive body cue:** This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's performances are lower than EUREKA after 2 ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: EUREKA can zero-shot generate executable rewards and then flexibly improve them with many distinct types of free-form modification, such as (1) changing the ...
- **p. 7 / 4.3 RESULTS - extractive body cue:** Furthermore, we ablate GPT-4 with GPT-3.5 and find EUREKA degrades in performance but still matches or exceeds human-level on most Isaac tasks, indicating that its ...
- **p. 30 / Figure/Table caption - extractive body cue:** Figure 14: EUREKA without the reward reflection mechanism exhibits degraded performance. EUREKA with GPT-3.5. In Fig. 15, we compare the performance of EUREKA with GPT- ...
- **p. 30 / Figure/Table caption - extractive body cue:** Figure 15: Using GPT3.5 observes performance degradation in EUREKA but still remains comparable to GPT-4 on a majority of the tasks. Reward Correlation Experiments. To ...

## Why Read It

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 2 PROBLEM SETTING AND DEFINITIONS The goal of reward design is to return a shaped reward function for a ground-truth reward function that may be difficult to optimize directly (e.g., sparse rewards); ...를 문제로 두고, We introduce Evolution-driven Universal REward Kit for Agent (EUREKA), a novel reward design algorithm powered by coding LLMs with the following contributions: 1.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 5 (3 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
