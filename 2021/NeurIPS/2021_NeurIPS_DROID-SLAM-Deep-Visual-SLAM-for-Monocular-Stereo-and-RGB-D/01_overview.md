# DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2108.10869.
> PDF retrieval source: https://arxiv.org/pdf/2108.10869. Reading tracker status/evidence was not changed.

- Year/Venue: 2021 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: CORE
- Tags: SLAM, RGB-D, geometry
- Aliases: DROID-SLAM
- Official paper: https://arxiv.org/abs/2108.10869
- Full-text retrieval: https://arxiv.org/pdf/2108.10869
- Code/Project: https://github.com/princeton-vl/DROID-SLAM
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Despite significant progress, current SLAM systems lack the robustness demanded for many real-world applications.를 문제로 두고, In this work we introduce DROID-SLAM, a new SLAM system based on deep learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce DROID-SLAM, a new deep learning based SLAM system.
- **p. 1 / Abstract - extractive body cue:** DROIDSLAM consists of recurrent iterative updates of camera pose and pixelwise depth through a Dense Bundle Adjustment layer.
- **p. 1 / Abstract - extractive body cue:** DROID-SLAM is accurate, achieving large improvements over prior work, and robust, suffering from substantially fewer catastrophic failures.
- **p. 1 / Abstract - extractive body cue:** Despite training on monocular video, it can leverage stereo or RGB-D video to achieve improved performance at test time.
- **p. 1 / 1 Introduction - extractive body cue:** Simultaneous Localization and Mapping (SLAM) aims to (1) build a map of the environment and (2) localize the agent within the environment.
- **p. 1 / 1 Introduction - extractive body cue:** Despite significant progress, current SLAM systems lack the robustness demanded for many real-world applications.
- **p. 2 / 1 Introduction - extractive body cue:** On TUM-RGBD [44], we reduce error by 83% among the methods with zero failures. • High Robustness: We have substantially fewer catastrophic failures than prior ...

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** In this work we introduce DROID-SLAM, a new SLAM system based on deep learning.
- **p. 2 / 1 Introduction - extractive body cue:** Specifically, it consists of recurrent iterative updates, building upon RAFT [49] for optical flow but introducing two key innovations.
- **p. 4 / 3 Approach - extractive body cue:** The network consists of 6 residual blocks and 3 downsampling layers, producing dense feature maps at 1/8 the input image resolution.
- **p. 6 / 3 Approach - extractive body cue:** Constructing training video Each training example consists of a 7-frame video sequence.
- **p. 2 / 1 Introduction - extractive body cue:** This DBA layer leverages geometric constraints, improves accuracy and robustness, and enables a monocular system to handle stereo or RGB-D input without retraining.
- **p. 7 / 3 Approach - extractive body cue:** At inference time, we use a custom CUDA kernel which takes advantage of the block-sparse structure of the problem, then perform sparse Cholesky decomposition on ...
- **p. 4 / 3 Approach - extractive body cue:** Like RAFT[49], we use two separate networks: a feature network and a context network.
- **p. 5 / 3 Approach - extractive body cue:** We denote the corrected correspondence as p∗ ij = rij + pij We then pool the hidden state over all features which share the same ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Feature Extraction Each of the input images are processed by a feature extraction network. | camera/depth stream, pose, map와 language goal | p. 4 (3 Approach), p. 5 (3 Approach) |
| State/latent | Feature, Extraction, input, images, processed, network, extract, global, context, averaging, hidden, state | robot pose, free-space/semantic map와 local goal | p. 4 (3 Approach), p. 5 (3 Approach), p. 5 (3 Approach) |
| Output/action | We extract global context by averaging the hidden state across the spatial dimensions of the image and use this feature vector as additional input to the GRU. | collision-free trajectory 또는 velocity command | p. 5 (3 Approach), p. 5 (3 Approach), p. 3 (3 Approach) |
| Objective/outcome | We define the cost function over the entire frame graph E(G′, d′) = X (i,j)∈E | goal reach, safety, localization error와 replanning latency | p. 5 (3 Approach), p. 7 (3 Approach), p. 3 (3 Approach) |

## Main Claims and Actual Contribution

- **p. 1 / 1 Introduction - extractive body cue:** In this work we introduce DROID-SLAM, a new SLAM system based on deep learning.
- **p. 2 / 1 Introduction - extractive body cue:** Specifically, it consists of recurrent iterative updates, building upon RAFT [49] for optical flow but introducing two key innovations.
- **p. 4 / 3 Approach - extractive body cue:** The network consists of 6 residual blocks and 3 downsampling layers, producing dense feature maps at 1/8 the input image resolution.
- **p. 6 / 3 Approach - extractive body cue:** Constructing training video Each training example consists of a 7-frame video sequence.
- **p. 2 / 1 Introduction - extractive body cue:** This DBA layer leverages geometric constraints, improves accuracy and robustness, and enables a monocular system to handle stereo or RGB-D input without retraining.
- **p. 8 / 4 Experiments - extractive body cue:** On most sequences, we outperform existing methods by an order-of-magnitude and achieve 8x lower average error than TartanVO [54] and 20x lower than DeepV2D [48].
- **p. 8 / 4 Experiments - extractive body cue:** In the monocular setting, we achieve an average ATE of 2.2cm, reducing error by 82% among methods with zero failures, and by 43% over ORB-SLAM3 ...
- **p. 9 / 4 Experiments - extractive body cue:** Method AUC (train) AUC (test) BundleFusion [11] 84.10 33.84 ElasticFusion [57] 89.06 34.02 RFusion [56] 17.37 51.94 DVO-SLAM [20] 193.89 71.83 ORB-SLAM2 [32] 156.10 104.28 ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Embodiment/environment | TUM-RGBD [44] The RGBD dataset consists of indoor scenes captured with handheld camera. | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Dataset/benchmark | Method AUC (train) AUC (test) BundleFusion [11] 84.10 33.84 ElasticFusion [57] 89.06 34.02 RFusion [56] 17.37 51.94 DVO-SLAM [20] 193.89 71.83 ORB-SLAM2 [32] 156.10 104.28 BAD-SLAM [42] 280.05 153.47 Ours 340.42 207.79 ... | role, split, size and leakage | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Metric | Following prior work, we evaluate the accuracy of the camera trajectory [31, 15, 42], primarily using Absolute Trajectory Error (ATE) [44]. | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Baseline/ablation | We retrain DeepV2D [48] on TartanAir as a baseline. | fair input/data/compute/action matching | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 13 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4 Experiments - extractive body cue:** 1 demonstrates both the robustness of our method (no catastrophic failures) and accuracy (very low drift).
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: DROID-SLAM can operate on monocular, stereo, and RGB-D video. It builds a dense 3D map of the environment while simultaneously localizing the camera ...
- **p. 8 / 4 Experiments - extractive body cue:** In the monocular setting, we achieve an average ATE of 2.2cm, reducing error by 82% among methods with zero failures, and by 43% over ORB-SLAM3 ...
- **p. 9 / 4 Experiments - extractive body cue:** While memory and resource requirements are currently the biggest limitation of our system, we believe these can be drastically reduced by culling redundant computation and ...
- **p. 9 / 5 Conclusion - extractive body cue:** DROID-SLAM is accurate, robust, and versatile and can be used on monocular, stereo, and RGB-D video.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Despite significant progress, current SLAM systems lack the robustness demanded for many real-world applications.를 문제로 두고, In this work we introduce DROID-SLAM, a new SLAM system based on deep learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 7 (3 Approach), p. 4 (3 Approach) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
