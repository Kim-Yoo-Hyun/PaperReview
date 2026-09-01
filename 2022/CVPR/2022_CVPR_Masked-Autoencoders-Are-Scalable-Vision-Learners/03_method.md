# Method - Masked Autoencoders Are Scalable Vision Learners

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2111.06377; PDF retrieval source: https://arxiv.org/pdf/2111.06377. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3. Approach), p. 3 (3. Approach), p. 4 (3. Approach), p. 4 (3. Approach), p. 11 (A. Implementation Details), p. 7 (4.3. Partial Fine-tuning)): Like all autoencoders, our approach has an encoder that maps the observed signal to a latent representation, and a decoder that reconstructs the original signal from the latent representation.

## Method Body Digest

- **p. 3 / 3. Approach - extractive PDF cue:** Like all autoencoders, our approach has an encoder that maps the observed signal to a latent representation, and a decoder that reconstructs the original signal ...
- **p. 3 / 3. Approach - extractive PDF cue:** Unlike classical autoencoders, we adopt an asymmetric design that allows the encoder to operate only on the partial, observed signal (without mask tokens) and a ...
- **p. 4 / 3. Approach - extractive PDF cue:** The MAE decoder is only used during pre-training to perform the image reconstruction task (only the encoder is used to produce image representations for recognition).
- **p. 4 / 3. Approach - extractive PDF cue:** Therefore, the decoder architecture can be flexibly designed in a manner that is independent of the encoder design.
- **p. 11 / A. Implementation Details - extractive PDF cue:** It has a stack of Transformer blocks [57], and each block consists of a multi-head self-attention block and an MLP block, both having LayerNorm (LN) ...
- **p. 7 / 4.3. Partial Fine-tuning - extractive PDF cue:** While the MAE representations are less linearly separable, they are stronger non-linear features and perform well when a non-linear head is tuned.
- **p. 8 / 4.3. Partial Fine-tuning - extractive PDF cue:** These observations suggest that linear separability is not the sole metric for evaluating representation quality.
- **p. 4 / 3. Approach - extractive PDF cue:** Our loss function computes the mean squared error (MSE) between the reconstructed and original images in the pixel space.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Driven by this analysis, we present a simple, effective, and scalable form of a masked autoencoder (MAE) for visual representation learning.
- **p. 11 / A. Implementation Details - extractive PDF cue:** It has a stack of Transformer blocks [57], and each block consists of a multi-head self-attention block and an MLP block, both having LayerNorm (LN) ...
- **p. 2 / 1. Introduction - extractive PDF cue:** For each triplet, we show the masked image (left), our MAE reconstruction† (middle), and the ground-truth (right).

## Source Evidence Cues

