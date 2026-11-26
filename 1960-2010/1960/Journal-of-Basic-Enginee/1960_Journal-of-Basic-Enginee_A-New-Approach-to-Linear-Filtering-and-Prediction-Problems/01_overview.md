# A New Approach to Linear Filtering and Prediction Problems

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1115/1.3662552.
> PDF retrieval source: https://doi.org/10.1115/1.3662552. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1960 / Journal of Basic Engineering
- Authors: R. E. Kalman
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: state estimation, Kalman Filter, Control
- Official paper: https://api.crossref.org/works/10.1115/1.3662552
- Full-text retrieval: https://doi.org/10.1115/1.3662552
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Kalman은 상태공간 표현에서 관측이 들어올 때마다 동적 시스템의 상태 추정치를 갱신하는 선형 필터를 도출한다.

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

선형 동적 계의 관측으로 상태의 최소 오차 추정치와 오차 공분산을 재귀적으로 갱신한다. 본문은 주로 이산시간 관측을 다루며 레귤레이터 문제와의 쌍대성을 설명한다. 제어 입력을 선택하는 정책은 제시하지 않는다. [PDF 2쪽](https://eceweb1.rutgers.edu/~gajic/pdffiles/519KalmanFiltering/kalman1960.pdf#page=2) · [PDF 7쪽](https://eceweb1.rutgers.edu/~gajic/pdffiles/519KalmanFiltering/kalman1960.pdf#page=7)

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 1 actually stands for n integrators such that the output of each is a state variable; F(t) indicates how the outputs of the integrators are fed back to the inputs of the ... | 과거 관측과 계·관측 잡음의 모형 | p. 5 (Introduction), p. 4 (Introduction) |
| State/latent | actually, stands, integrators, output, state, variable, indicates, outputs, back, inputs, Theorem, states | 상태 추정치와 오차 공분산 | p. 5 (Introduction), p. 4 (Introduction), p. 4 (Introduction) |
| Output/action | (g) Theorem 2 states in effect that the optimal estimate under conditions (A) or (B) is a linear combination of all previous observations. | 새 관측을 반영한 추정 및 예측 | p. 4 (Introduction), p. 4 (Introduction), p. 5 (Introduction) |
| Objective/outcome | Assume that L is of type (2) and that the conditional distribution function F(ξ) defined by (1) is: (A) symmetric about the mean ξ : F(ξ - ξ ) = 1 - ... | 평균제곱 추정 오차 | p. 3 (Introduction), p. 3 (Introduction), p. 4 (Introduction) |

## Main Claims and Actual Contribution

- 최적 추정 오차의 공분산 방정식으로부터 필터 계수를 계산한다.
- 잡음 없는 조절 문제와 필터링 사이의 쌍대성을 보이고 예제에 적용한다.

[원문 초록](https://api.crossref.org/works/10.1115/1.3662552)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (Introduction), p. 2 (Introduction), p. 3 (Introduction), p. 4 (Introduction), p. 5 (Introduction)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** This paper introduces a new look at this whole assemblage of problems, sidestepping the difficulties just mentioned. (p. 1, Introduction).
- **Actual contribution:** Zadeh and Ragazzini solved the finite-memory case [2]. (p. 1, Introduction).
- **Evaluation boundary:** These results may be summarized as follows: (p. 4, Introduction).
- **Explicit failure boundary:** In any case, x2*(t/t - 1) = 0 at all times; one cannot predict independent noise! (p. 9, Introduction).
