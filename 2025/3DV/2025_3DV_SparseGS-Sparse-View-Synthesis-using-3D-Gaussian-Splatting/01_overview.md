# SparseGS: Sparse View Synthesis using 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/.
> PDF retrieval source: https://openreview.net/attachment?id=O9GMl5UJbe&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D Vision
- Official paper: https://3dvconf.github.io/2025/accepted-papers/
- Full-text retrieval: https://openreview.net/attachment?id=O9GMl5UJbe&name=pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The challenge of learning 3D representations from 2D images has been a longstanding area of interest, but achieving a balance between efficiency and fidelity remains a persistent challenge.를 문제로 두고, Our method consists of three key components designed to function cohesively to improve view consistency and depth accuracy in novel view synthesis: a depth correlation loss, an Unseen Viewpoint Regularization (UVR) module, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian Splatting (3DGS) has recently enabled real-time rendering of unbounded 3D scenes for novel view synthesis.
- **p. 1 / Abstract - extractive body cue:** However, this technique requires dense training views to accurately reconstruct 3D geometry.
- **p. 1 / Abstract - extractive body cue:** A limited number of input views will significantly degrade reconstruction quality, resulting in artifacts such as "floaters" and "background collapse" at unseen viewpoints.
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce SparseGS, an efficient training pipeline designed to address the limitations of 3DGS in scenarios with sparse training views.
- **p. 1 / Abstract - extractive body cue:** SparseGS incorporates depth priors, novel depth rendering techniques, and a pruning heuristic to mitigate floater artifacts, alongside an Unseen Viewpoint Regularization module to alleviate background ...
- **p. 1 / 1. Introduction - extractive body cue:** The challenge of learning 3D representations from 2D images has been a longstanding area of interest, but achieving a balance between efficiency and fidelity remains ...
- **p. 1 / 1. Introduction - extractive body cue:** These issues are further exacerbated when the training set lacks substantial scene coverage, such as in multi-view unbounded scenes [2] (referred as 360-degree scenes in ...

## Core Idea

- **p. 3 / 3. Methods - extractive body cue:** Our method consists of three key components designed to function cohesively to improve view consistency and depth accuracy in novel view synthesis: a depth correlation ...
- **p. 2 / 1. Introduction - extractive body cue:** Next, we introduce a module designed to tackle background collapse by leveraging a 2D generative diffusion prior [16, 26] and depth warping [22, 44].
- **p. 2 / 1. Introduction - extractive body cue:** We propose a novel framework, SparseGS, for training coherent and robust 3D Gaussian representations from limited inputs, outperforming SOTA methods in sparse view synthesis.
- **p. 5 / 3.3. Unseen Viewpoints Regularization (UVR) - extractive body cue:** In this section, we propose two regularization methods to improve reconstruction from novel viewpoints: 1).
- **p. 6 / 3.4. Advanced Floater Pruning - extractive body cue:** Therefore, we propose a novel pruning operator to remove the Gaussians at false modes at the end of training.
- **p. 3 / 3. Methods - extractive body cue:** Then, we dissect the UVR module into two parts: a Score Distillation Sampling (SDS) loss and a depth warping loss, which are designed for regularizing ...
- **p. 5 / 3.3. Unseen Viewpoints Regularization (UVR) - extractive body cue:** Then, the renderings at the sampled viewpoints are encoded and decoded by the diffusion model, where the predicted noise is then supervised with our SDS ...
- **p. 5 / 3.3. Unseen Viewpoints Regularization (UVR) - extractive body cue:** Inspired by recent diffusion models [5, 9, 25, 26, 31, 45] and Score Distillation Sampling (SDS) [38] for zero-shot 3D reconstruction [6, 15, 16, 36], ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Combined, our pipeline achieves state-of-the-art (SOTA) performance in sparse-input novel view synthesis (NVS) problems, not only on forward-facing datasets but also on 360-degree unbounded scenes, a scenario that most current few-shot ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 6 (3.3. Unseen Viewpoints Regularization (UVR)) |
| State/latent | Combined, pipeline, achieves, state-of-the-art, SOTA, performance, sparse-input, novel, view, synthesis, NVS, problems | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 6 (3.3. Unseen Viewpoints Regularization (UVR)), p. 1 (1. Introduction) |
| Output/action | Mathematically, we define our image re-projection as follows: For pixel pi(xi, yi) in training image Isrc, the warping to the corresponding pixel pj(xj, yj) at an unseen viewpoint Itrg can be formulated ... | point map, pose, scene graph, affordance 또는 query result | p. 6 (3.3. Unseen Viewpoints Regularization (UVR)), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | Because the softmax depth loss is a soft constraint, there may exist regions where dmode and dalpha do not align. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3.4. Advanced Floater Pruning), p. 4 (3.1. Mode-selection & Softmax-scaling Depth Ren), p. 3 (3. Methods) |

