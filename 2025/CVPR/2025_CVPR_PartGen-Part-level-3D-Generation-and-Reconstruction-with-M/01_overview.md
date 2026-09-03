# PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 This has the benefit of removing most of the ambiguity in the reconstruction task, which is important because the 3D reconstructor network is deterministic and cannot handle ambiguity well.를 문제로 두고, We assess our method empirically on a large collection of 3D assets produced by 3D artists or scanned, both quantitatively and qualitatively.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1. Introduction - extractive body cue:** We assess our method empirically on a large collection of 3D assets produced by 3D artists or scanned, both quantitatively and qualitatively.
- **p. 2 / 1. Introduction - extractive body cue:** Inspired by these requirements, we introduce PartGen, a method to upgrade existing 3D generation pipelines from producing unstructured 3D objects to generating compositions of meaningful ...
- **p. 3 / 3. Method - extractive body cue:** This section introduces PartGen, our framework for generating 3D objects composed of several 3D parts.
- **p. 3 / 3. Method - extractive body cue:** 3.1, we introduce the necessary background on multiview diffusion and briefly describe how PartGen can be applied to text, image, or 3D model inputs.
- **p. 4 / 3.1. Background on 3D generation - extractive body cue:** Our method begins with text, single images, or existing 3D objects to obtain an initial grid view of the object.
- **p. 7 / 4.1. Part Segmentation - extractive body cue:** We first evaluate view part completion by computing scores w.r.t. the ground-truth multi-view part image J.
- **p. 7 / 4.1. Part Segmentation - extractive body cue:** As shown in the table, mAP results for our method are much higher than others, including SAM2 fine-tuned on our data.
- **p. 8 / 4.2. Part completion and reconstruction - extractive body cue:** We further provide qualitative results in Fig.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 This has the benefit of removing most of the ambiguity in the reconstruction task, which is important because the 3D reconstructor network is deterministic and cannot handle ambiguity well.를 문제로 두고, We assess our method empirically on a large collection of 3D assets produced by 3D artists or scanned, both quantitatively and qualitatively.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Background on 3D generation), p. 4 (3.1. Background on 3D generation), p. 3 (3. Method), p. 5 (3.5. Training data) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
