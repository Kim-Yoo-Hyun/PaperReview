# DINOv2: Learning Robust Visual Features without Supervision

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2304.07193.
> PDF retrieval source: https://arxiv.org/pdf/2304.07193. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / TMLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: self-supervised, representation
- Official paper: https://arxiv.org/abs/2304.07193
- Full-text retrieval: https://arxiv.org/pdf/2304.07193
- Code/Project: https://github.com/facebookresearch/dinov2
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 A major difficulty when dealing with images in the wild is to rebalance concepts and avoid overfitting on a few dominant modes.를 문제로 두고, Most of our technical contributions are tailored toward stabilizing and accelerating discriminative self-supervised learning when scaling in model and data sizes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The recent breakthroughs in natural language processing for model pretraining on large quantities of data have opened the way for similar foundation models in computer ...
- **p. 1 / Abstract - extractive body cue:** These models could greatly simplify the use of images in any system by producing generalpurpose visual features, i.e., features that work across image distributions and ...
- **p. 1 / Abstract - extractive body cue:** This work shows that existing pretraining methods, especially self-supervised methods, can produce such features if trained on enough curated data from diverse sources.
- **p. 1 / Abstract - extractive body cue:** We revisit existing approaches and combine different techniques to scale our pretraining in terms of data and model size.
- **p. 1 / Abstract - extractive body cue:** Most of the technical contributions aim at accelerating and stabilizing the training at scale.
- **p. 2 / 1 Introduction - extractive body cue:** A major difficulty when dealing with images in the wild is to rebalance concepts and avoid overfitting on a few dominant modes.
- **p. 2 / 1 Introduction - extractive body cue:** This is explained by the lack of control over the data quality and diversity, which are essential to produce good features.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Most of our technical contributions are tailored toward stabilizing and accelerating discriminative self-supervised learning when scaling in model and data sizes.
- **p. 2 / 1 Introduction - extractive body cue:** We gathered a small but diverse corpus of 142M images to validate our approach.
- **p. 3 / 1 Introduction - extractive body cue:** We show performance on eight types of vision tasks, as presented in Sec.
- **p. 31 / B.1 Unsupervised pre-training - extractive body cue:** We use MLP feed-forward networks for distilled models, and SwiGLU (Shazeer, 2020) when training from scratch.
- **p. 31 / B.2 High-Resolution adaptation - extractive body cue:** We initialise the model with the pretrained weights then train it for 10k iterations with the same procedure as the original pretraining.
- **p. 29 / B.1 Unsupervised pre-training - extractive body cue:** We use hyperparameters shown in Table 16, ViT architectures described in Table 17.
- **p. 29 / B.1 Unsupervised pre-training - extractive body cue:** For unsupervised pre-training we build on the DINO and iBOT codebases.
- **p. 30 / B.1 Unsupervised pre-training - extractive body cue:** We kept a few datasets aside in order to evaluate performance outside of the pretraining domain.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Additionally, the features output by self-supervised models have been shown to exhibit various useful properties, and have enabled enabled a wide variety of applications (Amir et al., 2022; Tumanyan et al., 2022; ... | 논문이 명시한 observation과 task input | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| State/latent | Additionally, features, output, self-supervised, models, have, been, exhibit, various, useful, properties, enabled | task state 또는 decision variable | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 31 (B.1 Unsupervised pre-training) |
| Output/action | Our family of models drastically improves over the previous state of the art in self-supervised learning and reaches performance comparable with weaklysupervised features. | paper-specific output/action | p. 3 (1 Introduction), p. 31 (B.1 Unsupervised pre-training), p. 2 (1 Introduction) |
| Objective/outcome | All models run for 625k iterations with optimizer AdamW, an initial LayerScale value of 1e-5, a weight decay cosine schedule from 0.04 to 0.2, a learning rate warmup of 100k iterations, a ... | primary task objective와 closed-loop behavior | p. 31 (B.1 Unsupervised pre-training), p. 29 (B.1 Unsupervised pre-training), p. 31 (B.1 Unsupervised pre-training) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Most of our technical contributions are tailored toward stabilizing and accelerating discriminative self-supervised learning when scaling in model and data sizes.
- **p. 2 / 1 Introduction - extractive body cue:** We gathered a small but diverse corpus of 142M images to validate our approach.
- **p. 3 / 1 Introduction - extractive body cue:** We show performance on eight types of vision tasks, as presented in Sec.
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 6: Role of resolution. Performance of ViT-L/16 trained on ImageNet-1k at fixed resolution ("224" and "416") or trained at 224 then 416 for a ...
- **p. 13 / 7 Results - extractive body cue:** Interestingly, our model significantly outperforms OpenCLIP ViT-G/14 on both variants of iNaturalist (+8.6% and +9.7% for 2018 and 2021 respectively), and lags slightly behind on ...
- **p. 14 / 7 Results - extractive body cue:** We see that our features significantly outperform both SSL (+41% mAP on Oxford-Hard), and weakly-supervised (+34% mAP on Oxford-Hard) ones.
- **p. 14 / 7 Results - extractive body cue:** Our model significantly outperforms state-of-the-art SSL models, with most notable differences on Stanford Cars (+14.8% versus DINO ViT-B/8) and FGVC Aircraft (+14.8% versus iBOT ViT-L/16).
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Ablation of the source of pretraining data. We compare the INet-22k dataset that was used in iBOT to our dataset, LVD-142M. Each model ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (Figure/Table caption), p. 13 (7 Results) |
| Embodiment/environment | This benchmark covers scenes, objects (food, cars, planes), and textures. | hardware/simulator version and reset protocol | p. 13 (7 Results), p. 13 (7 Results) |
| Dataset/benchmark | Accuracy on 12 benchmarks covering objects, scenes and textures following the evaluation protocol proposed in Chen et al. | role, split, size and leakage | p. 13 (7 Results), p. 13 (7 Results), p. 14 (7 Results), p. 14 (7 Results) |
| Metric | Table 3: (a) Effect of the KoLeo loss term. (b) Effect of the iBOT Masked Image Modeling (MIM) loss term. Evaluation performed on ImageNet-{1k,A} (classification with linear probe, accuracy %), ADE-20k (segmentation ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 11 (7 Results), p. 31 (B.3 Linear probing evaluation) |
| Baseline/ablation | When comparing with state-of-the-art SSL methods, our models shows drastically better robustness (+29.6% on A (Hendrycks et al., 2021b), +22.1% on R (Hendrycks et al., 2021a) and +23.0% on Sketch (Wang et ... | fair input/data/compute/action matching | p. 12 (7 Results), p. 14 (7 Results), p. 11 (7 Results) |

## Explicit Limitations and Failure Boundary

- **p. 15 / 7 Results - extractive body cue:** This procedure is extremely simple but cannot easily produce high-resolution segmentations. +ms: a boosted version of the linear setup.
- **p. 16 / 7 Results - extractive body cue:** This observation supports the intuition that caption-based feature learning fails to learn subtle patterns like this one.
- **p. 12 / 7 Results - extractive body cue:** When comparing with state-of-the-art SSL methods, our models shows drastically better robustness (+29.6% on A (Hendrycks et al., 2021b), +22.1% on R (Hendrycks et al., ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 5: Supervised finetuning on ImageNet-1k. We use the pipeline of Touvron et al. (2022) to finetune our encoders on ImageNet-1k at resolutions 224 × ...
- **p. 16 / 7 Results - extractive body cue:** Out-of-distribution generalization.
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 8: Examples of out-of-distribution examples with frozen DINOv2-g features and a linear probe. PCA of patch features. We show the results of the principal ...
- **p. 18 / 7 Results - extractive body cue:** We also observe that the model is robust to style (image versus drawing), and to large variation of poses (see the elephant).

## Why Read It

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 A major difficulty when dealing with images in the wild is to rebalance concepts and avoid overfitting on a few dominant modes.를 문제로 두고, Most of our technical contributions are tailored toward stabilizing and accelerating discriminative self-supervised learning when scaling in model and data sizes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 31 (B.1 Unsupervised pre-training), p. 31 (B.2 High-Resolution adaptation), p. 29 (B.1 Unsupervised pre-training), p. 29 (B.1 Unsupervised pre-training) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
