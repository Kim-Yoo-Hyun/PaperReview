# Semantically Consistent Language Gaussian Splatting for 3D Point-Level Open-Vocabulary Querying

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html.
> PDF retrieval source: https://arxiv.org/pdf/2503.21767. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Gaussian Splatting, semantic
- Official paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html
- Full-text retrieval: https://arxiv.org/pdf/2503.21767
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To mitigate this difficulty, we propose a novel Ground-Truth Anchored (GT-Anchored) querying method, which computes the threshold relative to, "anchored", ground-truth (GT) used in the distillation process instead of directly with the ...를 문제로 두고, Our contributions are as follows: • We introduce tracking for generating semantic and 3 를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary 3D scene understanding is crucial for robotics applications, such as natural language-driven manipulation, human-robot interaction, and autonomous navigation.
- **p. 1 / Abstract - extractive body cue:** Existing methods for querying 3D Gaussian Splatting often struggle with inconsistent 2D mask supervision and lack a robust 3D point-level retrieval mechanism.
- **p. 1 / Abstract - extractive body cue:** In this work, (i) we present a novel point-level querying framework that performs tracking on segmentation masks to establish a semantically consistent groundtruth for distilling ...
- **p. 1 / Abstract - extractive body cue:** Extensive experiments on three benchmark datasets demonstrate that the proposed method outperforms state-of-the-art performance.
- **p. 1 / Abstract - extractive body cue:** Our method achieves an mIoU improvement of +4.14, +20.42, and +1.7 on the LERF, 3D-OVS, and Replica datasets.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To mitigate this difficulty, we propose a novel Ground-Truth Anchored (GT-Anchored) querying method, which computes the threshold relative to, "anchored", ground-truth (GT) used in the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We observe that it does not have a consistent optimal threshold for all queries. consistent ground-truth to train language-aware Gaussians, which improves the distillation quality. ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our contributions are as follows: • We introduce tracking for generating semantic and 3D.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We observe that it does not have a consistent optimal threshold for all queries. consistent ground-truth to train language-aware Gaussians, which improves the distillation quality. ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To mitigate this difficulty, we propose a novel Ground-Truth Anchored (GT-Anchored) querying method, which computes the threshold relative to, "anchored", ground-truth (GT) used in the ...
- **p. 4 / IV. METHOD - extractive body cue:** Differently, we propose a novel method for constructing ground-truths that are more semantically consistent and robust across various 3D viewpoints (Sec.
- **p. 4 / IV. METHOD - extractive body cue:** Furthermore, the weighting scheme helps to suppress the contribution of small regions that often contain noisier language embeddings, i.e., we consider the reliability of individual ...
- **p. 4 / IV. METHOD - extractive body cue:** This is done by masking out the image It using the extracted masklet and then passing it to CLIP's image encoder: ¯ϕr = T X ...
- **p. 5 / IV. METHOD - extractive body cue:** Given the CLIP feature of a text query q ∈R512, we first apply a low threshold to filter out invalid prompts.
- **p. 5 / IV. METHOD - extractive body cue:** We then retrieve the most similar average feature (GT for distillation) over all regions feature ¯ϕ∗ r ≜ arg max r∈{r′/Cos( ¯ϕ′r,q)≥threshold} Cos(¯ϕr, q).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | III, a tracking module takes a sequence of images and regions of interest as input to track masks of the same region. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (IV. METHOD), p. 4 (IV. METHOD) |
| State/latent | III, tracking, module, takes, sequence, images, regions, interest, input, track, masks, same | geometry, map, object/relationship state | p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 2 (III. PRELIMINARIES) |
| Output/action | If the proposed region has not been tracked, we run the tracking model and add the output masklets to the set of tracked masklets ˜S1:T . | point map, pose, scene graph, affordance 또는 query result | p. 4 (IV. METHOD), p. 2 (III. PRELIMINARIES), p. 1 (I. INTRODUCTION) |
| Objective/outcome | IT ] with camera poses, we aim to construct a better ground-truth feature LOurs t for each of the frames to train LangSplat's parameters by minimizing the objective function in Eq. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (IV. METHOD), p. 5 (IV. METHOD) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our contributions are as follows: • We introduce tracking for generating semantic and 3D.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We observe that it does not have a consistent optimal threshold for all queries. consistent ground-truth to train language-aware Gaussians, which improves the distillation quality. ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To mitigate this difficulty, we propose a novel Ground-Truth Anchored (GT-Anchored) querying method, which computes the threshold relative to, "anchored", ground-truth (GT) used in the ...
- **p. 4 / IV. METHOD - extractive body cue:** Differently, we propose a novel method for constructing ground-truths that are more semantically consistent and robust across various 3D viewpoints (Sec.
- **p. 4 / IV. METHOD - extractive body cue:** Furthermore, the weighting scheme helps to suppress the contribution of small regions that often contain noisier language embeddings, i.e., we consider the reliability of individual ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** We observe that Ours consistently outperforms LangSplat-m and, on average, is better than OpenGaussian, achieving an improvement of +4.14 in mIoU and +10.66 in mAcc.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Acc, significantly outperforming baseline methods.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We also see that our proposed GT-anchored query significantly outperforms the canonical query.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Embodiment/environment | Following LangSplat [23], we conduct experiments on the further annotated LERF [12] dataset that contains a set of in-the-wild scenes and on the 3D-OVS [18] dataset, which includes a collection of long-tail ... | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Dataset/benchmark | 6: Qualitative results on 3D-OVS dataset for scene "lawn". | role, split, size and leakage | p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Metric | We also report mIoU accuracy (mAcc↑), a 2D metric proposed by OpenGaussian [29], where a query is considered correct if its IoU is greater than 0.25. | definition, denominator, direction and uncertainty | p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Baseline/ablation | Acc, significantly outperforming baseline methods. | fair input/data/compute/action matching | p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / V. EXPERIMENTS - extractive body cue:** Note that all four methods encounter a common failure mode of empty query, i.e., no valid Gaussians are returned for a text query, resulting in ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Acc, a query is considered correct if the center of the queried mask's exterior bounding box falls within the bounding box of the ground-truth.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: IoU metric per query vs. cosine similarity thresholds for the standard querying method. We observe that it does not have a consistent optimal ...
- **p. 5 / IV. METHOD - extractive body cue:** (11) As ¯ϕr is obtained as a weighted average of CLIP image embeddings and q comes from CLIP text embeddings, a direct comparison between them ...
- **p. 5 / IV. METHOD - extractive body cue:** Therefore, any high threshold works well, which improves the queries' reliability and robustness.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We observe that LangSplat-m and GaussianGrouping-m failed to retrieve the correct object, and OpenGaussian only retrieves part of the cloth with noisy points from other ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To mitigate this difficulty, we propose a novel Ground-Truth Anchored (GT-Anchored) querying method, which computes the threshold relative to, "anchored", ground-truth (GT) used in the distillation process instead of directly with the ...를 문제로 두고, Our contributions are as follows: • We introduce tracking for generating semantic and 3 를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
