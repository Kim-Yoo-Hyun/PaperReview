# TIGER: Time-Varying Denoising Model for 3D Point Cloud Generation with Diffusion Process

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Ren_TIGER_Time-Varying_Denoising_Model_for_3D_Point_Cloud_Generation_with_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Ren_TIGER_Time-Varying_Denoising_Model_for_3D_Point_Cloud_Generation_with_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Diffusion, Generation, point cloud, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Ren_TIGER_Time-Varying_Denoising_Model_for_3D_Point_Cloud_Generation_with_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Ren_TIGER_Time-Varying_Denoising_Model_for_3D_Point_Cloud_Generation_with_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, we observed that these PVCNNbased denoising models require a considerable number of timesteps to establish a rough shape since the limited receptive field cannot capture the global distribution of noise.를 문제로 두고, Our main contributions include: • We propose a novel two-stream denoising model, which uses timestep to optimally reweigh the global feature from Transformer and the local feature from shallow CNN. • We ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recently, diffusion models have emerged as a new powerful generative method for 3D point cloud generation tasks.
- **p. 1 / Abstract - extractive body cue:** However, few works study the effect of the architecture of the diffusion model in the 3D point cloud, resorting to the typical UNet model developed ...
- **p. 1 / Abstract - extractive body cue:** Inspired by the wide adoption of Transformers, we study the complementary role of convolution (from UNet) and attention (from Transformers).
- **p. 1 / Abstract - extractive body cue:** We discover that their respective importance change according to the timestep in the diffusion process.
- **p. 1 / Abstract - extractive body cue:** At early stage, attention has an outsized influence because Transformers are found to generate the overall shape more quickly, and at later stages when adding ...
- **p. 2 / 1. Introduction - extractive body cue:** However, we observed that these PVCNNbased denoising models require a considerable number of timesteps to establish a rough shape since the limited receptive field cannot ...
- **p. 1 / 1. Introduction - extractive body cue:** Existing point cloud generative models are built on a range of frameworks, including generative adversarial networks (GANs) [1, 5], variational autoencoders (VAEs) [24], normalizing flows ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions include: • We propose a novel two-stream denoising model, which uses timestep to optimally reweigh the global feature from Transformer and the ...
- **p. 1 / 1. Introduction - extractive body cue:** We propose to merge these two properties across different timesteps in the diffusion process. plore and develop efficient and effective model architectures for 3D point ...
- **p. 4 / 3.3. Latent Point Cloud Transformer - extractive body cue:** We propose two novel 3D space continuous position encoding methods: Phase Shift Position Encoding (PSPE) and Baseλ Position Encoding (BλPE).
- **p. 2 / 1. Introduction - extractive body cue:** To answer this question, we propose a Time-varying denoising model for 3D point cloud generation (TIGER), a two-stream architecture combining a shallow CNN branch and ...
- **p. 1 / 1. Introduction - extractive body cue:** However, these methods commonly utilize UNet-like convolutional networks that are originally designed for image processing.
- **p. 3 / 3. Method - extractive body cue:** Then, we dive into the details of our time-varying two-stream architecture, including the encoder part, latent point Transformer, time mask generator, and decoder part.
- **p. 4 / 3.3. Latent Point Cloud Transformer - extractive body cue:** Following [29], we use dual PatchNorm to project the latent point cloud into tokens, which place LayerNorm before and after an MLP layer for more ...
- **p. 4 / 3.2. Noisy Point Cloud Encoder - extractive body cue:** Specifically, a noisy point cloud encoder E : RN×3 →RM×d transforms the noisy point cloud Xt ∈RN×3 at timestep t into a latent point cloud ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our main contributions include: • We propose a novel two-stream denoising model, which uses timestep to optimally reweigh the global feature from Transformer and the local feature from shallow CNN. • We ... | conditioning observation와 noisy/intermediate sample | p. 2 (1. Introduction), p. 4 (3.2. Noisy Point Cloud Encoder) |
| State/latent | main, contributions, include, novel, two-stream, denoising, model, uses, timestep, optimally, reweigh, global | latent/noise variable와 conditional distribution | p. 2 (1. Introduction), p. 4 (3.2. Noisy Point Cloud Encoder), p. 1 (1. Introduction) |
| Output/action | We use furthest point sampling algorithm [11] to downsample the input noisy point cloud Xt ∈RN×3 into a sparser point cloud Xs t ∈RM×3 (M < N). | generated sample, action chunk 또는 trajectory | p. 4 (3.2. Noisy Point Cloud Encoder), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | In training, we optimize the MSE loss: Lsimple = Et∼[1,T ]∥µ -µθ(Xt, t)∥2 2 = Et∼[1,T ]∥ϵ -ϵθ(Xt, t)∥2 2, (3) where ϵ is the ground truth noise and ϵθ is the ... | distribution fit, multimodality, sample quality와 latency | p. 3 (3.1. Problem Formulation), p. 4 (3.3. Latent Point Cloud Transformer), p. 5 (3.4. Time Mask Generator) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions include: • We propose a novel two-stream denoising model, which uses timestep to optimally reweigh the global feature from Transformer and the ...
- **p. 1 / 1. Introduction - extractive body cue:** We propose to merge these two properties across different timesteps in the diffusion process. plore and develop efficient and effective model architectures for 3D point ...
- **p. 4 / 3.3. Latent Point Cloud Transformer - extractive body cue:** We propose two novel 3D space continuous position encoding methods: Phase Shift Position Encoding (PSPE) and Baseλ Position Encoding (BλPE).
- **p. 2 / 1. Introduction - extractive body cue:** To answer this question, we propose a Time-varying denoising model for 3D point cloud generation (TIGER), a two-stream architecture combining a shallow CNN branch and ...
- **p. 1 / 1. Introduction - extractive body cue:** However, these methods commonly utilize UNet-like convolutional networks that are originally designed for image processing.
- **p. 7 / 4.3. Ablation and Analysis - extractive body cue:** Furthermore, our proposed position encoding methods, PSPE and BλPE, significantly improve performance compared to no position encoding or learnable position encoding.
- **p. 6 / 4.2. Comparison with SoTA methods - extractive body cue:** 1, we outperform LION in four out of six metrics.
- **p. 6 / 4.2. Comparison with SoTA methods - extractive body cue:** Compared to other methods, our performance is significantly better.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (4.3. Ablation and Analysis), p. 6 (4.2. Comparison with SoTA methods) |
| Embodiment/environment | It is noteworthy that in order to compare with LION, which uses a different dataset splitting strategy (sampling from the first 10, 000 points instead of the latter 5, 000 points), we ... | hardware/simulator version and reset protocol | p. 6 (4.2. Comparison with SoTA methods), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | It is noteworthy that in order to compare with LION, which uses a different dataset splitting strategy (sampling from the first 10, 000 points instead of the latter 5, 000 points), we ... | role, split, size and leakage | p. 6 (4.2. Comparison with SoTA methods), p. 6 (4.1. Experimental Setup) |
| Metric | This metric has been shown to effectively measure both the quality and diversity of generated point clouds and a score closer to 50% indicates superior performance [51]. | definition, denominator, direction and uncertainty | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (Figure/Table caption) |
| Baseline/ablation | Figure 7. Our generation results (right) compared to baseline models (left). TIGER generates high-quality and diverse 3D point clouds. where WD×3 is the projection matrix to map the noise into 3D space ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 6 (4.2. Comparison with SoTA methods), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusions - extractive body cue:** Although we generate high-quality and natural samples, we cannot control the category of the generated shape.
- **p. 8 / 5. Conclusions - extractive body cue:** But future works can increase the backbone efficiency by proposing time-varying properties with only one network.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Illustration of our time-varying two-stream architecture (TIGER). The network's input is a noisy point cloud Xt at timestep t, and the goal is ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 7. Our generation results (right) compared to baseline models (left). TIGER generates high-quality and diverse 3D point clouds. where WD×3 is the projection matrix ...

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, we observed that these PVCNNbased denoising models require a considerable number of timesteps to establish a rough shape since the limited receptive field cannot capture the global distribution of noise.를 문제로 두고, Our main contributions include: • We propose a novel two-stream denoising model, which uses timestep to optimally reweigh the global feature from Transformer and the local feature from shallow CNN. • We ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 3 (3. Method), p. 4 (3.3. Latent Point Cloud Transformer) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
