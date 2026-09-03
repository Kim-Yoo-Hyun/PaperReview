# Text2Motion: From Natural Language Instructions to Feasible Plans

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2303.12153.
> PDF retrieval source: https://arxiv.org/pdf/2303.12153. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Robotics, LLM planning, task and motion planning, feasibility, skill chaining
- Official paper: https://arxiv.org/abs/2303.12153
- Full-text retrieval: https://arxiv.org/pdf/2303.12153
- Code/Project: https://sites.google.com/view/text-to-motion/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 Such strategies are challenged in long-horizon settings, where the 1 를 문제로 두고, We propose Text2Motion, a language-based planning framework that interfaces an LLM with a library of learned skills and a geometric feasibility planner [8] to solve complex sequential manipulation tasks (Figure 1).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We propose Text2Motion, a language-based planning framework enabling robots to solve sequential manipulation tasks that require long-horizon reasoning.
- **p. 1 / Abstract - extractive body cue:** Given a natural language instruction, our framework constructs both a task- and motion-level plan that is verified to reach inferred symbolic goals.
- **p. 1 / Abstract - extractive body cue:** Text2Motion uses feasibility heuristics encoded in Q-functions of a library of skills to guide task planning with Large Language Models.
- **p. 1 / Abstract - extractive body cue:** Whereas previous language-based planners only consider the feasibility of individual skills, Text2Motion actively resolves geometric dependencies spanning skill sequences by performing geometric feasibility planning during ...
- **p. 1 / Abstract - extractive body cue:** We evaluate our method on a suite of problems that require long-horizon reasoning, interpretation of abstract goals, and handling of partial affordance perception.
- **p. 1 / 1 Introduction - extractive body cue:** Such strategies are challenged in long-horizon settings, where the 1.
- **p. 3 / 3.1 LLM and skill library - extractive body cue:** If the skill succeeds, it receives a binary reward of r (or ¬r if it fails).

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We propose Text2Motion, a language-based planning framework that interfaces an LLM with a library of learned skills and a geometric feasibility planner [8] to solve ...
- **p. 5 / 4.2 Shooting-based planning - extractive body cue:** To this end, the first strategy we propose is a shooting-based Algorithm 1 Shooting-based LLM planner 1: globals: Lψ, Lχ, SatFunc, LLM, STAP 2: function ...
- **p. 6 / 4.3 Search-based planning - extractive body cue:** We propose a second planner, greedy-search (see Figure 2, Right), which at each planning iteration ranks candidate skills predicted by the LLM and adds the ...
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are twofold: (i) a hybrid LLM planner that synergistically integrates shooting-based and search-based planning strategies to construct geometrically feasible plans for tasks not ...
- **p. 3 / 3.1 LLM and skill library - extractive body cue:** Each skill ψ consists of a policy π(a/s) and a parameterized manipulation primitive ϕ(a) [59], and is associated with a contextual bandit, or a single-timestep ...
- **p. 5 / 4.1 Goal prediction - extractive body cue:** We define a satisfaction function F G sat (s) : S →{0, 1} which takes as input a geometric state s and evaluates to 1 ...
- **p. 6 / 4.3 Search-based planning - extractive body cue:** We then compute the usefulness scores Sllm(ψk t ) by summing the token Algorithm 2 Search-based LLM planner 1: globals: Lψ, Lχ, SatFunc, LLM, STAP ...
- **p. 7 / 4.4 Text2Motion - extractive body cue:** Algorithm 3 Text2Motion hybrid planner 1: globals: Lχ, SatFunc, Shooting, Greedy-Step 2: function Text2Motion(i, s1, G; K, dmax) 3: F G sat ←SatFunc(G, Lχ) ▷Goal ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We define a satisfaction function F G sat (s) : S →{0, 1} which takes as input a geometric state s and evaluates to 1 if any goal proposition g ∈G predicted ... | start/goal, map, dynamics와 successor/operator description | p. 5 (4.1 Goal prediction), p. 3 (3.1 LLM and skill library) |
| State/latent | define, satisfaction, function, takes, input, geometric, state, evaluates, goal, proposition, predicted, LLM | path, trajectory, symbolic state 또는 task-motion decision | p. 5 (4.1 Goal prediction), p. 3 (3.1 LLM and skill library), p. 5 (4.1 Goal prediction) |
| Output/action | Each skill ψ consists of a policy π(a/s) and a parameterized manipulation primitive ϕ(a) [59], and is associated with a contextual bandit, or a single-timestep Markov Decision Process (MDP): M = (S, ... | feasible action sequence 또는 minimum-cost plan | p. 3 (3.1 LLM and skill library), p. 5 (4.1 Goal prediction), p. 2 (1 Introduction) |
| Objective/outcome | 13 15: if C == ∅then 16: raise planning failure 17: end if 18: j∗= arg maxj∈C p(j) success 19: return ψ(j∗) 1:t-1 ▷Return best plan 20: end function planner, termed shooting ... | path cost, goal reachability, feasibility와 computation | p. 5 (4.2 Shooting-based planning), p. 4 (3.3 Geometric feasibility planning), p. 4 (4 Methods) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We propose Text2Motion, a language-based planning framework that interfaces an LLM with a library of learned skills and a geometric feasibility planner [8] to solve ...
- **p. 5 / 4.2 Shooting-based planning - extractive body cue:** To this end, the first strategy we propose is a shooting-based Algorithm 1 Shooting-based LLM planner 1: globals: Lψ, Lχ, SatFunc, LLM, STAP 2: function ...
- **p. 6 / 4.3 Search-based planning - extractive body cue:** We propose a second planner, greedy-search (see Figure 2, Right), which at each planning iteration ranks candidate skills predicted by the LLM and adds the ...
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are twofold: (i) a hybrid LLM planner that synergistically integrates shooting-based and search-based planning strategies to construct geometrically feasible plans for tasks not ...
- **p. 3 / 3.1 LLM and skill library - extractive body cue:** Each skill ψ consists of a policy π(a/s) and a parameterized manipulation primitive ϕ(a) [59], and is associated with a contextual bandit, or a single-timestep ...
- **p. 11 / 6.2 Search-based reasoning is - extractive body cue:** In the first two tasks (LH, Figure 5), we find that shooting achieves slightly higher success rates than greedy-search, while both methods achieve 100% success ...
- **p. 11 / 6.2 Search-based reasoning is - extractive body cue:** In terms of success, greedysearch solves 40%-60% of the PAP tasks, while shooting achieves a 10% success rate on Task 4 (LG + PAP) and ...
- **p. 10 / 6.1 Feasibility planning is required - extractive body cue:** This divergence arises because it is possible to make progress on tasks without resolving geometric dependencies in the earlier timesteps; however, failure to account for ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 11 (6.2 Search-based reasoning is), p. 11 (6.2 Search-based reasoning is) |
| Embodiment/environment | For example, Task 1 in Figure 4 requires the robot to pick and place three objects for a total of six skills. | hardware/simulator version and reset protocol | p. 9 (5.4 Task suite), p. 9 (5.4 Task suite) |
| Dataset/benchmark | Execution terminates when the score of the stop "skill" is larger than the other skills. innermono-gs: We implement the Object + Scene variant of Inner Monologue [4] by providing task-progress scene context ... | role, split, size and leakage | p. 9 (5.4 Task suite), p. 9 (5.4 Task suite), p. 8 (5.1 Baselines), p. 8 (5 Experiments) |
| Metric | Reported metrics: We report success rates and subgoal completion rates for all methods. | definition, denominator, direction and uncertainty | p. 10 (5.5 Evaluation and metrics), p. 10 (6.1 Feasibility planning is required), p. 11 (6.2 Search-based reasoning is) |
| Baseline/ablation | Top: Our method (Text2Motion) significantly outperforms all baselines on tasks involving partial affordance perception (Task 4, 5, 6). | fair input/data/compute/action matching | p. 10 (6.1 Feasibility planning is required), p. 10 (6.1 Feasibility planning is required), p. 8 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 11 / 6.1 Feasibility planning is required - extractive body cue:** Text2Motion relies on greedy-search as a fallback if shooting fails, and thus can also contend with PAP tasks.
- **p. 9 / 5.5 Evaluation and metrics - extractive body cue:** Two failure cases are tracked: i) planning failure: the method does not produce a sequence of skills ψ1:H whose optimized parameters a∗ 1:H (Eq.
- **p. 9 / 5.5 Evaluation and metrics - extractive body cue:** 4) results in a state that satisfies F G sat within a maximum plan length of dmax; ii) execution failure: the execution of a plan ...
- **p. 11 / 6.2 Search-based reasoning is - extractive body cue:** This is expected because shooting does not exhibit planning failures on these tasks (Figure 6) and Text2Motion starts by invoking shooting, which results in their ...
- **p. 12 / 7 Limitations and Future Work - extractive body cue:** While we mitigate such failures by combining greedy-search and shooting in the hybrid Text2Motion algorithm, leveraging calibration techniques to increase the reliability LLM likelihoods [64, ...
- **p. 10 / 5.5 Evaluation and metrics - extractive body cue:** To further delineate the performance of Text2Motion from shooting and greedy-search, we also report the percentages of planning and execution failures.
- **p. 10 / 6.1 Feasibility planning is required - extractive body cue:** This divergence arises because it is possible to make progress on tasks without resolving geometric dependencies in the earlier timesteps; however, failure to account for ...

## Why Read It

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 Such strategies are challenged in long-horizon settings, where the 1 를 문제로 두고, We propose Text2Motion, a language-based planning framework that interfaces an LLM with a library of learned skills and a geometric feasibility planner [8] to solve complex sequential manipulation tasks (Figure 1).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 3 (3.1 LLM and skill library), p. 4 (3.2 The planning objective), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 5 (4.2 Shooting-based planning) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
