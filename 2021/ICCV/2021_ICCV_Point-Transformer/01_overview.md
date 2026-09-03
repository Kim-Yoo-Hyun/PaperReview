# Point Transformer

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2012.09164.
> PDF retrieval source: https://arxiv.org/pdf/2012.09164. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: point cloud, 3D Vision
- Official paper: https://arxiv.org/abs/2012.09164
- Full-text retrieval: https://arxiv.org/pdf/2012.09164
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 A variety of approaches to deep learning on 3D point clouds have arisen in response to this challenge.를 문제로 두고, It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Self-attention networks have revolutionized natural language processing and are making impressive strides in image analysis tasks such as image classification and object detection.
- **p. 1 / Abstract - extractive body cue:** Inspired by this success, we investigate the application of self-attention networks to 3D point cloud processing.
- **p. 1 / Abstract - extractive body cue:** We design self-attention layers for point clouds and use these to construct self-attention networks for tasks such as semantic scene segmentation, object part segmentation, and ...
- **p. 1 / Abstract - extractive body cue:** Our Point Transformer design improves upon prior work across domains and tasks.
- **p. 1 / Abstract - extractive body cue:** For example, on the challenging S3DIS dataset for large-scale semantic scene segmentation, the Point Transformer attains an mIoU of 70.4% on Area 5, outperforming the ...
- **p. 1 / 1. Introduction - extractive body cue:** A variety of approaches to deep learning on 3D point clouds have arisen in response to this challenge.
- **p. 1 / 1. Introduction - extractive body cue:** Sparse convolutional networks relieve these limitations by operating only on voxels that are not empty [9, 3].

## Core Idea

- **p. 6 / 4.3. Object Part Segmentation - extractive body cue:** It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions include the following. • We design a highly expressive Point Transformer layer for point cloud processing.
- **p. 1 / 1. Introduction - extractive body cue:** We show that Point Transformers are remarkably effective in 3D deep learning tasks, both at the level of detailed object analysis and large-scale parsing of ...
- **p. 1 / 1. Introduction - extractive body cue:** We flesh out this intuition and develop a self-attention layer for 3D point cloud processing.
- **p. 5 / 3.5. Network Architecture - extractive body cue:** The feature encoder in point transformer networks for semantic segmentation and classification has five stages that operate on progressively downsampled point sets.
- **p. 5 / 3.5. Network Architecture - extractive body cue:** To pool feature vectors from P1 onto P2, we use a kNN graph on P1.
- **p. 4 / 3.5. Network Architecture - extractive body cue:** Note that the point transformer is the primary feature aggregation operator throughout the network.
- **p. 6 / 4.2. Shape Classification - extractive body cue:** To probe the representation learned by the Point Transformer, we conduct shape retrieval by retrieving nearest neighbors in the space of the output features produced ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Denote the point set provided as input to the transition down module as P1 and denote the output point set as P2. | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3.5. Network Architecture), p. 6 (Method) |
| State/latent | Denote, point, provided, input, transition, down, module, output, mAcc, DShapeNets, voxel, VoxNet | geometry, map, object/relationship state | p. 5 (3.5. Network Architecture), p. 6 (Method), p. 1 (1. Introduction) |
| Output/action | Method input mAcc OA 3DShapeNets [47] voxel 77.3 84.7 VoxNet [23] voxel 83.0 85.9 Subvolume [26] voxel 86.0 89.2 MVCNN [34] image - 90.1 PointNet [25] point 86.2 89.2 A-SCN [48] point ... | point map, pose, scene graph, affordance 또는 query result | p. 6 (Method), p. 1 (1. Introduction), p. 6 (4.2. Shape Classification) |
| Objective/outcome | (Note that we did not use loss-balancing during training, which can boost category mIoU.) | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (4.3. Object Part Segmentation), p. 5 (3.5. Network Architecture) |

## Main Claims and Actual Contribution

- **p. 6 / 4.3. Object Part Segmentation - extractive body cue:** It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions include the following. • We design a highly expressive Point Transformer layer for point cloud processing.
- **p. 1 / 1. Introduction - extractive body cue:** We show that Point Transformers are remarkably effective in 3D deep learning tasks, both at the level of detailed object analysis and large-scale parsing of ...
- **p. 1 / 1. Introduction - extractive body cue:** We flesh out this intuition and develop a self-attention layer for 3D point cloud processing.
- **p. 5 / 4.1. Semantic Segmentation - extractive body cue:** Point Transformer also substantially outperforms all prior models under 6-fold cross-validation.
- **p. 5 / 4.1. Semantic Segmentation - extractive body cue:** The Point Transformer outperforms all prior models according to all metrics in both evaluation modes.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Shape classification results on the ModelNet40 dataset.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Semantic segmentation results on the S3DIS dataset, evaluated on Area 5.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 5 (4.1. Semantic Segmentation), p. 5 (4.1. Semantic Segmentation) |
| Embodiment/environment | The S3DIS [1] dataset for semantic scene parsing consists of 271 rooms in six areas from three different buildings. | hardware/simulator version and reset protocol | p. 5 (4.1. Semantic Segmentation), p. 5 (4. Experiments) |
| Dataset/benchmark | The S3DIS [1] dataset for semantic scene parsing consists of 271 rooms in six areas from three different buildings. | role, split, size and leakage | p. 5 (4.1. Semantic Segmentation), p. 5 (4. Experiments) |
| Metric | For evaluation metrics, we use mean classwise intersection over union (mIoU), mean of classwise accuracy (mAcc), and overall pointwise accuracy (OA). | definition, denominator, direction and uncertainty | p. 5 (4.1. Semantic Segmentation), p. 5 (4. Experiments) |
| Baseline/ablation | On Area 5, the Point Transformer attains mIoU/mAcc/OA of 70.4%/76.5%/90.8%, outperforming all prior work by multiple percentage points in each metric. | fair input/data/compute/action matching | p. 5 (4.1. Semantic Segmentation), p. 5 (4.1. Semantic Segmentation), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Transformers have revolutionized natural language processing and are making impressive gains in 2D image analysis.
- **p. 8 / 5. Conclusion - extractive body cue:** Inspired by this progress, we have developed a transformer architecture for 3D point clouds.
- **p. 8 / 5. Conclusion - extractive body cue:** Transformers are perhaps an even more natural fit for point cloud processing than they are for language or image processing, because point clouds are essentially ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 A variety of approaches to deep learning on 3D point clouds have arisen in response to this challenge.를 문제로 두고, It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.3. Object Part Segmentation), p. 5 (3.5. Network Architecture), p. 5 (3.5. Network Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
