# Search3D: Hierarchical Open-Vocabulary 3D Segmentation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2409.18431.
> PDF retrieval source: https://arxiv.org/pdf/2409.18431. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, semantic
- Official paper: https://arxiv.org/abs/2409.18431
- Full-text retrieval: https://arxiv.org/pdf/2409.18431
- Code/Project: http://search3d-segmentation.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Finally, the least obvious limitation is derived from the way these models compute the point-level features: Although the projected open-vocabulary features are fine-grained at the level of the geometrical scene representation, the ...를 문제로 두고, To summarize our key contributions: • We propose a hierarchical open-vocabulary 3D segmentation method capable of segmenting both entire objects and their parts given arbitrary textual queries, by aggregating features anchored to ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / I. INTRODUCTION - extractive body cue:** To summarize our key contributions: • We propose a hierarchical open-vocabulary 3D segmentation method capable of segmenting both entire objects and their parts given arbitrary ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To evaluate our method, we introduce a novel evaluation suite for open-vocabulary scene-scale 3D part segmentation based on MultiScan [16].
- **p. 3 / III. METHOD - extractive body cue:** We introduce a novel hierarchical 3D scene representation enabling open-vocabulary segmentation for scene entities at multiple granularities, including objects and their parts.
- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: We propose Search3D, a method for open-vocabulary 3D search at multiple levels of granularity.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables searching across objects, parts, and attributes matching any given user query (right). critical to scene interaction.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** It demonstrates the strong open-vocabulary part-segmentation performance of our segment-level features, with at least + 13.8 AP improvement over baseline methods.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** V, our method has very strong 3D instance segmentation performance, outperforming other counterparts that rely solely on 3D masks for identifying object-level instances.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** II, where oracle mask experiment yields much higher AP scores than those with predicted part masks, indicating room for improvement in 3D part mask quality.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Finally, the least obvious limitation is derived from the way these models compute the point-level features: Although the projected open-vocabulary features are fine-grained at the level of the geometrical scene representation, the ...를 문제로 두고, To summarize our key contributions: • We propose a hierarchical open-vocabulary 3D segmentation method capable of segmenting both entire objects and their parts given arbitrary textual queries, by aggregating features anchored to ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
