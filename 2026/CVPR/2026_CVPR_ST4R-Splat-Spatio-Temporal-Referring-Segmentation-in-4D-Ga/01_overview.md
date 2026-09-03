# ST4R-Splat: Spatio-Temporal Referring Segmentation in 4D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Meng_ST4R-Splat_Spatio-Temporal_Referring_Segmentation_in_4D_Gaussian_Splatting_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_ST4R-Splat_Spatio-Temporal_Referring_Segmentation_in_4D_Gaussian_Splatting_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 4D, referring segmentation
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Meng_ST4R-Splat_Spatio-Temporal_Referring_Segmentation_in_4D_Gaussian_Splatting_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_ST4R-Splat_Spatio-Temporal_Referring_Segmentation_in_4D_Gaussian_Splatting_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these representations are primarily optimized for geometric fidelity and novel view synthesis, inherently lacking support for semantic reasoning and language-based scene understanding.를 문제로 두고, In summary, our main contributions are as follows: • We introduce the novel task of STRS-4DGS (SpatioTemporal Referring Segmentation in 4D Gaussian Splatting) and construct a corresponding benchmark with spatio-temporally grounded refer ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Understanding objects in dynamic 4D environments via natural language is crucial yet underexplored.
- **p. 1 / Abstract - extractive body cue:** While existing methods focus on static 3D referring segmentation or openvocabulary 4D querying, they struggle to ground complex spatio-temporal referring expressions in explicit 4D reconstructions.
- **p. 1 / Abstract - extractive body cue:** We introduce Spatio-Temporal Referring Segmentation in 4D Gaussian Splatting (STRS-4DGS), a novel task aiming to jointly identify and segment a target instance across space and ...
- **p. 1 / Abstract - extractive body cue:** To tackle this, we propose ST4R-Splat, the first framework for STRS-4DGS.
- **p. 1 / Abstract - extractive body cue:** Specifically, our framework incorporates an Instance-Aware 4D Gaussian Referring Field that assigns time-invariant embeddings for robust spatial grounding, and an Instance-Level Temporal State Mapping module ...
- **p. 1 / 1. Introduction - extractive body cue:** However, these representations are primarily optimized for geometric fidelity and novel view synthesis, inherently lacking support for semantic reasoning and language-based scene understanding.
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we propose ST4R-Splat, the pioneering framework for STRS-4DGS.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • We introduce the novel task of STRS-4DGS (SpatioTemporal Referring Segmentation in 4D Gaussian Splatting) and construct ...
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we propose ST4R-Splat, the pioneering framework for STRS-4DGS.
- **p. 2 / 1. Introduction - extractive body cue:** These results validate our framework and establish a strong foundation for languagedriven scene understanding in dynamic 4D environments.
- **p. 1 / 1. Introduction - extractive body cue:** However, these representations are primarily optimized for geometric fidelity and novel view synthesis, inherently lacking support for semantic reasoning and language-based scene understanding.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** This allows 4DGS to reconstruct complex motion and appearance changes over time.
- **p. 3 / 3.2. Overview - extractive body cue:** The objective is to achieve spatial instance grounding within the 4D representation, rendering its segmentation masks across all frames during inference. • Time-sensitive referring queries ...
- **p. 3 / 3.3. Object Captioning via Multimodal Prompting - extractive body cue:** To avoid the issue of inconsistent referring granularity, we first define a set of object categories of interest, then leverage off-the-shelf vision foundation models to ...
- **p. 5 / 3.5. Instance-Level Temporal State Modeling - extractive body cue:** Formally, our objective is to model a function F that maps an instance's representative feature ¯ek and a given time t to its corresponding dynamic ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The objective is to achieve spatial instance grounding within the 4D representation, rendering its segmentation masks across all frames during inference. • Time-sensitive referring queries Esensitive: The target instance is specified by ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.2. Overview), p. 3 (3.1. Preliminaries) |
| State/latent | objective, achieve, spatial, instance, grounding, within, representation, rendering, segmentation, masks, across, frames | geometry, map, object/relationship state | p. 3 (3.2. Overview), p. 3 (3.1. Preliminaries), p. 1 (1. Introduction) |
| Output/action | This is achieved by learning a deformation field that predicts the offset from a canonical Gaussian gi to its deformed state gi(t) at a given timestamp: (µi(t), si(t), ri(t)) = (µi+∆µi(t), si+∆si(t), ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Preliminaries), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | This avoids 2D rendering losses and ensures consistent temporal localization across viewpoints. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3.2. Overview), p. 3 (3.2. Overview), p. 5 (3.5. Instance-Level Temporal State Modeling) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • We introduce the novel task of STRS-4DGS (SpatioTemporal Referring Segmentation in 4D Gaussian Splatting) and construct ...
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we propose ST4R-Splat, the pioneering framework for STRS-4DGS.
- **p. 2 / 1. Introduction - extractive body cue:** These results validate our framework and establish a strong foundation for languagedriven scene understanding in dynamic 4D environments.
- **p. 1 / 1. Introduction - extractive body cue:** However, these representations are primarily optimized for geometric fidelity and novel view synthesis, inherently lacking support for semantic reasoning and language-based scene understanding.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** This allows 4DGS to reconstruct complex motion and appearance changes over time.
- **p. 6 / 4.2. Results - extractive body cue:** ST4RSplat achieves an average accuracy of 83.44% and vIoU 17603
- **p. 6 / 4.2. Results - extractive body cue:** Our method achieves an average mIoU of 77.67%, demonstrating exceptional segmentation performance.
- **p. 7 / 4.2. Results - extractive body cue:** Best results are highlighted in bold. of 57.98%, substantially outperforming 4DLangSplat.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.2. Results), p. 6 (4.2. Results) |
| Embodiment/environment | To adapt it to our dynamic 4D benchmark as a strong baseline for timeagnostic queries, we train the model utilizing the exact same instance masks and our automatically generated text descriptions as ... | hardware/simulator version and reset protocol | p. 6 (4.1. Setup), p. 6 (4.1. Setup) |
| Dataset/benchmark | Quantitative comparisons on the HyperNeRF dataset. | role, split, size and leakage | p. 6 (4.1. Setup), p. 6 (4.1. Setup), p. 7 (4.2. Results), p. 7 (4.2. Results) |
| Metric | To comprehensively assess both temporal accuracy and segmentation quality, we adopt the vIoU metric, defined as vIoU = 1 /Su/ P t∈Si IoU(ˆst, st), where Su and Si denote the sets of ... | definition, denominator, direction and uncertainty | p. 6 (4.1. Setup), p. 6 (4.1. Setup), p. 8 (4.2. Results) |
| Baseline/ablation | Consequently, we adapt state-of-the-art approaches from closely related domains to establish strong baselines: • ReferSplat [9]: The current state-of-the-art for referring segmentation in 3D Gaussian Splatting. | fair input/data/compute/action matching | p. 6 (4.1. Setup), p. 6 (4.1. Setup), p. 7 (4.2. Results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Results - extractive body cue:** 4DLangSplat often fails to parse complex spatial relations within referring expressions.
- **p. 8 / 4.2. Results - extractive body cue:** It fails to effectively obtain features representing the temporal state, resulting in a substantial drop in accuracy (51.92% Acc).
- **p. 8 / 5. Conclusion - extractive body cue:** To tackle this, we proposed ST4RSplat, which incorporates an Instance-Aware 4D Referring Field for robust spatial grounding and an Instance-Level Temporal State Mapping module for ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1. Overview of the ST4R-Splat framework. It mainly consists of three main components: (I) MLLM-based object captioning for generating decoupled textual supervision, (II) an ...
- **p. 6 / 4.1. Setup - extractive body cue:** For robust object segmentation and tracking, we use the Unipixel [25] model along with the Grounded-SAM-2 [24, 30] model.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these representations are primarily optimized for geometric fidelity and novel view synthesis, inherently lacking support for semantic reasoning and language-based scene understanding.를 문제로 두고, In summary, our main contributions are as follows: • We introduce the novel task of STRS-4DGS (SpatioTemporal Referring Segmentation in 4D Gaussian Splatting) and construct a corresponding benchmark with spatio-temporally grounded refer ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminaries), p. 3 (3.2. Overview), p. 3 (3.3. Object Captioning via Multimodal Prompting) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
