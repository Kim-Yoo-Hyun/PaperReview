# Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p118.html.
> PDF retrieval source: https://arxiv.org/pdf/2403.10454.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: NEXT
- Tags: Robotics, TAMP, POMDP, uncertainty, risk-aware planning, closed-loop control
- Official paper: https://www.roboticsproceedings.org/rss20/p118.html
- Full-text retrieval: https://arxiv.org/pdf/2403.10454.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 control 문제를 이해하기 위해 읽는다. 본문은 However, computing 1A reference for all notation introduced henceforth is provided in Table IV in the appendix. the belief updates exactly is intractable in many problems.를 문제로 두고, To mitigate this, we introduce the concept of a belief-space controller, which takes the current belief as input and executes in closedloop fashion over extended time horizons.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Integrated task and motion planning (TAMP) has proven to be a valuable approach to generalizable long-horizon robotic manipulation and navigation problems.
- **p. 1 / Abstract - extractive body cue:** However, the typical TAMP problem formulation assumes full observability and deterministic action effects.
- **p. 1 / Abstract - extractive body cue:** These assumptions limit the ability of the planner to gather information and make decisions that are risk-aware.
- **p. 1 / Abstract - extractive body cue:** We propose a strategy for TAMP with Uncertainty and Risk Awareness (TAMPURA) that is capable of efficiently solving long-horizon planning problems with initialstate and action ...
- **p. 1 / Abstract - extractive body cue:** Our planner reasons under uncertainty at both the abstract task level and continuous controller level.
- **p. 3 / III. BACKGROUND - extractive body cue:** However, computing 1A reference for all notation introduced henceforth is provided in Table IV in the appendix. the belief updates exactly is intractable in many ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these methods typically do not generalize to solving arbitrary complex goals over long time horizons.

## Core Idea

- **p. 3 / III. BACKGROUND - extractive body cue:** To mitigate this, we introduce the concept of a belief-space controller, which takes the current belief as input and executes in closedloop fashion over extended ...
- **p. 5 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** We introduce an extension to PDDL for specifying schemata for controllers with uncertain effects.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach, TAMPURA, is to exploit a coarse model of each controller's preconditions and effects to rapidly solve deterministic, symbolic planning problems that guide the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that in tasks requiring risk sensitivity, information gathering, and robustness to uncertainty, TAMPURA significantly outperforms reinforcement learning, Monte Carlo tree search, and determinized ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Advances in techniques like behavior cloning (BC) [1, 2], reinforcement learning (RL) [3, 4], and model-based control [5, 6] have made it possible to develop ...
- **p. 4 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** The first action recommended by this policy is the next controller to execute on the robot.
- **p. 4 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** 3: while abs(b) /∈G do 4: if abs(b) /∈Bsparse then 5: args ←(b0, G, O, s) 6: s, ˆT , Bsparse ←Model-Learning(args) 7: ▷Solve the ...
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** We use Bayes3D perception framework for probabilistic pose inference [29].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Belief-State Controller MDP When the action space A represents primitive controls to the robot such as joint torques or end-effector velocity commands, the time horizons to perform meaningful tasks can be enormous, ... | joint/task state, reference와 sensor feedback | p. 3 (III. BACKGROUND), p. 3 (III. BACKGROUND) |
| State/latent | Belief-State, Controller, MDP, When, action, space, represents, primitive, controls, robot, joint, torques | state estimate, task-space error와 control decision | p. 3 (III. BACKGROUND), p. 3 (III. BACKGROUND), p. 2 (I. INTRODUCTION) |
| Output/action | A POMDP is a tuple M = ⟨S, O, A, T , Z, r, b0, γ⟩.1 S, O, and A are the state, observation, and action spaces. | torque, force, velocity 또는 position command | p. 3 (III. BACKGROUND), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective/outcome | In this paper, we focus on planning problems with objectives modeled as goals in belief space (e.g., the goal may be to believe that with high probability the world is in a ... | tracking, stability, constraint satisfaction과 contact behavior | p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 9 (VII. REAL-WORLD IMPLEMENTATION) |

## Main Claims and Actual Contribution

- **p. 3 / III. BACKGROUND - extractive body cue:** To mitigate this, we introduce the concept of a belief-space controller, which takes the current belief as input and executes in closedloop fashion over extended ...
- **p. 5 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** We introduce an extension to PDDL for specifying schemata for controllers with uncertain effects.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach, TAMPURA, is to exploit a coarse model of each controller's preconditions and effects to rapidly solve deterministic, symbolic planning problems that guide the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that in tasks requiring risk sensitivity, information gathering, and robustness to uncertainty, TAMPURA significantly outperforms reinforcement learning, Monte Carlo tree search, and determinized ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Advances in techniques like behavior cloning (BC) [1, 2], reinforcement learning (RL) [3, 4], and model-based control [5, 6] have made it possible to develop ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to the green cell. ...
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** See the supplementary material for videos of successful completions under various initializations of these tasks.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| Embodiment/environment | Searching for Objects in Clutter This task is the real-world counterpart to the PARTIAL OBSERVABILITY simulated experiment. | hardware/simulator version and reset protocol | p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| Dataset/benchmark | We applied TAMPURA to five simulated and two realworld robotics problems, illustrated in Figure 2 and Figure 1, | role, split, size and leakage | p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 7 (VI. SIMULATED EXPERIMENTS & ANALYSIS) |
| Metric | Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to the green cell. Red intensity corresponds to p, the probability ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (VI. SIMULATED EXPERIMENTS & ANALYSIS) |
| Baseline/ablation | Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to the green cell. Red intensity corresponds to p, the probability ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 9 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / VIII. DISCUSSION - extractive body cue:** Despite these novelties, TAMPURA, and TAMP in general, have several limitations.
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** The primary failure modes were (1) failure in perception (due, we believe, to improperly calibrated hard-coded camera poses), and (2) issues with tension in the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Uncertainty and Risk Aware Task and Motion Planning. (a) The robot's continuous space of probabilistic beliefs about world state is partitioned into a ...

## Why Read It

Planning and control의 control 문제를 이해하기 위해 읽는다. 본문은 However, computing 1A reference for all notation introduced henceforth is provided in Table IV in the appendix. the belief updates exactly is intractable in many problems.를 문제로 두고, To mitigate this, we introduce the concept of a belief-space controller, which takes the current belief as input and executes in closedloop fashion over extended time horizons.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (III. BACKGROUND), p. 1 (I. INTRODUCTION), p. 3 (III. BACKGROUND), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
