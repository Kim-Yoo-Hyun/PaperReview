# ReconFusion: 3D Reconstruction with Diffusion Priors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: Rundi Wu, Ben Mildenhall, Philipp Henzler, Keunhong Park, Ruiqi Gao, Daniel Watson, Pratul P. Srinivasan, Dor Verbin, Jonathan T. Barron, Ben Poole, Aleksander Hołyński
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf)

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 4. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

ReconFusion은 적은 수의 실제 뷰로 방사장을 최적화할 때 새로운 뷰의 외관을 사전학습된 확산 모델로 제약한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf#page=3)

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
| Objective/outcome | 관측 camera pose에서 NeRF가 렌더링한 image와 관측 image의 reconstruction error를 평균한다. | Observed-view reconstruction loss; diffusion prior와 별도 항 | PDF p. 4 §3.2 / Eq. (4) |

## Main Claims and Actual Contribution

- 입력 영상으로 조건화한 다중 뷰 확산 사전분포를 학습하고, 관측하지 않은 카메라에서 렌더링한 영상에도 최적화 신호를 제공한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf#page=5)
- 전방 장면과 물체·장면을 둘러본 촬영 자료에서 입력 뷰 수를 바꿔 가며 새로운 시점의 재구성 품질을 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf#page=8)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Diffusion Model for Novel View Synthesis), p. 4 (3.1. Diffusion Model for Novel View Synthesis), p. 5 (3.3. Implementation Details)이다.

## 검색 태그 근거

사전학습한 조건부 영상 확산 모델이 적은 관측으로 최적화하는 방사장에 새 시점의 외관 사전분포를 제공한다. 평가는 희소 입력에서 복원한 장면과 뷰 합성에 집중한다. [원문 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf#page=3) · [원문 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf#page=7)
