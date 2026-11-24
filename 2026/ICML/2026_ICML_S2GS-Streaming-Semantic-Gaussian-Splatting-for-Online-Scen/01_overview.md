# S2GS: Streaming Semantic Gaussian Splatting for Online Scene Understanding and Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2026/poster/65536.
> PDF retrieval source: https://openreview.net/pdf/fec4864d5571755c82ad1d076f9a8e3e4ca69cf8.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Renhe Zhang, Yuyang Tan, Jingyu Gong, Zhizhong Zhang, Lizhuang Ma, Yuan Xie, Xin Tan
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, semantic, alignment, 3D Vision
- Official paper: https://icml.cc/virtual/2026/poster/65536
- Full-text retrieval: https://arxiv.org/pdf/2603.14232.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26fn/zhang26fn.pdf)

## Why This Paper Is Here

S2GS는 영상이 도착할 때마다 과거 프레임을 다시 처리하지 않고 장면의 기하·외관과 인스턴스 의미를 갱신한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26fn/zhang26fn.pdf#page=1) · [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26fn/zhang26fn.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Existing offline feed-forward methods for joint scene understanding and reconstruction on long image streams often repeatedly perform global computation over an ever-growing set of past ...
- **p. 1 / Abstract - extractive body cue:** We propose Streaming Semantic Gaussian Splatting (S2GS), a strictly causal, incremental 3D Gaussian semantic field framework: it does not leverage future frames and continuously updates ...
- **p. 1 / Abstract - extractive body cue:** S2GS adopts a geometry-semantic decoupled dual-backbone design: the geometry branch performs causal modeling to drive incremental Gaussian updates, while the semantic branch leverages a 2D ...
- **p. 1 / Abstract - extractive body cue:** Experiments show that S2GS matches or outperforms strong offline baselines on joint reconstruction-and-understanding benchmarks, while significantly improving longhorizon scalability: it processes 1,000+ frames with much ...
- **p. 1 / 1. Introduction - extractive body cue:** Recently, feed-forward methods (Xu et al., 2025; Sun et al., 2025; Tian et al., 2025) built upon 3D Gaussian Splatting (3DGS) (Kerbl et al., 2023) ...
- **p. 1 / 1. Introduction - extractive body cue:** However, most existing approaches remain limited to streaming modeling of geometry and appearance, lacking semantic scene understanding and instance-level, decomposable representations, and thus falling short ...
- **p. 1 / 1. Introduction - extractive body cue:** As shown in Figure 1, even on an H200 GPU equipped with 140 GB of VRAM, SIU3R (Xu et al., 2025) still encounters an out-ofmemory ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We propose S2GS, a strictly causal and reprocessing-free framework for online joint 3D reconstruction and scene understanding, which incrementally maintains scene geometry, appearance, and an ...
- **p. 5 / 3.4. Language-driven Open-vocabulary Segmentation - extractive body cue:** To bridge this gap, we introduce a lightweight Query Semantic Projector gθ(·) that maps each per-frame query embedding to the 2D foundation vision model (Tschannen ...
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: 1.
- **p. 3 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** (1) This design allows parallel processing of training clips while remaining equivalent to an autoregressive causal model.
- **p. 4 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** Semantic confidence is lifted to the 3D Gaussian field and decoded via splatting, enabling unified novel view synthesis, semantic segmentation, instance segmentation, and panoptic segmentation ...
- **p. 3 / 3.1. Overview and Online Setting - extractive body cue:** The model maintains a persistent 3D Gaussian scene representation and an instance-aware semantic state, enabling scalable long-horizon streaming inference.
- **p. 4 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** A causal Transformer encoder, guided by geometric priors from a 3D foundation model, predicts camera parameters, depth, and Gaussian attributes to incrementally construct 3D Gaussian ...
- **p. 5 / 3.4. Language-driven Open-vocabulary Segmentation - extractive body cue:** To make the projection robust to such dynamics, we enforce instancelevel semantic invariance during training: supervised querylevel contrastive learning encourages embeddings corresponding to the same ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This naturally imposes a causal constraint on online joint reconstruction and understanding: at each time step, the model can only rely on the current observation and a persistent state accumulated from the ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | naturally, imposes, causal, constraint, online, joint, reconstruction, understanding, time, step, model, only | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. Language-driven Open-vocabulary Segmentation) |
| Output/action | More fundamentally, in real-world online scenarios, inputs arrive sequentially over time and the system must update its state 1 | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 2 (1. Introduction) |
| Objective/outcome | Under the causal constraint, the Transformer aggregates information from {Iτ}τ≤t to form geometry features Ht. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3.2. Causal Transformer for 3D Gaussian Regression), p. 4 (3.3. Online Instance Tracking and Semantic), p. 3 (3.2. Causal Transformer for 3D Gaussian Regression) |

## Main Claims and Actual Contribution

- 인과적 기하 분기에서 가우시안을 갱신하고 의미 분기에서 쿼리 대조 학습과 인스턴스 메모리로 프레임 사이의 식별자를 연결한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26fn/zhang26fn.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26fn/zhang26fn.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26fn/zhang26fn.pdf#page=5)
- 복원과 분할을 함께 평가하고 입력 길이에 따른 메모리 사용량과 처리 시간을 오프라인 일괄 처리 모델과 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26fn/zhang26fn.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26fn/zhang26fn.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26fn/zhang26fn.pdf#page=8)

## Evaluation Scope

스트리밍 효율 비교는 현재 뷰를 처리해 누적 상태를 갱신하는 프레임당 지연과 최대 GPU 메모리를 입력 길이별로 측정했다. 재구성·분할·인스턴스 추적의 정확도는 별도 지표로 평가했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26fn/zhang26fn.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26fn/zhang26fn.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26fn/zhang26fn.pdf#page=8)

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.2. Results - extractive body cue:** As shown in Table 2, under the extremely sparse 2-view setting, S2GS does not achieve the best PSNR/SSIM.
- **p. 6 / 4.2. Results - extractive body cue:** This is expected, since offline baselines can exploit non-causal cross-view aggregation over the full input set to better resolve view ambiguity and occlusions when observations ...
- **p. 8 / 4.2. Results - extractive body cue:** Nevertheless, under the same training configuration, S2GS achieves better reconstruction and semantic performance on both datasets, demonstrating stronger cross-dataset generalization and robustness.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overview and Online Setting), p. 4 (3.2. Causal Transformer for 3D Gaussian Regression)이다.
