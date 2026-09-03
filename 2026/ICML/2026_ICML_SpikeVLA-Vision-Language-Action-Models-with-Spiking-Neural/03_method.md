# Method - SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=W86R5sIsxE; PDF retrieval source: https://openreview.net/pdf/27ac3094b9d6afc1c8c39e0ae99418fd937e0219.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Architecture), p. 5 (3.4. Spiking Neural Network for Action Policy), p. 5 (3.4. Spiking Neural Network for Action Policy), p. 6 (3.4. Spiking Neural Network for Action Policy), p. 3 (3.2. Spike Neural Network Vision Encoder), p. 6 (3.4. Spiking Neural Network for Action Policy)): We propose SpikeVLA, an end-to-end spiking VLA architecture for embodied navigation, consisting of a spiking vision encoder (Spike-V), a multimodal spiking language model (Spike-L), and a fully spiking action policy ...

## Method Body Digest

- **p. 3 / 3.1. Architecture - extractive body cue:** We propose SpikeVLA, an end-to-end spiking VLA architecture for embodied navigation, consisting of a spiking vision encoder (Spike-V), a multimodal spiking language model (Spike-L), and ...
- **p. 5 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** We propose an action policy network based on Spiking Neural Networks.
- **p. 5 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** During reinforcement learning, the network is trained using the Proximal Policy Optimization (PPO) algorithm to optimize its parameters.
- **p. 6 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** We train the spiking action policy network using surrogate-gradient spatiotemporal backpropagation, accumulating gradients over discrete timesteps t = 1, . . . , T and ...
- **p. 3 / 3.2. Spike Neural Network Vision Encoder - extractive body cue:** We introduce a recurrent auxiliary state into membrane updates to incrementally correct the input current based on both input changes and emitted spikes, aligning neuron ...
- **p. 6 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** At timestep t, the actor maps the observation st to a policy πθ(· / st) = N(µt, σt) and samples an action at, while the ...
- **p. 4 / 3.3. Multimodal Spiking Large Language Model - extractive body cue:** We project the history frames, the current frame, and the text into a shared latent space and concatenate them into a unified token sequence, which ...
- **p. 6 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** We optimize the policy by maximizing the clipped surrogate objective.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** SpikeVLA consists of three complementary modules.
- **p. 2 / 1. Introduction - extractive body cue:** 1) We propose SpikeVLA, the first VLA framework built on spiking neural networks.
- **p. 3 / 3.2. Spike Neural Network Vision Encoder - extractive body cue:** We propose an SNN-based visual encoder that fuses the current frame with history frames to provide temporal context for time-dependent VLA tasks.

## Source Evidence Cues

