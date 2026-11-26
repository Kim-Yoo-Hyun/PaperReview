# UrbanGS: Efficient and Scalable Architecture for Geometrically Accurate Large-Scene Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/108030643e640ac050e0ed5e6aace48f-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/248058. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Changbai Li, Haodong Zhu, Hanlin Chen, Xiuping Liang, Tongfei Chen, Shuwei Shao, Linlin Yang, Huobin Tan, Baochang Zhang
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, 3D Vision, Gaussian Splatting
- Aliases: UrbanGS: A Scalable and Efficient Architecture for Geometrically Accurate Large-Scene Reconstruction
- 게재 PDF 표제: UrbanGS: A Scalable and Efficient Architecture for Geometrically Accurate Large-Scene Reconstruction [표제면](https://proceedings.iclr.cc/paper_files/paper/2026/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf#page=1) · [학회 서지](https://proceedings.iclr.cc/paper_files/paper/2026/hash/108030643e640ac050e0ed5e6aace48f-Abstract-Conference.html)
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/108030643e640ac050e0ed5e6aace48f-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://proceedings.iclr.cc/paper_files/paper/2026/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf)

## Why This Paper Is Here

ICLR의 UrbanGS는 도시 규모 장면에서 깊이와 표면 법선의 일관성을 이용해 기하를 정제하고 중복 가우시안을 줄인다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf#page=1) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf#page=5)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** While 3D Gaussian Splatting (3DGS) enables high-quality, real-time rendering for bounded scenes, its extension to large-scale urban environments gives rise to critical challenges in terms ...
- **p. 1 / ABSTRACT - extractive body cue:** To address these issues, we present UrbanGS, a scalable reconstruction framework that effectively tackles these challenges for city-scale applications.
- **p. 1 / ABSTRACT - extractive body cue:** First, we propose a Depth-Consistent D-Normal Regularization module.
- **p. 1 / ABSTRACT - extractive body cue:** Unlike existing approaches that rely solely on monocular normal estimators, which can effectively update rotation parameters yet struggle to update position parameters, our method integrates ...
- **p. 1 / ABSTRACT - extractive body cue:** This allows for comprehensive updates of all geometric parameters.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, due to the unstructured nature of 3DGS, accurately representing surfaces-especially in large-scale complex scenes-remains a significant challenge.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** These limitations underscore the urgent need for a unified framework that balances geometric precision, memory efficiency, and seamless scalability.

## Core Idea

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our main contributions are summarized below: • We propose a Depth-Consistent D-Normal Regularizer that enables holistic optimization of all Gaussian parameters (position, rotation), addressing the ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To overcome this limitation, we introduce a Depth-Consistent D-Normal Regularization framework.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose UrbanGS, a strategy that achieves high geometric accuracy, fidelity, and efficiency in large-scale scene reconstruction.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To meet the memory and computational demands of urban-scale reconstruction, we propose a Spatially Adaptive Gaussian Pruning (SAGP) method.
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** (4) In our method, the depth map is rendered by performing a weighted sum of depths (Bae & Davison, 2024; Chen et al., 2024b; Yu ...
- **p. 7 / 3.1 PRELIMINARIES - extractive body cue:** First, when obtaining the global coarse 3DGS model, we first eliminate redundant Gaussians through SAGP pruning to prevent these redundant Gaussians from attracting non-contributing views ...
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** To reconstruct scene surfaces, we enforce normal priors N predicted by a pretrained monocular deep neural network (Bae & Davison, 2024) to supervise the rendered ...
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** The surface is then extracted using the Marching Cubes algorithm at the zero-level isosurface, enabling direct reconstruction of 3D geometry without relying on intermediate point ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | First, the rendered depth map is back-projected into point clouds{dk(n, p)}, using the camera intrinsic matrix. | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3.1 PRELIMINARIES), p. 7 (3.1 PRELIMINARIES) |
| State/latent | First, rendered, depth, back-projected, point, clouds, camera, intrinsic, matrix, ensures, Gaussian, retained | geometry, map, object/relationship state | p. 5 (3.1 PRELIMINARIES), p. 7 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES) |
| Output/action | D.5) and ensures that a Gaussian is retained only when it simultaneously exhibits high visibility, frequent observation across views, and appropriate geometric scale. | point map, pose, scene graph, affordance 또는 query result | p. 7 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES) |
| Objective/outcome | This formulation minimizes relative depth errors per pixel while enhancing distant surface accuracy where linear depth gradients diminish. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES) |

## Main Claims and Actual Contribution

- 외부 깊이와 렌더링 깊이에서 유도한 법선을 결합하고, 기울기·역깊이 일치도에 따라 제약의 신뢰도를 조절한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf#page=6)
- 국소 기하 복잡도와 가시성에 따라 가우시안을 제거하고, 도시 데이터에서 표면 오차·렌더링 품질·저장 비용을 비교했다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf#page=7) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Embodiment/environment | We compare our method with existing surface reconstruction approaches on the GauU-Scene datasets (Xiong et al., 2024). | hardware/simulator version and reset protocol | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Dataset/benchmark | Methods Residence Russian Building Modern Building P ↑ R ↑ F1 ↑ P ↑ R ↑ F1 ↑ P ↑ R ↑ F1 ↑ NeuS FAIL FAIL FAIL FAIL FAIL FAIL FAIL ... | role, split, size and leakage | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Metric | In particular, compared with CityGS-X, our approach attains higher F1 scores across all scenes by improving recall while maintaining comparable precision. | definition, denominator, direction and uncertainty | p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Baseline/ablation | Figure 4: Qualitative mesh and texture comparison between SOTA and our method on GauU-Scene dataset (Xiong et al., 2024). 4.2 MAIN RESULTS Novel View Synthesis. As shown in Table 1 and Fig. ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Detailed geometry evaluation on the GauU-Scene dataset (Xiong et al., 2024). "NaN" indicates that the method produced invalid numerical results, while "FAIL" denotes ...
- **p. 25 / C SUPPLEMENTATION TO THE PARTITIONING STRATEGY - extractive body cue:** Qualitative results in Figure F show that rendered views remain visually consistent across different weight combinations, with no catastrophic failures even for suboptimal settings.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We propose UrbanGS, a scalable framework for high-fidelity large-scale scene reconstruc- tion. Left: It reconstructs complex urban environments from multi-view RGB images, capturing ...
- **p. 23 / C SUPPLEMENTATION TO THE PARTITIONING STRATEGY - extractive body cue:** This discrepancy highlights a limitation of current geometry optimization objectives when applied to background regions lacking clear geometric structure.
- **p. 26 / C SUPPLEMENTATION TO THE PARTITIONING STRATEGY - extractive body cue:** E LIMITATIONS Although UrbanGS demonstrates advantages in large-scale reconstruction, it still exhibits certain limitations.
- **p. 26 / C SUPPLEMENTATION TO THE PARTITIONING STRATEGY - extractive body cue:** Additionally, the method primarily focuses on static environments and does not explicitly model dynamic objects commonly found in urban scenes.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Methods Residence Russian Building Modern Building P ↑ R ↑ F1 ↑ P ↑ R ↑ F1 ↑ P ↑ R ↑ F1 ↑ NeuS ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 7 (3.1 PRELIMINARIES)이다.

## 검색 태그 근거

단안 깊이 추정과 가우시안 렌더링의 일치로 표면 법선과 기하를 정제하고, 도시 장면의 가우시안을 중요도에 따라 줄인다. 평가 대상은 대규모 장면 복원이다. [원문 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf#page=4) · [원문 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf#page=8)
