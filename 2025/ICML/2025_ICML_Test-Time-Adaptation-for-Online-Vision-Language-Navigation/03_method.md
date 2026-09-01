# Method - Test-Time Adaptation for Online Vision-Language Navigation with Feedback-based Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=K4GaB4fdIq; PDF retrieval source: https://openreview.net/pdf/a273e15cd7e38fd010663df74dfea2486251fe0e.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Task Description), p. 3 (3.2. Binary Episodic Feedback), p. 4 (3.2. Binary Episodic Feedback), p. 4 (3.2. Binary Episodic Feedback), p. 5 (3.3. Stochastic Gradient Reversion), p. 5 (3.3. Stochastic Gradient Reversion)): Each element Xn consists of a natural language instruction In, and an initial visual state s0 n, which is a 360◦panoramic view of the surrounding environment.

## Method Body Digest

- **p. 3 / 3.1. Task Description - extractive PDF cue:** Each element Xn consists of a natural language instruction In, and an initial visual state s0 n, which is a 360◦panoramic view of the surrounding ...
- **p. 3 / 3.2. Binary Episodic Feedback - extractive PDF cue:** FEEDTTA leverages a Monte Carlo policy gradient algorithm REINFORCE (Williams, 1992) to learn from the received feedback at the end of each navigation episode.
- **p. 4 / 3.2. Binary Episodic Feedback - extractive PDF cue:** (Right) Specifically, among the variants of α, the negative value (reversion) shifts the original gradient closest to the counterfactual distribution. mated gradient of the policy ...
- **p. 4 / 3.2. Binary Episodic Feedback - extractive PDF cue:** Here, the parameter update directly depends on the navigation outcome F and the log probability for each selected action, implying that the policy flexibly adopts ...
- **p. 5 / 3.3. Stochastic Gradient Reversion - extractive PDF cue:** TTA for Online VLN with Feedback-based Reinforcement Learning J(θ)F=-1).
- **p. 5 / 3.3. Stochastic Gradient Reversion - extractive PDF cue:** However, our empirical observations indicate that reversing the gradient with a negative α yields better performance than when α ≥0 (see Exp.
- **p. 3 / 3.2. Binary Episodic Feedback - extractive PDF cue:** A general REINFORCE algorithm aims at optimizing the parameter θ of a policy πθ to maximize the score function of the expected return Gt = ...
- **p. 4 / 3.3. Stochastic Gradient Reversion - extractive PDF cue:** Utilizing the modified gradient, the parameter update at the nth iteration becomes: θn+1 ←θn + η∇J(θ)′, (6) where η > 0 is the learning rate.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, the contributions of this work are as follows. • We introduce FEEDTTA, a novel TTA framework for online VLN utilizing feedback-based RL.
- **p. 2 / 1. Introduction - extractive PDF cue:** Based on this analysis, we introduce FEEDTTA, a novel TTA framework for online VLN using feedback-based reinforcement learning (RL).
- **p. 3 / 3.1. Task Description - extractive PDF cue:** Each element Xn consists of a natural language instruction In, and an initial visual state s0 n, which is a 360◦panoramic view of the surrounding ...

## Source Evidence Cues

- **p. 3 / 3.1. Task Description - extractive PDF cue:** Each element Xn consists of a natural language instruction In, and an initial visual state s0 n, which is a 360◦panoramic view of the surrounding ...
- **p. 3 / 3.2. Binary Episodic Feedback - extractive PDF cue:** FEEDTTA leverages a Monte Carlo policy gradient algorithm REINFORCE (Williams, 1992) to learn from the received feedback at the end of each navigation episode.
- **p. 4 / 3.2. Binary Episodic Feedback - extractive PDF cue:** (Right) Specifically, among the variants of α, the negative value (reversion) shifts the original gradient closest to the counterfactual distribution. mated gradient of the policy ...
- **p. 4 / 3.2. Binary Episodic Feedback - extractive PDF cue:** Here, the parameter update directly depends on the navigation outcome F and the log probability for each selected action, implying that the policy flexibly adopts ...
- **p. 5 / 3.3. Stochastic Gradient Reversion - extractive PDF cue:** TTA for Online VLN with Feedback-based Reinforcement Learning J(θ)F=-1).
- **p. 5 / 3.3. Stochastic Gradient Reversion - extractive PDF cue:** However, our empirical observations indicate that reversing the gradient with a negative α yields better performance than when α ≥0 (see Exp.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Each element Xn consists of a natural language instruction In, and an initial visual state s0 n, which is a 360◦panoramic view ... | p. 3 (3.1. Task Description), p. 3 (3.2. Binary Episodic Feedback) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | FEEDTTA leverages a Monte Carlo policy gradient algorithm REINFORCE (Williams, 1992) to learn from the received feedback at the end of each ... | p. 3 (3.2. Binary Episodic Feedback), p. 4 (3.2. Binary Episodic Feedback) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | (Right) Specifically, among the variants of α, the negative value (reversion) shifts the original gradient closest to the counterfactual distribution. mated gradient ... | p. 4 (3.2. Binary Episodic Feedback), p. 4 (3.2. Binary Episodic Feedback) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.2. Binary Episodic Feedback - extractive PDF cue:** A general REINFORCE algorithm aims at optimizing the parameter θ of a policy πθ to maximize the score function of the expected return Gt = ...
- **p. 4 / 3.3. Stochastic Gradient Reversion - extractive PDF cue:** Utilizing the modified gradient, the parameter update at the nth iteration becomes: θn+1 ←θn + η∇J(θ)′, (6) where η > 0 is the learning rate.
- **p. 4 / 3.3. Stochastic Gradient Reversion - extractive PDF cue:** Therefore, we propose Stochastic Gradient Reversion (SGR), a gradient regularization method for FEEDTTA to maintain plasticity and stability during adaptation.
- **p. 5 / 3.3. Stochastic Gradient Reversion - extractive PDF cue:** In a standard gradient update, the EAV is given by: X E[/∇θJ(θ)/] = X /gθ/.
- **p. 5 / 3.3. Stochastic Gradient Reversion - extractive PDF cue:** While GD can bring robustness in the learning process to some extent, disregarding the updates in certain dimensions as a whole causes loss of plasticity ...
- **p. 3 / 3.2. Binary Episodic Feedback - extractive PDF cue:** (2) Then, according to the policy gradient theorem, the approxi3
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (3.3. Stochastic Gradient Reversion), p. 5 (3.3. Stochastic Gradient Reversion), p. 5 (3.3. Stochastic Gradient Reversion), p. 3 (3.2. Binary Episodic Feedback), p. 3 (3.2. Binary Episodic Feedback), p. 4 (3.2. Binary Episodic Feedback).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Right, Specifically, among, variants, negative, value, reversion, shifts, original, gradient, closest, counterfactual, distribution, mated | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Right, Specifically, among, variants, negative, value, reversion, shifts, original, gradient | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summary, contributions, follows, introduce, FEEDTTA, novel, TTA, framework, online, VLN | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | general, REINFORCE, algorithm, aims, optimizing, parameter, policy, maximize, score, function | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Binary Episodic Feedback - extractive PDF cue:** (Right) Specifically, among the variants of α, the negative value (reversion) shifts the original gradient closest to the counterfactual distribution. mated gradient of the policy ...
- **p. 3 / 3.1. Task Description - extractive PDF cue:** Each element Xn consists of a natural language instruction In, and an initial visual state s0 n, which is a 360◦panoramic view of the surrounding ...
- **p. 3 / 3.2. Binary Episodic Feedback - extractive PDF cue:** FEEDTTA leverages a Monte Carlo policy gradient algorithm REINFORCE (Williams, 1992) to learn from the received feedback at the end of each navigation episode.
- **p. 4 / 3.2. Binary Episodic Feedback - extractive PDF cue:** Although episodic feedback is an inexpensive interaction, human involvement may not always be possible in real-world environments.
- **p. 2 / 1. Introduction - extractive PDF cue:** Regardless of the feedback oracle, we show that the policy adaptation is possible, even with a small amount of streaming test data.
- **p. 2 / 1. Introduction - extractive PDF cue:** Specifically, this work studies a highly practical setting of binary episodic feedback, where after each episode, the oracle provides the agent with a binary scalar ...
- **p. 5 / 3.3. Stochastic Gradient Reversion - extractive PDF cue:** TTA for Online VLN with Feedback-based Reinforcement Learning J(θ)F=-1).
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | (1) Unlike step-wise feedback which requires tracking throughout the whole episode, it is trivial to simply evaluate whether the complete trajectory was ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | To accomplish the given instruction, the agent starts from s0 and predicts next action at each time step using πθ, until it ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Lastly, we compare the average inference time per 4 episodes. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Stochastic Gradient Reversion - extractive PDF cue:** TTA for Online VLN with Feedback-based Reinforcement Learning J(θ)F=-1).
- **p. 5 / 4.3. Implementation Details - extractive PDF cue:** Our proposed FEEDTTA is applied at the inference time of these offline trained VLN policies.
- **p. 6 / 5.1. Main Navigation Results - extractive PDF cue:** Lastly, we compare the average inference time per 4 episodes.
- **p. 6 / 4.3. Implementation Details - extractive PDF cue:** We use a batch size of 1 to properly simulate the online environment.
- **p. 9 / 5.5. Comparison with Different Feedback Strategies - extractive PDF cue:** The rationale behind choosing a simple binary episodic feedback mechanism stems from the practical limitations of the online test-time navigation environment: (1) Human involvement should ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** element, consists, natural, language, instruction, initial, visual, state, panoramic, view, surrounding, environment, FEEDTTA, leverages, Monte, Carlo, policy, gradient, algorithm, REINFORCE.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | For the REVERIE dataset, the results in the paper are obtained with p = 0.01 and α = -0.2 for the validation ... | p. 6 (4.3. Implementation Details), p. 9 (5.4. Effects of Stochastic Gradient Reversion) |
| Global / local decision | For the test unseen split, we utilize LLMs as the feedback oracle due to the unavailability of goal-viewpoint data, yet the results ... | p. 6 (5.1. Main Navigation Results), p. 6 (5.1. Main Navigation Results) |
| Motion execution / recovery | Furthermore, while GD and GS exhibit catastrophic forgetting, the proposed SGR rather brings substantial improvements in the success rates, strengthening the policy's ... | p. 9 (5.4. Effects of Stochastic Gradient Reversion), p. 5 (4.2. Evaluation Metrics) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. Effects of different gradient regularization variants on α. FEEDTTA w/o reg. denotes a variant of FEEDTTA without any regularization techniques applied. Methods TL ...
- **p. 5 / 4.1. Dataset Description - extractive PDF cue:** R2R-CE is a variant of R2R in a continuous environment.
- **p. 7 / 5.2. Quality and Quantity of Feedback - extractive PDF cue:** Another strategy to measure sensitivity on feedback quantity is to modify update intervals.
- **p. 7 / 5.2. Quality and Quantity of Feedback - extractive PDF cue:** The following experiments address RQ2 by studying the sensitivity of FEEDTTA on the quality (e.g., based on accuracy) and the quantity (e.g., based on first ...
- **p. 8 / 5.4. Effects of Stochastic Gradient Reversion - extractive PDF cue:** This corresponds to the changes in weight magnitude, where the two variants exhibits the largest scale.
- **p. 9 / 5.4. Effects of Stochastic Gradient Reversion - extractive PDF cue:** First, our FEEDTTA, without gradient regularization, enhances the OSR, SR and RGS metric after adaptation on the validation unseen dataset.
- **p. 9 / 5.5. Comparison with Different Feedback Strategies - extractive PDF cue:** As we observe from Table 7, our binary episodic feedback surpasses the distance-based dense reward system, even without access to ground-truth information.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.1. Task Description), p. 3 (3.2. Binary Episodic Feedback), p. 4 (3.2. Binary Episodic Feedback), p. 4 (3.2. Binary Episodic Feedback), p. 5 (3.3. Stochastic Gradient Reversion), p. 5 (3.3. Stochastic Gradient Reversion), objective p. 3 (3.2. Binary Episodic Feedback), p. 4 (3.3. Stochastic Gradient Reversion), p. 4 (3.3. Stochastic Gradient Reversion), p. 5 (3.3. Stochastic Gradient Reversion), p. 5 (3.3. Stochastic Gradient Reversion), p. 3 (3.2. Binary Episodic Feedback), temporal p. 3 (3.2. Binary Episodic Feedback), p. 3 (3.1. Task Description), p. 8 (5.3. LLMs as Feedback Oracle), p. 9 (5.5. Comparison with Different Feedback Strategies), p. 1 (Abstract), p. 6 (5.1. Main Navigation Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
