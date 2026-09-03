# Differentiable Robust Model Predictive Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p003.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p003.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: NEXT
- Tags: Robotics, MPC, robust control, differentiable optimization, uncertainty, Robotarium
- Official paper: https://www.roboticsproceedings.org/rss20/p003.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p003.html
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 control 문제를 이해하기 위해 읽는다. 본문은 However, when applied to autonomous systems acting in the real-world, deterministic MPC is often unable to respond to large disturbances that occur due to environmental factors, model uncertainty, etc.를 문제로 두고, The main contribution of this work is the development of a novel differentiable tube-based MPC (DT-MPC) framework for safe, robust control.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Deterministic model predictive control (MPC), while powerful, is often insufficient for effectively controlling autonomous systems in the real-world.
- **p. 1 / Abstract - extractive body cue:** Factors such as environmental noise and model error can cause deviations from the expected nominal performance.
- **p. 1 / Abstract - extractive body cue:** Robust MPC algorithms aim to bridge this gap between deterministic and uncertain control.
- **p. 1 / Abstract - extractive body cue:** However, these methods are often excessively difficult to tune for robustness due to the nonlinear and non-intuitive effects that controller parameters have on performance.
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we first present a unifying perspective on differentiable optimization for control using the implicit function theorem (IFT), from which existing state-of-the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, when applied to autonomous systems acting in the real-world, deterministic MPC is often unable to respond to large disturbances that occur due to environmental ...
- **p. 2 / II. MATHEMATICAL BACKGROUND - extractive body cue:** However, in practice, the system under study is subject to large dynamical uncertainty through effects such as unmodeled physics, random noise, etc., that results in ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contribution of this work is the development of a novel differentiable tube-based MPC (DT-MPC) framework for safe, robust control.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the main contributions of this work include: 1) the derivation of a general differentiable optimal control framework enabled through a novel application of ...
- **p. 1 / Abstract - extractive body cue:** Drawing parallels with differential dynamic programming, the IFT enables the derivation of an efficient differentiable optimal control framework.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This motivates the development of control algorithms that explicitly account for unknown disturbances in the dynamics and guarantee robustness.
- **p. 4 / II. MATHEMATICAL BACKGROUND - extractive body cue:** From the safe MPC via barrier methods perspective, the proposed work provides a novel expansion of the works [3], [14] and [19] to a tube-based ...
- **p. 5 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** However, we propose an alternative methodology enabled through differentiable optimization that allows the parameters to be learned and adapted online through minimization of an appropriately ...
- **p. 8 / IV. DIFFERENTIABLE TUBE-BASED MPC - extractive body cue:** In order to optimize both the nominal and ancillary controller, we propose to use a loss function of the form L(τ ∗(θ), ¯τ(¯θ)) =
- **p. 8 / IV. DIFFERENTIABLE TUBE-BASED MPC - extractive body cue:** Next, we propose an algorithm that applies the DOC methodology presented in Section III to the real-time tuning of tube-based controllers of the form given ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Safety is enforced through the use of discrete barrier states [3], which enables scalable constraint satisfaction such that safe planning and control can be executed in real-time. | joint/task state, reference와 sensor feedback | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| State/latent | Safety, enforced, through, discrete, barrier, states, enables, scalable, constraint, satisfaction, safe, planning | state estimate, task-space error와 control decision | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (II. MATHEMATICAL BACKGROUND) |
| Output/action | This allows for an implicit form of feedback since the controls are reoptimized from the current state of the system at every time step of the problem [43]. | torque, force, velocity 또는 position command | p. 1 (I. INTRODUCTION), p. 3 (II. MATHEMATICAL BACKGROUND), p. 3 (II. MATHEMATICAL BACKGROUND) |
| Objective/outcome | Algorithm 1: Differentiable Optimal Control (DOC) Input: Derivatives of L (equivalently f, ℓ, ϕ, and ξ) and L along the solution z∗ Output: Gradient of upper-level loss ∇θL 1 eVx, Vxx, ek, ... | tracking, stability, constraint satisfaction과 contact behavior | p. 6 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 4 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 2 (II. MATHEMATICAL BACKGROUND) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contribution of this work is the development of a novel differentiable tube-based MPC (DT-MPC) framework for safe, robust control.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the main contributions of this work include: 1) the derivation of a general differentiable optimal control framework enabled through a novel application of ...
- **p. 1 / Abstract - extractive body cue:** Drawing parallels with differential dynamic programming, the IFT enables the derivation of an efficient differentiable optimal control framework.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This motivates the development of control algorithms that explicitly account for unknown disturbances in the dynamics and guarantee robustness.
- **p. 4 / II. MATHEMATICAL BACKGROUND - extractive body cue:** From the safe MPC via barrier methods perspective, the proposed work provides a novel expansion of the works [3], [14] and [19] to a tube-based ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** On the other hand, the proposed DT-MPC bounds the true system within a safer tube around the nominal trajectory by tuning the ancillary MPC in ...
- **p. 11 / V. EXPERIMENTS - extractive body cue:** Overall, DT-MPC remains safe while increasing the task success rate by over 200% (20% success rate for NT-MPC vs.
- **p. 11 / V. EXPERIMENTS - extractive body cue:** The JAX-based Python implementation of our method runs at over 50 Hz on the Robotarium - we expect further speedups can be achieved through a ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 10 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS) |
| Embodiment/environment | The generality of the proposed DT-MPC is established through benchmarks on five nonlinear robotics systems subject to highly non-convex constraints such as dense obstacle fields. | hardware/simulator version and reset protocol | p. 9 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS) |
| Dataset/benchmark | Hardware Experiment - Robotarium Finally, we implement the proposed methodology on the Robotarium (Fig. | role, split, size and leakage | p. 9 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 10 (V. EXPERIMENTS) |
| Metric | On the other hand, the proposed DT-MPC bounds the true system within a safer tube around the nominal trajectory by tuning the ancillary MPC in real-time, drastically increasing the success rate to ... | definition, denominator, direction and uncertainty | p. 10 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS) |
| Baseline/ablation | 8), a state-of-the-art, remotely accessible robotics hardware platform for multi-agent control [52]. | fair input/data/compute/action matching | p. 11 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 20 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 10 / V. EXPERIMENTS - extractive body cue:** For this task, the nominal controller (tuned for deterministic task completion) is too aggressive for the magnitude of disturbances received, leading to a large number ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** The results in Table I show that, while NT-MPC fails to reach the target in the majority of the cases and occasionally violates the safety ...
- **p. 11 / V. EXPERIMENTS - extractive body cue:** While the deterministic nominal trajectory reaches the target state during every trial, the ancillary controller cannot keep up with the desired aggressive jumping maneuver due ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4: Controlled Dubins vehicle trajectories subject to large noise. NT-MPC trajectories diverge from the nominal trajec- tory and the uncertainty increases over time. Meanwhile, ...
- **p. 11 / V. EXPERIMENTS - extractive body cue:** NT-MPC is robust to disturbances due to both modeling error and process noise and can reach the target state successfully (Fig.
- **p. 9 / V. EXPERIMENTS - extractive body cue:** While both algorithms remain safe and avoid collisions (see Table I), only DT-MPC is able to complete the task the majority of the time.
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 8: Comparison of tube-based MPC approaches on the Robotarium hardware platform [52]. (a) NT-MPC successfully reaches the target when the task is in-distribution. (b) ...

## Why Read It

Planning and control의 control 문제를 이해하기 위해 읽는다. 본문은 However, when applied to autonomous systems acting in the real-world, deterministic MPC is often unable to respond to large disturbances that occur due to environmental factors, model uncertainty, etc.를 문제로 두고, The main contribution of this work is the development of a novel differentiable tube-based MPC (DT-MPC) framework for safe, robust control.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (II. MATHEMATICAL BACKGROUND), p. 3 (II. MATHEMATICAL BACKGROUND), p. 1 (I. INTRODUCTION), p. 3 (II. MATHEMATICAL BACKGROUND), p. 5 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (22 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** This allows for an implicit form of feedback since the controls are reoptimized from the current state of the system at every time step of the problem [43]. (p. 1, I. INTRODUCTION).
- **Actual contribution:** In summary, the main contributions of this work include: 1) the derivation of a general differentiable optimal control framework enabled through a novel application of the implicit function theorem, 2) ... (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Fig. 11: Robot arm numerical comparisons. As Diff-MPC [5] uses an LQ approximation to the control problem, their algorithm is able to achieve very fast timings. However, this results in ... (p. 20, Figure/Table caption).
- **Explicit failure boundary:** For this task, the nominal controller (tuned for deterministic task completion) is too aggressive for the magnitude of disturbances received, leading to a large number of failures even when controlled ... (p. 10, V. EXPERIMENTS).
