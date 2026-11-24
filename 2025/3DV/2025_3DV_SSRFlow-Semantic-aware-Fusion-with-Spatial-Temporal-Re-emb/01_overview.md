# SSRFlow: Semantic-aware Fusion with Spatial Temporal Re-embedding for Real-world Scene Flow

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/3dv66043.2025.00032.
> PDF retrieval source: https://openreview.net/attachment?id=9abfUtE6iQ&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: Zhiyang Lu, Qinghan Chen, Zhimin Yuan, Chenglu Wen, Ming Cheng, Cheng Wang
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Official paper: https://api.crossref.org/works/10.1109/3dv66043.2025.00032
- Full-text retrieval: https://arxiv.org/pdf/2408.07825.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125601)

## Why This Paper Is Here

SSRFlow는 합성 점군으로 학습한 장면 흐름을 실제 LiDAR로 전이하기 위해 두 프레임의 특징을 의미와 시공간 기하로 정렬한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125601#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125601#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Scene flow, which provides the 3D motion field of the first frame from two consecutive point clouds, is vital for dynamic scene perception.
- **p. 1 / Abstract - extractive body cue:** However, contemporary scene flow methods face three major challenges.
- **p. 1 / Abstract - extractive body cue:** Firstly, they lack global flow embedding or only consider the context of individual point clouds before embedding, leading to embedded points struggling to perceive the ...
- **p. 1 / Abstract - extractive body cue:** To address this issue, we propose a novel approach called Dual Cross Attentive (DCA) for the latent fusion and alignment between two frames based on ...
- **p. 1 / Abstract - extractive body cue:** This is then integrated into Global Fusion Flow Embedding (GF) to initialize flow embedding based on global correlations in both contextual and Euclidean spaces.
- **p. 2 / 1 Introduction - extractive body cue:** Overall, our contributions are as follows: • Our GF module leverages the dual cross-attentive mechanism to fuse and align the semantic context from both frames ...
- **p. 2 / 1 Introduction - extractive body cue:** Furthermore, as a point-level task, obtaining the ground truth (GT) of scene flow from real-world point clouds is difficultMenze et al.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Overall, our contributions are as follows: • Our GF module leverages the dual cross-attentive mechanism to fuse and align the semantic context from both frames ...
- **p. 2 / 1 Introduction - extractive body cue:** (2023), we introduce the Dual Cross Attentive (DCA) Fusion to merge the semantic contexts of point clouds from two frames in latent space, which allows ...
- **p. 3 / 2 Methodology - extractive body cue:** 2.3 Global Fusion Flow Embedding The GF module is designed to capture the global relation between consecutive frames during the flow initialization.
- **p. 4 / 2 Methodology - extractive body cue:** The obtained coarse dense flow is directly accumulated onto the source frame Sl to generate the warped source frame WSl = {wsi}Nl i=1 = {wxi ...
- **p. 3 / 2 Methodology - extractive body cue:** (2019) as the feature extraction backbone to build a pyramid network.
- **p. 3 / 2 Methodology - extractive body cue:** 2.2 Hierarchical Feature Extraction The overview of our proposed network is shown in Figure 1.
- **p. 4 / 2 Methodology - extractive body cue:** During the dual cross-attentive fusion phase, the semantic context in the latent feature space is obtained for S∗and T ∗through linear networks Q K and ...
- **p. 6 / 2 Methodology - extractive body cue:** Cross-frame Feature Similarity (CFS) Loss The semantic features of the points in the warped source frame are similar to those in the surrounding target frame, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2.2 Hierarchical Feature Extraction The overview of our proposed network is shown in Figure 1. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (2 Methodology), p. 2 (1 Introduction) |
| State/latent | Hierarchical, Feature, Extraction, overview, network, Figure, rely, stereo, RGB-D, images, input, backbone | geometry, map, object/relationship state | p. 3 (2 Methodology), p. 2 (1 Introduction), p. 3 (2 Methodology) |
| Output/action | (2008) rely on stereo or RGB-D images as input. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 Introduction), p. 3 (2 Methodology), p. 4 (2 Methodology) |
| Objective/outcome | 3 Training Losses 3.1 Hierarchical Supervised Loss A supervised loss is directly hooked to the GT of scene flow, and we leverage multi-level loss functions as supervision to optimize the model across ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (2 Methodology), p. 6 (2 Methodology), p. 5 (2 Methodology) |

## Main Claims and Actual Contribution

- 이중 교차 어텐션으로 두 프레임의 의미 정보를 교환하고 시공간 위치를 다시 부호화해 대응 특징을 만든다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125601#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125601#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125601#page=5)
- 도메인 적응 손실을 이용하고 합성 자료에서 실제 점군으로 옮긴 조건의 흐름 오차를 비교했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125601#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125601#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125601#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 8 (4 Experiments) |
| Embodiment/environment | (a) FT3Ds (b) KITTIs (c) SF-KITTI (d) LiDAR-KITTI Figure 4: Comparisons of scene flow datasets, including (a) synthetic stereo, (b) real-world stereo, and (c)(d) real-world LiDAR-scanned. | hardware/simulator version and reset protocol | p. 7 (4 Experiments), p. 6 (4 Experiments) |
| Dataset/benchmark | The quantitative results presented in Table 1 indicate that SSRFlow outperforms the other methods by a large margin, especially in real-world datasets. | role, split, size and leakage | p. 7 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Metric | After removing the DCA Fusion, the model experienced a substantial decline in accuracy, primarily due to its capability to fuse point features with another frame context before embedding. | definition, denominator, direction and uncertainty | p. 9 (4 Experiments), p. 14 (Figure/Table caption), p. 7 (4 Experiments) |
| Baseline/ablation | Figure 6: Illustration of results on other datasets of our proposed SSRFlow method. Colors mean the same as Figure 5. More visualization results are exhibited in Appendix, Sec F FT3Do and KITTIo ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 9 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 2 Methodology - extractive body cue:** The KNN+Radius search strategy effectively mitigates the influence of noise points resulting from occlusion and sparsity in point clouds, as demonstrated in Sec B.2 of ...
- **p. 8 / 4 Experiments - extractive body cue:** The experimental results are listed in Table 3, which reveal the good performance of our model even with occlusion.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 10: Ablation studies and analysis of adaption losses. From Figure 9 it can be observed that using only KNN introduces noise points that do ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 11: (a) The occlusion occurs between the source frame and the target frame. In this scenario, red bounding boxes delineate points in the source ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (2 Methodology), p. 4 (2 Methodology), p. 6 (2 Methodology)이다.
