# Method - Failure Prediction with Statistical Guarantees for Vision-Based Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2202.05894; PDF retrieval source: https://arxiv.org/pdf/2202.05894. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION)): To evaluate the performance of the failure predictor, we introduce the error of applying the predictor f in an environment E where a policy π is running: C(rf(E, π)) := ...

## Method Body Digest

- **p. 3 / III. PROBLEM FORMULATION - extractive PDF cue:** To evaluate the performance of the failure predictor, we introduce the error of applying the predictor f in an environment E where a policy π ...
- **p. 3 / III. PROBLEM FORMULATION - extractive PDF cue:** Let rf : E × Π →X T × YT denote the function that ‘rolls out' the system with the given policy and the predictor ...
- **p. 3 / III. PROBLEM FORMULATION - extractive PDF cue:** Our goal is to use the training environments S to learn failure predictors that minimize the errors and provably generalize to unseen environments drawn from ...
- **p. 3 / III. PROBLEM FORMULATION - extractive PDF cue:** IV-C, it is often useful to consider the class-conditional misclassfication error that allows us to trade-off false positives and false negatives: ˜C(rf(E, π)) := X ...
- **p. 2 / III. PROBLEM FORMULATION - extractive PDF cue:** For example, p0∩1 denotes the probability of the
- **p. 2 / III. PROBLEM FORMULATION - extractive PDF cue:** The only exception, D, instead denotes probability distributions.
- **p. 3 / III. PROBLEM FORMULATION - extractive PDF cue:** We consider a deterministic, black-box task policy π : O →A that maps (potentially a history of) observations to a control input.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our primary contribution is to develop an approach for learning a failure predictor with guaranteed bounds on error rates, given a black-box control policy that ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our primary contribution is to develop an approach for learning a failure predictor with guaranteed bounds on error rates, given a black-box control policy that ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** box policy for training purposes, we present a reduction of the failure prediction problem (which involves non-i.i.d. data in the form of sensor observations) to ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** We envision that the addition of a failure predictor could substantially improve the safety of the overall robotic system. ∗Equal Contribution Fig.

## Source Evidence Cues

