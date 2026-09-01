# Method - SPA: 3D Spatial-Awareness Enables Effective Embodied Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=6TLdqAZgzn; PDF retrieval source: https://openreview.net/pdf/69efa7c1cd34c4e72171331a81f56b7c914e9e24.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (2 METHODOLOGY), p. 3 (2 METHODOLOGY), p. 22 (C.2 PRE-TRAINING DETAILS), p. 4 (2 METHODOLOGY), p. 22 (C.2 PRE-TRAINING DETAILS), p. 24 (C.2 PRE-TRAINING DETAILS)): Finally, we explain the image rendering from the feature volume and loss functions for network optimization in Sec.

## Method Body Digest

- **p. 3 / 2 METHODOLOGY - extractive PDF cue:** Finally, we explain the image rendering from the feature volume and loss functions for network optimization in Sec.
- **p. 3 / 2 METHODOLOGY - extractive PDF cue:** We then unpatchify them to obtain a latent feature map of size H P × W P , where P is the ViT patch size.
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** Given an image pair from different viewpoints, we first extract features from each image using a frozen, pre-trained Vision Transformer (ViT) encoder.
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** For the semantic feature map, we use the feature map from AM-RADIO (Ranzinger et al., 2024) as supervision.
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** Following standard protocols for embodied evaluation, we use the [CLS] token as the feature representation.
- **p. 24 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** In this study, we maintained all settings identical-data loading, training techniques, hyperparameters, and the encoder-while replacing the volume neural rendering decoder with a multiview transformer-based ...
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** We then render depth, RGB, and semantic maps for loss computation.
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** (7) Additionally, we incorporate the Eikonal regularization loss Leikonal, near-surface SDF supervision loss Lsdf, and free space SDF loss Lfree, which are standard in neural ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Our contribution can be summarized as follows. • We propose a significant spatial hypothesis: 3D spatial awareness is crucial for embodied representation learning.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Our experiments provide clear evidence for the hypothesis. • We introduce SPA, a novel paradigm for representation learning in embodied AI.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** In this paper, we introduce SPA, a general 3D spatial-aware representation learning framework for embodied AI.

## Source Evidence Cues

