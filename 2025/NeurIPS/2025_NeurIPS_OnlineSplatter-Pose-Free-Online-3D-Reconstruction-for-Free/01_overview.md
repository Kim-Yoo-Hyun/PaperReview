# OnlineSplatter: Pose-Free Online 3D Reconstruction for Free-Moving Objects

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=Y9AdTCCEgI.
> PDF retrieval source: https://arxiv.org/pdf/2510.20605. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Official paper: https://openreview.net/forum?id=Y9AdTCCEgI
- Full-text retrieval: https://arxiv.org/pdf/2510.20605
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Eliminating camera pose as input remains a key challenge in 3D reconstruction.를 문제로 두고, To address these limitations, we propose a novel object-centric memory mechanism, Dual-Key 3D Object Memory, that consists of a key-value memory bank.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Free-moving object reconstruction from monocular video remains challenging, particularly without reliable pose or depth cues and under arbitrary object motion.
- **p. 1 / Abstract - extractive body cue:** We introduce OnlineSplatter, a novel online feed-forward framework generating highquality, object-centric 3D Gaussians directly from RGB frames without requiring camera pose, depth priors, or bundle ...
- **p. 1 / Abstract - extractive body cue:** Our approach anchors reconstruction using the first frame and progressively refines the object representation through a dense Gaussian primitive field, maintaining constant computational cost regardless ...
- **p. 1 / Abstract - extractive body cue:** Our core contribution is a dual-key memory module combining latent appearance-geometry keys with explicit directional keys, robustly fusing current frame features with temporally aggregated object ...
- **p. 1 / Abstract - extractive body cue:** This design enables effective handling of free-moving objects via spatial-guided memory readout and an efficient sparsification mechanism, ensuring comprehensive yet compact object coverage.
- **p. 2 / 1 Introduction - extractive body cue:** Eliminating camera pose as input remains a key challenge in 3D reconstruction.
- **p. 2 / 1 Introduction - extractive body cue:** Motivated by these challenges, we propose OnlineSplatter, a feed-forward framework for online reconstruction of freely moving objects.

## Core Idea

- **p. 5 / 3 Method - extractive body cue:** To address these limitations, we propose a novel object-centric memory mechanism, Dual-Key 3D Object Memory, that consists of a key-value memory bank.
- **p. 4 / 3 Method - extractive body cue:** The input to our framework consists of a stream of RGB images {Vt}N t=0, where object masks {Mt}N t=0 are generated and applied to remove ...
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are: (i) a novel feed-forward framework for object-centric online 3D reconstruction that operates on monocular RGB streams in real-time, eliminating the need for ...
- **p. 2 / 1 Introduction - extractive body cue:** Motivated by these challenges, we propose OnlineSplatter, a feed-forward framework for online reconstruction of freely moving objects.
- **p. 3 / 3 Method - extractive body cue:** To differentiate and contextualize these tokens, we introduce 3
- **p. 4 / 3 Method - extractive body cue:** These tokens are then fed into a transformer-based architecture, which directly reasons and outputs pixel-aligned 3D Gaussian representations in a canonical space.
- **p. 5 / 3 Method - extractive body cue:** While our latent key, derived from tokenized features through end-to-end training with 3D reasoning objectives, captures both visual and geometric information, relying solely on latent ...
- **p. 7 / 3 Method - extractive body cue:** Specifically, we optimize the view encoder (EncoderI 1), positional and view embeddings (f emb pos and f emb view), OnlineSplatter transformer, and unpatchify decoder in ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Moreover, to control memory growth as observations accumulate, we propose an attention-based memory module that fuses incoming frame features with a compact latent state, eliminating the overhead of bundle adjustment or additional ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 5 (3 Method) |
| State/latent | Moreover, control, memory, growth, observations, accumulate, attention-based, module, fuses, incoming, frame, features | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 5 (3 Method), p. 3 (3 Method) |
| Output/action | Specifically, a trainable value encoder (defined as EncoderV ) takes output tokens Tout src,t as input to produce the new value: v(L) t := f V t = EncoderV (Tout src,t) (6) ... | point map, pose, scene graph, affordance 또는 query result | p. 5 (3 Method), p. 3 (3 Method), p. 4 (3 Method) |
| Objective/outcome | These objectives present a challenging optimization landscape, as the gradients for the second objective only become meaningful after the first objective reaches a certain level of convergence. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 7 (3 Method), p. 7 (3 Method), p. 6 (3 Method) |

