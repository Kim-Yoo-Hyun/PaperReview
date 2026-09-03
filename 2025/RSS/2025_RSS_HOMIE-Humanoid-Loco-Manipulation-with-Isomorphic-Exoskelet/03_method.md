# Method - HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p070.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p070.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 8 (A. Humanoid Whole-body Control), p. 3 (B. Whole-body Loco-Manipulation), p. 2 (Abstract), p. 2 (Abstract), p. 4 (B. Humanoid Whole-body Control), p. 4 (A. System Overview)): Symmetry Utilization, We introduce three algorithmic variants for comparison with ours in terms of symmetry ut tion: w/ aug, which uses only symmetrical data augmentation; ‘w/ sym, which only uses ...

## Method Body Digest

- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** Symmetry Utilization, We introduce three algorithmic variants for comparison with ours in terms of symmetry ut tion: w/ aug, which uses only symmetrical data augmentation; ...
- **p. 3 / B. Whole-body Loco-Manipulation - extractive body cue:** Reinforcement Learning (RL)-based algorithms, especially those based on Proximal Policy Optimization (PPO) [32], offer a more powerful altemative.
- **p. 2 / Abstract - extractive body cue:** In responce, we introduce HOMIE, a semi-autonomous humanoid teleoperation system that integrates a RL policy for body control mapped to a pedal, an isomorphic exoskeleton ...
- **p. 2 / Abstract - extractive body cue:** Our RL-based training framework features three core techrniques: upper-body pose curriculum for dynamic balance adaptation, height-tracking reward for precise squatting, and symmetry utilization for action ...
- **p. 4 / B. Humanoid Whole-body Control - extractive body cue:** After the neural network computes ay based on Ort, We Use
- **p. 4 / A. System Overview - extractive body cue:** 2, HOMIE consists of low-level policy Toco and an exoskeleton-based hardware system.
- **p. 5 / 1 2001p - extractive body cue:** 4) Symmetry Urilization: We introduce the same trick as 50] to our training framework.
- **p. 7 / A. Humanoid Whole-body Control - extractive body cue:** Given that the symmetry loss can reach values on the order of 20 without constraints, no significant difference is observed across the three methods in ...

## Design Rationale

- **p. 4 / B. Humanoid Whole-body Control - extractive body cue:** We introduce the training settings and three key techniques of our framework in this section
- **p. 2 / Abstract - extractive body cue:** Unlike previous whole-body contro! methods that depend on motion priors derived from MoCap data [12], our framework eliminates this dependency, resulting in a more cfficient ...
- **p. 2 / Abstract - extractive body cue:** In responce, we introduce HOMIE, a semi-autonomous humanoid teleoperation system that integrates a RL policy for body control mapped to a pedal, an isomorphic exoskeleton ...

## Source Evidence Cues

- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** Symmetry Utilization, We introduce three algorithmic variants for comparison with ours in terms of symmetry ut tion: w/ aug, which uses only symmetrical data augmentation; ...
- **p. 3 / B. Whole-body Loco-Manipulation - extractive body cue:** Reinforcement Learning (RL)-based algorithms, especially those based on Proximal Policy Optimization (PPO) [32], offer a more powerful altemative.
- **p. 2 / Abstract - extractive body cue:** In responce, we introduce HOMIE, a semi-autonomous humanoid teleoperation system that integrates a RL policy for body control mapped to a pedal, an isomorphic exoskeleton ...
- **p. 2 / Abstract - extractive body cue:** Our RL-based training framework features three core techrniques: upper-body pose curriculum for dynamic balance adaptation, height-tracking reward for precise squatting, and symmetry utilization for action ...
- **p. 4 / B. Humanoid Whole-body Control - extractive body cue:** After the neural network computes ay based on Ort, We Use
- **p. 4 / A. System Overview - extractive body cue:** 2, HOMIE consists of low-level policy Toco and an exoskeleton-based hardware system.
- **p. 5 / 1 2001p - extractive body cue:** 4) Symmetry Urilization: We introduce the same trick as 50] to our training framework.
- **Detected method headings:** A. Network Architecture (p. 14)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | Symmetry Utilization, We introduce three algorithmic variants for comparison with ours in terms of symmetry ut tion: w/ aug, which uses only ... | p. 8 (A. Humanoid Whole-body Control), p. 3 (B. Whole-body Loco-Manipulation) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | Reinforcement Learning (RL)-based algorithms, especially those based on Proximal Policy Optimization (PPO) [32], offer a more powerful altemative. | p. 3 (B. Whole-body Loco-Manipulation), p. 2 (Abstract) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | In responce, we introduce HOMIE, a semi-autonomous humanoid teleoperation system that integrates a RL policy for body control mapped to a pedal, ... | p. 2 (Abstract), p. 2 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / A. Humanoid Whole-body Control - extractive body cue:** Given that the symmetry loss can reach values on the order of 20 without constraints, no significant difference is observed across the three methods in ...
- **p. 2 / Abstract - extractive body cue:** Our RL-based training framework features three core techrniques: upper-body pose curriculum for dynamic balance adaptation, height-tracking reward for precise squatting, and symmetry utilization for action ...
- **p. 5 / 1 2001p - extractive body cue:** These two losses are added to the network optimization process, thereby enforcing symmetry of the neural network.
- **p. 2 / A. Teleoperation Systems - extractive body cue:** However, due to the high cost of robotic arms, the establishment of such a system incurs significant expenses.
- **p. 3 / A. Teleoperation Systems - extractive body cue:** "Teleop System Cost (S) Arm Tracking _Dex-Hand Tracking Loco-Manip.
- **p. 3 / A. Teleoperation Systems - extractive body cue:** Another possible solution is an exoskeleton-based teleoperation system, which does not require an additional identical robot, thus the overall cost is relatively low.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 7 (A. Humanoid Whole-body Control), p. 4 (B. Humanoid Whole-body Control), p. 5 (1 2001p), p. 5 (1 2001p), p. 6 (C. Hardware System Design), p. 7 (A. Humanoid Whole-body Control).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Training, Settings, observations, step, defined, Cry, Where, command, body, angular, velocity, projection, robor, torso | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Training, Settings, observations, step, defined, Cry, Where, command, body, angular | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | introduce, training, settings, three, techniques, framework, section, Unlike, previous, whole-body | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | Given, symmetry, loss, reach, values, order, without, constraints, significant, difference | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / B. Humanoid Whole-body Control - extractive body cue:** 1) Training Settings: ‘The observations of one step are defined as O, = [Cry tes dts des de» ei], Where Cy is the command, «is ...
- **p. 4 / B. Humanoid Whole-body Control - extractive body cue:** The actions ay of the policy correspond one-to-one with the joints of the robot's lower body.
- **p. 2 / Abstract - extractive body cue:** Our RL-based training framework features three core techrniques: upper-body pose curriculum for dynamic balance adaptation, height-tracking reward for precise squatting, and symmetry utilization for action ...
- **p. 5 / C. Hardware System Design - extractive body cue:** For locomotion command acquisition, we design a foot pedal that simulates the press-and-release actions of the foot during driving, enabling control of the humanoid robot's ...
- **p. 1 / Abstract - extractive body cue:** The policy' incorporates novel des an upper-body pose curriculum, a height-trackin
- **p. 3 / B. Whole-body Loco-Manipulation - extractive body cue:** Reinforcement Learning (RL)-based algorithms, especially those based on Proximal Policy Optimization (PPO) [32], offer a more powerful altemative.
- **p. 5 / B. Humanoid Whole-body Control - extractive body cue:** Each time the policy drives the robot to track the linear velocity with a rewand function that reaches the threshold, increases by 0.05, eventually reaching ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | 1) Training Settings: ‘The observations of one step are defined as O, = [Cry tes dts des de» ei], Where Cy is ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | Since our system requires only 128 bytes(32-bit floats) per data packet, the measured communication latency under normal network conditions is 16 ms ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | Since our system requires only 128 bytes(32-bit floats) per data packet, the measured communication latency under normal network conditions is 16 ms ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / Abstract - extractive body cue:** Our RL-based training framework features three core techrniques: upper-body pose curriculum for dynamic balance adaptation, height-tracking reward for precise squatting, and symmetry utilization for action ...
- **p. 5 / 1 2001p - extractive body cue:** 4) Symmetry Urilization: We introduce the same trick as 50] to our training framework.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Symmetry, Utilization, introduce, three, algorithmic, variants, comparison, ours, terms, tion, uses, only, symmetrical, data, augmentation, loss, none, does, employ, stigmentation.
- **Relevant PDF headings:** A. Network Architecture (p. 14).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | This migration enables the use of HOMIE to control robots within a variety of simulated environments By leveraging these simulated scenes, the ... | p. 10 (20 Bet), p. 10 (20 Bet) |
| Balance-aware whole-body execution | Compared to the training setting of Unitree Gl. we only ‘change the range of height tracking and some robot-specific distance values, without ... | p. 8 (A. Humanoid Whole-body Control), p. 7 (A. Humanoid Whole-body Control) |
| Recovery / adaptation | In summary, symmetry data augmentation significantly improves training efficiency, while the use of symmetry loss effectively prevents the policy from sacrificing symmetry ... | p. 8 (A. Humanoid Whole-body Control), p. 10 (C. Teleoperation System) |