- **p. 3 / III. PROBLEM FORMULATION - extractive PDF cue:** To evaluate the performance of the failure predictor, we introduce the error of applying the predictor f in an environment E where a policy π ...
- **p. 3 / III. PROBLEM FORMULATION - extractive PDF cue:** Let rf : E × Π →X T × YT denote the function that ‘rolls out' the system with the given policy and the predictor ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | To evaluate the performance of the failure predictor, we introduce the error of applying the predictor f in an environment E where ... | p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | Let rf : E × Π →X T × YT denote the function that ‘rolls out' the system with the given policy ... | p. 3 (III. PROBLEM FORMULATION) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | To evaluate the performance of the failure predictor, we introduce the error of applying the predictor f in an environment E where ... | p. 3 (III. PROBLEM FORMULATION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. PROBLEM FORMULATION - extractive PDF cue:** Our goal is to use the training environments S to learn failure predictors that minimize the errors and provably generalize to unseen environments drawn from ...
- **p. 3 / III. PROBLEM FORMULATION - extractive PDF cue:** IV-C, it is often useful to consider the class-conditional misclassfication error that allows us to trade-off false positives and false negatives: ˜C(rf(E, π)) := X ...
- **p. 2 / III. PROBLEM FORMULATION - extractive PDF cue:** For example, p0∩1 denotes the probability of the
- **p. 2 / III. PROBLEM FORMULATION - extractive PDF cue:** The only exception, D, instead denotes probability distributions.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | consider, deterministic, black-box, task, policy, maps, potentially, history, observations, control, input, primary, contribution, develop | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | consider, deterministic, black-box, task, policy, maps, potentially, history, observations, control | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | primary, contribution, develop, learning, failure, predictor, guaranteed, bounds, error, rates | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | goal, training, environments, learn, failure, predictors, minimize, errors, provably, generalize | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. PROBLEM FORMULATION - extractive PDF cue:** We consider a deterministic, black-box task policy π : O →A that maps (potentially a history of) observations to a control input.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our primary contribution is to develop an approach for learning a failure predictor with guaranteed bounds on error rates, given a black-box control policy that ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** box policy for training purposes, we present a reduction of the failure prediction problem (which involves non-i.i.d. data in the form of sensor observations) to ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** How can we guarantee the safety of a control policy for a robot that operates using high-dimensional sensor observations (e.g., a vision-based navigation policy for ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Our algorithmic approach is then to train a failure predictor (e.g., in the form of a neural network that takes as input a history of ...
- **p. 3 / III. PROBLEM FORMULATION - extractive PDF cue:** Let rf : E × Π →X T × YT denote the function that ‘rolls out' the system with the given policy and the predictor ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | If at any time step, the failure class is largest, we say it is a prediction of failure; otherwise, it is a ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | We note TABLE II RESULTS FOR FAILURE PREDICTION ON NAVIGATION TASK Setting Standard Occluded Obstacle True Expected Failure (Sim) 0.253 0.514 Misclassification ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not recovered | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | We note TABLE II RESULTS FOR FAILURE PREDICTION ON NAVIGATION TASK Setting Standard Occluded Obstacle True Expected Failure (Sim) 0.253 0.514 Misclassification ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. PROBLEM FORMULATION - extractive PDF cue:** To evaluate the performance of the failure predictor, we introduce the error of applying the predictor f in an environment E where a policy π ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive PDF cue:** When the failure predictor stops the rollout due to a prediction of failure, we re-run the trial without the failure predictor to determine the true ...
- **p. 3 / III. PROBLEM FORMULATION - extractive PDF cue:** Thus there are four possible outcomes: (1) true positive (1∩1), predicting 1 at least once before failure; (2) true negative (0 ∩0), never predicting 1 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** evaluate, performance, failure, predictor, introduce, error, applying, environment, where, policy, running, Tfail, step, when, occurs, whole, rollout, successful, Let, denote.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | In order to create different environments for the robot, we obtained 50 mugs of diverse geometries from the ShapeNet dataset [49]. | p. 8 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Filtering / recovery | Across all three settings, we achieve tight guarantees on failure prediction compared to the true expected failure rate of the policies. | p. 8 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |
| Monitoring / re-entry | In order to evaluate the failure predictor on policies with different task success rates, we choose three different policies saved at different ... | p. 8 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |

## Failure and Ablation Link

- **p. 7 / V. EXPERIMENTAL RESULTS - extractive PDF cue:** When the failure predictor stops the rollout due to a prediction of failure, we re-run the trial without the failure predictor to determine the true ...
- **p. 5 / IV. FAILURE PREDICTION WITH GUARANTEED ERROR - extractive PDF cue:** Bound on Class-Conditional Misclassification Error The example above shows that minimizing the total misclassification error can fail to perform well when the relative importance of ...
- **p. 6 / IV. FAILURE PREDICTION WITH GUARANTEED ERROR - extractive PDF cue:** Thus, if the policy designer has access to a single training dataset to learn a failure predictor, conformal prediction does not guarantee that the expected ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive PDF cue:** We note TABLE II RESULTS FOR FAILURE PREDICTION ON NAVIGATION TASK Setting Standard Occluded Obstacle True Expected Failure (Sim) 0.253 0.514 Misclassification Bound 0.128 0.154 ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1. We train a failure predictor which guarantees (with high probability) detection of a failure ahead of time. A policy is tasked with avoiding ...
- **p. 8 / V. EXPERIMENTAL RESULTS - extractive PDF cue:** Since the gripper does not reach the mug in the first two out of five steps of the rollout, we only train the failure predictor ...
- **p. 3 / IV. FAILURE PREDICTION WITH GUARANTEED ERROR - extractive PDF cue:** BOUNDS Our approach for learning failure predictors with guaranteed error bounds relies on a reduction to results from the PACBayes generalization theory from supervised learning; ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION), objective p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION), p. 2 (III. PROBLEM FORMULATION), p. 2 (III. PROBLEM FORMULATION), temporal p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 8 (V. EXPERIMENTAL RESULTS), p. 8 (V. EXPERIMENTAL RESULTS), p. 3 (III. PROBLEM FORMULATION), p. 2 (II. RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
