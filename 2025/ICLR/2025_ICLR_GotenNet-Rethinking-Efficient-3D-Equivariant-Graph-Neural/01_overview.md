# GotenNet: Rethinking Efficient 3D Equivariant Graph Neural Networks

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/64d4ff4fff788cdffe236f9ce8b09400-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/111955. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Sarp Aykent, Tian Xia
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: equivariant, 3D Vision
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/64d4ff4fff788cdffe236f9ce8b09400-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/64d4ff4fff788cdffe236f9ce8b09400-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://proceedings.iclr.cc/paper_files/paper/2025/file/64d4ff4fff788cdffe236f9ce8b09400-Paper-Conference.pdf)

## Why This Paper Is Here

GotenNet은 분자의 좌표계를 회전·반사·이동시켜도 예측이 올바르게 변환되도록 3D 그래프에서 기하 텐서 특징을 학습한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/64d4ff4fff788cdffe236f9ce8b09400-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/64d4ff4fff788cdffe236f9ce8b09400-Paper-Conference.pdf#page=4)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Understanding complex three-dimensional (3D) structures of graphs is essential for accurately modeling various properties, yet many existing approaches struggle with fully capturing the intricate spatial ...
- **p. 1 / ABSTRACT - extractive body cue:** These methods often must balance trade-offs between expressiveness and computational efficiency, limiting their scalability.
- **p. 1 / ABSTRACT - extractive body cue:** To address this gap, we propose a novel Geometric Tensor Network (GotenNet) that effectively models the geometric intricacies of 3D graphs while ensuring strict equivariance ...
- **p. 1 / ABSTRACT - extractive body cue:** Our approach directly tackles the expressiveness-efficiency trade-off by leveraging effective geometric tensor representations without relying on irreducible representations or Clebsch-Gordan transforms, thereby reducing computational o ...
- **p. 1 / ABSTRACT - extractive body cue:** We introduce a unified structural embedding, incorporating geometryaware tensor attention and hierarchical tensor refinement that iteratively updates edge representations through inner product operations on high-degree ...
- **p. 2 / B L - extractive body cue:** The challenge is evident in existing models' inability to bridge the gap between scalarization-based and high-degree steerable approaches while maintaining practical applicability.
- **p. 1 / B L - extractive body cue:** Traditional graph neural networks (GNNs), while effective for general graph-structured data, face difficulties in handling the geometric and topological complexities of 3D molecular systems, where ...

## Core Idea

- **p. 1 / ABSTRACT - extractive body cue:** To address this gap, we propose a novel Geometric Tensor Network (GotenNet) that effectively models the geometric intricacies of 3D graphs while ensuring strict equivariance ...
- **p. 2 / B L - extractive body cue:** To address these challenges, we propose a novel framework, the Geometric Tensor Network (GotenNet).
- **p. 2 / B L - extractive body cue:** First, we introduce a spherical-scalarization model with an efficient representation and embedding strategy designed specifically with geometric tensors, eliminating the need for irreps and CG ...
- **p. 1 / ABSTRACT - extractive body cue:** We introduce a unified structural embedding, incorporating geometryaware tensor attention and hierarchical tensor refinement that iteratively updates edge representations through inner product operations on high-degree ...
- **p. 2 / B L - extractive body cue:** These mechanisms enhance transformer-based architectures by refining edge representations through high-degree steerable features, enabling the self-attention mechanism to leverage refined geometric relationships in determining node ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We evaluated models on QM9, rMD17, MD22, and Molecule3D datasets, where the proposed model consistently outperforms state-of-the-art methods in both scalar and high-degree property predictions, demonstrating exceptional robustness acros ... | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (ABSTRACT), p. 2 (B L) |
| State/latent | evaluated, models, QM9, rMD17, MD22, Molecule3D, datasets, where, model, consistently, outperforms, state-of-the-art | geometry, map, object/relationship state | p. 1 (ABSTRACT), p. 2 (B L), p. 2 (B L) |
| Output/action | These mechanisms enhance transformer-based architectures by refining edge representations through high-degree steerable features, enabling the self-attention mechanism to leverage refined geometric relationships in determining node inte ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (B L), p. 2 (B L), p. 1 (ABSTRACT) |
| Objective/outcome | We introduce a unified structural embedding, incorporating geometryaware tensor attention and hierarchical tensor refinement that iteratively updates edge representations through inner product operations on high-degree steerable feature ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (ABSTRACT), p. 2 (B L) |

## Main Claims and Actual Contribution

- 기하 텐서 attention과 계층적 특징 정제를 결합하고 방향에 따라 변하는 특징의 내적으로 그래프 간선 표현을 갱신한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/64d4ff4fff788cdffe236f9ce8b09400-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/64d4ff4fff788cdffe236f9ce8b09400-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/64d4ff4fff788cdffe236f9ce8b09400-Paper-Conference.pdf#page=6)
- QM9, rMD17 등 분자 데이터에서 스칼라 및 방향성 물성의 예측 오차와 연산 비용을 비교했다. [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/64d4ff4fff788cdffe236f9ce8b09400-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/64d4ff4fff788cdffe236f9ce8b09400-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/64d4ff4fff788cdffe236f9ce8b09400-Paper-Conference.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Embodiment/environment | This dataset contains over 29× more graphs than QM9, with approximately 1.6× and 1.9× increases in the average number of nodes and edges per graph, providing an ideal benchmark for both model ... | hardware/simulator version and reset protocol | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Dataset/benchmark | The rMD17 dataset (Christensen & Von Lilienfeld, 2020) is a revised version of the MD17 benchmark, featuring 10 small organic molecules with 100,000 conformations per molecule. | role, split, size and leakage | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Metric | The best log error of -4.65 in the random split further demonstrates the model's robustness on larger datasets. | definition, denominator, direction and uncertainty | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 24 (Figure/Table caption) |
| Baseline/ablation | As shown in Table 1, even our smallest variant GotenNetS outperforms baseline methods on nine out of twelve targets while surpassing baselines on std. | fair input/data/compute/action matching | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 5 CONCLUSION - extractive body cue:** Future work could further enhance its scalability to larger molecular systems and explore applications in molecular dynamics and materials science.
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 5: Mean absolute error of the molecules on rMD17 dataset for energy and forces. share the fundamental requirement of processing geometric relationships while preserving ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Architecture of GotenNet. The overall framework (a) includes an embedding, an interaction module, and a decoder; (b) shows the geometry-aware tensor attention (GATA); ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The best log error of -4.65 in the random split further demonstrates the model's robustness on larger datasets.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** These results highlight the robustness and versatility of GotenNet in handling diverse molecular structures, establishing it as a leading model in both energy and force ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** The results are averaged over five predefined splits to ensure robust evaluation.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (B L), p. 1 (B L), p. 1 (ABSTRACT)이다.
