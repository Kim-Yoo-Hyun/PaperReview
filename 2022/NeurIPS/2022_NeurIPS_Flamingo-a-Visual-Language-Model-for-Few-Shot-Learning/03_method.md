# Method - Flamingo: a Visual Language Model for Few-Shot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (54 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2204.14198; PDF retrieval source: https://arxiv.org/pdf/2204.14198. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (2 Approach), p. 4 (2 Approach), p. 5 (2 Approach), p. 6 (2 Approach), p. 8 (Method), p. 6 (2 Approach)): It takes as input a variable number of image or video features from the vision encoder and produces a fixed number of visual outputs (64), reducing the computational complexity of ...

## Method Body Digest

- **p. 5 / 2 Approach - extractive PDF cue:** It takes as input a variable number of image or video features from the vision encoder and produces a fixed number of visual outputs (64), ...
- **p. 4 / 2 Approach - extractive PDF cue:** First, the Perceiver Resampler (Section 2.1) receives spatio-temporal features from the Vision Encoder (obtained from either an image or a video) and outputs a fixed ...
- **p. 5 / 2 Approach - extractive PDF cue:** Our vision encoder is a pretrained and frozen NormalizerFree ResNet (NFNet) [10] - we use the F6 model.
- **p. 6 / 2 Approach - extractive PDF cue:** In particular, we use only up to 5 images per sequence when training on our interleaved datasets, yet our model is able to benefit from ...
- **p. 8 / Method - extractive PDF cue:** Note that we use smaller batch sizes and a shorter training schedule compared to the final models.
- **p. 6 / 2 Approach - extractive PDF cue:** This single-image cross-attention scheme importantly allows the model to seamlessly generalise to any number of visual inputs, regardless of how many are used during training.
- **p. 9 / Method - extractive PDF cue:** VANILLA XATTN, refers to the vanilla cross-attention from the original Transformer decoder [115].
- **p. 9 / Method - extractive PDF cue:** In light of this trade-off, we maximize the number of added layers under hardware constraints and add a GATED XATTN-DENSE every fourth layer for Flamingo-9B ...

## Design Rationale