- **p. 3 / 3.1. Architecture - extractive body cue:** We propose SpikeVLA, an end-to-end spiking VLA architecture for embodied navigation, consisting of a spiking vision encoder (Spike-V), a multimodal spiking language model (Spike-L), and ...
- **p. 5 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** We propose an action policy network based on Spiking Neural Networks.
- **p. 5 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** During reinforcement learning, the network is trained using the Proximal Policy Optimization (PPO) algorithm to optimize its parameters.
- **p. 6 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** We train the spiking action policy network using surrogate-gradient spatiotemporal backpropagation, accumulating gradients over discrete timesteps t = 1, . . . , T and ...
- **p. 3 / 3.2. Spike Neural Network Vision Encoder - extractive body cue:** We introduce a recurrent auxiliary state into membrane updates to incrementally correct the input current based on both input changes and emitted spikes, aligning neuron ...
- **p. 6 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** At timestep t, the actor maps the observation st to a policy πθ(· / st) = N(µt, σt) and samples an action at, while the ...
- **p. 4 / 3.3. Multimodal Spiking Large Language Model - extractive body cue:** We project the history frames, the current frame, and the text into a shared latent space and concatenate them into a unified token sequence, which ...
- **Detected method headings:** 3. Method (p. 3); 3.1. Architecture (p. 3); 3.3. Multimodal Spiking Large Language Model (p. 4); 3.4. Spiking Neural Network for Action Policy (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | We propose SpikeVLA, an end-to-end spiking VLA architecture for embodied navigation, consisting of a spiking vision encoder (Spike-V), a multimodal spiking language ... | p. 3 (3.1. Architecture), p. 5 (3.4. Spiking Neural Network for Action Policy) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We propose an action policy network based on Spiking Neural Networks. | p. 5 (3.4. Spiking Neural Network for Action Policy), p. 5 (3.4. Spiking Neural Network for Action Policy) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | During reinforcement learning, the network is trained using the Proximal Policy Optimization (PPO) algorithm to optimize its parameters. | p. 5 (3.4. Spiking Neural Network for Action Policy), p. 6 (3.4. Spiking Neural Network for Action Policy) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** We optimize the policy by maximizing the clipped surrogate objective.
- **p. 4 / 3.2. Spike Neural Network Vision Encoder - extractive body cue:** Equation (3) specifies the membrane-potential update for neurons in the l-th layer.
- **p. 4 / 3.2. Spike Neural Network Vision Encoder - extractive body cue:** This mapping is given by the following equations, which convert continuous nonlinear operators into graded updates to improve efficiency and avoid redundant computation. cl[t] = ...
- **p. 3 / 3.1. Architecture - extractive body cue:** SpikeL fuses visual and text tokens and performs event-driven channel-wise sparsification to reduce computational cost (see Section 3.3).
- **p. 3 / 3.1. Architecture - extractive body cue:** Spike-A maps the fused multimodal representation to continuous actions with a fully spiking policy network, achieving stable and robust closed-loop control under low-power constraints (see ...
- **p. 6 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** We train the spiking action policy network using surrogate-gradient spatiotemporal backpropagation, accumulating gradients over discrete timesteps t = 1, . . . , T and ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.2. Spike Neural Network Vision Encoder), p. 4 (3.2. Spike Neural Network Vision Encoder), p. 3 (3.1. Architecture), p. 6 (3.4. Spiking Neural Network for Action Policy), p. 6 (3.4. Spiking Neural Network for Action Policy), p. 3 (3.2. Spike Neural Network Vision Encoder).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | timestep, actor, maps, observation, policy, samples, action, while, critic, estimates, state, value, compute, advantage | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | timestep, actor, maps, observation, policy, samples, action, while, critic, estimates | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | SpikeVLA, consists, three, complementary, modules, first, VLA, framework, built, spiking | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | optimize, policy, maximizing, clipped, surrogate, objective, Equation, specifies, membrane-potential, update | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** At timestep t, the actor maps the observation st to a policy πθ(· / st) = N(µt, σt) and samples an action at, while the ...
- **p. 5 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** To encode continuous observation inputs into discrete spike outputs, we adopt population encoding.
- **p. 6 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** Decoder parameters are updated independently for output populations i = 1, . . . , M corresponding to action dimensions, and encoder parameters [µ(i), σ(i)] ...
- **p. 3 / 3.1. Architecture - extractive body cue:** We propose SpikeVLA, an end-to-end spiking VLA architecture for embodied navigation, consisting of a spiking vision encoder (Spike-V), a multimodal spiking language model (Spike-L), and ...
- **p. 5 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** We propose an action policy network based on Spiking Neural Networks.
- **p. 3 / 3.1. Architecture - extractive body cue:** Spike-A maps the fused multimodal representation to continuous actions with a fully spiking policy network, achieving stable and robust closed-loop control under low-power constraints (see ...
- **p. 4 / 3.2. Spike Neural Network Vision Encoder - extractive body cue:** The output xl[t] is the result of combining the two inputs over time and serves as the updated value at the time step t.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | (4) where F l(·) denotes the nonlinear operator in layer l that takes a single input xl-1[t], and cl[t] denotes the membrane ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | We propose an SNN-based visual encoder that fuses the current frame with history frames to provide temporal context for time-dependent VLA tasks. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | We propose an SNN-based visual encoder that fuses the current frame with history frames to provide temporal context for time-dependent VLA tasks. | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** During reinforcement learning, the network is trained using the Proximal Policy Optimization (PPO) algorithm to optimize its parameters.
- **p. 6 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** We train the spiking action policy network using surrogate-gradient spatiotemporal backpropagation, accumulating gradients over discrete timesteps t = 1, . . . , T and ...
- **p. 6 / 4.2. Main Results - extractive body cue:** SpikeVLA substantially reduces inference cost, lowering GPU memory usage from 16.1 GB to 6.2 GB and achieving an energy metric of E=49.09J, which is approximately ...
- **p. 6 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** We train the spiking action policy network using surrogate-gradient spatiotemporal backpropagation, accumulating gradients over discrete timesteps t = 1, . . . , T and ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** SpikeVLA, end-to-end, spiking, VLA, architecture, embodied, navigation, consisting, vision, encoder, Spike-V, multimodal, language, model, Spike-L, fully, action, policy, network, Spike-A.
- **Relevant PDF headings:** 3. Method (p. 3); 3.1. Architecture (p. 3); 3.3. Multimodal Spiking Large Language Model (p. 4); 3.4. Spiking Neural Network for Action Policy (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Navigation Performance on VLN-CE Benchmarks. | p. 6 (4.2. Main Results), p. 6 (4.1. Experimental Setups) |
| Action / skill decoding | The current results suggest that SpikeVLA achieves performance comparable to strong baselines (Zhang et al., 2024a; Cheng et al., 2025) under the ... | p. 6 (4.2. Main Results), p. 6 (4.2. Main Results) |
| Receding execution / feedback | As shown in Table 2, it achieves a strong and stable navigation performance, maintaining high metric scores compared to NaVILA (Cheng et ... | p. 6 (4.2. Main Results), p. 6 (4.2. Main Results) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: SNN action policy network ablations. The top row compares different spike encoding kernels (Laplacian, Gaussian, Triangular, and IMQ) in terms of reward, linear ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 9: Ablation study of time step T of SNN action policy network. The baseline configuration is marked with ∗.
- **p. 14 / Figure/Table caption - extractive body cue:** Table 8: Ablation study on the Val-Unseen split of R2R-CE and RxR-CE across different modules of the SpikeVLA. T R2R-CE Val Unseen RxR-CE Val Unseen ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 10: Ablation study of population encoding size P. The baseline configuration is marked with ∗.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 7: Ablation study of the population encoding size hyperparameter. It shows the performance of different population encoding dimensions (P = 2, 3, 5) across ...
- **p. 6 / 4.2. Main Results - extractive body cue:** The left side shows a comparison of resource consumption between the different components of SpikeVLA and NaVILA (Cheng et al., 2025), while the right side ...
- **p. 6 / 4.1. Experimental Setups - extractive body cue:** For low-level locomotion, we quantify command tracking and safety using linear and angular velocity tracking errors and the collision rate.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.1. Architecture), p. 5 (3.4. Spiking Neural Network for Action Policy), p. 5 (3.4. Spiking Neural Network for Action Policy), p. 6 (3.4. Spiking Neural Network for Action Policy), p. 3 (3.2. Spike Neural Network Vision Encoder), p. 6 (3.4. Spiking Neural Network for Action Policy), objective p. 6 (3.4. Spiking Neural Network for Action Policy), p. 4 (3.2. Spike Neural Network Vision Encoder), p. 4 (3.2. Spike Neural Network Vision Encoder), p. 3 (3.1. Architecture), p. 3 (3.1. Architecture), p. 6 (3.4. Spiking Neural Network for Action Policy), temporal p. 4 (3.2. Spike Neural Network Vision Encoder), p. 3 (3.2. Spike Neural Network Vision Encoder), p. 3 (3.1. Architecture), p. 4 (3.3. Multimodal Spiking Large Language Model), p. 6 (3.4. Spiking Neural Network for Action Policy), p. 5 (3.3. Multimodal Spiking Large Language Model).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
