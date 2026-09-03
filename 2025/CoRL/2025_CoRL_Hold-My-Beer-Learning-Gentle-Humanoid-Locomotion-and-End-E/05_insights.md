# Insights — Hold My Beer: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Bl2VfU9NhF; PDF retrieval source: https://arxiv.org/pdf/2505.24198. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** Our key contributions are: • We introduce SoFTA, a novel slow-fast two-agent RL framework that decouples control for locomotion and EE stabilization in both temporal ...
- **p. 2 / 1 Introduction - extractive body cue:** To bridge the gap, we propose SoFTA-a Slow-Fast Two-Agent reinforcement learning (RL) framework that decouples the action and value spaces of the upper and lower ...
- **p. 16 / A.1 Training Details - extractive body cue:** After obtaining a stable policy, we introduce push disturbances to further improve robustness under external disturbance.
- **p. 16 / A.1 Training Details - extractive body cue:** Notice that the termination is a shared reward component Also, we introduce several penalties and energy regularization in order to achieve robust sim-to-real performance like ...
- **p. 17 / A.1 Training Details - extractive body cue:** These include general PPO settings, action std for different body modules, and the network architecture shared across policy and value networks.
- **p. 17 / A.1 Training Details - extractive body cue:** Parameter Value General PPO Settings Gamma (γ) 0.99 GAE Lambda (λ) 0.95 Value Loss Coef 1.0 Entropy Coef 0.01 Actor Learning Rate 1 × 10-3 ...
- **p. 15 / A.1 Training Details - extractive body cue:** The first value is a binary indicator of whether the desired gait is a double-stance (both feet in contact).
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 16 (A.1 Training Details), p. 16 (A.1 Training Details), p. 17 (A.1 Training Details), p. 17 (A.1 Training Details)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** The nature of ground contacts makes it more susceptible to the sim-to-real gap, demanding greater robustness against noise and disturbances.
- **p. 2 / 1 Introduction - extractive body cue:** To bridge the gap, we propose SoFTA-a Slow-Fast Two-Agent reinforcement learning (RL) framework that decouples the action and value spaces of the upper and lower ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Max Acc under Different Control Frequencies in Simulation and Real World: Higher values reflect reduced stability. N/A indicates unstable or failed trials in ...
- **p. 9 / 5 Conclusion - extractive body cue:** 6 Limitation Despite its strong performance, SoFTA still faces several limitations.
- **p. 9 / 5 Conclusion - extractive body cue:** First, while it significantly reduces EE acceleration, the achieved stability still falls short of human-level performance.
- **p. 18 / A.2 More Analysis on Frequency Ablation - extractive body cue:** We observe that increasing the upper-body control frequency reduces recovery time (defined as the time when the error first falls below 1 e of its ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for tasks ...
- **Boundary to test:** Figure 7: Max Acc under Different Control Frequencies in Simulation and Real World: Higher values reflect reduced stability. N/A indicates unstable or failed trials in the real-world testing. We observe that in ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our key contributions are: • We introduce SoFTA, a novel slow-fast two-agent RL framework that decouples control for locomotion and EE stabilization in both temporal and task objective space, enabling robust locomotion ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for tasks requiring precise EE stability. While Whole-body RL ... | p. 7 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Failure/limitation | Figure 7: Max Acc under Different Control Frequencies in Simulation and Real World: Higher values reflect reduced stability. N/A indicates unstable or failed trials in the real-world testing. We observe that in ... | p. 8 (Figure/Table caption), p. 9 (5 Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 The actor relies solely on onboard-accessible inputs-proprioception, command signals, and recent actions-excluding global position data, thus removing dependence on odometry or external tracking.를 Type Observation Actor Critic Scale Noise Scale Privileged base lin vel ✗ ✓ 2.0 0.0 end effector relative pos ✗ ✓ 1.0 0.0 end effector gravity ✗ ✓ 1.0 0.0 Proprioception base ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 7: Max Acc under Different Control Frequencies in Simulation and Real World: Higher values reflect reduced stability. N/A indicates unstable or failed trials in the real-world testing. We observe that in ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our key contributions are: • We introduce SoFTA, a novel slow-fast two-agent RL framework that decouples control for locomotion and EE stabilization in both temporal and task objective space, enabling robust locomotion ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, locomotion, end-effector stabilization, multi-rate control`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 7: Max Acc under Different Control Frequencies in Simulation and Real World: Higher values reflect reduced stability. N/A indicates unstable or failed trials in the real-world testing. We observe that in ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Across both simulation and real-world environments, our experiments show that a 50 Hz lower-body control frequency consistently achieves stable locomotion, regardless of the upper-body control frequency, whereas other lower-body frequen ....
3. Compare against the body-reported baseline or a matched simpler baseline: Table 1: Simulation Results: EE stability is evaluated in Isaac Gym across various tasks. SoFTA consistently outperforms the baselines in most metrics, demonstrating superior EE stability. Baselines. We compare SoFTA with the ....
4. Report the body metric and its denominator/aggregation: Figure 2: Overview of the SoFTA framework: The framework employs two distinct agents that share the same observation but act within separate action spaces at different rates, targeting two fundamentally different task: ....
5. Re-run the body-reported ablation/failure condition: Figure 1: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control with SoFTA: (A) Carrying bottles of drink during a 1m/s large-step walk. (B) Liquid surface when the robot is tapping in place. ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 16 (A.1 Training Details), p. 17 (A.1 Training Details), p. 17 (A.1 Training Details); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, introduce, SoFTA mechanism이 Table 1: Simulation Results: EE stability is evaluated in Isaac Gym across various tasks. SoFTA consistently ... 대비 Figure 2: Overview of the SoFTA framework: The framework employs two distinct agents that share the same observation ...을 개선하고, Figure 7: Max Acc under Different Control Frequencies in Simulation and Real World: Higher values reflect ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
