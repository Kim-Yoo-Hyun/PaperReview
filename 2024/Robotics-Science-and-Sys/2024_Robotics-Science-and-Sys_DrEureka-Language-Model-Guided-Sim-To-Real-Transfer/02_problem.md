# Problem - DrEureka: Language Model Guided Sim-To-Real Transfer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p094.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p094.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM SETTING)): Directly synthesizing robot policies from LLMs is difficult because it does not explicitly reason through the physics of the environment, however, when a simulator is available, we can combine the ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Transferring policies learned in simulation to the real world is a promising strategy for acquiring robot skills at scale.
- **p. 1 / Abstract - extractive body cue:** However, sim-to-real approaches typically rely on manual design and tuning of the task reward function as well as the simulation physics parameters, rendering the process ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we investigate using Large Language Models (LLMs) to automate and accelerate sim-to-real design.
- **p. 1 / Abstract - extractive body cue:** Our LLM-guided sim-to-real approach, DrEureka, requires only the physics simulation for the target task and automatically constructs suitable reward functions and domain randomization distributions to ...
- **p. 1 / Abstract - extractive body cue:** We first demonstrate that our approach can discover sim-to-real configurations that are competitive with existing human-designed ones on quadruped locomotion and dexterous manipulation tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Directly synthesizing robot policies from LLMs is difficult because it does not explicitly reason through the physics of the environment, however, when a simulator is ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These characteristics of designing DR parameters make it an ideal problem for LLMs to tackle because of their strong grasp of physical knowledge [1, 18] ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Directly synthesizing robot policies from LLMs is difficult because it does not explicitly reason through the physics of the environment, however, when ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | A sim-to-real algorithm Algo for reward design and domain randomization takes M and task specification ltask as inputs, and outputs a reward ... | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF |
| State / latent | sim-to-real, algorithm, Algo, reward, design, domain, randomization, takes, task, specification | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | Algorithm, DrEureka, Reward, Design, Require, Task, description, ltask | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: sim-to-real, algorithm, Algo, reward, design, domain, randomization, takes, task, specification | p. 3 (III. PROBLEM SETTING), p. 3 (IV. METHOD), p. 4 (IV. METHOD) |
| Decision / output variable | normalized sample or downstream action; body terms: DrEureka, Domain, Randomization, Eureka, novel, algorithm, leverages, LLMs | p. 1 (I. INTRODUCTION), p. 4 (IV. METHOD), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: scores, well, other, training, statistics, values, reward, components | p. 4 (IV. METHOD), p. 4 (IV. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (IV. METHOD), p. 3 (IV. METHOD), p. 5 (IV. METHOD) |
| Success / guarantee | cross-domain transfer and task performance | p. 21 (Figure/Table caption), p. 6 (V. EXPERIMENTAL SETUP), p. 2 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** These characteristics of designing DR parameters make it an ideal problem for LLMs to tackle because of their strong grasp of physical knowledge [1, 18] ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Walking globe is a novel task to show DrEureka's capability for guiding the sim-to-real transfer of a challenging new task without pre-existing sim-to-real configurations.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Then, it tests the policy under different simulation conditions to build a reward-aware physics prior, which is provided to the LLM to generate a set ...
- **p. 3 / III. PROBLEM SETTING - extractive body cue:** We formalize the sim-to-real design problem setting.

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 4 (IV. METHOD), p. 1 (I. INTRODUCTION), p. 3 (IV. METHOD), p. 4 (IV. METHOD)): In this work, we propose DrEureka (Domain Randomization Eureka), a novel algorithm that leverages LLMs to automate reward design and domain randomization parameter configuration simultaneously for sim-to-real transfer.

- **p. 4 / IV. METHOD - extractive body cue:** Instead, we propose to directly exploit the strong instructionfollowing capability of instruction-tuned LLMs [62] and prompt the LLM to explicitly consider including safety terms for ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We evaluate DrEureka on quadruped and dexterous manipulator platforms, demonstrating that our method is general
- **p. 3 / IV. METHOD - extractive body cue:** In this section, we introduce DrEureka, which uses LLMs to automate two important bottlenecks in sim-to-real design: reward design and domain randomization.
- **p. 4 / IV. METHOD - extractive body cue:** We introduce a simple reward aware physics prior (RAPP) mechanism to restrict the base ranges for the LLM.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Sim-to-real Configuration Rotation (rad) Time-to-Fall (s) Human-Designed [25] 3.24 ± 1.66 20.00 ± 0.00 Our Method (Best) 9.39 ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Fig. 6: Walking Globe sim and real environments. In lab settings, we loosely strap the robot horizontally to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 28 | Fig. 13: DrEureka with safety instruction successfully learns transferable gait from simulation to real. In contrast, removing the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. PROBLEM SETTING), p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM SETTING), interface p. 3 (III. PROBLEM SETTING), p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD), objective p. 4 (IV. METHOD), p. 4 (IV. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
