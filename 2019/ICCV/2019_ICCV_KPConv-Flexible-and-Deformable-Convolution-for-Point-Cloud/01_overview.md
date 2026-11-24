# KPConv: Flexible and Deformable Convolution for Point Clouds

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1904.08889.
> PDF retrieval source: https://arxiv.org/pdf/1904.08889. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / ICCV
- Authors: Hugues Thomas, Charles R. Qi, Jean-Emmanuel Deschaud, Beatriz Marcotegui, Francois Goulette, Leonidas Guibas
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: point cloud, 3D Vision
- Official paper: https://arxiv.org/abs/1904.08889
- Full-text retrieval: https://arxiv.org/pdf/1904.08889
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content_ICCV_2019/papers/Thomas_KPConv_Flexible_and_Deformable_Convolution_for_Point_Clouds_ICCV_2019_paper.pdf)

## Why This Paper Is Here

KPConv는 불규칙한 점군의 각 이웃이 커널 점에서 얼마나 떨어졌는지에 따라 가중치를 배분해 점 좌표에 직접 합성곱을 적용한다. [PDF 1쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Thomas_KPConv_Flexible_and_Deformable_Convolution_for_Point_Clouds_ICCV_2019_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Thomas_KPConv_Flexible_and_Deformable_Convolution_for_Point_Clouds_ICCV_2019_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present Kernel Point Convolution1 (KPConv), a new design of point convolution, i.e. that operates on point clouds without any intermediate representation.
- **p. 1 / Abstract - extractive body cue:** The convolution weights of KPConv are located in Euclidean space by kernel points, and applied to the input points close to them.
- **p. 1 / Abstract - extractive body cue:** Its capacity to use any number of kernel points gives KPConv more flexibility than fixed grid convolutions.
- **p. 1 / Abstract - extractive body cue:** Furthermore, these locations are continuous in space and can be learned by the network.
- **p. 1 / Abstract - extractive body cue:** Therefore, KPConv can be extended to deformable convolutions that learn to adapt kernel points to local geometry.
- **p. 1 / 1. Introduction - extractive body cue:** Input points with a constant scalar feature (in grey) are convolved through a KPConv that is defined by a set of kernel points (in black) ...
- **p. 2 / 1. Introduction - extractive body cue:** KPConv also consists of a set of local 3D filters, but overcomes previous point convolution limitations as shown in related work.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we propose a deformable version of our convolution [7], which consists of learning local shifts applied to the kernel points (see Figure 3).
- **p. 2 / 1. Introduction - extractive body cue:** KPConv also consists of a set of local 3D filters, but overcomes previous point convolution limitations as shown in related work.
- **p. 1 / 1. Introduction - extractive body cue:** Various approaches have been proposed to handle such data, and can be grouped into different categories that we will develop in the related work section.
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive body cue:** Combining analogy with successful image networks and empirical studies, we designed two network architectures for the classification and the segmentation tasks.
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive body cue:** Our convolutional blocks are designed like bottleneck ResNet blocks [12] with a KPConv replacing the image convolution, batch normalization and leaky ReLu activation.
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive body cue:** Skip links are used to pass the features between intermediate layers of the encoder and the decoder.
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive body cue:** The encoder part is the same as in KP-CNN, and the decoder part uses nearest upsampling to get the final pointwise features.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Input points with a constant scalar feature (in grey) are convolved through a KPConv that is defined by a set of kernel points (in black) with filter weights on each point. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | Input, points, constant, scalar, feature, grey, convolved, through, KPConv, defined, kernel, black | geometry, map, object/relationship state | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | The kernel weights are thus carried by points, like the input features, and their area of influence is defined by a correlation function. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | geometric accuracy, semantic consistency와 planning/manipulation utility | geometric accuracy, semantic consistency와 planning/manipulation utility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 연속 공간에 둔 커널 점의 위치를 고정하는 방식과 입력에 따라 이동시키는 방식을 제시하고, 변형 커널이 입력 표면을 따르도록 정규화한다. [PDF 3쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Thomas_KPConv_Flexible_and_Deformable_Convolution_for_Point_Clouds_ICCV_2019_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Thomas_KPConv_Flexible_and_Deformable_Convolution_for_Point_Clouds_ICCV_2019_paper.pdf#page=4)
- 물체 분류와 실내·실외 장면 분할에서 점군 합성곱을 평가하고 커널 변형에 따른 차이를 분석했다. [PDF 5쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Thomas_KPConv_Flexible_and_Deformable_Convolution_for_Point_Clouds_ICCV_2019_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Thomas_KPConv_Flexible_and_Deformable_Convolution_for_Point_Clouds_ICCV_2019_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content_ICCV_2019/papers/Thomas_KPConv_Flexible_and_Deformable_Convolution_for_Point_Clouds_ICCV_2019_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (4.2. 3D Scene Segmentation), p. 8 (4.4. Learned Features and Effective Receptive Field) |
| Embodiment/environment | The 3D scenes in these datasets are too big to be segmented as a whole. | hardware/simulator version and reset protocol | p. 6 (4.2. 3D Scene Segmentation), p. 6 (4.2. 3D Scene Segmentation) |
| Dataset/benchmark | We use Scannet dataset (same parameters as before) and use the official validation set, because the test set cannot be used for such evaluations. | role, split, size and leakage | p. 6 (4.2. 3D Scene Segmentation), p. 6 (4.2. 3D Scene Segmentation), p. 7 (4.3. Ablation Study), p. 8 (4.4. Learned Features and Effective Receptive Field) |
| Metric | Table 6. Semantic segmentation IoU scores on S3DIS Area-5. Additionally, we give the mean class recall, a measure that some previous works call mean class accuracy. | definition, denominator, direction and uncertainty | p. 14 (Figure/Table caption), p. 6 (Figure/Table caption), p. 6 (4.2. 3D Scene Segmentation) |
| Baseline/ablation | As shown on Table 1, our networks outperform other state-of-the-art methods using only points (we do not take into account methods using normals as additional input). | fair input/data/compute/action matching | p. 5 (4.1. 3D Shape Classification and Segmentation), p. 6 (4.1. 3D Shape Classification and Segmentation), p. 6 (4.2. 3D Scene Segmentation) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.3. Ablation Study - extractive body cue:** We use Scannet dataset (same parameters as before) and use the official validation set, because the test set cannot be used for such evaluations.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Kernel Point Network Architectures), p. 6 (4.2. 3D Scene Segmentation)이다.
