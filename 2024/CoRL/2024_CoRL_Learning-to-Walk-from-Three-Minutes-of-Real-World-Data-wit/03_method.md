# Method - Learning to Walk from Three Minutes of Real-World Data with Semi-structured Dynamics Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=evCXwlCMIi; PDF retrieval source: https://arxiv.org/pdf/2410.09163. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 14 (A.3 Control Architecture), p. 14 (A.3 Control Architecture), p. 13 (A.1 Observation and Action Spaces), p. 13 (A Implementation Details)): The desired joint angles are sent to the joint level PD controllers, where the desired torque outputs are: τt = Kp(qdes -qj) -Kp ˙qj, (11) and we use proportional gain ...

## Method Body Digest

- **p. 14 / A.3 Control Architecture - extractive PDF cue:** The desired joint angles are sent to the joint level PD controllers, where the desired torque outputs are: τt = Kp(qdes -qj) -Kp ˙qj, (11) ...
- **p. 14 / A.3 Control Architecture - extractive PDF cue:** Referring to the action space definition Table 2, the policy takes in the current observation and a history of observations and outputs offsets to foot ...
- **p. 13 / A.1 Observation and Action Spaces - extractive PDF cue:** The observation space Ω⊂R36 consists of the elements in Table 1.
- **p. 13 / A Implementation Details - extractive PDF cue:** In this appendix, we provide details of our implementation for the Unitree Go1 Quadruped, including the observation and action spaces, the reward function, the termination ...
- **p. 14 / A.2 Reward Function and Termination Condition - extractive PDF cue:** Reward Term Expression Weight Maximize forward velocity vx t+1 0.42 Limit base yaw rate exp  -(ωz t+1)2/0.2  0.11 Limit base roll exp  ...
- **p. 13 / A.2 Reward Function and Termination Condition - extractive PDF cue:** The reward function is a weighted sum of the terms in Table 3.
- **p. 14 / A.2 Reward Function and Termination Condition - extractive PDF cue:** The reward at each time step is a weighted sum of these terms.
- **p. 5 / 1 Introduction - extractive PDF cue:** Algorithm 1 Auto-Regressive State Predictions 1: Inputs hallucination buffer Dmodel, models {ˆpi ψi}, policy πθ, start state s0, start history h0 2: for t = ...

## Design Rationale

- **p. 6 / 1 Introduction - extractive PDF cue:** This, when combined with the accuracy of our predictions over long-horizons (Section 4.2) provides insight into why our approach enables such effective policy optimization [38].
- **p. 3 / 1 Introduction - extractive PDF cue:** The space of observations Ωconsists of the states that can be measured, and the observation distribution O(·/st, at, et) provides (noisy) estimates of the states ...
- **p. 4 / 1 Introduction - extractive PDF cue:** 3 Semi-structured Reinforcement Learning A high-level overview of our method is presented in Fig.

## Source Evidence Cues

