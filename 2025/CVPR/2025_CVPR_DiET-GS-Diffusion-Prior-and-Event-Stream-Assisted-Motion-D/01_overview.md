# DiET-GS: Diffusion Prior and Event Stream-Assisted Motion Deblurring 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: Seungjun Lee, Gim Hee Lee
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, Diffusion, Generation, 3D Vision, event camera
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf)

## Why This Paper Is Here

DiET-GS는 카메라 움직임으로 흐려진 영상에서 선명한 3D 가우시안 장면을 복원하기 위해 노출 중 이벤트와 확산 사전분포를 이용한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf#page=3)

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

- 노출 시간 동안의 밝기 변화에 이벤트 관측을 연결하고 확산 모델이 제공하는 가장자리 정보를 최적화에 반영한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf#page=5)
- 합성 및 실제 장면에서 흐림 제거와 새 시점 렌더링을 평가하고 이벤트·확산 단서를 각각 제거해 비교했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf#page=8)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 4 (4. Our Method)이다.

## 검색 태그 근거

흐린 RGB와 같은 노출 동안의 이벤트를 이용해 장면 가우시안을 최적화한다. 확산 모델은 영상 선명화의 사전정보로 사용하며 합성·실제 촬영으로 복원 품질을 평가했다. [원문 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf#page=4) · [원문 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf#page=7)
