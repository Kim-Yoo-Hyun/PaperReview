# Method - HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=lduY9csXqw; PDF retrieval source: https://openreview.net/pdf/f0a4b4b3d1775cb04d6e602c68bf3c4914033562.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (3.4. Training Recipe), p. 5 (3.4. Training Recipe), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Unified Architecture), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Unified Architecture)): Crucially, we employ a dual-path visual pathway that integrates complementary semantic and spatial representations: a ViT branch first captures high-level semantic context, while a VAE branch provides spatially grounded latent ...

## Method Body Digest

- **p. 6 / 3.4. Training Recipe - extractive PDF cue:** Crucially, we employ a dual-path visual pathway that integrates complementary semantic and spatial representations: a ViT branch first captures high-level semantic context, while a VAE ...
- **p. 5 / 3.4. Training Recipe - extractive PDF cue:** This diversity ensures the model develops a generalized representation capable of supporting complex downstream reasoning. • VQA (Mutilmodal understanding): We use LLaVA-NeXT-779k (Liu et al., ...
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** Traditional VLA models typically learn a monolithic policy πθ(at:t+m / l, ot-k:t) that directly maps history observations and instructions to action chunks.
- **p. 4 / 3.2. Unified Architecture - extractive PDF cue:** By default, the model operates as an auto-regressive planner; however, the generation of specific tokens (e.g., ⟨visual start⟩or ⟨action start⟩) triggers the routing of hidden ...
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** Let τ = {(ot, l, at)}T t=1 denote a trajectory, comprising visual observations ot ∈O, language instructions l ∈L, and continuous actions at ∈A.
- **p. 4 / 3.2. Unified Architecture - extractive PDF cue:** Drawing inspiration from the capability of BAGEL (Deng et al., 2025) to harmonize multimodal tasks, we adopt a Mixture-of-Transformers (MoT) (Liang et al., 2024) architecture ...
- **p. 5 / 3.4. Training Recipe - extractive PDF cue:** The primary objective of this phase is to unify multimodal understanding, physical dynamics prediction, and foundational manipulation skills into a single architecture.
- **p. 6 / 3.4. Training Recipe - extractive PDF cue:** The fine-tuning objective minimizes the joint loss: Lft = Lr + Lˆo + La, (5) where Lr, Lˆo, and La represent the losses for textual ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To address this, we propose HALO, a unified VLA model that enables embodied multimodal chain-of-thought (EM-CoT) reasoning.
- **p. 2 / 1. Introduction - extractive PDF cue:** Third, we propose a carefully designed training recipe that combines broad generalization with embodied reasoning specialization.
- **p. 1 / 1. Introduction - extractive PDF cue:** Existing approaches (Zhao et al., 2025; Gu et al., 2025) often tightly couple visual *Equal contribution. †Corresponding author.

## Source Evidence Cues

- **p. 6 / 3.4. Training Recipe - extractive PDF cue:** Crucially, we employ a dual-path visual pathway that integrates complementary semantic and spatial representations: a ViT branch first captures high-level semantic context, while a VAE ...
- **p. 5 / 3.4. Training Recipe - extractive PDF cue:** This diversity ensures the model develops a generalized representation capable of supporting complex downstream reasoning. • VQA (Mutilmodal understanding): We use LLaVA-NeXT-779k (Liu et al., ...
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** Traditional VLA models typically learn a monolithic policy πθ(at:t+m / l, ot-k:t) that directly maps history observations and instructions to action chunks.
- **p. 4 / 3.2. Unified Architecture - extractive PDF cue:** By default, the model operates as an auto-regressive planner; however, the generation of specific tokens (e.g., ⟨visual start⟩or ⟨action start⟩) triggers the routing of hidden ...
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** Let τ = {(ot, l, at)}T t=1 denote a trajectory, comprising visual observations ot ∈O, language instructions l ∈L, and continuous actions at ∈A.
- **p. 4 / 3.2. Unified Architecture - extractive PDF cue:** Drawing inspiration from the capability of BAGEL (Deng et al., 2025) to harmonize multimodal tasks, we adopt a Mixture-of-Transformers (MoT) (Liang et al., 2024) architecture ...
- **p. 5 / 3.4. Training Recipe - extractive PDF cue:** The primary objective of this phase is to unify multimodal understanding, physical dynamics prediction, and foundational manipulation skills into a single architecture.
- **Detected method headings:** 3. Method (p. 3); 3.2. Unified Architecture (p. 4); A. Details on Model Architecture (p. 12)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Crucially, we employ a dual-path visual pathway that integrates complementary semantic and spatial representations: a ViT branch first captures high-level semantic context, ... | p. 6 (3.4. Training Recipe), p. 5 (3.4. Training Recipe) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | This diversity ensures the model develops a generalized representation capable of supporting complex downstream reasoning. • VQA (Mutilmodal understanding): We use LLaVA-NeXT-779k ... | p. 5 (3.4. Training Recipe), p. 3 (3.1. Problem Formulation) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Traditional VLA models typically learn a monolithic policy πθ(at:t+m / l, ot-k:t) that directly maps history observations and instructions to action chunks. | p. 3 (3.1. Problem Formulation), p. 4 (3.2. Unified Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3.4. Training Recipe - extractive PDF cue:** The fine-tuning objective minimizes the joint loss: Lft = Lr + Lˆo + La, (5) where Lr, Lˆo, and La represent the losses for textual ...
- **p. 5 / 3.3. EM-CoT Data Pipeline - extractive PDF cue:** (3) Cross-modality interactions and text generation follow causal constraints.
- **p. 5 / 3.4. Training Recipe - extractive PDF cue:** This task aligns linguistic instructions with visual contexts via a cross-entropy loss, denoted as LCE. • VG (Visual Generation): To instill physical common sense, we ...
- **p. 6 / 3.4. Training Recipe - extractive PDF cue:** To address the varying optimization difficulties across these tasks, we balance the pre-training objective by assigning higher weights to manipulation intensive tasks.
- **p. 16 / C. Training Implementation - extractive PDF cue:** Configuration Pre-training Fine-tuning Base Architecture Qwen2.5-1.5B × 3 Experts Total Parameters ≈4.5B Optimizer AdamW Learning Rate 1 × 10-4 5 × 10-5 Learning Rate Schedule ...
- **p. 3 / 3. Method - extractive PDF cue:** Collectively, these components empower the model to engage in textual reasoning, visual foresight, and grounded action prediction.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 6 (3.4. Training Recipe), p. 5 (3.3. EM-CoT Data Pipeline), p. 5 (3.4. Training Recipe), p. 6 (3.4. Training Recipe), p. 16 (C. Training Implementation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Traditional, VLA, models, typically, learn, monolithic, policy, ot-k, directly, maps, history, observations, instructions, action | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Traditional, VLA, models, typically, learn, monolithic, policy, ot-k, directly, maps | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | address, HALO, unified, VLA, model, enables, embodied, multimodal, chain-of-thought, EM-CoT | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | fine-tuning, objective, minimizes, joint, loss, Lft, where, represent, losses, textual | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** Traditional VLA models typically learn a monolithic policy πθ(at:t+m / l, ot-k:t) that directly maps history observations and instructions to action chunks.
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** Let τ = {(ot, l, at)}T t=1 denote a trajectory, comprising visual observations ot ∈O, language instructions l ∈L, and continuous actions at ∈A.
- **p. 5 / 3.3. EM-CoT Data Pipeline - extractive PDF cue:** The pipeline converts raw robotic trajectories into EM-CoT data in three phases: (1) action primitives are extracted from robot proprioception via rule-based matching; (2) a ...
- **p. 2 / 1. Introduction - extractive PDF cue:** These experts collaborate seamlessly through shared selfattention, while preserving each expert's natural generative workflow-autoregressive text generation for reasoning and diffusion-based prediction for visual states and ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Keep the right arm idle. <move_end> … <\think> ②Textual Reasoning & Planning Current Observations ④Action Chunk Environment Context Shared Self-Attention QKV QKV QKV FFN FFN ...
- **p. 4 / 3.2. Unified Architecture - extractive PDF cue:** By default, the model operates as an auto-regressive planner; however, the generation of specific tokens (e.g., ⟨visual start⟩or ⟨action start⟩) triggers the routing of hidden ...
- **p. 5 / 3.3. EM-CoT Data Pipeline - extractive PDF cue:** (c) Action Prediction Task Instruction: Set the blocks in the order of red, green, blue.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Traditional VLA models typically learn a monolithic policy πθ(at:t+m / l, ot-k:t) that directly maps history observations and instructions to action chunks. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The model learns to predict the next action chunk at given the history, supervised by an L1 flow-matching loss, LL1. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | Traditional VLA models typically learn a monolithic policy πθ(at:t+m / l, ot-k:t) that directly maps history observations and instructions to action chunks. | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 16 / C. Training Implementation - extractive PDF cue:** Configuration Pre-training Fine-tuning Base Architecture Qwen2.5-1.5B × 3 Experts Total Parameters ≈4.5B Optimizer AdamW Learning Rate 1 × 10-4 5 × 10-5 Learning Rate Schedule ...
- **p. 7 / 4.1. Experiment Settings - extractive PDF cue:** Using these datasets, HALO is fine-tuned for 110k steps in simulation and 80k steps in real-world experiments.
- **p. 7 / 4.1. Experiment Settings - extractive PDF cue:** During pre-training, following (Deng et al., 2025), training samples are concatenated to a maximum sequence length of 27k tokens, and Flex Attention (Dong et al., ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Crucially, employ, dual-path, visual, pathway, integrates, complementary, semantic, spatial, representations, ViT, branch, first, captures, high-level, context, while, VAE, provides, spatially.
- **Relevant PDF headings:** 3. Method (p. 3); 3.2. Unified Architecture (p. 4); A. Details on Model Architecture (p. 12).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | The simulation dataset contains 2,500 expert demonstrations (50 per task) collected in clean environments, while the real-world dataset consists of 320 demonstrations ... | p. 7 (4.1. Experiment Settings), p. 7 (4.2. Simulation Results) |
| Action / skill decoding | It can be observed that HALO consistently outperforms all competitive baselines across both Easy and Hard settings. | p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results) |
| Receding execution / feedback | While the baselines suffer noticeable performance degradation in the presence of visual distractions, lighting and background variations, and novel objects, HALO remains ... | p. 8 (4.5. Real-World Results), p. 6 (4. Experiments) |

## Failure and Ablation Link

- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** We perform ablation studies to validate the effectiveness of HALO's mechanism design, including the versatile pre-training and the EM-CoT-augmented Fine-tuning.
- **p. 7 / 4.2. Simulation Results - extractive PDF cue:** Baseline results are taken directly from the official RoboTwin 2.0 leaderboard.1 To isolate the contribution of EM-CoT, we further include a variant of our method ...
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** Notably, without any pre-training (w/o V+T+A), the model's performance falls to a complete 0% on hard tasks, demonstrating that pre-training is an absolutely foundational requirement ...
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** As shown in Panel B, both visual subgoal images and textual reasoning are crucial components for EM-CoT, removing either component degrades performance.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Overview of dataset recipe. HALO training involves two stages: Stage 1 pre-trains on general VQA, visual generation, and action prediction to build foundation ...
- **p. 16 / C. Training Implementation - extractive PDF cue:** In this section, we provide details on pre-training and fine-tuning of HALO.
- **p. 16 / C. Training Implementation - extractive PDF cue:** Then, we fine-tune HALO on 32 Nvidia H100 GPUs with sequence length of 27k, 110k steps for simulation, 80k steps for real experiment.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (3.4. Training Recipe), p. 5 (3.4. Training Recipe), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Unified Architecture), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Unified Architecture), objective p. 6 (3.4. Training Recipe), p. 5 (3.3. EM-CoT Data Pipeline), p. 5 (3.4. Training Recipe), p. 6 (3.4. Training Recipe), p. 16 (C. Training Implementation), p. 3 (3. Method), temporal p. 3 (3.1. Problem Formulation), p. 6 (3.4. Training Recipe), p. 7 (4.1. Experiment Settings), p. 16 (C. Training Implementation), p. 16 (C. Training Implementation), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