- **p. 4 / 1 Introduction - extractive PDF cue:** In summary, our contributions are the following: (i) We introduce the Flamingo family of VLMs which can perform various multimodal tasks (such as captioning, visual ...
- **p. 3 / 1 Introduction - extractive PDF cue:** We introduce Flamingo, a Visual Language Model (VLM) that sets a new state of the art in few-shot learning on a wide range of open-ended ...
- **p. 3 / 1 Introduction - extractive PDF cue:** While initial progress has been made towards a similar capability in computer vision, the most widely used paradigm still consists of first pretraining on a ...

## Source Evidence Cues

- **p. 5 / 2 Approach - extractive PDF cue:** It takes as input a variable number of image or video features from the vision encoder and produces a fixed number of visual outputs (64), ...
- **p. 4 / 2 Approach - extractive PDF cue:** First, the Perceiver Resampler (Section 2.1) receives spatio-temporal features from the Vision Encoder (obtained from either an image or a video) and outputs a fixed ...
- **p. 5 / 2 Approach - extractive PDF cue:** Our vision encoder is a pretrained and frozen NormalizerFree ResNet (NFNet) [10] - we use the F6 model.
- **p. 6 / 2 Approach - extractive PDF cue:** In particular, we use only up to 5 images per sequence when training on our interleaved datasets, yet our model is able to benefit from ...
- **p. 8 / Method - extractive PDF cue:** Note that we use smaller batch sizes and a shorter training schedule compared to the final models.
- **p. 6 / 2 Approach - extractive PDF cue:** This single-image cross-attention scheme importantly allows the model to seamlessly generalise to any number of visual inputs, regardless of how many are used during training.
- **p. 9 / Method - extractive PDF cue:** VANILLA XATTN, refers to the vanilla cross-attention from the original Transformer decoder [115].
- **Detected method headings:** 2 Approach (p. 4); Method (p. 7); Method (p. 8); A Method (p. 23); A.1 Model details (p. 23); A.1.4 Transformer architecture (p. 24); B.1.1 Models (p. 28); B.1.2 Training details for the Flamingo models (p. 29); B.1.3 Contrastive model details (p. 30); Model (p. 33); B.2.2 Fine-tuning Flamingo as a pretrained vision-language model (p. 33); B.2.3 Zero-shot performance of the pretrained contrastive model (p. 34)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | It takes as input a variable number of image or video features from the vision encoder and produces a fixed number of ... | p. 5 (2 Approach), p. 4 (2 Approach) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | First, the Perceiver Resampler (Section 2.1) receives spatio-temporal features from the Vision Encoder (obtained from either an image or a video) and ... | p. 4 (2 Approach), p. 5 (2 Approach) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | Our vision encoder is a pretrained and frozen NormalizerFree ResNet (NFNet) [10] - we use the F6 model. | p. 5 (2 Approach), p. 6 (2 Approach) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 9 / Method - extractive PDF cue:** In light of this trade-off, we maximize the number of added layers under hardware constraints and add a GATED XATTN-DENSE every fourth layer for Flamingo-9B ...
- **p. 5 / 2 Approach - extractive PDF cue:** We pretrain the vision encoder using a contrastive objective on our datasets of image and text pairs, using the two-term contrastive loss from Radford et ...
- **p. 8 / Method - extractive PDF cue:** Step time measures the time spent to perform gradient updates on all training datasets.
- **p. 9 / Method - extractive PDF cue:** We show in row (ii) the importance of our gradient accumulation strategy compared to using round-robin updates [17].
- **p. 6 / 2 Approach - extractive PDF cue:** 2.3 Multi-visual input support: per-image/video attention masking The image-causal modelling introduced in Equation (1) is obtained by masking the full text-to-image cross-attention matrix, limiting which ...
- **p. 6 / 2 Approach - extractive PDF cue:** We train our models by minimizing a weighted sum of per-dataset expected negative log-likelihoods of text, given the visual inputs: 𝑀 ∑︁ 𝑚=1 𝜆𝑚· E(𝑥,𝑦)∼𝒟𝑚 ...
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 5 (2 Approach), p. 8 (Method), p. 9 (Method), p. 6 (2 Approach), p. 6 (2 Approach), p. 9 (Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | section, describes, Flamingo, visual, language, model, accepts, text, interleaved, images/videos, input, outputs, free-form, introduce | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | section, describes, Flamingo, visual, language, model, accepts, text, interleaved, images/videos | task state 또는 decision variable | body cue; notation verify |
| Action/output | summary, contributions, following, introduce, Flamingo, family, VLMs, perform, various, multimodal | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | light, trade-off, maximize, number, added, layers, under, hardware, constraints, GATED | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 2 Approach - extractive PDF cue:** This section describes Flamingo: a visual language model that accepts text interleaved with images/videos as input and outputs free-form text.
- **p. 3 / 1 Introduction - extractive PDF cue:** We introduce Flamingo, a Visual Language Model (VLM) that sets a new state of the art in few-shot learning on a wide range of open-ended ...
- **p. 5 / 2 Approach - extractive PDF cue:** It takes as input a variable number of image or video features from the vision encoder and produces a fixed number of visual outputs (64), ...
- **p. 5 / 2 Approach - extractive PDF cue:** Gated Feed Forward (dense) Layer y = y + tanh(alpha_dense) * ffw(y) # Regular self-attention + FFW on language y = y + frozen_attention(q=y, kv=y) ...
- **p. 4 / 1 Introduction - extractive PDF cue:** Flamingo is a family of visual language models (VLMs) that take as input visual data interleaved with text and produce free-form text as output. mixture ...
- **p. 6 / 2 Approach - extractive PDF cue:** 2.3 Multi-visual input support: per-image/video attention masking The image-causal modelling introduced in Equation (1) is obtained by masking the full text-to-image cross-attention matrix, limiting which ...
- **p. 7 / Method - extractive PDF cue:** A single Flamingo model reaches the state of the art on a wide array of image (I) and video (V) understanding tasks with few-shot learning, ...
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | For video inputs, frames are sampled at 1 FPS and encoded independently to obtain a 3D spatio-temporal grid of features to which ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | Step time measures the time spent to perform gradient updates on all training datasets. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | Compute/Memory vs. performance trade-offs. | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | For video inputs, frames are sampled at 1 FPS and encoded independently to obtain a 3D spatio-temporal grid of features to which ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 2 Approach - extractive PDF cue:** Our vision encoder is a pretrained and frozen NormalizerFree ResNet (NFNet) [10] - we use the F6 model.
- **p. 6 / 2 Approach - extractive PDF cue:** In particular, we use only up to 5 images per sequence when training on our interleaved datasets, yet our model is able to benefit from ...
- **p. 8 / Method - extractive PDF cue:** Note that we use smaller batch sizes and a shorter training schedule compared to the final models.
- **p. 6 / 2 Approach - extractive PDF cue:** This single-image cross-attention scheme importantly allows the model to seamlessly generalise to any number of visual inputs, regardless of how many are used during training.
- **p. 8 / Method - extractive PDF cue:** Note that we use smaller batch sizes and a shorter training schedule compared to the final models.
- **p. 8 / Method - extractive PDF cue:** In short, we do so by fine-tuning the model on a short schedule with a small learning rate by additionally unfreezing the vision backbone to ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** takes, input, variable, number, image, video, features, vision, encoder, produces, fixed, visual, outputs, reducing, computational, complexity, vision-text, cross-attention, First, Perceiver.
- **Relevant PDF headings:** 2 Approach (p. 4); Method (p. 7); Method (p. 8); A Method (p. 23); A.1 Model details (p. 23); A.1.4 Transformer architecture (p. 24); B.1.1 Models (p. 28); B.1.2 Training details for the Flamingo models (p. 29); B.1.3 Contrastive model details (p. 30); Model (p. 33); B.2.2 Fine-tuning Flamingo as a pretrained vision-language model (p. 33); B.2.3 Zero-shot performance of the pretrained contrastive model (p. 34).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | For the DEV benchmarks that are used both to validate design decisions and hyperparameters, as well as to report final performance, we ... | p. 7 (3 Experiments), p. 7 (3 Experiments) |
| Core objective / transformation | Table 3: Ablation studies. Each row should be compared to the baseline Flamingo run (top row). Step time measures the time spent ... | p. 8 (Figure/Table caption), p. 35 (Figure/Table caption) |
| Downstream transfer boundary | Figure 2: Flamingo results overview. Left: Our largest model, dubbed Flamingo, outperforms state-of-the-art fine-tuned models on 6 of the 16 tasks we ... | p. 3 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 37 / Figure/Table caption - extractive PDF cue:** Table 11: Effect of contrastive pretraining datasets and combination strategies. The first two rows show the effect of training a small model on LTIP and ...
- **p. 7 / 3 Experiments - extractive PDF cue:** An ablation study is given in Section 3.3.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison to the state of the art. A single Flamingo model reaches the state of the art on a wide array of image ...
- **p. 35 / Figure/Table caption - extractive PDF cue:** Table 10. We ablate the size of our Resampler with three options: Small, Medium (default value for all Flamingo models), and Large. We see that ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: Flamingo architecture overview. Flamingo is a family of visual language models (VLMs) that take as input visual data interleaved with text and produce ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Ablation studies. Each row should be compared to the baseline Flamingo run (top row). Step time measures the time spent to perform gradient ...
- **p. 35 / Figure/Table caption - extractive PDF cue:** Table 10: Additional ablation studies. Each row in this ablation study table should be compared to the baseline Flamingo run reported at the top of ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (2 Approach), p. 4 (2 Approach), p. 5 (2 Approach), p. 6 (2 Approach), p. 8 (Method), p. 6 (2 Approach), objective p. 9 (Method), p. 5 (2 Approach), p. 8 (Method), p. 9 (Method), p. 6 (2 Approach), p. 6 (2 Approach), temporal p. 5 (2 Approach), p. 8 (Method), p. 8 (Method), p. 9 (Method), p. 9 (Method), p. 4 (2 Approach).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
