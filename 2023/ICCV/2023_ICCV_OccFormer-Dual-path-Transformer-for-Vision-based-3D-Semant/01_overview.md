# OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2304.05316.
> PDF retrieval source: https://arxiv.org/pdf/2304.05316. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, semantic, occupancy, Transformer
- Official paper: https://arxiv.org/abs/2304.05316
- Full-text retrieval: https://arxiv.org/pdf/2304.05316
- Code/Project: https://github.com/zhangyp15/OccFormer
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the 3D convolution suffers from several limitations.를 문제로 두고, For the encoder part, we propose the dual-path transformer block to unleash the capacity of selfattention while limiting the quadratic complexity.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The vision-based perception for autonomous driving has undergone a transformation from the bird-eye-view (BEV) representations to the 3D semantic occupancy.
- **p. 1 / Abstract - extractive body cue:** Compared with the BEV planes, the 3D semantic occupancy further provides structural information along the vertical direction.
- **p. 1 / Abstract - extractive body cue:** This paper presents OccFormer, a dual-path transformer network to effectively process the 3D volume for semantic occupancy prediction.
- **p. 1 / Abstract - extractive body cue:** OccFormer achieves a long-range, dynamic, and efficient encoding of the camera-generated 3D voxel features.
- **p. 1 / Abstract - extractive body cue:** It is obtained by decomposing the heavy 3D processing into the local and global transformer pathways along the horizontal plane.
- **p. 1 / 1. Introduction - extractive body cue:** However, the 3D convolution suffers from several limitations.
- **p. 1 / 1. Introduction - extractive body cue:** Also, its spatial invariance cannot well process the sparse and discontinuous 3D features, generated from the state-of-the-art practices for image-to-3D transformation [40, 20, 29].

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** For the encoder part, we propose the dual-path transformer block to unleash the capacity of selfattention while limiting the quadratic complexity.
- **p. 2 / 3.1. Overview - extractive body cue:** The image encoder consists of a backbone network for extracting multi-scale features and a neck for further fusion.
- **p. 2 / 1. Introduction - extractive body cue:** Our method surpasses TPVFormer by 1.4% mIoU and generates more complete and realistic predictions for 3D semantic occupancy prediction.
- **p. 3 / 3.2. Dual-path Transformer Encoder - extractive body cue:** We introduce the dual-path processing with more details in the following paragraph.
- **p. 3 / 3.2. Dual-path Transformer Encoder - extractive body cue:** To pursue long-range, dynamic, and efficient processing of the 3D feature volumes, we propose the dual-path transformer block to build the 3D encoder.
- **p. 3 / 3.1. Overview - extractive body cue:** The pipeline consists of the image encoder for extracting multi-scale 2D features, the image-to-3D transformation for lifting the 2D features to 3D volumes, and the ...
- **p. 2 / 3.1. Overview - extractive body cue:** With the monocular image or multi-camera images as the input, the multi-scale features are first extracted by the image encoder, and then lifted to 3D ...
- **p. 4 / 3.3. Transformer Occupancy Decoder - extractive body cue:** With the above interactions, each processed feature volume is enhanced by the multi-scale semantic information, which facilitates the following transformer decoder.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The output of the image encoder is one fused feature map with 1 16 of the input resolution. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (3.1. Overview), p. 3 (3.1. Overview) |
| State/latent | output, image, encoder, fused, feature, input, resolution, Transformer, Occupancy, Decoder, Depth, Distribution | geometry, map, object/relationship state | p. 2 (3.1. Overview), p. 3 (3.1. Overview), p. 1 (1. Introduction) |
| Output/action | Input Image Image Encoder Transformer Occupancy Decoder Depth Distribution Voxel Pooling Depth Net Context Net 3D Feature Volume Masked Attention Query Features Mask Context Feature Dual-path Transformer Blocks Conv Dual-path Transforme ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Overview), p. 1 (1. Introduction), p. 2 (3.1. Overview) |
| Objective/outcome | The matching cost includes the class loss and the binary mask loss. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.4. Loss Functions), p. 5 (3.4. Loss Functions) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** For the encoder part, we propose the dual-path transformer block to unleash the capacity of selfattention while limiting the quadratic complexity.
- **p. 2 / 3.1. Overview - extractive body cue:** The image encoder consists of a backbone network for extracting multi-scale features and a neck for further fusion.
- **p. 2 / 1. Introduction - extractive body cue:** Our method surpasses TPVFormer by 1.4% mIoU and generates more complete and realistic predictions for 3D semantic occupancy prediction.
- **p. 3 / 3.2. Dual-path Transformer Encoder - extractive body cue:** We introduce the dual-path processing with more details in the following paragraph.
- **p. 3 / 3.2. Dual-path Transformer Encoder - extractive body cue:** To pursue long-range, dynamic, and efficient processing of the 3D feature volumes, we propose the dual-path transformer block to build the 3D encoder.
- **p. 6 / 4.1. Datasets - extractive body cue:** The proposed OccFormer outperforms the only vision-based method TPVFormer [21] and achieves comparable performance with LiDAR-based methods.
- **p. 7 / 4.4. Main Results - extractive body cue:** OccFormer achieves comparable IoU for scene completion and significantly better performance for the SSC mIoU.
- **p. 8 / 4.5. Ablation Studies - extractive body cue:** On the other hand, the proposed class-guided sampling significantly outperforms the default uniform sampling because it can better adapt to the task of 3D semantic ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.1. Datasets), p. 7 (4.4. Main Results) |
| Embodiment/environment | The SemanticKITTI dataset [2] is based on the popular KITTI Odometry Benchmark [16] and focuses on the semantic scene understanding with LiDAR points and front cameras. | hardware/simulator version and reset protocol | p. 5 (4.1. Datasets), p. 6 (4.1. Datasets) |
| Dataset/benchmark | The nuScenes dataset [3] is a large-scale autonomous driving dataset, collected in Boston and Singapore. | role, split, size and leakage | p. 5 (4.1. Datasets), p. 6 (4.1. Datasets), p. 6 (4.1. Datasets), p. 7 (4.4. Main Results) |
| Metric | OccFormer achieves comparable IoU for scene completion and significantly better performance for the SSC mIoU. | definition, denominator, direction and uncertainty | p. 7 (4.4. Main Results), p. 6 (4.3. Metrics), p. 7 (4.4. Main Results) |
| Baseline/ablation | 3, our method outperforms the only vision-based method TPVFormer and achieves comparable performance with the state-of-the-art LiDAR-based methods. | fair input/data/compute/action matching | p. 7 (4.4. Main Results), p. 6 (4.2. Implementation Details), p. 7 (4.5. Ablation Studies) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5. Conclusion - extractive body cue:** It indicates that the predicted semantic occupancy from TPVFormer, despite reasonable visualizations, fails to contain accurate 3D positions.
- **p. 7 / 4.4. Main Results - extractive body cue:** Note that our method requires only one model to perform both the LiDAR segmentation and the semantic occupancy prediction, while the TPVFormer [21] model trained ...
- **p. 9 / 5. Conclusion - extractive body cue:** Second, we remove the windowed attention in the global path, whose weights are shared with the local path, and observe a degradation of around 0.5 ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the 3D convolution suffers from several limitations.를 문제로 두고, For the encoder part, we propose the dual-path transformer block to unleash the capacity of selfattention while limiting the quadratic complexity.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overview), p. 2 (3.1. Overview), p. 2 (3.1. Overview) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
