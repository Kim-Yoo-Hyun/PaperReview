# Vision Transformers for Dense Prediction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2103.13413.
> PDF retrieval source: https://arxiv.org/pdf/2103.13413. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, monocular depth, Vision Transformer, geometry
- Official paper: https://arxiv.org/abs/2103.13413
- Full-text retrieval: https://arxiv.org/pdf/2103.13413
- Code/Project: https://github.com/isl-org/DPT
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 While these techniques can significantly improve prediction quality, the networks are still bottlenecked by their fundamental building block: the convolution.를 문제로 두고, In this work, we introduce the dense prediction transformer (DPT).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce dense vision transformers, an architecture that leverages vision transformers in place of convolutional networks as a backbone for dense prediction tasks.
- **p. 1 / Abstract - extractive body cue:** We assemble tokens from various stages of the vision transformer into image-like representations at various resolutions and progressively combine them into full-resolution predictions using a ...
- **p. 1 / Abstract - extractive body cue:** The transformer backbone processes representations at a constant and relatively high resolution and has a global receptive field at every stage.
- **p. 1 / Abstract - extractive body cue:** These properties allow the dense vision transformer to provide finer-grained and more globally coherent predictions when compared to fully-convolutional networks.
- **p. 1 / Abstract - extractive body cue:** Our experiments show that this architecture yields substantial improvements on dense prediction tasks, especially when a large amount of training data is available.
- **p. 1 / 1. Introduction - extractive body cue:** While these techniques can significantly improve prediction quality, the networks are still bottlenecked by their fundamental building block: the convolution.
- **p. 1 / 1. Introduction - extractive body cue:** Virtually all existing architectures for dense prediction are based on convolutional networks [6, 31, 34, 42, 49, 50, 53].

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we introduce the dense prediction transformer (DPT).
- **p. 1 / 1. Introduction - extractive body cue:** Downsampling enables a progressive increase of the receptive field, the grouping of low-level features into abstract highlevel features, and simultaneously ensures that memory and computational ...
- **p. 3 / 3. Architecture - extractive body cue:** We propose a simple three-stage Reassemble operation to recover image-like representations from the output tokens of arbitrary layers of the transformer encoder: Reassemble ˆ D ...
- **p. 2 / 1. Introduction - extractive body cue:** We show that these properties are especially advantageous for dense prediction tasks as they naturally lead to fine-grained and globally coherent predictions.
- **p. 4 / 3. Architecture - extractive body cue:** We use features from the first and second ResNet block from the embedding network and stages l = {9, 12} when using ViT-Hybrid.
- **p. 3 / 3. Architecture - extractive body cue:** We use three variants in our work: ViT-Base, which uses the patch-based embedding procedure and features 12 transformer layers; ViT-Large, which uses the same embedding ...
- **p. 2 / 3. Architecture - extractive body cue:** Transformers transform the set of tokens using sequential blocks of multi-headed self-attention (MHSA) [39], which relate tokens to each other to transform the representation.
- **p. 2 / 3. Architecture - extractive body cue:** We leverage vision transformers [11] as the backbone, show how the representation that is produced by this encoder can be effectively transformed into dense predictions, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We propose a simple three-stage Reassemble operation to recover image-like representations from the output tokens of arbitrary layers of the transformer encoder: Reassemble ˆ D s (t) = (Resamples ◦Concatenate ◦Read)(t), where ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3. Architecture), p. 3 (3. Architecture) |
| State/latent | simple, three-stage, Reassemble, operation, recover, image-like, representations, output, tokens, arbitrary, layers, transformer | geometry, map, object/relationship state | p. 3 (3. Architecture), p. 3 (3. Architecture), p. 1 (1. Introduction) |
| Output/action | The input tokens are transformed using L transformer layers into new representations tl, where l refers to the output of the l-th transformer layer. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Architecture), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | This is in stark contrast to convolutional networks, which progressively increase their receptive field as features pass through consecutive convolution and downsampling layers. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 2 (3. Architecture), p. 3 (3. Architecture), p. 3 (3. Architecture) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we introduce the dense prediction transformer (DPT).
- **p. 1 / 1. Introduction - extractive body cue:** Downsampling enables a progressive increase of the receptive field, the grouping of low-level features into abstract highlevel features, and simultaneously ensures that memory and computational ...
- **p. 3 / 3. Architecture - extractive body cue:** We propose a simple three-stage Reassemble operation to recover image-like representations from the output tokens of arbitrary layers of the transformer encoder: Reassemble ˆ D ...
- **p. 2 / 1. Introduction - extractive body cue:** We show that these properties are especially advantageous for dense prediction tasks as they naturally lead to fine-grained and globally coherent predictions.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 3. Evaluation on KITTI (Eigen split). Zero-shot cross-dataset transfer. Table 1 shows the re- sults of zero-shot transfer to different datasets that were not ...
- **p. 4 / 4. Experiments - extractive body cue:** For both tasks, we show that DPT can significantly improve accuracy when compared to convolutional networks with a similar capacity, especially if a large training ...
- **p. 8 / 4.3. Ablations - extractive body cue:** ViT-Base has comparable performance to ResNext101WSL, while ViT-Hybrid and ViT-Large improve performance even though they have been pretrained on significantly less data.
- **p. 6 / 4.1. Monocular Depth Estimation - extractive body cue:** Our architecture matches or improves state-of-the-art performance on both datasets in all metrics.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (Figure/Table caption), p. 4 (4. Experiments) |
| Embodiment/environment | We split each dataset into a training set and a small validation set of about 1,000 images total. | hardware/simulator version and reset protocol | p. 7 (4.3. Ablations), p. 5 (4.1. Monocular Depth Estimation) |
| Dataset/benchmark | For both tasks, we show that DPT can significantly improve accuracy when compared to convolutional networks with a similar capacity, especially if a large training dataset is available. | role, split, size and leakage | p. 7 (4.3. Ablations), p. 5 (4.1. Monocular Depth Estimation), p. 4 (4. Experiments), p. 4 (4.1. Monocular Depth Estimation) |
| Metric | For both tasks, we show that DPT can significantly improve accuracy when compared to convolutional networks with a similar capacity, especially if a large training dataset is available. | definition, denominator, direction and uncertainty | p. 4 (4. Experiments), p. 5 (4.1. Monocular Depth Estimation), p. 6 (4.2. Semantic Segmentation) |
| Baseline/ablation | The hybrid and large backbones consistently outperform the convolutional baselines. | fair input/data/compute/action matching | p. 8 (4.3. Ablations), p. 8 (4.3. Ablations), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 4.1. Monocular Depth Estimation - extractive body cue:** We thus first align predictions of the initial network to each training sample using the robust alignment procedure described in [30].
- **p. 8 / 4.3. Ablations - extractive body cue:** We observe that the performance of DPT variants indeed degrades more gracefully as inference resolution increases.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 While these techniques can significantly improve prediction quality, the networks are still bottlenecked by their fundamental building block: the convolution.를 문제로 두고, In this work, we introduce the dense prediction transformer (DPT).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Architecture), p. 4 (3. Architecture), p. 3 (3. Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
