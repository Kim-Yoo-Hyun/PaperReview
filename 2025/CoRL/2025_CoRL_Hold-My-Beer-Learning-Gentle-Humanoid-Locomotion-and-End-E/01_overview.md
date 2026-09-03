# Hold My Beer: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=Bl2VfU9NhF.
> PDF retrieval source: https://arxiv.org/pdf/2505.24198. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, locomotion, end-effector stabilization, multi-rate control
- Official paper: https://openreview.net/forum?id=Bl2VfU9NhF
- Full-text retrieval: https://arxiv.org/pdf/2505.24198
- Code/Project: https://lecar-lab.github.io/SoFTA/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 The nature of ground contacts makes it more susceptible to the sim-to-real gap, demanding greater robustness against noise and disturbances.를 문제로 두고, Our key contributions are: • We introduce SoFTA, a novel slow-fast two-agent RL framework that decouples control for locomotion and EE stabilization in both temporal and task objective space, enabling robust locomotion ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Can your humanoid walk up and hand you a full cup of beer-without spilling a drop?
- **p. 1 / Abstract - extractive body cue:** While humanoids are increasingly featured in flashy demos-dancing, delivering packages, traversing rough terrain-fine-grained control during locomotion remains a significant challenge.
- **p. 1 / Abstract - extractive body cue:** In particular, stabilizing a filled end-effector (EE) while walking is far from solved, due to a fundamental mismatch in task characteristics: locomotion demands slow-timescale, robust ...
- **p. 1 / Abstract - extractive body cue:** To address this, we propose SoFTA, a Slow-Fast Two-Agent framework that decouples upper-body and lower-body control into separate agents operating at different frequencies and with ...
- **p. 1 / Abstract - extractive body cue:** This temporal and objective separation mitigates policy interference and enables coordinated whole-body behavior.
- **p. 2 / 1 Introduction - extractive body cue:** The nature of ground contacts makes it more susceptible to the sim-to-real gap, demanding greater robustness against noise and disturbances.
- **p. 2 / 1 Introduction - extractive body cue:** To bridge the gap, we propose SoFTA-a Slow-Fast Two-Agent reinforcement learning (RL) framework that decouples the action and value spaces of the upper and lower ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our key contributions are: • We introduce SoFTA, a novel slow-fast two-agent RL framework that decouples control for locomotion and EE stabilization in both temporal ...
- **p. 2 / 1 Introduction - extractive body cue:** To bridge the gap, we propose SoFTA-a Slow-Fast Two-Agent reinforcement learning (RL) framework that decouples the action and value spaces of the upper and lower ...
- **p. 16 / A.1 Training Details - extractive body cue:** After obtaining a stable policy, we introduce push disturbances to further improve robustness under external disturbance.
- **p. 16 / A.1 Training Details - extractive body cue:** Notice that the termination is a shared reward component Also, we introduce several penalties and energy regularization in order to achieve robust sim-to-real performance like ...
- **p. 17 / A.1 Training Details - extractive body cue:** These include general PPO settings, action std for different body modules, and the network architecture shared across policy and value networks.
- **p. 17 / A.1 Training Details - extractive body cue:** Parameter Value General PPO Settings Gamma (γ) 0.99 GAE Lambda (λ) 0.95 Value Loss Coef 1.0 Entropy Coef 0.01 Actor Learning Rate 1 × 10-3 ...
- **p. 15 / A.1 Training Details - extractive body cue:** The first value is a binary indicator of whether the desired gait is a double-stance (both feet in contact).
- **p. 15 / A.1 Training Details - extractive body cue:** Observation We adopt an asymmetric observation structure to enable efficient policy learning in simulation while ensuring robust real-world deployment under partial observability.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The actor relies solely on onboard-accessible inputs-proprioception, command signals, and recent actions-excluding global position data, thus removing dependence on odometry or external tracking. | proprioception, reference pose/motion, visual or language command | p. 15 (A.1 Training Details), p. 15 (A.1 Training Details) |
| State/latent | actor, relies, solely, onboard-accessible, inputs-proprioception, command, signals, recent, actions-excluding, global, position, data | whole-body pose, balance/contact state와 skill/mode | p. 15 (A.1 Training Details), p. 15 (A.1 Training Details), p. 17 (A.1 Training Details) |
| Output/action | Type Observation Actor Critic Scale Noise Scale Privileged base lin vel ✗ ✓ 2.0 0.0 end effector relative pos ✗ ✓ 1.0 0.0 end effector gravity ✗ ✓ 1.0 0.0 Proprioception base ... | joint/whole-body action, motion target 또는 task trajectory | p. 15 (A.1 Training Details), p. 17 (A.1 Training Details), p. 2 (1 Introduction) |
| Objective/outcome | Notice that the termination is a shared reward component Also, we introduce several penalties and energy regularization in order to achieve robust sim-to-real performance like dof limit, stand symmetry, contact force, feet ... | tracking, balance, skill/task success와 recovery | p. 16 (A.1 Training Details), p. 15 (A.1 Training Details), p. 16 (A.1 Training Details) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Our key contributions are: • We introduce SoFTA, a novel slow-fast two-agent RL framework that decouples control for locomotion and EE stabilization in both temporal ...
- **p. 2 / 1 Introduction - extractive body cue:** To bridge the gap, we propose SoFTA-a Slow-Fast Two-Agent reinforcement learning (RL) framework that decouples the action and value spaces of the upper and lower ...
- **p. 16 / A.1 Training Details - extractive body cue:** After obtaining a stable policy, we introduce push disturbances to further improve robustness under external disturbance.
- **p. 16 / A.1 Training Details - extractive body cue:** Notice that the termination is a shared reward component Also, we introduce several penalties and energy regularization in order to achieve robust sim-to-real performance like ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for tasks ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Simulation Results: EE stability is evaluated in Isaac Gym across various tasks. SoFTA consistently outperforms the baselines in most metrics, demonstrating superior EE ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Real-World Results: EE stability evaluated in Real World across diverse task settings. SoFTA consistently outperforms baselines, especially in Acc-Z metric. Jointly Learn Locomotion ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 4: Comparison of actor and critic observations with scaling factors. Privileged observations used only by the critic are shaded and marked in red. During ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Embodiment/environment | Across both simulation and real-world environments, our experiments show that a 50 Hz lower-body control frequency consistently achieves stable locomotion, regardless of the upper-body control frequency, whereas other lower-body frequen ... | hardware/simulator version and reset protocol | p. 17 (A.2 More Analysis on Frequency Ablation) |
| Dataset/benchmark | Across both simulation and real-world environments, our experiments show that a 50 Hz lower-body control frequency consistently achieves stable locomotion, regardless of the upper-body control frequency, whereas other lower-body frequen ... | role, split, size and leakage | p. 17 (A.2 More Analysis on Frequency Ablation) |
| Metric | Figure 2: Overview of the SoFTA framework: The framework employs two distinct agents that share the same observation but act within separate action spaces at different rates, targeting two fundamentally different task: ... | definition, denominator, direction and uncertainty | p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 16 (Figure/Table caption) |
| Baseline/ablation | Table 1: Simulation Results: EE stability is evaluated in Isaac Gym across various tasks. SoFTA consistently outperforms the baselines in most metrics, demonstrating superior EE stability. Baselines. We compare SoFTA with the ... | fair input/data/compute/action matching | p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Max Acc under Different Control Frequencies in Simulation and Real World: Higher values reflect reduced stability. N/A indicates unstable or failed trials in ...
- **p. 9 / 5 Conclusion - extractive body cue:** 6 Limitation Despite its strong performance, SoFTA still faces several limitations.
- **p. 9 / 5 Conclusion - extractive body cue:** First, while it significantly reduces EE acceleration, the achieved stability still falls short of human-level performance.
- **p. 18 / A.2 More Analysis on Frequency Ablation - extractive body cue:** We observe that increasing the upper-body control frequency reduces recovery time (defined as the time when the error first falls below 1 e of its ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for tasks ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Emergent Compensation Behavior. 4.2 Real-World Results To answer Q2 (What capabilities does SoFTA enable in real world?), we assess EE stability in three ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 4: Comparison of actor and critic observations with scaling factors. Privileged observations used only by the critic are shaded and marked in red. During ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 The nature of ground contacts makes it more susceptible to the sim-to-real gap, demanding greater robustness against noise and disturbances.를 문제로 두고, Our key contributions are: • We introduce SoFTA, a novel slow-fast two-agent RL framework that decouples control for locomotion and EE stabilization in both temporal and task objective space, enabling robust locomotion ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 16 (A.1 Training Details), p. 17 (A.1 Training Details), p. 17 (A.1 Training Details), p. 16 (A.1 Training Details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
