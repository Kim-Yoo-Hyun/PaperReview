# Method - BA-GS: Bayesian Adaptive Gaussian Splatting for SFM-Free 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ma_BA-GS_Bayesian_Adaptive_Gaussian_Splatting_for_SFM-Free_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_BA-GS_Bayesian_Adaptive_Gaussian_Splatting_for_SFM-Free_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4.1. Variational Bayesian Initialization), p. 4 (4.1. Variational Bayesian Initialization), p. 6 (4.3. Kalman Filtering for Position Denoising), p. 5 (4.2. Prior-Guided Adaptive Density Control), p. 5 (4.1. Variational Bayesian Initialization), p. 6 (4.3. Kalman Filtering for Position Denoising)): Since the exact posterior distribution is intractable for most mixture models, we introduce a variational distribution q, which is optimized to be as close as possible to the true posterior: ...

## Method Body Digest

- **p. 4 / 4.1. Variational Bayesian Initialization - extractive PDF cue:** Since the exact posterior distribution is intractable for most mixture models, we introduce a variational distribution q, which is optimized to be as close as ...
- **p. 4 / 4.1. Variational Bayesian Initialization - extractive PDF cue:** Hence, we introduce a variational optimization scheme to obtain a cleaner and more structured initialization.
- **p. 6 / 4.3. Kalman Filtering for Position Denoising - extractive PDF cue:** Noise Covriance Matrix Proposed Adaptive Kalman Filter Optimization Loop Step t-1 Step t Step t+1 Gradient Density Position Prior Propagate State Noisy Position Element-wise Multiplication ...
- **p. 5 / 4.2. Prior-Guided Adaptive Density Control - extractive PDF cue:** This ensures that the newly generated primitives maintain a consistent feature representation with the original region.
- **p. 5 / 4.1. Variational Bayesian Initialization - extractive PDF cue:** The initial Gaussian primitives from MASt3R are refined via a gradient- and density-guided variational clustering model, providing a better starting state for subsequent processing.
- **p. 6 / 4.3. Kalman Filtering for Position Denoising - extractive PDF cue:** Detailed architecture of the local refinement-level Bayesian model.
- **p. 4 / 4.1. Variational Bayesian Initialization - extractive PDF cue:** To make this optimization tractable, we maximize the Evidence Lower Bound (ELBO): L(q) = Eq[log p(X, Z, π, µ, Σ)] -Eq[log q(Z, π, µ, Σ)] ...
- **p. 5 / 4.3. Kalman Filtering for Position Denoising - extractive PDF cue:** 3DGS optimizes Gaussian positions via gradient descent.

## Design Rationale

- **p. 4 / 4.1. Variational Bayesian Initialization - extractive PDF cue:** Hence, we introduce a variational optimization scheme to obtain a cleaner and more structured initialization.
- **p. 4 / 4.1. Variational Bayesian Initialization - extractive PDF cue:** Since the exact posterior distribution is intractable for most mixture models, we introduce a variational distribution q, which is optimized to be as close as ...
- **p. 5 / 4.3. Kalman Filtering for Position Denoising - extractive PDF cue:** To stabilize this update, we introduce an Adaptive Kalman Filter that recursively fuses predicted positions with observed projections.

## Source Evidence Cues

