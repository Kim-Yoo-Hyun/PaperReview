# Method - A New Approach to Linear Filtering and Prediction Problems

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1115/1.3662552; PDF retrieval source: https://doi.org/10.1115/1.3662552. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

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

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| State / observation model | latent robot/world state와 measurement 관계를 표현한다 | prior state와 sensor observation | transition, observation, uncertainty 또는 learned encoder를 구성 | state/uncertainty representation | The dynamics is then described in terms of state transitions, i.e., one must specify how one state is transformed into another as ... | p. 5 (Introduction), p. 5 (Introduction) |
| Prediction / fusion | 새 시점의 prior 또는 fused state를 계산한다 | history, model, multi-sensor input | recursive prediction, registration, fusion 또는 temporal aggregation을 수행 | prior/fused state | In fact, if we consider (15) in the steady state (assuming it is a stable system), in other words, if we neglect ... | p. 5 (Introduction), p. 1 (Introduction) |
| Correction / downstream handoff | measurement feedback으로 state를 보정하고 전달한다 | prior와 current observation | innovation, refinement, confidence update 또는 query를 수행 | posterior/map/task cue | We shall emphasize the concepts of state and state transition; in other words, linear systems will be specified by systems of first-order ... | p. 1 (Introduction), p. 2 (Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / Introduction - extractive body cue:** Assume that L is of type (2) and that the conditional distribution function F(ξ) defined by (1) is: (A) symmetric about the mean ξ : ...
- **p. 3 / Introduction - extractive body cue:** One (but by no means the only) natural way of choosing the random variable X1 is to require that this choice should minimize the average ...
- **p. 4 / Introduction - extractive body cue:** This shows that, if w also minimizes the quadratic loss, we must have 0 ) ( 2 = -w x E
- **p. 4 / Introduction - extractive body cue:** There is another way in which the orthogonal projection can be characterized: x is that vector in Y(t) (i.e., that linear function of the random ...
- **p. 6 / Introduction - extractive body cue:** Given the observed values of y(t0), ..., y(t) find an estimate x*(t1/t) of x(t1) which minimizes the expected loss.
- **p. 1 / Introduction - extractive body cue:** Booton discussed the nonstationary Wiener-Hopf equation [4].
- **Formal bridge:** latent state x_t and observation o_t -> estimate x̂_t and uncertainty Σ_t -> estimation error or posterior uncertainty -> calibrated state estimate for downstream control.
- **Equation/algorithm anchors:** p. 1 (Introduction), p. 1 (Introduction), p. 2 (Introduction), p. 2 (Introduction), p. 3 (Introduction), p. 3 (Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | actually, stands, integrators, output, state, variable, indicates, outputs, back, inputs, Theorem, states, effect, optimal | 시간별 sensor observation과 알려진 model/control input | body cue; exact tensor/frame verify |
| State/latent | actually, stands, integrators, output, state, variable, indicates, outputs, back, inputs | latent state와 uncertainty/belief | body cue; notation verify |
| Action/output | developed, here, applied, well-known, problems, confirming, extending, earlier, duality, theorem | causal estimate, prediction 또는 smoothing output | body cue; unit/decoder verify |
| Objective/constraint | Assume, type, conditional, distribution, function, defined, symmetric, about, mean, convex | estimation error or posterior uncertainty | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / Introduction - extractive body cue:** 1 actually stands for n integrators such that the output of each is a state variable; F(t) indicates how the outputs of the integrators are ...
- **p. 4 / Introduction - extractive body cue:** (g) Theorem 2 states in effect that the optimal estimate under conditions (A) or (B) is a linear combination of all previous observations.
- **p. 4 / Introduction - extractive body cue:** In other words, the optimal estimate can be regarded as the output of a linear filter, with the input being the actually occurring values of ...
- **p. 5 / Introduction - extractive body cue:** Thus fij(t) is the coefficient with which the output of the jth integrator is fed back to the input of the ith integrator.
- **p. 6 / Introduction - extractive body cue:** It includes also the problem of reconstructing all the state variables of a linear dynamic system from noisy observations of some of the state variables ...
- **p. 6 / Introduction - extractive body cue:** The state of the estimator is the previous estimate, the input is the last measured value of the observable random variable y(t) , the transition ...
- **p. 8 / Introduction - extractive body cue:** 8 M(t0 + τ) effect of state on observation.
- **Normalized interface:** observation=시간별 sensor observation과 알려진 model/control input; state=latent state와 uncertainty/belief; output/action=causal estimate, prediction 또는 smoothing output.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 observation의 filtering과 필요 시 future prediction/history smoothing horizon을 구분한다. | Zadeh and Ragazzini solved the finite-memory case [2]. | episode/sequence/action-chunk boundary |
| Rate / latency | observation arrival마다 estimator update; numeric sensor/control rate는 paper-specific. | Fundamental assumptions and their consequences tend to be obscured. | Hz/fps, inference time and control rate |
| Memory | state estimate와 uncertainty summary; smoothing이면 observation/history buffer가 추가된다. | Zadeh and Ragazzini solved the finite-memory case [2]. | window and reset |
| Compute | state dimension, covariance/model update와 sensor synchronization이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** dynamics, then, described, terms, state, transitions, must, specify, transformed, another, time, passes, fact, consider, steady, assuming, stable, system, other, words.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| State / observation model | Of course, the solution of Equation (32), or of its differential-equation equivalent, is a much simpler task than solution of the Wiener-Hopf ... | p. 7 (Introduction), p. 7 (Introduction) |
| Prediction / fusion | Without being able to separate in some sense causes and effects, i.e., without the assumption of causality, one can hardly hope for ... | p. 4 (Introduction), p. 9 (Introduction) |
| Correction / downstream handoff | This is due to two things: (1) The time dependence of Φ(t + 1; t) and M(t); (2) the fact that the ... | p. 8 (Introduction), p. 4 (Introduction) |

## Failure and Ablation Link

- **p. 4 / Introduction - extractive body cue:** Without being able to separate in some sense causes and effects, i.e., without the assumption of causality, one can hardly hope for useful results.
- **p. 8 / Introduction - extractive body cue:** 8 M(t0 + τ) effect of state on observation.
- **p. 8 / Introduction - extractive body cue:** Mˆ (T - τ) effect of control vectors on state.
- **p. 5 / Introduction - extractive body cue:** If all coefficients of F(t), D(t), M(t) are constants, we say that the dynamic system (12) is timeinvariant or stationary.
- **p. 7 / Introduction - extractive body cue:** Now we remove the restriction that t1 = t + 1.
- **p. 9 / Introduction - extractive body cue:** In a few cases, ∆* and Φ* can be put into "closed form." Without discussing here how (if at all) such closed forms can be ...
- **p. 5 / Introduction - extractive body cue:** where x is an n-vector, the state of the system (the components xi of x are called state variables); u(t) is an m-vector (m ≤ ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (Introduction), p. 5 (Introduction), p. 1 (Introduction), p. 2 (Introduction), p. 3 (Introduction), p. 1 (Introduction), objective p. 3 (Introduction), p. 3 (Introduction), p. 4 (Introduction), p. 4 (Introduction), p. 6 (Introduction), p. 1 (Introduction), temporal p. 1 (Introduction), p. 1 (Introduction), p. 2 (Introduction), p. 2 (Introduction), p. 3 (Introduction), p. 4 (Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
