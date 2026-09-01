# Problem - Eureka: Human-Level Reward Design via Coding Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (45 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=IEduRUO55F; PDF retrieval source: https://openreview.net/forum?id=IEduRUO55F. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION)): 2 PROBLEM SETTING AND DEFINITIONS The goal of reward design is to return a shaped reward function for a ground-truth reward function that may be difficult to optimize directly (e.g., ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Large Language Models (LLMs) have excelled as high-level semantic planners for sequential decision-making tasks.
- **p. 1 / ABSTRACT - extractive body cue:** However, harnessing them to learn complex lowlevel manipulation tasks, such as dexterous pen spinning, remains an open problem.
- **p. 1 / ABSTRACT - extractive body cue:** We bridge this fundamental gap and present EUREKA, a human-level reward design algorithm powered by LLMs.
- **p. 1 / ABSTRACT - extractive body cue:** EUREKA exploits the remarkable zero-shot generation, code-writing, and in-context improvement capabilities of state-of-theart LLMs, such as GPT-4, to perform evolutionary optimization over reward code.
- **p. 1 / ABSTRACT - extractive body cue:** The resulting rewards can then be used to acquire complex skills via reinforcement learning.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 2 PROBLEM SETTING AND DEFINITIONS The goal of reward design is to return a shaped reward function for a ground-truth reward function that may be ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Then, it iterates between reward sampling, GPU-accelerated reward evaluation, and reward reflection to progressively improve its reward outputs. domain expertise to construct task prompts or ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | 2 PROBLEM SETTING AND DEFINITIONS The goal of reward design is to return a shaped reward function for a ground-truth reward function ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | Given that any reward function is a function over the environment's state and action variables, the only requirement in the source code ... | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF |
| State / latent | Given, reward, function, over, environment, state, action, variables, only, requirement | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | reward, reflection, automated, feedback, summarizes, policy, training, dynamics | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: Given, reward, function, over, environment, state, action, variables, only, requirement | p. 3 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD) |
| Decision / output variable | normalized sample or downstream action; body terms: introduce, Evolution-driven, Universal, REward, Kit, Agent, EUREKA, novel | p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 3 (3 METHOD) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: Algorithm, EUREKA, Require, Task, description, environment, code, coding | p. 4 (3 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD) |
| Success / guarantee | cross-domain transfer and task performance | p. 29 (Figure/Table caption), p. 22 (Figure/Table caption), p. 29 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Then, it iterates between reward sampling, GPU-accelerated reward evaluation, and reward reflection to progressively improve its reward outputs. domain expertise to construct task prompts or ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Despite their fundamental importance, reward functions are known to be notoriously difficult to design in practice (Russell & Norvig, 1995; Sutton & Barto, 2018); a ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Existing attempts require substantial Figure 1: EUREKA generates human-level reward functions across diverse robots and tasks.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Large Language Models (LLMs) have excelled as high-level semantic planners for robotics tasks (Ahn et al., 2022; Singh et al., 2023), but whether they can ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 3 (3 METHOD), p. 5 (3 METHOD), p. 2 (1 INTRODUCTION)): We introduce Evolution-driven Universal REward Kit for Agent (EUREKA), a novel reward design algorithm powered by coding LLMs with the following contributions: 1.

- **p. 3 / 3 METHOD - extractive body cue:** EUREKA consists of three algorithmic components: 1) environment as context that enables zero-shot generation of executable rewards, 2) evolutionary search that iteratively proposes and refines ...
- **p. 3 / 3 METHOD - extractive body cue:** We propose directly feeding the raw environment source code (without the reward code, if exists) as context.
- **p. 5 / 3 METHOD - extractive body cue:** We propose reward reflection, an automated feedback that summarizes the policy training dynamics in texts.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Enables a new gradient-free in-context learning approach to reinforcement learning from human feedback (RLHF) that can generate more performant and human-aligned reward functions 2

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | This consistent improvement also cannot be replaced by just sampling more in the first iteration as the ablation's ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 3: EUREKA can zero-shot generate executable rewards and then flexibly improve them with many distinct types of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Furthermore, we ablate GPT-4 with GPT-3.5 and find EUREKA degrades in performance but still matches or exceeds human-level ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 30 | Figure 14: EUREKA without the reward reflection mechanism exhibits degraded performance. EUREKA with GPT-3.5. In Fig. 15, we ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 3 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), interface p. 3 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 3 (1 INTRODUCTION), objective p. 4 (3 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
