# Method - HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10011640; PDF retrieval source: https://arxiv.org/pdf/2503.00923. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 15 (A.2 Implementation Details), p. 15 (A.2 Implementation Details), p. 17 (A.2 Implementation Details), p. 16 (A.2 Implementation Details), p. 16 (A.2 Implementation Details), p. 17 (A.2 Implementation Details)): Action Space: The policy outputs continuous actions at ∈Rn, which are utilized as target positions for a PD controller to compute joint torques.

## Method Body Digest

- **p. 15 / A.2 Implementation Details - extractive body cue:** Action Space: The policy outputs continuous actions at ∈Rn, which are utilized as target positions for a PD controller to compute joint torques.
- **p. 15 / A.2 Implementation Details - extractive body cue:** The training terrain consists of various types, including flat planes, rough surfaces, steps, and slopes.
- **p. 17 / A.2 Implementation Details - extractive body cue:** To further promote stable posture restoration and enable smooth transitions back to the goal-tracking policy, we introduce an additional stand reward, defined as: rstand = ...
- **p. 16 / A.2 Implementation Details - extractive body cue:** During training, two trained low-level policies are loaded and rolled out to generate training data for optimizing the high-level policy.
- **p. 16 / A.2 Implementation Details - extractive body cue:** For the High-level policy, the input is the same set of observations as used by the low-level policies, with the output being a two-dimensional Q-value.
- **p. 17 / A.2 Implementation Details - extractive body cue:** However, they may hinder reward acquisition during the initial stages of training.
- **p. 17 / A.2 Implementation Details - extractive body cue:** As a result, this reward term serves as a back-tracking reward for the safety recovery mechanism, encouraging it to return to a stable goal-tracking state.
- **p. 16 / A.2 Implementation Details - extractive body cue:** The objective is to enable the robot to track goal commands across a variety of terrains.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** To develop a reliable locomotion policy capable of generalizing from the training to the deployment environment, we propose formulating policy optimization as a robust optimization ...
- **p. 2 / 1 Introduction - extractive body cue:** To address this limitation, we propose a high-level planning policy that dynamically selects which policy to activate based on the scenario.
- **p. 15 / A.2 Implementation Details - extractive body cue:** To address this, we introduce a terrain curriculum method [63].

## Source Evidence Cues

- **p. 15 / A.2 Implementation Details - extractive body cue:** Action Space: The policy outputs continuous actions at ∈Rn, which are utilized as target positions for a PD controller to compute joint torques.
- **p. 15 / A.2 Implementation Details - extractive body cue:** The training terrain consists of various types, including flat planes, rough surfaces, steps, and slopes.
- **p. 17 / A.2 Implementation Details - extractive body cue:** To further promote stable posture restoration and enable smooth transitions back to the goal-tracking policy, we introduce an additional stand reward, defined as: rstand = ...
- **p. 16 / A.2 Implementation Details - extractive body cue:** During training, two trained low-level policies are loaded and rolled out to generate training data for optimizing the high-level policy.
- **p. 16 / A.2 Implementation Details - extractive body cue:** For the High-level policy, the input is the same set of observations as used by the low-level policies, with the output being a two-dimensional Q-value.
- **p. 17 / A.2 Implementation Details - extractive body cue:** However, they may hinder reward acquisition during the initial stages of training.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | Action Space: The policy outputs continuous actions at ∈Rn, which are utilized as target positions for a PD controller to compute joint ... | p. 15 (A.2 Implementation Details), p. 15 (A.2 Implementation Details) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | The training terrain consists of various types, including flat planes, rough surfaces, steps, and slopes. | p. 15 (A.2 Implementation Details), p. 17 (A.2 Implementation Details) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | To further promote stable posture restoration and enable smooth transitions back to the goal-tracking policy, we introduce an additional stand reward, defined ... | p. 17 (A.2 Implementation Details), p. 16 (A.2 Implementation Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 17 / A.2 Implementation Details - extractive body cue:** As a result, this reward term serves as a back-tracking reward for the safety recovery mechanism, encouraging it to return to a stable goal-tracking state.
- **p. 16 / A.2 Implementation Details - extractive body cue:** The objective is to enable the robot to track goal commands across a variety of terrains.
- **p. 16 / A.2 Implementation Details - extractive body cue:** From left to right, the terrains are flats, obstacles, slopes, and stairs Learning for Policy Transition: High-level planning policy is utilized to switch between low-level ...
- **p. 17 / A.2 Implementation Details - extractive body cue:** However, they may hinder reward acquisition during the initial stages of training.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 16 (A.2 Implementation Details), p. 16 (A.2 Implementation Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | High-level, policy, input, same, observations, low-level, policies, output, being, two-dimensional, Q-value, Action, Space, outputs | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | High-level, policy, input, same, observations, low-level, policies, output, being, two-dimensional | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | develop, reliable, locomotion, policy, capable, generalizing, training, deployment, environment, formulating | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | result, reward, term, serves, back-tracking, safety, recovery, mechanism, encouraging, return | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 16 / A.2 Implementation Details - extractive body cue:** For the High-level policy, the input is the same set of observations as used by the low-level policies, with the output being a two-dimensional Q-value.
- **p. 15 / A.2 Implementation Details - extractive body cue:** Action Space: The policy outputs continuous actions at ∈Rn, which are utilized as target positions for a PD controller to compute joint torques.
- **p. 15 / A.2 Implementation Details - extractive body cue:** Proprioception: For the Unitree H1, proprioception op t ∈R65, which denotes the internal state of the robot, including the base angular velocity wt ∈R3, base ...
- **p. 2 / 1 Introduction - extractive body cue:** The goal-tracking policy is designed to follow task-specific commands (e.g., moving velocity).
- **p. 17 / A.2 Implementation Details - extractive body cue:** To further promote stable posture restoration and enable smooth transitions back to the goal-tracking policy, we introduce an additional stand reward, defined as: rstand = ...
- **p. 1 / 1 Introduction - extractive body cue:** To develop an end-to-end solution with promising generalizability, recent studies [11-15] adopted Reinforcement Learning (RL) methods by training a neural model to control based on ...
- **p. 2 / 1 Introduction - extractive body cue:** To address this limitation, we propose a high-level planning policy that dynamically selects which policy to activate based on the scenario.
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | Under these general locomotion settings, we design three types of disturbances as follows: 1) External force/torque disturbances, where random forces and torques ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | As the velocity increases, both stride length and step frequency adjust dynamically, mimicking typical human locomotion. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | Under these general locomotion settings, we design three types of disturbances as follows: 1) External force/torque disturbances, where random forces and torques ... | hardware, batch and throughput |

