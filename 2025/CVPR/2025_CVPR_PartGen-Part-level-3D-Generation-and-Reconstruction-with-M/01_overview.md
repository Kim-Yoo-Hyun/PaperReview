# PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: Minghao Chen, Roman Shapovalov, Iro Laina, Tom Monnier, Jianyuan Wang, David Novotny, Andrea Vedaldi
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision, object completion
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf)

## Why This Paper Is Here

PartGen은 물체를 여러 뷰에서 부품별로 분해하고, 다른 부품에 가려졌던 각 부품의 표면까지 완성해 개별 3D 자산을 만든다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Text- or image-to-3D generators and 3D scanners can now produce 3D assets with high-quality shapes and textures, but as single, fused entities lacking meaningful structure.
- **p. 1 / Abstract - extractive body cue:** In contrast, most applications and creative workflows require 3D assets to be composed of distinct, meaningful parts that can be independently manipulated.
- **p. 1 / Abstract - extractive body cue:** To bridge this gap, we introduce PartGen, a novel approach for generating, from text, images, or unstructured 3D objects, 3D objects composed of meaningful parts.
- **p. 1 / Abstract - extractive body cue:** Our method leverages a multi-view diffusion model to extract plausible and view-consistent part segmentations from multiple views of a Work completed during Minghao Chen's internship ...
- **p. 1 / Abstract - extractive body cue:** 3D object, dividing it into meaningful components.
- **p. 2 / 1. Introduction - extractive body cue:** This has the benefit of removing most of the ambiguity in the reconstruction task, which is important because the 3D reconstructor network is deterministic and ...
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, current 3D reconstruction and generation methods only model an object's visible outer surface, omitting internal details.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We assess our method empirically on a large collection of 3D assets produced by 3D artists or scanned, both quantitatively and qualitatively.
- **p. 2 / 1. Introduction - extractive body cue:** Inspired by these requirements, we introduce PartGen, a method to upgrade existing 3D generation pipelines from producing unstructured 3D objects to generating compositions of meaningful ...
- **p. 3 / 3. Method - extractive body cue:** This section introduces PartGen, our framework for generating 3D objects composed of several 3D parts.
- **p. 3 / 3. Method - extractive body cue:** 3.1, we introduce the necessary background on multiview diffusion and briefly describe how PartGen can be applied to text, image, or 3D model inputs.
- **p. 4 / 3.1. Background on 3D generation - extractive body cue:** Our method begins with text, single images, or existing 3D objects to obtain an initial grid view of the object.
- **p. 5 / 3.5. Training data - extractive body cue:** In the case of text conditioning, the training data consists of the pairs {(In, yn)}N n=1 of multi-view images and their text captions.
- **p. 5 / 3.5. Training data - extractive body cue:** In the case of image conditioning, we use all 140k models, and the conditioning yn comes in the form of single renders from a randomly ...
- **p. 4 / 3.1. Background on 3D generation - extractive body cue:** In the experiments, we follow AssetGen [73] and obtain Φ by fine-tuning a pretrained text-to-image diffusion model with an architecture similar to Emu [13], an ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The input to the model is a multi-view image I, and the output is a set of multi-view part masks M 1, M 2, . . . , M S corresponding to ... | conditioning observation와 noisy/intermediate sample | p. 4 (3.2. Multi-view part segmentation), p. 3 (3.1. Background on 3D generation) |
| State/latent | input, model, multi-view, image, output, part, masks, corresponding, parts, addition, text, images | latent/noise variable와 conditional distribution | p. 4 (3.2. Multi-view part segmentation), p. 3 (3.1. Background on 3D generation), p. 3 (3.1. Background on 3D generation) |
| Output/action | In addition to text and images, the input y can also be an existing 3D model. | generated sample, action chunk 또는 trajectory | p. 3 (3.1. Background on 3D generation), p. 3 (3.1. Background on 3D generation), p. 4 (3.2. Multi-view part segmentation) |
| Objective/outcome | Addressing 3D object segmentation through the lens of multi-view diffusion offers several advantages. | distribution fit, multimodality, sample quality와 latency | p. 4 (3.2. Multi-view part segmentation), p. 4 (3.1. Background on 3D generation) |

## Main Claims and Actual Contribution

- 다중 뷰 분할로 동일 부품을 찾아낸 뒤 전체 물체 맥락을 조건으로 보이지 않는 부품 영역을 생성해 3D로 재구성한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf#page=5)
- 부품별 분할·복원을 평가하고 복원한 부품의 교체와 재배치 등 기존 물체의 부분 편집을 시연했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 4 (Figure/Table caption), p. 7 (4.1. Part Segmentation) |
| Embodiment/environment | For all experiments, we use 100 held-out objects from the dataset described in Sec. | hardware/simulator version and reset protocol | p. 6 (4. Experiments), p. 8 (4.4. Applications) |
| Dataset/benchmark | PartGen can also decompose real-world 3D objects. | role, split, size and leakage | p. 6 (4. Experiments), p. 8 (4.4. Applications), p. 8 (4.4. Applications), p. 6 (4.1. Part Segmentation) |
| Metric | We first evaluate view part completion by computing scores w.r.t. the ground-truth multi-view part image J. | definition, denominator, direction and uncertainty | p. 7 (4.1. Part Segmentation), p. 6 (4.1. Part Segmentation), p. 8 (4.2. Part completion and reconstruction) |
| Baseline/ablation | We consider the original and fine-tuned SAM2 [67] as our baselines for multi-view segmentation. | fair input/data/compute/action matching | p. 6 (4.1. Part Segmentation), p. 7 (4.2. Part completion and reconstruction), p. 7 (4.1. Part Segmentation) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.1. Part Segmentation - extractive body cue:** Second, we concatenate the four orthogonal views in a multi-view image I and fine-tune SAM2 to predict the multi-view mask M (in this case, the ...
- **p. 7 / 4.2. Part completion and reconstruction - extractive body cue:** We then compare ˆJ to the ground-truth render J using Peak Signalto-Noise Ratio (PSNR) of the foreground pixels, Learned Perceptual Image Patch Similarity (LPIPS) [97], ...
- **p. 8 / 4.4. Applications - extractive body cue:** 6, PartGen can effectively generate 3D objects with distinct and completed parts, even in challenging cases with heavy occlusions, such as the gummy bear.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (3.1. Background on 3D generation), p. 4 (3.1. Background on 3D generation), p. 3 (3. Method), p. 5 (3.5. Training data)이다.

## 검색 태그 근거

텍스트나 다중 시점 영상을 바탕으로 부품 마스크를 만들고, 다른 부품에 가려진 표면의 뷰를 생성한다. 보완된 각 부품을 개별 3D 자산으로 재구성한다. [원문 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf#page=3) · [원문 8쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf#page=8)
