# Method - Hold My Beer: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Bl2VfU9NhF; PDF retrieval source: https://arxiv.org/pdf/2505.24198. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 16 (A.1 Training Details), p. 17 (A.1 Training Details), p. 17 (A.1 Training Details), p. 16 (A.1 Training Details), p. 15 (A.1 Training Details), p. 15 (A.1 Training Details)): Notice that the termination is a shared reward component Also, we introduce several penalties and energy regularization in order to achieve robust sim-to-real performance like dof limit, stand symmetry, contact ...

## Method Body Digest

- **p. 16 / A.1 Training Details - extractive body cue:** Notice that the termination is a shared reward component Also, we introduce several penalties and energy regularization in order to achieve robust sim-to-real performance like ...
- **p. 17 / A.1 Training Details - extractive body cue:** These include general PPO settings, action std for different body modules, and the network architecture shared across policy and value networks.
- **p. 17 / A.1 Training Details - extractive body cue:** Parameter Value General PPO Settings Gamma (γ) 0.99 GAE Lambda (λ) 0.95 Value Loss Coef 1.0 Entropy Coef 0.01 Actor Learning Rate 1 × 10-3 ...
- **p. 16 / A.1 Training Details - extractive body cue:** After obtaining a stable policy, we introduce push disturbances to further improve robustness under external disturbance.
- **p. 15 / A.1 Training Details - extractive body cue:** The first value is a binary indicator of whether the desired gait is a double-stance (both feet in contact).
- **p. 15 / A.1 Training Details - extractive body cue:** Observation We adopt an asymmetric observation structure to enable efficient policy learning in simulation while ensuring robust real-world deployment under partial observability.
- **p. 15 / A.1 Training Details - extractive body cue:** If this value is zero, all stabilization-related rewards are disabled for that EE.
- **p. 16 / A.1 Training Details - extractive body cue:** Rewards Design We show the grouped SoFTA task reward components in Table 8.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Our key contributions are: • We introduce SoFTA, a novel slow-fast two-agent RL framework that decouples control for locomotion and EE stabilization in both temporal ...
- **p. 2 / 1 Introduction - extractive body cue:** To bridge the gap, we propose SoFTA-a Slow-Fast Two-Agent reinforcement learning (RL) framework that decouples the action and value spaces of the upper and lower ...
- **p. 16 / A.1 Training Details - extractive body cue:** After obtaining a stable policy, we introduce push disturbances to further improve robustness under external disturbance.

## Source Evidence Cues

