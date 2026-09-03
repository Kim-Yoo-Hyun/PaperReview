# Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, language embedding, grounding
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Despite its promise, such rendering-based distillation methods [30, 34] share two limitations.를 문제로 두고, Splat, direct registration and referencing of language-aligned features in 3D Gaussians, bypassing intermediate rendering and preserving feature accuracy. • We introduce the PQ encoding method for compact feature representation, reducin ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Splat, a novel approach for openvocabulary 3D scene understanding leveraging 3D Gaussian Splatting.
- **p. 1 / Abstract - extractive body cue:** Unlike existing language-embedded 3DGS methods, which rely on a rendering process, our method directly associates language-aligned CLIP embeddings with 3D Gaussians for holistic 3D scene ...
- **p. 1 / Abstract - extractive body cue:** The key of our method is a language feature registration technique where CLIP embeddings are assigned to the dominant Gaussians intersected by each pixel-ray.
- **p. 1 / Abstract - extractive body cue:** Moreover, we integrate Product Quantization (PQ) trained on general large-scale image data to compactly represent embeddings without per-scene optimization.
- **p. 1 / Abstract - extractive body cue:** Experiments demonstrate that our approach significantly outperforms existing approaches in 3D perception benchmarks, such as openvocabulary 3D semantic segmentation, 3D object localization, and 3D object ...
- **p. 1 / 1. Introduction - extractive body cue:** Despite its promise, such rendering-based distillation methods [30, 34] share two limitations.
- **p. 1 / 1. Introduction - extractive body cue:** This gap This CVPR paper is the Open Access version, provided by the Computer Vision Foundation.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Splat, direct registration and referencing of language-aligned features in 3D Gaussians, bypassing intermediate rendering and preserving feature accuracy. • We introduce the PQ encoding method ...
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We propose Dr.
- **p. 3 / 3. Dr. Splat - extractive body cue:** Then, we introduce Product Quantization (PQ) into our framework to efficiently store Gaussian-registered language embeddings, Sec.
- **p. 4 / 3.1. Feature registration process - extractive body cue:** The proposed process can be interpreted as an inverse volume rendering without gradient-based optimization, which enables our method to be faster than the prior methods ...
- **p. 1 / 1. Introduction - extractive body cue:** Our method directly links language features to 3D Gaussians, enabling efficient and complete spatial coverage.
- **p. 2 / 1. Introduction - extractive body cue:** Moreover, we propose to use a Product Quantization (PQ) feature encoding method to represent embeddings compactly and efficiently without any per-scene optimization.
- **p. 6 / 3.3. Text-query based 3D localization - extractive body cue:** After training 3D Gaussians Φours with our feature registration process and PQ, we describe the details of an inference mode that facilitates direct interaction with ...
- **p. 6 / 3.3. Text-query based 3D localization - extractive body cue:** Given a text, we first extract a query feature q using CLIP text encoder [31].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | After training 3D Gaussians Φours with our feature registration process and PQ, we describe the details of an inference mode that facilitates direct interaction with 3DGS upon receiving input queries, such as ... | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (3.3. Text-query based 3D localization), p. 2 (1. Introduction) |
| State/latent | After, training, Gaussians, ours, feature, registration, process, describe, details, inference, mode, facilitates | geometry, map, object/relationship state | p. 6 (3.3. Text-query based 3D localization), p. 2 (1. Introduction), p. 4 (3.1. Feature registration process) |
| Output/action | Our method bypasses the rendering stage, enabling direct interaction with 3D Gaussians for registering and referring the well-preserved language-aligned CLIP embeddings in the 3D space. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 4 (3.1. Feature registration process), p. 4 (3.1. Feature registration process) |
| Objective/outcome | The centroid indices ji = [ji1, ji2, . . . , jiL] are optimized by minimizing arg mink∥vi -sik∥to quantize a given vector vi where jik is an 8-bit unsigned integer. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.2. Product-Quantized CLIP embeddings), p. 4 (3.1. Feature registration process), p. 1 (1. Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Splat, direct registration and referencing of language-aligned features in 3D Gaussians, bypassing intermediate rendering and preserving feature accuracy. • We introduce the PQ encoding method ...
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We propose Dr.
- **p. 3 / 3. Dr. Splat - extractive body cue:** Then, we introduce Product Quantization (PQ) into our framework to efficiently store Gaussian-registered language embeddings, Sec.
- **p. 4 / 3.1. Feature registration process - extractive body cue:** The proposed process can be interpreted as an inverse volume rendering without gradient-based optimization, which enables our method to be faster than the prior methods ...
- **p. 1 / 1. Introduction - extractive body cue:** Our method directly links language features to 3D Gaussians, enabling efficient and complete spatial coverage.
- **p. 8 / 4.2. 3D object localization - extractive body cue:** Even with the 3D space search method, OpenGaussian [37], our model consistently demonstrates superior performance and achieves higher accuracy in localization.
- **p. 8 / 4.4. Ablation study - extractive body cue:** We observe that increasing the aggregating number of Gaussians per ray improves localization performance; however, it results in higher memory consumption and the number of ...
- **p. 7 / 4. Experiments - extractive body cue:** Note that, not specifically designed for segmentation, it achieves high performance as a result of language-based Gaussian updates.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4.2. 3D object localization), p. 8 (4.4. Ablation study) |
| Embodiment/environment | 4.1), we use the LERF [17] dataset annotated by LangSplat [30], which consists of several multi-view images of 3D scenes containing long-tail objects and includes ground truth 2D ground truth annotations for ... | hardware/simulator version and reset protocol | p. 6 (4. Experiments), p. 7 (4. Experiments) |
| Dataset/benchmark | 4.3 task, we employ the ScanNet [4] dataset. | role, split, size and leakage | p. 6 (4. Experiments), p. 7 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.1. 3D object selection) |
| Metric | Figure 6. Limitations of point-based IoU measurement. This figure shows the effect of removing the top and bottom 30% of Gaussians according to the proposed significant score, implying that volume differences significantly ... | definition, denominator, direction and uncertainty | p. 5 (Figure/Table caption), p. 7 (4.2. 3D object localization), p. 7 (4.2. 3D object localization) |
| Baseline/ablation | The results demonstrate that our method performs better object selection in most scenes, showing an improvement of over 0.5 in mIoU and more than 4.5 in mAcc compared to counterpart models. | fair input/data/compute/action matching | p. 7 (4.1. 3D object selection), p. 7 (4. Experiments), p. 8 (4.3. 3D semantic segmentation) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.1. 3D object selection - extractive body cue:** For LangSplat-m, the activations often shows random 3D Gaussians or fail to localize entirely (e.g., see "coffee mug"), highlighting the limitations of rasterization-based methods and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6. Limitations of point-based IoU measurement. This figure shows the effect of removing the top and bottom 30% of Gaussians according to the proposed ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. 3D object selection results on the LeRF-OVS dataset [17]. To measure 3D object selection performance, we calculate 2D segmentation accuracy on rendering of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 7. Qualitative results of 3D object localization. We visualize 3D localization activations (yellow) for "chair" and "desk" in the ScanNet dataset, comparing our method ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Despite its promise, such rendering-based distillation methods [30, 34] share two limitations.를 문제로 두고, Splat, direct registration and referencing of language-aligned features in 3D Gaussians, bypassing intermediate rendering and preserving feature accuracy. • We introduce the PQ encoding method for compact feature representation, reducin ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
