# Method - Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p125.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p125.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (B. Whole-body Controller Pre-training), p. 5 (A. Comparing System Identification Approaches), p. 3 (B. Whole-body Controller Pre-training), p. 5 (A. Comparing System Identification Approaches), p. 6 (A. Comparing System Identification Approaches), p. 4 (B. Whole-body Controller Pre-training)): 2) Observation Space: ‘The policy's observation space consists of proprioceptive readings from the robot's onboard sen= sors including the gravity vector projected in the robot's body frame g, a base ...

## Method Body Digest

- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** 2) Observation Space: ‘The policy's observation space consists of proprioceptive readings from the robot's onboard sen= sors including the gravity vector projected in the robot's ...
- **p. 5 / A. Comparing System Identification Approaches - extractive body cue:** We first evaluate the modeling accuracy of these approaches by reporting the mean-square joint position error on both the training data and on an unseen ...
- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** 1) Policy Architecture: "The WBC is a control policy, a, = ro(Or-yc4)e Where the action at time f, ay, is a vector of position targets ...
- **p. 5 / A. Comparing System Identification Approaches - extractive body cue:** We compare several methods for modeling the actuator dynamics of the Unitree Z1 Pro arm in Isaac Sim.
- **p. 6 / A. Comparing System Identification Approaches - extractive body cue:** However, only UAN achieves a tight fit to the training data, thanks to its capacity to model the nonlinear effects introduced by the harmonic reducers.
- **p. 4 / B. Whole-body Controller Pre-training - extractive body cue:** 6) Command Sampling Scheme: We adopt the approach first proposed in [7] to sample commands during training.
- **p. 6 / A. Comparing System Identification Approaches - extractive body cue:** In contrast, the UAN policy achieved the farthest throws on hardware with the smallest sim-to-real gap.
- **p. 4 / B. Whole-body Controller Pre-training - extractive body cue:** The EE tracking term rewards ‘minimizing the distance between four key points, where one key point is positioned at the frame's origin, and the others ...

## Design Rationale

