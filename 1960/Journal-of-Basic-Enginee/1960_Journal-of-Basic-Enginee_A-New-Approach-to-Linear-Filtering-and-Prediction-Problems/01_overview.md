# A New Approach to Linear Filtering and Prediction Problems

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1115/1.3662552.
> PDF retrieval source: https://doi.org/10.1115/1.3662552. Reading tracker status/evidence was not changed.

- Year/Venue: 1960 / Journal of Basic Engineering
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: CORE
- Tags: Robotics, state estimation, Kalman Filter, Control
- Official paper: https://doi.org/10.1115/1.3662552
- Full-text retrieval: https://doi.org/10.1115/1.3662552
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 estimation 문제를 이해하기 위해 읽는다. 본문은 (3) Important generalizations (e.g., growing-memory filters, nonstationary prediction) require new derivations, frequently of considerable difficulty to the nonspecialist.를 문제로 두고, The new method developed here is applied to two well-known problems, confirming and extending earlier results.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Introduction - extractive body cue:** AN IMPORTANT class of theoretical and practical problems in communication and control is of a statistical nature.
- **p. 1 / Introduction - extractive body cue:** Such problems are: (i) Prediction of random signals; (ii) separation of random signals from random noise; (iii) detection of signals of known form (pulses, sinusoids) ...
- **p. 1 / Introduction - extractive body cue:** In his pioneering work, Wiener [1]3 showed that problems (i) and (ii) lead to the so-called Wiener-Hopf integral equation; he also gave a method (spectral ...
- **p. 1 / Introduction - extractive body cue:** Many extensions and generalizations followed Wiener's basic work.
- **p. 1 / Introduction - extractive body cue:** Zadeh and Ragazzini solved the finite-memory case [2].
- **p. 1 / Introduction - extractive body cue:** (3) Important generalizations (e.g., growing-memory filters, nonstationary prediction) require new derivations, frequently of considerable difficulty to the nonspecialist.
- **p. 2 / Introduction - extractive body cue:** With the state-transition method, a single derivation covers a large variety of problems: growing and infinite memory filters, stationary and nonstationary statistics, etc.; difficulty (3) ...

## Core Idea

- **p. 1 / Introduction - extractive body cue:** The new method developed here is applied to two well-known problems, confirming and extending earlier results.
- **p. 9 / Introduction - extractive body cue:** (q) The duality theorem offers a powerful tool for developing more deeply the theory (as opposed to the computation) of Wiener filters, as mentioned in ...
- **p. 5 / Introduction - extractive body cue:** The dynamics is then described in terms of state transitions, i.e., one must specify how one state is transformed into another as time passes.
- **p. 5 / Introduction - extractive body cue:** In fact, if we consider (15) in the steady state (assuming it is a stable system), in other words, if we neglect the initial state ...
- **p. 1 / Introduction - extractive body cue:** We shall emphasize the concepts of state and state transition; in other words, linear systems will be specified by systems of first-order difference (or differential) ...
- **p. 2 / Introduction - extractive body cue:** Solution of the equation for the covariance matrix starts at the time t0 when the first observation is taken; at each later time t the ...
- **p. 3 / Introduction - extractive body cue:** Assume that L is of type (2) and that the conditional distribution function F(ξ) defined by (1) is: (A) symmetric about the mean ξ : ...
- **p. 1 / Introduction - extractive body cue:** The classical filtering and prediction problem is re-examined using the BodeShannon representation of random processes and the "state transition" method of analysis of dynamic systems.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 1 actually stands for n integrators such that the output of each is a state variable; F(t) indicates how the outputs of the integrators are fed back to the inputs of the ... | 시간별 sensor observation과 알려진 model/control input | p. 5 (Introduction), p. 4 (Introduction) |
| State/latent | actually, stands, integrators, output, state, variable, indicates, outputs, back, inputs, Theorem, states | latent state와 uncertainty/belief | p. 5 (Introduction), p. 4 (Introduction), p. 4 (Introduction) |
| Output/action | (g) Theorem 2 states in effect that the optimal estimate under conditions (A) or (B) is a linear combination of all previous observations. | causal estimate, prediction 또는 smoothing output | p. 4 (Introduction), p. 4 (Introduction), p. 5 (Introduction) |
| Objective/outcome | Assume that L is of type (2) and that the conditional distribution function F(ξ) defined by (1) is: (A) symmetric about the mean ξ : F(ξ - ξ ) = 1 - ... | estimation error, covariance 또는 downstream state quality | p. 3 (Introduction), p. 3 (Introduction), p. 4 (Introduction) |

## Main Claims and Actual Contribution

- **p. 1 / Introduction - extractive body cue:** The new method developed here is applied to two well-known problems, confirming and extending earlier results.
- **p. 9 / Introduction - extractive body cue:** (q) The duality theorem offers a powerful tool for developing more deeply the theory (as opposed to the computation) of Wiener filters, as mentioned in ...
- **p. 8 / Introduction - extractive body cue:** This is due to two things: (1) The time dependence of Φ(t + 1; t) and M(t); (2) the fact that the estimation starts at ...
- **p. 4 / Introduction - extractive body cue:** These results may be summarized as follows:
- **p. 4 / Introduction - extractive body cue:** These results are well-known though not easily accessible in the control systems literature.
- **p. 7 / Introduction - extractive body cue:** (i) The results stated in Theorem 3 do not resolve completely Problem I.
- **p. 7 / Introduction - extractive body cue:** If t1 ≥ t + 1, we first observe by repeated application of (16) that x(t + s) = Φ(t + s; t + 1)x(t ...
- **p. 8 / Introduction - extractive body cue:** and the minimum performance index at time t is given by

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (Introduction), p. 4 (Introduction) |
| Embodiment/environment | Of course, the solution of Equation (32), or of its differential-equation equivalent, is a much simpler task than solution of the Wiener-Hopf equation. | hardware/simulator version and reset protocol | p. 7 (Introduction) |
| Dataset/benchmark | Of course, the solution of Equation (32), or of its differential-equation equivalent, is a much simpler task than solution of the Wiener-Hopf equation. | role, split, size and leakage | p. 7 (Introduction) |
| Metric | The covariance matrix of the estimation error is | definition, denominator, direction and uncertainty | p. 7 (Introduction), p. 6 (Introduction), p. 7 (Introduction) |
| Baseline/ablation | Without being able to separate in some sense causes and effects, i.e., without the assumption of causality, one can hardly hope for useful results. | fair input/data/compute/action matching | p. 4 (Introduction), p. 9 (Introduction), p. 4 (Introduction) |

## Explicit Limitations and Failure Boundary

- **p. 9 / Introduction - extractive body cue:** In any case, x2*(t/t - 1) = 0 at all times; one cannot predict independent noise!
- **p. 5 / Introduction - extractive body cue:** but of course now Φ(t + 1; t), ∆(t) cannot be expressed in general in closed form.
- **p. 6 / Introduction - extractive body cue:** If y~ (t/t - 1) ≡0, which means that the values of all components of this random vector are zero for almost every possible event, ...
- **p. 5 / Introduction - extractive body cue:** It is a fairly generally accepted fact that primary macroscopic sources of random phenomena are independent gaussian processes.5 A well-known example is the noise voltage ...
- **p. 8 / Introduction - extractive body cue:** The first general solution of the noise-free regulator problem is due to the author [18].
- **p. 8 / Introduction - extractive body cue:** The Dual Problem Let us now consider another problem which is conceptually very different from optimal estimation, namely, the noise-free regulator problem.
- **p. 9 / Introduction - extractive body cue:** Let x1(t) be the position and x2(t) the velocity of the particle; x3(t) is the noise.

## Why Read It

Planning and control의 estimation 문제를 이해하기 위해 읽는다. 본문은 (3) Important generalizations (e.g., growing-memory filters, nonstationary prediction) require new derivations, frequently of considerable difficulty to the nonspecialist.를 문제로 두고, The new method developed here is applied to two well-known problems, confirming and extending earlier results.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (Introduction), p. 2 (Introduction), p. 1 (Introduction), p. 3 (Introduction), p. 4 (Introduction), p. 5 (Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