- **p. 3 / 3. Approach - extractive PDF cue:** Like all autoencoders, our approach has an encoder that maps the observed signal to a latent representation, and a decoder that reconstructs the original signal ...
- **p. 3 / 3. Approach - extractive PDF cue:** Unlike classical autoencoders, we adopt an asymmetric design that allows the encoder to operate only on the partial, observed signal (without mask tokens) and a ...
- **p. 4 / 3. Approach - extractive PDF cue:** The MAE decoder is only used during pre-training to perform the image reconstruction task (only the encoder is used to produce image representations for recognition).
- **p. 4 / 3. Approach - extractive PDF cue:** Therefore, the decoder architecture can be flexibly designed in a manner that is independent of the encoder design.
- **p. 11 / A. Implementation Details - extractive PDF cue:** It has a stack of Transformer blocks [57], and each block consists of a multi-head self-attention block and an MLP block, both having LayerNorm (LN) ...
- **p. 7 / 4.3. Partial Fine-tuning - extractive PDF cue:** While the MAE representations are less linearly separable, they are stronger non-linear features and perform well when a non-linear head is tuned.
- **p. 8 / 4.3. Partial Fine-tuning - extractive PDF cue:** These observations suggest that linear separability is not the sole metric for evaluating representation quality.
- **Detected method headings:** 3. Approach (p. 3); method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | Like all autoencoders, our approach has an encoder that maps the observed signal to a latent representation, and a decoder that reconstructs ... | p. 3 (3. Approach), p. 3 (3. Approach) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | Unlike classical autoencoders, we adopt an asymmetric design that allows the encoder to operate only on the partial, observed signal (without mask ... | p. 3 (3. Approach), p. 4 (3. Approach) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | The MAE decoder is only used during pre-training to perform the image reconstruction task (only the encoder is used to produce image ... | p. 4 (3. Approach), p. 4 (3. Approach) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3. Approach - extractive PDF cue:** Our loss function computes the mean squared error (MSE) between the reconstructed and original images in the pixel space.
- **p. 4 / 3. Approach - extractive PDF cue:** This choice is purely result-driven: computing the loss on all pixels leads to a slight decrease in accuracy (e.g., ∼0.5%).
- **p. 11 / A. Implementation Details - extractive PDF cue:** Our recipe can finish training with no NaN loss.
- **p. 11 / A. Implementation Details - extractive PDF cue:** A NaN loss is frequently observed during training.
- **p. 12 / A. Implementation Details - extractive PDF cue:** config value optimizer AdamW base learning rate 1e-4 weight decay 0.3 optimizer momentum β1, β2=0.9, 0.95 batch size 4096 learning rate schedule cosine decay warmup ...
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 4 (3. Approach), p. 4 (3. Approach), p. 11 (A. Implementation Details), p. 11 (A. Implementation Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | decoder, output, reshaped, form, reconstructed, image, MAE, masks, random, patches, input, reconstructs, missing, pixel | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | decoder, output, reshaped, form, reconstructed, image, MAE, masks, random, patches | task state 또는 decision variable | body cue; notation verify |
| Action/output | Driven, analysis, present, simple, effective, scalable, form, masked, autoencoder, MAE | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | loss, function, computes, mean, squared, error, MSE, between, reconstructed, original | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3. Approach - extractive PDF cue:** The decoder's output is reshaped to form a reconstructed image.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our MAE masks random patches from the input image and reconstructs the missing patches in the pixel space.
- **p. 2 / 1. Introduction - extractive PDF cue:** (iii) The autoencoder's decoder, which maps the latent representation back to the input, plays a different role between reconstructing text and images.
- **p. 3 / 3. Approach - extractive PDF cue:** This allows us to train very large encoders with only a fraction of compute and memory.
- **p. 3 / 3. Approach - extractive PDF cue:** Finally, the highly sparse input creates an opportunity for designing an efficient encoder, introduced next.
- **p. 4 / 3. Approach - extractive PDF cue:** Our MAE reconstructs the input by predicting the pixel values for each masked patch.
- **p. 8 / 4.3. Partial Fine-tuning - extractive PDF cue:** These observations suggest that linear separability is not the sole metric for evaluating representation quality.
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | The time and memory efficiency makes our MAE favorable for training very large models. | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | In addition, memory is greatly reduced, which can enable training even larger models or speeding up more by large-batch training. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | The time and memory efficiency makes our MAE favorable for training very large models. | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | Pre-training setting. config value optimizer AdamW base learning rate 1e-3 weight decay 0.05 optimizer momentum β1, β2=0.9, 0.999 layer-wise lr decay [10, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3. Approach - extractive PDF cue:** The MAE decoder is only used during pre-training to perform the image reconstruction task (only the encoder is used to produce image representations for recognition).
- **p. 11 / A. Implementation Details - extractive PDF cue:** 3Alternatively, we can pre-compute the mean and std of the features and use the normalized features to train linear classifiers. config value optimizer AdamW [39] ...
- **p. 11 / A. Implementation Details - extractive PDF cue:** Pre-training setting. config value optimizer AdamW base learning rate 1e-3 weight decay 0.05 optimizer momentum β1, β2=0.9, 0.999 layer-wise lr decay [10, 2] 0.75 batch ...
- **p. 12 / A. Implementation Details - extractive PDF cue:** We fine-tune end-to-end for 100 epochs with a batch size of 16.
- **p. 12 / A. Implementation Details - extractive PDF cue:** The hyper-parameters we search for are the learning rate, weight decay, drop path rate, and fine-tuning epochs.
- **p. 5 / 4.1. Main Properties - extractive PDF cue:** The decoder width is 512, and the mask ratio is 75%. †: This entry is estimated by training ten epochs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Like, autoencoders, encoder, maps, observed, signal, latent, representation, decoder, reconstructs, original, Unlike, classical, adopt, asymmetric, design, allows, operate, only, partial.
- **Relevant PDF headings:** 3. Approach (p. 3); method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | It makes sense of the gestalt of objects and scenes, which cannot be simply completed by extending lines or textures. | p. 4 (4.1. Main Properties), p. 5 (4.1. Main Properties) |
| Core objective / transformation | The following is a comparison between ViT-L trained from scratch vs. fine-tuned from our baseline MAE: scratch, original [16] scratch, our impl. ... | p. 4 (4. ImageNet Experiments), p. 11 (A. Implementation Details) |
| Downstream transfer boundary | More significantly, with the larger ViT-L, our MAE pre-training outperforms supervised pre-training by 4.0 points (53.3 vs. | p. 8 (5. Transfer Learning Experiments), p. 5 (4.1. Main Properties) |

## Failure and Ablation Link

- **p. 11 / A. Implementation Details - extractive PDF cue:** We note that the layer does not break the linear property, and it can be absorbed into the linear classifier after training: it is essentially ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 13. Robustness evaluation on ImageNet variants (top-1 accuracy, except for IN-C [27] which evaluates mean corruption error). We test the same MAE models (Table ...
- **p. 4 / 4. ImageNet Experiments - extractive PDF cue:** We use ViT-Large (ViT-L/16) [16] as the backbone in our ablation study.
- **p. 5 / 4.1. Main Properties - extractive PDF cue:** MAE ablation experiments with ViT-L/16 on ImageNet-1K.
- **p. 5 / 4.1. Main Properties - extractive PDF cue:** An encoder without mask tokens is more accurate and faster (Table 2). case ft lin pixel (w/o norm) 84.9 73.5 pixel (w/ norm) 85.4 73.9 ...
- **p. 6 / 4.1. Main Properties - extractive PDF cue:** Our ablations thus far are based on 800-epoch pre-training.
- **p. 6 / 4.1. Main Properties - extractive PDF cue:** Middle: block-wise sampling [2] that removes large random blocks.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3. Approach), p. 3 (3. Approach), p. 4 (3. Approach), p. 4 (3. Approach), p. 11 (A. Implementation Details), p. 7 (4.3. Partial Fine-tuning), objective p. 4 (3. Approach), p. 4 (3. Approach), p. 11 (A. Implementation Details), p. 11 (A. Implementation Details), p. 12 (A. Implementation Details), temporal p. 5 (4.1. Main Properties), p. 5 (4.1. Main Properties), p. 6 (4.1. Main Properties), p. 6 (4.1. Main Properties), p. 2 (1. Introduction), p. 3 (3. Approach).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
