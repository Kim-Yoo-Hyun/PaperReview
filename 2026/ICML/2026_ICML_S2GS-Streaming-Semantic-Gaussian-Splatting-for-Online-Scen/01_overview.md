# S2GS: Streaming Semantic Gaussian Splatting for Online Scene Understanding and Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=CbWCaD8tRC.
> PDF retrieval source: https://openreview.net/pdf/fec4864d5571755c82ad1d076f9a8e3e4ca69cf8.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, semantic, alignment, 3D Vision
- Official paper: https://openreview.net/forum?id=CbWCaD8tRC
- Full-text retrieval: https://openreview.net/pdf/fec4864d5571755c82ad1d076f9a8e3e4ca69cf8.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, most existing approaches remain limited to streaming modeling of geometry and appearance, lacking semantic scene understanding and instance-level, decomposable representations, and thus falling short for downstream applications ...를 문제로 두고, We propose S2GS, a strictly causal and reprocessing-free framework for online joint 3D reconstruction and scene understanding, which incrementally maintains scene geometry, appearance, and an instance-level semantic field.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1. Introduction - extractive body cue:** We propose S2GS, a strictly causal and reprocessing-free framework for online joint 3D reconstruction and scene understanding, which incrementally maintains scene geometry, appearance, and an ...
- **p. 5 / 3.4. Language-driven Open-vocabulary Segmentation - extractive body cue:** To bridge this gap, we introduce a lightweight Query Semantic Projector gθ(·) that maps each per-frame query embedding to the 2D foundation vision model (Tschannen ...
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: 1.
- **p. 3 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** (1) This design allows parallel processing of training clips while remaining equivalent to an autoregressive causal model.
- **p. 4 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** Semantic confidence is lifted to the 3D Gaussian field and decoded via splatting, enabling unified novel view synthesis, semantic segmentation, instance segmentation, and panoptic segmentation ...
- **p. 6 / 4.2. Results - extractive body cue:** Nevertheless, as the number of input views increases (8/14/32), S2GS consistently improves and achieves strong performance in both reconstruction quality and temporal semantic/instance consistency, highlighting ...
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** The results demonstrate that the distillation loss significantly improves reconstruction quality.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** As shown in Table 7, geometry-semantic decoupling leads to a clear improvement in per-frame semantic accuracy and yields even larger gains in temporal instance consistency ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.2. Results), p. 8 (4.3. Ablation Studies) |
| Embodiment/environment | Comparison with feed-forward methods on the ScanNet (Dai et al., 2017) dataset under short-sequence inputs. "•", "†", and "⋆" denote reconstruction-only, understanding-only, and joint reconstruction-and-understanding methods, respectively. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results) |
| Dataset/benchmark | Zero-shot cross-dataset comparison under 32-view input. | role, split, size and leakage | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results), p. 7 (4.2. Results), p. 8 (4.2. Results) |
| Metric | Detailed sequence construction, the IoU definition, and training settings are provided in the appendix. | definition, denominator, direction and uncertainty | p. 5 (4.1. Experimental Setup), p. 6 (82.49 Method), p. 8 (4.3. Ablation Studies) |
| Baseline/ablation | We also include widely used 2D semantic segmentation baselines, LSeg (Li et al., 2022) and Mask2Former (Cheng et al., 2022). | fair input/data/compute/action matching | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Results) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.2. Results - extractive body cue:** As shown in Table 2, under the extremely sparse 2-view setting, S2GS does not achieve the best PSNR/SSIM.
- **p. 6 / 4.2. Results - extractive body cue:** This is expected, since offline baselines can exploit non-causal cross-view aggregation over the full input set to better resolve view ambiguity and occlusions when observations ...
- **p. 8 / 4.2. Results - extractive body cue:** Nevertheless, under the same training configuration, S2GS achieves better reconstruction and semantic performance on both datasets, demonstrating stronger cross-dataset generalization and robustness.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, most existing approaches remain limited to streaming modeling of geometry and appearance, lacking semantic scene understanding and instance-level, decomposable representations, and thus falling short for downstream applications ...를 문제로 두고, We propose S2GS, a strictly causal and reprocessing-free framework for online joint 3D reconstruction and scene understanding, which incrementally maintains scene geometry, appearance, and an instance-level semantic field.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overview and Online Setting), p. 4 (3.2. Causal Transformer for 3D Gaussian Regression) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
