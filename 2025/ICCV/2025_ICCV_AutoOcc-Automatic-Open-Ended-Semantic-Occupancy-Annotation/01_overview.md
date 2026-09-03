# AutoOcc: Automatic Open-Ended Semantic Occupancy Annotation via Vision-Language Guided Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_AutoOcc_Automatic_Open-Ended_Semantic_Occupancy_Annotation_via_Vision-Language_Guided_Gaussian_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_AutoOcc_Automatic_Open-Ended_Semantic_Occupancy_Annotation_via_Vision-Language_Guided_Gaussian_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: semantic occupancy, Vision-Language, Gaussian Splatting
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_AutoOcc_Automatic_Open-Ended_Semantic_Occupancy_Annotation_via_Vision-Language_Guided_Gaussian_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_AutoOcc_Automatic_Open-Ended_Semantic_Occupancy_Annotation_via_Vision-Language_Guided_Gaussian_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Despite its promising applications, automatic generation of precise and complete semantic occupancy annotations from raw sensor data remains a fundamental challenge, particularly in the pursuit of costeffective solutions for real-world ...를 문제로 두고, Our main contributions include: • We present AutoOcc, a vision-centric automatic annotation pipeline that supports open-ended semantic 3D occupancy label generation, based on vision-language guided differentiable reconstruction. • We de ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Obtaining high-quality 3D semantic occupancy from raw sensor data remains an essential yet challenging task, often requiring extensive manual labeling.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose AutoOcc, a vision-centric automated pipeline for open-ended semantic occupancy annotation that integrates differentiable Gaussian splatting guided by visionlanguage models.
- **p. 1 / Abstract - extractive body cue:** We formulate the open-ended semantic 3D occupancy reconstruction task to automatically generate scene occupancy by combining attention maps from vision-language models and foundation vision models.
- **p. 1 / Abstract - extractive body cue:** We devise semantic-aware Gaussians as intermediate geometric descriptors and propose a cumulative Gaussian-to-voxel splatting algorithm that enables effective and efficient occupancy annotation.
- **p. 1 / Abstract - extractive body cue:** Our framework outperforms existing automated occupancy annotation methods without human *Corresponding author. labels.
- **p. 1 / 1. Introduction - extractive body cue:** Despite its promising applications, automatic generation of precise and complete semantic occupancy annotations from raw sensor data remains a fundamental challenge, particularly in the pursuit ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these limitations, we present AutoOcc, a fully automated framework for open-ended semantic occupancy annotation that requires neither manual labeling nor predefined categories.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions include: • We present AutoOcc, a vision-centric automatic annotation pipeline that supports open-ended semantic 3D occupancy label generation, based on vision-language guided ...
- **p. 5 / 3.2. VL-GS - extractive body cue:** Unlike dense voxels or point clouds, our method allows for representing regions of interest with sparse Gaussians, aided by scalability and semantic attention maps.
- **p. 2 / 1. Introduction - extractive body cue:** Our method further exhibits excellent open-ended and zero-shot generalization capabilities, as evidenced by cross-dataset experiments.
- **p. 4 / 3. Method - extractive body cue:** Concurrently, our method supports LiDAR input, serving as a robust geometric prior constraint.
- **p. 4 / 3.1. Vision-Language Guidance - extractive body cue:** To overcome these limitations, we propose a guidance framework centered around semantic attention maps and resolve ambiguities through scene reconstruction, thereby preserving 3D semantic and ...
- **p. 4 / 3.1. Vision-Language Guidance - extractive body cue:** Specifically, we use the attention map generation method [1, 29] to compute and aggregate the attentions from transformer decoder, with N output tokens S = ...
- **p. 4 / 3.1. Vision-Language Guidance - extractive body cue:** We then rasterize the attention maps corresponding to these semantic categories into 2D feature maps, with each category represented by an aggregated attention map M.
- **p. 5 / 3.2. VL-GS - extractive body cue:** We then implement a geometry-aware loss to enforce the alignment of Gaussian ellipsoid distributions with the geometric 3371

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given a multi-view image sequence as input, we employ a fixed text prompt to enumerate all possible objects within the scene. | camera/depth stream, pose, map와 language goal | p. 4 (3. Method), p. 4 (3.1. Vision-Language Guidance) |
| State/latent | Given, multi-view, image, sequence, input, employ, fixed, text, prompt, enumerate, possible, objects | robot pose, free-space/semantic map와 local goal | p. 4 (3. Method), p. 4 (3.1. Vision-Language Guidance), p. 6 (3.2. VL-GS) |
| Output/action | Specifically, we use the attention map generation method [1, 29] to compute and aggregate the attentions from transformer decoder, with N output tokens S = s1, · · · , sN and ... | collision-free trajectory 또는 velocity command | p. 4 (3.1. Vision-Language Guidance), p. 6 (3.2. VL-GS), p. 2 (1. Introduction) |
| Objective/outcome | Our pipeline also supports the use of LiDAR to obtain geometric constraints and continuously optimize the distribution of Gaussians. | goal reach, safety, localization error와 replanning latency | p. 5 (3.2. VL-GS), p. 4 (3.1. Vision-Language Guidance), p. 4 (3. Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions include: • We present AutoOcc, a vision-centric automatic annotation pipeline that supports open-ended semantic 3D occupancy label generation, based on vision-language guided ...
- **p. 5 / 3.2. VL-GS - extractive body cue:** Unlike dense voxels or point clouds, our method allows for representing regions of interest with sparse Gaussians, aided by scalability and semantic attention maps.
- **p. 2 / 1. Introduction - extractive body cue:** Our method further exhibits excellent open-ended and zero-shot generalization capabilities, as evidenced by cross-dataset experiments.
- **p. 4 / 3. Method - extractive body cue:** Concurrently, our method supports LiDAR input, serving as a robust geometric prior constraint.
- **p. 4 / 3.1. Vision-Language Guidance - extractive body cue:** To overcome these limitations, we propose a guidance framework centered around semantic attention maps and resolve ambiguities through scene reconstruction, thereby preserving 3D semantic and ...
- **p. 6 / 4.2. Performance Evaluation and Analysis - extractive body cue:** As shown in Table 2, our vision-centric method outperforms these pipelines that utilize LiDAR point clouds.
- **p. 7 / 4.2. Performance Evaluation and Analysis - extractive body cue:** As shown in Table 2, using pure visual input, our method outperforms GaussianOcc [13], which utilizes vanilla GS as an intermediate representation.
- **p. 7 / 4.2. Performance Evaluation and Analysis - extractive body cue:** In extreme weather conditions (e.g., rain and nighttime), our method maintains robust performance, achieving annotation results comparable to or even surpassing manually labeled ground truth.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis) |
| Embodiment/environment | We use two benchmarks for evaluation: Occ3D-nuScenes, which is used to compare the performance of our method with other occupancy annotation methods for specific categories, while SemanticKITTI is used to assess the ... | hardware/simulator version and reset protocol | p. 6 (4.1. Implementation Details), p. 7 (4.2. Performance Evaluation and Analysis) |
| Dataset/benchmark | Our method enables high-quality annotation of semantic 3D occupancy, capturing fine-grained geometry, structurally challenging regions, and dynamic objects across complex scenes. demonstrates better performance, based on the deep integr ... | role, split, size and leakage | p. 6 (4.1. Implementation Details), p. 7 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis), p. 6 (4.1. Implementation Details) |
| Metric | Table 2. Semantic occupancy annotation on Occ3D-nuScenes [46]. C represents camera, and L denotes LiDAR. "cons. veh." and "drive. surf." stand for construction vehicles and driveable surfaces, respectively. AutoOcc-V uses only images ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 6 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis) |
| Baseline/ablation | We evaluate our method against the state-of-the-art (SOTA) methods for automatic semantic occupancy annotation, including offline methods [32, 49, 51] and self-supervised online methods [3, 13, 66]. | fair input/data/compute/action matching | p. 6 (4.2. Performance Evaluation and Analysis), p. 6 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Performance Evaluation and Analysis - extractive body cue:** In extreme weather conditions (e.g., rain and nighttime), our method maintains robust performance, achieving annotation results comparable to or even surpassing manually labeled ground truth.
- **p. 7 / 4.2. Performance Evaluation and Analysis - extractive body cue:** While the aforementioned approaches do not require additional supervision, they struggle with efficiently modeling semantic geometry and neglect dynamic objects, leading to performance degradation.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Despite its promising applications, automatic generation of precise and complete semantic occupancy annotations from raw sensor data remains a fundamental challenge, particularly in the pursuit of costeffective solutions for real-world ...를 문제로 두고, Our main contributions include: • We present AutoOcc, a vision-centric automatic annotation pipeline that supports open-ended semantic 3D occupancy label generation, based on vision-language guided differentiable reconstruction. • We de ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.1. Vision-Language Guidance), p. 4 (3.1. Vision-Language Guidance) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
