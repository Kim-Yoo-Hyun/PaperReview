# PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2026/poster/62351.
> PDF retrieval source: https://openreview.net/pdf/859969c4505c940b506d06cb01ee1bce1e5d07d0.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Haofei Xu, Rundi Wu, Philipp Henzler, Nikolai Kalischek, Michael Oechsle, Fabian Manhardt, Marc Pollefeys, Andreas Geiger, Federico Tombari, Michael Niemeyer
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Diffusion, depth, point cloud, 3D Vision, flow-matching
- Official paper: https://icml.cc/virtual/2026/poster/62351
- Full-text retrieval: https://arxiv.org/pdf/2607.02515.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

PointDiT는 단일 영상에 대응하는 3D 점 지도를 영상 공간의 확산 과정으로 예측한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** State-of-the-art single-image 3D reconstruction methods often rely on complex hybrid architectures and loss functions, or compress geometry into latent spaces in order to leverage pre-trained ...
- **p. 1 / Abstract - extractive body cue:** In this work, we show that such architectural overhead and intricate loss formulations are unnecessary.
- **p. 1 / Abstract - extractive body cue:** We introduce a minimalist pixel-space Diffusion Transformer, built on a plain ViT, that operates directly on raw 3D point map patches and is conditioned on ...
- **p. 1 / Abstract - extractive body cue:** Unlike existing latent diffusion approaches, we train our diffusion backbone entirely from scratch, eliminating the need for point map tokenizers.
- **p. 1 / Abstract - extractive body cue:** Despite its simplicity, our approach surpasses complex latent-based diffusion models while remaining significantly simpler than hybrid alternatives.
- **p. 1 / 1. Introduction - extractive body cue:** Existing approaches to this challenge fall broadly into two categories.
- **p. 2 / 1. Introduction - extractive body cue:** PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation distribution, often yielding over-smoothed geometry that lacks high-frequency detail, particularly in complex scene regions (Figure 2b).

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Inspired by JiT (Li & He, 2026), we introduce a minimalist pixel-space diffusion framework that trains directly on the raw point map space.
- **p. 3 / 3. Approach - extractive body cue:** Our method learns to transport a simple Gaussian noise distribution to the data distribution of point maps, conditioned on the input image.
- **p. 3 / 3. Approach - extractive body cue:** To model the inherent ambiguities of this single-image setting, we propose a flow matching framework parameterized by a Vision Transformer (ViT) (Dosovitskiy, 2020; Peebles & ...
- **p. 4 / 3.1. Point Map Generation with Flow Matching - extractive body cue:** This, in turn, enables stable joint training across heterogeneous indoor and outdoor datasets.
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we show that such architectural overhead and intricate loss formulations are unnecessary.
- **p. 5 / 3.3. Training - extractive body cue:** This creates a train-test discrepancy, since inference always starts at t = 0, and the model may then struggle to initiate the flow trajectory from ...
- **p. 5 / 3.2. Architecture - extractive body cue:** The sequence is then processed by a stack of Transformer blocks (Dosovitskiy, 2020; Li & He, 2026), each comprising multi-head self-attention and an MLP.
- **p. 4 / 3.2. Architecture - extractive body cue:** This yields a composite image representation Tc ∈RN×4D, where D is the perlayer feature dimension.

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | 한 장의 RGB 영상 |
| 표현 | RGB 패치와 잡음이 있는 픽셀 정렬 점 지도 |
| 출력 | 3D 점 지도 및 깊이 |
| 평가 | 스케일·오프셋 정렬 후 기하 정확도 |

[원문 4쪽](https://arxiv.org/pdf/2607.02515v1#page=4) · [원문 5쪽](https://arxiv.org/pdf/2607.02515v1#page=5) · [원문 7쪽](https://arxiv.org/pdf/2607.02515v1#page=7)

## Main Claims and Actual Contribution

- 영상 조건에서 잡음 분포를 점 지도 분포로 변환하도록 학습한다.
- 단안 영상에서 복원한 장면 기하를 평가한다.

[저자 원문](https://icml.cc/virtual/2026/poster/62351)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 7 (4.4. Evaluation Results) |
| Embodiment/environment | By default we train on the 256 × 256 SceneNet-RGBD dataset and report the average metrics on the seven unseen test sets with single-step inference. | hardware/simulator version and reset protocol | p. 8 (4.5. Ablation and Analysis), p. 6 (4.2. Implementation Details) |
| Dataset/benchmark | To assess the zero-shot generalization of our model, we evaluate on seven commonly used real-world datasets: DIODE (Vasiljevic et al., 2019), KITTI (Geiger et al., 2012), NYUv2 (Silberman et al., 2012), ETH3D ... | role, split, size and leakage | p. 8 (4.5. Ablation and Analysis), p. 6 (4.2. Implementation Details), p. 6 (4.3. Evaluation Setup and Metrics), p. 10 (4.5. Ablation and Analysis) |
| Metric | We assess prediction quality in both the point map and depth domains using standard metrics (Wang et al., 2025b): • Accuracy (δ1): the percentage of pixels for which the ratio between prediction ... | definition, denominator, direction and uncertainty | p. 7 (4.3. Evaluation Setup and Metrics), p. 7 (4.4. Evaluation Results), p. 9 (4.5. Ablation and Analysis) |
| Baseline/ablation | For a fair comparison, we benchmark against several state-of-the-art baselines, evaluating their publicly available pre-trained weights under the same preprocessing and cropping protocol. | fair input/data/compute/action matching | p. 7 (4.3. Evaluation Setup and Metrics), p. 7 (Figure/Table caption), p. 8 (4.4. Evaluation Results) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Comparison with latent diffusion and regression. The two dominant paradigms each have an inherent limitation: (a) the VAE in latent diffusion models introduces ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. PointDiT. A minimalist pixel-space Diffusion Trans- former operating directly on raw point map patches, conditioned on image tokens from a pre-trained DINOv3. The ...
- **p. 10 / 5. Conclusion - extractive body cue:** The same flexibility makes it natural to explore multi-view generation, alternative 3D representations, and richer conditioning signals (e.g., camera parameters), which we view as exciting ...
- **p. 10 / 5. Conclusion - extractive body cue:** While our framework delivers robust geometric estimation, it is currently trained at fixed resolutions (256 × 256 and 512 × 512); mixed-resolution training is a ...
- **p. 7 / 4.4. Evaluation Results - extractive body cue:** In Table 2, we study the model's sensitivity to noise sampling in single-step inference, and find it highly robust across stochastic initializations.
- **p. 7 / 4.3. Evaluation Setup and Metrics - extractive body cue:** Performance is nearly invariant to the noise, with all-zeros matching or slightly exceeding stochastic sampling, indicating the model learns to be robust to different noise ...
- **p. 6 / 4.1. Datasets - extractive body cue:** These self-supervised representations provide robust, domain-invariant visual cues that allow our model to focus on geometric reconstruction while generalizing to natural images.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Training), p. 3 (3. Approach), p. 5 (3.2. Architecture)이다.

## 검색 태그 근거

RGB 한 장에서 픽셀 정렬 3D 점 지도와 깊이를 추정한다. 손실은 조건부 flow matching이며, 실험에서 깊이와 점 지도는 스케일과 오프셋을 정렬한 뒤 평가했다. [원문 4쪽](https://arxiv.org/pdf/2607.02515v1#page=4) · [원문 5쪽](https://arxiv.org/pdf/2607.02515v1#page=5) · [원문 7쪽](https://arxiv.org/pdf/2607.02515v1#page=7)
