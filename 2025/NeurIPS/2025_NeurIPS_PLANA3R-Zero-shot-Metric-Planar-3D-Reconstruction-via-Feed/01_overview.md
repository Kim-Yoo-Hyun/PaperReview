# PLANA3R: Zero-shot Metric Planar 3D Reconstruction via Feed-forward Planar Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=YTwRZP8mNO.
> PDF retrieval source: https://arxiv.org/pdf/2510.18714. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openreview.net/forum?id=YTwRZP8mNO
- Full-text retrieval: https://arxiv.org/pdf/2510.18714
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these approaches face two key limitations: • Annotation dependence for feedforward methods: Learning feedforward models [36, 24, 28] typically requires accurate plane masks and 3D plane annotations from monocular or binocular ...를 문제로 두고, To address these challenges and facilitate training, we introduce a patch loss designed to stabilize primitive positioning and orientation: Lpatch ∗ = α1를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper addresses metric 3D reconstruction of indoor scenes by exploiting their inherent geometric regularities with compact representations.
- **p. 1 / Abstract - extractive body cue:** Using planar 3D primitives - a well-suited representation for man-made environments - we introduce PLANA3R, a pose-free framework for metric Planar 3D Reconstruction from unposed ...
- **p. 1 / Abstract - extractive body cue:** Our approach employs Vision Transformers to extract a set of sparse planar primitives, estimate relative camera poses, and supervise geometry learning via planar splatting, where ...
- **p. 1 / Abstract - extractive body cue:** Unlike prior feedforward methods that require 3D plane annotations during training, PLANA3R learns planar 3D structures without explicit plane supervision, enabling scalable training on large-scale ...
- **p. 1 / Abstract - extractive body cue:** We validate PLANA3R on multiple indoor-scene datasets with metric supervision and demonstrate strong generalization to out-of-domain indoor environments across diverse tasks under metric evaluation protocols, ...
- **p. 2 / 1 Introduction - extractive body cue:** However, these approaches face two key limitations: • Annotation dependence for feedforward methods: Learning feedforward models [36, 24, 28] typically requires accurate plane masks and ...
- **p. 2 / 1 Introduction - extractive body cue:** Factors such as the difficulty of accurate camera pose estimation from indoor images [28, 11, 1] and structural distortions in the resulting 3D reconstructions [22, ...

## Core Idea

- **p. 5 / 3 Method - extractive body cue:** To address these challenges and facilitate training, we introduce a patch loss designed to stabilize primitive positioning and orientation: Lpatch ∗ = α1
- **p. 2 / 1 Introduction - extractive body cue:** Once the model is trained, our method generates a set of 3D planar primitives that approximate indoor scenes far more efficiently than per-scene optimization methods ...
- **p. 4 / 3 Method - extractive body cue:** The input consists of two images I1, I2 ∈R3×H×W with camera intrinsics K1 and K2.
- **p. 4 / 3 Method - extractive body cue:** The core innovation of our method lies in the sparse primitive prediction architecture outlined in Sec.
- **p. 5 / 3 Method - extractive body cue:** After the warm-up phase, we introduce a rendering loss.
- **p. 4 / 3 Method - extractive body cue:** These features are then processed by two transformer decoders with cross-attention to produce low-resolution decoder embeddings {Gi low}i=1,2 ∈ R H 16 × W 16 ...
- **p. 5 / 3 Method - extractive body cue:** To achieve a more compact and efficient geometric representation using fewer primitives, we propose a hierarchical primitive prediction architecture (HPPA) to fit the scene using ...
- **p. 4 / 3 Method - extractive body cue:** Input images {Ii}i=1,2 are first encoded in a Siamese fashion using a ViT encoder [7], producing feature maps {F i}i=1,2 ∈R H 16 × W ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our goal is to train a network F outputs a set of sparse 3D planar primitives and the 6-DoF relative camera pose Prel. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3 Method), p. 4 (3 Method) |
| State/latent | goal, train, network, outputs, sparse, planar, primitives, DoF, relative, camera, pose, Prel | geometry, map, object/relationship state | p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method) |
| Output/action | Given two images captured from the same scene, PLANA3R outputs a set of 3D planar primitives and 6-DoF relative camera pose Prel in metric scale. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method) |
| Objective/outcome | 3.2, outline training objectives in Sec. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method) |

