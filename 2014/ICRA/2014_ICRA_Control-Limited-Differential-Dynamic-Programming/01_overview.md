# Control-Limited Differential Dynamic Programming

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1109/ICRA.2014.6907001.
> PDF retrieval source: https://roboti.us/lab/papers/TassaICRA14.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2014 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, optimal control, trajectory optimization, control limits
- Official paper: https://doi.org/10.1109/ICRA.2014.6907001
- Full-text retrieval: https://roboti.us/lab/papers/TassaICRA14.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 control 문제를 이해하기 위해 읽는다. 본문은 Ad-hoc task trajectories can be learned [9], which enlarge the convergence basin with a-priori knowledge and provide a consistent way to define complex task trajectories, but this is difficult to generalize to ...를 문제로 두고, Finally, Section IV describes the results, illustrating the usefulness of our approach.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Trajectory optimizers are a powerful class of methods for generating goal-directed robot motion.
- **p. 1 / Abstract - extractive body cue:** Differential Dynamic Programming (DDP) is an indirect method which optimizes only over the unconstrained control-space and is therefore fast enough to allow real-time control of ...
- **p. 1 / Abstract - extractive body cue:** Although indirect methods automatically take into account state constraints, control limits pose a difficulty.
- **p. 1 / Abstract - extractive body cue:** This is particularly problematic when an expensive robot is strong enough to break itself.
- **p. 1 / Abstract - extractive body cue:** In this paper, we demonstrate that simple heuristics used to enforce limits (clamping and penalizing) are not efficient in general.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Ad-hoc task trajectories can be learned [9], which enlarge the convergence basin with a-priori knowledge and provide a consistent way to define complex task trajectories, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In that context the problem is transcribed into a generic sequential quadratic programming (SQP) which easily admits both equality and inequality constraints.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, Section IV describes the results, illustrating the usefulness of our approach.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show experimentally in simulation that simplistic ways of handling them are inefficient and detrimental to convergence.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Trajectory optimization is the process of finding a statecontrol sequence which locally minimizes a given cost function.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Because the dynamics are folded into the optimization, state-control trajectories are always strictly feasible and "dynamic constraints" are unnecessary.
- **p. 2 / II. DIFFERENTIAL DYNAMIC PROGRAMMING - extractive body cue:** The dynamics is modeled by the generic function f xi+1 = f(xi,ui), (1) which describes the evolution from time i to i+1 of the state ...
- **p. 3 / III. CONTROL LIMITS - extractive body cue:** Na¨ıve Clamping A first attempt to enforce box constraints is to clamp the controls in the forward-pass.
- **p. 3 / C. Line Search - extractive body cue:** Once the backward pass is completed, the proposed locally-linear policy is evaluated with a forward pass: ˆx0 = x0 (7a) ˆui = ui + αki ...
- **p. 2 / II. DIFFERENTIAL DYNAMIC PROGRAMMING - extractive body cue:** Plugging this policy back into the expansion of Q, a quadratic model of V is obtained.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (5a) This is a locally-linear feedback policy with k ≜-Q-1 uuQu and K ≜-Q-1 uuQux (5b) the feed-forward modification and feedback gain matrix, respectively. | joint/task state, reference와 sensor feedback | p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 1 (Abstract) |
| State/latent | locally-linear, feedback, policy, Q-1, uuQu, uuQux, feed-forward, modification, gain, matrix, respectively, Although | state estimate, task-space error와 control decision | p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 1 (Abstract), p. 1 (I. INTRODUCTION) |
| Output/action | Although indirect methods automatically take into account state constraints, control limits pose a difficulty. | torque, force, velocity 또는 position command | p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 3 (C. Line Search) |
| Objective/outcome | Trajectory optimization is the process of finding a statecontrol sequence which locally minimizes a given cost function. | tracking, stability, constraint satisfaction과 contact behavior | p. 1 (I. INTRODUCTION), p. 4 (III. CONTROL LIMITS), p. 1 (I. INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, Section IV describes the results, illustrating the usefulness of our approach.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show experimentally in simulation that simplistic ways of handling them are inefficient and detrimental to convergence.
- **p. 6 / IV. RESULTS - extractive body cue:** However, despite some recent work in this direction [34], direct feed-forward current control is not yet a functional option, while the lack of joint torque ...
- **p. 5 / IV. RESULTS - extractive body cue:** 3 compares the results obtained with the two solvers.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 6 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Embodiment/environment | Finally, we demonstrate box-DDP on a complex platform, the humanoid robot HRP-2. | hardware/simulator version and reset protocol | p. 4 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Dataset/benchmark | Two solutions are possible to apply the DDP on a robot such as HRP-2. | role, split, size and leakage | p. 4 (IV. RESULTS), p. 5 (IV. RESULTS), p. 6 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Metric | We generated random LQ problems as follows. | definition, denominator, direction and uncertainty | p. 4 (IV. RESULTS), p. 4 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Baseline/ablation | The bottom row of Figure 2 shows a comparison between the clamping and squashing heuristics and the proposed algorithm. | fair input/data/compute/action matching | p. 4 (IV. RESULTS), p. 4 (IV. RESULTS), p. 5 (IV. RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 4 / III. CONTROL LIMITS - extractive body cue:** As reported below, in our experiments the average number of factorizations was never larger than 2.
- **p. 4 / IV. RESULTS - extractive body cue:** We begin with an initial comparison of the three solution types on a set of simple linear systems randomly selected in Sec.
- **p. 4 / IV. RESULTS - extractive body cue:** We then compare the behavior of squashing and quadratic programming on a nonholonomic car problem in Sec.

## Why Read It

Manipulation, contact, tactile, and dexterity의 control 문제를 이해하기 위해 읽는다. 본문은 Ad-hoc task trajectories can be learned [9], which enlarge the convergence basin with a-priori knowledge and provide a consistent way to define complex task trajectories, but this is difficult to generalize to ...를 문제로 두고, Finally, Section IV describes the results, illustrating the usefulness of our approach.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
