# SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=W86R5sIsxE.
> PDF retrieval source: https://openreview.net/pdf/27ac3094b9d6afc1c8c39e0ae99418fd937e0219.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://openreview.net/forum?id=W86R5sIsxE
- Full-text retrieval: https://openreview.net/pdf/27ac3094b9d6afc1c8c39e0ae99418fd937e0219.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 To address this challenge, previous work has explored efficiency-oriented designs.를 문제로 두고, SpikeVLA consists of three complementary modules.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have become a dominant paradigm for embodied intelligence.
- **p. 1 / Abstract - extractive body cue:** However, most existing approaches are built on large-scale transformers, resulting in substantial inference latency and energy consumption that limit their practical deployment in low-power, real-time ...
- **p. 1 / Abstract - extractive body cue:** We propose SpikeVLA, a spiking VLA architecture for embodied navigation with energy-efficient inference, consisting of three key components.
- **p. 1 / Abstract - extractive body cue:** (i) A spiking vision encoder, Spike-V, that replaces dense continuous layers with event-driven spiking layers to reduce the energy consumption of visual representation learning.
- **p. 1 / Abstract - extractive body cue:** (ii) A multi-modal spiking large language model, Spike-L, that reformulates cross-modal reasoning with spiking dynamics and token-level event-driven sparsity to further lower computational cost.
- **p. 1 / 1. Introduction - extractive body cue:** To address this challenge, previous work has explored efficiency-oriented designs.
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose SpikeVLA, the first VLA architecture built on spiking neural networks, which represents a trade-off between performance and efficiency, as ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** SpikeVLA consists of three complementary modules.
- **p. 2 / 1. Introduction - extractive body cue:** 1) We propose SpikeVLA, the first VLA framework built on spiking neural networks.
- **p. 3 / 3.2. Spike Neural Network Vision Encoder - extractive body cue:** We propose an SNN-based visual encoder that fuses the current frame with history frames to provide temporal context for time-dependent VLA tasks.
- **p. 3 / 3.1. Architecture - extractive body cue:** We propose SpikeVLA, an end-to-end spiking VLA architecture for embodied navigation, consisting of a spiking vision encoder (Spike-V), a multimodal spiking language model (Spike-L), and ...
- **p. 4 / 3.2. Spike Neural Network Vision Encoder - extractive body cue:** Building on differential coding, we introduce differential spiking neurons and perform unified differential conversion of linear and nonlinear operators in SigLIPv2, thereby obtaining a spiking ...
- **p. 5 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** We propose an action policy network based on Spiking Neural Networks.
- **p. 5 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** During reinforcement learning, the network is trained using the Proximal Policy Optimization (PPO) algorithm to optimize its parameters.
- **p. 6 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** We train the spiking action policy network using surrogate-gradient spatiotemporal backpropagation, accumulating gradients over discrete timesteps t = 1, . . . , T and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | At timestep t, the actor maps the observation st to a policy πθ(· / st) = N(µt, σt) and samples an action at, while the critic estimates the state value Vϕ(st) to ... | image/video, language instruction, proprioception과 history | p. 6 (3.4. Spiking Neural Network for Action Policy), p. 5 (3.4. Spiking Neural Network for Action Policy) |
| State/latent | timestep, actor, maps, observation, policy, samples, action, while, critic, estimates, state, value | language-grounded task state와 action-policy context | p. 6 (3.4. Spiking Neural Network for Action Policy), p. 5 (3.4. Spiking Neural Network for Action Policy), p. 6 (3.4. Spiking Neural Network for Action Policy) |
| Output/action | To encode continuous observation inputs into discrete spike outputs, we adopt population encoding. | continuous action, pose 또는 action chunk | p. 5 (3.4. Spiking Neural Network for Action Policy), p. 6 (3.4. Spiking Neural Network for Action Policy), p. 3 (3.1. Architecture) |
| Objective/outcome | We optimize the policy by maximizing the clipped surrogate objective. | instruction following, task success, generalization과 latency | p. 6 (3.4. Spiking Neural Network for Action Policy), p. 4 (3.2. Spike Neural Network Vision Encoder), p. 4 (3.2. Spike Neural Network Vision Encoder) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** SpikeVLA consists of three complementary modules.
- **p. 2 / 1. Introduction - extractive body cue:** 1) We propose SpikeVLA, the first VLA framework built on spiking neural networks.
- **p. 3 / 3.2. Spike Neural Network Vision Encoder - extractive body cue:** We propose an SNN-based visual encoder that fuses the current frame with history frames to provide temporal context for time-dependent VLA tasks.
- **p. 3 / 3.1. Architecture - extractive body cue:** We propose SpikeVLA, an end-to-end spiking VLA architecture for embodied navigation, consisting of a spiking vision encoder (Spike-V), a multimodal spiking language model (Spike-L), and ...
- **p. 4 / 3.2. Spike Neural Network Vision Encoder - extractive body cue:** Building on differential coding, we introduce differential spiking neurons and perform unified differential conversion of linear and nonlinear operators in SigLIPv2, thereby obtaining a spiking ...
- **p. 6 / 4.2. Main Results - extractive body cue:** As shown in Table 2, it achieves a strong and stable navigation performance, maintaining high metric scores compared to NaVILA (Cheng et al., 2025).
- **p. 6 / 4.2. Main Results - extractive body cue:** The current results suggest that SpikeVLA achieves performance comparable to strong baselines (Zhang et al., 2024a; Cheng et al., 2025) under the same RGB-only, nowaypoint ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 8: Ablation of Actor Network Dimensions. It shows the performance of different Actor network dimensions (A = [128, 128], A = [256, 128], A ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.2. Main Results), p. 6 (4.2. Main Results) |
| Embodiment/environment | Navigation Performance on VLN-CE Benchmarks. | hardware/simulator version and reset protocol | p. 6 (4.2. Main Results), p. 6 (4.1. Experimental Setups) |
| Dataset/benchmark | Navigation Performance on VLN-CE Benchmarks. | role, split, size and leakage | p. 6 (4.2. Main Results), p. 6 (4.1. Experimental Setups) |
| Metric | We evaluated VLN-CE R2R/RxR and VLN-CE-Isaac using a unified set of metrics, including NE, OS, SR, SPL, and nDTW, which capture goal-reaching accuracy, feasibility, success rate, path efficiency and trajectory fidelity, respectively. | definition, denominator, direction and uncertainty | p. 6 (4.1. Experimental Setups), p. 15 (Figure/Table caption), p. 7 (4.2. Main Results) |
| Baseline/ablation | The current results suggest that SpikeVLA achieves performance comparable to strong baselines (Zhang et al., 2024a; Cheng et al., 2025) under the same RGB-only, nowaypoint settings, while maintaining the energy-efficiency advantages obs ... | fair input/data/compute/action matching | p. 6 (4.2. Main Results), p. 6 (4.2. Main Results), p. 14 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.1. Experimental Setups - extractive body cue:** For low-level locomotion, we quantify command tracking and safety using linear and angular velocity tracking errors and the collision rate.
- **p. 5 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** This approach transforms continuous observations into sparse and robust spike events, improving the stability and noise robustness of quadruped locomotion control.
- **p. 8 / A ANN - extractive body cue:** Therefore, SpikeVLA does not simply trade accuracy for efficiency. instead, it achieves higher energy efficiency through a sparse, event-driven computational paradigm.
- **p. 6 / 4.2. Main Results - extractive body cue:** We evaluated SpikeVLA in the VLN-CE-Isaac simulator using the Unitree Go2 platform to assess its transferability to closedloop embodied execution under realistic dynamics and sensor ...
- **p. 8 / A ANN - extractive body cue:** Resource Efficiency Error ↓ Error ↓ Mem(MB)↓Eng(µJ)↓ACEs(106)↓ NaVILA 0.23 0.38 1.20 5.80 161.48 SpikeVLA 0.42 0.29 2.35 0.31 5.53 mance degradation.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 8: Ablation of Actor Network Dimensions. It shows the performance of different Actor network dimensions (A = [128, 128], A = [256, 128], A ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 To address this challenge, previous work has explored efficiency-oriented designs.를 문제로 두고, SpikeVLA consists of three complementary modules.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Architecture), p. 5 (3.4. Spiking Neural Network for Action Policy), p. 5 (3.4. Spiking Neural Network for Action Policy), p. 6 (3.4. Spiking Neural Network for Action Policy) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
