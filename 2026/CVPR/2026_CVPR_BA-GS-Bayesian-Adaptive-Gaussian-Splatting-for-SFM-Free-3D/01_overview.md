# BA-GS: Bayesian Adaptive Gaussian Splatting for SFM-Free 3D Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ma_BA-GS_Bayesian_Adaptive_Gaussian_Splatting_for_SFM-Free_3D_Reconstruction_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_BA-GS_Bayesian_Adaptive_Gaussian_Splatting_for_SFM-Free_3D_Reconstruction_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Ma_BA-GS_Bayesian_Adaptive_Gaussian_Splatting_for_SFM-Free_3D_Reconstruction_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_BA-GS_Bayesian_Adaptive_Gaussian_Splatting_for_SFM-Free_3D_Reconstruction_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Although these approaches partially alleviate the challenges of sparse-view reconstruction such as rendering uncertainty and geometric inconsistency, they do not fundamentally resolve the issue.를 문제로 두고, Hence, we introduce a variational optimization scheme to obtain a cleaner and more structured initialization.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian Splatting (3DGS) has demonstrated exceptional performance in reconstruction and novel view synthesis tasks.
- **p. 1 / Abstract - extractive body cue:** However, its reliance on Structure-from-Motion preprocessing may lead to degraded performance under sparse-view scenarios.
- **p. 1 / Abstract - extractive body cue:** Recent works attempt to address this limitation by leveraging pre-trained image matching models to generate Gaussian primitives but overlook the probabilistic uncertainty embedded in both ...
- **p. 1 / Abstract - extractive body cue:** This uncertainty can accumulate and degrade reconstruction fidelity.
- **p. 1 / Abstract - extractive body cue:** Hence, we propose BA-GS, a Bayesian framework that models both the global distribution and local uncertainty of Gaussian primitives.
- **p. 1 / 1. Introduction - extractive body cue:** Although these approaches partially alleviate the challenges of sparse-view reconstruction such as rendering uncertainty and geometric inconsistency, they do not fundamentally resolve the issue.
- **p. 1 / 1. Introduction - extractive body cue:** Reconstructing real-world scenes from images is a fundamental problem in computer vision.

## Core Idea

- **p. 4 / 4.1. Variational Bayesian Initialization - extractive body cue:** Hence, we introduce a variational optimization scheme to obtain a cleaner and more structured initialization.
- **p. 4 / 4.1. Variational Bayesian Initialization - extractive body cue:** Since the exact posterior distribution is intractable for most mixture models, we introduce a variational distribution q, which is optimized to be as close as ...
- **p. 5 / 4.3. Kalman Filtering for Position Denoising - extractive body cue:** To stabilize this update, we introduce an Adaptive Kalman Filter that recursively fuses predicted positions with observed projections.
- **p. 1 / 1. Introduction - extractive body cue:** Recent advances such as Neural Radiance Fields (NeRFs) and 3D Gaussian Splatting (3DGS) [12, 20] have enabled high-quality novel view * Co-Corresponding authors. synthesis and ...
- **p. 5 / 4.2. Prior-Guided Adaptive Density Control - extractive body cue:** This allows the control mechanism to adapt to local geometric complexity rather than relying on a uniform hyperparameter.
- **p. 6 / 4.3. Kalman Filtering for Position Denoising - extractive body cue:** Noise Covriance Matrix Proposed Adaptive Kalman Filter Optimization Loop Step t-1 Step t Step t+1 Gradient Density Position Prior Propagate State Noisy Position Element-wise Multiplication ...
- **p. 5 / 4.2. Prior-Guided Adaptive Density Control - extractive body cue:** This ensures that the newly generated primitives maintain a consistent feature representation with the original region.
- **p. 5 / 4.1. Variational Bayesian Initialization - extractive body cue:** The initial Gaussian primitives from MASt3R are refined via a gradient- and density-guided variational clustering model, providing a better starting state for subsequent processing.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Noise Covriance Matrix Proposed Adaptive Kalman Filter Optimization Loop Step t-1 Step t Step t+1 Gradient Density Position Prior Propagate State Noisy Position Element-wise Multiplication Linear Fusion Kalman Filtering Posterior State ... | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (4.3. Kalman Filtering for Position Denoising), p. 5 (4.3. Kalman Filtering for Position Denoising) |
| State/latent | Noise, Covriance, Matrix, Adaptive, Kalman, Filter, Optimization, Loop, Step, Gradient, Density, Position | geometry, map, object/relationship state | p. 6 (4.3. Kalman Filtering for Position Denoising), p. 5 (4.3. Kalman Filtering for Position Denoising), p. 6 (4.3. Kalman Filtering for Position Denoising) |
| Output/action | State and Observation Equations As analyzed in Section 3, for each Gaussian primitive i in the scene, we define its state vector xi = [x, y, z]T , representing its position in ... | point map, pose, scene graph, affordance 또는 query result | p. 5 (4.3. Kalman Filtering for Position Denoising), p. 6 (4.3. Kalman Filtering for Position Denoising), p. 1 (1. Introduction) |
| Objective/outcome | To make this optimization tractable, we maximize the Evidence Lower Bound (ELBO): L(q) = Eq[log p(X, Z, π, µ, Σ)] -Eq[log q(Z, π, µ, Σ)] (7) After convergence, each primitive is associated ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (4.1. Variational Bayesian Initialization), p. 5 (4.3. Kalman Filtering for Position Denoising), p. 5 (4.3. Kalman Filtering for Position Denoising) |

