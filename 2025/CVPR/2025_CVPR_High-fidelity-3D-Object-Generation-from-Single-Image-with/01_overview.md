# High-fidelity 3D Object Generation from Single Image with RGBN-Volume Gaussian Reconstruction Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: Yiyang Shen, Kun Zhou, He Wang, Yin Yang, Tianjia Shao
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf)

## Why This Paper Is Here

GS-RGBN은 한 장의 물체 영상으로부터 여러 시점의 색과 표면 법선을 결합해 가우시안으로 표현한 3D 물체를 생성한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recently single-view 3D generation via Gaussian splatting has emerged and developed quickly.
- **p. 1 / Abstract - extractive body cue:** They learn 3D Gaussians from 2D RGB images generated from pre-trained multi-view diffusion (MVD) models, and have shown a promising avenue for 3D generation through ...
- **p. 1 / Abstract - extractive body cue:** Despite the current progress, these methods still suffer from the inconsistency jointly caused by the geometric ambiguity in the 2D images, and the lack of ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose to fix these issues by GS-RGBN, a new RGBN-volume Gaussian Reconstruction Model designed to generate high-fidelity 3D objects from single-view ...
- **p. 1 / Abstract - extractive body cue:** Our key insight is a structured 3D representation can simultaneously mitigate the afore-mentioned two issues.
- **p. 1 / 1. Introduction - extractive body cue:** However, the persisting challenge arises due to the inherent geometric ambiguity and limited information provided in single-view images.
- **p. 2 / 1. Introduction - extractive body cue:** However, the direct learning of 3D Gaussians from 2D images for high-fidelity 3D object generation remains a challenge due to the spatially unstructured nature of ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose a novel RGBN-volume Gaussian reconstruction model, called GS-RGBN, to generate high-quality 3D assets from single-view ...
- **p. 2 / 1. Introduction - extractive body cue:** GS-RGBN implements two key insights: first, unlike traditional methods that employ 2D convolutions to encode image features and decode corresponding per-pixel 3D Gaussian attributes in ...
- **p. 3 / 3. Method - extractive body cue:** Then, we propose a simple but effective feature-level crossvolume fusion module that fuses the RGB and normal volumes to reproduce a fine-grained RGBN volume, aligning ...
- **p. 3 / 3. Method - extractive body cue:** Next, we describe how to decode the RGBN volume to generate high-quality 2D Gaussians for novel view rendering and high-quality shape reconstruction (Sec.
- **p. 3 / 3. Method - extractive body cue:** 2, GS-RGBN takes as input a single image of a 3D object into the MVD model Wonder3D [31] to obtain two sets of multi-view RGB ...
- **p. 4 / 3.1. Hybrid Voxel-Gaussian - extractive body cue:** RGB Volume 𝑽𝑽𝒓𝒓𝒓𝒓𝒓𝒓 Normal Volume 𝑽𝑽𝒏𝒏𝒏𝒏𝒏𝒏 Voxel Residual Blockṡ 𝑽𝑽𝒓𝒓𝒓𝒓𝒓𝒓̇ 𝑽𝑽𝒏𝒏𝒏𝒏𝒏𝒏 Group RGBN Volume 𝑽𝑽𝒓𝒓𝒓𝒓𝒓𝒓𝒓𝒓 Cross Attention Cross Attention Self Attention Q Q K V ...
- **p. 5 / 3.4. Training Objective - extractive body cue:** We train the full paradigm via color Lc and depth Ld loss supervision, optimizing reconstruction objectives between rendered and ground-truth RGB/depth images.
- **p. 5 / 3.4. Training Objective - extractive body cue:** L1 and Llp denote the L1 loss and VGG-based LPIPS loss [66].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2, GS-RGBN takes as input a single image of a 3D object into the MVD model Wonder3D [31] to obtain two sets of multi-view RGB and normal images, which are used to ... | conditioning observation와 noisy/intermediate sample | p. 3 (3. Method), p. 2 (1. Introduction) |
| State/latent | GS-RGBN, takes, input, single, image, object, MVD, model, Wonder3D, obtain, sets, multi-view | latent/noise variable와 conditional distribution | p. 3 (3. Method), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | However, the direct learning of 3D Gaussians from 2D images for high-fidelity 3D object generation remains a challenge due to the spatially unstructured nature of 3DGS [63, 70] and the inherent geometric ... | generated sample, action chunk 또는 trajectory | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Hybrid Voxel-Gaussian) |
| Objective/outcome | Lastly, we will present the training objective, which includes the supervision of color, depth and regularization loss functions (Sec. | distribution fit, multimodality, sample quality와 latency | p. 3 (3. Method), p. 5 (3.4. Training Objective), p. 5 (3.4. Training Objective) |

## Main Claims and Actual Contribution

- 다중 뷰 RGB·법선 특징을 공통 3D 복셀 공간에 모으고 이 체적 특징에서 가우시안의 위치와 외관을 예측한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf#page=5)
- 새 시점의 외관과 복원 형상 품질을 평가하고 RGB에 법선 특징을 더했을 때 달라지는 결과를 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 5 (4.2. Novel View Synthesis), p. 8 (Figure/Table caption) |
| Embodiment/environment | For evaluation, We adopt the most widely used Google Scanned Objects (GSO) dataset [13]. | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings) |
| Dataset/benchmark | Qualitative comparisons of novel view synthesis between GS-RGBN and other methods on the GSO dataset. | role, split, size and leakage | p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings), p. 6 (4.2. Novel View Synthesis), p. 6 (4.2. Novel View Synthesis) |
| Metric | The model performance decreases when the LPIPS, depth, and regularization loss terms are successively removed, as demonstrated in Table 2. | definition, denominator, direction and uncertainty | p. 7 (4.5. Ablation study), p. 6 (4.2. Novel View Synthesis), p. 7 (4.4. Runtime Efficiency) |
| Baseline/ablation | Our method significantly outperforms all recent methods by a large margin 21562 | fair input/data/compute/action matching | p. 5 (4.2. Novel View Synthesis), p. 5 (4.2. Novel View Synthesis), p. 6 (4.2. Novel View Synthesis) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion and Limitations - extractive body cue:** Besides, voxels cannot be directly used for representing large-scale scenes.
- **p. 7 / 4.5. Ablation study - extractive body cue:** Especially, the depth and regularization loss functions, which cannot be achieved by 3D 21564
- **p. 8 / 5. Conclusion and Limitations - extractive body cue:** The performance degradation occurs when the MVD models generate images with a higher level of view inconsistency.
- **p. 6 / 4.2. Novel View Synthesis - extractive body cue:** These inconsistencies once again underscore the importance of effectively integrating RGB and normal images for the recovery of both geometric and semantic details.
- **p. 7 / 4.3. Single View Reconstruction - extractive body cue:** Ablation study on the different loss functions and normal fusion strategies on the GSO dataset. planeGaussian [70] can generate shapes that exhibit rough alignment with ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 4 (3.1. Hybrid Voxel-Gaussian)이다.

## 검색 태그 근거

단일 영상에서 파생한 여러 뷰의 색과 표면 법선 특징을 체적 공간에 융합하고, 가우시안 물체를 생성한다. 확산 기반 다중 뷰 생성은 입력 뷰를 보강하는 구성요소다. [원문 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf#page=3) · [원문 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf#page=7)