## Failure and Ablation Link

- **p. 7 / A. Humanoid Whole-body Control - extractive body cue:** environments, where components unrelated to the ablation are kept unchanged, and only relevant parts are modified for training, Detailed parameters used in training and evaluation ...
- **p. 7 / C. Hardware System Design - extractive body cue:** 7: Ablation experiments of our RL training framework.
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** Compared to the training setting of Unitree Gl. we only ‘change the range of height tracking and some robot-specific distance values, without any other changes ...
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** Symmetry Utilization, We introduce three algorithmic variants for comparison with ours in terms of symmetry ut tion: w/ aug, which uses only symmetrical data augmentation; ...
- **p. 9 / B. Teleoperation Hardware Performance - extractive body cue:** Therefore, our approach achieves a very high output frequency without requiring GPU and System on Chip (SoC) intensive hardware.
- **p. 9 / C. Teleoperation System - extractive body cue:** In all these tasks, each robot is controlled by a single operator, and the communication between the robot and operator is facilitated via Wi-Fi, without ...
- **p. 10 / 20 Bet - extractive body cue:** Multi-view images are processed through a MAE-pretrained ViT encoder, and the features of robot proprioceptive states are extracted using an MLP.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 8 (A. Humanoid Whole-body Control), p. 3 (B. Whole-body Loco-Manipulation), p. 2 (Abstract), p. 2 (Abstract), p. 4 (B. Humanoid Whole-body Control), p. 4 (A. System Overview), objective p. 7 (A. Humanoid Whole-body Control), p. 2 (Abstract), p. 5 (1 2001p), p. 2 (A. Teleoperation Systems), p. 3 (A. Teleoperation Systems), p. 3 (A. Teleoperation Systems), temporal p. 4 (B. Humanoid Whole-body Control), p. 9 (C. Teleoperation System), p. 2 (Abstract), p. 2 (Abstract), p. 3 (A. Teleoperation Systems), p. 3 (B. Whole-body Loco-Manipulation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Reinforcement Learning (RL)-based algorithms, especially those based on Proximal Policy Optimization (PPO) [32], offer a more powerful altemative. (p. 3, B. Whole-body Loco-Manipulation).
- **Objective/update evidence:** These two losses are added to the network optimization process, thereby enforcing symmetry of the neural network. (p. 5, 1 2001p).
- **Temporal/runtime evidence:** 1) Training Settings: ‘The observations of one step are defined as O, = [Cry tes dts des de» ei], Where Cy is the command, «is the body's angular velocity, gis ... (p. 4, B. Humanoid Whole-body Control).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
