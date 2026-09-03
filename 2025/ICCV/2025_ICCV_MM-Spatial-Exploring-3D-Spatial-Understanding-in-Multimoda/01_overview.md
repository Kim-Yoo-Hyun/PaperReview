# MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Daxberger_MM-Spatial_Exploring_3D_Spatial_Understanding_in_Multimodal_LLMs_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Daxberger_MM-Spatial_Exploring_3D_Spatial_Understanding_in_Multimodal_LLMs_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Daxberger_MM-Spatial_Exploring_3D_Spatial_Understanding_in_Multimodal_LLMs_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Daxberger_MM-Spatial_Exploring_3D_Spatial_Understanding_in_Multimodal_LLMs_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Multimodal large language models (MLLMs) excel at 2D visual understanding but remain limited in their ability to reason about 3D space.를 문제로 두고, We use the MM1.5 architecture [85, 128] (focusing on the mobile-friendly 3B variant), comprising of a DFN-CLIP [34, 89] image encoder and a decoder-only LLM backbone, which are bridged via a C-Abstractor ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Multimodal large language models (MLLMs) excel at 2D visual understanding but remain limited in their ability to reason about 3D space.
- **p. 1 / Abstract - extractive body cue:** In this work, we leverage large-scale high-quality 3D scene data with open-set annotations to introduce 1) a novel supervised fine-tuning dataset and 2) a new ...
- **p. 1 / Abstract - extractive body cue:** Our Cubify Anything VQA (CA-VQA) data covers diverse spatial tasks including spatial relationship prediction, metric size and distance estimation, and 3D grounding.
- **p. 1 / Abstract - extractive body cue:** We show that CA-VQA enables us to train MM-Spatial, a strong generalist MLLM that also achieves state-of-the-art performance on 3D spatial understanding benchmarks, including our ...
- **p. 1 / 1. Introduction - extractive body cue:** Understanding object locations and spatial relationships in both 2D and 3D space is crucial for interpreting complex visual scenes.

## Core Idea

