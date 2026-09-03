# An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2010.11929.
> PDF retrieval source: https://arxiv.org/pdf/2010.11929. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Foundations: Vision and Language Models
- Tier: ARCHIVE
- Tags: Vision Transformer, representation
- Official paper: https://arxiv.org/abs/2010.11929
- Full-text retrieval: https://arxiv.org/pdf/2010.11929
- Code/Project: https://github.com/google-research/vision_transformer
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 Thanks to Transformers' computational efficiency and scalability, it has become possible to train models of unprecedented size, with over 100B parameters (Brown et al., 2020; Lepikhin et al., 2020).를 문제로 두고, The Transformer encoder (Vaswani et al., 2017) consists of alternating layers of multiheaded selfattention (MSA, see Appendix A) and MLP blocks (Eq.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited.
- **p. 1 / ABSTRACT - extractive body cue:** In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure ...
- **p. 1 / ABSTRACT - extractive body cue:** We show that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well ...
- **p. 1 / ABSTRACT - extractive body cue:** When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision Transformer (ViT) attains ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Self-attention-based architectures, in particular Transformers (Vaswani et al., 2017), have become the model of choice in natural language processing (NLP).
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Thanks to Transformers' computational efficiency and scalability, it has become possible to train models of unprecedented size, with over 100B parameters (Brown et al., 2020; ...

## Core Idea

- **p. 3 / 3 METHOD - extractive body cue:** The Transformer encoder (Vaswani et al., 2017) consists of alternating layers of multiheaded selfattention (MSA, see Appendix A) and MLP blocks (Eq.
- **p. 3 / 3 METHOD - extractive body cue:** Similar to BERT's [class] token, we prepend a learnable embedding to the sequence of embedded patches (z0 0 = xclass), whose state at the output ...
- **p. 4 / 3 METHOD - extractive body cue:** Note that this resolution adjustment and patch extraction are the only points at which an inductive bias about the 2D structure of the images is ...
- **p. 4 / 3 METHOD - extractive body cue:** As a special case, the patches can have spatial size 1x1, which means that the input sequence is obtained by simply flattening the spatial dimensions ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Similar to BERT's [class] token, we prepend a learnable embedding to the sequence of embedded patches (z0 0 = xclass), whose state at the output of the Transformer encoder (z0 L) serves ... | 논문이 명시한 observation과 task input | p. 3 (3 METHOD), p. 3 (3 METHOD) |
| State/latent | Similar, BERT, class, token, prepend, learnable, embedding, sequence, embedded, patches, xclass, whose | task state 또는 decision variable | p. 3 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD) |
| Output/action | To handle 2D images, we reshape the image x ∈RH×W ×C into a sequence of flattened 2D patches xp ∈RN×(P 2·C), where (H, W) is the resolution of the original image, C ... | paper-specific output/action | p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD) |
| Objective/outcome | The Vision Transformer can handle arbitrary sequence lengths (up to memory constraints), however, the pre-trained position embeddings may no longer be meaningful. | primary task objective와 closed-loop behavior | p. 4 (3 METHOD), p. 3 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 3 / 3 METHOD - extractive body cue:** The Transformer encoder (Vaswani et al., 2017) consists of alternating layers of multiheaded selfattention (MSA, see Appendix A) and MLP blocks (Eq.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Performance versus pre-training compute for different architectures: Vision Transformers, ResNets, and hybrids. Vision Transformers generally outperform ResNets with the same compu- tational budget. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Comparison with state of the art on popular image classification benchmarks. We re- port mean and standard deviation of the accuracies, averaged over ...
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** The larger model, ViT-H/14, further improves the performance, especially on the more challenging datasets - ImageNet, CIFAR-100, and the VTAB suite.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** This is because the resolution increase during fine-tuning improves the performance.
- **p. 15 / Figure/Table caption - extractive body cue:** Table 5: Top1 accuracy (in %) of Vision Transformer on various datasets when pre-trained on Im- ageNet, ImageNet-21k or JFT300M. These values correspond to Figure ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 8: Scaling different model dimensions of the Vision Transformer. performance of two ResNets - 50x1 and 152x2 - pre-trained on JFT with SGD and ...
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** These modifications improve transfer (Kolesnikov et al., 2020), and we denote the modified model "ResNet (BiT)".

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Embodiment/environment | We transfer the models trained on these dataset to several benchmark tasks: ImageNet on the original validation labels and the cleaned-up ReaL labels (Beyer et al., 2020), CIFAR-10/100 (Krizhevsky, 2009), Oxford-IIIT Pets ... | hardware/simulator version and reset protocol | p. 4 (4 EXPERIMENTS), p. 4 (4 EXPERIMENTS) |
| Dataset/benchmark | The smaller ViT-L/16 model pre-trained on JFT-300M outperforms BiT-L (which is pre-trained on the same dataset) on all tasks, while requiring substantially less computational resources to train. | role, split, size and leakage | p. 4 (4 EXPERIMENTS), p. 4 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS) |
| Metric | VTAB (19 tasks) 65 70 75 80 Accuracy [%] Natural (7 tasks) 70 80 90 Specialized (4 tasks) 80 82 85 88 90 Structured (8 tasks) 50 60 70 ViT-H/14 BiT-L (R152x4) ... | definition, denominator, direction and uncertainty | p. 6 (4 EXPERIMENTS), p. 20 (Figure/Table caption), p. 5 (4 EXPERIMENTS) |
| Baseline/ablation | Vision Transformer models pre-trained on the JFT-300M dataset outperform ResNet-based baselines on all datasets, while taking substantially less computational resources to pre-train. | fair input/data/compute/action matching | p. 6 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 300 M - extractive body cue:** Further analysis of few-shot properties of ViT is an exciting direction of future work.
- **p. 8 / 300 M - extractive body cue:** In this setting data size does not bottleneck the models' performances, and we assess performance versus pre-training cost of each model.

## Why Read It

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 Thanks to Transformers' computational efficiency and scalability, it has become possible to train models of unprecedented size, with over 100B parameters (Brown et al., 2020; Lepikhin et al., 2020).를 문제로 두고, The Transformer encoder (Vaswani et al., 2017) consists of alternating layers of multiheaded selfattention (MSA, see Appendix A) and MLP blocks (Eq.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 3 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 7 (Figure/Table caption) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