- **p. 2 / 1. Iyrropucrion - extractive body cue:** Rather than enforcing strict adherence to a reference trajectory, we propose treating it as a hint to guide exploration, In our approach, « WBC is ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** First, we introduce the Un= supervised Actuator Net (UAN), which leverages real-world data {o bridge the sim-to-real gap for complex actuation mechanisms without requiring access ...
- **p. 2 / A. Unsupervised Actuator Net - extractive body cue:** Alternatively, we propose a method for matching the transition dynamics of the actuator such that

## Source Evidence Cues

- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** 2) Observation Space: ‘The policy's observation space consists of proprioceptive readings from the robot's onboard sen= sors including the gravity vector projected in the robot's ...
- **p. 5 / A. Comparing System Identification Approaches - extractive body cue:** We first evaluate the modeling accuracy of these approaches by reporting the mean-square joint position error on both the training data and on an unseen ...
- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** 1) Policy Architecture: "The WBC is a control policy, a, = ro(Or-yc4)e Where the action at time f, ay, is a vector of position targets ...
- **p. 5 / A. Comparing System Identification Approaches - extractive body cue:** We compare several methods for modeling the actuator dynamics of the Unitree Z1 Pro arm in Isaac Sim.
- **p. 6 / A. Comparing System Identification Approaches - extractive body cue:** However, only UAN achieves a tight fit to the training data, thanks to its capacity to model the nonlinear effects introduced by the harmonic reducers.
- **p. 4 / B. Whole-body Controller Pre-training - extractive body cue:** 6) Command Sampling Scheme: We adopt the approach first proposed in [7] to sample commands during training.
- **p. 6 / A. Comparing System Identification Approaches - extractive body cue:** In contrast, the UAN policy achieved the farthest throws on hardware with the smallest sim-to-real gap.
- **Detected method headings:** B. Whole-body Controller Pre-training (p. 3); 3) Does our approach enable simt-to-real transfer of athletic (p. 5); A. Comparing System Identification Approaches (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | 2) Observation Space: ‘The policy's observation space consists of proprioceptive readings from the robot's onboard sen= sors including the gravity vector projected ... | p. 3 (B. Whole-body Controller Pre-training), p. 5 (A. Comparing System Identification Approaches) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | We first evaluate the modeling accuracy of these approaches by reporting the mean-square joint position error on both the training data and ... | p. 5 (A. Comparing System Identification Approaches), p. 3 (B. Whole-body Controller Pre-training) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | 1) Policy Architecture: "The WBC is a control policy, a, = ro(Or-yc4)e Where the action at time f, ay, is a vector ... | p. 3 (B. Whole-body Controller Pre-training), p. 5 (A. Comparing System Identification Approaches) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / B. Whole-body Controller Pre-training - extractive body cue:** The EE tracking term rewards ‘minimizing the distance between four key points, where one key point is positioned at the frame's origin, and the others ...
- **p. 4 / B. Whole-body Controller Pre-training - extractive body cue:** Furthermore, we clip the arm torques a second time to satisfy the constraint
- **p. 5 / A. Comparing System Identification Approaches - extractive body cue:** 5) CEM: A method in which friction, frictional damping, ‘and armature parameters are optimized using the crossentropy method to minimize the mean-square joint position error ...
- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** The value function approximator network has the same architecture but does not share weights with the policy.
- **p. 5 / A. Comparing System Identification Approaches - extractive body cue:** 3) ROA: A domain randomization baseline enhanced with ‘an online system identification module via Regularized Online Adaptation [7]
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 4 (B. Whole-body Controller Pre-training), p. 4 (B. Whole-body Controller Pre-training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Observation, Space, policy, consists, proprioceptive, readings, robot, onboard, sors, including, gravity, vector, projected, body | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | Observation, Space, policy, consists, proprioceptive, readings, robot, onboard, sors, including | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | Rather, enforcing, strict, adherence, reference, trajectory, treating, hint, guide, exploration | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | tracking, term, rewards, minimizing, distance, between, four, points, where, point | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** 2) Observation Space: ‘The policy's observation space consists of proprioceptive readings from the robot's onboard sen= sors including the gravity vector projected in the robot's ...
- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** 1) Policy Architecture: "The WBC is a control policy, a, = ro(Or-yc4)e Where the action at time f, ay, is a vector of position targets ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** policy can track reference trajectories if provided as a sequence fof base velocity and end effector pose commands.
- **p. 4 / B. Whole-body Controller Pre-training - extractive body cue:** This clipping strategy enforces a physical motor constraint by ensuring that torque commands ‘do not demand power beyond the motor's maximum output, capacity.
- **p. 4 / B. Whole-body Controller Pre-training - extractive body cue:** To encourage learning recovery behaviors, we randomize the initial joint and body states of the robot and periodically perturb it with external forces and torques ...
- **p. 2 / A. Unsupervised Actuator Net - extractive body cue:** We Fearn a residual model, xyan(e). that observes a history of position and velocity errors, e, and outputs a corrective torque, 57, for the simulator ...
- **p. 6 / A. Comparing System Identification Approaches - extractive body cue:** As shown by Figure 6, UAN can even accurately capture the arm's response to Gaussian noise control input, which is commonly used for exploration in ...
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | Each training episode consists of a 20s rollout executing the torque sequence from the hardware data from 3, t0 8744.20 Through taining ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | 1) Policy Architecture: "The WBC is a control policy, a, = ro(Or-yc4)e Where the action at time f, ay, is a vector ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | 1) Policy Architecture: "The WBC is a control policy, a, = ro(Or-yc4)e Where the action at time f, ay, is a vector ... | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | Each training episode consists of a 20s rollout executing the torque sequence from the hardware data from 3, t0 8744.20 Through taining ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** 2) Observation Space: ‘The policy's observation space consists of proprioceptive readings from the robot's onboard sen= sors including the gravity vector projected in the robot's ...
- **p. 5 / A. Comparing System Identification Approaches - extractive body cue:** We first evaluate the modeling accuracy of these approaches by reporting the mean-square joint position error on both the training data and on an unseen ...
- **p. 6 / A. Comparing System Identification Approaches - extractive body cue:** However, only UAN achieves a tight fit to the training data, thanks to its capacity to model the nonlinear effects introduced by the harmonic reducers.
- **p. 4 / B. Whole-body Controller Pre-training - extractive body cue:** 6) Command Sampling Scheme: We adopt the approach first proposed in [7] to sample commands during training.
- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** ining scheme buikls upon the method proposed in {7] by incorporating a strategy for learning to track an EE orientation command, As in Section -A3, ...
- **p. 4 / C. Task-Specific Finetuning - extractive body cue:** To avoid policy collapse, we set a low initial learning rate (1 x 10~®) for the actor and retain the standard deviation from pre-training.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Observation, Space, policy, consists, proprioceptive, readings, robot, onboard, sors, including, gravity, vector, projected, body, frame, base, velocity, command, effector, pose.
- **Relevant PDF headings:** B. Whole-body Controller Pre-training (p. 3); 3) Does our approach enable simt-to-real transfer of athletic (p. 5); A. Comparing System Identification Approaches (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | On hardware, the ball was thrown approximately 20m, with the real robot throwing slightly further than in simulation - possibly due to ... | p. 6 (B. Finetuning Foundational WBC), p. 3 (A. Unsupervised Actuator Net) |
| Whole-body policy / controller | Fig. 4: UAN improves simulator accuracy and real throwing performance. UAN (Ours) achieves lower sim-to-real difference in throw distance as compared to ... | p. 5 (Figure/Table caption), p. 5 (A. Comparing System Identification Approaches) |
| Adaptation / recovery | Fig. 4: UAN improves simulator accuracy and real throwing performance. UAN (Ours) achieves lower sim-to-real difference in throw distance as compared to ... | p. 5 (Figure/Table caption), p. 5 (A. Comparing System Identification Approaches) |

## Failure and Ablation Link

- **p. 5 / A. Arm Modifications - extractive body cue:** In this section, we report ablations that identify the contribution of key system components and present results for the athletic tasks.
- **p. 5 / C. Task-Specific Finetuning - extractive body cue:** Following our UAN training (Section II-A), we pre-trained a WBC (Section II-B) and then fine-tuned policies for each task (Section II-C), Ablations comparing our method ...
- **p. 8 / B. Overcoming the sim-to-real gap - extractive body cue:** Some policy architectures (i.e., CNNs [22] and transformers [35]) have been shown to achieve in-context adaptation without relying on a teacher-student distillation.
- **p. 8 / B. Overcoming the sim-to-real gap - extractive body cue:** In contrast, our approach, UAN, employs an actuator net without relying on torque data, Instead, we train the network to predict corrective torques for the ...
- **p. 3 / A. Unsupervised Actuator Net - extractive body cue:** Train UAN 2.Pre-train / Fine-tune WBC 3.
- **p. 3 / A. Unsupervised Actuator Net - extractive body cue:** and EE pose), then and fine-tune it on an athlet
- **p. 4 / C. Task-Specific Finetuning - extractive body cue:** To address this, we fine-tune the policy directly with task rewards.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (B. Whole-body Controller Pre-training), p. 5 (A. Comparing System Identification Approaches), p. 3 (B. Whole-body Controller Pre-training), p. 5 (A. Comparing System Identification Approaches), p. 6 (A. Comparing System Identification Approaches), p. 4 (B. Whole-body Controller Pre-training), objective p. 4 (B. Whole-body Controller Pre-training), p. 4 (B. Whole-body Controller Pre-training), p. 5 (A. Comparing System Identification Approaches), p. 3 (B. Whole-body Controller Pre-training), p. 5 (A. Comparing System Identification Approaches), temporal p. 3 (A. Unsupervised Actuator Net), p. 3 (B. Whole-body Controller Pre-training), p. 2 (A. Unsupervised Actuator Net), p. 8 (B. Overcoming the sim-to-real gap), p. 2 (1. Iyrropucrion), p. 4 (B. Whole-body Controller Pre-training).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