- **p. 4 / 4.1. Model Architecture - extractive body cue:** We use the MM1.5 architecture [85, 128] (focusing on the mobile-friendly 3B variant), comprising of a DFN-CLIP [34, 89] image encoder and a decoder-only LLM ...
- **p. 4 / 4.2. Data and Training - extractive body cue:** We use AXLearn [7] for model training.
- **p. 6 / Model - extractive body cue:** 13 ), suggesting that our model can successfully use additional views to improve 3D perception. • Multi-view 19 vs.
- **p. 6 / Model - extractive body cue:** 2D object grounding and depth prediction) and/or leveraging more test-time compute benefits model accuracy. • Depth (GT): Tool-use vs.
- **p. 7 / Model - extractive body cue:** We evaluate the metric depth estimates of our CoT model produced as part of its responses on the CA-VQA benchmark.
- **p. 7 / Model - extractive body cue:** MM-Spatial-3B substantially outperforms the (much larger) SOTA models, with CoT and depth input further improving performance.
- **p. 8 / Model - extractive body cue:** Training on a mixture of CA-VQAω and OSD performs best.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | MM-Spatial-3B achieves SOTA with both image-only input and tool-use monocular depth, outperforming SpatialRGPT-VILA-1.5-8B (which fully encodes depth). | RGB-D, image set, point cloud, depth와 camera pose | p. 8 (Model), p. 1 (1. Introduction) |
| State/latent | MM-Spatial-3B, achieves, SOTA, image-only, input, tool-use, monocular, depth, outperforming, SpatialRGPT-VILA-1, fully, encodes | geometry, map, object/relationship state | p. 8 (Model), p. 1 (1. Introduction), p. 4 (4.1. Model Architecture) |
| Output/action | There have been comparatively few works on 3D object perception with MLLMs [15, 20, 27, 28, 32, 98]; moreover, they only consider a subset of tasks, and do not comprehensively assess depth ... | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 4 (4.1. Model Architecture), p. 4 (4.1. Model Architecture) |
| Objective/outcome | geometric accuracy, semantic consistency와 planning/manipulation utility | geometric accuracy, semantic consistency와 planning/manipulation utility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. CA-VQA Results. MM-Spatial-3B significantly outperforms (much larger) top open-source and commercial models across all tasks, demonstrating its strong spatial understanding ability. Model performance ...
- **p. 5 / 5.2. Overview of Benchmark Category Results - extractive body cue:** MM-Spatial significantly improves on the Spatial category while maintaining performance competitive with MM1.5 across the other categories, suggesting that spatial reasoning can be improved without ...
- **p. 7 / 5.4. CV-Bench Results - extractive body cue:** 4 demonstrate that MMSpatial-3B 10 significantly outperforms the much larger SOTA Cambrian-1-34B 8 , highlighting the effectiveness of SFT on similar data.
- **p. 2 / 3. We run extensive experiments illustrating the benefits - extractive body cue:** We show that 1) we can train MM-Spatial, a generalist MLLM achieving SOTA on spatial understanding benchmarks (CV-Bench, SpatialRGPT-Bench, CA-VQA), while retaining performance on other ...
- **p. 5 / 5.1. Model Variants - extractive body cue:** Benchmark Category Results MM-Spatial is a generalist MLLM that improves strongly on the Spatial category while rivaling the MM1.5 baseline across the other task categories. ...
- **p. 7 / 5.4. CV-Bench Results - extractive body cue:** Notably, MM-Spatial (Blind eval) 13 achieves the best accuracy among all models on the 2D Object Count task, revealing a substantial bias in this benchmark.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 6. SpatialRGPT-Bench Results. MM-Spatial-3B achieves SOTA with both image-only input and tool-use monocular depth, out- performing SpatialRGPT-VILA-1.5-8B (which fully encodes depth). Training on a ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 5 (5.2. Overview of Benchmark Category Results) |
| Embodiment/environment | CA-VQA is the first dataset that is based on high-quality 3D ground truth, includes depth maps (both from sensors and monocular) and multi-view images, covers a variety of tasks (relationships, metric estimation, ... | hardware/simulator version and reset protocol | p. 2 (Dataset), p. 2 (Dataset) |
| Dataset/benchmark | To enable a fair comparison of model capabilities, we thus align with the benchmark by generating CA-VQAω, a variant of CA-VQA adopting their AABB-based definitions, and train 1Note that DepthPro's training data ... | role, split, size and leakage | p. 2 (Dataset), p. 2 (Dataset), p. 7 (5.5. SpatialRGPT-Bench Results), p. 5 (5.1. Model Variants) |
| Metric | Table 5. Metric Depth Estimation Results. We evaluate the metric depth estimates of our CoT model produced as part of its responses on the CA-VQA benchmark. We compare against the tool-use estimates ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 5 (5.1. Model Variants), p. 7 (5.4. CV-Bench Results) |
| Baseline/ablation | In contrast, on our CA-VQA benchmark, using vision input outperforms the blind baseline on Counting by →13 points. | fair input/data/compute/action matching | p. 7 (5.4. CV-Bench Results), p. 6 (Figure/Table caption), p. 5 (5.2. Overview of Benchmark Category Results) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Dataset - extractive body cue:** CA-VQA is the first dataset that is based on high-quality 3D ground truth, includes depth maps (both from sensors and monocular) and multi-view images, covers ...
- **p. 8 / 6. Conclusion - extractive body cue:** In future work, we aim to extend our scope to outdoor scenes to complement our high-quality indoor dataset.
- **p. 5 / 5.3. Results on our CA-VQA Benchmark - extractive body cue:** MM-Spatial-3B 8 substantially outperforms various (much larger) top opensource and commercial models 1 - 6 , incl. the SOTA GPT-4o model 3 , demonstrating 1) ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 6. SpatialRGPT-Bench Results. MM-Spatial-3B achieves SOTA with both image-only input and tool-use monocular depth, out- performing SpatialRGPT-VILA-1.5-8B (which fully encodes depth). Training on a ...
- **p. 5 / 5.1. Model Variants - extractive body cue:** Strong commercial (2a&b) and research models (2c&d) fail.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Multimodal large language models (MLLMs) excel at 2D visual understanding but remain limited in their ability to reason about 3D space.를 문제로 두고, We use the MM1.5 architecture [85, 128] (focusing on the mobile-friendly 3B variant), comprising of a DFN-CLIP [34, 89] image encoder and a decoder-only LLM backbone, which are bridged via a C-Abstractor ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (4.1. Model Architecture), p. 4 (4.2. Data and Training), p. 6 (Model), p. 6 (Model), p. 7 (Model), p. 7 (Model) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
