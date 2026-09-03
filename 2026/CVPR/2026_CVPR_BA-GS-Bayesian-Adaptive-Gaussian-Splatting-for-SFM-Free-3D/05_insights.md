# Insights — BA-GS: Bayesian Adaptive Gaussian Splatting for SFM-Free 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ma_BA-GS_Bayesian_Adaptive_Gaussian_Splatting_for_SFM-Free_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_BA-GS_Bayesian_Adaptive_Gaussian_Splatting_for_SFM-Free_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / 4.1. Variational Bayesian Initialization - extractive body cue:** Hence, we introduce a variational optimization scheme to obtain a cleaner and more structured initialization.
- **p. 4 / 4.1. Variational Bayesian Initialization - extractive body cue:** Since the exact posterior distribution is intractable for most mixture models, we introduce a variational distribution q, which is optimized to be as close as ...
- **p. 5 / 4.3. Kalman Filtering for Position Denoising - extractive body cue:** To stabilize this update, we introduce an Adaptive Kalman Filter that recursively fuses predicted positions with observed projections.
- **p. 1 / 1. Introduction - extractive body cue:** Recent advances such as Neural Radiance Fields (NeRFs) and 3D Gaussian Splatting (3DGS) [12, 20] have enabled high-quality novel view * Co-Corresponding authors. synthesis and ...
- **p. 5 / 4.2. Prior-Guided Adaptive Density Control - extractive body cue:** This allows the control mechanism to adapt to local geometric complexity rather than relying on a uniform hyperparameter.
- **p. 6 / 4.3. Kalman Filtering for Position Denoising - extractive body cue:** Noise Covriance Matrix Proposed Adaptive Kalman Filter Optimization Loop Step t-1 Step t Step t+1 Gradient Density Position Prior Propagate State Noisy Position Element-wise Multiplication ...
- **p. 5 / 4.2. Prior-Guided Adaptive Density Control - extractive body cue:** This ensures that the newly generated primitives maintain a consistent feature representation with the original region.
- **Contribution anchor:** p. 4 (4.1. Variational Bayesian Initialization), p. 4 (4.1. Variational Bayesian Initialization), p. 5 (4.3. Kalman Filtering for Position Denoising), p. 1 (1. Introduction), p. 5 (4.2. Prior-Guided Adaptive Density Control), p. 6 (4.3. Kalman Filtering for Position Denoising)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Although these approaches partially alleviate the challenges of sparse-view reconstruction such as rendering uncertainty and geometric inconsistency, they do not fundamentally resolve the issue.
- **p. 1 / 1. Introduction - extractive body cue:** Reconstructing real-world scenes from images is a fundamental problem in computer vision.
- **p. 8 / 6. Conclusion - extractive body cue:** Future works will explore richer priors, extending the Bayesian formulation to color and opacity estimation.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the global initialization Bayesian model (VB-GMM). The initial Gaussian primitives from MASt3R are refined via a gradient- and density-guided variational clustering ...
- **p. 8 / 6. Conclusion - extractive body cue:** But the current formulation assumes Gaussian noise assumption and relies on density/gradient priors, which may not fully capture uncertainty in highly textureless or heavily occluded ...
- **p. 7 / 5.2. Experiment Results - extractive body cue:** When replacing the globally-aligned MASt3R initialization with VGGT, the deterministic optimization of InstantSplat degrades severely due to its inability to handle positional noise.
- **p. 7 / 5.3. Ablation Study - extractive body cue:** Removing it causes a severe drop in PSNR and degrades perceptual metrics, confirming that modeling the latent probabilistic distribution of primitives is essential for mitigating ...
- **Boundary to test:** Future works will explore richer priors, extending the Bayesian formulation to color and opacity estimation.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Hence, we introduce a variational optimization scheme to obtain a cleaner and more structured initialization. | p. 4 (4.1. Variational Bayesian Initialization), p. 4 (4.1. Variational Bayesian Initialization) |
| Reported outcome | Figure 5. Convergence analysis on the MVImgNet dataset (12 views). BA-GS achieves a higher performance ceiling and bet- ter stability compared to the baseline. The baseline suffers from performance degradation and jittering ... | p. 8 (Figure/Table caption), p. 6 (5.2. Experiment Results) |
| Failure/limitation | Future works will explore richer priors, extending the Bayesian formulation to color and opacity estimation. | p. 8 (6. Conclusion), p. 5 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Noise Covriance Matrix Proposed Adaptive Kalman Filter Optimization Loop Step t-1 Step t Step t+1 Gradient Density Position Prior Propagate State Noisy Position Element-wise Multiplication Linear Fusion Kalman Filtering Posterior State ...를 State and Observation Equations As analyzed in Section 3, for each Gaussian primitive i in the scene, we define its state vector xi = [x, y, z]T , representing its position in ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Future works will explore richer priors, extending the Bayesian formulation to color and opacity estimation.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Hence, we introduce a variational optimization scheme to obtain a cleaner and more structured initialization.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, 3D reconstruction, geometry, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Future works will explore richer priors, extending the Bayesian formulation to color and opacity estimation.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We uniformly sample 3, 6, 12, and 18 spatially distributed views across each scene to form the training sets, while randomly sampling 12 remaining views for the test set..
3. Compare against the body-reported baseline or a matched simpler baseline: As shown in our quantitative results(3-12 views of NeRFmm data are from [8]), BA-GS outperforms both SfM-based and SfM-free baselines..
4. Report the body metric and its denominator/aggregation: Shaded regions represent the variance across different scenes. strates notable improvements in both performance optimum and optimization dynamics..
5. Re-run the body-reported ablation/failure condition: Ablation Variant VB-GMM Adaptive Density Control Position Filtering Rendering Time (s) ↓ PSNR ↑ SSIM ↑ LPIPS ↓ Full (Ours) ✓ ✓ ✓ 153.88 31.6129 0.9367 0.0673 Baseline × × × 190.25 ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (4.1. Variational Bayesian Initialization), p. 4 (4.1. Variational Bayesian Initialization), p. 6 (4.3. Kalman Filtering for Position Denoising); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 6 (5.2. Experiment Results), p. 6 (5.2. Experiment Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Hence, introduce, variational mechanism이 As shown in our quantitative results(3-12 views of NeRFmm data are from [8]), BA-GS outperforms both ... 대비 Shaded regions represent the variance across different scenes. strates notable improvements in both performance optimum and optimization dynamics.을 개선하고, Future works will explore richer priors, extending the Bayesian formulation to color and opacity estimation. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
