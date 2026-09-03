# Flash3D: Feed-Forward Generalisable 3D Scene Reconstruction from a Single Image

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/.
> PDF retrieval source: https://openreview.net/attachment?id=05T81ScPFb&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, 3D Vision
- Official paper: https://3dvconf.github.io/2025/accepted-papers/
- Full-text retrieval: https://openreview.net/attachment?id=05T81ScPFb&name=pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, in scene reconstruction, there is not such a reservoir of background pixels, which poses a challenge for the method.를 문제로 두고, In this work, we introduce a new, simple, efficient and performant approach for monocular scene reconstruction called를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We propose Flash3D, a method for scene reconstruction and novel view synthesis from a single image which is both very generalisable and efficient.
- **p. 1 / Abstract - extractive body cue:** For generalisability, we start from a ‘foundation' model for monocular depth estimation and extend it to a full 3D shape and appearance reconstructor.
- **p. 1 / Abstract - extractive body cue:** For efficiency, we base this extension on feed-forward Gaussian Splatting.
- **p. 1 / Abstract - extractive body cue:** Specifically, we predict a first layer of 3D Gaussians at the predicted depth, and then add additional layers of Gaussians that are offset in space, ...
- **p. 1 / Abstract - extractive body cue:** Flash3D is very efficient, trainable on a single GPU in a day, and thus accessible to most researchers.
- **p. 1 / 1. Introduction - extractive body cue:** However, in scene reconstruction, there is not such a reservoir of background pixels, which poses a challenge for the method.
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, pixelSplat [9], MVSplat [11], latentSplat [87] and GS-LRM [102], which share a similar design, were designed for scene reconstruction; however, they address the ...

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** In this work, we introduce a new, simple, efficient and performant approach for monocular scene reconstruction called
- **p. 4 / 3.2. Monocular feed-forward multi-Gaussians - extractive body cue:** Hence, we propose to predict a small number K > 1 of different Gaussians for each pixel.
- **p. 4 / 3.2. Monocular feed-forward multi-Gaussians - extractive body cue:** For generalisation, we propose to build Flash3D on a highquality pre-trained model trained on a large amount of data.
- **p. 2 / 1. Introduction - extractive body cue:** We show, in particular, that by building on a high-quality depth predictor [49], we can achieve excellent generalisation to new datasets, to the point that ...
- **p. 5 / 3.2. Monocular feed-forward multi-Gaussians - extractive body cue:** As we show empirically, it is important for the network to be able to model 3D content just outside its field-of-view.
- **p. 4 / 3.2. Monocular feed-forward multi-Gaussians - extractive body cue:** Given an image I and estimated depth map D, our baseline model consists of an additional network Φ(I, D) that takes as input the image ...
- **p. 3 / 3. Method - extractive body cue:** Our goal is to learn a neural network Φ that takes as input I and predicts a representation G = Φ(I) of the 3D content ...
- **p. 4 / 3.2. Monocular feed-forward multi-Gaussians - extractive body cue:** The decoder network thus outputs a tensor Φdec(Φenc(I, D)) ∈R(C-1)×H×W .

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Input: 1 Image of any Scene Flash 3D Output: Full 3D Reconstruction In-domain: RealEstate10k Cross-domain: KITTI, NYU Figure 1. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 5 (3.2. Monocular feed-forward multi-Gaussians) |
| State/latent | Input, Image, Scene, Flash, Output, Full, Reconstruction, In-domain, RealEstate10k, Cross-domain, KITTI, NYU | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 5 (3.2. Monocular feed-forward multi-Gaussians), p. 4 (3.2. Monocular feed-forward multi-Gaussians) |
| Output/action | To facilitate obtaining such Gaussians, the encoder Φenc starts with padding the input image and depth (I, D) with P > 0 pixels on each side, so that the outputs Φk(I, D) ... | point map, pose, scene graph, affordance 또는 query result | p. 5 (3.2. Monocular feed-forward multi-Gaussians), p. 4 (3.2. Monocular feed-forward multi-Gaussians), p. 4 (3.2. Monocular feed-forward multi-Gaussians) |
| Objective/outcome | To learn the network parameters, one simply minimises the rendering loss L(G, π, J) = ∥Rend(G, π) -J∥. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3. Method), p. 4 (3. Method) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** In this work, we introduce a new, simple, efficient and performant approach for monocular scene reconstruction called
- **p. 4 / 3.2. Monocular feed-forward multi-Gaussians - extractive body cue:** Hence, we propose to predict a small number K > 1 of different Gaussians for each pixel.
- **p. 4 / 3.2. Monocular feed-forward multi-Gaussians - extractive body cue:** For generalisation, we propose to build Flash3D on a highquality pre-trained model trained on a large amount of data.
- **p. 2 / 1. Introduction - extractive body cue:** We show, in particular, that by building on a high-quality depth predictor [49], we can achieve excellent generalisation to new datasets, to the point that ...
- **p. 5 / 3.2. Monocular feed-forward multi-Gaussians - extractive body cue:** As we show empirically, it is important for the network to be able to model 3D content just outside its field-of-view.
- **p. 7 / 4.3. In-domain novel view synthesis - extractive body cue:** 2, we observe that we achieve state-of-the-art results on this mature benchmark across all distances between the source and the target.
- **p. 5 / 4.1. Experiment settings - extractive body cue:** We outperform baselines which were trained on KITTI specifically.
- **p. 5 / 4.1. Experiment settings - extractive body cue:** With this, Flash3D can be trained to achieve state-of-the-art quality on a single A6000 GPU in 16 hours.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.3. In-domain novel view synthesis), p. 5 (4.1. Experiment settings) |
| Embodiment/environment | We follow the default training/testing split with 67,477 scenes for training and 7,289 for testing. | hardware/simulator version and reset protocol | p. 5 (4.1. Experiment settings), p. 5 (4.2. Cross-domain novel view synthesis) |
| Dataset/benchmark | Q1: Is leveraging a monocular depth predictor useful in the task of reconstructing appearance and geometry of scenes? | role, split, size and leakage | p. 5 (4.1. Experiment settings), p. 5 (4.2. Cross-domain novel view synthesis), p. 7 (4.5. Ablation study and analysis), p. 6 (4.2. Cross-domain novel view synthesis) |
| Metric | We evaluate Novel View Synthesis accuracy on datasets not used in training of our method. | definition, denominator, direction and uncertainty | p. 5 (4.1. Experiment settings), p. 5 (4. Experiments), p. 6 (4.2. Cross-domain novel view synthesis) |
| Baseline/ablation | We outperform baselines which were trained on KITTI specifically. | fair input/data/compute/action matching | p. 5 (4.1. Experiment settings), p. 6 (4.2. Cross-domain novel view synthesis), p. 5 (4.1. Experiment settings) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.2. Cross-domain novel view synthesis - extractive body cue:** This is thanks to leveraging a depth predictor which, when used on its own (fourth column), cannot represent occluded regions (third row, fourth row).
- **p. 7 / 4.4. Comparison to few-view novel view synthesis - extractive body cue:** Here, Flash3D cannot outperform two-view approaches on the interpolation task, due to receiving less information.
- **p. 8 / 4.5. Ablation study and analysis - extractive body cue:** 5 additionally reveals a limitation of our method.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Ablation. We show how Flash3D degrades when components are removed. Removing the depth network (4th column) results in incorrect geometry (orange wall, corner ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, in scene reconstruction, there is not such a reservoir of background pixels, which poses a challenge for the method.를 문제로 두고, In this work, we introduce a new, simple, efficient and performant approach for monocular scene reconstruction called를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Monocular feed-forward multi-Gaussians), p. 3 (3. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
