# ReconFusion: 3D Reconstruction with Diffusion Priors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 NeRF's dense capture requirement poses a major challenge, necessitating tens to hundreds of images for even simple objects to ensure a clean reconstruction (Fig.를 문제로 두고, This enables our models to scale to large numbers of input images while selecting inputs that are most useful for the sampled novel view.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D reconstruction methods such as Neural Radiance Fields (NeRFs) excel at rendering photorealistic novel views of complex scenes.
- **p. 1 / Abstract - extractive body cue:** However, recovering a highquality NeRF typically requires tens to hundreds of input images, resulting in a time-consuming capture process.
- **p. 1 / Abstract - extractive body cue:** We present ReconFusion to reconstruct real-world scenes using only a few photos.
- **p. 1 / Abstract - extractive body cue:** Our approach leverages a diffusion prior for novel view synthesis, trained on synthetic and multiview datasets, which regularizes a NeRF-based 3D reconstruction pipeline at novel ...
- **p. 1 / Abstract - extractive body cue:** Our method synthesizes realistic geometry and texture in underconstrained regions while preserving the appearance of observed regions.
- **p. 1 / 1. Introduction - extractive body cue:** NeRF's dense capture requirement poses a major challenge, necessitating tens to hundreds of images for even simple objects to ensure a clean reconstruction (Fig.
- **p. 2 / 1. Introduction - extractive body cue:** We contribute an end-to-end system that markedly improves 3D reconstruction quality, uniquely combining the challenges of developing a multiview-conditioned image diffusion model and integrating it ...

## Core Idea