- **p. 14 / A.3 Control Architecture - extractive PDF cue:** The desired joint angles are sent to the joint level PD controllers, where the desired torque outputs are: τt = Kp(qdes -qj) -Kp ˙qj, (11) ...
- **p. 14 / A.3 Control Architecture - extractive PDF cue:** Referring to the action space definition Table 2, the policy takes in the current observation and a history of observations and outputs offsets to foot ...
- **p. 13 / A.1 Observation and Action Spaces - extractive PDF cue:** The observation space Ω⊂R36 consists of the elements in Table 1.
- **p. 13 / A Implementation Details - extractive PDF cue:** In this appendix, we provide details of our implementation for the Unitree Go1 Quadruped, including the observation and action spaces, the reward function, the termination ...
- **Detected method headings:** A.3 Control Architecture (p. 14); B.2 Model Rollout Accuracy (p. 15); B.4 Modeling Uncertainty (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | The desired joint angles are sent to the joint level PD controllers, where the desired torque outputs are: τt = Kp(qdes -qj) ... | p. 14 (A.3 Control Architecture), p. 14 (A.3 Control Architecture) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | Referring to the action space definition Table 2, the policy takes in the current observation and a history of observations and outputs ... | p. 14 (A.3 Control Architecture), p. 13 (A.1 Observation and Action Spaces) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | The observation space Ω⊂R36 consists of the elements in Table 1. | p. 13 (A.1 Observation and Action Spaces), p. 13 (A Implementation Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 14 / A.2 Reward Function and Termination Condition - extractive PDF cue:** Reward Term Expression Weight Maximize forward velocity vx t+1 0.42 Limit base yaw rate exp  -(ωz t+1)2/0.2  0.11 Limit base roll exp  ...
- **p. 13 / A.2 Reward Function and Termination Condition - extractive PDF cue:** The reward function is a weighted sum of the terms in Table 3.
- **p. 13 / A Implementation Details - extractive PDF cue:** In this appendix, we provide details of our implementation for the Unitree Go1 Quadruped, including the observation and action spaces, the reward function, the termination ...
- **p. 14 / A.2 Reward Function and Termination Condition - extractive PDF cue:** The reward at each time step is a weighted sum of these terms.
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 13 (A.2 Reward Function and Termination Condition), p. 14 (A.2 Reward Function and Termination Condition), p. 13 (A.1 Observation and Action Spaces).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Algorithm, Auto-Regressive, State, Predictions, Inputs, hallucination, buffer, Dmodel, models, policy, start, history, Sample, action | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | Algorithm, Auto-Regressive, State, Predictions, Inputs, hallucination, buffer, Dmodel, models, policy | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | when, combined, accuracy, predictions, over, long-horizons, Section, provides, insight, enables | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | Reward, Term, Expression, Weight, Maximize, forward, velocity, Limit, base, rate | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 1 Introduction - extractive PDF cue:** Algorithm 1 Auto-Regressive State Predictions 1: Inputs hallucination buffer Dmodel, models {ˆpi ψi}, policy πθ, start state s0, start history h0 2: for t = ...
- **p. 14 / A.3 Control Architecture - extractive PDF cue:** Referring to the action space definition Table 2, the policy takes in the current observation and a history of observations and outputs offsets to foot ...
- **p. 3 / 1 Introduction - extractive PDF cue:** We optimize a neural network policy πθ(·/st, ht) conditioned on previous observations which outputs (i) changes to parameters of a nominal gait generator that outputs ...
- **p. 4 / 1 Introduction - extractive PDF cue:** Given a state st and state history ht, to generate a synthetic rollout we: (i) sample an action from the policy, (ii) randomly choose a ...
- **p. 5 / 1 Introduction - extractive PDF cue:** Steps in the real environment are taken using a deterministic policy µθ which simply outputs the mean action from the stochastic policy πθ.
- **p. 4 / 1 Introduction - extractive PDF cue:** First, we let τt = G(st, at) denote a zeroorder hold estimate for the low-level motor torques applied to the robot; here, G is a ...
- **p. 3 / 1 Introduction - extractive PDF cue:** The space of observations Ωconsists of the states that can be measured, and the observation distribution O(·/st, at, et) provides (noisy) estimates of the states ...
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | We use an observation history length of h = 5, a multi-step loss horizon of H = 4, and hallucinate synthetic rollouts ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | We set the weights and use exponentials in most of the terms to normalize the reward such that a forward velocity of ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | We use an observation history length of h = 5, a multi-step loss horizon of H = 4, and hallucinate synthetic rollouts ... | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | We use an observation history length of h = 5, a multi-step loss horizon of H = 4, and hallucinate synthetic rollouts ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** desired, joint, angles, sent, level, controllers, where, torque, outputs, qdes, proportional, gain, rad-1, derivative, Referring, action, space, definition, Table, policy.
- **Relevant PDF headings:** A.3 Control Architecture (p. 14); B.2 Model Rollout Accuracy (p. 15); B.4 Modeling Uncertainty (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from ... | p. 16 (Figure/Table caption), p. 18 (Figure/Table caption) |
| Whole-body policy / controller | Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an ... | p. 7 (Figure/Table caption), p. 2 (Figure/Table caption) |
| Adaptation / recovery | Figure 12: Simulated benchmark results. Better performance is achieved when using our semi- structured dynamics models and a multi-step loss. Plots show ... | p. 18 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 17 / Figure/Table caption - extractive PDF cue:** Figure 9: Training performance when removing the noise estimators and removing both the noise estimators and ensemble. B.5 Additional Simulated Terrain Experiments To further demonstrate ...
- **p. 8 / 5 Related Work - extractive PDF cue:** However there are several key limitations.
- **p. 8 / 5 Related Work - extractive PDF cue:** 6 Limitations This paper presents a novel framework for model-based reinforcement learning, which leverages physics-informed, semi-structured dynamics models to enable highly sample-efficient policy learning in ...
- **p. 14 / A.2 Reward Function and Termination Condition - extractive PDF cue:** The termination flag dt stops the accumulation of reward after the quadruped falls and is defined by: dt = 1 if /φx t / > ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 8: Our approach is robust to errors in a priori knowledge of the robot's inertial properties. B.4 Modeling Uncertainty Here, we examine the benefit ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: The SSRL framework. A deterministic policy is used to collect data from the real world while a stochastic policy is utilized in conjunction ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- or ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 14 (A.3 Control Architecture), p. 14 (A.3 Control Architecture), p. 13 (A.1 Observation and Action Spaces), p. 13 (A Implementation Details), objective p. 14 (A.2 Reward Function and Termination Condition), p. 13 (A.2 Reward Function and Termination Condition), p. 13 (A Implementation Details), p. 14 (A.2 Reward Function and Termination Condition), temporal p. 6 (1 Introduction), p. 13 (A.2 Reward Function and Termination Condition), p. 14 (A.2 Reward Function and Termination Condition), p. 4 (1 Introduction), p. 6 (1 Introduction), p. 3 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
