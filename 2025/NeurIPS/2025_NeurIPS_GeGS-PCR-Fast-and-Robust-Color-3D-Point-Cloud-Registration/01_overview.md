# GeGS-PCR: Effective and Robust 3D Point Cloud Registration with Two-Stage Color-Enhanced Geometric-3DGS Fusion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://neurips.cc/virtual/2025/poster/117748.
> PDF retrieval source: https://arxiv.org/pdf/2604.17721. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: Jiayi Tian, Haiduo Huang, Tian Xia, Wenzhe Zhao, Pengju Ren
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: geometry, sensor fusion, LiDAR, point cloud, 3D Vision
- Publication index title: GeGS-PCR: Fast and Robust Color 3D Point Cloud Registration with Two-Stage Geometric-3DGS Fusion
- Official paper: https://neurips.cc/virtual/2025/poster/117748
- Published PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/0d2e544c1baa964a0e274e711ecdacf5-Paper-Conference.pdf
- Full-text retrieval at original review: https://arxiv.org/pdf/2604.17721
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

GeGS-PCR는 색이 있는 점군 쌍에서 기하·색 특징으로 초기 대응을 구하고 미분 가능한 Gaussian 렌더링으로 정합을 정제한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d2e544c1baa964a0e274e711ecdacf5-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We address the challenge of point cloud registration using color information, where traditional methods relying solely on geometric features often struggle in lowoverlap and incomplete ...
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, we propose GeGS-PCR, a novel two-stage method that combines geometric, color, and Gaussian information for robust registration.
- **p. 1 / Abstract - extractive body cue:** Our approach incorporates a dedicated color encoder that enhances color features by extracting multi-level geometric and color data from the original point cloud.
- **p. 1 / Abstract - extractive body cue:** We introduce the Geometric-3DGS module, which encodes the local neighborhood information of colored superpoints to ensure a globally invariant geometric-color context.
- **p. 1 / Abstract - extractive body cue:** Leveraging LORA optimization, we maintain high performance while preserving the expressiveness of 3DGS.
- **p. 2 / 1 Introduction - extractive body cue:** When color differences are not distinct, simply incorporating color information still fails to establish the correct correspondences.
- **p. 2 / 1 Introduction - extractive body cue:** Despite rapid progress, point cloud registration remains challenging in real-world scenarios with low overlap between point clouds [11, 18], where registration often fails.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Additionally, we introduce a joint photometric loss to improve the utilization of color information during the registration process.
- **p. 2 / 1 Introduction - extractive body cue:** To address the challenges of point cloud registration in low-overlap real-world scenarios, we propose GeGS-PCR, a two-stage method that integrates Geometric-3DGS for colored point cloud ...
- **p. 3 / 1 Introduction - extractive body cue:** • We propose the Geometric-3DGS module to encode multimodal representations of superpoint neighborhood information.
- **p. 3 / 1 Introduction - extractive body cue:** Using attention with 3DGS embeddings, we focus on global geometric distribution-color features and perform fast coarse registration by reducing computational complexity with LORA. • We ...
- **p. 5 / 3 Method - extractive body cue:** Based on this, we introduce a learned scalar weight α = δ(ω), where ω represents the parameter, to adaptively fuse the geometric and color features.
- **p. 5 / 3 Method - extractive body cue:** We use this color encoder in feature extraction at different levels.
- **p. 5 / 3 Method - extractive body cue:** 3.1.2 Geometric-3DGS Module The Geometric-3DGS module mainly consists of three components: the 3DGS encoder, attention with 3DGS embeddings, and Gaussian superpoint registration, as shown in ...
- **p. 4 / 3 Method - extractive body cue:** The feature extraction module extracts and integrates geometric and color information from the input point clouds P and Q using the color encoder and geometric ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The feature extraction module extracts and integrates geometric and color information from the input point clouds P and Q using the color encoder and geometric encoder, producing superpoint representations ˆP and ˆQ. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3 Method), p. 4 (3 Method) |
| State/latent | feature, extraction, module, extracts, integrates, geometric, color, information, input, point, clouds, encoder | geometry, map, object/relationship state | p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method) |
| Output/action | The noise-robust color mapping is as follows: F ′ C = δ(LN(W3 · δ(LN(W2 · (δ(LN(W1δ))))))), (2) where W1, W2, and W3 ∈Rdin×dout are learnable weights, din and dout are input and ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method) |
| Objective/outcome | Using differentiable rendering, we backpropagate the loss to the transformation parameters R∗, t∗and update them with gradient descent. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3 Method), p. 6 (3 Method), p. 14 (A.1 Proof of photometric optimization) |