- **p. 3 / 2 METHODOLOGY - extractive PDF cue:** Finally, we explain the image rendering from the feature volume and loss functions for network optimization in Sec.
- **p. 3 / 2 METHODOLOGY - extractive PDF cue:** We then unpatchify them to obtain a latent feature map of size H P × W P , where P is the ViT patch size.
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** Given an image pair from different viewpoints, we first extract features from each image using a frozen, pre-trained Vision Transformer (ViT) encoder.
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** For the semantic feature map, we use the feature map from AM-RADIO (Ranzinger et al., 2024) as supervision.
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** Following standard protocols for embodied evaluation, we use the [CLS] token as the feature representation.
- **p. 24 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** In this study, we maintained all settings identical-data loading, training techniques, hyperparameters, and the encoder-while replacing the volume neural rendering decoder with a multiview transformer-based ...
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** We then render depth, RGB, and semantic maps for loss computation.
- **Detected method headings:** 2 METHODOLOGY (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Finally, we explain the image rendering from the feature volume and loss functions for network optimization in Sec. | p. 3 (2 METHODOLOGY), p. 3 (2 METHODOLOGY) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We then unpatchify them to obtain a latent feature map of size H P × W P , where P is the ... | p. 3 (2 METHODOLOGY), p. 22 (C.2 PRE-TRAINING DETAILS) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Given an image pair from different viewpoints, we first extract features from each image using a frozen, pre-trained Vision Transformer (ViT) encoder. | p. 22 (C.2 PRE-TRAINING DETAILS), p. 4 (2 METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 2 METHODOLOGY - extractive PDF cue:** Finally, we explain the image rendering from the feature volume and loss functions for network optimization in Sec.
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** (7) Additionally, we incorporate the Eikonal regularization loss Leikonal, near-surface SDF supervision loss Lsdf, and free space SDF loss Lfree, which are standard in neural ...
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** We employ the Mean Squared Error (MSE) loss function and optimize the model using the AdamW optimizer with a OneCycle learning rate scheduler.
- **p. 3 / 2 METHODOLOGY - extractive PDF cue:** Following MAE, we apply random masking to input images to enhance robustness, but without a ViT decoder and MAE's pixel reconstruction objective.
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** Detailed definitions of these losses are provided in Appendix A.
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** The model is trained for 2000 epochs on 80 NVIDIA A100-80G GPUs, using a gradient clipping threshold of 1.0.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (2 METHODOLOGY), p. 3 (2 METHODOLOGY), p. 4 (2 METHODOLOGY), p. 4 (2 METHODOLOGY), p. 22 (C.2 PRE-TRAINING DETAILS), p. 22 (C.2 PRE-TRAINING DETAILS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | section, first, describe, process, handling, multi-view, image, inputs, feature, extraction, Sec, INPUT, Given, images | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | section, first, describe, process, handling, multi-view, image, inputs, feature, extraction | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contribution, summarized, follows, significant, spatial, hypothesis, awareness, crucial, embodied, representation | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Finally, explain, image, rendering, feature, volume, loss, functions, network, optimization | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 2 METHODOLOGY - extractive PDF cue:** In this section, we first describe our process for handling multi-view image inputs and feature extraction in Sec.
- **p. 3 / 2 METHODOLOGY - extractive PDF cue:** 2.1 INPUT PROCESS AND FEATURE EXTRACTION Given a set of multi-view images I = {I1, I2, . . . , IN}, where each Ii ∈R3×H×W ...
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** Published as a conference paper at ICLR 2025 Vision Transformer Upsampler Multi-View Input Images Masked Patches Multi-View Feature Maps Volume Construction Rays SDF Values SH ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Unlike explicit 3D representations like point clouds or meshes-which prior work (Wang et al., 2024b;a; Ze et al., 2024; Zhu et al., 2024) has shown ...
- **p. 23 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** (2023) to use DrQ-v2 (Yarats et al., 2021), a state-of-the-art off-policy actor-critic approach for continuous vision-based control.
- **p. 4 / 2 METHODOLOGY - extractive PDF cue:** Given multi-view images, we randomly mask patches and input the remaining into a Vision Transformer.
- **p. 22 / C.1 DATASET DETAILS - extractive PDF cue:** Consequently, we resize the images to 1024 × 1024 before feeding them into RADIO, which outputs a feature map of size 64 × 64.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Consequently, our approach leads to substantial improvements in both time and memory efficiency, especially when sampling a large number of points during ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Our framework has the capability to distill knowledge from multiple vision foundation models by adding multiple rendering heads. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | Consequently, our approach leads to substantial improvements in both time and memory efficiency, especially when sampling a large number of points during ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** Given an image pair from different viewpoints, we first extract features from each image using a frozen, pre-trained Vision Transformer (ViT) encoder.
- **p. 24 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** In this study, we maintained all settings identical-data loading, training techniques, hyperparameters, and the encoder-while replacing the volume neural rendering decoder with a multiview transformer-based ...
- **p. 23 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** We train for a total of 1.1M frames and all other hyperparameters including random seeds are kept as default and same.
- **p. 24 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** In this study, we maintained all settings identical-data loading, training techniques, hyperparameters, and the encoder-while replacing the volume neural rendering decoder with a multiview transformer-based ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Finally, explain, image, rendering, feature, volume, loss, functions, network, optimization, Sec, then, unpatchify, them, obtain, latent, size, where, ViT, patch.
- **Relevant PDF headings:** 2 METHODOLOGY (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | (14) F REAL-WORLD EXPERIMENT DETAILS Our real-world hardware setup is based on the open-source Low-Cost-Robot project (Koch, 2024). | p. 23 (C.2 PRE-TRAINING DETAILS), p. 23 (C.2 PRE-TRAINING DETAILS) |
| Action / skill decoding | Figure 4: Correlation between mean success rate and camera pose regression error. 5.2 ADDITIONAL COMPARISONS (Q1) We primarily compare with SOTA methods ... | p. 8 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Receding execution / feedback | Tab. 3. For detailed results on each task and each random seed, please refer to Appendix D. We also have visualized the ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 6: Additional ablations on VC-1. Methods SPA-B SPA-MAE RADIO E-RADIO VC-1 AD
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Correlation between mean success rate and camera pose regression error. 5.2 ADDITIONAL COMPARISONS (Q1) We primarily compare with SOTA methods using the ViT-L ...
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** This initialization does not affect the validity of our conclusions, as demonstrated by the ablation study of SPA-MAE in Sec.
- **p. 24 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** It was trained on the ScanNet dataset without semantic supervision, ensuring a fair comparison with the result in the last line of Tab.
- **p. 24 / Figure/Table caption - extractive PDF cue:** Table 11: Additional Ablation Study on Neural Rendering. The models are evaluated on two subsets of the VC-1 benchmark. The model architectures are both ViT-base.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 7: Mask ratio and loss components. C., D., S. denote color, depth, and semantic. Mask Ratio Loss VC-1 Benchmark Mean S.R.
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive PDF cue:** To facilitate faster convergence and improve stability, we initialize the encoder with ImageNet pretrained weights from the Masked Autoencoder (MAE), applying a learning rate layer ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (2 METHODOLOGY), p. 3 (2 METHODOLOGY), p. 22 (C.2 PRE-TRAINING DETAILS), p. 4 (2 METHODOLOGY), p. 22 (C.2 PRE-TRAINING DETAILS), p. 24 (C.2 PRE-TRAINING DETAILS), objective p. 3 (2 METHODOLOGY), p. 4 (2 METHODOLOGY), p. 22 (C.2 PRE-TRAINING DETAILS), p. 3 (2 METHODOLOGY), p. 4 (2 METHODOLOGY), p. 22 (C.2 PRE-TRAINING DETAILS), temporal p. 3 (2 METHODOLOGY), p. 4 (2 METHODOLOGY), p. 21 (C.1 DATASET DETAILS), p. 21 (C.1 DATASET DETAILS), p. 22 (C.1 DATASET DETAILS), p. 22 (C.1 DATASET DETAILS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
