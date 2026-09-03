# Multimodality Helps Few-shot 3D Point Cloud Semantic Segmentation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=jXvwJ51vcK.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/111762. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic, alignment, point cloud, 3D Vision
- Official paper: https://openreview.net/forum?id=jXvwJ51vcK
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/111762
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To address this challenge, few-shot 3D point cloud semantic segmentation (FS-PCS) has recently attracted increasing attention, enabling models to generalize to unseen/novel categories with just a few annotated samples.를 문제로 두고, Under this cost-free multimodal FS-PCS setup, we introduce a novel model, MultiModal Few-Shot SegNet (MM-FSS), to effectively address FS-PCS by harnessing complementary information from different modalities.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Few-shot 3D point cloud segmentation (FS-PCS) aims at generalizing models to segment novel categories with minimal annotated support samples.
- **p. 1 / ABSTRACT - extractive body cue:** While existing FS-PCS methods have shown promise, they primarily focus on unimodal point cloud inputs, overlooking the potential benefits of leveraging multimodal information.
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we address this gap by introducing a multimodal FS-PCS setup, utilizing textual labels and the potentially available 2D image modality.
- **p. 1 / ABSTRACT - extractive body cue:** Under this easy-to-achieve setup, we present the MultiModal Few-Shot SegNet (MM-FSS), a model effectively harnessing complementary information from multiple modalities.
- **p. 1 / ABSTRACT - extractive body cue:** MM-FSS employs a shared backbone with two heads to extract intermodal and unimodal visual features, and a pretrained text encoder to generate text embeddings.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To address this challenge, few-shot 3D point cloud semantic segmentation (FS-PCS) has recently attracted increasing attention, enabling models to generalize to unseen/novel categories with just ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Existing FS-PCS methods (Zhao et al., 2021; Xu et al., 2023; Zhu et al., 2023; Mao et al., 2022; Wang et al., 2023; Zhang et ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Under this cost-free multimodal FS-PCS setup, we introduce a novel model, MultiModal Few-Shot SegNet (MM-FSS), to effectively address FS-PCS by harnessing complementary information from different ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (ii) We introduce a novel model, MM-FSS, to effectively exploit information from different modalities, which includes multimodal correlation fusion, multimodal semantic fusion, and test-time adaptive ...
- **p. 6 / 3 METHODOLOGY - extractive body cue:** To this end, we propose two novel modules for cross-modal knowledge fusion: MCF and MSF.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Additionally, we propose a simple yet effective Test-time Adaptive Cross-modal Calibration (TACC) technique to mitigate training bias inherent in few-shot models (Cheng et al., 2022).
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Different from the existing setup, we propose a multimodal FS-PCS setup where two additional modalities exist: the textual modality and the 2D image modality.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** To utilize the potentially available 2D modality, we propose to use the visual encoder of LSeg to generate 2D visual features, which exhibit excellent generalizability ...
- **p. 7 / 3 METHODOLOGY - extractive body cue:** (5) Then, our MSF module consists of K MSF blocks, with the correlation input to the current block denoted as Ck (k ∈{0, 1, · ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** Both intermodal and unimodal features are then forwarded to the Multimodal Correlation Fusion (MCF) module to produce multimodal correlations between support and query point clouds.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our method processes point cloud inputs through a joint backbone and two distinct heads of IF and UF, as depicted in Fig. | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3 METHODOLOGY), p. 1 (1 INTRODUCTION) |
| State/latent | processes, point, cloud, inputs, through, joint, backbone, distinct, heads, depicted, Fig, However | geometry, map, object/relationship state | p. 5 (3 METHODOLOGY), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/action | However, these methods predominantly focus on unimodal point cloud inputs, overlooking the potential benefits of leveraging multimodal information. | point map, pose, scene graph, affordance 또는 query result | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective/outcome | (2023), we employ a cosine similarity loss to minimize the distance between 3D point intermodal features and corresponding 2D pixel features (see Appendix B). | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3 METHODOLOGY), p. 7 (3 METHODOLOGY), p. 17 (B ADDITIONAL IMPLEMENTATION DETAILS) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Under this cost-free multimodal FS-PCS setup, we introduce a novel model, MultiModal Few-Shot SegNet (MM-FSS), to effectively address FS-PCS by harnessing complementary information from different ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (ii) We introduce a novel model, MM-FSS, to effectively exploit information from different modalities, which includes multimodal correlation fusion, multimodal semantic fusion, and test-time adaptive ...
- **p. 6 / 3 METHODOLOGY - extractive body cue:** To this end, we propose two novel modules for cross-modal knowledge fusion: MCF and MSF.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Additionally, we propose a simple yet effective Test-time Adaptive Cross-modal Calibration (TACC) technique to mitigate training bias inherent in few-shot models (Cheng et al., 2022).
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Different from the existing setup, we propose a multimodal FS-PCS setup where two additional modalities exist: the textual modality and the 2D image modality.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative comparison of predictions from each head and our final prediction using TACC (Default) in the 1-way 1-shot setting on the S3DIS dataset. ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Despite leveraging the 2D-aligned backbone weights, COSeg† does not significantly improve over COSeg, highlighting the critical role of well-designed fusion modules in achieving significant advancements.
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** 3d shows that adding the image modality improves the 3D-only baseline, and further incorporating the textual modality leads to better results.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 8 (4 EXPERIMENTS) |
| Embodiment/environment | (2021), we divide the large-scale scenes into 1m × 1m blocks. | hardware/simulator version and reset protocol | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Dataset/benchmark | Similarly, it achieves +4.53% and +8.58% improvements on the S3DIS dataset in the 1/2-way settings, respectively. | role, split, size and leakage | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Metric | This performance gap underscores our model's superior ability to utilize multimodal knowledge for FS-PCS and the importance of considering commonly-ignored multimodal information to enhance few-shot generalization for future research. | definition, denominator, direction and uncertainty | p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Baseline/ablation | In contrast, MM-FSS consistently outperforms the former state-of-the-art across all settings, demonstrating superior cross-modal knowledge integration to enhance novel class segmentation. | fair input/data/compute/action matching | p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Using only Gq (1:0) yields the lowest performance due to the IF head's limitations in utilizing support samples for learning novel classes.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Despite leveraging the 2D-aligned backbone weights, COSeg† does not significantly improve over COSeg, highlighting the critical role of well-designed fusion modules in achieving significant advancements.
- **p. 17 / B ADDITIONAL IMPLEMENTATION DETAILS - extractive body cue:** In the first step, we concentrate on training the IF head to learn robust 3D features aligned with 2D modality, providing a solid foundation for ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To address this challenge, few-shot 3D point cloud semantic segmentation (FS-PCS) has recently attracted increasing attention, enabling models to generalize to unseen/novel categories with just a few annotated samples.를 문제로 두고, Under this cost-free multimodal FS-PCS setup, we introduce a novel model, MultiModal Few-Shot SegNet (MM-FSS), to effectively address FS-PCS by harnessing complementary information from different modalities.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (3 METHODOLOGY), p. 7 (3 METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
