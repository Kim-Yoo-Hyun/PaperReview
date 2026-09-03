# Insights — SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=W86R5sIsxE; PDF retrieval source: https://arxiv.org/pdf/2606.27807.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** SpikeVLA consists of three complementary modules.
- **p. 2 / 1. Introduction - extractive body cue:** 1) We propose SpikeVLA, the first VLA framework built on spiking neural networks.
- **p. 3 / 3.2. Spike Neural Network Vision Encoder - extractive body cue:** We propose an SNN-based visual encoder that fuses the current frame with history frames to provide temporal context for time-dependent VLA tasks.
- **p. 3 / 3.1. Architecture - extractive body cue:** We propose SpikeVLA, an end-to-end spiking VLA architecture for embodied navigation, consisting of a spiking vision encoder (Spike-V), a multimodal spiking language model (Spike-L), and ...
- **p. 4 / 3.2. Spike Neural Network Vision Encoder - extractive body cue:** Building on differential coding, we introduce differential spiking neurons and perform unified differential conversion of linear and nonlinear operators in SigLIPv2, thereby obtaining a spiking ...
- **p. 5 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** We propose an action policy network based on Spiking Neural Networks.
- **p. 5 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** During reinforcement learning, the network is trained using the Proximal Policy Optimization (PPO) algorithm to optimize its parameters.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Spike Neural Network Vision Encoder), p. 3 (3.1. Architecture), p. 4 (3.2. Spike Neural Network Vision Encoder), p. 5 (3.4. Spiking Neural Network for Action Policy)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** To address this challenge, previous work has explored efficiency-oriented designs.
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose SpikeVLA, the first VLA architecture built on spiking neural networks, which represents a trade-off between performance and efficiency, as ...
- **p. 6 / 4.1. Experimental Setups - extractive body cue:** For low-level locomotion, we quantify command tracking and safety using linear and angular velocity tracking errors and the collision rate.
- **p. 5 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** This approach transforms continuous observations into sparse and robust spike events, improving the stability and noise robustness of quadruped locomotion control.
- **p. 8 / A ANN - extractive body cue:** Therefore, SpikeVLA does not simply trade accuracy for efficiency. instead, it achieves higher energy efficiency through a sparse, event-driven computational paradigm.
- **p. 6 / 4.2. Main Results - extractive body cue:** We evaluated SpikeVLA in the VLN-CE-Isaac simulator using the Unitree Go2 platform to assess its transferability to closedloop embodied execution under realistic dynamics and sensor ...
- **p. 8 / A ANN - extractive body cue:** Resource Efficiency Error ↓ Error ↓ Mem(MB)↓Eng(µJ)↓ACEs(106)↓ NaVILA 0.23 0.38 1.20 5.80 161.48 SpikeVLA 0.42 0.29 2.35 0.31 5.53 mance degradation.
- **Boundary to test:** For low-level locomotion, we quantify command tracking and safety using linear and angular velocity tracking errors and the collision rate.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | SpikeVLA consists of three complementary modules. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | As shown in Table 2, it achieves a strong and stable navigation performance, maintaining high metric scores compared to NaVILA (Cheng et al., 2025). | p. 6 (4.2. Main Results), p. 6 (4.2. Main Results) |
| Failure/limitation | For low-level locomotion, we quantify command tracking and safety using linear and angular velocity tracking errors and the collision rate. | p. 6 (4.1. Experimental Setups), p. 5 (3.4. Spiking Neural Network for Action Policy) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 At timestep t, the actor maps the observation st to a policy πθ(· / st) = N(µt, σt) and samples an action at, while the critic estimates the state value Vϕ(st) to ...를 To encode continuous observation inputs into discrete spike outputs, we adopt population encoding.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 For low-level locomotion, we quantify command tracking and safety using linear and angular velocity tracking errors and the collision rate.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: SpikeVLA consists of three complementary modules.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** For low-level locomotion, we quantify command tracking and safety using linear and angular velocity tracking errors and the collision rate.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Navigation Performance on VLN-CE Benchmarks..
3. Compare against the body-reported baseline or a matched simpler baseline: The current results suggest that SpikeVLA achieves performance comparable to strong baselines (Zhang et al., 2024a; Cheng et al., 2025) under the same RGB-only, nowaypoint settings, while maintaining the energy-efficiency advantages obs ....
4. Report the body metric and its denominator/aggregation: We evaluated VLN-CE R2R/RxR and VLN-CE-Isaac using a unified set of metrics, including NE, OS, SR, SPL, and nDTW, which capture goal-reaching accuracy, feasibility, success rate, path efficiency and trajectory fidelity, respectively..
5. Re-run the body-reported ablation/failure condition: Figure 4: SNN action policy network ablations. The top row compares different spike encoding kernels (Laplacian, Gaussian, Triangular, and IMQ) in terms of reward, linear velocity error, angular velocity error, and terrain ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3.1. Architecture), p. 5 (3.4. Spiking Neural Network for Action Policy), p. 5 (3.4. Spiking Neural Network for Action Policy); the primary result is directionally consistent at p. 6 (4.2. Main Results), p. 6 (4.2. Main Results), p. 15 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 SpikeVLA, consists, three mechanism이 The current results suggest that SpikeVLA achieves performance comparable to strong baselines (Zhang et al., 2024a; ... 대비 We evaluated VLN-CE R2R/RxR and VLN-CE-Isaac using a unified set of metrics, including NE, OS, SR, SPL, and ...을 개선하고, For low-level locomotion, we quantify command tracking and safety using linear and angular velocity tracking errors ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
