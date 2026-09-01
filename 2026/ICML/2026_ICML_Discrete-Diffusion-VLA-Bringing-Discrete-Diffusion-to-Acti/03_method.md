# Method - Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=c3BVcHcSiR; PDF retrieval source: https://openreview.net/pdf/7c6c1101cef920f79b251ef422b6399d7e8f4ae1.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.5. Adaptive Decoding and Secondary Re-Masking), p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 4 (3.4. Algorithmic Pipeline), p. 4 (3.3. Architecture of Discrete Diffusion VLA), p. 5 (3.5. Adaptive Decoding and Secondary Re-Masking)): As illustrated above, the inference pipeline starts from a fully masked action chunk a1 = ML with mask ratio γ1=1, and then performs T refinement steps with a monotone schedule ...

## Method Body Digest

- **p. 5 / 3.5. Adaptive Decoding and Secondary Re-Masking - extractive PDF cue:** As illustrated above, the inference pipeline starts from a fully masked action chunk a1 = ML with mask ratio γ1=1, and then performs T refinement ...
- **p. 3 / 3.1. Overview - extractive PDF cue:** Given image observations (single- or multi-view) and a language instruction, the model extends a VLM backbone to generate actions via discrete diffusion.
- **p. 3 / 3.1. Overview - extractive PDF cue:** A unified transformer jointly attends to visual features, language embeddings, and partially unmasked action tokens, progressively demasking remaining masked action tokens according to a diffusion ...
- **p. 4 / 3.4. Algorithmic Pipeline - extractive PDF cue:** No additional loss terms, auxiliary objectives, or special training procedures are involved.
- **p. 4 / 3.3. Architecture of Discrete Diffusion VLA - extractive PDF cue:** All tokens pass through the unified transformer, with hidden states at action positions projected to a 256-way vocabulary via a shared classification head.
- **p. 5 / 3.5. Adaptive Decoding and Secondary Re-Masking - extractive PDF cue:** At step t, the model yields perposition posteriors pθ(at-1 / at, c) instantiating Eq.
- **p. 4 / 3.2. Formulation of Discrete Diffusion over Actions - extractive PDF cue:** In implementation, we follow mask diffusion formulations and collapse the multi-step chain into a single masked-token prediction objective.
- **p. 3 / 3.1. Overview - extractive PDF cue:** This formulation eliminates the competing gradients introduced by a separate diffusion loss, preserving VLM priors while unifying perception, instruction grounding, and action denoising within a ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions are threefold: 1) We introduce the first discrete diffusion VLA, unifying action generation with vision-language modeling in one transformer, demonstrating superior ...
- **p. 2 / 1. Introduction - extractive PDF cue:** 2) We develop an adaptive decoding strategy with secondary re-masking that enables confidence-based actiontoken decoding and robust error correction, improving both effectiveness and efficiency.
- **p. 1 / 1. Introduction - extractive PDF cue:** Drawing on recent advances in discrete diffusion and discrete flow-matching for language and multi-modal generation (Nie et al., 2025a; Shi et al., 2024b; Gat et ...

## Source Evidence Cues

- **p. 5 / 3.5. Adaptive Decoding and Secondary Re-Masking - extractive PDF cue:** As illustrated above, the inference pipeline starts from a fully masked action chunk a1 = ML with mask ratio γ1=1, and then performs T refinement ...
- **p. 3 / 3.1. Overview - extractive PDF cue:** Given image observations (single- or multi-view) and a language instruction, the model extends a VLM backbone to generate actions via discrete diffusion.
- **p. 3 / 3.1. Overview - extractive PDF cue:** A unified transformer jointly attends to visual features, language embeddings, and partially unmasked action tokens, progressively demasking remaining masked action tokens according to a diffusion ...
- **p. 4 / 3.4. Algorithmic Pipeline - extractive PDF cue:** No additional loss terms, auxiliary objectives, or special training procedures are involved.
- **p. 4 / 3.3. Architecture of Discrete Diffusion VLA - extractive PDF cue:** All tokens pass through the unified transformer, with hidden states at action positions projected to a 256-way vocabulary via a shared classification head.
- **p. 5 / 3.5. Adaptive Decoding and Secondary Re-Masking - extractive PDF cue:** At step t, the model yields perposition posteriors pθ(at-1 / at, c) instantiating Eq.
- **Detected method headings:** 2.1. Vision-Language-Action Models (p. 2); 2.2. Discrete Diffusion Models (p. 2); 3. Discrete Diffusion VLA Model (p. 3); 3.3. Architecture of Discrete Diffusion VLA (p. 4); 3.4. Algorithmic Pipeline (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | As illustrated above, the inference pipeline starts from a fully masked action chunk a1 = ML with mask ratio γ1=1, and then ... | p. 5 (3.5. Adaptive Decoding and Secondary Re-Masking), p. 3 (3.1. Overview) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Given image observations (single- or multi-view) and a language instruction, the model extends a VLM backbone to generate actions via discrete diffusion. | p. 3 (3.1. Overview), p. 3 (3.1. Overview) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | A unified transformer jointly attends to visual features, language embeddings, and partially unmasked action tokens, progressively demasking remaining masked action tokens according ... | p. 3 (3.1. Overview), p. 4 (3.4. Algorithmic Pipeline) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Formulation of Discrete Diffusion over Actions - extractive PDF cue:** In implementation, we follow mask diffusion formulations and collapse the multi-step chain into a single masked-token prediction objective.
- **p. 4 / 3.4. Algorithmic Pipeline - extractive PDF cue:** No additional loss terms, auxiliary objectives, or special training procedures are involved.
- **p. 3 / 3.1. Overview - extractive PDF cue:** This formulation eliminates the competing gradients introduced by a separate diffusion loss, preserving VLM priors while unifying perception, instruction grounding, and action denoising within a ...
- **p. 3 / 3.2. Formulation of Discrete Diffusion over Actions - extractive PDF cue:** The forward (noising) process of discrete diffusion is a Markov chain {at}T t=0 with per-step transition matrices Qt ∈RV ×V that independently map each token ...
- **p. 5 / 3.5. Adaptive Decoding and Secondary Re-Masking - extractive PDF cue:** We keep the top (1-γt+1)L positions Kt and update the tokens via tempered Gumbel sampling to encourage exploration: at+1,i∈Kt ∼Categorical  softmax log pθ(· / ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (3.1. Overview), p. 4 (3.4. Algorithmic Pipeline), p. 4 (3.4. Algorithmic Pipeline), p. 5 (3.5. Adaptive Decoding and Secondary Re-Masking), p. 5 (3.5. Adaptive Decoding and Secondary Re-Masking).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, image, observations, single-, multi-view, language, instruction, model, extends, VLM, backbone, generate, actions, discrete | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Given, image, observations, single-, multi-view, language, instruction, model, extends, VLM | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, threefold, introduce, first, discrete, diffusion, VLA, unifying, action | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | implementation, follow, mask, diffusion, formulations, collapse, multi-step, chain, single, masked-token | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Overview - extractive PDF cue:** Given image observations (single- or multi-view) and a language instruction, the model extends a VLM backbone to generate actions via discrete diffusion.
- **p. 1 / 1. Introduction - extractive PDF cue:** Modern VLA frameworks typically adapt a large pretrained vision-language model (VLM) by adding an action-generation head that outputs motor commands (either continuous trajectories or discrete ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We evaluate Discrete Diffusion VLA on a Franka Panda arm (LIBERO (Liu et al., 2023)), a Google Robot (SimplerEnvFractal (Li et al., 2025)), and a ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Vision-Language-Action (VLA) models enable robots to interpret visual and linguistic inputs and execute corresponding action sequences.
- **p. 2 / 1. Introduction - extractive PDF cue:** At inference, the method starts with all action tokens masked, concatenated with visual and language inputs, and iteratively predicts and re-masks low-confidence tokens until convergence, ...
- **p. 3 / 3.1. Overview - extractive PDF cue:** This formulation eliminates the competing gradients introduced by a separate diffusion loss, preserving VLM priors while unifying perception, instruction grounding, and action denoising within a ...
- **p. 4 / 3.3. Architecture of Discrete Diffusion VLA - extractive PDF cue:** All tokens pass through the unified transformer, with hidden states at action positions projected to a 256-way vocabulary via a shared classification head.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Method Latency (ms) Speed (Hz) NFE OpenVLA (AR) 136.2 7.34 56 OpenVLA w/o KVcache (AR) 209.5 4.77 56 OpenVLA-OFT (Parallel Decoding) 31.1 ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Discrete Diffusion VLA achieves 68.8 ms per chunk (14.53 Hz), 2× faster than AR (136.2 ms), and comparable to continuous diffusion when ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Method Latency (ms) Speed (Hz) NFE OpenVLA (AR) 136.2 7.34 56 OpenVLA w/o KVcache (AR) 209.5 4.77 56 OpenVLA-OFT (Parallel Decoding) 31.1 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.5. Adaptive Decoding and Secondary Re-Masking - extractive PDF cue:** As illustrated above, the inference pipeline starts from a fully masked action chunk a1 = ML with mask ratio γ1=1, and then performs T refinement ...
- **p. 4 / 3.4. Algorithmic Pipeline - extractive PDF cue:** No additional loss terms, auxiliary objectives, or special training procedures are involved.
- **p. 5 / 4.1. Simulation Benchmarks and Baselines - extractive PDF cue:** A complete per-table breakdown of sources, hardware, and training steps is provided in Appendix C.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** illustrated, above, inference, pipeline, starts, fully, masked, action, chunk, mask, ratio, then, performs, refinement, steps, monotone, schedule, Given, image, observations.
- **Relevant PDF headings:** 2.1. Vision-Language-Action Models (p. 2); 2.2. Discrete Diffusion Models (p. 2); 3. Discrete Diffusion VLA Model (p. 3); 3.3. Architecture of Discrete Diffusion VLA (p. 4); 3.4. Algorithmic Pipeline (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We evaluate Discrete Diffusion VLA on three different robot settings: (i) Franka Panda arm on LIBERO (Liu et al., 2023) (four suites: ... | p. 5 (4.1. Simulation Benchmarks and Baselines), p. 8 (4.6. Real-Robot Evaluation) |
| Action / skill decoding | 5 shows Discrete Diffusion VLA achieves SOTA performance with 54.2% overall, outperforming all continuous diffusion/flowmatching policies (π0: 40.1%, +14.1%; GR00T-N1: 49.5%, +4.7%) ... | p. 6 (4.3. Extended Evaluation Across Robot Platforms), p. 5 (4.1. Simulation Benchmarks and Baselines) |
| Receding execution / feedback | 5 shows Discrete Diffusion VLA achieves SOTA performance with 54.2% overall, outperforming all continuous diffusion/flowmatching policies (π0: 40.1%, +14.1%; GR00T-N1: 49.5%, +4.7%) ... | p. 6 (4.3. Extended Evaluation Across Robot Platforms), p. 7 (4.4. Ablation Study) |

## Failure and Ablation Link

- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** Action head without robot pretraining.
- **p. 5 / 4.1. Simulation Benchmarks and Baselines - extractive PDF cue:** We evaluate Discrete Diffusion VLA on three different robot settings: (i) Franka Panda arm on LIBERO (Liu et al., 2023) (four suites: Spatial, Object, Goal, ...
- **p. 6 / 4.3. Extended Evaluation Across Robot Platforms - extractive PDF cue:** On Variant Aggregation, Discrete Diffusion VLA attains 56.9%, competitive with RT-2-X (64.3%) and π0FAST (59.0%).
- **p. 7 / 4.3. Extended Evaluation Across Robot Platforms - extractive PDF cue:** Model Visual Matching Variant Aggregation #Overall Average Pick Coke Mv Near Drawer Avg.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Ablation study on decoding strategy.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** (ii) Right y-axis: Ablation on denoising steps.
- **p. 5 / 4.1. Simulation Benchmarks and Baselines - extractive PDF cue:** We fine-tune Discrete Diffusion VLA from OpenVLA backbone (Prismatic-7B) with images resized to 224 × 224.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.5. Adaptive Decoding and Secondary Re-Masking), p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 4 (3.4. Algorithmic Pipeline), p. 4 (3.3. Architecture of Discrete Diffusion VLA), p. 5 (3.5. Adaptive Decoding and Secondary Re-Masking), objective p. 4 (3.2. Formulation of Discrete Diffusion over Actions), p. 4 (3.4. Algorithmic Pipeline), p. 3 (3.1. Overview), p. 3 (3.2. Formulation of Discrete Diffusion over Actions), p. 5 (3.5. Adaptive Decoding and Secondary Re-Masking), temporal p. 7 (4.4. Ablation Study), p. 8 (4.5. Inference Efficiency), p. 6 (4.1. Simulation Benchmarks and Baselines), p. 8 (4.5. Inference Efficiency), p. 4 (3.3. Architecture of Discrete Diffusion VLA), p. 2 (2.1. Vision-Language-Action Models).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