## Training vs Inference

- **p. 15 / A.2 Implementation Details - extractive body cue:** The training terrain consists of various types, including flat planes, rough surfaces, steps, and slopes.
- **p. 16 / A.2 Implementation Details - extractive body cue:** During training, two trained low-level policies are loaded and rolled out to generate training data for optimizing the high-level policy.
- **p. 17 / A.2 Implementation Details - extractive body cue:** However, they may hinder reward acquisition during the initial stages of training.
- **p. 7 / 5 Experiment - extractive body cue:** All policies are trained using three random seeds and evaluated in 1000 distinct environments.
- **p. 15 / A.2 Implementation Details - extractive body cue:** The training terrain consists of various types, including flat planes, rough surfaces, steps, and slopes.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Action, Space, policy, outputs, continuous, actions, utilized, target, positions, controller, compute, joint, torques, training, terrain, consists, various, types, including, flat.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | Second, the humanoid robot used in real-world deployment has only 19 degrees of freedom, which limits whole-body coordination and constrains the expression ... | p. 9 (5 Experiment), p. 7 (5 Experiment) |
| Balance-aware whole-body execution | HWC-Loco reaches a success rate of 81.27%, outperforming all baselines by a significant margin. | p. 8 (5 Experiment), p. 9 (5 Experiment) |
| Recovery / adaptation | Figure 9: Extreme State: Policy's state distribution in the extreme cases A.8 History Length Experiments We investigate the impact of observation history ... | p. 20 (Figure/Table caption), p. 8 (5 Experiment) |

## Failure and Ablation Link

- **p. 7 / 5 Experiment - extractive body cue:** To evaluate the effectiveness of different components in HWC-Loco, we design a comparison method using an ablation approach as follows: 1) HWC-Loco-l sets α to ...
- **p. 7 / 5 Experiment - extractive body cue:** 3) DreamWaQ-Humanoid further removes the human imitation objective Df from objective (5), effectively reducing our method to an adaptation of DreamWaQ [18] for humanoid control.
- **p. 8 / 5 Experiment - extractive body cue:** Comparably, when downplaying the sensitivity to safety-critical events and removing the safety-recovery policy, the success data drops significantly from nearly 85% to around 60% in ...
- **p. 15 / A.2 Implementation Details - extractive body cue:** The projected gravity refers to the component of gravity expressed in the robot's local coordinate system.
- **p. 7 / 5 Experiment - extractive body cue:** To evaluate the effectiveness of different components in HWC-Loco, we design a comparison method using an ablation approach as follows: 1) HWC-Loco-l sets α to ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 10: Climb Stairs Test. The blue segments indicate the activation of the goal-tracking policy, while the orange segments correspond to the safety recovery policy. ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 13: Robustness in Outdoor Settings: The robot responds to external disturbances in an outdoor environment by waving its arms and adjusting its gaits to ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 15 (A.2 Implementation Details), p. 15 (A.2 Implementation Details), p. 17 (A.2 Implementation Details), p. 16 (A.2 Implementation Details), p. 16 (A.2 Implementation Details), p. 17 (A.2 Implementation Details), objective p. 17 (A.2 Implementation Details), p. 16 (A.2 Implementation Details), p. 16 (A.2 Implementation Details), p. 17 (A.2 Implementation Details), temporal p. 8 (5 Experiment), p. 9 (5 Experiment), p. 9 (5 Experiment), p. 3 (2 Related Work), p. 8 (5 Experiment), p. 15 (A.2 Implementation Details).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
