# Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2401.10891.
> PDF retrieval source: https://arxiv.org/pdf/2401.10891. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: Lihe Yang, Bingyi Kang, Zilong Huang, Xiaogang Xu, Jiashi Feng, Hengshuang Zhao
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: depth, 3D Vision
- Official paper: https://arxiv.org/abs/2401.10891
- Full-text retrieval: https://arxiv.org/pdf/2401.10891
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Depth Anything은 대규모 비표지 영상에 의사 깊이 레이블을 생성해 단안 영상에서 상대 깊이를 추정하는 모델을 학습한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Depth_Anything_Unleashing_the_Power_of_Large-Scale_Unlabeled_Data_CVPR_2024_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This work presents Depth Anything1, a highly practical solution for robust monocular depth estimation.
- **p. 1 / Abstract - extractive body cue:** Without pursuing novel technical modules, we aim to build a simple yet powerful foundation model dealing with any images under any circumstances.
- **p. 1 / Abstract - extractive body cue:** To this end, we scale up the dataset by designing a data engine to collect and automatically annotate large-scale unlabeled data (∼62M), which significantly enlarges ...
- **p. 1 / Abstract - extractive body cue:** We investigate two simple yet effective strategies that make data scaling-up promising.
- **p. 1 / Abstract - extractive body cue:** First, a more challenging optimization target is created by leveraging data augmentation tools.
- **p. 1 / 1. Introduction - extractive body cue:** However, this has been underexplored due to the difficulty of building datasets with tens of millions of depth labels.
- **p. 2 / 1. Introduction - extractive body cue:** To address the dilemma, we propose to challenge the student model with a more difficult optimization target when learning the pseudo labels.

## Core Idea

- **p. 5 / Method - extractive body cue:** This allows our method to enjoy both the semantic-aware representation from DINOv2 and the part-level discriminative representation from depth supervision.
- **p. 2 / 1. Introduction - extractive body cue:** To address the dilemma, we propose to challenge the student model with a more difficult optimization target when learning the pseudo labels.
- **p. 2 / 1. Introduction - extractive body cue:** Therefore, considering the excellent performance of DINOv2 in semantic-related tasks, we propose to maintain the rich semantic priors from it with a simple feature alignment ...
- **p. 6 / 4.4. Fine-tuned to Semantic Segmentation - extractive body cue:** In our method, we design our MDE model to inherit the rich semantic priors from a pre-trained encoder via a simple feature alignment constraint.
- **p. 7 / Method - extractive body cue:** More importantly, as emphasized in Section 4.4, this auxiliary constraint also enables our trained encoder to serve as a key component in a multi-task visual ...
- **p. 5 / Method - extractive body cue:** Thus, it is not beneficial to exhaustively enforce our depth model to produce exactly the same features as the frozen encoder.
- **p. 5 / Method - extractive body cue:** The feature alignment loss is formulated as: \ma t h c a l {L } _{f eat} = 1 - \frac {1}{HW}\sum _{i=1}^{HW}\cos (f_i, f'_i), ...
- **p. 6 / 4.3. Fine-tuned to Metric Depth Estimation - extractive body cue:** In this part, we use our ViT-L encoder for fine-tuning.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Meantime, we use ControlNet to synthesize new images from the depth map. | RGB-D, image set, point cloud, depth와 camera pose | p. 8 (Method), p. 6 (4.4. Fine-tuned to Semantic Segmentation) |
| State/latent | Meantime, ControlNet, synthesize, images, depth, Similar, observations, hold, ADE20K, dataset, Table, goal | geometry, map, object/relationship state | p. 8 (Method), p. 6 (4.4. Fine-tuned to Semantic Segmentation), p. 1 (1. Introduction) |
| Output/action | Similar observations hold on the ADE20K dataset [89] in Table 8. | point map, pose, scene graph, affordance 또는 query result | p. 6 (4.4. Fine-tuned to Semantic Segmentation), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | Best, second best results. depth model with an auxiliary feature alignment loss. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (Method), p. 5 (Method), p. 6 (4.4. Fine-tuned to Semantic Segmentation) |

## Main Claims and Actual Contribution

- 레이블이 있는 자료로 학습한 교사가 비표지 영상을 감독하고, 학생에게 강한 영상 증강과 의미 특징 보존 손실을 적용한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Depth_Anything_Unleashing_the_Power_of_Large-Scale_Unlabeled_Data_CVPR_2024_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Depth_Anything_Unleashing_the_Power_of_Large-Scale_Unlabeled_Data_CVPR_2024_paper.pdf#page=4)
- 여러 데이터셋의 무학습 전이에서 상대 깊이를 평가하고, 미터 단위 깊이 추정에는 별도의 미세조정과 평가를 수행했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Depth_Anything_Unleashing_the_Power_of_Large-Scale_Unlabeled_Data_CVPR_2024_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Depth_Anything_Unleashing_the_Power_of_Large-Scale_Unlabeled_Data_CVPR_2024_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Depth_Anything_Unleashing_the_Power_of_Large-Scale_Unlabeled_Data_CVPR_2024_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 5 (4.2. Zero-Shot Relative Depth Estimation) |
| Embodiment/environment | Moreover, our ViT-S model, whose scale is less than 1/10 of the MiDaS model, even outperforms MiDaS on several unseen datasets, including Sintel, DDAD, and ETH3D. | hardware/simulator version and reset protocol | p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 5 (4.2. Zero-Shot Relative Depth Estimation) |
| Dataset/benchmark | We visualize our model predictions on the six unseen datasets in Figure 3. | role, split, size and leakage | p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 8 (4.6. Qualitative Results), p. 9 (9. More Qualitative Results) |
| Metric | Our model exhibits higher depth estimation accuracy and stronger robustness. | definition, denominator, direction and uncertainty | p. 9 (9. More Qualitative Results), p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 5 (4.2. Zero-Shot Relative Depth Estimation) |
| Baseline/ablation | Moreover, our ViT-S model, whose scale is less than 1/10 of the MiDaS model, even outperforms MiDaS on several unseen datasets, including Sintel, DDAD, and ETH3D. | fair input/data/compute/action matching | p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 8 (Figure/Table caption), p. 5 (4.1. Implementation Details) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** In this work, we present Depth Anything, a highly practical solution to robust monocular depth estimation.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Zero-shot relative depth estimation. Better: AbsRel ↓, δ1 ↑. We compare with the best model from MiDaS v3.1. Note that MiDaS does not ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our model exhibits impressive generalization ability across extensive unseen scenes. Left two columns: COCO [36]. Middle two: SA-1B [27] (a hold-out unseen set). ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. In total, our Depth Anything is trained on 1.5M labeled images and 62M unlabeled images jointly. our easy-to-acquire and diverse unlabeled images will ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Our pipeline. Solid line: flow of labeled images, dotted line: unlabeled images. We especially highlight the value of large-scale unlabeled images. The S ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 8. Transferring our MDE encoder to ADE20K for semantic segmentation. We use Mask2Former as our segmentation model. since the labeled images are already sufficient. ...
- **p. 8 / 4.6. Qualitative Results - extractive body cue:** Our model is robust to test images from various domains.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (Method)이다.
