# LE-Object: Language Embedded Object-Level Neural Radiance Fields for Open-Vocabulary Scene

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf.
> PDF retrieval source: https://arxiv.org/pdf/2406.08009v1. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic
- Official paper: https://www.proceedings.com/content/081/081087webtoc.pdf
- Full-text retrieval: https://arxiv.org/pdf/2406.08009v1
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To address this limitation, some works [11], [12] have proposed instance-oriented open-vocabulary mapping methods.를 문제로 두고, In summary, Our contributions are summarized as follows: • We present OpenObj, the open-vocabulary object-level neural radiance fields with fine-grained understanding, supporting downstream tasks at multiple scales. • We propose a two-s ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In recent years, there has been a surge of interest in open-vocabulary 3D scene reconstruction facilitated by visual language models (VLMs), which showcase remarkable capabilities ...
- **p. 1 / Abstract - extractive body cue:** However, existing methods face some limitations: they either focus on learning point-wise features, resulting in blurry semantic understanding, or solely tackle object-level reconstruction, thereby overlooking ...
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce OpenObj, an innovative approach to build openvocabulary object-level Neural Radiance Fields (NeRF) with fine-grained understanding.
- **p. 1 / Abstract - extractive body cue:** In essence, OpenObj establishes a robust framework for efficient and watertight scene modeling and comprehension at the object-level.
- **p. 1 / Abstract - extractive body cue:** Moreover, we incorporate part-level features into the neural fields, enabling a nuanced representation of object interiors.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address this limitation, some works [11], [12] have proposed instance-oriented open-vocabulary mapping methods.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these semantics are limited to a closed-set of labels predefined during the training phase [3], making it challenging to generalize to new scenes or ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, Our contributions are summarized as follows: • We present OpenObj, the open-vocabulary object-level neural radiance fields with fine-grained understanding, supporting downstream tasks at ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Following this inspiration, we proposed OpenObj, an innovative approach to build open-vocabulary objectlevel neural radiance fields with fine-grained understanding.
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce OpenObj, an innovative approach to build openvocabulary object-level Neural Radiance Fields (NeRF) with fine-grained understanding.
- **p. 4 / III. OPENOBJ - extractive body cue:** To address this problem, we propose considering all frames together and devising a two-stage approach as shown in Fig.
- **p. 3 / III. OPENOBJ - extractive body cue:** In this paper, we use the visual encoder of CLIP [4] to encode images cropped according to the mask mobj t,i as VLM feature f ...
- **p. 5 / III. OPENOBJ - extractive body cue:** Next, we superimpose the features of these masks mpart t,j and perform normalization: If t = P j  mpart t,j · f clip t,j ...
- **p. 3 / III. OPENOBJ - extractive body cue:** Specifically, we use the bounding boxes of the masks mobj t,i as prompts and use the TAP (Tokenize Anything via Prompting) model [29] to generate ...
- **p. 4 / III. OPENOBJ - extractive body cue:** Part-level Fine-Grained Feature Extraction Both of the above modules operate at the instance level and do not perceive the interior details of the object.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Based on this, we can render the occupancy, depth, color, and feature as: ˆO(r[u,v]) = X m Tm, ˆD(r[u,v]) = X m Tmdm ˆC(r[u,v]) = X m Tmcm, ˆF(r[u,v]) = X m ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (III. OPENOBJ), p. 3 (III. OPENOBJ) |
| State/latent | render, occupancy, depth, color, feature, Tmdm, Tmcm, Tmfm, Loss, Function, Supervised, training | geometry, map, object/relationship state | p. 5 (III. OPENOBJ), p. 3 (III. OPENOBJ), p. 3 (III. OPENOBJ) |
| Output/action | Framework Overview OpenObj processes a series of multi-view color images I = {Ic 1, Ic 2, ..., Ic t } and depth images I = {Id 1, Id 2, ..., Id t ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (III. OPENOBJ), p. 3 (III. OPENOBJ), p. 4 (III. OPENOBJ) |
| Objective/outcome | (6d) The overall loss function is obtained by summing the losses of all objects: L = X k (λ1Lk occ + λ2Lk depth + λ3Lk color + λ4Lk feat) (7) F. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (III. OPENOBJ), p. 5 (III. OPENOBJ), p. 3 (III. OPENOBJ) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, Our contributions are summarized as follows: • We present OpenObj, the open-vocabulary object-level neural radiance fields with fine-grained understanding, supporting downstream tasks at ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Following this inspiration, we proposed OpenObj, an innovative approach to build open-vocabulary objectlevel neural radiance fields with fine-grained understanding.
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce OpenObj, an innovative approach to build openvocabulary object-level Neural Radiance Fields (NeRF) with fine-grained understanding.
- **p. 4 / III. OPENOBJ - extractive body cue:** To address this problem, we propose considering all frames together and devising a two-stage approach as shown in Fig.
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** In this section, we aim to use experiments to validate OpenObj, through the following specific questions: 1) Without fine-tuning any model, can OpenObj achieve 2D ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: 2D & 3D zero-shot segmentation results. OpenObj's object-level NeRF and comprehensive understanding enable it to achieve clear boundaries and accurate semantics.
- **p. 4 / III. OPENOBJ - extractive body cue:** In the coarse clustering phase, a graph is constructed for all masks, and the Louvain algorithm is applied to achieve clustering.
- **p. 7 / 2) Are OpenObj's open-vocabulary object-level and part - extractive body cue:** OpenObj consistently outperforms ConceptGraphs across all types of retrieval tasks.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (Figure/Table caption) |
| Embodiment/environment | Datasets and Metrics: The experiments are conducted on four scenes in Replica [32], each featuring a diverse array of objects. | hardware/simulator version and reset protocol | p. 7 (2) Are OpenObj's open-vocabulary object-level and part), p. 6 (2) Are OpenObj's open-vocabulary object-level and part) |
| Dataset/benchmark | In summary, Our contributions are summarized as follows: • We present OpenObj, the open-vocabulary object-level neural radiance fields with fine-grained understanding, supporting downstream tasks at multiple scales. • We propose a two-s ... | role, split, size and leakage | p. 7 (2) Are OpenObj's open-vocabulary object-level and part), p. 6 (2) Are OpenObj's open-vocabulary object-level and part), p. 2 (I. INTRODUCTION), p. 3 (III. OPENOBJ) |
| Metric | For the evaluation metrics, we use mean IoU (mIoU) and mean accuracy (mAcc). | definition, denominator, direction and uncertainty | p. 6 (2) Are OpenObj's open-vocabulary object-level and part), p. 4 (III. OPENOBJ), p. 3 (Figure/Table caption) |
| Baseline/ablation | 2D & 3D Zero-shot Semantic Segmentation Baseline: For 2D semantic segmentation, we compare OpenObj with the language-driven image segmentation method LSeg [31], as well as two state-of-the-art NeRFbased open-vocabulary mapping methods, ... | fair input/data/compute/action matching | p. 6 (2) Are OpenObj's open-vocabulary object-level and part), p. 6 (2) Are OpenObj's open-vocabulary object-level and part), p. 7 (2) Are OpenObj's open-vocabulary object-level and part) |

