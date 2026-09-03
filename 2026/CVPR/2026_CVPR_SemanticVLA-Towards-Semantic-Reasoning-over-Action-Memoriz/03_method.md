# Method - SemanticVLA: Towards Semantic Reasoning over Action Memorization via Synergistic Explicit Trace and Latent Action Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ni_SemanticVLA_Towards_Semantic_Reasoning_over_Action_Memorization_via_Synergistic_Explicit_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ni_SemanticVLA_Towards_Semantic_Reasoning_over_Action_Memorization_via_Synergistic_Explicit_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Flow Matching Action Decoding), p. 4 (3.1. Semantic Latent Action Tokenizer), p. 5 (3.3. Flow Matching Action Decoding), p. 3 (3.1. Semantic Latent Action Tokenizer), p. 4 (3.1. Semantic Latent Action Tokenizer), p. 3 (3. Method)): Following established architectures [4, 11], the decoder predicts velocity fields through cross-attention between latent and visual features, generating actions via iterative denoising.

## Method Body Digest

- **p. 5 / 3.3. Flow Matching Action Decoding - extractive body cue:** Following established architectures [4, 11], the decoder predicts velocity fields through cross-attention between latent and visual features, generating actions via iterative denoising.
- **p. 4 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** We extract DINOv2 [42] features hvisual from observations ot, ot+H, then combine with trace codebook entry ctrace qtrace through fusion encoder ϕfused enc employing cross-attention, ...
- **p. 5 / 3.3. Flow Matching Action Decoding - extractive body cue:** The VLM processes visual observations and language instructions to generate interpretable trace coordinates and latent action tokens, which are then fused to condition the flow ...
- **p. 3 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** To bridge this gap, we propose leveraging spatial trace priors as explicit supervision to guide latent action learning while excluding language from pretraining.
- **p. 4 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** Visual Decoder DINOv2 Decoder Encoder Cosine Similarity Trace Decoder Ot Ot+H Cross Attention FiLM Ot VQ-VAE Tracet Ot+H Tracet Semantic Fusion Latent Action Figure 2.
- **p. 3 / 3. Method - extractive body cue:** Our approach consists of three stages: (1) Semantic Latent Token Pretraining (Sec.
- **p. 4 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** The training objective of latent action tokenizer LLAT combines: LLAT = La vq + Ltrace recon + Lvisual recon (3) where La vq = ∥sg(ϕfused ...
- **p. 3 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** Given trace τ = (p1, . . . , pL) where pi = (ui, vi) ∈[0, 1]2, we train encoder ϕtrace enc and decoder ϕtrace ...

## Design Rationale

- **p. 3 / 3. Method - extractive body cue:** Our approach consists of three stages: (1) Semantic Latent Token Pretraining (Sec.
- **p. 2 / 1. Introduction - extractive body cue:** By bridging VLM reasoning and action control through semantically explicit trace and compact latent action tokens, our approach enables genuine reasoning rather than action memorization.
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce SemanticVLA, a dual-path reasoning framework that synergistically combines explicit trace reasoning and latent action planning.

## Source Evidence Cues

- **p. 5 / 3.3. Flow Matching Action Decoding - extractive body cue:** Following established architectures [4, 11], the decoder predicts velocity fields through cross-attention between latent and visual features, generating actions via iterative denoising.
- **p. 4 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** We extract DINOv2 [42] features hvisual from observations ot, ot+H, then combine with trace codebook entry ctrace qtrace through fusion encoder ϕfused enc employing cross-attention, ...
- **p. 5 / 3.3. Flow Matching Action Decoding - extractive body cue:** The VLM processes visual observations and language instructions to generate interpretable trace coordinates and latent action tokens, which are then fused to condition the flow ...
- **p. 3 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** To bridge this gap, we propose leveraging spatial trace priors as explicit supervision to guide latent action learning while excluding language from pretraining.
- **p. 4 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** Visual Decoder DINOv2 Decoder Encoder Cosine Similarity Trace Decoder Ot Ot+H Cross Attention FiLM Ot VQ-VAE Tracet Ot+H Tracet Semantic Fusion Latent Action Figure 2.
- **p. 3 / 3. Method - extractive body cue:** Our approach consists of three stages: (1) Semantic Latent Token Pretraining (Sec.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Following established architectures [4, 11], the decoder predicts velocity fields through cross-attention between latent and visual features, generating actions via iterative denoising. | p. 5 (3.3. Flow Matching Action Decoding), p. 4 (3.1. Semantic Latent Action Tokenizer) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We extract DINOv2 [42] features hvisual from observations ot, ot+H, then combine with trace codebook entry ctrace qtrace through fusion encoder ϕfused ... | p. 4 (3.1. Semantic Latent Action Tokenizer), p. 5 (3.3. Flow Matching Action Decoding) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | The VLM processes visual observations and language instructions to generate interpretable trace coordinates and latent action tokens, which are then fused to ... | p. 5 (3.3. Flow Matching Action Decoding), p. 3 (3.1. Semantic Latent Action Tokenizer) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** The training objective of latent action tokenizer LLAT combines: LLAT = La vq + Ltrace recon + Lvisual recon (3) where La vq = ∥sg(ϕfused ...
- **p. 3 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** Given trace τ = (p1, . . . , pL) where pi = (ui, vi) ∈[0, 1]2, we train encoder ϕtrace enc and decoder ϕtrace ...
- **p. 4 / 3.2. VLM Co-training with Trace and Latent Action - extractive body cue:** Given observation ot and instruction ℓt, the VLM autoregressively predicts waypoints: p(τ / ot, ℓt) = L Y j=1 p(pj / ot, ℓt, τ<j) (4) ...
- **p. 5 / 3.3. Flow Matching Action Decoding - extractive body cue:** For the final stage, we fine-tune end-to-end on robot demonstrations with the combined objective: Lfinetune = λVLMLVLM + Lflow (7) where λVLM provides weak supervision ...
- **p. 3 / 3. Method - extractive body cue:** 3.2), where both pathways mutually reinforce through joint optimization; and (3) Flow Matching Action Decoding (Sec.
- **p. 5 / 3.4. Training Recipe - extractive body cue:** Finally in Stage 3, we fine-tune the complete model end-to-end on downstream benchmarks, enabling flow matching action decoding while preserving VLM reasoning through weak regularization.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.1. Semantic Latent Action Tokenizer), p. 3 (3.1. Semantic Latent Action Tokenizer), p. 4 (3.2. VLM Co-training with Trace and Latent Action), p. 5 (3.3. Flow Matching Action Decoding).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | latent, action, guidance, obtain, hidden, states, hqN, VLM, final, layer, encoding, multimodal, reasoning, over | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | latent, action, guidance, obtain, hidden, states, hqN, VLM, final, layer | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | consists, three, stages, Semantic, Latent, Token, Pretraining, Sec, bridging, VLM | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | training, objective, latent, action, tokenizer, LLAT, combines, Ltrace, recon, Lvisual | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.3. Flow Matching Action Decoding - extractive body cue:** For latent action guidance, we obtain hidden states Ea = {hq1, . . . , hqN } from the VLM's final layer, encoding multimodal reasoning ...
- **p. 5 / 3.3. Flow Matching Action Decoding - extractive body cue:** The VLM processes visual observations and language instructions to generate interpretable trace coordinates and latent action tokens, which are then fused to condition the flow ...
- **p. 4 / 3.2. VLM Co-training with Trace and Latent Action - extractive body cue:** Given observation ot and instruction ℓt, the VLM autoregressively predicts waypoints: p(τ / ot, ℓt) = L Y j=1 p(pj / ot, ℓt, τ<j) (4) ...
- **p. 4 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** Stage 2 grounds them in visual observations, with dual reconstruction of trace and visual representations producing latent actions with both spatial and visual semantics. scene ...
- **p. 3 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** To bridge this gap, we propose leveraging spatial trace priors as explicit supervision to guide latent action learning while excluding language from pretraining.
- **p. 2 / 1. Introduction - extractive body cue:** This synergy enables trace to leverage VLM's compositional reasoning for structured waypoint generation, while latent tokens learn compact, semantically-rich visuomotor primitives by fusing trace intension ...
- **p. 2 / 1. Introduction - extractive body cue:** Recent studies reveal critical brittleness under instruction rephrasing [17, 18] and sharp performance drops on reasoning-intensive tasks [35, 49]-VLAs succeed at direct instructions like "place ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | To obtain dense spatial annotations between keyframes, we apply CoTracker [23] for interpolation, ensuring temporally-aligned trace sequences covering complete manipulation trajectories. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | After generating trace τ, the VLM predicts a sequence of latent action tokens for action chunking: p(q1:N / ot, ℓt, τ) = ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Following established protocols [27], we finetune independently per suite on 16 H200 GPUs for 30K steps with batch size 128 and action ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Semantic Latent Action Tokenizer - extractive body cue:** To bridge this gap, we propose leveraging spatial trace priors as explicit supervision to guide latent action learning while excluding language from pretraining.
- **p. 3 / 3. Method - extractive body cue:** Our approach consists of three stages: (1) Semantic Latent Token Pretraining (Sec.
- **p. 5 / 3.4. Training Recipe - extractive body cue:** In Stage 1, we pretrain the semantic latent action tokenizer on TraceX-240K for 50K steps with batch size 512, learning clean geometric primitives without language ...
- **p. 5 / 3.4. Training Recipe - extractive body cue:** In Stage 2, we co-train the VLM to jointly predict trace coordinates and latent action tokens on the same dataset for 100K steps with batch ...
- **p. 4 / 3.2. VLM Co-training with Trace and Latent Action - extractive body cue:** To enable latent action prediction, we augment the VLM vocabulary with special tokens {ACT_1, ..., ACT_K} indexing into the pretrained codebook from Section 3.1.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Following, established, architectures, decoder, predicts, velocity, fields, through, cross-attention, between, latent, visual, features, generating, actions, iterative, denoising, extract, DINOv2, hvisual.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Our experiments validate three core properties: Effectiveness (Section 4.1, 4.2) competitive task success rates on simulation benchmarks and real-world deployments; Robustness (Section ... | p. 5 (4. Experiments), p. 6 (4.1. Simulation Benchmarks) |
| Action / skill decoding | As shown in Table 1, SemanticVLA achieves 97.0% average success rate, outperforming strong baselines across task categories. | p. 6 (4.1. Simulation Benchmarks), p. 6 (4.1. Simulation Benchmarks) |
| Receding execution / feedback | As shown in Table 1, SemanticVLA achieves 97.0% average success rate, outperforming strong baselines across task categories. | p. 6 (4.1. Simulation Benchmarks), p. 6 (4.1. Simulation Benchmarks) |

## Failure and Ablation Link

- **p. 8 / 4.4. Explicit Trace-Guided Latent Action Learning - extractive body cue:** More critically, to isolate the effect of trace-guided pretraining, we conduct a controlled ablation comparing our latent tokens against UniVLA's-both trained without explicit trace reasoning.
- **p. 7 / 4.4. Explicit Trace-Guided Latent Action Learning - extractive body cue:** To validate that trace guidance produces semanticallygrounded latent tokens beyond architectural benefits, we conduct ablations on LIBERO instruction rephrasing with three variants: SemanticVLA with full ...
- **p. 8 / 4.5. Latent Tokens Stabilize Trace Execution - extractive body cue:** Our ablation without laVisual 58 14 Task Language Success Rate (%) 56 53 29 35 51 11 30 33 48 8 27 29 46 HAMSTER ...
- **p. 6 / 4.2. Real-world Robotics Evaluation - extractive body cue:** We evaluate two complementary categories with 20 rollouts per task across 5 variants that vary objects, positions and scene layouts.
- **p. 7 / 4.3. Instruction Variance Robustness - extractive body cue:** The evaluation settings include paraphrased variants with appearance-based references such as "orange object" instead of "carrot", negation phrases like "not the towel", and commonsense cues ...
- **p. 6 / 4.1. Simulation Benchmarks - extractive body cue:** Our trace-guided latent pretraining provides explicit spatial semantics beyond UniVLA and VQ-VLA, whose latents lack geometric scaffolding and rely solely on visual reconstruction or raw ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. SemanticVLA Overview. Current VLA models struggle with instruction variations and reasoning-intensive tasks, often mem- orizing patterns rather than understanding semantics. We introduce a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.3. Flow Matching Action Decoding), p. 4 (3.1. Semantic Latent Action Tokenizer), p. 5 (3.3. Flow Matching Action Decoding), p. 3 (3.1. Semantic Latent Action Tokenizer), p. 4 (3.1. Semantic Latent Action Tokenizer), p. 3 (3. Method), objective p. 4 (3.1. Semantic Latent Action Tokenizer), p. 3 (3.1. Semantic Latent Action Tokenizer), p. 4 (3.2. VLM Co-training with Trace and Latent Action), p. 5 (3.3. Flow Matching Action Decoding), p. 3 (3. Method), p. 5 (3.4. Training Recipe), temporal p. 5 (3.4. Training Recipe), p. 4 (3.2. VLM Co-training with Trace and Latent Action), p. 5 (3.3. Flow Matching Action Decoding), p. 6 (4.1. Simulation Benchmarks), p. 6 (4.2. Real-world Robotics Evaluation), p. 3 (3.1. Semantic Latent Action Tokenizer).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
