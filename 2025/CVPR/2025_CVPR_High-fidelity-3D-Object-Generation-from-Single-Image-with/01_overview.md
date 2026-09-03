# High-fidelity 3D Object Generation from Single Image with RGBN-Volume Gaussian Reconstruction Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, the persisting challenge arises due to the inherent geometric ambiguity and limited information provided in single-view images.를 문제로 두고, In summary, our contributions are as follows: • We propose a novel RGBN-volume Gaussian reconstruction model, called GS-RGBN, to generate high-quality 3D assets from single-view images in just a few seconds. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose a novel RGBN-volume Gaussian reconstruction model, called GS-RGBN, to generate high-quality 3D assets from single-view ...
- **p. 2 / 1. Introduction - extractive body cue:** GS-RGBN implements two key insights: first, unlike traditional methods that employ 2D convolutions to encode image features and decode corresponding per-pixel 3D Gaussian attributes in ...
- **p. 3 / 3. Method - extractive body cue:** Then, we propose a simple but effective feature-level crossvolume fusion module that fuses the RGB and normal volumes to reproduce a fine-grained RGBN volume, aligning ...
- **p. 3 / 3. Method - extractive body cue:** Next, we describe how to decode the RGBN volume to generate high-quality 2D Gaussians for novel view rendering and high-quality shape reconstruction (Sec.
- **p. 5 / 4.2. Novel View Synthesis - extractive body cue:** Our method significantly outperforms all recent methods by a large margin 21562
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Ablation study of different training models. Our full model achieves the best 3D object reconstruction with consistent details. Gaussian-based methods due to varying ...
- **p. 7 / 4.4. Runtime Efficiency - extractive body cue:** Given the superior performance achieved, it is deemed acceptable for our method to allocate additional time towards establishing a structured 3D voxel grid and aggregating ...
- **p. 6 / 4.2. Novel View Synthesis - extractive body cue:** The PSNR, SSIM, and LPIPS metrics for novel view synthesis on the GSO dataset are improved by 5.59dB, 0.063, and 0.064, respectively, compared to the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, the persisting challenge arises due to the inherent geometric ambiguity and limited information provided in single-view images.를 문제로 두고, In summary, our contributions are as follows: • We propose a novel RGBN-volume Gaussian reconstruction model, called GS-RGBN, to generate high-quality 3D assets from single-view images in just a few seconds. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. Hybrid Voxel-Gaussian) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
