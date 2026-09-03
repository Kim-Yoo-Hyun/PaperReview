# ThermalGaussian: Thermal 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=ybFRoGxZjs.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114610. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D Vision
- Official paper: https://openreview.net/forum?id=ybFRoGxZjs
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/114610
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these datasets suffer from problems such as lack of color images registered with thermal images, inconsistencies in thermal information from different views, and watermarked images.를 문제로 두고, The final design of this loss is: L = γLRGB + (1 -γ)Lthermal (12) 4 SELF-COLLECTED THERAML DATASET We introduce a new dataset, named RGBT-Scenes, which consists of aligned collections of thermal ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Thermography is especially valuable for the military and other users of surveillance cameras.
- **p. 1 / ABSTRACT - extractive body cue:** Some recent methods based on Neural Radiance Fields (NeRF) are proposed to reconstruct the thermal scenes in 3D from a set of thermal and RGB ...
- **p. 1 / ABSTRACT - extractive body cue:** However, unlike NeRF, 3D Gaussian splatting (3DGS) prevails due to its rapid training and real-time rendering.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we propose ThermalGaussian, the first thermal 3DGS approach capable of rendering high-quality images in RGB and thermal modalities.
- **p. 1 / ABSTRACT - extractive body cue:** We first calibrate the RGB camera and the thermal camera to ensure that both modalities are accurately aligned.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, these datasets suffer from problems such as lack of color images registered with thermal images, inconsistencies in thermal information from different views, and watermarked ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, these methods not only fail to fully exploit thermal information but are also constrained by the limitations of traditional 3D reconstruction techniques, which impede ...

## Core Idea

- **p. 7 / 3 METHOD - extractive body cue:** The final design of this loss is: L = γLRGB + (1 -γ)Lthermal (12) 4 SELF-COLLECTED THERAML DATASET We introduce a new dataset, named RGBT-Scenes, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, the main contributions as follows: (1)We propose ThermalGaussian, the first multimodal 3DGS capable of simultaneously rendering photorealistic thermal and RGB images of a ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In contrast, our method not only improves thermal rendering quality but also enhances RGB rendering quality by 1 dB.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** The dataset consists of paired RGB and thermal images captured from multiple viewpoints across 10 different scenes.
- **p. 4 / 3 METHOD - extractive body cue:** Then, we provide a detailed description of our method's specific implementation details, including multimodal initialization, three types of multimodal thermal Gaussians, thermal loss, and multimodal ...
- **p. 5 / 3 METHOD - extractive body cue:** Multimodal Fine-Tuning Gaussians (MFTG): Inspired by the fine-tuning approach used in largescale models, our first multimodal training strategy is training a basic Gaussian with RGB ...
- **p. 6 / 3 METHOD - extractive body cue:** However, because thermal images exhibit unique low-texture and ghosting characteristics, we design a specific thermal loss function to better accommodate these features.
- **p. 7 / 3 METHOD - extractive body cue:** Therefore, a regularization strategy is needed to dynamically adjust the weight of each modality's loss during training.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We capture simultaneous color and thermal images before thermal equilibrium, which occurs when two systems reach a balanced state with equal temperatures, halting heat flow. | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3 METHOD), p. 6 (3 METHOD) |
| State/latent | capture, simultaneous, color, thermal, images, before, equilibrium, occurs, when, systems, reach, balanced | geometry, map, object/relationship state | p. 5 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD) |
| Output/action | Subsequently, these rendered images of both modalities are compared separately with the ground truth of their respective inputs using loss functions: L = LRGB + Lthermal (7) The details of Lthermal constraint ... | point map, pose, scene graph, affordance 또는 query result | p. 6 (3 METHOD), p. 4 (3 METHOD), p. 2 (1 INTRODUCTION) |
| Objective/outcome | RGB rendering is achieved using Formula 3, while thermal rendering follows the equation below: T (x′) = X k∈N tkαk k-1 Y j=1 (1 -αj) (8) 3.4 THERMAL LOSS & MULTIMODAL REGULARIZATION ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 7 / 3 METHOD - extractive body cue:** The final design of this loss is: L = γLRGB + (1 -γ)Lthermal (12) 4 SELF-COLLECTED THERAML DATASET We introduce a new dataset, named RGBT-Scenes, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, the main contributions as follows: (1)We propose ThermalGaussian, the first multimodal 3DGS capable of simultaneously rendering photorealistic thermal and RGB images of a ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In contrast, our method not only improves thermal rendering quality but also enhances RGB rendering quality by 1 dB.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** The dataset consists of paired RGB and thermal images captured from multiple viewpoints across 10 different scenes.
- **p. 4 / 3 METHOD - extractive body cue:** Then, we provide a detailed description of our method's specific implementation details, including multimodal initialization, three types of multimodal thermal Gaussians, thermal loss, and multimodal ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** We not only achieve simultaneous rendering of thermal and RGB images but also significantly improve the rendering quality of both color and thermal images.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Compared to NeRF-based methods (Hassan et al., 2024) and methods that directly use thermal images for training 3DGS, our approach not only improves ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 5.1 IMPLEMENTATION DETAILS Our method is an improvement upon the 3DGS framework, with all experimental settings (e.g., λ) remaining consistent with the reference 3DGS.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Embodiment/environment | As shown in Table 2, even in scenes with pronounced thermal variations, specifically targeting lowtexture thermal characteristics, direct application of thermal data proves challenging for 3DGS. | hardware/simulator version and reset protocol | p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Dataset/benchmark | This enables our method to advance 3D reconstruction in low-light scenes and enhances the robustness of 3D reconstruction techniques to some extent. | role, split, size and leakage | p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Metric | In very few successful cases, inadequate precision in thermal camera positioning has compromised the quality of thermal reconstructions. | definition, denominator, direction and uncertainty | p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Baseline/ablation | We conducted ablation experiments by gradually adding each component to the baseline 3DGS model. | fair input/data/compute/action matching | p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Top: camera poses and point cloud generated by SfM. Bottom: input images for SfM. geometry methods (Newcombe et al., 2011) are used to ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Quantitative evaluation of thermal image using our method compared to previous work from test views. "×" indicates a failure to localize using only ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** We then performed a comprehensive comparison across various dimensions, including rendering capability, the quality of rendered color and thermal images, training time, model memory usage, ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Our results demonstrate that, under multimodal constraints, when one modality fails, our approach leverages accurate information from the other modality to enhance the model's understanding ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** In the appendix, we discuss the limitations of this work and potential directions for future research.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** This enables our method to advance 3D reconstruction in low-light scenes and enhances the robustness of 3D reconstruction techniques to some extent.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these datasets suffer from problems such as lack of color images registered with thermal images, inconsistencies in thermal information from different views, and watermarked images.를 문제로 두고, The final design of this loss is: L = γLRGB + (1 -γ)Lthermal (12) 4 SELF-COLLECTED THERAML DATASET We introduce a new dataset, named RGBT-Scenes, which consists of aligned collections of thermal ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 7 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 6 (3 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