- **p. 16 / A.1 Training Details - extractive body cue:** Notice that the termination is a shared reward component Also, we introduce several penalties and energy regularization in order to achieve robust sim-to-real performance like ...
- **p. 17 / A.1 Training Details - extractive body cue:** These include general PPO settings, action std for different body modules, and the network architecture shared across policy and value networks.
- **p. 17 / A.1 Training Details - extractive body cue:** Parameter Value General PPO Settings Gamma (γ) 0.99 GAE Lambda (λ) 0.95 Value Loss Coef 1.0 Entropy Coef 0.01 Actor Learning Rate 1 × 10-3 ...
- **p. 16 / A.1 Training Details - extractive body cue:** After obtaining a stable policy, we introduce push disturbances to further improve robustness under external disturbance.
- **p. 15 / A.1 Training Details - extractive body cue:** The first value is a binary indicator of whether the desired gait is a double-stance (both feet in contact).
- **p. 15 / A.1 Training Details - extractive body cue:** Observation We adopt an asymmetric observation structure to enable efficient policy learning in simulation while ensuring robust real-world deployment under partial observability.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | Notice that the termination is a shared reward component Also, we introduce several penalties and energy regularization in order to achieve robust ... | p. 16 (A.1 Training Details), p. 17 (A.1 Training Details) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | These include general PPO settings, action std for different body modules, and the network architecture shared across policy and value networks. | p. 17 (A.1 Training Details), p. 17 (A.1 Training Details) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | Parameter Value General PPO Settings Gamma (γ) 0.99 GAE Lambda (λ) 0.95 Value Loss Coef 1.0 Entropy Coef 0.01 Actor Learning Rate ... | p. 17 (A.1 Training Details), p. 16 (A.1 Training Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 16 / A.1 Training Details - extractive body cue:** Notice that the termination is a shared reward component Also, we introduce several penalties and energy regularization in order to achieve robust sim-to-real performance like ...
- **p. 15 / A.1 Training Details - extractive body cue:** If this value is zero, all stabilization-related rewards are disabled for that EE.
- **p. 16 / A.1 Training Details - extractive body cue:** Rewards Design We show the grouped SoFTA task reward components in Table 8.
- **p. 17 / A.1 Training Details - extractive body cue:** 2 termination -100.0 1terminate Table 7: Reward terms categorized by body group, including task rewards and penalties with corresponding expressions and weights.
- **p. 17 / A.1 Training Details - extractive body cue:** Parameter Value General PPO Settings Gamma (γ) 0.99 GAE Lambda (λ) 0.95 Value Loss Coef 1.0 Entropy Coef 0.01 Actor Learning Rate 1 × 10-3 ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 17 (A.1 Training Details), p. 16 (A.1 Training Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | actor, relies, solely, onboard-accessible, inputs-proprioception, command, signals, recent, actions-excluding, global, position, data, thus, removing | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | actor, relies, solely, onboard-accessible, inputs-proprioception, command, signals, recent, actions-excluding, global | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | contributions, introduce, SoFTA, novel, slow-fast, two-agent, framework, decouples, control, locomotion | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | Notice, termination, shared, reward, component, introduce, several, penalties, energy, regularization | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 15 / A.1 Training Details - extractive body cue:** The actor relies solely on onboard-accessible inputs-proprioception, command signals, and recent actions-excluding global position data, thus removing dependence on odometry or external tracking.
- **p. 15 / A.1 Training Details - extractive body cue:** Type Observation Actor Critic Scale Noise Scale Privileged base lin vel ✗ ✓ 2.0 0.0 end effector relative pos ✗ ✓ 1.0 0.0 end effector ...
- **p. 17 / A.1 Training Details - extractive body cue:** These include general PPO settings, action std for different body modules, and the network architecture shared across policy and value networks.
- **p. 2 / 1 Introduction - extractive body cue:** To bridge the gap, we propose SoFTA-a Slow-Fast Two-Agent reinforcement learning (RL) framework that decouples the action and value spaces of the upper and lower ...
- **p. 2 / 1 Introduction - extractive body cue:** This capability is essential for safe and precise physical interaction with objects-such as handing over a cup of water or recording stable video-yet current humanoids ...
- **p. 16 / A.1 Training Details - extractive body cue:** Notice that the termination is a shared reward component Also, we introduce several penalties and energy regularization in order to achieve robust sim-to-real performance like ...
- **p. 16 / A.1 Training Details - extractive body cue:** After obtaining a stable policy, we introduce push disturbances to further improve robustness under external disturbance.
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | Our key contributions are: • We introduce SoFTA, a novel slow-fast two-agent RL framework that decouples control for locomotion and EE stabilization ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | Observations are stacked over five timesteps to provide short-term temporal context. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | The proprioceptive input sprop t includes a 5-step history of joint positions qt ∈R27, joint velocities ˙qt ∈R27, root angular velocities ωroot ... | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | We train our policy in Isaac Gym at 200 Hz simulation frequency. | hardware, batch and throughput |

## Training vs Inference

- **p. 17 / A.1 Training Details - extractive body cue:** Parameter Value General PPO Settings Gamma (γ) 0.99 GAE Lambda (λ) 0.95 Value Loss Coef 1.0 Entropy Coef 0.01 Actor Learning Rate 1 × 10-3 ...
- **p. 17 / A.1 Training Details - extractive body cue:** Parameter Value General PPO Settings Gamma (γ) 0.99 GAE Lambda (λ) 0.95 Value Loss Coef 1.0 Entropy Coef 0.01 Actor Learning Rate 1 × 10-3 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Notice, termination, shared, reward, component, introduce, several, penalties, energy, regularization, order, achieve, robust, sim-to-real, performance, like, limit, stand, symmetry, contact.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | Across both simulation and real-world environments, our experiments show that a 50 Hz lower-body control frequency consistently achieves stable locomotion, regardless of ... | p. 17 (A.2 More Analysis on Frequency Ablation), p. 4 (Figure/Table caption) |
| Balance-aware whole-body execution | Table 1: Simulation Results: EE stability is evaluated in Isaac Gym across various tasks. SoFTA consistently outperforms the baselines in most metrics, ... | p. 5 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Recovery / adaptation | Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are ... | p. 7 (Figure/Table caption), p. 5 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control with SoFTA: (A) Carrying bottles of drink during a 1m/s large-step walk. (B) Liquid surface ...
- **p. 18 / A.2 More Analysis on Frequency Ablation - extractive body cue:** 0.00 0.02 0.04 0.06 0.08 0.10 Time(s) 0.4 0.2 0.0 0.2 0.4 Joint shoulder_pitch Target Pos Upper-body 50 Hz Upper-body 100 Hz Base Vel(0.3m/s) 0.00 ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of the SoFTA framework: The framework employs two distinct agents that share the same observation but act within separate action spaces at ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Humanoid as Camera Stabilizer to record videos. Case 2: Humanoid as Camera Stabilizer. Figure 6 shows video footage recorded by the robot during ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for tasks ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 8: PPO Multi-Actor-Critic Training Configuration A.2 More Analysis on Frequency Ablation Methods Response Time (s) ↓ Max Acc (m/s2) ↓ Max Vel (m/s) ↓ ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 5: Command ranges used during training. Domain Randomization To enhance the robustness and generalization of SoFTA, we apply do- main randomization techniques, as detailed ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 16 (A.1 Training Details), p. 17 (A.1 Training Details), p. 17 (A.1 Training Details), p. 16 (A.1 Training Details), p. 15 (A.1 Training Details), p. 15 (A.1 Training Details), objective p. 16 (A.1 Training Details), p. 15 (A.1 Training Details), p. 16 (A.1 Training Details), p. 17 (A.1 Training Details), p. 17 (A.1 Training Details), temporal p. 2 (1 Introduction), p. 15 (A.1 Training Details), p. 3 (2 Related Work), p. 5 (13 DoFs), p. 5 (13 DoFs), p. 8 (33.3 Hz).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
