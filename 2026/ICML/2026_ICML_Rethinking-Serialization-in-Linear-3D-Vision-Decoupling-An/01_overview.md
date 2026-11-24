# Rethinking Serialization in Linear 3D Vision: Decoupling Anisotropic Geometry from Isotropic Semantics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2026/poster/64540.
> PDF retrieval source: https://openreview.net/pdf/fa9e033b756ac063d19be2b3bb91daea759e1ae1.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: YinYun Yan, Liping Zhang, Tingran Wang, Jiaxin Deng, Changshuo Wang, Limin Jiang, Shanwei Gao, Xin Ning
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic, alignment, 3D Vision
- Official paper: https://icml.cc/virtual/2026/poster/64540
- Published PDF: https://raw.githubusercontent.com/mlresearch/v306/main/assets/yan26v/yan26v.pdf
- Full-text retrieval at original review: https://openreview.net/pdf/fa9e033b756ac063d19be2b3bb91daea759e1ae1.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/yan26v/yan26v.pdf)

## Why This Paper Is Here

AnIsoNet은 점군 직렬화 순서에 따른 편향을 줄이기 위해 국소 기하와 넓은 범위의 의미 정보를 서로 다르게 집계한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/yan26v/yan26v.pdf#page=1) · [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/yan26v/yan26v.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Current linear State-Space Models (SSMs) for 3D point clouds typically rely on 1D serialization schemes (e.g., Hilbert curves) for global modeling.
- **p. 1 / Abstract - extractive body cue:** In dense scenes, such imposed order can disrupt spatial continuity and induce what we call serialization bias.
- **p. 1 / Abstract - extractive body cue:** We propose AnIsoNet, a framework that decouples anisotropic geometry from isotropic semantics via two dedicated modules: Local Anisotropy Geometric Modeling (LAGM) and Global Isotropy Semantic ...
- **p. 1 / Abstract - extractive body cue:** LAGM uses ellipsoidal encoding to capture local directionality without relying on global order.
- **p. 1 / Abstract - extractive body cue:** GISA is configured according to dataset-level geometric density: dense-scene datasets use Identity Mode to avoid additional geometry-driven re-serialization, whereas sparseobject datasets use Morton serialization to ...
- **p. 1 / 1. Introduction - extractive body cue:** Effective 3D point cloud understanding must reconcile local anisotropic geometry with global isotropic semantics, but the irregular and unordered nature of point sets makes this ...
- **p. 2 / 1. Introduction - extractive body cue:** However, unlike Transformers that support noncausal attention, the strict recurrent path dependency of SSMs (where state ht strictly depends on ht-1) introduces a new serialization ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Based on this observation, we propose AnIsoNet, which decouples local anisotropic geometry modeling from global semantic aggregation.
- **p. 3 / 3.1. Overview - extractive body cue:** The framework consists of two complementary modules: 1.
- **p. 3 / 3.1. Overview - extractive body cue:** To address this limitation, we propose AnIsoNet, a unified framework that decouples these two processes (Figure 2).
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We identify serialization bias as a key bottleneck in 3D SSMs and propose a decoupling paradigm that addresses local ...
- **p. 5 / 3.1. Overview - extractive body cue:** The recurrence ht = f(ht-1, xt) inherently requires a sequential ordering, so 3D point clouds must be artificially serialized and the contribution of xs to ...
- **p. 4 / 3.1. Overview - extractive body cue:** Following the DeLA architecture (Chen et al., 2023), we use dataset-specific hierarchical LAGM encoders (Figure 2a).
- **p. 4 / 3.1. Overview - extractive body cue:** The projected ESE feature is injected into the stage representation and then aggregated on the k-NN graph.
- **p. 3 / 3.1. Overview - extractive body cue:** Current 3D State-Space Models (SSMs) typically force point clouds into a single 1D sequence via space-filling curves, conflating local geometric modeling with global semantic aggregation.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In Mamba (Gu & Dao, 2024), the state evolves as: ht = ¯A · ht-1 + ¯Bt · xt, yt = Ct · ht, (9) where ht is the recurrent hidden state, ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3.1. Overview), p. 5 (3.1. Overview) |
| State/latent | Mamba, Dao, state, evolves, ht-1, where, recurrent, hidden, inputdependent, step, size, continuous-time | geometry, map, object/relationship state | p. 5 (3.1. Overview), p. 5 (3.1. Overview), p. 3 (3.1. Overview) |
| Output/action | Unlike standard DeltaNet (Yang et al., 2024) which maintains a matrix state S ∈RD×D to capture cross-dimensional interactions, we employ a dimension-wise vector state st ∈RD, initialized as s0 = 0, that ... | point map, pose, scene graph, affordance 또는 query result | p. 5 (3.1. Overview), p. 3 (3.1. Overview), p. 3 (3.1. Overview) |
| Objective/outcome | The objective of LAGM is to capture local anisotropy within k-NN neighborhoods, independent of any global serialization order. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 4 (3.1. Overview) |

## Main Claims and Actual Contribution

- 국소 이웃은 방향에 민감하게 모델링하고 전역 의미는 등방적으로 집계해 서로 다른 인접 관계를 이용한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/yan26v/yan26v.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/yan26v/yan26v.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/yan26v/yan26v.pdf#page=5)
- 실내 점군 의미 분할 자료에서 정확도를 평가하고 두 집계 방식과 직렬화 순서의 영향을 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/yan26v/yan26v.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/yan26v/yan26v.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/yan26v/yan26v.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4.4. Efficiency Analysis), p. 6 (4.1. Experimental Setup) |
| Embodiment/environment | Dataset Regime Protocol Identity/Default (%) Hilbert (%) Morton (%) S3DIS Dense scene Mode ablation 82.62 74.46 74.68 ScanObjectNN Sparse object Mode ablation 92.51 93.86 94.21 Order Robustness in Dense Scenes. | hardware/simulator version and reset protocol | p. 7 (4.3. Analysis and Ablation), p. 8 (4.3. Analysis and Ablation) |
| Dataset/benchmark | We evaluate AnIsoNet on three benchmarks spanning different geometric regimes: (1) S3DIS (Armeni et al., 2016) Area 5: Dense indoor scenes with approximately 100K points per room, suitable for evaluating isotropic aggregation. | role, split, size and leakage | p. 7 (4.3. Analysis and Ablation), p. 8 (4.3. Analysis and Ablation), p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Metric | Overall, the figure shows that AnIsoNet improves accuracy while remaining in a much smaller parameter regime, rather than trading scale for performance. | definition, denominator, direction and uncertainty | p. 8 (4.4. Efficiency Analysis), p. 8 (4.4. Efficiency Analysis), p. 6 (4.2. Main Results) |
| Baseline/ablation | Relative to linear-complexity baselines, it outperforms PCM (Zhang et al., 2025) by 3.0% and Sonata (lin.) by 10.3%. | fair input/data/compute/action matching | p. 6 (4.2. Main Results), p. 7 (4.3. Analysis and Ablation), p. 6 (4.2. Main Results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.3. Analysis and Ablation - extractive body cue:** A mismatched mode therefore causes noticeable degradation rather than collapse.
- **p. 7 / 4.3. Analysis and Ablation - extractive body cue:** Because our claim concerns robustness rather than strict permutation invariance, we directly test the task-relevant notion of robustness by perturbing the inference-time input order on ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Overview)이다.