## Main Claims and Actual Contribution

- **p. 5 / 3 Method - extractive body cue:** To address these limitations, we propose a novel object-centric memory mechanism, Dual-Key 3D Object Memory, that consists of a key-value memory bank.
- **p. 4 / 3 Method - extractive body cue:** The input to our framework consists of a stream of RGB images {Vt}N t=0, where object masks {Mt}N t=0 are generated and applied to remove ...
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are: (i) a novel feed-forward framework for object-centric online 3D reconstruction that operates on monocular RGB streams in real-time, eliminating the need for ...
- **p. 2 / 1 Introduction - extractive body cue:** Motivated by these challenges, we propose OnlineSplatter, a feed-forward framework for online reconstruction of freely moving objects.
- **p. 3 / 3 Method - extractive body cue:** To differentiate and contextualize these tokens, we introduce 3
- **p. 8 / 4.2 Results - extractive body cue:** Even with fewer than four observations, OnlineSplatter significantly outperforms all baselines.
- **p. 7 / 4 Experiments - extractive body cue:** We therefore design a stage-wise evaluation protocol that examines performance across three distinct phases: 1) Early Stage (Tearly := {1 ≤t ≤4}): Tests the model's ...
- **p. 8 / 4.2 Results - extractive body cue:** Across all metrics and stages, OnlineSplatter achieves superior performance-improving up to +7.596 PSNR and +0.106 SSIM on GSO, and +4.981 PSNR and +0.092 SSIM on ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.2 Results), p. 7 (4 Experiments) |
| Embodiment/environment | Second, we assess generalization to real-world monocular videos with occlusions using the HO3D dataset [10], which contains hand-object interaction sequences. | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Dataset/benchmark | Future work could explore modeling non-rigid objects and integrate it with downstream tasks like robotic manipulation. | role, split, size and leakage | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 10 (4.2 Results), p. 7 (4 Experiments) |
| Metric | 3, where our method delivers notably better visual quality and geometric accuracy from early to late stages. | definition, denominator, direction and uncertainty | p. 8 (4.2 Results), p. 8 (4.2 Results), p. 9 (4.2 Results) |
| Baseline/ablation | This section evaluates our approach by outlining the evaluation protocol, describing the datasets for training and testing, comparing against state-of-the-art baselines, and conducting ablation studies to analyze each component's impact. | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 8 (4.2 Results), p. 8 (4.2 Results) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 4.2 Results - extractive body cue:** 5 Limitations and Future Work Our current framework has some limitations that warrant attention.
- **p. 8 / 4.2 Results - extractive body cue:** Baselines using explicit frame selection often exhibit unstable or stagnant performance.
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 5: Impact of Training Data Quantity and Quality. C.2 Impact of Ray Alignment Loss in Geometrical Supervision. While photometric RGB-based loss can effectively supervise ...
- **p. 10 / 4.2 Results - extractive body cue:** Future work could explore hybrid representations that maintain both rendering efficiency and mesh compatibility.
- **p. 8 / 4 Experiments - extractive body cue:** Second, we assess generalization to real-world monocular videos with occlusions using the HO3D dataset [10], which contains hand-object interaction sequences.
- **p. 9 / 4.2 Results - extractive body cue:** Specifically: Dual-key Design: Removing the latent key severely degrades performance at all stages due to loss of visual-geometrical cues.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Eliminating camera pose as input remains a key challenge in 3D reconstruction.를 문제로 두고, To address these limitations, we propose a novel object-centric memory mechanism, Dual-Key 3D Object Memory, that consists of a key-value memory bank.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (3 Method), p. 5 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