## Main Claims and Actual Contribution

- **p. 4 / 4.1. Variational Bayesian Initialization - extractive body cue:** Hence, we introduce a variational optimization scheme to obtain a cleaner and more structured initialization.
- **p. 4 / 4.1. Variational Bayesian Initialization - extractive body cue:** Since the exact posterior distribution is intractable for most mixture models, we introduce a variational distribution q, which is optimized to be as close as ...
- **p. 5 / 4.3. Kalman Filtering for Position Denoising - extractive body cue:** To stabilize this update, we introduce an Adaptive Kalman Filter that recursively fuses predicted positions with observed projections.
- **p. 1 / 1. Introduction - extractive body cue:** Recent advances such as Neural Radiance Fields (NeRFs) and 3D Gaussian Splatting (3DGS) [12, 20] have enabled high-quality novel view * Co-Corresponding authors. synthesis and ...
- **p. 5 / 4.2. Prior-Guided Adaptive Density Control - extractive body cue:** This allows the control mechanism to adapt to local geometric complexity rather than relying on a uniform hyperparameter.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Convergence analysis on the MVImgNet dataset (12 views). BA-GS achieves a higher performance ceiling and bet- ter stability compared to the baseline. The ...
- **p. 6 / 5.2. Experiment Results - extractive body cue:** The results consistently outperform baselines in both numerical and perceptual metrics across most settings, indicating that the performance gain is attributable to the method itself ...
- **p. 6 / 5.2. Experiment Results - extractive body cue:** In addition, by removing redundant or noisy primitives during initialization, our method significantly decreases the number of active primitives, therefore improves runtime efficiency while maintaining ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 6 (5.2. Experiment Results) |
| Embodiment/environment | We uniformly sample 3, 6, 12, and 18 spatially distributed views across each scene to form the training sets, while randomly sampling 12 remaining views for the test set. | hardware/simulator version and reset protocol | p. 6 (5.1. Experiment Setup), p. 6 (5.1. Experiment Setup) |
| Dataset/benchmark | Quantitative results on the LLFF dataset. | role, split, size and leakage | p. 6 (5.1. Experiment Setup), p. 6 (5.1. Experiment Setup), p. 7 (5.2. Experiment Results), p. 7 (5.2. Experiment Results) |
| Metric | Shaded regions represent the variance across different scenes. strates notable improvements in both performance optimum and optimization dynamics. | definition, denominator, direction and uncertainty | p. 8 (5.3. Ablation Study), p. 7 (5.3. Ablation Study), p. 7 (5.2. Experiment Results) |
| Baseline/ablation | As shown in our quantitative results(3-12 views of NeRFmm data are from [8]), BA-GS outperforms both SfM-based and SfM-free baselines. | fair input/data/compute/action matching | p. 6 (5.2. Experiment Results), p. 6 (5.2. Experiment Results), p. 8 (5.3. Ablation Study) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** Future works will explore richer priors, extending the Bayesian formulation to color and opacity estimation.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the global initialization Bayesian model (VB-GMM). The initial Gaussian primitives from MASt3R are refined via a gradient- and density-guided variational clustering ...
- **p. 8 / 6. Conclusion - extractive body cue:** But the current formulation assumes Gaussian noise assumption and relies on density/gradient priors, which may not fully capture uncertainty in highly textureless or heavily occluded ...
- **p. 7 / 5.2. Experiment Results - extractive body cue:** When replacing the globally-aligned MASt3R initialization with VGGT, the deterministic optimization of InstantSplat degrades severely due to its inability to handle positional noise.
- **p. 7 / 5.3. Ablation Study - extractive body cue:** Removing it causes a severe drop in PSNR and degrades perceptual metrics, confirming that modeling the latent probabilistic distribution of primitives is essential for mitigating ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Overview of BA-GS. Our method follows the classical Gaussian Splatting pipeline but introduces a Bayesian optimization stage that adaptively refines the Gaussian primitives ...
- **p. 6 / 5.1. Experiment Setup - extractive body cue:** In the Kalman filter module, the base noise covariance R0 is initialized as 10-2, with βg and βd also set to 0.5.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Although these approaches partially alleviate the challenges of sparse-view reconstruction such as rendering uncertainty and geometric inconsistency, they do not fundamentally resolve the issue.를 문제로 두고, Hence, we introduce a variational optimization scheme to obtain a cleaner and more structured initialization.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (4.1. Variational Bayesian Initialization), p. 4 (4.1. Variational Bayesian Initialization), p. 6 (4.3. Kalman Filtering for Position Denoising), p. 5 (4.2. Prior-Guided Adaptive Density Control) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
