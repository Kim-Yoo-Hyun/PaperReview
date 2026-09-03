# OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Chow_OV-SCAN_Semantically_Consistent_Alignment_for_Novel_Object_Discovery_in_Open-Vocabulary_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Chow_OV-SCAN_Semantically_Consistent_Alignment_for_Novel_Object_Discovery_in_Open-Vocabulary_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, semantic
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Chow_OV-SCAN_Semantically_Consistent_Alignment_for_Novel_Object_Discovery_in_Open-Vocabulary_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Chow_OV-SCAN_Semantically_Consistent_Alignment_for_Novel_Object_Discovery_in_Open-Vocabulary_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Due to the aforementioned challenges with online methods, recent work has increasingly shifted toward offline approaches.를 문제로 두고, We summarize our main contributions as follows: • We present OV-SCAN, an OV-3D object detector benefiting from improved cross-modal alignment, see Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary 3D object detection for autonomous driving aims to detect novel objects beyond the predefined training label sets in point cloud scenes.
- **p. 1 / Abstract - extractive body cue:** Existing approaches achieve this by connecting traditional 3D object detectors with vision-language models (VLMs) to regress 3D bounding boxes for novel objects and perform open-vocabulary ...
- **p. 1 / Abstract - extractive body cue:** However, achieving robust cross-modal alignment remains a challenge due to semantic inconsistencies when generating corresponding 3D and 2D feature pairs.
- **p. 1 / Abstract - extractive body cue:** To overcome this challenge, we present OV-SCAN, an Open-Vocabulary 3D framework that enforces Semantically Consistent Alignment for Novel object discovery.
- **p. 1 / Abstract - extractive body cue:** OVSCAN employs two core strategies: discovering precise 3D annotations and filtering out low-quality or corrupted alignment pairs (arising from 3D annotation, occlusioninduced, or resolution-induced noise).
- **p. 1 / 1. Introduction - extractive body cue:** Due to the aforementioned challenges with online methods, recent work has increasingly shifted toward offline approaches.
- **p. 1 / 1. Introduction - extractive body cue:** OV-3D object detection faces two main challenges: (1) novel object discovery (NOD), which involves generating 3D labels for novel objects in order to train an ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We summarize our main contributions as follows: • We present OV-SCAN, an OV-3D object detector benefiting from improved cross-modal alignment, see Fig.
- **p. 2 / 1. Introduction - extractive body cue:** More specifically, we introduce the Semantically-Consistent Novel-Object Discovery (SCNOD) module to handle the inherent challenges of noisy cross-modal alignment.
- **p. 4 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** Our method relies on CLIP to classify the object into its corresponding novel class c.
- **p. 3 / 3. Method - extractive body cue:** In this section, we present the details of OV-SCAN.
- **p. 3 / 3.1. Notation and Preliminaries - extractive body cue:** Our method extends the traditional target pair of 3D bounding box and class label, into a triplet target denoted by !→= {(Bi, ci, A2D,i)}N i=1.
- **p. 4 / 3.1. Notation and Preliminaries - extractive body cue:** Cross-Modal Target Preparation 2D Image Features 3D Annotations CLIP Image Encoder Adaptive 3D Box Search Predicted Objects Selective Alignment Filter CLIP Image Encoder Adaptive 3D ...
- **p. 3 / 3.1. Notation and Preliminaries - extractive body cue:** These alignment features are then used for prompt-based classification by comparing them with text embeddings generated from class prompts, enabling fine-grained recognition of novel objects.
- **p. 5 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** The continuous nonlinear optimization problem is then formulated in standard form: min ω J (ω, Pobj, e, bimg) = J3D(ω, Pobj, e) + J2D(ω, bimg) ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In addition, the proposed H2SA head effectively aligns 3D-to-2D alignment pairs by introducing a two-stage alignment process. • We validate OV-SCAN on the nuScenes [2] and KITTI [12] datasets, demonstrating that OV-SCAN ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 3 (3.1. Notation and Preliminaries) |
| State/latent | addition, H2SA, head, effectively, aligns, D-to-2D, alignment, pairs, introducing, two-stage, process, validate | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 3 (3.1. Notation and Preliminaries), p. 3 (3.1. Notation and Preliminaries) |
| Output/action | In traditional LiDAR-based 3D object detection, the objective is to train a detector using inputtarget pairs D = {P, !}. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Notation and Preliminaries), p. 3 (3.1. Notation and Preliminaries), p. 4 (3.1. Notation and Preliminaries) |
| Objective/outcome | (7) The optimization is governed by a cost function that balances multiple objectives. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 4 (3.2. Semantically Consistent NOD (SC-NOD)) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We summarize our main contributions as follows: • We present OV-SCAN, an OV-3D object detector benefiting from improved cross-modal alignment, see Fig.
- **p. 2 / 1. Introduction - extractive body cue:** More specifically, we introduce the Semantically-Consistent Novel-Object Discovery (SCNOD) module to handle the inherent challenges of noisy cross-modal alignment.
- **p. 4 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** Our method relies on CLIP to classify the object into its corresponding novel class c.
- **p. 3 / 3. Method - extractive body cue:** In this section, we present the details of OV-SCAN.
- **p. 3 / 3.1. Notation and Preliminaries - extractive body cue:** Our method extends the traditional target pair of 3D bounding box and class label, into a triplet target denoted by !→= {(Bi, ci, A2D,i)}N i=1.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** A simple occlusion filter with a fixed threshold ςocc yields a notable performance gain, while class-based thresholds achieve the highest improvement (+1.7 mAP).
- **p. 7 / 4.2. Main Results - extractive body cue:** Without being given 3D human-annotations, OV-SCAN achieves an AP score above 60 for both car and pedestrian categories.
- **p. 7 / 4.2. Main Results - extractive body cue:** Furthermore, we show that simply adding camera as an additional input modality to OV-SCAN and then fine-tuning can improve the overall performance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4.3. Ablation Studies), p. 7 (4.2. Main Results) |
| Embodiment/environment | Our OV-3D object detection experiments are conducted on the nuScenes [2] and KITTI [12] datasets. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Main Results) |
| Dataset/benchmark | SC-NOD generates 319,028 3D annotations for training, a fraction of the 797,179 available in the nuScenes dataset. | role, split, size and leakage | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Main Results), p. 7 (4.2. Main Results), p. 8 (4.3. Ablation Studies) |
| Metric | Figure 3. Sources of Semantic Discrepancies. (a) CLIP sim- ilarity scores for a truck reveal that occlusion cases result in an ambiguous 2D image feature. (b) CLIP similarity scores for a dis- ... | definition, denominator, direction and uncertainty | p. 2 (Figure/Table caption), p. 7 (4.1. Experimental Setup), p. 7 (4.2. Main Results) |
| Baseline/ablation | OV-SCAN outperforms OV-3DET [25] and ImOV3D [42] in the overall metric, achieving comparable results to ImOV3D [42] in the car category while surpassing both in the other two classes. | fair input/data/compute/action matching | p. 7 (4.2. Main Results), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.4. Limitations - extractive body cue:** The primary limitation of SC-NOD is its limited annotation recovery (Fig.
- **p. 8 / 4.4. Limitations - extractive body cue:** These insights motivate future work exploring alternative methods less dependent on 2D proposals and anchor-free box-parameterization strategies.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. 3D Annotation Errors. Common 3D annotation errors during box parametrization, including but not limited to, poor L- shape fitting, misinterpreted surfaces, and misaligned ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 3. Sources of Semantic Discrepancies. (a) CLIP sim- ilarity scores for a truck reveal that occlusion cases result in an ambiguous 2D image feature. ...
- **p. 7 / 4.2. Main Results - extractive body cue:** The remainder of generated annotations are excluded as a result of filtering due to significant occlusion (39%) or insufficient resolution (7%).
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** (a) 3D Box Search Cost Weights (b) Resolution Filter (ω1, ω2, ω3, ε) mAP Filter mAP (5.0, 0.0, 0.0, 3.0) 26.1 w/o 30.4 (1.0, 1.0, ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Due to the aforementioned challenges with online methods, recent work has increasingly shifted toward offline approaches.를 문제로 두고, We summarize our main contributions as follows: • We present OV-SCAN, an OV-3D object detector benefiting from improved cross-modal alignment, see Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Notation and Preliminaries), p. 3 (3.1. Notation and Preliminaries) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
