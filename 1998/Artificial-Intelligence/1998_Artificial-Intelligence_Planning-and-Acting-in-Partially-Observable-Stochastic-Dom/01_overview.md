# Planning and Acting in Partially Observable Stochastic Domains

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (45 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.sciencedirect.com/science/article/pii/S000437029800023X.
> PDF retrieval source: https://www.cassandra.org/arc/papers/aij98.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1998 / Artificial Intelligence
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: CORE
- Tags: Robotics, Planning, POMDP, partial observability, uncertainty, decision making
- Official paper: https://www.sciencedirect.com/science/article/pii/S000437029800023X
- Full-text retrieval: https://www.cassandra.org/arc/papers/aij98.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (45 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 Problems like the one described above can be modeled as partially observable Markov decision processes (POMDPs).를 문제로 두고, This paper is intended to make two contributions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we bring techniques from operations research to bear on the problem of choosing optimal actions in partially observable stochastic domains, We begin ...
- **p. 1 / Abstract - extractive body cue:** We then outline a novel algorithm for solving Pours off line and show how, in some cases, a finitememory controller can be extracted from the ...
- **p. 1 / Abstract - extractive body cue:** We conclude with a discussion of how our approach relates to previous work, the complexity of finding exact solutions to PoMDPs, and of some possibilities ...
- **p. 1 / Abstract - extractive body cue:** Key wonds: planning, uncertainty, partially observable Markov decision processes
- **p. 1 / Abstract - extractive body cue:** Consider the problem of a robot navigating in a large office building.
- **p. 2 / 1 Introduction - extractive body cue:** Problems like the one described above can be modeled as partially observable Markov decision processes (POMDPs).
- **p. 2 / 1 Introduction - extractive body cue:** This is essentially a plareing problem: given a complete and correct model of the world dynamics and a reward structure, find an optimal way to ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** This paper is intended to make two contributions.
- **p. 3 / 1 Introduction - extractive body cue:** The second is to describe a novel algorithmic approach for solving POMDPs exactly.
- **p. 19 / 44 The Witness Algorithm - extractive body cue:** The code in Table 2 outlines our approach to solving PompPs.
- **p. 23 / 4.5. Alternative Approaches - extractive body cue:** The resulting algorithm might be called the two-pass algorithm [9], and, its form is much like the witness algorithm because it first constructs each separate ...
- **p. 19 / 44 The Witness Algorithm - extractive body cue:** This is because maximizing over actions and then policy trees is the same as maximizing over the pooled sets of policy trees.
- **p. 7 / 2.9 Computing an Optimal Policy - extractive body cue:** Tt makes use of an aundliary function, Q/(s), which is the tstep value of starting in state s, taking action a, then continuing with the ...
- **p. 23 / 4.5. Alternative Approaches - extractive body cue:** Although the algorithm is sophisticated and, in principle, avoids exhaustively enumerating the set of possibly useful policy trees at each iteration, it appears to run ...
- **p. 18 / 44 The Witness Algorithm - extractive body cue:** Tn what sense is the witness algorithm superior to previous algorithms for solving Pompps, then?

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The component labeled SE is the state estimator: it is responsible for updating the belief state based on the last action, the current observation, and the previous belief state, The component labeled ... | start/goal, map, dynamics와 successor/operator description | p. 9 (3.2 Problem Structure), p. 3 (1 Introduction) |
| State/latent | component, labeled, state, estimator, responsible, updating, belief, last, action, current, observation, previous | path, trajectory, symbolic state 또는 task-motion decision | p. 9 (3.2 Problem Structure), p. 3 (1 Introduction), p. 10 (3.2 Problem Structure) |
| Output/action | As shown in Figure 1, the agent takes as input the state of the world and generates as output actions, which themselves affect the state of the world. | feasible action sequence 또는 minimum-cost plan | p. 3 (1 Introduction), p. 10 (3.2 Problem Structure), p. 25 (5.1 The Tiger Problem) |
| Objective/outcome | This is because maximizing over actions and then policy trees is the same as maximizing over the pooled sets of policy trees. | path cost, goal reachability, feasibility와 computation | p. 19 (44 The Witness Algorithm), p. 19 (44 The Witness Algorithm), p. 12 (3.4 Finding an Optimal Policy) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** This paper is intended to make two contributions.
- **p. 3 / 1 Introduction - extractive body cue:** The second is to describe a novel algorithmic approach for solving POMDPs exactly.
- **p. 19 / 44 The Witness Algorithm - extractive body cue:** The code in Table 2 outlines our approach to solving PompPs.
- **p. 18 / 44 The Witness Algorithm - extractive body cue:** ‘To improve the complexity of the valueiteration algorithm, we must avoid generating V;*; instead, we would like to generate the elements of V; direct] Ifwe ...
- **p. 20 / 441 Witness inner loop - extractive body cue:** The tree p is built with subtrees 7» for each observation 0, We add the new policy tree to Uy to improve the approximation.
- **p. 20 / 442 Identifying a witness - extractive body cue:** That is, if there is a belief state, b, for which Prey is an improvement over all the policy trees we have found so far, ...
- **p. 21 / 44.3. Checking the witness condition - extractive body cue:** If the linear program finds that the biggest advantage is not positive, that is, that 5 <0, then Pyew is not an improvement over all ...
- **p. 21 / 44.3. Checking the witness condition - extractive body cue:** The linear program in Table 3 solves exactly this problem, The variable d is the minimum amount of improvement of Pew Over any policy tree ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 18 (44 The Witness Algorithm), p. 20 (441 Witness inner loop) |
| Embodiment/environment | A plan graph is essentially a finite-state controller, It uses the minimal possible amount of memory to act optimally in a partially observable environment. | hardware/simulator version and reset protocol | p. 30 (5.4 Plan Graphs) |
| Dataset/benchmark | A plan graph is essentially a finite-state controller, It uses the minimal possible amount of memory to act optimally in a partially observable environment. | role, split, size and leakage | p. 30 (5.4 Plan Graphs) |
| Metric | i pproptiately and so tends to gain less long-term reward. | definition, denominator, direction and uncertainty | p. 15 (1) I step to go), p. 15 (1) I step to go), p. 24 (5.1 The Tiger Problem) |
| Baseline/ablation | As a result, compared to exhaustive caumeration, very few nonuseful policy trees are considered and the algorithm runs extremely quickly. | fair input/data/compute/action matching | p. 24 (4.5. Alternative Approaches), p. 30 (5.4 Plan Graphs), p. 29 (5.4 Plan Graphs) |

