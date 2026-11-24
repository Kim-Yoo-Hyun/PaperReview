# Flash3D: Feed-Forward Generalisable 3D Scene Reconstruction from a Single Image

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/3dv66043.2025.00067.
> PDF retrieval source: https://openreview.net/attachment?id=05T81ScPFb&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: Stanislaw Szymanowicz, Eldar Insafutdinov, Chuanxia Zheng, Dylan Campbell, João F. Henriques, Christian Rupprecht, Andrea Vedaldi
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, 3D Vision
- Official paper: https://api.crossref.org/works/10.1109/3dv66043.2025.00067
- Full-text retrieval: https://arxiv.org/pdf/2406.04343.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125585)

## Why This Paper Is Here

Flash3D는 한 장의 RGB 영상에서 단안 깊이를 추정하고 여러 층의 가우시안을 배치해 새로운 시점을 렌더링한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125585#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125585#page=3)

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

- 첫 층은 보이는 표면의 깊이에 고정하고 추가 층은 그 뒤의 가려진 표면을 나타내도록 상대 깊이와 외관을 예측한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125585#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125585#page=4)
- RealEstate10K의 새 시점 합성과 KITTI로의 전이에서 단일 입력 뷰의 예측을 비교하고 추가 가우시안 층의 효과를 평가했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125585#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125585#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125585#page=7)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Monocular feed-forward multi-Gaussians), p. 3 (3. Method)이다.
