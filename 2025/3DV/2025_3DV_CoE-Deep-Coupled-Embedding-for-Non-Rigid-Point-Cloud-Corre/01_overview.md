# CoE: Deep Coupled Embedding for Non-Rigid Point Cloud Correspondences

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/3dv66043.2025.00031.
> PDF retrieval source: https://openreview.net/attachment?id=pIDl4wuZoG&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: Huajian Zeng, Maolin Gao, Daniel Cremers
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: point cloud, 3D Vision
- Official paper: https://api.crossref.org/works/10.1109/3dv66043.2025.00031
- Full-text retrieval: https://arxiv.org/pdf/2412.05557.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125562)

## Why This Paper Is Here

CoE는 비강체 변형이 있는 두 점군을 공통 임베딩 공간으로 옮겨 점별 최근접 이웃으로 조밀한 대응을 구한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125562#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125562#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The interest in matching non-rigidly deformed shapes represented as raw point clouds is rising due to the proliferation of low-cost 3D sensors.
- **p. 1 / Abstract - extractive body cue:** Yet, the task is challenging since point clouds are irregular and there is a lack of intrinsic shape information.
- **p. 1 / Abstract - extractive body cue:** We propose to tackle these challenges by learning a new shape representation - a per-point high dimensional embedding, in an embedding space where semantically similar ...
- **p. 1 / Abstract - extractive body cue:** The learned embedding has multiple beneficial properties: it is aware of the underlying shape geometry and is robust to shape deformations and various shape artefacts, ...
- **p. 1 / Abstract - extractive body cue:** Consequently, this embedding can be directly employed to retrieve high-quality dense correspondences through a simple nearest neighbor search in the embedding space.
- **p. 4 / 3. Background and Notation - extractive body cue:** (1), this modification greatly reduced the computational complexity, however it still involves difficult manifold optimisation for only approximately solving the original one.
- **p. 1 / 1. Introduction - extractive body cue:** Most of them are designed for shapes represented as triangular meshes and cannot be extended to point clouds without performance degradation [7, 21, 28].

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • We propose a novel unsupervised way to learn per-point embeddings directly from raw point clouds under various non-rigid deformations.
- **p. 2 / 1. Introduction - extractive body cue:** Inspired by classical geometry processing technique, our method is effective and simple that only requires to train a single network. • In our learned embedding ...
- **p. 4 / 3. Background and Notation - extractive body cue:** To overcome these issues, we propose to directly learn coupled embeddings without any ground truth correspondences and without any subspace parameterisation.
- **p. 5 / 4.2. Unsupervised Loss - extractive body cue:** Our unsupervised loss is inspired by the work of classical geometry processing [16, 22] and consists of three terms.
- **p. 5 / 4.2. Unsupervised Loss - extractive body cue:** To our best knowledge, this enables, for the first time, the practical application
- **p. 4 / 4.1. Network Architecture - extractive body cue:** Our network architecture is simple, efficient and comprises two main building blocks: an embedding extractor fθ and a cross attention module hφ with learnable parameters ...
- **p. 5 / 4.1. Network Architecture - extractive body cue:** It follows the Transformer architecture [51] and learns a non-linear mapping: hφ : { ˆΨS, ˆΨT } →{ΨS, ΨT } (3) The output ΨS and ...
- **p. 4 / 4.1. Network Architecture - extractive body cue:** Embedding Extractor Module computes per point intermediate embedding ˆΨ(·), which is a non-linear mapping:

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | All methods only take point clouds as input except the multimodal method SSMSM [7], which requires meshes. | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (4.2. Unsupervised Loss), p. 2 (1. Introduction) |
| State/latent | methods, only, take, point, clouds, input, except, multimodal, SSMSM, requires, meshes, Due | geometry, map, object/relationship state | p. 6 (4.2. Unsupervised Loss), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | Due to insights gained from the classical geometry processing, we can obtain high-quality dense correspondences directly via a simple proximity search in the embedding space by training a single network, while all ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | Orthogonal Loss: The orthogonal constraint in Eq. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4.2. Unsupervised Loss), p. 5 (4.2. Unsupervised Loss), p. 6 (4.2. Unsupervised Loss) |

## Main Claims and Actual Contribution

- 형상의 기하를 반영하는 점별 특징을 쌍으로 학습해 원점군에 메시 연결이나 수작업 대응점이 없는 경우를 다룬다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125562#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125562#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125562#page=5)
- 비강체 형상 정합에서 대응 오차를 측정하고 잡음·부분 관측을 넣었을 때의 견고성을 비교했다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125562#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125562#page=7) · [PDF 8쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125562#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (5.7. Shape Segmentation), p. 7 (5.3. Non-isometric Shape Matching) |
| Embodiment/environment | Datasets We employ the recent non-isometric benchmark DT4D-M [27] as the testbed for this task. | hardware/simulator version and reset protocol | p. 7 (5.3. Non-isometric Shape Matching), p. 7 (5.2. Near-isometric Shape Matching) |
| Dataset/benchmark | Datasets We choose FAUST [6], SCAPE [1] and SHREC19 [29] as testbeds for the task of near-isometric shape matching, specifically the more recent remeshed version [13, 35] of them. | role, split, size and leakage | p. 7 (5.3. Non-isometric Shape Matching), p. 7 (5.2. Near-isometric Shape Matching), p. 6 (5.2. Near-isometric Shape Matching), p. 8 (5.5. Robustness) |
| Metric | Note that the mean geodesic error deteriorates in all cases, underlining the importance of smoothness of learned embeddings. | definition, denominator, direction and uncertainty | p. 7 (5.2. Near-isometric Shape Matching), p. 7 (5.2. Near-isometric Shape Matching), p. 8 (5.5. Robustness) |
| Baseline/ablation | Our method outperforms all learning based baselines. | fair input/data/compute/action matching | p. 7 (5.3. Non-isometric Shape Matching), p. 7 (5.4. Generalisation), p. 8 (5.5. Robustness) |

## Explicit Limitations and Failure Boundary

- **p. 15 / Figure/Table caption - extractive body cue:** Figure 16. Qualitative results on DT4D-M. More qualitative non-isometric matching results (top) . Failure cases mainly due to challenging topological noise (bottom) .
- **p. 8 / 5.7. Shape Segmentation - extractive body cue:** Limitations, Future Work and Conclusion In this paper, we proposed an unsupervised method to learn high-quality, well-generalised embeddings directly from raw point clouds.
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 13. Failure cases on FAUST. All three failure examples relate to the touching hands, where the points of two hands are locally mixed and ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 7. Visualisation of a challenging pair with crossed legs. We show our full design can successfully handle this challenge while all baseline methods fails ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 10. Illustration of mean geodesic error under different spec- tral resolutions. Our method is robust for different choice of spec- tral resolution. We conduct ...
- **p. 7 / 5.5. Robustness - extractive body cue:** We evaluate robustness from two perspectives: (1) random additive Gaussian noise to point clouds, (2) changes and inconsistency in shape topology.
- **p. 8 / 5.5. Robustness - extractive body cue:** Compared to the noise-free case, we also have the least overall performance degradation.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 4 (3. Background and Notation), p. 1 (1. Introduction), p. 3 (3. Background and Notation), p. 4 (4.1. Network Architecture), p. 5 (4.1. Network Architecture)이다.
