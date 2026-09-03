# FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://journals.sagepub.com/doi/10.1177/0278364917739114.
> PDF retrieval source: https://journals.sagepub.com/doi/10.1177/0278364917739114. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / The International Journal of Robotics Research
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: NEXT
- Tags: Robotics, Planning, task and motion planning, manipulation
- Official paper: https://journals.sagepub.com/doi/10.1177/0278364917739114
- Full-text retrieval: https://journals.sagepub.com/doi/10.1177/0278364917739114
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 Planning for mobile manipulation problems involving cluttered environments and multiple manipulation primitives still presents substantial challenges.를 문제로 두고, We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Mobile manipulation problems involving many objects are challenging to solve due to the high dimensionality and multi-modality of their hybrid configuration spaces.
- **p. 1 / Abstract - extractive body cue:** Planners that perform a purely geometric search are prohibitively slow for solving these problems because they are unable to factor the configuration space.
- **p. 1 / Abstract - extractive body cue:** Symbolic task planners can efficiently construct plans involving many variables but cannot represent the geometric and kinematic constraints required in manipulation.
- **p. 1 / Abstract - extractive body cue:** We present the FFROB algorithm for solving task and motion planning problems.
- **p. 1 / Abstract - extractive body cue:** First, we introduce Extended Action Specification (EAS) as a general purpose planning representation that supports arbitrary predicates as conditions.
- **p. 1 / 1 Introduction - extractive body cue:** Planning for mobile manipulation problems involving cluttered environments and multiple manipulation primitives still presents substantial challenges.
- **p. 2 / 1 Introduction - extractive body cue:** Manipulation planning remains challenging because it is notoriously difficult to work in a high-dimensional space and make a long sequence of intertwined decisions.

## Core Idea

- **p. 2 / 1.1 Approach - extractive body cue:** We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions.
- **p. 2 / 1.1 Approach - extractive body cue:** The primary contribution of this paper is FFROB, an efficient and probabilistically complete algorithm for fully integrated task and motion planning.
- **p. 1 / 1 Introduction - extractive body cue:** A long-standing goal in robotics is to develop robots that can operate autonomously in unstructured human environments.
- **p. 2 / 1.1 Approach - extractive body cue:** EAS is able to represent actions with complex conditions much more concisely than a traditional symbolic planning representation.
- **p. 3 / 1.1 Approach - extractive body cue:** Finally, we perform experiments on challenging manipulation problems and explore the effect of various planner configurations on their performance.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2004) have been tackling problems that require long sequences of actions and large discrete state-spaces. | start/goal, map, dynamics와 successor/operator description | p. 1 (1 Introduction), p. 2 (1.1 Approach) |
| State/latent | have, been, tackling, problems, require, long, sequences, actions, large, discrete, state-spaces, involves | path, trajectory, symbolic state 또는 task-motion decision | p. 1 (1 Introduction), p. 2 (1.1 Approach), p. 2 (1.1 Approach) |
| Output/action | This involves batch sampling a set of placement poses and grasp transforms to identify the pick and place actions. | feasible action sequence 또는 minimum-cost plan | p. 2 (1.1 Approach), p. 2 (1.1 Approach), p. 1 (1 Introduction) |
| Objective/outcome | We model task and motion planning as symbolic planning where the conditions of actions are complex predicates involving geometric and kinematic constraints. | path cost, goal reachability, feasibility와 computation | p. 2 (1.1 Approach), p. 2 (1.1 Approach) |

## Main Claims and Actual Contribution

- **p. 2 / 1.1 Approach - extractive body cue:** We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions.
- **p. 2 / 1.1 Approach - extractive body cue:** The primary contribution of this paper is FFROB, an efficient and probabilistically complete algorithm for fully integrated task and motion planning.
- **p. 1 / 1 Introduction - extractive body cue:** A long-standing goal in robotics is to develop robots that can operate autonomously in unstructured human environments.
- **p. 30 / 11.4 Results - extractive body cue:** HF F Rob, HA gave the best performance in both success rate and runtime.
- **p. 30 / 11.4 Results - extractive body cue:** Helpful actions improved the performance of HF F Rob, HA over HF F Rob.
- **p. 31 / 11.4 Results - extractive body cue:** Experiment results over 50 trials. informative heuristic estimate.
- **p. 31 / 11.4 Results - extractive body cue:** All but 1 of our algorithms were able to solve it with an above 95 percent success ratio in less than 40 seconds.
- **p. 32 / Figure/Table caption - extractive body cue:** Figure 27. Best-first search extract and process procedures. A.2 Deferred Best-First Search Deferred best-first search (also called lazy greedy search) is a variant of standard ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 30 (11.4 Results), p. 30 (11.4 Results) |
| Embodiment/environment | We will restrict the robot to four side grasps per objects except on problems 1-1 & 1-2 where we use a single top grasp. | hardware/simulator version and reset protocol | p. 30 (11 Experiments), p. 30 (11 Experiments) |
| Dataset/benchmark | Problem 5 demonstrates that FFROB is able to quickly solve a long-horizon, real-world problem involving symbolic actions, cluttered environments, and nonmonotonic requirements. | role, split, size and leakage | p. 30 (11 Experiments), p. 30 (11 Experiments), p. 31 (11.4 Results), p. 27 (11 Experiments) |
| Metric | HF F Rob, HA gave the best performance in both success rate and runtime. | definition, denominator, direction and uncertainty | p. 30 (11.4 Results), p. 30 (11 Experiments), p. 31 (11.4 Results) |
| Baseline/ablation | The following heuristics are compared in the experiments: 1. | fair input/data/compute/action matching | p. 29 (11 Experiments), p. 30 (11 Experiments), p. 31 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 30 / 11 Experiments - extractive body cue:** In practice, we do not increase the sampling parameter sizes upon a sampling failure.
- **p. 30 / 11 Experiments - extractive body cue:** We enforce timeouts of 30 iterations for S-PICK-PLACE due to inverse reachability, inverse kinematics, or motion planning failures.
- **p. 33 / B.1 Proof of Theorem 1 - extractive body cue:** Finally, each segment from q0 to q0 ∈B0 or from q∗to qk ∈Bk is collision-free by the problem being robustly feasible.
- **p. 33 / B.1 Proof of Theorem 1 - extractive body cue:** For any robustly feasible motion planning problem, there exists a sequence of k + 1, where k = l 2L δ m , d-spheres (B0, ...
- **p. 31 / 12 Conclusion - extractive body cue:** Future work includes analytically and empirically investigating the quality of solutions returned by FFROB with respect to costs.
- **p. 32 / 12 Conclusion - extractive body cue:** Future work involves using the planning to guide the sampling such as done by Garrett et al.
- **p. 32 / 12 Conclusion - extractive body cue:** Additional future work involves applying FFROB to different manipulation tasks or generally planning domains involving continuous variables.

## Why Read It

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 Planning for mobile manipulation problems involving cluttered environments and multiple manipulation primitives still presents substantial challenges.를 문제로 두고, We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1.1 Approach), p. 2 (1.1 Approach) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (35 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Planning for mobile manipulation problems involving cluttered environments and multiple manipulation primitives still presents substantial challenges. (p. 1, 1 Introduction).
- **Actual contribution:** We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions. (p. 2, 1.1 Approach).
- **Evaluation boundary:** Experiment results over 50 trials. informative heuristic estimate. (p. 31, 11.4 Results).
- **Explicit failure boundary:** In practice, we do not increase the sampling parameter sizes upon a sampling failure. (p. 30, 11 Experiments).