## Explicit Limitations and Failure Boundary

- **p. 5 / III. OPENOBJ - extractive body cue:** This approach helps to mitigate the effects of outliers caused by poor observation viewpoints or model failures.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We introduce OpenObj, a framework of open-vocabulary object-level neural radiance fields with fine-grained understanding. OpenObj facilitates various downstream tasks, including open-vocabulary object retrieval, ...
- **p. 3 / III. OPENOBJ - extractive body cue:** Additionally, we apply another method to compensate for the limitations of VLM features f clip t,i in semantic reasoning.
- **p. 4 / III. OPENOBJ - extractive body cue:** Since this method does not distinguish between the sources of the masks, it can effectively correlate masks across different frames and within the same frame, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** recognize scenes only at the object level and fail to provide a more granular understanding of internal structures.
- **p. 7 / 2) Are OpenObj's open-vocabulary object-level and part - extractive body cue:** OpenObj correctly and clearly highlights the most relevant instance in each query. more comprehensive and robust understanding of objects.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To address this limitation, some works [11], [12] have proposed instance-oriented open-vocabulary mapping methods.를 문제로 두고, In summary, Our contributions are summarized as follows: • We present OpenObj, the open-vocabulary object-level neural radiance fields with fine-grained understanding, supporting downstream tasks at multiple scales. • We propose a two-s ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. OPENOBJ), p. 5 (III. OPENOBJ), p. 2 (I. INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
