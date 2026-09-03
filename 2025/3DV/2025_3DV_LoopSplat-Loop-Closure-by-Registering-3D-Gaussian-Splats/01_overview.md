# LoopSplat: Loop Closure by Registering 3D Gaussian Splats

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/.
> PDF retrieval source: https://openreview.net/attachment?id=0CNSbBa85A&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D Vision
- Official paper: https://3dvconf.github.io/2025/accepted-papers/
- Full-text retrieval: https://openreview.net/attachment?id=0CNSbBa85A&name=pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To address limitations of current systems, we seek a coupled SLAM system that avoids saving all mapped input frames and is able to extract loop constraints directly from the dense map, without ...를 문제로 두고, We introduce LoopSplat, a coupled RGB-D SLAM system based on Gaussian Splatting, featuring a novel loop closure module.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Simultaneous Localization and Mapping (SLAM) based on 3D Gaussian Splats (3DGS) has recently shown promise towards more accurate, dense 3D scene maps.
- **p. 1 / Abstract - extractive body cue:** However, existing 3DGS-based methods fail to address the global consistency of the scene via loop closure and/or global bundle adjustment.
- **p. 1 / Abstract - extractive body cue:** To this end, we propose LoopSplat, which takes RGB-D images as input and performs dense mapping with 3DGS submaps and frame-to-model tracking.
- **p. 1 / Abstract - extractive body cue:** LoopSplat triggers loop closure online and computes relative loop edge constraints between submaps directly via 3DGS registration, leading to improvements in efficiency and accuracy over ...
- **p. 1 / Abstract - extractive body cue:** It uses a robust pose graph optimization formulation and rigidly aligns the submaps to achieve global consistency.
- **p. 2 / 1. Introduction - extractive body cue:** To address limitations of current systems, we seek a coupled SLAM system that avoids saving all mapped input frames and is able to extract loop ...
- **p. 1 / 1. Introduction - extractive body cue:** On the other hand, all coupled 3DGS SLAM methods lack strategies for achieving global consistency on the map and the poses, which leads to an ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We introduce LoopSplat, a coupled RGB-D SLAM system based on Gaussian Splatting, featuring a novel loop closure module.
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose a dense RGB-D SLAM system that uses submaps of 3D Gaussians for local frame-to-model tracking and dense mapping and is ...
- **p. 6 / 4.1. Tracking - extractive body cue:** We note that the ground truth poses in ScanNet, derived from BundleFusion [18], appear to have limited accuracy: visual inspection suggests that our method achieves ...
- **p. 7 / 4.2. Reconstruction - extractive body cue:** Our method recovers more geometric details (e.g., on the chairs).
- **p. 7 / 4.3. Rendering - extractive body cue:** It is noteworthy that both the NeRF-based LoopySLAM and Point-SLAM methods require ground truth depth input to guide the depth rendering, whereas our method, leveraging ...
- **p. 6 / Method - extractive body cue:** We compare LoopSplat with state-of-theart coupled RGB-D SLAM methods, categorized into two groups based on the underlying scene representation: (i) Neural implicit fields: MIPS-Fusion [77], ...
- **p. 6 / Method - extractive body cue:** Tracking accuracy is measured by the root mean square absolute trajectory error (ATE RMSE) [73].
- **p. 7 / 4.3. Rendering - extractive body cue:** 6 reports our rendering performance on training views.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It is noteworthy that both the NeRF-based LoopySLAM and Point-SLAM methods require ground truth depth input to guide the depth rendering, whereas our method, leveraging 3DGS, only requires estimated camera poses at ... | RGB-D, image set, point cloud, depth와 camera pose | p. 7 (4.3. Rendering), p. 6 (Method) |
| State/latent | noteworthy, NeRF-based, LoopySLAM, Point-SLAM, methods, require, ground, truth, depth, input, guide, rendering | geometry, map, object/relationship state | p. 7 (4.3. Rendering), p. 6 (Method), p. 7 (4.2. Reconstruction) |
| Output/action | Rendering quality is evaluated by comparing full-resolution rendered images to input training views in terms of PSNR, SSIM [84], and LPIPS [100]. | point map, pose, scene graph, affordance 또는 query result | p. 6 (Method), p. 7 (4.2. Reconstruction), p. 2 (1. Introduction) |
| Objective/outcome | Runtime is reported as average per-frame tracking and map optimization time, as well as loop edge registration runtime. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (Method), p. 7 (4.3. Rendering), p. 7 (4.4. Memory and Runtime Analysis) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We introduce LoopSplat, a coupled RGB-D SLAM system based on Gaussian Splatting, featuring a novel loop closure module.
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose a dense RGB-D SLAM system that uses submaps of 3D Gaussians for local frame-to-model tracking and dense mapping and is ...
- **p. 6 / 4.1. Tracking - extractive body cue:** We note that the ground truth poses in ScanNet, derived from BundleFusion [18], appear to have limited accuracy: visual inspection suggests that our method achieves ...
- **p. 7 / 4.2. Reconstruction - extractive body cue:** Our method recovers more geometric details (e.g., on the chairs).
- **p. 7 / 4.3. Rendering - extractive body cue:** It is noteworthy that both the NeRF-based LoopySLAM and Point-SLAM methods require ground truth depth input to guide the depth rendering, whereas our method, leveraging ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Tracking Performance on ScanNet++ [93] (ATE RMSE ↓[cm]). LoopSplat achieves the highest accuracy and can robustly deal with the large camera motions in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 6. Rendering Performance on 3 Datasets. LoopSplat achieves competitive results on synthetic and real-world datasets. Gray indicates evaluation on submaps instead of a global ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Tracking Performance on ScanNet [17]. LoopSplat outperforms 3DGS-based systems by a large margin and is on par with the state-of-the-art baselines. real-world datasets, ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | Additionally, we require the least GPU memory to process a room-sized scene. | hardware/simulator version and reset protocol | p. 7 (4.4. Memory and Runtime Analysis) |
| Dataset/benchmark | Additionally, we require the least GPU memory to process a room-sized scene. | role, split, size and leakage | p. 7 (4.4. Memory and Runtime Analysis) |
| Metric | Table 2. Tracking Performance on ScanNet++ [93] (ATE RMSE ↓[cm]). LoopSplat achieves the highest accuracy and can robustly deal with the large camera motions in the sequence. computed directly from the Gaussian ... | definition, denominator, direction and uncertainty | p. 5 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Baseline/ablation | Table 3. Tracking Performance on ScanNet [17]. LoopSplat outperforms 3DGS-based systems by a large margin and is on par with the state-of-the-art baselines. real-world datasets, with a dedicated ablation study for loop ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 5 (4. Experiments), p. 7 (4.4. Memory and Runtime Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.4. Memory and Runtime Analysis - extractive body cue:** While our per-frame tracking and map optimization time falls behind the fastest baselines, our Gaussian Splattingbased registration significantly shortens the loop edge registration time compared ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Reconstruction Performance on Replica [70]. Loop- Splat obtains the second-best F1-score, falling behind only to Loopy-SLAM. It is noteworthy that both the NeRF-based ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Comparison of Mesh Reconstruction on two ScanNet [17] scenes. For the first scene, we highlight shape details with normal shading, showing that LoopSplat ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Dense Reconstruction on ScanNet [17] scene0054. LoopSplat demonstrates superior performance in geometric accuracy, robust tracking, and high-quality re-rendering. This is enabled by our ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Tracking Performance on ScanNet++ [93] (ATE RMSE ↓[cm]). LoopSplat achieves the highest accuracy and can robustly deal with the large camera motions in ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To address limitations of current systems, we seek a coupled SLAM system that avoids saving all mapped input frames and is able to extract loop constraints directly from the dense map, without ...를 문제로 두고, We introduce LoopSplat, a coupled RGB-D SLAM system based on Gaussian Splatting, featuring a novel loop closure module.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 6 (Method), p. 6 (Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
