# FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/.
> PDF retrieval source: https://openreview.net/attachment?id=QI6HrBseVF&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: geometry, depth, 3D Vision
- Official paper: https://3dvconf.github.io/2025/accepted-papers/
- Full-text retrieval: https://openreview.net/attachment?id=QI6HrBseVF&name=pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, conventional SfM has a major limitation: it is not differentiable with respect to its free variables (camera poses, camera intrinsics, and perpixel depths).를 문제로 두고, In this paper, we present FlowMap, a differentiable and surprisingly simple camera and geometry estimation method whose outputs enable photorealistic novel view synthesis.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Reconstructing a 3D scene from video is one of the most fundamental problems in vision and has been studied for over five decades.
- **p. 1 / 1 Introduction - extractive body cue:** Today, essentially all state-ofthe-art approaches are built on top of Structure-from-Motion (SfM) methods like COLMAP [58].
- **p. 1 / 1 Introduction - extractive body cue:** These approaches extract sparse correspondences across frames, match them, discard outliers, and then optimize the correspondences' 3D positions alongside the camera parameters by minimizing reprojection ...
- **p. 1 / 1 Introduction - extractive body cue:** This framework has delivered excellent results which underlie many presentday vision applications, and so it is unsurprising that SfM systems have remained largely unchanged in ...
- **p. 1 / 1 Introduction - extractive body cue:** However, conventional SfM has a major limitation: it is not differentiable with respect to its free variables (camera poses, camera intrinsics, and perpixel depths).
- **p. 1 / 1 Introduction - extractive body cue:** This means that SfM acts as an isolated pre-processing step that cannot be embedded into end-to-end deep learning pipelines.
- **p. 2 / 1 Introduction - extractive body cue:** Unlike prior attempts at gradient-based optimization of cameras and 3D geometry [2, 35, 73], we do not treat depth, intrinsics, and camera poses as free ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we present FlowMap, a differentiable and surprisingly simple camera and geometry estimation method whose outputs enable photorealistic novel view synthesis.
- **p. 2 / 1 Introduction - extractive body cue:** We show that this uniquely enables high-quality SfM via gradient descent while making FlowMap compatible with standard deep-learning pipelines.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We empirically show that camera parameters and dense depth recovered by our method enable photo-realistic novel view synthesis on 360◦trajectories using Gaussian Splatting.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Our method not only far outperforms prior gradient-descent based bundle adjustment methods, but surprisingly performs on par with COLMAP, the state-of-the-art SfM method, on the ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Alongside the use of point tracks to encourage long-term geometric consistency, we introduce differentiable re-parameterizations of depth, intrinsics, and pose that are amenable to first-order ...
- **p. 2 / 1 Introduction - extractive body cue:** Rather, we introduce differentiable feed-forward estimates of each one: depth is parameterized via a neural network, pose is parameterized as the solution to a least-squares ...
- **p. 2 / 1 Introduction - extractive body cue:** In other words, FlowMap solves SfM by learning the depth network's parameters; camera poses and intrinsics are computed via analytical feed-forward modules without free parameters ...
- **p. 3 / 1 Introduction - extractive body cue:** Gaussian Splats obtained from FlowMap reconstructions far outperform the state-of-the-art gradient-based bundle-adjustment method, NoPe-NeRF [2], and those obtained using the SLAM algorithm DROIDSLAM [67], even ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 1: We present FlowMap, an end-to-end differentiable method that recovers poses, intrinsics, and depth maps of an input video. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | present, FlowMap, end-to-end, differentiable, recovers, poses, intrinsics, depth, maps, input, video, Unlike | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)) |
| Output/action | Unlike conventional SfM, which outputs sparse 3D points that are each constrained by several views, FlowMap outputs dense per-frame depth estimates. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)) |
| Objective/outcome | Our method performs per-video gradient-descent minimization of a simple least-squares objective that compares the optical flow induced by depth, intrinsics, and poses against correspondences obtained via off-the-shelf optical flow and p ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (Body text (section not recovered)), p. 2 (1 Introduction), p. 1 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we present FlowMap, a differentiable and surprisingly simple camera and geometry estimation method whose outputs enable photorealistic novel view synthesis.
- **p. 2 / 1 Introduction - extractive body cue:** We show that this uniquely enables high-quality SfM via gradient descent while making FlowMap compatible with standard deep-learning pipelines.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We empirically show that camera parameters and dense depth recovered by our method enable photo-realistic novel view synthesis on 360◦trajectories using Gaussian Splatting.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Our method not only far outperforms prior gradient-descent based bundle adjustment methods, but surprisingly performs on par with COLMAP, the state-of-the-art SfM method, on the ...
- **p. 11 / 6 Results - extractive body cue:** Quantitatively, FlowMap performs slightly better than COLMAP SfM and significantly outperforms DROID-SLAM and NoPE-NeRF.
- **p. 13 / 6 Results - extractive body cue:** 7 Ablations and Analysis We perform ablations to answer the following questions: - Question 1: Are FlowMap's reparameterizations of depth, pose, and intrinsics necessary, or ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 10: Effects of pretraining. While a randomly initialized FlowMap network often provides accurate poses after optimization, pre-training leads to faster convergence and slightly improved ...
- **p. 13 / 6 Results - extractive body cue:** We find that free-variable variants of FlowMap produce significantly worse reconstruction results and converge much more slowly, confirming that FlowMap's reparameterizations are crucial.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 11 (6 Results), p. 13 (6 Results) |
| Embodiment/environment | We benchmark FlowMap via the downstream task of 3D Gaussian reconstruction [29]. | hardware/simulator version and reset protocol | p. 10 (6 Results), p. 14 (6 Results) |
| Dataset/benchmark | We benchmark FlowMap against several baselines. | role, split, size and leakage | p. 10 (6 Results), p. 14 (6 Results), p. 10 (6 Results), p. 11 (6 Results) |
| Metric | Fig. 10: Effects of pretraining. While a randomly initialized FlowMap network often provides accurate poses after optimization, pre-training leads to faster convergence and slightly improved poses. Here we plot depth estimates at ... | definition, denominator, direction and uncertainty | p. 14 (Figure/Table caption), p. 12 (6 Results), p. 12 (6 Results) |
| Baseline/ablation | Table 1: Camera parameter and geometry intializations from FlowMap produce 3D Gaussian reconstruction results that far outperform prior gradient-based baselines and are generally on par with those produced by COLMAP. Methods marked ... | fair input/data/compute/action matching | p. 10 (Figure/Table caption), p. 10 (6 Results), p. 11 (6 Results) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 8 Discussion - extractive body cue:** FlowMap has several limitations that suggest exciting directions for future work.
- **p. 13 / 6 Results - extractive body cue:** However, on about 20 percent of scenes, this approach falls into a local minimum and reconstruction fails catastrophically.
- **p. 12 / 6 Results - extractive body cue:** DROID-SLAM* COLMAP Ours ATE Failure Fig.
- **p. 12 / 6 Results - extractive body cue:** We note that COLMAP failed to estimate poses for 36 scenes, possibly because we ran it at a sparser frame rate to be consistent with ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Camera parameter and geometry intializations from FlowMap produce 3D Gaussian reconstruction results that far outperform prior gradient-based baselines and are generally on par ...
- **p. 14 / 8 Discussion - extractive body cue:** Second, we mainly analyze FlowMap in the setting of per-scene optimization, where our results demonstrate that the gradients provided by FlowMap's formulation are robustly lead ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, conventional SfM has a major limitation: it is not differentiable with respect to its free variables (camera poses, camera intrinsics, and perpixel depths).를 문제로 두고, In this paper, we present FlowMap, a differentiable and surprisingly simple camera and geometry estimation method whose outputs enable photorealistic novel view synthesis.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 2 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
