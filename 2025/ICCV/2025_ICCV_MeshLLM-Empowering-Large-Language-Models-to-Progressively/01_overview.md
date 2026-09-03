# MeshLLM: Empowering Large Language Models to Progressively Understand and Generate 3D Mesh

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (3 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (3 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The evaluation of the generation of 3D mesh can be challenging due to the lack of direct correspondence with ground truth data.를 문제로 두고, In MeshLLM, we introduce a progressive training strategy that begins with KNN-based Primitive-Mesh samples, followed by Semantic-based Primitive-Mesh samples, and concludes with training on specific mesh generation and understanding tasks.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Body text (section not recovered) - extractive body cue:** MeshLLM: Empowering Large Language Models to Progressively Understand and Generate 3D Mesh Supplementary Material
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** We begin by densely sampling point clouds from the mesh and then apply farthest point sampling (FPS) and KNN to identify central points and point ...
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** For mesh-derived dense point clouds, FPS begins with a random point and iteratively chooses the farthest point to yield N center points.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** These N points serve as centroids for KNN clustering.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** The face category is determined through a voting process based on the categories of these sampled points.
- **p. 1 / 1.2. Metric Details - extractive body cue:** The evaluation of the generation of 3D mesh can be challenging due to the lack of direct correspondence with ground truth data.
- **p. 1 / 2.1. Shape Novelty Analysis - extractive body cue:** This demonstrates that our model possesses generalization ability and creativity rather than merely replicating training samples.

## Core Idea

- **p. 2 / 2.2. Training Strategy Analysis - extractive body cue:** In MeshLLM, we introduce a progressive training strategy that begins with KNN-based Primitive-Mesh samples, followed by Semantic-based Primitive-Mesh samples, and concludes with training on specific ...
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** SamPart3D is pretrained on Objaverse [2] with a 3D backbone network designed to extract visual features.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** This ensures compliance with the token length constraints of large language models, effectively expanding the scale of trainable data.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For mesh-derived dense point clouds, FPS begins with a random point and iteratively chooses the farthest point to yield N center points. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh) |
| State/latent | mesh-derived, dense, point, clouds, FPS, begins, random, iteratively, chooses, farthest, yield, center | geometry, map, object/relationship state | p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh) |
| Output/action | We begin by densely sampling point clouds from the mesh and then apply farthest point sampling (FPS) and KNN to identify central points and point clusters. | point map, pose, scene graph, affordance 또는 query result | p. 1 (1.1. Construction of Primitive-Mesh) |
| Objective/outcome | This strategy provides more accurate semantic information for mesh parts but is time-consuming and incurs API query costs. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh) |

## Main Claims and Actual Contribution

- **p. 2 / 2.2. Training Strategy Analysis - extractive body cue:** In MeshLLM, we introduce a progressive training strategy that begins with KNN-based Primitive-Mesh samples, followed by Semantic-based Primitive-Mesh samples, and concludes with training on specific ...
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** SamPart3D is pretrained on Objaverse [2] with a 3D backbone network designed to extract visual features.
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Effect of the training order. MeshLLMR refers to the reversed training order, where the Semantic-based Primitive-Mesh is trained first, followed by the KNN-based ...
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** By integrating these segments with their corresponding textual labels, our proposed MeshLLM significantly enhances performance.
- **p. 2 / 2.2. Training Strategy Analysis - extractive body cue:** As shown in Table 1, training on semantic Primitive-Mesh samples later yields better results.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** This strategy is highly efficient, requiring only 0.2 seconds to segment a 3D mesh, enabling the rapid generation of large-scale results.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 3 (Figure/Table caption), p. 1 (1.1. Construction of Primitive-Mesh) |
| Embodiment/environment | We utilize 128 A800 GPUs and spent over three days constructing this dataset. | hardware/simulator version and reset protocol | p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh) |
| Dataset/benchmark | In MeshLLM, we introduce a progressive training strategy that begins with KNN-based Primitive-Mesh samples, followed by Semantic-based Primitive-Mesh samples, and concludes with training on specific mesh generation and understanding tasks. | role, split, size and leakage | p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh), p. 2 (2.2. Training Strategy Analysis) |
| Metric | We compute the Chamfer Distance between samples to identify the three most similar training meshes to the generated meshes for comparison. | definition, denominator, direction and uncertainty | p. 1 (2.1. Shape Novelty Analysis), p. 1 (2.1. Shape Novelty Analysis), p. 2 (2.1. Shape Novelty Analysis) |
| Baseline/ablation | And NX in the 1-NNA metric is a point cloud that is closest to X in both the generated and reference dataset, i.e., NX = arg min K∈Sr∪Sg D(X, K) To evaluate ... | fair input/data/compute/action matching | p. 1 (1.2. Metric Details), p. 1 (2.1. Shape Novelty Analysis), p. 3 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Failure case. The limited semantic dataset size reduces text-geometry alignment for more fine-grained generations.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The evaluation of the generation of 3D mesh can be challenging due to the lack of direct correspondence with ground truth data.를 문제로 두고, In MeshLLM, we introduce a progressive training strategy that begins with KNN-based Primitive-Mesh samples, followed by Semantic-based Primitive-Mesh samples, and concludes with training on specific mesh generation and understanding tasks.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1.2. Metric Details), p. 1 (2.1. Shape Novelty Analysis), p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh), p. 3 (Figure/Table caption), p. 1 (1.1. Construction of Primitive-Mesh) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
