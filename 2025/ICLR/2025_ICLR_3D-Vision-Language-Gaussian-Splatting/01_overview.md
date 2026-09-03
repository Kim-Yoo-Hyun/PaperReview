# 3D Vision-Language Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=SSE9myD9SG.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114008. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision, Gaussian Splatting, semantic
- Official paper: https://openreview.net/forum?id=SSE9myD9SG
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/114008
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Moreover, vision-language models like CLIP (Radford et al., 2021) and LSeg (Li et al., 2022) have been bridging the gap between color images and semantic features in 2D space.를 문제로 두고, Besides, we introduce a language-specific parameter that enables the meaningful blending of language features from different Gaussians.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Recent advancements in 3D reconstruction methods and vision-language models have propelled the development of multi-modal 3D scene understanding, which has vital applications in robotics, autonomous ...
- **p. 1 / ABSTRACT - extractive body cue:** However, current multi-modal scene understanding approaches have naively embedded semantic representations into 3D reconstruction methods without striking a balance between visual and language modalities, which ...
- **p. 1 / ABSTRACT - extractive body cue:** To alleviate these limitations, we propose a solution that adequately handles the distinct visual and semantic modalities, i.e., a 3D visionlanguage Gaussian splatting model for ...
- **p. 1 / ABSTRACT - extractive body cue:** We propose a novel cross-modal rasterizer, using modality fusion along with a smoothed semantic indicator for enhancing semantic rasterization.
- **p. 1 / ABSTRACT - extractive body cue:** We also employ a camera-view blending technique to improve semantic consistency between existing and synthesized views, thereby effectively mitigating over-fitting.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Moreover, vision-language models like CLIP (Radford et al., 2021) and LSeg (Li et al., 2022) have been bridging the gap between color images and semantic ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Given these limitations, our intuition is to strike a balance between visual and language modalities, rather than simply embedding language features into RGB-based 3D reconstruction.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Besides, we introduce a language-specific parameter that enables the meaningful blending of language features from different Gaussians.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** All in all, our 3D vision-language Gaussian splatting can be summarized into the following contributions: • We propose a cross-modal rasterizer that places greater emphasis ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** To address this problem, we propose a novel α-blending strategy specifically designed for exploring semantic information.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** To address this gap, we propose a novel crossmodal rasterizer that emphasizes semantic-specific design, as illustrated in Fig.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** A) We propose a novel multi-modal Gaussian splatting model; B) we enrich the input images and poses for the model to better fit the semantic ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** To train these semantically-enriched 3DGS models, the standard procedure consists of first generating the set of 2D language-feature maps H corresponding to the input images ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** In this paper, we propose to adapt the usual rasterization scheme to better fit the language-feature modality.
- **p. 6 / 3 METHODOLOGY - extractive body cue:** For two randomly selected samples (I1, W1) and (I2, W2) from the training set T r, where W1̸ = W2, we first utilize the camera ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | These solutions rely on 2D supervision to learn a multi-modal (color and semantic) 3D scene representation, i.e., projecting the learned 3D representation back to 2D views for comparison with the input observations ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| State/latent | solutions, rely, supervision, learn, multi-modal, color, semantic, scene, representation, projecting, learned, back | geometry, map, object/relationship state | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/action | Modality fusion occurs prior to rasterization, accompanied by a learnable and independent semantic indicator parameter for the α-blending of language features, enabling a more accurate representation of translucent or reflective objects ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (3 METHODOLOGY) |
| Objective/outcome | 2) and the ground-truth 2D semantic embeddings: L = E(I,W )∈T rEv∈ILsem(F W (v), HW (v)), (3) where L is the overall optimization objective. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Besides, we introduce a language-specific parameter that enables the meaningful blending of language features from different Gaussians.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** All in all, our 3D vision-language Gaussian splatting can be summarized into the following contributions: • We propose a cross-modal rasterizer that places greater emphasis ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** To address this problem, we propose a novel α-blending strategy specifically designed for exploring semantic information.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** To address this gap, we propose a novel crossmodal rasterizer that emphasizes semantic-specific design, as illustrated in Fig.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** A) We propose a novel multi-modal Gaussian splatting model; B) we enrich the input images and poses for the model to better fit the semantic ...
- **p. 8 / 4.2 RESULTS - extractive body cue:** Our proposed method achieves state-of-the-art performance across all scenes, notably outperforming the second best method LangSplat (Qin et al., 2024) by 10.6 in mIoU on ...
- **p. 14 / A.2.2 QUALITATIVE RESULTS - extractive body cue:** The results demonstrate that our proposed method significantly outperforms the competing approaches.
- **p. 8 / 4.2 RESULTS - extractive body cue:** The results indicate that both Slerp-based rotation blending and Lerp-based translation blending contribute to performance improvements.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4.2 RESULTS), p. 14 (A.2.2 QUALITATIVE RESULTS) |
| Embodiment/environment | (1) LERF dataset (Kerr et al., 2023), captured using the Polycam application on an iPhone, comprises complex, in-the-wild scenes and is specifically tailored for 3D object localization tasks. | hardware/simulator version and reset protocol | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Dataset/benchmark | Our proposed method achieves state-of-the-art performance across all scenes, notably outperforming the second best method LangSplat (Qin et al., 2024) by 10.6 in mIoU on the LERF dataset. | role, split, size and leakage | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4.2 RESULTS), p. 20 (A.5.1 EXTENDED RESULTS ON 3D-OVS SCENES) |
| Metric | The goal is to verify that, while this work focuses on semantic accuracy, our solution does not sacrifice visual precision too much. | definition, denominator, direction and uncertainty | p. 21 (A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION), p. 7 (4 EXPERIMENTS), p. 8 (4.2 RESULTS) |
| Baseline/ablation | Our proposed method achieves state-of-the-art performance across all scenes, notably outperforming the second best method LangSplat (Qin et al., 2024) by 10.6 in mIoU on the LERF dataset. | fair input/data/compute/action matching | p. 8 (4.2 RESULTS), p. 10 (4.2 RESULTS), p. 8 (4.2 RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.2 RESULTS - extractive body cue:** However, this new attribute cannot be naively fixed, e.g., to 1 or 0.5 for all Gaussians.
- **p. 8 / 4.2 RESULTS - extractive body cue:** It is important to note that FMGS (Zuo et al., 2024) does not report mIoU results on the LERF dataset and is also not open-sourced, ...
- **p. 21 / A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION - extractive body cue:** The goal is to verify that, while this work focuses on semantic accuracy, our solution does not sacrifice visual precision too much.
- **p. 21 / A.5.2 EXTENDED EFFICIENCY ANALYSIS AND IMAGE QUALITY EVALUATION - extractive body cue:** Moreover, comparing to the results from color-only 3DGS (same as LangSplat as this method fixes all 3DGS parameters after its pre-training), we observe that semantic ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Moreover, vision-language models like CLIP (Radford et al., 2021) and LSeg (Li et al., 2022) have been bridging the gap between color images and semantic features in 2D space.를 문제로 두고, Besides, we introduce a language-specific parameter that enables the meaningful blending of language features from different Gaussians.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 3 (3 METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
