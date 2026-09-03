# DiET-GS: Diffusion Prior and Event Stream-Assisted Motion Deblurring 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 Earlier works [1, 11, 42] focus on utilizing solely event-based data, lacking the capacity to preserve color information.를 문제로 두고, Once optimized, our method is capable of recovering well-defined details with accurate color from the input blurry images. • Qualitative and quantitative results show that our framework significantly surpasses the existing baselines, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Reconstructing sharp 3D representations from blurry multi-view images is a long-standing problem in computer vision.
- **p. 1 / Abstract - extractive body cue:** Recent works attempt to enhance high-quality novel view synthesis from the motion blur by leveraging eventbased cameras, benefiting from high dynamic range and microsecond temporal ...
- **p. 1 / Abstract - extractive body cue:** However, they often reach sub-optimal visual quality in either restoring inaccurate color or losing fine-grained details.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present DiET-GS, a diffusion prior and event streamassisted motion deblurring 3DGS.
- **p. 1 / Abstract - extractive body cue:** Our framework effectively leverages blur-free event streams and diffusion prior in a two-stage training strategy.
- **p. 1 / 1. Introduction - extractive body cue:** Earlier works [1, 11, 42] focus on utilizing solely event-based data, lacking the capacity to preserve color information.
- **p. 2 / 1. Introduction - extractive body cue:** However, most of these existing works still rely on blurry images alone to recover accurate color, often resulting in unwanted color artifacts.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Once optimized, our method is capable of recovering well-defined details with accurate color from the input blurry images. • Qualitative and quantitative results show that ...
- **p. 1 / 1. Introduction - extractive body cue:** Given a set of blurry images and corresponding event streams, we propose a novel framework to construct deblurring 3DGS by jointly leveraging the EDI [33] ...
- **p. 2 / 1. Introduction - extractive body cue:** To restore both accurate color and well-defined details, we introduce a novel framework that uses the EDI prior to achieve 1) fine-grained details, 2) accurate ...
- **p. 4 / 4. Our Method - extractive body cue:** To this end, we propose a novel optimization problem that leverages EDI prior to further constrain the 3DGS in terms of 1) fine-grained details, 2) ...
- **p. 1 / 1. Introduction - extractive body cue:** Our DiET-GS++ enables highquality novel-view synthesis by recovering precise color and welldefined details from the blurry multi-view images. tured and free from any artifact.
- **p. 5 / 4. Our Method - extractive body cue:** Since the input of the diffusion model ˆCB is obtained by averaging a set of rendered sharp images { ˆC}n-1 i=0 along the camera trajectory, ...
- **p. 4 / 4. Our Method - extractive body cue:** Since EDI is defined in the monochrome brightness domain, we first model the EDI based on pixel intensity values.
- **p. 5 / 4. Our Method - extractive body cue:** Given the predicted noise and zt, we then obtain the predicted denoised latent ˆzt-1 via the DDPM reverse process.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Based on the latent image I, a sharp latent image Ii at a randomly sampled timestep ti can be recovered by warping I to timestep ti as stated in the initialization step. | conditioning observation와 noisy/intermediate sample | p. 4 (4. Our Method), p. 5 (4. Our Method) |
| State/latent | latent, image, sharp, randomly, sampled, timestep, recovered, warping, stated, initialization, step, However | latent/noise variable와 conditional distribution | p. 4 (4. Our Method), p. 5 (4. Our Method), p. 5 (4. Our Method) |
| Output/action | However, unlike [20], our setting lacks the clean images which are necessary to guide noise prediction of diffusion model as conditional input. | generated sample, action chunk 또는 trajectory | p. 5 (4. Our Method), p. 5 (4. Our Method), p. 4 (4. Our Method) |
| Objective/outcome | Jointly optimizing these two constraints reaches an equilibrium between scene-specific details guided by the event-based loss and the prior knowledge of the pretrained diffusion model. | distribution fit, multimodality, sample quality와 latency | p. 5 (4. Our Method), p. 4 (4. Our Method), p. 5 (4. Our Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Once optimized, our method is capable of recovering well-defined details with accurate color from the input blurry images. • Qualitative and quantitative results show that ...
- **p. 1 / 1. Introduction - extractive body cue:** Given a set of blurry images and corresponding event streams, we propose a novel framework to construct deblurring 3DGS by jointly leveraging the EDI [33] ...
- **p. 2 / 1. Introduction - extractive body cue:** To restore both accurate color and well-defined details, we introduce a novel framework that uses the EDI prior to achieve 1) fine-grained details, 2) accurate ...
- **p. 4 / 4. Our Method - extractive body cue:** To this end, we propose a novel optimization problem that leverages EDI prior to further constrain the 3DGS in terms of 1) fine-grained details, 2) ...
- **p. 1 / 1. Introduction - extractive body cue:** Our DiET-GS++ enables highquality novel-view synthesis by recovering precise color and welldefined details from the blurry multi-view images. tured and free from any artifact.
- **p. 7 / 5.4. Quantitative Comparisons - extractive body cue:** Furthermore, our DiET-GS++ shows significant improvement in MUSIQ and CLIP-IQA metrics, achieving the best results but showing a slight drop in PSNR and SSIM metrics.
- **p. 7 / 5.4. Quantitative Comparisons - extractive body cue:** Nonetheless, DiET-GS++ still substantially improves the visual quality as shown in NR-IQA metrics.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Ablation on Ledi simul (1st row) and Lrsd (S1) (2nd row). adding EDI simulation Ledi simul further aids fine-grained deblurring as shown in ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (5.4. Quantitative Comparisons), p. 7 (5.4. Quantitative Comparisons) |
| Embodiment/environment | The EvDeblur-CDAVIS Dataset contains five real-world scenes, each with 11 to 18 blurry training images paired with corresponding event streams. | hardware/simulator version and reset protocol | p. 6 (5.2. Datasets), p. 6 (5.2. Datasets) |
| Dataset/benchmark | Qualitative comparisons on both synthetic (1st-2nd rows) and real-world (3rd-4th rows) datasets. | role, split, size and leakage | p. 6 (5.2. Datasets), p. 6 (5.2. Datasets), p. 7 (5.3. Experiment Settings), p. 7 (5.4. Quantitative Comparisons) |
| Metric | Table 1. Quantitative comparisons on both synthetic and real-world dataset. The results are the average of every scenes within the dataset. The best results are in bold while the second best results ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 6 (5.1. Implementation Details), p. 7 (5.3. Experiment Settings) |
| Baseline/ablation | Our DiETGS largely outperforms all baselines in PSNR, SSIM, and LPIPS on both synthetic and real-world datasets, showing the effectiveness of our framework to leverage EDI prior. | fair input/data/compute/action matching | p. 7 (5.4. Quantitative Comparisons), p. 7 (5.3. Experiment Settings), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Dataset - extractive body cue:** Gaussian noise samples at timesteps t and t -1 are then introduced to z′0 to get noised latents z′t and z′t-1.
- **p. 6 / Dataset - extractive body cue:** Finally, given ˆC as conditional input, the UNet backbone of pretrained diffusion model predicts the noise residual of z′t to derive the denoised latent ˆz′ ...
- **p. 7 / 5.3. Experiment Settings - extractive body cue:** We employ three standard metrics: Peak Signal-to-Noise Ratio (PSNR), Structural Similarity Index Measure (SSIM), and VGG-based Learned Perceptual Image Patch Similarity (LPIPS) [65] to evaluate ...

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 Earlier works [1, 11, 42] focus on utilizing solely event-based data, lacking the capacity to preserve color information.를 문제로 두고, Once optimized, our method is capable of recovering well-defined details with accurate color from the input blurry images. • Qualitative and quantitative results show that our framework significantly surpasses the existing baselines, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 4 (4. Our Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
