# Masked Autoencoders Are Scalable Vision Learners

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2111.06377.
> PDF retrieval source: https://arxiv.org/pdf/2111.06377. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: Vision Foundation Model, self-supervised, representation
- Official paper: https://arxiv.org/abs/2111.06377
- Full-text retrieval: https://arxiv.org/pdf/2111.06377
- Code/Project: https://github.com/facebookresearch/mae
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 This architectural gap, however, has been addressed with the introduction of Vision Transformers (ViT) [16] and should no longer present an obstacle.를 문제로 두고, Driven by this analysis, we present a simple, effective, and scalable form of a masked autoencoder (MAE) for visual representation learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper shows that masked autoencoders (MAE) are scalable self-supervised learners for computer vision.
- **p. 1 / Abstract - extractive body cue:** Our MAE approach is simple: we mask random patches of the input image and reconstruct the missing pixels.
- **p. 1 / Abstract - extractive body cue:** First, we develop an asymmetric encoder-decoder architecture, with an encoder that operates only on the visible subset of patches (without mask tokens), along with a ...
- **p. 1 / Abstract - extractive body cue:** Second, we find that masking a high proportion of the input image, e.g., 75%, yields a nontrivial and meaningful self-supervisory task.
- **p. 1 / Abstract - extractive body cue:** Coupling these two designs enables us to train large models efficiently and effectively: we accelerate training (by 3× or more) and improve accuracy.
- **p. 1 / 1. Introduction - extractive body cue:** This architectural gap, however, has been addressed with the introduction of Vision Transformers (ViT) [16] and should no longer present an obstacle.
- **p. 2 / 1. Introduction - extractive body cue:** Our MAE learns very high-capacity models that generalize well.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Driven by this analysis, we present a simple, effective, and scalable form of a masked autoencoder (MAE) for visual representation learning.
- **p. 11 / A. Implementation Details - extractive body cue:** It has a stack of Transformer blocks [57], and each block consists of a multi-head self-attention block and an MLP block, both having LayerNorm (LN) ...
- **p. 2 / 1. Introduction - extractive body cue:** For each triplet, we show the masked image (left), our MAE reconstruction† (middle), and the ground-truth (right).
- **p. 3 / 3. Approach - extractive body cue:** Like all autoencoders, our approach has an encoder that maps the observed signal to a latent representation, and a decoder that reconstructs the original signal ...
- **p. 3 / 3. Approach - extractive body cue:** This allows us to train very large encoders with only a fraction of compute and memory.
- **p. 3 / 3. Approach - extractive body cue:** Unlike classical autoencoders, we adopt an asymmetric design that allows the encoder to operate only on the partial, observed signal (without mask tokens) and a ...
- **p. 4 / 3. Approach - extractive body cue:** The MAE decoder is only used during pre-training to perform the image reconstruction task (only the encoder is used to produce image representations for recognition).
- **p. 4 / 3. Approach - extractive body cue:** Therefore, the decoder architecture can be flexibly designed in a manner that is independent of the encoder design.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The decoder's output is reshaped to form a reconstructed image. | 논문이 명시한 observation과 task input | p. 4 (3. Approach), p. 2 (1. Introduction) |
| State/latent | decoder, output, reshaped, form, reconstructed, image, MAE, masks, random, patches, input, reconstructs | task state 또는 decision variable | p. 4 (3. Approach), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | Our MAE masks random patches from the input image and reconstructs the missing patches in the pixel space. | paper-specific output/action | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Approach) |
| Objective/outcome | Our loss function computes the mean squared error (MSE) between the reconstructed and original images in the pixel space. | primary task objective와 closed-loop behavior | p. 4 (3. Approach), p. 4 (3. Approach), p. 11 (A. Implementation Details) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Driven by this analysis, we present a simple, effective, and scalable form of a masked autoencoder (MAE) for visual representation learning.
- **p. 11 / A. Implementation Details - extractive body cue:** It has a stack of Transformer blocks [57], and each block consists of a multi-head self-attention block and an MLP block, both having LayerNorm (LN) ...
- **p. 2 / 1. Introduction - extractive body cue:** For each triplet, we show the masked image (left), our MAE reconstruction† (middle), and the ground-truth (right).
- **p. 3 / 3. Approach - extractive body cue:** Like all autoencoders, our approach has an encoder that maps the observed signal to a latent representation, and a decoder that reconstructs the original signal ...
- **p. 3 / 3. Approach - extractive body cue:** This allows us to train very large encoders with only a fraction of compute and memory.
- **p. 8 / 5. Transfer Learning Experiments - extractive body cue:** More significantly, with the larger ViT-L, our MAE pre-training outperforms supervised pre-training by 4.0 points (53.3 vs.
- **p. 5 / 4.1. Main Properties - extractive body cue:** By removing the mask token from the encoder, we constrain the encoder to always see real patches and thus improve accuracy.
- **p. 5 / 4.1. Main Properties - extractive body cue:** A deep decoder can improve linear probing accuracy. dim ft lin 128 84.9 69.1 256 84.8 71.3 512 84.9 73.5 768 84.4 73.1 1024 84.3 ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (5. Transfer Learning Experiments), p. 5 (4.1. Main Properties) |
| Embodiment/environment | It makes sense of the gestalt of objects and scenes, which cannot be simply completed by extending lines or textures. | hardware/simulator version and reset protocol | p. 4 (4.1. Main Properties), p. 5 (4.1. Main Properties) |
| Dataset/benchmark | Transfer learning accuracy on classification datasets, using MAE pre-trained on IN1K and then fine-tuned. | role, split, size and leakage | p. 4 (4.1. Main Properties), p. 5 (4.1. Main Properties), p. 8 (5. Transfer Learning Experiments), p. 8 (5. Transfer Learning Experiments) |
| Metric | Table 13. Robustness evaluation on ImageNet variants (top-1 accuracy, except for IN-C [27] which evaluates mean corruption error). We test the same MAE models (Table 3) on different Im- ageNet validation sets, ... | definition, denominator, direction and uncertainty | p. 12 (Figure/Table caption), p. 7 (4.2. Comparisons with Previous Results), p. 4 (4. ImageNet Experiments) |
| Baseline/ablation | The following is a comparison between ViT-L trained from scratch vs. fine-tuned from our baseline MAE: scratch, original [16] scratch, our impl. baseline MAE 76.5 82.5 84.9 We note that it is ... | fair input/data/compute/action matching | p. 4 (4. ImageNet Experiments), p. 11 (A. Implementation Details), p. 7 (4.2. Comparisons with Previous Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Discussion and Conclusion - extractive body cue:** We hope this perspective will inspire future work.
- **p. 4 / 4.1. Main Properties - extractive body cue:** It makes sense of the gestalt of objects and scenes, which cannot be simply completed by extending lines or textures.
- **p. 5 / 4.1. Main Properties - extractive body cue:** In this case, there is a gap between pre-training and deploying: this encoder has a large portion of mask tokens in its input in pretraining, ...
- **p. 6 / 4.1. Main Properties - extractive body cue:** Using pixels does not suffer from these problems.
- **p. 11 / A. Implementation Details - extractive body cue:** Directly applying the previous recipes to these larger models does not work.
- **p. 11 / A. Implementation Details - extractive body cue:** Our MAE does not use relative position or layer scaling (which are used in the code of [2]).
- **p. 5 / 4.1. Main Properties - extractive body cue:** This gap may degrade accuracy in deployment.

## Why Read It

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 This architectural gap, however, has been addressed with the introduction of Vision Transformers (ViT) [16] and should no longer present an obstacle.를 문제로 두고, Driven by this analysis, we present a simple, effective, and scalable form of a masked autoencoder (MAE) for visual representation learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (3. Approach), p. 3 (3. Approach) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
