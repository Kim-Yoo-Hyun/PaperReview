# Segment Any 3D Object with Language

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=ENv1CeTwxc.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114011. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://openreview.net/forum?id=ENv1CeTwxc
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/114011
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Failure to segment such instances drastically narrows the scope of application.를 문제로 두고, To circumvent this issue, we introduce Cross Modality Decoder (CMD) to incorporate textual information in the decoding process of our framework.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we investigate Open-Vocabulary 3D Instance Segmentation (OV3DIS) with free-form language instructions.
- **p. 1 / ABSTRACT - extractive body cue:** Earlier works mainly rely on annotated base categories for training which leads to limited generalization to unseen novel categories.
- **p. 1 / ABSTRACT - extractive body cue:** To mitigate the poor generalizability to novel categories, recent works generate class-agnostic masks or projecting generalized masks from 2D to 3D, subsequently classifying them with ...
- **p. 1 / ABSTRACT - extractive body cue:** However, these works often disregard semantic information in the mask generation, leading to sub-optimal performance.
- **p. 1 / ABSTRACT - extractive body cue:** Instead, generating generalizable but semantic-aware masks directly from 3D point clouds would result in superior outcomes.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Failure to segment such instances drastically narrows the scope of application.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Due to the lack of novel classes during training, these methods easily overfit to the base categories and thus yielding sub-optimal performance on novel categories.

## Core Idea

- **p. 5 / 3 METHOD - extractive body cue:** To circumvent this issue, we introduce Cross Modality Decoder (CMD) to incorporate textual information in the decoding process of our framework.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We propose a visual-language learning framework for OV-3DIS, SOLE.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** A multimodal fusion network is designed for SOLE, which can directly predict semantic-related masks from 3D point clouds with multimodal information, leading to high-quality and ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose SOLE: Segment any 3D Object with LanguagE to circumvent the abovementioned issues for OV-3DIS.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose the semantic-aware mask generator to obtain semantic-related masks from 3D point clouds, yielding better and more generalizable 3D masks.
- **p. 6 / 3 METHOD - extractive body cue:** 4, we first extract all the noun phrases ei for each mask caption ci and obtain the text feature of each noun phrase from CLIP ...
- **p. 6 / 3 METHOD - extractive body cue:** To this end, we propose a soft matching to get mask-entity association by multimodal attention.
- **p. 7 / 3 METHOD - extractive body cue:** For benchmark evaluation, we use CLIP textual features of all category names as the classifier.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The goal of open-vocabulary 3D instance segmentation (OV-3DIS) with free-form language instructions is defined as follows: Given a 3D point cloud P ∈RM×C, the corresponding 2D images I and the instance-level 3D ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3 METHOD), p. 3 (1 INTRODUCTION) |
| State/latent | goal, open-vocabulary, instance, segmentation, OV-3DIS, free-form, language, instructions, defined, follows, Given, point | geometry, map, object/relationship state | p. 4 (3 METHOD), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/action | The associations improve the mask quality and the response ability to language instructions. • SOLE achieves state-of-the-art results on ScanNetv2, Scannet200 and Replica benchmarks, and the results are even close to the ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective/outcome | The overall training loss is the combination of mask loss and semantic loss: | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 7 (3 METHOD), p. 7 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 5 / 3 METHOD - extractive body cue:** To circumvent this issue, we introduce Cross Modality Decoder (CMD) to incorporate textual information in the decoding process of our framework.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We propose a visual-language learning framework for OV-3DIS, SOLE.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** A multimodal fusion network is designed for SOLE, which can directly predict semantic-related masks from 3D point clouds with multimodal information, leading to high-quality and ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose SOLE: Segment any 3D Object with LanguagE to circumvent the abovementioned issues for OV-3DIS.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose the semantic-aware mask generator to obtain semantic-related masks from 3D point clouds, yielding better and more generalizable 3D masks.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** SOLE outperforms all the OV-3DIS methods and achieves competitive results with the fully-supervised model.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** SOLE outperforms state-of-the-art methods (Nguyen et al., 2024; Takmaz et al., 2023) on five out of the six metrics and achieves comparable performance on the ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** First, using any of multimodal associations can already achieve significant performance, outperforming previous state-of-the-art method (OpenIns3D (Huang et al., 2023b)) with larger voxel size (lower ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Embodiment/environment | Therefore, despite slightly impairing the performance on benchmark, mask-visual association and mask-caption association are crucial to recognizing free-form language instructions, benefiting the applications in real-world scenarios. | hardware/simulator version and reset protocol | p. 10 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Dataset/benchmark | Replica (Straub et al., 2019) is a high-quality synthetic dataset annotated with 48 instance categories. | role, split, size and leakage | p. 10 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Metric | Average precision (AP) of different IoU thresholds is adopted as the evaluation metric, including AP under 25%, 50% IoU and the average AP from 50% to 95% IoU. | definition, denominator, direction and uncertainty | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Baseline/ablation | Table 2: The comparison of closed-set 3D instance segmentation setting on ScanNet200. SOLE is compared with mask training methods on the overall segmentation performance and on each subset. SOLE significantly outperforms state-of-the-ar ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Left (a) : Previous works train class-agnostic mask proposal module with only using mask annotations. In the inference time, generated 3D masks are ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** In contrast, solely using 3D instance backbone feature f b (second row) cannot inherit the generalizable semantic information, resulting in sub-optimal performance.
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Given a free-form language instruction instead of category name, e.g., "I wanna see outside", the model only using mask-entity association cannot segment the correct instance ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4, our method further shows superior robustness on more out-of-distribution data from Replica, achieving +9.8% improvement in AP score compared to Open3DIS.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Both in-distribution ("base") and out-of-distribution ("novel") classes are reported in Tab.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Failure to segment such instances drastically narrows the scope of application.를 문제로 두고, To circumvent this issue, we introduce Cross Modality Decoder (CMD) to incorporate textual information in the decoding process of our framework.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
