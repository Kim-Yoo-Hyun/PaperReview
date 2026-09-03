# ProgPrompt: Generating Situated Robot Task Plans using Large Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ieeexplore.ieee.org/document/10161317.
> PDF retrieval source: https://arxiv.org/pdf/2209.11302. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Robotics, LLM planning, program synthesis, situated planning, long-horizon tasks
- Official paper: https://ieeexplore.ieee.org/document/10161317
- Full-text retrieval: https://arxiv.org/pdf/2209.11302
- Code/Project: https://progprompt.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 We illustrate a scenario where an assertion succeeds or fails, and how the generated plan corrects the error before executing the next step.를 문제로 두고, We present a programmatic LLM prompt structure that enables plan generation functional across situated environments, robot capabilities, and tasks.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Task planning can require defining myriad domain knowledge about the world in which a robot needs to act.
- **p. 1 / Abstract - extractive body cue:** To ameliorate that effort, large language models (LLMs) can be used to score potential next actions during task planning, and even generate action sequences directly, ...
- **p. 1 / Abstract - extractive body cue:** However, such methods either require enumerating all possible next steps for scoring, or generate free-form text that may contain actions not possible on a given ...
- **p. 1 / Abstract - extractive body cue:** We present a programmatic LLM prompt structure that enables plan generation functional across situated environments, robot capabilities, and tasks.
- **p. 1 / Abstract - extractive body cue:** Our key insight is to prompt the LLM with program-like specifications of the available actions and objects in an environment, as well as with example ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We illustrate a scenario where an assertion succeeds or fails, and how the generated plan corrects the error before executing the next step.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Everyday household tasks require both commonsense understanding of the world and situated knowledge about the current environment.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** We present a programmatic LLM prompt structure that enables plan generation functional across situated environments, robot capabilities, and tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We introduce PROGPROMPT, a prompting scheme that goes beyond conditioning LLMs in natural language.
- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: PROGPROMPT leverages LLMs' strengths in both world knowledge and programming language understanding to generate situated task plans that can be directly executed. words, which ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** PROGPROMPT provides an LLM a Pythonic program header that imports available actions and their expected parameters, shows a list of environment objects, and then defines ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** PROMPT for State Feedback represents example assertion checks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For example, if the LLM produced "reach in and pick up the jar of pickles," that string would have to neatly map to an executable action like "pick up jar." A key ... | start/goal, map, dynamics와 successor/operator description | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| State/latent | example, LLM, produced, reach, pick, pickles, string, would, have, neatly, executable, action | path, trajectory, symbolic state 또는 task-motion decision | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/action | We incorporate situated state feedback from the environment by asserting preconditions of our plan, such as being close to the fridge before attempting to open it, and responding to failed assertions with ... | feasible action sequence 또는 minimum-cost plan | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective/outcome | We make concrete recommendations about prompt structure and generation constraints through ablation experiments, demonstrate state of the art success rates in VirtualHome household tasks, and deploy our method on a physical robot ... | path cost, goal reachability, feasibility와 computation | p. 1 (Abstract) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** We present a programmatic LLM prompt structure that enables plan generation functional across situated environments, robot capabilities, and tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We introduce PROGPROMPT, a prompting scheme that goes beyond conditioning LLMs in natural language.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Evaluation Metrics We use three metrics to evaluate system performance: success rate (SR), goal conditions recall (GCR), and executability (Exec).
- **p. 5 / V. RESULTS - extractive body cue:** We find that while this method achieves reasonable partial success through GCR, it does not match [2] for program executability Exec and does not generate ...
- **p. 5 / V. RESULTS - extractive body cue:** First, we find that FEEDBACK mechanisms in the example programs, namely the assertions and recovery actions, improve performance (rows 3 versus 4 and 5 versus ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** SR is the fraction of executions that achieved all task-relevant goal-conditions.
- **p. 6 / V. RESULTS - extractive body cue:** All results shown use PROGPROMPT with comments, but not feedback.
- **p. 6 / V. RESULTS - extractive body cue:** Physical Robot Results The physical robot results are shown in Tab.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 4 (IV. EXPERIMENTS), p. 5 (V. RESULTS) |
| Embodiment/environment | We create a dataset of 70 household tasks. | hardware/simulator version and reset protocol | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Dataset/benchmark | 4: Robot plan execution rollout example on the sorting task showing relevant objects banana, strawberry, bottle, plate and box, and a distractor object drill. | role, split, size and leakage | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS), p. 5 (V. RESULTS) |
| Metric | Evaluation Metrics We use three metrics to evaluate system performance: success rate (SR), goal conditions recall (GCR), and executability (Exec). | definition, denominator, direction and uncertainty | p. 4 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 4 (IV. EXPERIMENTS) |
| Baseline/ablation | First, PROGPROMPT (rows 3-6) outperforms prior work [2] (row 8) by a substantial margin on all metrics using the same large language model backbone. | fair input/data/compute/action matching | p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 6 (V. RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / V. RESULTS - extractive body cue:** Qualitative Analysis and Limitations We manually inspect generated programs and their execution traces from PROGPROMPT and characterize common failure modes.
- **p. 5 / V. RESULTS - extractive body cue:** Many failures stem from the decision to make PROGPROMPT agnostic to the deployed environment and its peculiarities, which may be resolved through explicitly communicating, for ...
- **p. 6 / V. RESULTS - extractive body cue:** Our physical robot setup did not allow reliably tracking system state and checking assertions, and is prone to random failures due to things like grasps ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning). The Generated Plan is for microwave salmon. We highlight prompt ...
- **p. 6 / V. RESULTS - extractive body cue:** The run without distractors failed due to a random gripper failure.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We use the system of [37] to implement the policy, and use MPPI for motion generation, SceneCollisionNet [37] to avoid collisions, and generate grasp poses ...

## Why Read It

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 We illustrate a scenario where an assertion succeeds or fails, and how the generated plan corrects the error before executing the next step.를 문제로 두고, We present a programmatic LLM prompt structure that enables plan generation functional across situated environments, robot capabilities, and tasks.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
