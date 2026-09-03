# VGGT: Visual Geometry Grounded Transformer

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2503.11651.
> PDF retrieval source: https://arxiv.org/pdf/2503.11651. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D reconstruction, geometry, Transformer
- Official paper: https://arxiv.org/abs/2503.11651
- Full-text retrieval: https://arxiv.org/pdf/2503.11651
- Code/Project: https://github.com/facebookresearch/vggt
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Machine learning has often played an important complementary role, addressing tasks that cannot be solved by geometry alone, such as feature matching and monocular depth prediction.를 문제로 두고, To summarize, we make the following contributions: (1) We introduce VGGT, a large feed-forward transformer that, given one, a few, or even hundreds of images of a scene, can predict all its ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present VGGT, a feed-forward neural network that directly infers all key 3D attributes of a scene, including camera parameters, point maps, depth maps, and ...
- **p. 1 / Abstract - extractive body cue:** This approach is a step forward in 3D computer vision, where models have typically been constrained to and specialized for single tasks.
- **p. 1 / Abstract - extractive body cue:** It is also simple and efficient, reconstructing images in under one second, and still outperforming alternatives that require post-processing with visual geometry optimization techniques.
- **p. 1 / Abstract - extractive body cue:** The network achieves state-of-the-art results in multiple 3D tasks, including camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, and 3D point tracking.
- **p. 1 / Abstract - extractive body cue:** We also show that using pretrained VGGT as a feature backbone significantly enhances downstream tasks, such as non-rigid point tracking and feed-forward novel view synthesis.
- **p. 1 / 1. Introduction - extractive body cue:** Machine learning has often played an important complementary role, addressing tasks that cannot be solved by geometry alone, such as feature matching and monocular depth ...
- **p. 4 / 3.1. Problem definition and notation - extractive body cue:** In the second row, our method correctly recovers a 3D scene from two images with no overlap, while DUSt3R fails.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, we make the following contributions: (1) We introduce VGGT, a large feed-forward transformer that, given one, a few, or even hundreds of images ...
- **p. 3 / 3. Method - extractive body cue:** We introduce VGGT, a large transformer that ingests a set of images as input and produces a variety of 3D quantities as output.
- **p. 4 / 3.1. Problem definition and notation - extractive body cue:** In the second row, our method correctly recovers a 3D scene from two images with no overlap, while DUSt3R fails.
- **p. 4 / 3.1. Problem definition and notation - extractive body cue:** As shown in the top row, our method successfully predicts the geometric structure of an oil painting, while DUSt3R predicts a slightly distorted plane.
- **p. 1 / 1. Introduction - extractive body cue:** Recent contributions like DUSt3R [129] and its evolution 1.
- **p. 5 / 3.3. Prediction heads - extractive body cue:** In order to implement the tracking module T , we use the CoTracker2 architecture [57], which takes the dense tracking features Ti as input.
- **p. 3 / 3.1. Problem definition and notation - extractive body cue:** The network architecture is designed to be permutation equivariant for all but the first frame.
- **p. 3 / 3.1. Problem definition and notation - extractive body cue:** It ingests the query point yq and the dense tracking features Ti output by the transformer f and then computes the track.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We introduce VGGT, a large transformer that ingests a set of images as input and produces a variety of 3D quantities as output. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3. Method), p. 5 (3.3. Prediction heads) |
| State/latent | introduce, VGGT, large, transformer, ingests, images, input, produces, variety, quantities, output, Additionally | geometry, map, object/relationship state | p. 3 (3. Method), p. 5 (3.3. Prediction heads), p. 5 (3.3. Prediction heads) |
| Output/action | Additionally, the DPT head also outputs dense features Ti ∈RC×H×W , which serve as input to the tracking head. | point map, pose, scene graph, affordance 또는 query result | p. 5 (3.3. Prediction heads), p. 5 (3.3. Prediction heads), p. 6 (3.3. Prediction heads) |
| Objective/outcome | We train the model by optimizing the training loss (2) with the AdamW optimizer for 160K iterations. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3.4. Training), p. 6 (3.4. Training), p. 5 (3.3. Prediction heads) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, we make the following contributions: (1) We introduce VGGT, a large feed-forward transformer that, given one, a few, or even hundreds of images ...
- **p. 3 / 3. Method - extractive body cue:** We introduce VGGT, a large transformer that ingests a set of images as input and produces a variety of 3D quantities as output.
- **p. 4 / 3.1. Problem definition and notation - extractive body cue:** In the second row, our method correctly recovers a 3D scene from two images with no overlap, while DUSt3R fails.
- **p. 4 / 3.1. Problem definition and notation - extractive body cue:** As shown in the top row, our method successfully predicts the geometric structure of an oil painting, while DUSt3R predicts a slightly distorted plane.
- **p. 1 / 1. Introduction - extractive body cue:** Recent contributions like DUSt3R [129] and its evolution 1.
- **p. 12 / Figure/Table caption - extractive body cue:** Table 10. Camera Pose Estimation on IMC [54]. Our method achieves state-of-the-art performance on the challenging pho- totropism data, outperforming VGGSfMv2 [125] which ranked first ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Visualization of Rigid and Dynamic Point Tracking. Top: VGGT's tracking module T outputs keypoint tracks for an unordered set of input images depicting ...
- **p. 7 / 4.1. Camera Pose Estimation - extractive body cue:** Hence, while the feed-forward mode of VGGT outperforms all previous alternatives (whether they are feed-forward or not), there is still room for improvement since post-optimization ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 12 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | It represents a specific case of rigid point tracking, which is restricted to only two views, and hence a suitable evaluation benchmark to measure our tracking accuracy, even though our model is ... | hardware/simulator version and reset protocol | p. 8 (4.4. Image Matching), p. 6 (4.1. Camera Pose Estimation) |
| Dataset/benchmark | Dense MVS Estimation on the DTU [51] Dataset. | role, split, size and leakage | p. 8 (4.4. Image Matching), p. 6 (4.1. Camera Pose Estimation), p. 7 (4.1. Camera Pose Estimation), p. 7 (4.1. Camera Pose Estimation) |
| Metric | The row Ours (Point) indicates the results using the point map head directly, while Ours (Depth + Cam) denotes constructing point clouds from the depth map head combined with the camera head. ... | definition, denominator, direction and uncertainty | p. 7 (4.1. Camera Pose Estimation), p. 6 (4.1. Camera Pose Estimation), p. 8 (4.3. Point Map Estimation) |
| Baseline/ablation | Although our tracking head is not specialized for the twoview setting, it outperforms the state-of-the-art two-view matching method Roma. | fair input/data/compute/action matching | p. 7 (4.1. Camera Pose Estimation), p. 9 (4.5. Ablation Studies), p. 12 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 5. Discussions - extractive body cue:** While our method exhibits strong generalization to diverse in-the-wild scenes, several limitations remain.
- **p. 10 / 5. Discussions - extractive body cue:** Moreover, although our model handles scenes with minor non-rigid motions, it fails in scenarios involving substantial non-rigid deformation.
- **p. 11 / 5. Discussions - extractive body cue:** While customizing a framework to expedite training could be a potential solution, it falls outside the scope of this work.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative comparison of our predicted 3D points to DUSt3R on in-the-wild images. As shown in the top row, our method successfully predicts the ...
- **p. 12 / 6. Conclusions - extractive body cue:** It is worth mentioning that we apply aggressive color augmentation independently across each frame within the same scene, enhancing the model's robustness to varying lighting ...
- **p. 9 / 4.6. Finetuning for Downstream Tasks - extractive body cue:** Following standard practices, we report these point-tracking metrics: Occlusion Accuracy (OA), which comprises the binary accuracy of occlusion predictions; δvis avg, comprising the 9

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Machine learning has often played an important complementary role, addressing tasks that cannot be solved by geometry alone, such as feature matching and monocular depth prediction.를 문제로 두고, To summarize, we make the following contributions: (1) We introduce VGGT, a large feed-forward transformer that, given one, a few, or even hundreds of images of a scene, can predict all its ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 4 (3.1. Problem definition and notation), p. 1 (1. Introduction), p. 3 (3.1. Problem definition and notation), p. 5 (3.3. Prediction heads), p. 3 (3.1. Problem definition and notation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