## Main Claims and Actual Contribution

- 슈퍼포인트의 주변 색과 기하를 함께 인코딩하고 렌더링 기반 광도 손실로 두 점군의 정렬을 개선한다. [PDF 3쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d2e544c1baa964a0e274e711ecdacf5-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d2e544c1baa964a0e274e711ecdacf5-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d2e544c1baa964a0e274e711ecdacf5-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d2e544c1baa964a0e274e711ecdacf5-Paper-Conference.pdf#page=6)
- 색을 입힌 KITTI와 실내 점군에서 겹침이 다른 조건의 정합 재현율 및 회전·이동 오차를 비교했다. [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d2e544c1baa964a0e274e711ecdacf5-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d2e544c1baa964a0e274e711ecdacf5-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d2e544c1baa964a0e274e711ecdacf5-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 18 (A.5 Additional Experiments), p. 8 (4 Experiments) |
| Embodiment/environment | To validate the performance of the GeGS-PCR model, we evaluate it on the indoor benchmarks Color3DMatch (C3DM) and Color3DLoMatch (C3DLM), as well as our colorized outdoor ColorKitti (The specific data construction process, ... | hardware/simulator version and reset protocol | p. 7 (4 Experiments), p. 17 (A.5 Additional Experiments) |
| Dataset/benchmark | Each point cloud in these datasets includes an RGB color value. | role, split, size and leakage | p. 7 (4 Experiments), p. 17 (A.5 Additional Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments) |
| Metric | In addition, removing LoRA optimization (row f) leads to a slight drop in registration performance, particularly in IR and RR, indicating that LoRA mainly accelerates convergence and provides a modest yet consistent ... | definition, denominator, direction and uncertainty | p. 9 (4 Experiments), p. 18 (A.5 Additional Experiments), p. 9 (4 Experiments) |
| Baseline/ablation | We compared GeGS-PCR with several SOTA methods (metrics in Appendix A.3). | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 9 (4 Experiments), p. 19 (A.5 Additional Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 5 Conclusion - extractive body cue:** Through local Gaussian feature extraction, GeGS-PCR effectively suppresses noise interference and robustly fuses geometric and color features.
- **p. 19 / A.6 Limitations - extractive body cue:** In future work, we aim to explore scene-level registration of 3DGS for more realistic environmental registration.
- **p. 10 / 4 Experiments - extractive body cue:** Further limitations and a comprehensive performance analysis can be found in Appendix A.5 and Appendix A.6.
- **p. 9 / 4 Experiments - extractive body cue:** Removing color information (row e) causes the most significant degradation, with PIR, IR, and RR dropping notably on both C3DM and C3DLM, highlighting the critical ...
- **p. 17 / A.5 Additional Experiments - extractive body cue:** Specifically, compared to Vanilla Self-attention, 3DGS Self-attention shows stronger robustness across the entire overlap range, with its advantages becoming more pronounced in complex environments.
- **p. 17 / A.5 Additional Experiments - extractive body cue:** As the overlap decreases, GeGS-PCR maintains strong performance even in the 0.5-0.6 overlap range, with a PIR of 0.938, an IR of 0.872, and an ...
- **p. 19 / A.7 Qualitative Results - extractive body cue:** 8, GeGS-PCR demonstrates its robustness, providing accurate registration results even in complex scenarios.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 5 (3 Method), p. 4 (3 Method), p. 6 (3 Method)이다.