- **p. 5 / 3.3. Implementation Details - extractive body cue:** This enables our models to scale to large numbers of input images while selecting inputs that are most useful for the sampled novel view.
- **p. 2 / 1. Introduction - extractive body cue:** Our approach outperforms existing baselines on several datasets of both forward-facing and unbounded 360◦ scenes.
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we show that our diffusion prior is an effective drop-in regularizer for NeRFs across a range of capture settings.
- **p. 4 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** This enables the model to be trained and evaluated with a variable number of observed posed images.
- **p. 1 / 1. Introduction - extractive body cue:** Advances in 3D reconstruction have enabled the transformation of images of real-world scenes into 3D models which produce photorealistic renderings from novel viewpoints [26, 32].
- **p. 3 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** For relative camera pose and geometric information, we use a PixelNeRF [67] model Rϕ to render a feature map f with the same spatial resolution ...
- **p. 4 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** Training We freeze the weights of the pretrained encoder and decoder, initialize the U-Net parameters θ from pretrained weights, and optimize the modified architecture for ...
- **p. 5 / 3.3. Implementation Details - extractive body cue:** The encoder of our PixelNeRF is a small U-Net that takes as input an image of resolution 512×512 and outputs a feature map of resolution ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The encoder of our PixelNeRF is a small U-Net that takes as input an image of resolution 512×512 and outputs a feature map of resolution 64 × 64 with 128 channels (see ... | conditioning observation와 noisy/intermediate sample | p. 5 (3.3. Implementation Details), p. 4 (3.2. 3D Reconstruction with Diffusion Priors) |
| State/latent | encoder, PixelNeRF, small, U-Net, takes, input, image, resolution, outputs, feature, channels, supplement | latent/noise variable와 conditional distribution | p. 5 (3.3. Implementation Details), p. 4 (3.2. 3D Reconstruction with Diffusion Priors), p. 1 (1. Introduction) |
| Output/action | To enable 3D reconstruction from a smaller number of posed inputs, we augment the state-of-the-art 3D reconstruction pipeline from Zip-NeRF [2] with a prior from our diffusion model trained for novel view ... | generated sample, action chunk 또는 trajectory | p. 4 (3.2. 3D Reconstruction with Diffusion Priors), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | The NeRF parameters ψ are optimized by minimizing the reconstruction error between a rendered image x = x(ψ, πobs) and an observed image xobs at pose πobs: LRecon(ψ) = Exobs,πobs  ℓ(x(ψ, ... | distribution fit, multimodality, sample quality와 latency | p. 4 (3.2. 3D Reconstruction with Diffusion Priors), p. 4 (3.2. 3D Reconstruction with Diffusion Priors), p. 5 (3.3. Implementation Details) |

## Main Claims and Actual Contribution

- **p. 5 / 3.3. Implementation Details - extractive body cue:** This enables our models to scale to large numbers of input images while selecting inputs that are most useful for the sampled novel view.
- **p. 2 / 1. Introduction - extractive body cue:** Our approach outperforms existing baselines on several datasets of both forward-facing and unbounded 360◦ scenes.
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we show that our diffusion prior is an effective drop-in regularizer for NeRFs across a range of capture settings.
- **p. 4 / 3.1. Diffusion Model for Novel View Synthesis - extractive body cue:** This enables the model to be trained and evaluated with a variable number of observed posed images.
- **p. 1 / 1. Introduction - extractive body cue:** Advances in 3D reconstruction have enabled the transformation of images of real-world scenes into 3D models which produce photorealistic renderings from novel viewpoints [26, 32].
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative evaluation of few-view 3D reconstruction methods. Datasets are ordered in terms of sparsity from easier (novel views are close to observed views) ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Our learned diffusion prior improves performance over the Zip-NeRF baseline up to as many as 81 input views on the kitchenlego scene from ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Methods for reconstructing a 3D scene from images, such as Neural Radiance Fields (NeRF), often exhibit artifacts when trained with few input views. ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | For the mip-NeRF 360 dataset, we retain its original test set and select the input views from the training set using a heuristic to encourage reasonable camera spacing and coverage of the ... | hardware/simulator version and reset protocol | p. 5 (4.1. Experiment Setup), p. 5 (4.1. Experiment Setup) |
| Dataset/benchmark | A visual comparison of rendered images and depth maps on scenes from the RealEstate10K [71], LLFF [31], DTU [23], CO3D [39], and mip-NeRF 360 [1] datasets (input view count indicated in parentheses). | role, split, size and leakage | p. 5 (4.1. Experiment Setup), p. 5 (4.1. Experiment Setup), p. 6 (4.2. Comparison Results), p. 7 (4.2. Comparison Results) |
| Metric | We evaluate ReconFusion on five real-world datasets to demonstrate the performance and generalizability of our approach for few-view 3D reconstruction (Sec. | definition, denominator, direction and uncertainty | p. 5 (4. Experiments), p. 3 (Figure/Table caption), p. 5 (4. Experiments) |
| Baseline/ablation | Our method outperforms all baselines on both in-distribution and out-of-distribution datasets, achieving state-of-the-art performance for few-view NeRF reconstructions. | fair input/data/compute/action matching | p. 7 (4.2. Comparison Results), p. 5 (4.1. Experiment Setup), p. 7 (4.2. Comparison Results) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Methods for reconstructing a 3D scene from images, such as Neural Radiance Fields (NeRF), often exhibit artifacts when trained with few input views. ...
- **p. 8 / 5. Discussion - extractive body cue:** Many current limitations are evident: the heavyweight diffusion model is costly and slows down reconstruction significantly; our current results demonstrate only limited 3D outpainting abilities ...
- **p. 6 / 4.2. Comparison Results - extractive body cue:** Both the appearance and geometry of our method are of higher quality than the baselines in these examples-typical failure modes exhibited by the baselines include ...
- **p. 7 / 4.2. Comparison Results - extractive body cue:** However, they fall short on 360-degree scenes (e.g. the CO3D dataset), where a large portion of the scene is undersampled or even unobserved due to ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative evaluation of few-view 3D reconstruction methods. Datasets are ordered in terms of sparsity from easier (novel views are close to observed views) ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. (a) We optimize a NeRF to minimize a reconstruction loss Lrecon between renderings and a limited set of input images, alongside a sample ...
- **p. 5 / 3.3. Implementation Details - extractive body cue:** Regardless of t, we always sample the denoised image with k = 10 steps.

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 NeRF's dense capture requirement poses a major challenge, necessitating tens to hundreds of images for even simple objects to ensure a clean reconstruction (Fig.를 문제로 두고, This enables our models to scale to large numbers of input images while selecting inputs that are most useful for the sampled novel view.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Diffusion Model for Novel View Synthesis), p. 4 (3.1. Diffusion Model for Novel View Synthesis), p. 5 (3.3. Implementation Details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
