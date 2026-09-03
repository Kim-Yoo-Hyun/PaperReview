# Weakly Supervised Cross-Modal Learning for 4D Radar Scene Flow Estimation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=MCu8SOjPad.
> PDF retrieval source: https://openreview.net/pdf/ed47436b3c090baac63dc92adf3fafca0e15cc01.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: sensor fusion, LiDAR, 3D Vision
- Official paper: https://openreview.net/forum?id=MCu8SOjPad
- Full-text retrieval: https://openreview.net/pdf/ed47436b3c090baac63dc92adf3fafca0e15cc01.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 A straightforward attempt is to extend LiDAR-based self-supervised approaches, but the commonly used clustering strategies (Zhang et al., 2024b; Lin et al., 2025b) and Chamfer-guided (Wu et al., 2020; Mittal et al., ...를 문제로 두고, Given the high cost of high-performance LiDAR sensors, we propose a novel setting, weakly supervised cross-modal learning for 4D radar scene flow, that relies only on RGB images and odometry, which are ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Due to the difficulty of obtaining ground-truth data for 4D radar scene flow estimation, previous methods typically rely on either self-supervised losses or cross-modal supervision ...
- **p. 1 / Abstract - extractive body cue:** However, self-supervised approaches often yield suboptimal results due to radar's inherently low-fidelity measurements, while existing cross-modal supervised methods introduce complex multi-task architecture and require costly ...
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, we propose a task-specific iterative framework for weakly supervised radar scene flow learning, using only images and odometry for auxiliary supervision ...
- **p. 1 / Abstract - extractive body cue:** Specially, we establish two novel instance-aware selfsupervised losses by exploiting off-the-shelf 2D tracking and segmentation algorithms to obtain tracked instance masks, which are back-projected into ...
- **p. 1 / Abstract - extractive body cue:** Extensive experiments on the real-world View-of-Delft (VoD) dataset demonstrate that our method not only surpasses state-of-the-art cross-modal supervised approaches that rely on 3D multi-object tracking ...
- **p. 2 / 1. Introduction - extractive body cue:** A straightforward attempt is to extend LiDAR-based self-supervised approaches, but the commonly used clustering strategies (Zhang et al., 2024b; Lin et al., 2025b) and Chamfer-guided ...
- **p. 2 / 1. Introduction - extractive body cue:** IterFlow is lightweight, featuring iterative flow refinement scheme and ball query-based cross-frame correlation, both tailored to the challenging radar domain. • We design two novel ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Given the high cost of high-performance LiDAR sensors, we propose a novel setting, weakly supervised cross-modal learning for 4D radar scene flow, that relies only ...
- **p. 3 / 3.1. IterFlow - extractive body cue:** To address these limitations and achieve high-accuracy flow estimation on challenging 4D radar data, we propose IterFlow, a task-specific iterative network designed to refine scene ...
- **p. 3 / 3. Method - extractive body cue:** Every radar point consists of five attributes: its 3D coordinates, radar cross-section (RCS), and relative radial velocity (RRV).
- **p. 4 / 3.1. IterFlow - extractive body cue:** Each pointwise feature φ(xi) ∈Et and φ(yi) ∈Et+1 consists of the original input 3D position and the feature dimension C.
- **p. 5 / 3.2. Instance-aware Loss Functions - extractive body cue:** To address this problem, we introduce an instance-level flow smoothness loss Lis.
- **p. 4 / 3.1. IterFlow - extractive body cue:** Pt is first warped by estimated scene flow and then used to calculate chamfer loss with Pt+1.
- **p. 4 / 3.1. IterFlow - extractive body cue:** With set abstraction in (Qi et al., 2017a;b), the ball query-based cross-frame correlation feature is then computed as: ck i = max l (MLP(concat yl∈NL ...
- **p. 5 / 3.2. Instance-aware Loss Functions - extractive body cue:** To mitigate this issue, we propose calculating the Chamfer loss exclusively between point pairs that belong to the same instance, utilizing the pointwise instance label ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | These features are fused to form the GRU input xk, and the hidden state is updated as follows: zk = σ(Conv1d([hk-1, xk], Wz)) (2) rk = σ(Conv1d([hk-1, xk], Wr)) (3) ˆhk = ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.1. IterFlow), p. 6 (3.3. Rigid Static Loss) |
| State/latent | features, fused, form, GRU, input, hidden, state, updated, follows, Conv1d, hk-1, tanh | geometry, map, object/relationship state | p. 4 (3.1. IterFlow), p. 6 (3.3. Rigid Static Loss), p. 2 (1. Introduction) |
| Output/action | R represents radar point clouds input. | point map, pose, scene graph, affordance 또는 query result | p. 6 (3.3. Rigid Static Loss), p. 2 (1. Introduction), p. 3 (3. Method) |
| Objective/outcome | Subsequently, auxiliary 2D image and odometry are used to construct three losses for optimizing the predicted flows: Ltotal = Lstat + Lic + Lis. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. IterFlow) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Given the high cost of high-performance LiDAR sensors, we propose a novel setting, weakly supervised cross-modal learning for 4D radar scene flow, that relies only ...
- **p. 3 / 3.1. IterFlow - extractive body cue:** To address these limitations and achieve high-accuracy flow estimation on challenging 4D radar data, we propose IterFlow, a task-specific iterative network designed to refine scene ...
- **p. 3 / 3. Method - extractive body cue:** Every radar point consists of five attributes: its 3D coordinates, radar cross-section (RCS), and relative radial velocity (RRV).
- **p. 4 / 3.1. IterFlow - extractive body cue:** Each pointwise feature φ(xi) ∈Et and φ(yi) ∈Et+1 consists of the original input 3D position and the feature dimension C.
- **p. 5 / 3.2. Instance-aware Loss Functions - extractive body cue:** To address this problem, we introduce an instance-level flow smoothness loss Lis.
- **p. 8 / 4.2. Ablation Studies - extractive body cue:** The experimental results in Table 3 illustrate that the addition of Lis successfully improves the prediction accuracy in both dynamic and static areas in the ...
- **p. 7 / 4.1. Main Results - extractive body cue:** When compared to LiDAR-based approaches, our method even surpasses the best fully supervised model, PVRAFT (Wei et al., 2021), achieving performance improvements across all metrics, ...
- **p. 7 / 4.1. Main Results - extractive body cue:** In particular, IterFlow yields a 34.7% performance improvement on the EPE metric, while increasing AccS and AccR by 13.6% and 21.4%, respectively.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.2. Ablation Studies), p. 7 (4.1. Main Results) |
| Embodiment/environment | Since the VoD dataset does not provide ready-made scene flow ground truth, we adopt the commonly used preprocessing methods to generate scene flow labels from annotated 3D tracking boxes for the training ... | hardware/simulator version and reset protocol | p. 6 (4. Experiments), p. 6 (4. Experiments) |
| Dataset/benchmark | Note that fully-supervised methods are trained with the radar scene flow ground truth derived from the annotated 3D tracking boxes provided by the dataset, and CMFlow (Ding et al., 2023) is trained ... | role, split, size and leakage | p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.1. Main Results), p. 7 (4.1. Main Results) |
| Metric | The experimental results in Table 3 illustrate that the addition of Lis successfully improves the prediction accuracy in both dynamic and static areas in the scene, achieving a performance improvement of 16.3% ... | definition, denominator, direction and uncertainty | p. 8 (4.2. Ablation Studies), p. 7 (4.1. Main Results), p. 6 (4. Experiments) |
| Baseline/ablation | For a fair comparison with the baselines, we use their official loss configuration and hyperparameter settings for network retraining on the VoD radar scene flow dataset. | fair input/data/compute/action matching | p. 6 (4. Experiments), p. 6 (4.1. Main Results), p. 7 (4.1. Main Results) |