## Explicit Limitations and Failure Boundary

- **p. 15 / 1) I step to go - extractive body cue:** In such belief states, the agent cannot select
- **p. 18 / 42 Value Functions as Sets of Vectors - extractive body cue:** Pruning requires one linear program for each element of the starting set of policy trees and does not add to the asymptotic complexity of the ...
- **p. 25 / 5.1 The Tiger Problem - extractive body cue:** The LISTEN action does not change the state of the world.
- **p. 26 / 5.2. Finite-Horizon Policies - extractive body cue:** If the agent starts from the uniform belief state, b= (0.5,0.5), listening once does not change the belief state enough to make the expected value ...

## Why Read It

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 Problems like the one described above can be modeled as partially observable Markov decision processes (POMDPs).를 문제로 두고, This paper is intended to make two contributions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 23 (4.5. Alternative Approaches) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (45 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Problems like the one described above can be modeled as partially observable Markov decision processes (POMDPs). (p. 2, 1 Introduction).
- **Actual contribution:** This paper is intended to make two contributions. (p. 3, 1 Introduction).
- **Evaluation boundary:** The linear program in Table 3 solves exactly this problem, The variable d is the minimum amount of improvement of Pew Over any policy tree in Uy at b. (p. 21, 44.3. Checking the witness condition).
- **Explicit failure boundary:** as the agent does not observe the goal state, it will alwajrs have some non-zero belief that it is in any of the non-goal states, since the actions have non-zero ... (p. 11, 3.2 Problem Structure).
