# LLM+P: Empowering Large Language Models with Optimal Planning Proficiency

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2304.11477.
> PDF retrieval source: https://arxiv.org/pdf/2304.11477. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Robotics, LLM planning, classical planning, PDDL, plan verification
- Official paper: https://arxiv.org/abs/2304.11477
- Full-text retrieval: https://arxiv.org/pdf/2304.11477
- Code/Project: https://github.com/Cranial-XIX/llm-p
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 A Failure Example of GPT-4 in Planning Problem (P1): You have 5 blocks.를 문제로 두고, Given how LLMs are designed and trained, this phenomenon should come as no surprise.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Large language models (LLMs) have demonstrated remarkable zero-shot generalization abilities: stateof-the-art chatbots can provide plausible answers to many common questions that arise in daily life.
- **p. 1 / Abstract - extractive body cue:** However, so far, LLMs cannot reliably solve long-horizon robot planning problems.
- **p. 1 / Abstract - extractive body cue:** By contrast, classical planners, once a problem is given in a formatted way, can use efficient search algorithms to quickly identify correct, or even optimal, ...
- **p. 1 / Abstract - extractive body cue:** In an effort to get the best of both worlds, this paper introduces LLM+P, the first framework that incorporates the strengths of classical planners into ...
- **p. 1 / Abstract - extractive body cue:** LLM+P takes in a natural language description of a planning problem, then returns a correct (or optimal) plan for solving that problem in natural language.
- **p. 1 / I. INTRODUCTION - extractive body cue:** A Failure Example of GPT-4 in Planning Problem (P1): You have 5 blocks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** One cannot place more than one block on another block. b5 is on top of b3. b4 is on top of b2. b2 is on ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Given how LLMs are designed and trained, this phenomenon should come as no surprise.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Specifically, they can be (relatively) easily fooled by, for example, asking for the result of a straightforward arithmetic problem that does not appear in their ...
- **p. 3 / III. METHOD - extractive body cue:** Large Language Model + Classical Planner (LLM+P) Having introduced the LLM's ability to encode problems in PDDL and in-context learning, we are ready to introduce ...
- **p. 3 / III. METHOD - extractive body cue:** When the context is included with the prompt from the example above, the resulting PDDL problem file is directly solvable by the planner.
- **p. 4 / III. METHOD - extractive body cue:** 2) A domain PDDL is provided to define the actions that the robot is capable of.
- **p. 4 / III. METHOD - extractive body cue:** Once the problem PDDL file is generated, we feed it into any classical planner, together with the provided domain PDDL file, to generate a PDDL ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | S G are usually specified as a list of goal conditions, all of which must hold in a goal state. • A is a set of symbolic actions. • f is the ... | start/goal, map, dynamics와 successor/operator description | p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND) |
| State/latent | usually, specified, list, goal, conditions, must, hold, state, symbolic, actions, underlying, transition | path, trajectory, symbolic state 또는 task-motion decision | p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND), p. 3 (III. METHOD) |
| Output/action | It includes a set of predicates that define the state space S and the actions (i.e., A ) with their preconditions and effects (i.e., the transition function f). | feasible action sequence 또는 minimum-cost plan | p. 2 (II. BACKGROUND), p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Objective/outcome | path cost, goal reachability, feasibility와 computation | path cost, goal reachability, feasibility와 computation | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Given how LLMs are designed and trained, this phenomenon should come as no surprise.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Specifically, they can be (relatively) easily fooled by, for example, asking for the result of a straightforward arithmetic problem that does not appear in their ...
- **p. 5 / 1) How well does LLM-AS-P work? To what extent - extractive body cue:** We report the success rate of the optimal alias, and for the domains that time out, we show the success rate of the sub-optimal alias ...
- **p. 5 / 1) How well does LLM-AS-P work? To what extent - extractive body cue:** Domain Success Rate % LLMLLM LLMToT LLM+PLLM+P BARMAN 0 0 0 0 20 (100) BLOCKSWORLD 20 15 (30) 0 (5) 0 90 FLOORTILE 0 0 ...
- **p. 2 / II. BACKGROUND - extractive body cue:** A solution to a planning problem P is a symbolic plan π in the form of ⟨a1,a2,...,aN⟩, such that the preconditions of a1 hold in ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent) |
| Embodiment/environment | Benchmark Problems We present seven robot planning domains borrowed from past International Planning Competitions and 20 automatically generated tasks for each domain [67]. | hardware/simulator version and reset protocol | p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent) |
| Dataset/benchmark | Robot Demonstration We verify that LLM+P can efficiently solve realistic service robot problems by deploying it on a real robot tasked with tidying up a home. | role, split, size and leakage | p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent), p. 6 (1) We observe that though LLM-AS-P provides a plan), p. 3 (III. METHOD) |
| Metric | We report the success rate of the optimal alias, and for the domains that time out, we show the success rate of the sub-optimal alias in parentheses. | definition, denominator, direction and uncertainty | p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent), p. 6 (1) We observe that though LLM-AS-P provides a plan) |
| Baseline/ablation | can state-of-the-art LLMs and LLM-based reasoning methods be directly used for planning? | fair input/data/compute/action matching | p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent), p. 3 (III. METHOD) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 2: Demonstration of the optimal tidy-up plan. The robot starts at the coffee table and 1) picks up the bottle, 2) navigates to a ...
- **p. 2 / 3. Move b4 from b2 to the table - extractive body cue:** Limitation: In this paper, we do not ask the LLM to recognize that it has been posed a prompt that is suitable for processing using ...
- **p. 5 / 1) How well does LLM-AS-P work? To what extent - extractive body cue:** Robots can move around and change colors but cannot step on painted tiles.
- **p. 6 / 1) We observe that though LLM-AS-P provides a plan - extractive body cue:** In particular, in the BLOCKSWORLD domain, LLM-AS-P cannot keep track of properties like ON and CLEAR.

## Why Read It

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 A Failure Example of GPT-4 in Planning Problem (P1): You have 5 blocks.를 문제로 두고, Given how LLMs are designed and trained, this phenomenon should come as no surprise.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND), p. 3 (III. METHOD), p. 3 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
