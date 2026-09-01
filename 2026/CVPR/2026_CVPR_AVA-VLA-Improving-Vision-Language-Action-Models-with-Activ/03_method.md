# Method - AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. AVA-VLA Framework), p. 3 (3.1. Preliminaries), p. 3 (3.2. AVA-VLA Framework), p. 5 (3.3. Active Visual Attention), p. 4 (3.2. AVA-VLA Framework), p. 5 (3.4. Training and Inference Procedure)): Then the AVA module combines this recurrent state with textconditioned visual features from the current observation to generate soft importance scores, which modulate the visual attention matrices throughout the backbone ...

## Method Body Digest

- **p. 4 / 3.2. AVA-VLA Framework - extractive body cue:** Then the AVA module combines this recurrent state with textconditioned visual features from the current observation to generate soft importance scores, which modulate the visual ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** A typical VLA model Pθ, parameterized by θ, consists of four main components: a Large-Language-Model (LLM) backbone M, a vision encoder E, a language tokenizer ...
- **p. 3 / 3.2. AVA-VLA Framework - extractive body cue:** To utilize the recurrent state, we introduce the active visual attention module by quantifying the importance of visual tokens and dynamically modulating the processing of ...
- **p. 5 / 3.3. Active Visual Attention - extractive body cue:** Therefore, the proposed AVA module uses the recurrent state and current visual observation to calculate soft weights to guide the VLA model to filter and ...
- **p. 4 / 3.2. AVA-VLA Framework - extractive body cue:** Moreover, in order to preserve the rich historical information, we use this recurrent state rt-1 for action placeholder [20, 23] embedding initialization, i.e., pt = ...
- **p. 5 / 3.4. Training and Inference Procedure - extractive body cue:** Training such a recurrent model ideally requires backpropagation through time over the entire trajectory to capture long-term dependencies.
- **p. 5 / 3.4. Training and Inference Procedure - extractive body cue:** However, given the substantial memory constraint and computational cost of modern VLA backbones, performing the full backpropagation through time is computationally prohibitive [34].
- **p. 5 / 3.4. Training and Inference Procedure - extractive body cue:** Visual tokens with low importance scores can be pruned to reduce the computational cost of the LLM backbone.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models.
- **p. 2 / 1. Introduction - extractive body cue:** To our knowledge, it is the first VLA framework to explicitly address this limitation via a POMDP-inspired approach. • We introduce an Active Visual Attention ...
- **p. 3 / 3. Methods - extractive body cue:** In this section, we present our proposed VLA method.

## Source Evidence Cues

