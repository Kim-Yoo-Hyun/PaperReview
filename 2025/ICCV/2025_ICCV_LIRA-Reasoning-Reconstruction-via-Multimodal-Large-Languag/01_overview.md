# LIRA: Reasoning Reconstruction via Multimodal Large Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Vision-Language
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, existing systems [15, 27, 46, 47] mainly rely on explicit instructions, such as explicitly indicating target objects or categories, to reconstruct instruction-relevant regions, while implicit instruction reasoning is more impor ...를 문제로 두고, In summary, our major contributions are as follows: • We introduce the reasoning reconstruction task, which requires online 3D reconstruction guided by implicit and complex instructions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Existing language instruction-guided online 3D reconstruction systems mainly rely on explicit instructions or queryable maps, showing inadequate capability to handle implicit and complex instructions.
- **p. 1 / Abstract - extractive body cue:** In this paper, we first introduce a reasoning reconstruction task.
- **p. 1 / Abstract - extractive body cue:** This task inputs an implicit instruction involving complex reasoning and an RGB-D sequence, and outputs incremental 3D reconstruction of instances that conform to the instruction.
- **p. 1 / Abstract - extractive body cue:** To handle this task, we propose LIRA: Language Instructed Reconstruction Assistant.
- **p. 1 / Abstract - extractive body cue:** It leverages a multimodal large language model to actively reason about the implicit instruction and obtain instruction-relevant 2D candidate instances and their attributes.
- **p. 1 / 1. Introduction - extractive body cue:** However, existing systems [15, 27, 46, 47] mainly rely on explicit instructions, such as explicitly indicating target objects or categories, to reconstruct instruction-relevant regions, while ...
- **p. 2 / 1. Introduction - extractive body cue:** Particularly for implicit instructions involving complex reasoning, they are more difficult to handle.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our major contributions are as follows: • We introduce the reasoning reconstruction task, which requires online 3D reconstruction guided by implicit and complex ...
- **p. 2 / 1. Introduction - extractive body cue:** To achieve higher-quality instance fusion, we propose TIFF, a Text-enhanced Instance Fusion module operating within a Fragment bounding volume (FBV), which is learning-based and fuses ...
- **p. 4 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive body cue:** (3) Then, fimg and ˆhseg (text feature prompt) are input into the mask decoder Fdec of the segmentation foundation model to output the binary mask ...
- **p. 7 / 4.5. Runtime Analysis - extractive body cue:** To achieve real-time inference, we propose LIRA-Fast.
- **p. 4 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive body cue:** The image features directly use the image embeddings fimg of the segmentation foundation model in the 2D reasoning segmentation module.
- **p. 5 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive body cue:** Current Instances Global Instances Mask Confidence Branch Similarity Matrix Calculation x y z w h l 3D Bounding Boxes Masked Cross-Attention MLP Add & Norm ...
- **p. 7 / 4.4. Explicit Instruction-Guided Reconstruction - extractive body cue:** For example, an inStage Method AP AP50 AP25 I Replace with SEEM [59] 3.68 11.00 19.57 Replace with Grounded-SAM [25] 3.06 10.12 18.26 Replace with ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given an implicit and complex instruction L and posed RGB-D sequences as input, LIRA first incrementally performs geometric reconstruction, and leverages a MLLM to actively reason about L and obtain instruction-relevant 2D ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3. Method), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV) |
| State/latent | Given, implicit, complex, instruction, posed, RGB-D, sequences, input, LIRA, first, incrementally, performs | geometry, map, object/relationship state | p. 3 (3. Method), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 1 (1. Introduction) |
| Output/action | An image can only provide instance information within a local field of view, and the complex language instruction requires reasoning based on the global map. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | The perceptual information is progressively constructed into a global map containing multiple candidate instances in the brain. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3. Method), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 4 (3.1.1. Incremental Geometric Reconstruction) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our major contributions are as follows: • We introduce the reasoning reconstruction task, which requires online 3D reconstruction guided by implicit and complex ...
- **p. 2 / 1. Introduction - extractive body cue:** To achieve higher-quality instance fusion, we propose TIFF, a Text-enhanced Instance Fusion module operating within a Fragment bounding volume (FBV), which is learning-based and fuses ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Ablation studies of the three stages of LIRA. struction "Appliances or furniture used to store food" is replaced with "Cabinet, Refrigerator". The generated ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Visualization results of different reasoning reconstruction methods on the ReasonRecon test set. The reconstructed geometric results are augmented with image textures. Single-layered mesh ...
- **p. 6 / 4.3. Reasoning Reconstruction Results - extractive body cue:** Some of them are improved to support multi-instance outputs for a fair 1767
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Runtime analysis of reasoning reconstruction. comparison. VLMaps is extended to a 3D map by can- celing top-down projection. LIRA* represents that LIRA uses ...
- **p. 6 / 4.2. Evaluation Metrics - extractive body cue:** These metrics evaluate the performance of both geometric reconstruction and instance matching.
- **p. 8 / 4.7. Qualitative Results - extractive body cue:** More visualization results are given in the supplementary material.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | To establish a comprehensive evaluation system suitable for the reasoning reconstruction task, a benchmark ReasonRecon is constructed and the data collection pipeline is shown in Fig. | hardware/simulator version and reset protocol | p. 5 (3.4. Benchmark), p. 6 (3.4. Benchmark) |
| Dataset/benchmark | The training set and test set are divided into 8: 2. | role, split, size and leakage | p. 5 (3.4. Benchmark), p. 6 (3.4. Benchmark), p. 6 (3.4. Benchmark), p. 5 (3.4. Benchmark) |
| Metric | We evaluate using standard Average Precision (AP) metrics at IoU thresholds of 50% and 25%, and also calculate mean score across IoU thresholds from 50% to 95% in 5% increments. | definition, denominator, direction and uncertainty | p. 6 (4.2. Evaluation Metrics), p. 7 (Figure/Table caption), p. 7 (4.5. Runtime Analysis) |
| Baseline/ablation | Table 4. Runtime analysis of reasoning reconstruction. comparison. VLMaps is extended to a 3D map by can- celing top-down projection. LIRA* represents that LIRA uses LLaVA-13B and applies ChatGPT-4o for reasoning in ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 7 (4.5. Runtime Analysis), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** One limitation is that LIRA exhibits relatively low performance in high-precision reconstruction.
- **p. 8 / 5. Conclusion - extractive body cue:** Future work will consider further optimization in 3D space.
- **p. 6 / 3.4. Benchmark - extractive body cue:** Erroneous projected pixels caused by occlusion are filtered out.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, existing systems [15, 27, 46, 47] mainly rely on explicit instructions, such as explicitly indicating target objects or categories, to reconstruct instruction-relevant regions, while implicit instruction reasoning is more impor ...를 문제로 두고, In summary, our major contributions are as follows: • We introduce the reasoning reconstruction task, which requires online 3D reconstruction guided by implicit and complex instructions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 7 (4.5. Runtime Analysis) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
