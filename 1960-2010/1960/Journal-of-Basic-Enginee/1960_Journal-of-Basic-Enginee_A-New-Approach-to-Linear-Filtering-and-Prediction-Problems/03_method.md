# Method - A New Approach to Linear Filtering and Prediction Problems

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1115/1.3662552; PDF retrieval source: https://doi.org/10.1115/1.3662552. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (Introduction), p. 5 (Introduction), p. 1 (Introduction), p. 2 (Introduction), p. 3 (Introduction), p. 1 (Introduction)): The dynamics is then described in terms of state transitions, i.e., one must specify how one state is transformed into another as time passes.

## Method Body Digest

- **p. 5 / Introduction - extractive body cue:** The dynamics is then described in terms of state transitions, i.e., one must specify how one state is transformed into another as time passes.
- **p. 5 / Introduction - extractive body cue:** In fact, if we consider (15) in the steady state (assuming it is a stable system), in other words, if we neglect the initial state ...
- **p. 1 / Introduction - extractive body cue:** We shall emphasize the concepts of state and state transition; in other words, linear systems will be specified by systems of first-order difference (or differential) ...
- **p. 2 / Introduction - extractive body cue:** Solution of the equation for the covariance matrix starts at the time t0 when the first observation is taken; at each later time t the ...
- **p. 3 / Introduction - extractive body cue:** Assume that L is of type (2) and that the conditional distribution function F(ξ) defined by (1) is: (A) symmetric about the mean ξ : ...
- **p. 1 / Introduction - extractive body cue:** The classical filtering and prediction problem is re-examined using the BodeShannon representation of random processes and the "state transition" method of analysis of dynamic systems.
- **p. 2 / Introduction - extractive body cue:** The new formulation of the Wiener problem brings it into contact with the growing new theory of control systems based on the "state" point of ...
- **p. 3 / Introduction - extractive body cue:** One (but by no means the only) natural way of choosing the random variable X1 is to require that this choice should minimize the average ...

## Design Rationale

- **p. 1 / Introduction - extractive body cue:** The new method developed here is applied to two well-known problems, confirming and extending earlier results.
- **p. 9 / Introduction - extractive body cue:** (q) The duality theorem offers a powerful tool for developing more deeply the theory (as opposed to the computation) of Wiener filters, as mentioned in ...

## Source Evidence Cues

- **p. 5 / Introduction - extractive body cue:** The dynamics is then described in terms of state transitions, i.e., one must specify how one state is transformed into another as time passes.
- **p. 5 / Introduction - extractive body cue:** In fact, if we consider (15) in the steady state (assuming it is a stable system), in other words, if we neglect the initial state ...
- **p. 1 / Introduction - extractive body cue:** We shall emphasize the concepts of state and state transition; in other words, linear systems will be specified by systems of first-order difference (or differential) ...
- **p. 2 / Introduction - extractive body cue:** Solution of the equation for the covariance matrix starts at the time t0 when the first observation is taken; at each later time t the ...
- **p. 3 / Introduction - extractive body cue:** Assume that L is of type (2) and that the conditional distribution function F(ξ) defined by (1) is: (A) symmetric about the mean ξ : ...
- **p. 1 / Introduction - extractive body cue:** The classical filtering and prediction problem is re-examined using the BodeShannon representation of random processes and the "state transition" method of analysis of dynamic systems.
- **p. 2 / Introduction - extractive body cue:** The new formulation of the Wiener problem brings it into contact with the growing new theory of control systems based on the "state" point of ...
- **Detected method headings:** none reliably recovered

## Pipeline