## Main Claims and Actual Contribution

- **p. 3 / 3. Methods - extractive body cue:** Our method consists of three key components designed to function cohesively to improve view consistency and depth accuracy in novel view synthesis: a depth correlation ...
- **p. 2 / 1. Introduction - extractive body cue:** Next, we introduce a module designed to tackle background collapse by leveraging a 2D generative diffusion prior [16, 26] and depth warping [22, 44].
- **p. 2 / 1. Introduction - extractive body cue:** We propose a novel framework, SparseGS, for training coherent and robust 3D Gaussian representations from limited inputs, outperforming SOTA methods in sparse view synthesis.
- **p. 5 / 3.3. Unseen Viewpoints Regularization (UVR) - extractive body cue:** In this section, we propose two regularization methods to improve reconstruction from novel viewpoints: 1).
- **p. 6 / 3.4. Advanced Floater Pruning - extractive body cue:** Therefore, we propose a novel pruning operator to remove the Gaussians at false modes at the end of training.
- **p. 7 / 4.2. Comparison - extractive body cue:** 1, SparseGS significantly outperforms previous NeRF-based methods and concurrent works, FSGS and DNGaussian, in both 12-view and 24-view settings.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Our proposed pipeline incorporates depth priors, diffusion constraints, and a floater pruning technique to improve few- shot novel view synthesis performance. During training, ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The quality of 3DGS [12] degrades as the number of input views decreases, particularly in unbounded scenes. SparseGS significantly improves novel view synthesis ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (4.2. Comparison), p. 3 (Figure/Table caption) |
| Embodiment/environment | The LLFF dataset comprises eight complex forward-facing real scenes, while the DTU dataset includes object-centric scenes with foreground masks. | hardware/simulator version and reset protocol | p. 7 (4.2. Comparison), p. 6 (4.1. Experimental Settings) |
| Dataset/benchmark | We use the Mip-NeRF360 dataset to evaluate 3D reconstruction of unbounded 360° scenes. | role, split, size and leakage | p. 7 (4.2. Comparison), p. 6 (4.1. Experimental Settings), p. 7 (4.2. Comparison), p. 6 (4.1. Experimental Settings) |
| Metric | Figure 2. Our proposed pipeline incorporates depth priors, diffusion constraints, and a floater pruning technique to improve few- shot novel view synthesis performance. During training, we render the softmax depth and use ... | definition, denominator, direction and uncertainty | p. 3 (Figure/Table caption), p. 7 (4.2. Comparison), p. 7 (4.2. Comparison) |
| Baseline/ablation | 1, SparseGS significantly outperforms previous NeRF-based methods and concurrent works, FSGS and DNGaussian, in both 12-view and 24-view settings. | fair input/data/compute/action matching | p. 7 (4.2. Comparison), p. 7 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Comparison - extractive body cue:** This limitation actually prompted the introduction of positional encoding [20, 37].
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** In contrast, FSGS excels in preserving fine details due to its densification technique but fails to reconstruct background geometry.
- **p. 8 / 5. Conclusion - extractive body cue:** In regions with little coverage by input views, we leverage Score Distillation Sampling (SDS) and Depth Warping to reduce collapse in geometry and noise in ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The quality of 3DGS [12] degrades as the number of input views decreases, particularly in unbounded scenes. SparseGS significantly improves novel view synthesis ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Illustration of benefits from the SDS loss. While the scene structure is well preserved, the high-frequency noise in both geometry and texture is ...
- **p. 7 / 4.2. Comparison - extractive body cue:** We also provide evaluations on the forward-facing datasets (LLFF and DTU) to demonstrate robustness of our pipeline.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The challenge of learning 3D representations from 2D images has been a longstanding area of interest, but achieving a balance between efficiency and fidelity remains a persistent challenge.를 문제로 두고, Our method consists of three key components designed to function cohesively to improve view consistency and depth accuracy in novel view synthesis: a depth correlation loss, an Unseen Viewpoint Regularization (UVR) module, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methods), p. 5 (3.3. Unseen Viewpoints Regularization (UVR)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
