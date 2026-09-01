# Method - Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p073.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p073.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION)): Let g(Ar / Or) denote the generator, where O, represents the environment observation (e.g. image features and robot states) at time f, and g is a stochastic predictor of a ...

## Method Body Digest

- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Let g(Ar / Or) denote the generator, where O, represents the environment observation (e.g. image features and robot states) at time f, and g is ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** The first A' <H actions Ave, sje are executed, after which the robot re-plans by generating a new sequence of HY actions attime t+-11'.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** In the first stage, we extract scalar signals from policy inputs and/or outputs (e-g., robot states, visual features, generated future actions) that are discriminative between ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** The models may also encounter out-ofdistribution (OOD) conditions where the input observations deviate from the training data distribution, In such cases, the generated actions may ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Given an initial condition Op and the generator g to output the next actions, we obtain a trajectory 14 = (Oo, Ao, Ou, An', -.-,Ot, ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** passed through a feature extractor and then, along with robot states, constitute observations O,.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** (Left - Stage 1) Multi-view camera images and robot states are distilled into failure detection scalar scores.

## Design Rationale

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Aside from being performant, our method enables faster inference than prior work [1], which requires sampling, ‘multiple robot actions during inference.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** ur contributions are as follows, We present FAIL-Detect, ‘4 modular two stage uncertainty-aware runtime failure detec~ tion framework for generative imitation learning-based robotic ‘manipulation, First, ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** A key novelty of our method is the ability to learn failure detection signals without access 10 failure data.

## Source Evidence Cues

- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Let g(Ar / Or) denote the generator, where O, represents the environment observation (e.g. image features and robot states) at time f, and g is ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** The first A' <H actions Ave, sje are executed, after which the robot re-plans by generating a new sequence of HY actions attime t+-11'.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | Let g(Ar / Or) denote the generator, where O, represents the environment observation (e.g. image features and robot states) at time f, ... | p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | The first A' <H actions Ave, sje are executed, after which the robot re-plans by generating a new sequence of HY actions ... | p. 3 (III. PROBLEM FORMULATION) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | Let g(Ar / Or) denote the generator, where O, represents the environment observation (e.g. image features and robot states) at time f, ... | p. 3 (III. PROBLEM FORMULATION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | first, stage, extract, scalar, signals, policy, inputs, and/or, outputs, robot, states, visual, features, generated | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | first, stage, extract, scalar, signals, policy, inputs, and/or, outputs, robot | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | Aside, being, performant, enables, faster, inference, prior, requires, sampling, multiple | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | not recovered | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. INTRODUCTION - extractive body cue:** In the first stage, we extract scalar signals from policy inputs and/or outputs (e-g., robot states, visual features, generated future actions) that are discriminative between ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Let g(Ar / Or) denote the generator, where O, represents the environment observation (e.g. image features and robot states) at time f, and g is ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** The models may also encounter out-ofdistribution (OOD) conditions where the input observations deviate from the training data distribution, In such cases, the generated actions may ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Given an initial condition Op and the generator g to output the next actions, we obtain a trajectory 14 = (Oo, Ao, Ou, An', -.-,Ot, ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** passed through a feature extractor and then, along with robot states, constitute observations O,.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** (Left - Stage 1) Multi-view camera images and robot states are distilled into failure detection scalar scores.
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | In simulation, we adjust the thirdperson camera 10cm upwards atthe first time step after = 50 to simulate a camera bump mid-rollout'. | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | We reproduce the method and adopt hyperparameters used in their push-T example, where we generate a batch of 256 action predictions per ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not recovered | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | For instance, testing on an A6000 GPU with 50 rollouts, logpZO score computation takes 0.04 (Square) and 0.033% (Transport) per time step, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / V. EXPERIMENTS - extractive body cue:** Due to the long STAC inference time (even after parallelization) and resulting high system latency, we omit its comparison on the two robot hardware tasks.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** visual encoded features jointly trained with the policy on the demonstration data, PCA-kmeans first uses PCA to embed the training features and then applies K-means ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Let, denote, generator, where, represents, environment, observation, image, features, robot, states, time, stochastic, predictor, sequence, actions, Age, Avsates, AtsH-aie, next.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | significantly fewer rollouts in the robot hardware tasks (i.e., 50 rollouts) compared to the simulation tasks (i.e., 2000 rollouts) | p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Filtering / recovery | Fig. 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP. We consider two ... | p. 7 (Figure/Table caption), p. 6 (V. EXPERIMENTS) |
| Monitoring / re-entry | Fig. 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP. We consider two ... | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / V. EXPERIMENTS - extractive body cue:** We did not employ the VLM component of the STAC failure detector to remain as real-time feasible as possible.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** visual encoded features jointly trained with the policy on the demonstration data, PCA-kmeans first uses PCA to embed the training features and then applies K-means ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel from the position in (a) towards the ...
- **p. 7 / C. Do failure detections align with human intuition? - extractive body cue:** This performance shows the capacity of failure-free failure detection methods to robustly identify failures across many scenarios.
- **p. 3 / IV. FAILURE DETECTION FRAMEWORK - extractive body cue:** 2) Calibrate time-varying thresholds 1, based on a CP band. ‘The final decision D(r:8) = 1(Dry(Ar.Or:6) > me) raises a failure flag if the sealar ...
- **p. 7 / C. Do failure detections align with human intuition? - extractive body cue:** How performant is failure detection without failure data?
- **p. 8 / C. Do failure detections align with human intuition? - extractive body cue:** and higher failure/suecess separation.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION), objective 본문 anchor 없음, temporal p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 3 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), p. 8 (C. Do failure detections align with human intuition?).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
