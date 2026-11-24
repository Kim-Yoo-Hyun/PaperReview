# ThermalGaussian: Thermal 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/03bdba50e3741ac5e3eaa0e55423587e-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114610. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Rongfeng Lu, Hangyu Chen, Zunjie Zhu, Yuhang Qin, Ming Lu, Le Zhang, Chenggang Yan, Anke Xue
- 저자 판본: ICLR 게재본 표제면에 따라 Le Zhang과 Anke Xue의 대소문자를 고쳤다. [표제면](https://proceedings.iclr.cc/paper_files/paper/2025/file/03bdba50e3741ac5e3eaa0e55423587e-Paper-Conference.pdf#page=1) · [학회 서지](https://proceedings.iclr.cc/paper_files/paper/2025/hash/03bdba50e3741ac5e3eaa0e55423587e-Abstract-Conference.html)
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D Vision
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/03bdba50e3741ac5e3eaa0e55423587e-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/03bdba50e3741ac5e3eaa0e55423587e-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://proceedings.iclr.cc/paper_files/paper/2025/file/03bdba50e3741ac5e3eaa0e55423587e-Paper-Conference.pdf)

## Why This Paper Is Here

ThermalGaussian은 같은 장면을 촬영한 RGB와 열화상 카메라를 정렬해 두 종류의 영상을 렌더링할 수 있는 가우시안 지도를 만든다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/03bdba50e3741ac5e3eaa0e55423587e-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/03bdba50e3741ac5e3eaa0e55423587e-Paper-Conference.pdf#page=4)

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

- 카메라 간 기하 보정을 수행하고 두 모달리티의 공동 정규화 및 열화상 평활화 제약으로 하나의 장면 표현을 학습한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/03bdba50e3741ac5e3eaa0e55423587e-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/03bdba50e3741ac5e3eaa0e55423587e-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/03bdba50e3741ac5e3eaa0e55423587e-Paper-Conference.pdf#page=6)
- 휴대형 열적외선 장비로 수집한 RGBT-Scenes를 제공하고, RGB와 열화상 렌더링 품질을 별도 표에서 비교했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/03bdba50e3741ac5e3eaa0e55423587e-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/03bdba50e3741ac5e3eaa0e55423587e-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/03bdba50e3741ac5e3eaa0e55423587e-Paper-Conference.pdf#page=9)

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

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 7 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 6 (3 METHOD)이다.
