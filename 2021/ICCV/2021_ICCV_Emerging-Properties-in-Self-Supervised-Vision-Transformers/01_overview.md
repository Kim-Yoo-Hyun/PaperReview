# Emerging Properties in Self-Supervised Vision Transformers

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2104.14294.
> PDF retrieval source: https://arxiv.org/pdf/2104.14294. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: Vision Foundation Model, self-supervised, representation
- Official paper: https://arxiv.org/abs/2104.14294
- Full-text retrieval: https://arxiv.org/pdf/2104.14294
- Code/Project: https://github.com/facebookresearch/dino
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 text specific, many existing self-supervised methods have shown their potential on images with convnets [10, 12, 30, 33].를 문제로 두고, However, our method shares also similarities with knowledge distillation [35] and we present it under this angle.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we question if self-supervised learning provides new properties to Vision Transformer (ViT) [19] that stand out compared to convolutional networks (convnets).
- **p. 1 / Abstract - extractive body cue:** Beyond the fact that adapting self-supervised methods to this architecture works particularly well, we make the following observations: first, self-supervised ViT features contain explicit information ...
- **p. 1 / Abstract - extractive body cue:** Second, these features are also excellent k-NN classifiers, reaching 78.3% top-1 on ImageNet with a small ViT.
- **p. 1 / Abstract - extractive body cue:** Our study also underlines the importance of momentum encoder [33], multi-crop training [10], and the use of small patches with ViTs.
- **p. 1 / Abstract - extractive body cue:** We implement our findings into a simple self-supervised method, called DINO, which we interpret as a form of self-distillation with no labels.
- **p. 2 / 1. Introduction - extractive body cue:** text specific, many existing self-supervised methods have shown their potential on images with convnets [10, 12, 30, 33].

## Core Idea

