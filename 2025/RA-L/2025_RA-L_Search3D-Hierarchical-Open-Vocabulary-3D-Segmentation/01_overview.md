# Search3D: Hierarchical Open-Vocabulary 3D Segmentation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2409.18431.
> PDF retrieval source: https://arxiv.org/pdf/2409.18431. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RA-L
- Authors: Ayca Takmaz, Alexandros Delitzas, Robert W. Sumner, Francis Engelmann, Johanna Wald, Federico Tombari
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, semantic, 3D segmentation
- Official paper: https://arxiv.org/abs/2409.18431
- Full-text retrieval: https://arxiv.org/pdf/2409.18431
- Code/Project: http://search3d-segmentation.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Search3D는 자유로운 텍스트 질의로 3D 장면의 물체와 그보다 작은 부위·속성 영역을 찾는다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary 3D segmentation enables exploration of 3D spaces using free-form text descriptions.
- **p. 1 / Abstract - extractive body cue:** Existing methods for open-vocabulary 3D instance segmentation primarily focus on identifying object-level instances but struggle with finer-grained scene entities such as object parts, or regions ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce Search3D, an approach to construct hierarchical open-vocabulary 3D scene representations, enabling 3D search at multiple levels of granularity: fine-grained object ...
- **p. 1 / Abstract - extractive body cue:** Unlike prior methods, Search3D shifts towards a more flexible open-vocabulary 3D search paradigm, moving beyond explicit object-centric queries.
- **p. 1 / Abstract - extractive body cue:** For systematic evaluation, we further contribute a scene-scale open-vocabulary 3D part segmentation benchmark based on MultiScan, along with a set of open-vocabulary fine-grained part annotations ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, the least obvious limitation is derived from the way these models compute the point-level features: Although the projected open-vocabulary features are fine-grained at the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, storing these per-point features is memoryintensive, they are inherently noisy, and they lack instance-level information - a critical requirement for real-world applications in which ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** To summarize our key contributions: • We propose a hierarchical open-vocabulary 3D segmentation method capable of segmenting both entire objects and their parts given arbitrary ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To evaluate our method, we introduce a novel evaluation suite for open-vocabulary scene-scale 3D part segmentation based on MultiScan [16].
- **p. 3 / III. METHOD - extractive body cue:** We introduce a novel hierarchical 3D scene representation enabling open-vocabulary segmentation for scene entities at multiple granularities, including objects and their parts.
- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: We propose Search3D, a method for open-vocabulary 3D search at multiple levels of granularity.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables searching across objects, parts, and attributes matching any given user query (right). critical to scene interaction.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Object-centric open-vocabulary 3D segmentation methods typically first extract a set of class-agnostic 3D object instance masks and then compute a feature representation per object, represented ...
- **p. 4 / 2) Computing open-vocabulary features for the scene repre - extractive body cue:** These 2D segment crops are then passed through the SigLIP [32] image encoder, producing feature vectors of dimension D for each segment.
- **p. 4 / 2) Computing open-vocabulary features for the scene repre - extractive body cue:** To address this challenge, we propose a method to extract pixel-aligned features capable of representing finer-grained scene entities.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This representation is built upon 3D scenes reconstructed using posed RGB-D image sequences, as shown in Fig. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| State/latent | representation, built, upon, scenes, reconstructed, posed, RGB-D, image, sequences, Fig, enables, searching | geometry, map, object/relationship state | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Output/action | This enables searching across objects, parts, and attributes matching any given user query (right). critical to scene interaction. | point map, pose, scene graph, affordance 또는 query result | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (2) Computing open-vocabulary features for the scene repre) |
| Objective/outcome | For each 3D segment, neighboring segments within the same object that exhibit similar features are identified and merged based on two constraints: 1) Proximity: The closest distance between points in the segments ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (2) Computing open-vocabulary features for the scene repre), p. 4 (2) Computing open-vocabulary features for the scene repre) |

## Main Claims and Actual Contribution

- 여러 크기의 장면 요소에 대응하는 표현을 사용해 세밀한 질의를 지원한다.
- MultiScan 기반 부위 분할 벤치마크와 ScanNet++의 세밀한 부위 주석을 제공한다.

[원문 초록](https://arxiv.org/abs/2409.18431)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Embodiment/environment | 3D Material Segmentation Next, we perform an analysis on 3D material segmentation task using the object-level material annotations from the 3RScan dataset [18]. | hardware/simulator version and reset protocol | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Dataset/benchmark | 3D Part Segmentation To evaluate our method's ability to handle queries beyond object-level descriptions, we introduce the task of scene-level 3D open-vocabulary part segmentation. | role, split, size and leakage | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Metric | Additionally, averaging the objectlevel and part-level similarity scores yields slightly better results than using the maximum of these scores. | definition, denominator, direction and uncertainty | p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Baseline/ablation | First, we evaluate the quality of our segment features for identifying object parts using an oracle mask experiment, isolating feature quality from the effect of 3D geometric part segmentation quality. | fair input/data/compute/action matching | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / V. EXPERIMENTS - extractive body cue:** Nevertheless, there are limitations to the geometrical segmentation method we employ for part segmentation, as it relies on surface normals.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Discussion and Limitations One limitation of our work is the reliance on a simple geometrical over-segmentation method for identifying object parts.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)이다.