과거 관측과 계·관측 잡음의 모형 → 상태 추정치와 오차 공분산 → 새 관측을 반영한 추정 및 예측. [방법·평가의 원문 근거](./01_overview.md#observation-state-and-output-interface)

## Objective / Update Rule

- **p. 3 / Introduction - extractive body cue:** Assume that L is of type (2) and that the conditional distribution function F(ξ) defined by (1) is: (A) symmetric about the mean ξ : ...
- **p. 3 / Introduction - extractive body cue:** One (but by no means the only) natural way of choosing the random variable X1 is to require that this choice should minimize the average ...
- **p. 4 / Introduction - extractive body cue:** This shows that, if w also minimizes the quadratic loss, we must have 0 ) ( 2 = -w x E
- **p. 4 / Introduction - extractive body cue:** There is another way in which the orthogonal projection can be characterized: x is that vector in Y(t) (i.e., that linear function of the random ...
- **p. 6 / Introduction - extractive body cue:** Given the observed values of y(t0), ..., y(t) find an estimate x*(t1/t) of x(t1) which minimizes the expected loss.
- **p. 1 / Introduction - extractive body cue:** Booton discussed the nonstationary Wiener-Hopf equation [4].
- **Formal bridge:** 과거 관측과 계·관측 잡음의 모형 → 상태 추정치와 오차 공분산 → 새 관측을 반영한 추정 및 예측.
- **Equation/algorithm anchors:** p. 1 (Introduction), p. 1 (Introduction), p. 2 (Introduction), p. 2 (Introduction), p. 3 (Introduction), p. 3 (Introduction).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | actually, stands, integrators, output, state, variable, indicates, outputs, back, inputs, Theorem, states, effect, optimal | 과거 관측과 계·관측 잡음의 모형 | body cue; exact tensor/frame verify |
| State/latent | actually, stands, integrators, output, state, variable, indicates, outputs, back, inputs | 상태 추정치와 오차 공분산 | body cue; notation verify |
| Action/output | developed, here, applied, well-known, problems, confirming, extending, earlier, duality, theorem | 새 관측을 반영한 추정 및 예측 | body cue; unit/decoder verify |
| Objective/constraint | Assume, type, conditional, distribution, function, defined, symmetric, about, mean, convex | estimation error or posterior uncertainty | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / Introduction - extractive body cue:** 1 actually stands for n integrators such that the output of each is a state variable; F(t) indicates how the outputs of the integrators are ...
- **p. 4 / Introduction - extractive body cue:** (g) Theorem 2 states in effect that the optimal estimate under conditions (A) or (B) is a linear combination of all previous observations.
- **p. 4 / Introduction - extractive body cue:** In other words, the optimal estimate can be regarded as the output of a linear filter, with the input being the actually occurring values of ...
- **p. 5 / Introduction - extractive body cue:** Thus fij(t) is the coefficient with which the output of the jth integrator is fed back to the input of the ith integrator.
- **p. 6 / Introduction - extractive body cue:** It includes also the problem of reconstructing all the state variables of a linear dynamic system from noisy observations of some of the state variables ...
- **p. 6 / Introduction - extractive body cue:** The state of the estimator is the previous estimate, the input is the last measured value of the observable random variable y(t) , the transition ...
- **p. 8 / Introduction - extractive body cue:** 8 M(t0 + τ) effect of state on observation.
- **Normalized interface:** observation=과거 관측과 계·관측 잡음의 모형; state=상태 추정치와 오차 공분산; output/action=새 관측을 반영한 추정 및 예측.

## Temporal and Runtime Contract

| Contract | PDF body cue | Unresolved detail |
|---|---|---|
| Horizon | Zadeh and Ragazzini solved the finite-memory case [2]. | episode/sequence/action-chunk boundary |
| Rate / latency | Fundamental assumptions and their consequences tend to be obscured. | Hz/fps, inference time and control rate |
| Memory | Zadeh and Ragazzini solved the finite-memory case [2]. | window and reset |
| Compute | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

## Method-Specific Formal Details

- **Body-defined terms:** dynamics, then, described, terms, state, transitions, must, specify, transformed, another, time, passes, fact, consider, steady, assuming, stable, system, other, words.
- **Relevant PDF headings:** not reliably recovered.

## Evaluation Link

| 평가 근거 | 원문에서 추출한 내용 | 원문 위치 |
|---|---|---|
| 원문 대조 | Of course, the solution of Equation (32), or of its differential-equation equivalent, is a much simpler task than solution of the Wiener-Hopf ... | p. 7 (Introduction), p. 7 (Introduction) |
| 원문 대조 | Without being able to separate in some sense causes and effects, i.e., without the assumption of causality, one can hardly hope for ... | p. 4 (Introduction), p. 9 (Introduction) |
| 원문 대조 | This is due to two things: (1) The time dependence of Φ(t + 1; t) and M(t); (2) the fact that the ... | p. 8 (Introduction), p. 4 (Introduction) |

## Failure and Ablation Link

- **p. 4 / Introduction - extractive body cue:** Without being able to separate in some sense causes and effects, i.e., without the assumption of causality, one can hardly hope for useful results.
- **p. 8 / Introduction - extractive body cue:** 8 M(t0 + τ) effect of state on observation.
- **p. 8 / Introduction - extractive body cue:** Mˆ (T - τ) effect of control vectors on state.
- **p. 5 / Introduction - extractive body cue:** If all coefficients of F(t), D(t), M(t) are constants, we say that the dynamic system (12) is timeinvariant or stationary.
- **p. 7 / Introduction - extractive body cue:** Now we remove the restriction that t1 = t + 1.
- **p. 9 / Introduction - extractive body cue:** In a few cases, ∆* and Φ* can be put into "closed form." Without discussing here how (if at all) such closed forms can be ...
- **p. 5 / Introduction - extractive body cue:** where x is an n-vector, the state of the system (the components xi of x are called state variables); u(t) is an m-vector (m ≤ ...

## Reproduction Checklist

[공통 검토 기준](../../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (Introduction), p. 5 (Introduction), p. 1 (Introduction), p. 2 (Introduction), p. 3 (Introduction), p. 1 (Introduction), objective p. 3 (Introduction), p. 3 (Introduction), p. 4 (Introduction), p. 4 (Introduction), p. 6 (Introduction), p. 1 (Introduction), temporal p. 1 (Introduction), p. 1 (Introduction), p. 2 (Introduction), p. 2 (Introduction), p. 3 (Introduction), p. 4 (Introduction).

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** 1 actually stands for n integrators such that the output of each is a state variable; F(t) indicates how the outputs of the integrators are fed back to the inputs ... (p. 5, Introduction).
- **Objective/update evidence:** Booton discussed the nonstationary Wiener-Hopf equation [4]. (p. 1, Introduction).
- **Temporal/runtime evidence:** Zadeh and Ragazzini solved the finite-memory case [2]. (p. 1, Introduction).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
