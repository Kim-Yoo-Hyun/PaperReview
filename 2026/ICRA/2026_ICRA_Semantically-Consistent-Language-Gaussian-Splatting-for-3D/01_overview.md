# Semantically Consistent Language Gaussian Splatting for 3D Point-Level Open-Vocabulary Querying

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/icra57385.2026.11697173.
> PDF retrieval source: https://arxiv.org/pdf/2503.21767. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: Hairong Yin, Huangying Zhan, Yi Xu, Raymond A. Yeh
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Gaussian Splatting, semantic
- Official paper: https://api.crossref.org/works/10.1109/icra57385.2026.11697173
- Full-text retrieval: https://arxiv.org/pdf/2503.21767
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11697173)
- 저자판 표제: Semantic Consistent Language Gaussian Splatting for Point-Level Open-vocabulary Querying. 게재본에서는 첫 단어가 Semantically로 바뀌고 Point-Level 앞에 3D가 추가됐다. [저자판 v2](https://arxiv.org/abs/2503.21767v2) · [게재 서지](https://api.crossref.org/works/10.1109/icra57385.2026.11697173)

## Why This Paper Is Here

이 연구는 여러 뷰에 나타난 동일 물체의 마스크를 추적해 언어 특징을 가우시안에 증류하고, 텍스트로 개별 3D 점을 검색한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11697173#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11697173#page=3)

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

- 마스크 추적으로 만든 참조 임베딩에 먼저 질의한 뒤 대응하는 가우시안을 찾아 뷰마다 달라지는 2D 감독 신호의 영향을 줄인다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11697173#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11697173#page=4)
- LERF, 3D-OVS, Replica에서 개방 어휘 분할을 평가하고 참조 임베딩을 경유하는 검색을 직접 질의 방식과 비교했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11697173#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11697173#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11697173#page=7)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (IV. METHOD), p. 5 (IV. METHOD)이다.