## Explicit Limitations and Failure Boundary

- **p. 16 / Figure/Table caption - extractive body cue:** Figure 8. Visualization of failure cases on VoD validation set. Each row displays a driving scenario and regions with large scene flow estimation errors are ...
- **p. 8 / 4.2. Ablation Studies - extractive body cue:** The advantage of Lic over Lsc is twofold: on one hand, Lic only calculates the chamfer distance between points within the same instance across frames, ...
- **p. 6 / 4. Experiments - extractive body cue:** Since the VoD dataset does not provide ready-made scene flow ground truth, we adopt the commonly used preprocessing methods to generate scene flow labels from ...
- **p. 5 / 3.2. Instance-aware Loss Functions - extractive body cue:** The resulting enforced consistency between incorrect point pairs can significantly degrade network performance.
- **p. 7 / 4.1. Main Results - extractive body cue:** This result highlights that our ball query-based correlation operation is more robust in sparse radar scenarios than the KNN-based and voxelbased correlation modules used in ...
- **p. 8 / 4.1. Main Results - extractive body cue:** Finally, comparing rows 5 and 7, we find that using LiDARbased losses in (Wu et al., 2020) to train our IterFlow results in dramatic performance ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 A straightforward attempt is to extend LiDAR-based self-supervised approaches, but the commonly used clustering strategies (Zhang et al., 2024b; Lin et al., 2025b) and Chamfer-guided (Wu et al., 2020; Mittal et al., ...를 문제로 두고, Given the high cost of high-performance LiDAR sensors, we propose a novel setting, weakly supervised cross-modal learning for 4D radar scene flow, that relies only on RGB images and odometry, which are ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. IterFlow), p. 4 (3.1. IterFlow), p. 3 (3.1. IterFlow), p. 5 (3.2. Instance-aware Loss Functions) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
