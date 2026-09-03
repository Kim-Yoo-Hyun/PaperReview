# PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=hQWwTWGAyu.
> PDF retrieval source: https://openreview.net/pdf/859969c4505c940b506d06cb01ee1bce1e5d07d0.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Diffusion, Generation, depth, point cloud, 3D Vision
- Official paper: https://openreview.net/forum?id=hQWwTWGAyu
- Full-text retrieval: https://openreview.net/pdf/859969c4505c940b506d06cb01ee1bce1e5d07d0.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 Existing approaches to this challenge fall broadly into two categories.를 문제로 두고, Inspired by JiT (Li & He, 2026), we introduce a minimalist pixel-space diffusion framework that trains directly on the raw point map space.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Formally, given an input image c ∈RH×W ×3, our goal is to estimate the corresponding point map x ∈ RH×W ×3, in which each pixel encodes its 3D spatial (X, Y , ... | conditioning observation와 noisy/intermediate sample | p. 3 (3. Approach), p. 4 (3.2. Architecture) |
| State/latent | Formally, given, input, image, goal, estimate, corresponding, point, pixel, encodes, spatial, coordinates | latent/noise variable와 conditional distribution | p. 3 (3. Approach), p. 4 (3.2. Architecture), p. 4 (3.1. Point Map Generation with Flow Matching) |
| Output/action | The network takes the noisy point map zt, the current time step t, and the conditioning image c as input. | generated sample, action chunk 또는 trajectory | p. 4 (3.2. Architecture), p. 4 (3.1. Point Map Generation with Flow Matching), p. 5 (3.4. Inference) |
| Objective/outcome | The final optimization objective is the weighted sum: L = Lfm + λLrel, (7) where λ = 0.1 is the loss weight. | distribution fit, multimodality, sample quality와 latency | p. 5 (3.3. Training), p. 5 (3.3. Training), p. 3 (3.1. Point Map Generation with Flow Matching) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Inspired by JiT (Li & He, 2026), we introduce a minimalist pixel-space diffusion framework that trains directly on the raw point map space.
- **p. 3 / 3. Approach - extractive body cue:** Our method learns to transport a simple Gaussian noise distribution to the data distribution of point maps, conditioned on the input image.
- **p. 3 / 3. Approach - extractive body cue:** To model the inherent ambiguities of this single-image setting, we propose a flow matching framework parameterized by a Vision Transformer (ViT) (Dosovitskiy, 2020; Peebles & ...
- **p. 4 / 3.1. Point Map Generation with Flow Matching - extractive body cue:** This, in turn, enables stable joint training across heterogeneous indoor and outdoor datasets.
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we show that such architectural overhead and intricate loss formulations are unnecessary.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Different diffusion sampling steps. Our single-step diffusion already significantly outperforms prior works, and in- creasing the sampling steps further enhances reconstruction details (see ...
- **p. 7 / 4.4. Evaluation Results - extractive body cue:** Our largest model, PointDiT-H, achieves the best depth accuracy (Reld and δd 1) and the best point map δp 1, while PointDiT achieves the highest ...
- **p. 8 / 4.4. Evaluation Results - extractive body cue:** As shown in Table 1, more steps steadily improve the boundary metric BF1, while Rel and δ1 remain stable, since a single step already yields ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 Existing approaches to this challenge fall broadly into two categories.를 문제로 두고, Inspired by JiT (Li & He, 2026), we introduce a minimalist pixel-space diffusion framework that trains directly on the raw point map space.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Training), p. 3 (3. Approach), p. 5 (3.2. Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