- **p. 4 / 4.1. Variational Bayesian Initialization - extractive PDF cue:** Since the exact posterior distribution is intractable for most mixture models, we introduce a variational distribution q, which is optimized to be as close as ...
- **p. 4 / 4.1. Variational Bayesian Initialization - extractive PDF cue:** Hence, we introduce a variational optimization scheme to obtain a cleaner and more structured initialization.
- **p. 6 / 4.3. Kalman Filtering for Position Denoising - extractive PDF cue:** Noise Covriance Matrix Proposed Adaptive Kalman Filter Optimization Loop Step t-1 Step t Step t+1 Gradient Density Position Prior Propagate State Noisy Position Element-wise Multiplication ...
- **p. 5 / 4.2. Prior-Guided Adaptive Density Control - extractive PDF cue:** This ensures that the newly generated primitives maintain a consistent feature representation with the original region.
- **p. 5 / 4.1. Variational Bayesian Initialization - extractive PDF cue:** The initial Gaussian primitives from MASt3R are refined via a gradient- and density-guided variational clustering model, providing a better starting state for subsequent processing.
- **p. 6 / 4.3. Kalman Filtering for Position Denoising - extractive PDF cue:** Detailed architecture of the local refinement-level Bayesian model.
- **Detected method headings:** 2.3. Probabilistic Approaches in Neural Rendering (p. 3); 4. Methods (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Since the exact posterior distribution is intractable for most mixture models, we introduce a variational distribution q, which is optimized to be ... | p. 4 (4.1. Variational Bayesian Initialization), p. 4 (4.1. Variational Bayesian Initialization) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Hence, we introduce a variational optimization scheme to obtain a cleaner and more structured initialization. | p. 4 (4.1. Variational Bayesian Initialization), p. 6 (4.3. Kalman Filtering for Position Denoising) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Noise Covriance Matrix Proposed Adaptive Kalman Filter Optimization Loop Step t-1 Step t Step t+1 Gradient Density Position Prior Propagate State Noisy ... | p. 6 (4.3. Kalman Filtering for Position Denoising), p. 5 (4.2. Prior-Guided Adaptive Density Control) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4.1. Variational Bayesian Initialization - extractive PDF cue:** To make this optimization tractable, we maximize the Evidence Lower Bound (ELBO): L(q) = Eq[log p(X, Z, π, µ, Σ)] -Eq[log q(Z, π, µ, Σ)] ...
- **p. 5 / 4.3. Kalman Filtering for Position Denoising - extractive PDF cue:** 3DGS optimizes Gaussian positions via gradient descent.
- **p. 5 / 4.3. Kalman Filtering for Position Denoising - extractive PDF cue:** The state update equation can be written as: xi,t = Ftxi,t-1 + wt (9) where Ft is the state transition matrix, and wt represents 26128
- **p. 6 / 4.3. Kalman Filtering for Position Denoising - extractive PDF cue:** Noise Covriance Matrix Proposed Adaptive Kalman Filter Optimization Loop Step t-1 Step t Step t+1 Gradient Density Position Prior Propagate State Noisy Position Element-wise Multiplication ...
- **p. 4 / 4.1. Variational Bayesian Initialization - extractive PDF cue:** Primitives can be categorized into four regions in the density-gradient space.
- **p. 6 / 4.3. Kalman Filtering for Position Denoising - extractive PDF cue:** The Kalman filter fuses priors with measurements, where the noise covariance is adjusted by gradient and density.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4.3. Kalman Filtering for Position Denoising), p. 4 (4.1. Variational Bayesian Initialization), p. 4 (4.1. Variational Bayesian Initialization), p. 5 (4.3. Kalman Filtering for Position Denoising), p. 6 (4.3. Kalman Filtering for Position Denoising), p. 6 (4.3. Kalman Filtering for Position Denoising).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Noise, Covriance, Matrix, Adaptive, Kalman, Filter, Optimization, Loop, Step, Gradient, Density, Position, Prior, Propagate | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Noise, Covriance, Matrix, Adaptive, Kalman, Filter, Optimization, Loop, Step, Gradient | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Hence, introduce, variational, optimization, scheme, obtain, cleaner, more, structured, initialization | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | make, optimization, tractable, maximize, Evidence, Lower, Bound, ELBO, After, convergence | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 4.3. Kalman Filtering for Position Denoising - extractive PDF cue:** Noise Covriance Matrix Proposed Adaptive Kalman Filter Optimization Loop Step t-1 Step t Step t+1 Gradient Density Position Prior Propagate State Noisy Position Element-wise Multiplication ...
- **p. 5 / 4.3. Kalman Filtering for Position Denoising - extractive PDF cue:** State and Observation Equations As analyzed in Section 3, for each Gaussian primitive i in the scene, we define its state vector xi = [x, ...
- **p. 6 / 4.3. Kalman Filtering for Position Denoising - extractive PDF cue:** Since the amplitude of gradients in different regions reflects the complexity of the image structure, the filter can automatically adjust the observation noise covariance matrix ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The sparsity of input views leads to insufficient image constraints, causing ambiguities where a single point may correspond to multiple plausible locations, thereby introducing noise ...
- **p. 4 / 4.1. Variational Bayesian Initialization - extractive PDF cue:** Observing that each Gaussian primitive has attributes such as local gradient and density, we can construct an observation matrix: X =   d1 g1 ...
- **p. 5 / 4.3. Kalman Filtering for Position Denoising - extractive PDF cue:** The state update equation can be written as: xi,t = Ftxi,t-1 + wt (9) where Ft is the state transition matrix, and wt represents 26128
- **p. 4 / 4.1. Variational Bayesian Initialization - extractive PDF cue:** Each point is projected into valid image regions, checked for depth consistency, and assigned fused color and depth gradients.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Interpolation & Trimming Interpolated Gaussians Trimmed Gaussians VB-GMM T step T+1 step T+2 step T+3 step Prior Measurement Posterior Kalman Filter Pruned ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Each optimization iteration corresponds to one Kalman update step, where xi,t denotes the primitive position at iteration t. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Interpolation & Trimming Interpolated Gaussians Trimmed Gaussians VB-GMM T step T+1 step T+2 step T+3 step Prior Measurement Posterior Kalman Filter Pruned ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Since, exact, posterior, distribution, intractable, most, mixture, models, introduce, variational, optimized, close, possible, true, Where, denotes, latent, variables, indicating, cluster.
- **Relevant PDF headings:** 2.3. Probabilistic Approaches in Neural Rendering (p. 3); 4. Methods (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We uniformly sample 3, 6, 12, and 18 spatially distributed views across each scene to form the training sets, while randomly sampling ... | p. 6 (5.1. Experiment Setup), p. 6 (5.1. Experiment Setup) |
| Semantic / temporal fusion | As shown in our quantitative results(3-12 views of NeRFmm data are from [8]), BA-GS outperforms both SfM-based and SfM-free baselines. | p. 6 (5.2. Experiment Results), p. 6 (5.2. Experiment Results) |
| Robot query / planning handoff | Figure 5. Convergence analysis on the MVImgNet dataset (12 views). BA-GS achieves a higher performance ceiling and bet- ter stability compared to ... | p. 8 (Figure/Table caption), p. 6 (5.2. Experiment Results) |

## Failure and Ablation Link

- **p. 8 / 5.3. Ablation Study - extractive PDF cue:** Ablation Variant VB-GMM Adaptive Density Control Position Filtering Rendering Time (s) ↓ PSNR ↑ SSIM ↑ LPIPS ↓ Full (Ours) ✓ ✓ ✓ 153.88 31.6129 ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation study evaluating the contribution of each module in our framework (12 views setting). We report rendering time and three perceptual metrics. Ablation ...
- **p. 7 / 5.3. Ablation Study - extractive PDF cue:** We conduct an ablation study on the Tanks and Temples dataset to evaluate the importance of key components such as position filtering and optimization for ...
- **p. 6 / 5.2. Experiment Results - extractive PDF cue:** In addition, by removing redundant or noisy primitives during initialization, our method significantly decreases the number of active primitives, therefore improves runtime efficiency while maintaining ...
- **p. 7 / 5.3. Ablation Study - extractive PDF cue:** Removing it causes a severe drop in PSNR and degrades perceptual metrics, confirming that modeling the latent probabilistic distribution of primitives is essential for mitigating ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. Overview of BA-GS. Our method follows the classical Gaussian Splatting pipeline but introduces a Bayesian optimization stage that adaptively refines the Gaussian primitives ...
- **p. 8 / 6. Conclusion - extractive PDF cue:** Future works will explore richer priors, extending the Bayesian formulation to color and opacity estimation.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4.1. Variational Bayesian Initialization), p. 4 (4.1. Variational Bayesian Initialization), p. 6 (4.3. Kalman Filtering for Position Denoising), p. 5 (4.2. Prior-Guided Adaptive Density Control), p. 5 (4.1. Variational Bayesian Initialization), p. 6 (4.3. Kalman Filtering for Position Denoising), objective p. 4 (4.1. Variational Bayesian Initialization), p. 5 (4.3. Kalman Filtering for Position Denoising), p. 5 (4.3. Kalman Filtering for Position Denoising), p. 6 (4.3. Kalman Filtering for Position Denoising), p. 4 (4.1. Variational Bayesian Initialization), p. 6 (4.3. Kalman Filtering for Position Denoising), temporal p. 2 (2. Global Initialization), p. 6 (4.3. Kalman Filtering for Position Denoising), p. 6 (5.2. Experiment Results), p. 8 (5.3. Ablation Study), p. 1 (Abstract), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
