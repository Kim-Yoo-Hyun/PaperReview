# UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_UniPre3D_Unified_Pre-training_of_3D_Point_Cloud_Models_with_Cross-Modal_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_UniPre3D_Unified_Pre-training_of_3D_Point_Cloud_Models_with_Cross-Modal_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Gaussian Splatting, point cloud, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_UniPre3D_Unified_Pre-training_of_3D_Point_Cloud_Models_with_Cross-Modal_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_UniPre3D_Unified_Pre-training_of_3D_Point_Cloud_Models_with_Cross-Modal_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 A key challenge lies in the greater scale diversity of point clouds compared to images.를 문제로 두고, In conclusion, the contributions of our paper are as follows: (1) We propose UniPre3D, the first unified pretraining method for point clouds of any scale and 3D models of any architecture.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The scale diversity of point cloud data presents significant challenges in developing unified representation learning techniques for 3D vision.
- **p. 1 / Abstract - extractive body cue:** Currently, there are few unified 3D models, and no existing pre-training method is equally effective for both object- and scene-level point clouds.
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce UniPre3D, the first unified pretraining method that can be seamlessly applied to point clouds of any scale and 3D models ...
- **p. 1 / Abstract - extractive body cue:** Our approach predicts Gaussian primitives as the pre-training task and employs differentiable Gaussian splatting to render images, enabling precise pixel-level supervision and end-to-end optimization.
- **p. 1 / Abstract - extractive body cue:** To further regulate the complexity of the pre-training task and direct the model's focus toward geometric structures, we integrate 2D features from pretrained image models ...
- **p. 1 / 1. Introduction - extractive body cue:** A key challenge lies in the greater scale diversity of point clouds compared to images.
- **p. 2 / 1. Introduction - extractive body cue:** tance loss is computationally expensive and fails to supervise large-scale data.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In conclusion, the contributions of our paper are as follows: (1) We propose UniPre3D, the first unified pretraining method for point clouds of any scale ...
- **p. 3 / 3.2. Overall Pipeline - extractive body cue:** To further enhance the scale adaptability, we propose the integration of a pre-trained image model, which provides supplementary color and texture information through our novel ...
- **p. 2 / 1. Introduction - extractive body cue:** This enables end-toend optimization and allows for precise pixel-wise supervision in the image domain.
- **p. 1 / 1. Introduction - extractive body cue:** We propose a unified pre-training method that is applicable and effective to both object- and scene-level point clouds and models. tain hundreds of times more ...
- **p. 3 / 3.2. Overall Pipeline - extractive body cue:** Based on this observation, we propose using the image domain as an intermediary to reduce the scale differences in point cloud data.
- **p. 4 / 3.3. Scale-Adaptive Cross-Modal Fusion - extractive body cue:** To modulate the difficulty of the pretraining task and enhance the point cloud model's focus on geometry extraction, we propose the integration of pretrained image ...
- **p. 4 / 3.2. Overall Pipeline - extractive body cue:** These 2D features are then encoded into the 3D domain using a learnable but lightweight adaptation block A, followed by back-projection to the 3D space, ...
- **p. 5 / 3.3. Scale-Adaptive Cross-Modal Fusion - extractive body cue:** We then treat the back-projected pixels as a pseudo point cloud P2D and merge it with P3D, the output from the first encoding layer of ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Based on this observation, we propose using the image domain as an intermediary to reduce the scale differences in point cloud data. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.2. Overall Pipeline), p. 4 (3.3. Scale-Adaptive Cross-Modal Fusion) |
| State/latent | observation, image, domain, intermediary, reduce, scale, differences, point, cloud, data, modulate, difficulty | geometry, map, object/relationship state | p. 3 (3.2. Overall Pipeline), p. 4 (3.3. Scale-Adaptive Cross-Modal Fusion), p. 3 (3.2. Overall Pipeline) |
| Output/action | To modulate the difficulty of the pretraining task and enhance the point cloud model's focus on geometry extraction, we propose the integration of pretrained image features with the intermediate 3D features derived ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.3. Scale-Adaptive Cross-Modal Fusion), p. 3 (3.2. Overall Pipeline), p. 4 (3.3. Scale-Adaptive Cross-Modal Fusion) |
| Objective/outcome | We employ a pixel-wise supervision Mean Squared Error (MSE) loss during the pre-training process: \ma thca l | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.4. Optimization Objectives), p. 3 (3. Approach), p. 3 (3.2. Overall Pipeline) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In conclusion, the contributions of our paper are as follows: (1) We propose UniPre3D, the first unified pretraining method for point clouds of any scale ...
- **p. 3 / 3.2. Overall Pipeline - extractive body cue:** To further enhance the scale adaptability, we propose the integration of a pre-trained image model, which provides supplementary color and texture information through our novel ...
- **p. 2 / 1. Introduction - extractive body cue:** This enables end-toend optimization and allows for precise pixel-wise supervision in the image domain.
- **p. 1 / 1. Introduction - extractive body cue:** We propose a unified pre-training method that is applicable and effective to both object- and scene-level point clouds and models. tain hundreds of times more ...
- **p. 3 / 3.2. Overall Pipeline - extractive body cue:** Based on this observation, we propose using the image domain as an intermediary to reduce the scale differences in point cloud data.
- **p. 6 / 4.2.1. Object-level Fine-tuning - extractive body cue:** For part segmentation in Table 2, UniPre3D achieves the best performance on the mIoUC metric and competitive results with TAP on mIoUI.
- **p. 7 / 4.2.2. Scene-level Fine-tuning - extractive body cue:** For instance segmentation in Table 4, UniPre3D also achieves state-ofthe-art performance across most benchmarks, with particularly strong results on ScanNet200.
- **p. 7 / 4.2.2. Scene-level Fine-tuning - extractive body cue:** When compared to prior scene pre-training approaches with the SparseUNet backbone, UniPre3D also achieves the best results on ScanNet20 and ScanNet200.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.2.1. Object-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning) |
| Embodiment/environment | For scene-level pre-training, we utilize the real-world ScanNetV2 dataset [10] with more than 1,500 scans of indoor scenes. | hardware/simulator version and reset protocol | p. 5 (4.1. Pre-training), p. 6 (4.2.1. Object-level Fine-tuning) |
| Dataset/benchmark | Model Pre-train mIoUC mIoUI PointNet [34] ✗ 80.4 83.7 PointNet++ [35] ✗ 81.9 85.1 DGCNN [55] ✗ 82.3 85.2 KPConv [45] ✗ 85.1 86.4 Standard Transformer [48] ✗ 83.4 84.7 Point-BERT [67] ... | role, split, size and leakage | p. 5 (4.1. Pre-training), p. 6 (4.2.1. Object-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning), p. 5 (4.1. Pre-training) |
| Metric | Across more advanced models [14, 29, 71], UniPre3D delivers consistent and substantial performance gains, even on Mamba3D [14] with already high accuracy. | definition, denominator, direction and uncertainty | p. 6 (4.2.1. Object-level Fine-tuning), p. 6 (4.2.1. Object-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning) |
| Baseline/ablation | Additionally, we use the advanced PointTransformerV3 [59] as the backbone, which demonstrates significantly higher baseline performance than SparseUNet, to show that UniPre3D remains effective for models with high inherent performance. | fair input/data/compute/action matching | p. 5 (4.1. Pre-training), p. 6 (4.2.1. Object-level Fine-tuning), p. 7 (4.3. Ablation Studies) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.4. Limitations - extractive body cue:** Even though we make an effective effort towards unified pre-training, there are still some limitations to be resolved in future research.
- **p. 7 / 4.2.2. Scene-level Fine-tuning - extractive body cue:** However, the application of pointbased models has been limited to S3DIS, and their performance still falls short of voxel-based models.
- **p. 8 / 5. Conclusion - extractive body cue:** Our unified approach consistently outperforms prior scale-specific pre-training methods on most benchmarks, underscoring its robustness and adaptability.
- **p. 6 / 4.1. Pre-training - extractive body cue:** However, UniPre3D accurately predicts both geometry and color for other perspectives, demonstrating the 3D backbone is pre-trained to extract robust geometric features.
- **p. 7 / 4.2.2. Scene-level Fine-tuning - extractive body cue:** Model Pre-train ScanNet20 ScanNet200 S3DIS Point-based Model PointNet [34] ✗ - - 41.1 PointNet++ [35] ✗ - - 53.5 PointNeXt [39] ✗ 71.5 - 70.5 ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 A key challenge lies in the greater scale diversity of point clouds compared to images.를 문제로 두고, In conclusion, the contributions of our paper are as follows: (1) We propose UniPre3D, the first unified pretraining method for point clouds of any scale and 3D models of any architecture.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.3. Scale-Adaptive Cross-Modal Fusion), p. 4 (3.2. Overall Pipeline) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
