# Language-driven Semantic Segmentation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2201.03546.
> PDF retrieval source: https://arxiv.org/pdf/2201.03546. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, semantic, open-vocabulary, alignment
- Official paper: https://arxiv.org/abs/2201.03546
- Full-text retrieval: https://arxiv.org/pdf/2201.03546
- Code/Project: https://github.com/isl-org/lang-seg
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 The main reason for the restricted label sets in existing methods is the cost of annotating images to produce sufficient training data.를 문제로 두고, Our approach enables the synthesis of zero-shot semantic segmentation models on the fly.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** We present LSeg, a novel model for language-driven semantic image segmentation.
- **p. 1 / ABSTRACT - extractive body cue:** LSeg uses a text encoder to compute embeddings of descriptive input labels (e.g., "grass" or "building") together with a transformer-based image encoder that computes dense ...
- **p. 1 / ABSTRACT - extractive body cue:** The image encoder is trained with a contrastive objective to align pixel embeddings to the text embedding of the corresponding semantic class.
- **p. 1 / ABSTRACT - extractive body cue:** The text embeddings provide a flexible label representation in which semantically similar labels map to similar regions in the embedding space (e.g., "cat" and "furry").
- **p. 1 / ABSTRACT - extractive body cue:** This allows LSeg to generalize to previously unseen categories at test time, without retraining or even requiring a single additional training sample.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The main reason for the restricted label sets in existing methods is the cost of annotating images to produce sufficient training data.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Since the text encoder is trained to embed closely related concepts near one another (for example, "dog" is closer to "pet" than to "vehicle"), we ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our approach enables the synthesis of zero-shot semantic segmentation models on the fly.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this work, we present a simple approach to leveraging modern language models to increase the flexibility and generality of semantic segmentation models.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose to use state-of-the-art text encoders that have been co-trained on visual data, such as CLIP, to embed labels from the training set into ...
- **p. 1 / ABSTRACT - extractive body cue:** We present LSeg, a novel model for language-driven semantic image segmentation.
- **p. 5 / C Input Label Set - extractive body cue:** In contrast, our approach can dynamically handle label sets with varying length, content, and order.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Since the text encoder is trained to embed closely related concepts near one another (for example, "dog" is closer to "pet" than to "vehicle"), we ...
- **p. 4 / C Input Label Set - extractive body cue:** We use an additional post-processing module that spatially regularizes and upsamples the predictions to the original input resolution.
- **p. 1 / ABSTRACT - extractive body cue:** The image encoder is trained with a contrastive objective to align pixel embeddings to the text embedding of the corresponding semantic class.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We propose to use state-of-the-art text encoders that have been co-trained on visual data, such as CLIP, to embed labels from the training set into an embedding space and to train a ... | camera/depth stream, pose, map와 language goal | p. 2 (1 INTRODUCTION), p. 4 (C Input Label Set) |
| State/latent | state-of-the-art, text, encoders, have, been, co-trained, visual, data, CLIP, embed, labels, training | robot pose, free-space/semantic map와 local goal | p. 2 (1 INTRODUCTION), p. 4 (C Input Label Set), p. 1 (ABSTRACT) |
| Output/action | In other words, there should be no interactions between the input channels, whose order is defined by the order of the words and can thus be arbitrary. | collision-free trajectory 또는 velocity command | p. 4 (C Input Label Set), p. 1 (ABSTRACT), p. 4 (C Input Label Set) |
| Objective/outcome | During training, we minimize a per-pixel softmax with cross-entropy loss (with temperature scaling) as is standard in semantic segmentation1. | goal reach, safety, localization error와 replanning latency | p. 4 (C Input Label Set), p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our approach enables the synthesis of zero-shot semantic segmentation models on the fly.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this work, we present a simple approach to leveraging modern language models to increase the flexibility and generality of semantic segmentation models.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose to use state-of-the-art text encoders that have been co-trained on visual data, such as CLIP, to embed labels from the training set into ...
- **p. 1 / ABSTRACT - extractive body cue:** We present LSeg, a novel model for language-driven semantic image segmentation.
- **p. 5 / C Input Label Set - extractive body cue:** In contrast, our approach can dynamically handle label sets with varying length, content, and order.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We notice that a consistent improvement can be achieved by adding a few regularization blocks.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The strongest improvement is achieved by stacking two BottleneckBlocks, an addition to the architecture that incurs little overhead.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We observe that using RN50×16 achieves the best performance among all text encoders and surpasses the weakest ViT-B/32 text encoder by 2.5%.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Embodiment/environment | However, due to a lack of a standardized protocol and sufficient datasets and baselines for the zero-shot setting, we compare LSeg to zero- and few-shot semantic segmentation models on few-shot benchmarks. | hardware/simulator version and reset protocol | p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Dataset/benchmark | It contains a significant number of unseen or unannotated objects in comparison to previous datasets such as PASCAL and COCO. | role, split, size and leakage | p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Metric | Note that few-shot methods have access to more information and are thus expected to yield higher accuracy. | definition, denominator, direction and uncertainty | p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Baseline/ablation | Our model (with the same ResNet101 backbone) outperforms the zero-shot baseline by a considerable margin across folds and datasets and is even competitive with several few-shot methods. | fair input/data/compute/action matching | p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4 EXPERIMENTS - extractive body cue:** We hope that these failure cases can inform future work, which could involve augmenting training with negative samples or building fine-grained language-driven semantic segmentation models ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** While LSeg in general achieves very promising results, we also observe some failure cases, as illustrated in Figure 6.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Example results. LSeg is able to handle unseen labels as well as label sets of arbitrary length and order. This enables flexible synthesis ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 The main reason for the restricted label sets in existing methods is the cost of annotating images to produce sufficient training data.를 문제로 두고, Our approach enables the synthesis of zero-shot semantic segmentation models on the fly.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (C Input Label Set) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