## Main Claims and Actual Contribution

- **p. 5 / 3 Method - extractive body cue:** To address these challenges and facilitate training, we introduce a patch loss designed to stabilize primitive positioning and orientation: Lpatch ∗ = α1
- **p. 2 / 1 Introduction - extractive body cue:** Once the model is trained, our method generates a set of 3D planar primitives that approximate indoor scenes far more efficiently than per-scene optimization methods ...
- **p. 4 / 3 Method - extractive body cue:** The input consists of two images I1, I2 ∈R3×H×W with camera intrinsics K1 and K2.
- **p. 4 / 3 Method - extractive body cue:** The core innovation of our method lies in the sparse primitive prediction architecture outlined in Sec.
- **p. 5 / 3 Method - extractive body cue:** After the warm-up phase, we introduce a rendering loss.
- **p. 7 / 4 Experiment - extractive body cue:** 1, both MASt3R and our PLANA3R significantly outperform prior learning-based planar reconstruction methods [28, 11, 1] in terms of pose estimation accuracy.
- **p. 7 / 4 Experiment - extractive body cue:** 1, PLANA3R achieves SOTA performance on ScanNetV2.
- **p. 9 / 4 Experiment - extractive body cue:** 5, using approximately half the number of high-resolution primitives achieves performance comparable to using the full high-resolution set.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4 Experiment), p. 7 (4 Experiment) |
| Embodiment/environment | 4.2 Datasets Since PLANA3R targets structured indoor scenes, we train it on a combination of four public indoorscene datasets: ScanNetV2 [4], ScanNet++ [39], ARKitScenes [5], and Habitat [23]. | hardware/simulator version and reset protocol | p. 6 (4 Experiment), p. 7 (4 Experiment) |
| Dataset/benchmark | We present more visualization results in the supplementary materials and conduct tests on the 7-Scenes [25] dataset. | role, split, size and leakage | p. 6 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 7 (4 Experiment) |
| Metric | Pose accuracy is measured by the metric translation error (in meters) and rotation error (in degrees). | definition, denominator, direction and uncertainty | p. 7 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment) |
| Baseline/ablation | 4.3 Baselines and Evaluation Metrics We evaluate our PLANA3R against state-of-the-art (SOTA) planar reconstruction methods across multiple tasks, including 3D reconstruction, pose estimation, depth estimation, and plane segmentation, us ... | fair input/data/compute/action matching | p. 6 (4 Experiment), p. 9 (4 Experiment), p. 7 (4 Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 18 / A.5 Limitations - extractive body cue:** While this represents a limitation in our current analysis, it also highlights the urgent need for better benchmarks in this field.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of our PLANA3R. Given two images captured from the same scene, PLANA3R outputs a set of 3D planar primitives and 6-DoF relative ...
- **p. 7 / 4 Experiment - extractive body cue:** This process does not require merging the primitives and can be performed with a single feed-forward pass.
- **p. 9 / 4 Experiment - extractive body cue:** 4.4 Multi-view Reconstruction with More Than Two Views PLANA3R currently supports multi-view reconstruction in a pairwise manner, but does not support a single forward pass ...
- **p. 14 / A.1 Extra Results - extractive body cue:** Although the 7-Scenes dataset is a widely used indoor dataset and is very suitable for out-of-domain evaluation, it does not provide official plane segmentation masks.
- **p. 16 / A.2 Implementation Details - extractive body cue:** Furthermore, we observe that as the overlap ratio in the test set decreases, the model's accuracy consistently degrades.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these approaches face two key limitations: • Annotation dependence for feedforward methods: Learning feedforward models [36, 24, 28] typically requires accurate plane masks and 3D plane annotations from monocular or binocular ...를 문제로 두고, To address these challenges and facilitate training, we introduce a patch loss designed to stabilize primitive positioning and orientation: Lpatch ∗ = α1를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