- **p. 3 / 3.1. SSL with Knowledge Distillation - extractive body cue:** However, our method shares also similarities with knowledge distillation [35] and we present it under this angle.
- **p. 2 / 1. Introduction - extractive body cue:** Of particular importance, our framework is flexible and works on both convnets and ViTs without the need to modify the architecture, nor adapt internal normalizations ...
- **p. 2 / 1. Introduction - extractive body cue:** Interestingly, our method can work with only a centering and sharpening of the teacher output to avoid collapse, while other popular components such as predictor ...
- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive body cue:** Of particular interest, using an exponential moving average (EMA) on the student weights, i.e., a momentum encoder [33], is particularly well suited for our framework.
- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive body cue:** However, in our framework, its role differs since we do not have a queue nor a contrastive loss, and may be closer to the role ...
- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive body cue:** The neural network g is composed of a backbone f (ViT [19] or ResNet [34]), and of a projection head h: g = h ◦f.
- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive body cue:** While our framework can be stabilized with multiple normalizations [10], it can also work with only a centering and sharpening of the momentum teacher outputs ...
- **p. 3 / 3.1. SSL with Knowledge Distillation - extractive body cue:** Both networks share the same architecture g with different sets of parameters θs and θt.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given an input image x, both networks output probability distributions over K dimensions denoted by Ps and Pt. | 논문이 명시한 observation과 task input | p. 3 (3.1. SSL with Knowledge Distillation), p. 2 (1. Introduction) |
| State/latent | Given, input, image, networks, output, probability, distributions, over, dimensions, denoted, model, passes | task state 또는 decision variable | p. 3 (3.1. SSL with Knowledge Distillation), p. 2 (1. Introduction), p. 3 (3.1. SSL with Knowledge Distillation) |
| Output/action | The model passes two different random transformations of an input image to the student and teacher networks. | paper-specific output/action | p. 2 (1. Introduction), p. 3 (3.1. SSL with Knowledge Distillation), p. 4 (3.1. SSL with Knowledge Distillation) |
| Objective/outcome | Given a fixed teacher network gθt, we learn to match these distributions by minimizing the cross-entropy loss w.r.t. the parameters of the student network θs: min θs H(Pt(x), Ps(x)), (2) where H(a, ... | primary task objective와 closed-loop behavior | p. 3 (3.1. SSL with Knowledge Distillation), p. 3 (3.1. SSL with Knowledge Distillation), p. 4 (3.1. SSL with Knowledge Distillation) |

## Main Claims and Actual Contribution

- **p. 3 / 3.1. SSL with Knowledge Distillation - extractive body cue:** However, our method shares also similarities with knowledge distillation [35] and we present it under this angle.
- **p. 2 / 1. Introduction - extractive body cue:** Of particular importance, our framework is flexible and works on both convnets and ViTs without the need to modify the architecture, nor adapt internal normalizations ...
- **p. 2 / 1. Introduction - extractive body cue:** Interestingly, our method can work with only a centering and sharpening of the teacher output to avoid collapse, while other popular components such as predictor ...
- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive body cue:** Of particular interest, using an exponential moving average (EMA) on the student weights, i.e., a momentum encoder [33], is particularly well suited for our framework.
- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive body cue:** However, in our framework, its role differs since we do not have a queue nor a contrastive loss, and may be closer to the role ...
- **p. 6 / 4.1. Comparing with SSL frameworks on ImageNet - extractive body cue:** While training a larger ViT with DINO improves the performance, reducing the size of the patches ("/8" variants) has a bigger impact on the performance.
- **p. 7 / 4.2. Properties of ViT trained with SSL - extractive body cue:** Finally, self-supervised pretraining greatly improves results on ImageNet (+1-2%).
- **p. 14 / Figure/Table caption - extractive body cue:** Table 13: Methodology comparison for DEIT-small and ResNet-50. We report ImageNet linear and k-NN evaluations validation accuracy after 300 epochs pre-training. All numbers are run ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.1. Comparing with SSL frameworks on ImageNet), p. 7 (4.2. Properties of ViT trained with SSL) |
| Embodiment/environment | 5 that even though our training objective nor our architecture are designed for dense tasks, the performance is competitive on this benchmark. | hardware/simulator version and reset protocol | p. 7 (4.2. Properties of ViT trained with SSL), p. 5 (3.2. Implementation and evaluation protocols) |
| Dataset/benchmark | This evaluation protocol does not require any other hyperparameter tuning, nor data augmentation and can be run with only one pass over the downstream dataset, greatly simplifying the feature evaluation. | role, split, size and leakage | p. 7 (4.2. Properties of ViT trained with SSL), p. 5 (3.2. Implementation and evaluation protocols), p. 5 (3.2. Implementation and evaluation protocols), p. 7 (4.2. Properties of ViT trained with SSL) |
| Metric | Table 14: Relation to MoCo-v2 and BYOL. We ablate the com- ponents that differ between DINO, MoCo-v2 and BYOL: the loss function (cross-entropy, CE, versus InfoNCE, INCE, versus mean- square error, MSE), ... | definition, denominator, direction and uncertainty | p. 15 (Figure/Table caption), p. 5 (3.2. Implementation and evaluation protocols), p. 9 (Figure/Table caption) |
| Baseline/ablation | We observe that DINO features outperform those trained on ImageNet with labels. | fair input/data/compute/action matching | p. 6 (4.2. Properties of ViT trained with SSL), p. 6 (4.2. Properties of ViT trained with SSL), p. 14 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 9 SwAV - extractive body cue:** However, the performance gain from using smaller patches comes at the expense of throughput: when using 5×5 patches, the throughput falls to 44 im/s, vs ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 9: Projection head design w/ or w/o l2-norm bottleneck. linear layers is n + 1 (n from the MLP and 1 from the weight ...
- **p. 5 / 3.2. Implementation and evaluation protocols - extractive body cue:** This evaluation protocol does not require any other hyperparameter tuning, nor data augmentation and can be run with only one pass over the downstream dataset, ...
- **p. 6 / 4.1. Comparing with SSL frameworks on ImageNet - extractive body cue:** This property emerges only when using DINO with ViT architectures, and does not appear with other existing self-supervised methods nor with a ResNet-50.
- **p. 7 / 4.2. Properties of ViT trained with SSL - extractive body cue:** 4, we show that a supervised ViT does not attend well to objects in presence of clutter both qualitatively and quantitatively.
- **p. 8 / 5.1. Importance of the Different Components - extractive body cue:** First, we observe that in the absence of momentum, our framework does not work (row 2) and more advanced operations, SK for example, are required ...
- **p. 9 / 5.2. Impact of the choice of Teacher Network - extractive body cue:** In our setting, using a teacher based on a recent version of the student does not converge.

## Why Read It

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 text specific, many existing self-supervised methods have shown their potential on images with convnets [10, 12, 30, 33].를 문제로 두고, However, our method shares also similarities with knowledge distillation [35] and we present it under this angle.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 4 (3.1. SSL with Knowledge Distillation), p. 4 (3.1. SSL with Knowledge Distillation), p. 3 (3.1. SSL with Knowledge Distillation), p. 3 (3.1. SSL with Knowledge Distillation), p. 6 (4.1. Comparing with SSL frameworks on ImageNet) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
