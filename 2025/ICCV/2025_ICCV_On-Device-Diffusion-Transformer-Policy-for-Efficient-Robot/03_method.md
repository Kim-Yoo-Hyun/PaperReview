# Method - On-Device Diffusion Transformer Policy for Efficient Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (4.1. Problem Formulation), p. 4 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning), p. 4 (4.3. Prune the Model by Learning), p. 3 (4.1. Problem Formulation)): A diffusion policy πϕ(a/o, g) is trained to imitate the expert's behavior by maximizing the log-likelihood of the action a Diffusion Transformer Observation Encoder x4 action Vision Encoder FFN MHCA ...

## Method Body Digest

- **p. 3 / 4.1. Problem Formulation - extractive body cue:** A diffusion policy πϕ(a/o, g) is trained to imitate the expert's behavior by maximizing the log-likelihood of the action a Diffusion Transformer Observation Encoder x4 ...
- **p. 4 / 4.3. Prune the Model by Learning - extractive body cue:** To address this, a common approach is a two-stage pruning process: first determine the mask M (by minimizing the loss L with a given criterion), ...
- **p. 5 / 4.3. Prune the Model by Learning - extractive body cue:** Then, two noised actions at and at+k are fed into the Student Model fϕ and the Target Model fϕ⋆to calculate the consistency loss.
- **p. 5 / 4.3. Prune the Model by Learning - extractive body cue:** xN Action Action Moving Aerage Target Model Transformer Block Transformer Block Transformer Block Transformer Block Pruned Model MHCA Transformer Block Transformer Block Transformer Block FFN ...
- **p. 4 / 4.3. Prune the Model by Learning - extractive body cue:** To address this issue, we propose to use a single-stage pruning method [10], where the mask M and weight ˆϕ are jointly optimized to minimize ...
- **p. 3 / 4.1. Problem Formulation - extractive body cue:** Given the demonstration T , a trajectory τ ∈T is a sequence of observation o and robot action a, denoted as τ = {(o1, a1), ...
- **p. 7 / Method - extractive body cue:** Performance comparison of LightDP compressed models with varying depth and inference steps.
- **p. 4 / 4.3. Prune the Model by Learning - extractive body cue:** Conventionally, the pruning process is formulated as an optimization problem to minimize the loss L after pruning, which can be formulated as minM,π ˆ ϕ ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** In this work, we introduce a novel framework named LightDP for Diffusion Policies that enables models to achieve real-time generation on mobile devices.
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We present a novel framework for Diffusion Policies to obtain the efficient diffusion transformer that achieves real-time action ...
- **p. 5 / 4.3. Prune the Model by Learning - extractive body cue:** In the left figure, we present the consistency distillation pipeline adopted in our method.

## Source Evidence Cues

- **p. 3 / 4.1. Problem Formulation - extractive body cue:** A diffusion policy πϕ(a/o, g) is trained to imitate the expert's behavior by maximizing the log-likelihood of the action a Diffusion Transformer Observation Encoder x4 ...
- **p. 4 / 4.3. Prune the Model by Learning - extractive body cue:** To address this, a common approach is a two-stage pruning process: first determine the mask M (by minimizing the loss L with a given criterion), ...
- **p. 5 / 4.3. Prune the Model by Learning - extractive body cue:** Then, two noised actions at and at+k are fed into the Student Model fϕ and the Target Model fϕ⋆to calculate the consistency loss.
- **p. 5 / 4.3. Prune the Model by Learning - extractive body cue:** xN Action Action Moving Aerage Target Model Transformer Block Transformer Block Transformer Block Transformer Block Pruned Model MHCA Transformer Block Transformer Block Transformer Block FFN ...
- **p. 4 / 4.3. Prune the Model by Learning - extractive body cue:** To address this issue, we propose to use a single-stage pruning method [10], where the mask M and weight ˆϕ are jointly optimized to minimize ...
- **p. 3 / 4.1. Problem Formulation - extractive body cue:** Given the demonstration T , a trajectory τ ∈T is a sequence of observation o and robot action a, denoted as τ = {(o1, a1), ...
- **p. 7 / Method - extractive body cue:** Performance comparison of LightDP compressed models with varying depth and inference steps.
- **Detected method headings:** 2.2. Network Pruning for Diffusion Models (p. 2); 4. Method (p. 3); 4.3. Prune the Model by Learning (p. 4); 5.3. Evaluation on DiffusionPolicy Transformer (p. 6); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | A diffusion policy πϕ(a/o, g) is trained to imitate the expert's behavior by maximizing the log-likelihood of the action a Diffusion Transformer ... | p. 3 (4.1. Problem Formulation), p. 4 (4.3. Prune the Model by Learning) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | To address this, a common approach is a two-stage pruning process: first determine the mask M (by minimizing the loss L with ... | p. 4 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Then, two noised actions at and at+k are fed into the Student Model fϕ and the Target Model fϕ⋆to calculate the consistency ... | p. 5 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4.3. Prune the Model by Learning - extractive body cue:** To address this issue, we propose to use a single-stage pruning method [10], where the mask M and weight ˆϕ are jointly optimized to minimize ...
- **p. 4 / 4.3. Prune the Model by Learning - extractive body cue:** Conventionally, the pruning process is formulated as an optimization problem to minimize the loss L after pruning, which can be formulated as minM,π ˆ ϕ ...
- **p. 3 / 4.1. Problem Formulation - extractive body cue:** A diffusion policy πϕ(a/o, g) is trained to imitate the expert's behavior by maximizing the log-likelihood of the action a Diffusion Transformer Observation Encoder x4 ...
- **p. 5 / 4.3. Prune the Model by Learning - extractive body cue:** Then, two noised actions at and at+k are fed into the Student Model fϕ and the Target Model fϕ⋆to calculate the consistency loss.
- **p. 5 / 4.3. Prune the Model by Learning - extractive body cue:** The Target Model is updated by the Student Model with a momentum update.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (4.3. Prune the Model by Learning), p. 4 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | diffusion, policy, trained, imitate, expert, behavior, maximizing, log-likelihood, action, Transformer, Observation, Encoder, Vision, FFN | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | diffusion, policy, trained, imitate, expert, behavior, maximizing, log-likelihood, action, Transformer | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | introduce, novel, framework, named, LightDP, Diffusion, Policies, enables, models, achieve | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | address, issue, single-stage, pruning, where, mask, weight, jointly, optimized, minimize | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 4.1. Problem Formulation - extractive body cue:** A diffusion policy πϕ(a/o, g) is trained to imitate the expert's behavior by maximizing the log-likelihood of the action a Diffusion Transformer Observation Encoder x4 ...
- **p. 3 / 4.1. Problem Formulation - extractive body cue:** Given the demonstration T , a trajectory τ ∈T is a sequence of observation o and robot action a, denoted as τ = {(o1, a1), ...
- **p. 5 / 4.3. Prune the Model by Learning - extractive body cue:** xN Action Action Moving Aerage Target Model Transformer Block Transformer Block Transformer Block Transformer Block Pruned Model MHCA Transformer Block Transformer Block Transformer Block FFN ...
- **p. 4 / 4.3. Prune the Model by Learning - extractive body cue:** If the i-th block is dropped during training, we make its output identical to its input (an identity mapping)., which could be formulated as: x_ ...
- **p. 2 / 3. Preliminaries - extractive body cue:** Forward Diffusion Process: Noise is progressively added to the input data, transforming it into a noise14074
- **p. 1 / 1. Introduction - extractive body cue:** First, we provide an analysis of two Diffusion Policies named DiffusionPolicy Transformer (DP-T) [8] and MDT-V [36].
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, recent work by DeeR-VLA [49] introduces a multi-exit architecture built on the Roboflamingo framework [26], enabling dynamic termination of the computation ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | We provide a comprehensive analysis of these policies' computational cost and memory footprint. • We integrate the pruning and step distillation process ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Likewise, employing consistency distillation (MDT-V w/CD) considerably reduces the GFLOPs and latency with only minimal reduction in the average rollout length. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | We provide a comprehensive analysis of these policies' computational cost and memory footprint. • We integrate the pruning and step distillation process ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Since MDT-V consists of 4-layer TransformerEncoder and 4-layer TransformerDecoder, we keep the number of encoder layers the same as the decoder layers, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 4.1. Problem Formulation - extractive body cue:** A diffusion policy πϕ(a/o, g) is trained to imitate the expert's behavior by maximizing the log-likelihood of the action a Diffusion Transformer Observation Encoder x4 ...
- **p. 4 / 4.3. Prune the Model by Learning - extractive body cue:** To address this, a common approach is a two-stage pruning process: first determine the mask M (by minimizing the loss L with a given criterion), ...
- **p. 7 / Method - extractive body cue:** Performance comparison of LightDP compressed models with varying depth and inference steps.
- **p. 6 / 5.2. Implementation Details - extractive body cue:** Then, we converted the model trained on GPU to Core ML model format (mlpackage, based on Apple's ml-stable-diffusion) and measured latency in Xcode Instruments on ...
- **p. 4 / 4.2. Latency Analysis of Diffusion Policies - extractive body cue:** IE: Image Encoder, DT: Diffusion Transformer, GLE: Goal Language Encoder, NFE is short for the number of score function evaluations, i.e., inference steps., M: Million, ...
- **p. 3 / 4.1. Problem Formulation - extractive body cue:** A diffusion policy πϕ(a/o, g) is trained to imitate the expert's behavior by maximizing the log-likelihood of the action a Diffusion Transformer Observation Encoder x4 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** diffusion, policy, trained, imitate, expert, behavior, maximizing, log-likelihood, action, Transformer, Observation, Encoder, Vision, FFN, MHCA, Block, image, Linear, Perceiver, Goal.
- **Relevant PDF headings:** 2.2. Network Pruning for Diffusion Models (p. 2); 4. Method (p. 3); 4.3. Prune the Model by Learning (p. 4); 5.3. Evaluation on DiffusionPolicy Transformer (p. 6); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | The benchmark dataset is split into four manipulation environments, A, B, C, and D. | p. 6 (5.1. Benchmarks and Evaluation Metrics), p. 8 (5.6. Qualitative Results) |
| Action / skill decoding | Table 2. Performance comparison of LightDP compressed models with varying depth and inference steps. All models are trained on the same Push-T ... | p. 7 (Figure/Table caption), p. 5 (5. Experiments) |
| Receding execution / feedback | The results show that through our method, the pruned model can achieve a comparable success rate with the vanilla model. | p. 6 (5.3. Evaluation on DiffusionPolicy Transformer), p. 6 (5.3. Evaluation on DiffusionPolicy Transformer) |

## Failure and Ablation Link

- **p. 8 / 5.6. Qualitative Results - extractive body cue:** Ablation study on the effect of the proposed learnable pruning and step distillation based on MDT-V, the performance is evaluated on the CALVIN D→D task ...
- **p. 7 / 5.4. Evaluation on MDT-V - extractive body cue:** In contrast, the pruned variants show a noticeable decline in performance, where MDTV/E1-D1, for instance, achieves only 92.3% initially and drops to 61.4%, with a ...
- **p. 7 / 5.6. Qualitative Results - extractive body cue:** In the Push-T task, the pruned model successfully pushed the T-shaped block into the goal zone, without any failure in the manipu14079
- **p. 4 / 4.2. Latency Analysis of Diffusion Policies - extractive body cue:** For DP-T, the network consists of two major components, the image encoder employs a ResNet18 model for converting the input image into embedding as the ...
- **p. 4 / 4.2. Latency Analysis of Diffusion Policies - extractive body cue:** Components IE DT Latency (ms) 1.28 0.906 Parameter (M) 11.2 8.97 NFE 1 100 Total Latency (ms) 1.28 90.6 Latency (ms) 1.28 0.68 Parameter (M) ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. The network architecture of MDT-V model. The model consists of three main components: the observation encoder E, the goal encoder G, and the ...
- **p. 7 / 5.6. Qualitative Results - extractive body cue:** In the Push-T task, the pruned model successfully pushed the T-shaped block into the goal zone, without any failure in the manipu14079

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (4.1. Problem Formulation), p. 4 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning), p. 4 (4.3. Prune the Model by Learning), p. 3 (4.1. Problem Formulation), objective p. 4 (4.3. Prune the Model by Learning), p. 4 (4.3. Prune the Model by Learning), p. 3 (4.1. Problem Formulation), p. 5 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning), temporal p. 2 (1. Introduction), p. 7 (5.5. Ablation Study), p. 3 (3. Preliminaries), p. 3 (3. Preliminaries), p. 1 (Abstract), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
