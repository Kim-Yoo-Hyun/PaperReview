# KPConv: Flexible and Deformable Convolution for Point Clouds

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1904.08889.
> PDF retrieval source: https://arxiv.org/pdf/1904.08889. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: point cloud, 3D Vision
- Official paper: https://arxiv.org/abs/1904.08889
- Full-text retrieval: https://arxiv.org/pdf/1904.08889
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Input points with a constant scalar feature (in grey) are convolved through a KPConv that is defined by a set of kernel points (in black) with filter weights on each point. 를 문제로 두고, Furthermore, we propose a deformable version of our convolution [7], which consists of learning local shifts applied to the kernel points (see Figure 3).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we propose a deformable version of our convolution [7], which consists of learning local shifts applied to the kernel points (see Figure 3).
- **p. 2 / 1. Introduction - extractive body cue:** KPConv also consists of a set of local 3D filters, but overcomes previous point convolution limitations as shown in related work.
- **p. 1 / 1. Introduction - extractive body cue:** Various approaches have been proposed to handle such data, and can be grouped into different categories that we will develop in the related work section.
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive body cue:** Combining analogy with successful image networks and empirical studies, we designed two network architectures for the classification and the segmentation tasks.
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive body cue:** Our convolutional blocks are designed like bottleneck ResNet blocks [12] with a KPConv replacing the image convolution, batch normalization and leaky ReLu activation.
- **p. 6 / 4.2. 3D Scene Segmentation - extractive body cue:** Among these 4 datasets, KPConv deformable kernels improved the results on Paris-Lille-3D and S3DIS while the rigid version was better on Scannet and Semantic3D.
- **p. 8 / 4.4. Learned Features and Effective Receptive Field - extractive body cue:** This adaptive behavior shows that deformable KPConv improves the network ability to adapt to the geometry of the scene objects, and explains the better performances ...
- **p. 5 / 4.1. 3D Shape Classification and Segmentation - extractive body cue:** As shown on Table 1, our networks outperform other state-of-the-art methods using only points (we do not take into account methods using normals as additional ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Input points with a constant scalar feature (in grey) are convolved through a KPConv that is defined by a set of kernel points (in black) with filter weights on each point. 를 문제로 두고, Furthermore, we propose a deformable version of our convolution [7], which consists of learning local shifts applied to the kernel points (see Figure 3).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Kernel Point Network Architectures), p. 5 (3.4. Kernel Point Network Architectures), p. 6 (4.2. 3D Scene Segmentation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