- **p. 4 / 3.2. AVA-VLA Framework - extractive body cue:** Then the AVA module combines this recurrent state with textconditioned visual features from the current observation to generate soft importance scores, which modulate the visual ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** A typical VLA model Pθ, parameterized by θ, consists of four main components: a Large-Language-Model (LLM) backbone M, a vision encoder E, a language tokenizer ...
- **p. 3 / 3.2. AVA-VLA Framework - extractive body cue:** To utilize the recurrent state, we introduce the active visual attention module by quantifying the importance of visual tokens and dynamically modulating the processing of ...
- **p. 5 / 3.3. Active Visual Attention - extractive body cue:** Therefore, the proposed AVA module uses the recurrent state and current visual observation to calculate soft weights to guide the VLA model to filter and ...
- **p. 4 / 3.2. AVA-VLA Framework - extractive body cue:** Moreover, in order to preserve the rich historical information, we use this recurrent state rt-1 for action placeholder [20, 23] embedding initialization, i.e., pt = ...
- **p. 5 / 3.4. Training and Inference Procedure - extractive body cue:** Training such a recurrent model ideally requires backpropagation through time over the entire trajectory to capture long-term dependencies.
- **Detected method headings:** 3. Methods (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Then the AVA module combines this recurrent state with textconditioned visual features from the current observation to generate soft importance scores, which ... | p. 4 (3.2. AVA-VLA Framework), p. 3 (3.1. Preliminaries) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | A typical VLA model Pθ, parameterized by θ, consists of four main components: a Large-Language-Model (LLM) backbone M, a vision encoder E, ... | p. 3 (3.1. Preliminaries), p. 3 (3.2. AVA-VLA Framework) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To utilize the recurrent state, we introduce the active visual attention module by quantifying the importance of visual tokens and dynamically modulating ... | p. 3 (3.2. AVA-VLA Framework), p. 5 (3.3. Active Visual Attention) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Training and Inference Procedure - extractive body cue:** However, given the substantial memory constraint and computational cost of modern VLA backbones, performing the full backpropagation through time is computationally prohibitive [34].
- **p. 5 / 3.4. Training and Inference Procedure - extractive body cue:** Visual tokens with low importance scores can be pruned to reduce the computational cost of the LLM backbone.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3.4. Training and Inference Procedure), p. 5 (3.4. Training and Inference Procedure).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | POMDP, framework, optimal, policy, timestep, should, conditioned, only, current, observation, belief, state, bt-1, captures | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | POMDP, framework, optimal, policy, timestep, should, conditioned, only, current, observation | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, threefold, novel, AVA-VLA, framework, solve, critical, limitation, lacking, historical | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | However, given, substantial, memory, constraint, computational, cost, modern, VLA, backbones | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.2. AVA-VLA Framework - extractive body cue:** In a POMDP framework, the optimal policy at timestep t should be conditioned not only on the current observation xt but also on a belief ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** (1) Recent representative VLA models, such as OpenVLAOFT [20] and its variant [23], map the output hidden states into an executable action chunk At = ...
- **p. 4 / 3.2. AVA-VLA Framework - extractive body cue:** Therefore, the forward pass at timestep t, incorporating the AVA module and statebased initialization, is formulated as: At = Q(Mparallel(zt I, V(xt, rt-1), zt S, ...
- **p. 4 / 3.2. AVA-VLA Framework - extractive body cue:** Attn Attn Attn Attn Attn Attn Attn Attn Tokenizer Action Head Action Head Attn Attn Attn Attn Attn Attn Attn Attn Vision Encoder Vision Encoder ...
- **p. 2 / 1. Introduction - extractive body cue:** Therefore, the proposed AVA-VLA framework does not rely solely on the current observation but learns to explicitly condition the action prediction on the recurrent state.
- **p. 1 / 1. Introduction - extractive body cue:** This implicitly formulates robot manipulation as a Markov Decision Process (MDP) [16, 31], where actions are generated from the current visual observation, assumed to represent ...
- **p. 1 / 1. Introduction - extractive body cue:** VLA model VLA model Observation T-1 Observation T VLA model VLA model Observation T-1 Observation T Action T-1 Action T-1 Action T Action T Vanilla ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | For each timestep t in this sequence, we calculate the action chunk prediction loss using the Mean Absolute Error (MAE): Lt,n = ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Specifically, at time step t, let the total sequence length be Lt o, we denote the attention score of the mth layer ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Therefore, the total loss of one training batch is the sum of the prediction loss and penalty loss of N truncated sequences: ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.4. Training and Inference Procedure - extractive body cue:** Training such a recurrent model ideally requires backpropagation through time over the entire trajectory to capture long-term dependencies.
- **p. 5 / 3.4. Training and Inference Procedure - extractive body cue:** Therefore, the total loss of one training batch is the sum of the prediction loss and penalty loss of N truncated sequences: Ltotal = XN ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, AVA, module, combines, recurrent, state, textconditioned, visual, features, current, observation, generate, soft, importance, scores, modulate, attention, matrices, throughout, backbone.
- **Relevant PDF headings:** 3. Methods (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We conduct experiments on three challenging settings: the LIBERO [28] and CALVIN [31] benchmarks for evaluation in simulation environments, and a real-world ... | p. 5 (4.1. Experimental Setup), p. 5 (4. Experiments) |
| Action / skill decoding | The results show that the proposed AVA-VLA framework comprehensively outperforms baseline methods across all tasks. | p. 7 (4.2. Evaluation Results), p. 7 (4.2. Evaluation Results) |
| Receding execution / feedback | Each component alone improves over OpenVLA-OFT, and their combination achieves the best overall performance. | p. 7 (4.3. Ablation Studies), p. 7 (4.2. Evaluation Results) |

## Failure and Ablation Link

- **p. 5 / 4. Experiments - extractive body cue:** Additionally, we conduct a comprehensive ablation study and analysis to validate the effectiveness of our approach.
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** To validate their individual effectiveness, we conduct ablation experiments on the LIBERO benchmark.
- **p. 8 / 4.4. Analysis - extractive body cue:** Ablation study on the two key components in the AVA-VLA framework.
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** Ablation study on the model backbones.
- **p. 8 / 4.4. Analysis - extractive body cue:** Furthermore, a direct comparison in Figure 1 reveals that while the vanilla OpenVLA-OFT baseline fails to localize the task-relevant region across viewpoints, AVAVLA maintains a ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (a) Visualized comparison of the proposed AVA-VLA framework and vanilla VLAs. (b) Qualitative comparison of vi- sual focus from two viewpoints while executing ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Due to space limitations, implementation details are provided in Appendix A.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. AVA-VLA Framework), p. 3 (3.1. Preliminaries), p. 3 (3.2. AVA-VLA Framework), p. 5 (3.3. Active Visual Attention), p. 4 (3.2. AVA-VLA Framework), p. 5 (3.4. Training and Inference Procedure), objective p. 5 (3.4. Training and Inference Procedure), p. 5 (3.4. Training and Inference Procedure), temporal p. 5 (3.4. Training and Inference Procedure), p. 4 (3.3. Active Visual Attention), p. 3 (3.2. AVA-VLA Framework), p. 3 (3.2. AVA-VLA Framework), p. 5 (3.4. Training and Inference Procedure), p. 4 (3.2. AVA-VLA Framework).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
