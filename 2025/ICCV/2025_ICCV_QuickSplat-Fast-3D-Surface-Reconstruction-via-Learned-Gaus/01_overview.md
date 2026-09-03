# QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Liu_QuickSplat_Fast_3D_Surface_Reconstruction_via_Learned_Gaussian_Initialization_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_QuickSplat_Fast_3D_Surface_Reconstruction_via_Learned_Gaussian_Initialization_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Liu_QuickSplat_Fast_3D_Surface_Reconstruction_via_Learned_Gaussian_Initialization_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_QuickSplat_Fast_3D_Surface_Reconstruction_via_Learned_Gaussian_Initialization_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In particular, achieving both high fidelity as well as efficient and fast reconstruction for large scenes remains a difficult problem.를 문제로 두고, To summarize, our contributions are: • We propose a learned, generalized initializer network, that leverages scene priors to create effective Gaussian initializations for more efficient and accurate 3D surface reconstruction optimizatio ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Surface reconstruction is fundamental to computer vision and graphics, enabling applications in 3D modeling, mixed reality, robotics, and more.
- **p. 1 / Abstract - extractive body cue:** Existing approaches based on volumetric rendering obtain promising results, but optimize on a per-scene basis, resulting in a slow optimization that can struggle to model ...
- **p. 1 / Abstract - extractive body cue:** We introduce QuickSplat, which learns datadriven priors to generate dense initializations for 2D gaussian splatting optimization of large-scale indoor scenes.
- **p. 1 / Abstract - extractive body cue:** This provides a strong starting point for the reconstruction, which accelerates the convergence of the optimization and improves the geometry of flat wall structures.
- **p. 1 / Abstract - extractive body cue:** We further learn to jointly estimate the densification and update of the scene parameters during each iteration; our proposed densifier network predicts new Gaussians based ...
- **p. 1 / 1. Introduction - extractive body cue:** In particular, achieving both high fidelity as well as efficient and fast reconstruction for large scenes remains a difficult problem.
- **p. 2 / 1. Introduction - extractive body cue:** Our priors also guide the optimization towards high-quality indoor-scene geometry and thus overcome limitations stemming from insufficient observations or textureless regions (e.g., floating artifacts or ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are: • We propose a learned, generalized initializer network, that leverages scene priors to create effective Gaussian initializations for more efficient ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose a novel generalized prior for 3D surface reconstruction.
- **p. 3 / 3.2. Initialization Prior - extractive body cue:** The first step in our method is to create an initialization of all Gaussians G.
- **p. 3 / 3.1. Surface Representation - extractive body cue:** We propose to predict G with neural networks instead of optimizing the primitives directly with gradient descent.
- **p. 4 / 3.3. Iterative Gaussian Optimization - extractive body cue:** To this end, we introduce another learnable component, the densifier network θD, that predicts additional voxel features in free space.
- **p. 4 / 3.3. Iterative Gaussian Optimization - extractive body cue:** Top: the densifier network predicts a pool of additional voxel features in an encoder-decoder architecture from the current Gaussians and their gradients as input.
- **p. 3 / 3.2. Initialization Prior - extractive body cue:** In contrast to SGNN, which produces sparse voxel outputs, we employ a decoder MLP to interpret the densified voxel latent features as output Gaussian primitives.
- **p. 3 / 3.2. Initialization Prior - extractive body cue:** Inspired by SGNN [14], this network comprises sparse 3D convolutions in an encoder-decoder architecture.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our method reconstructs the surface of large-scale indoor scenes from posed images as input. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (3. Method), p. 2 (1. Introduction) |
| State/latent | reconstructs, surface, large-scale, indoor, scenes, posed, images, input, learn, several, sparse, CNN-based | geometry, map, object/relationship state | p. 2 (3. Method), p. 2 (1. Introduction), p. 3 (3. Method) |
| Output/action | We learn several sparse 3D CNN-based networks that jointly produce Gaussian parameters from the input posed multi-view images. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 3 (3. Method), p. 5 (3.3. Iterative Gaussian Optimization) |
| Objective/outcome | Initializer SfM points New GS Densifier Optimizer Gradients Rendering loss Update Gaussian parameters iteratively Gaussians Gradients Updates Concat new GS with Before After Figure 2. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3. Method), p. 5 (3.3. Iterative Gaussian Optimization), p. 4 (3.3. Iterative Gaussian Optimization) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are: • We propose a learned, generalized initializer network, that leverages scene priors to create effective Gaussian initializations for more efficient ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose a novel generalized prior for 3D surface reconstruction.
- **p. 3 / 3.2. Initialization Prior - extractive body cue:** The first step in our method is to create an initialization of all Gaussians G.
- **p. 3 / 3.1. Surface Representation - extractive body cue:** We propose to predict G with neural networks instead of optimizing the primitives directly with gradient descent.
- **p. 4 / 3.3. Iterative Gaussian Optimization - extractive body cue:** To this end, we introduce another learnable component, the densifier network θD, that predicts additional voxel features in free space.
- **p. 5 / 4. Experiments - extractive body cue:** PGSR renders unbiased depth maps from flattened 3D Gaussians and introduces both single-view and multi-view regularization losses to improve geometric reconstruction.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. In general, our proposed QuickSplat achieves better performance: it reconstructs scenes with cleaner structures and flat surfaces that matches the ground truth compared ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Ablation study. We ablate the impact of our learned priors for initialization, densification, and optimization updates. Only using our optimizer network does not ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (4. Experiments), p. 6 (Figure/Table caption) |
| Embodiment/environment | We evaluate our method on 20 unseen test scenes and report averaged metrics. | hardware/simulator version and reset protocol | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Dataset/benchmark | We evaluate our method on 20 unseen test scenes and report averaged metrics. | role, split, size and leakage | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Metric | We calculate the absolute error, as well as the accuracy within different thresholds (2cm, 5cm, 10cm). | definition, denominator, direction and uncertainty | p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (Figure/Table caption) |
| Baseline/ablation | Fig. 4. In general, our proposed QuickSplat achieves better performance: it reconstructs scenes with cleaner structures and flat surfaces that matches the ground truth compared to the baselines while maintaining similar level ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.3. Limitations - extractive body cue:** Second, we assume static environments and therefore cannot reconstruct dynamic scenes (e.g., people walking inside of a room).
- **p. 8 / 4.3. Limitations - extractive body cue:** Lastly, even though we significantly reduce optimization runtime, our method does not yet reconstruct in real-time, but could be integrated with recent SLAM-based approaches [26, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Ablation study. We ablate the impact of our learned priors for initialization, densification, and optimization updates. Only using our optimizer network does not ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In particular, achieving both high fidelity as well as efficient and fast reconstruction for large scenes remains a difficult problem.를 문제로 두고, To summarize, our contributions are: • We propose a learned, generalized initializer network, that leverages scene priors to create effective Gaussian initializations for more efficient and accurate 3D surface reconstruction optimizatio ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.3. Iterative Gaussian Optimization), p. 3 (3.2. Initialization Prior) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
