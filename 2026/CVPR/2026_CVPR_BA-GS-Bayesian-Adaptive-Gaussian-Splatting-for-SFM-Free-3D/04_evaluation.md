# Evaluation - BA-GS: Bayesian Adaptive Gaussian Splatting for SFM-Free 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ma_BA-GS_Bayesian_Adaptive_Gaussian_Splatting_for_SFM-Free_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_BA-GS_Bayesian_Adaptive_Gaussian_Splatting_for_SFM-Free_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 6 (5.2. Experiment Results), p. 6 (5.2. Experiment Results), p. 7 (5.3. Ablation Study), p. 7 (5.2. Experiment Results), p. 2 (Figure/Table caption)): Figure 5. Convergence analysis on the MVImgNet dataset (12 views). BA-GS achieves a higher performance ceiling and bet- ter stability compared to the baseline. The baseline suffers from performance degradation ...

## Evaluation Body Digest

- **p. 6 / 5.1. Experiment Setup - extractive body cue:** We uniformly sample 3, 6, 12, and 18 spatially distributed views across each scene to form the training sets, while randomly sampling 12 remaining views ...
- **p. 6 / 5.1. Experiment Setup - extractive body cue:** For consistency, all experiments use the downsampled resolution images provided by the datasets.
- **p. 7 / 5.2. Experiment Results - extractive body cue:** Quantitative results on the LLFF dataset.
- **p. 7 / 5.2. Experiment Results - extractive body cue:** Comparison of rendering time, PSNR, SSIM, and LPIPS on the MVImgNet dataset.
- **p. 8 / 5.3. Ablation Study - extractive body cue:** Convergence analysis on the MVImgNet dataset (12 views).
- **p. 8 / 5.3. Ablation Study - extractive body cue:** Shaded regions represent the variance across different scenes. strates notable improvements in both performance optimum and optimization dynamics.
- **p. 7 / 5.3. Ablation Study - extractive body cue:** Position filtering further improves pixel-level accuracy.
- **p. 7 / 5.2. Experiment Results - extractive body cue:** Notably, VGGT+BA-GS achieves the best LPIPS scores across 3 to 18 views, demonstrating that our approach effectively mitigates floater artifacts induced by noisy feed-forward priors.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Experiment Setup (p. 6); 5.2. Experiment Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5. Convergence analysis on the MVImgNet dataset (12 views). BA-GS achieves a higher performance ceiling and bet- ter stability compared to the baseline. ... | p. 8 (Figure/Table caption) |
| 5.2. Experiment Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results consistently outperform baselines in both numerical and perceptual metrics across most settings, indicating that the performance gain is attributable to the method ... | p. 6 (5.2. Experiment Results) |
| 5.2. Experiment Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | In addition, by removing redundant or noisy primitives during initialization, our method significantly decreases the number of active primitives, therefore improves runtime efficiency while ... | p. 6 (5.2. Experiment Results) |
| 5.3. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | Position filtering further improves pixel-level accuracy. | p. 7 (5.3. Ablation Study) |
| 5.2. Experiment Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notably, VGGT+BA-GS achieves the best LPIPS scores across 3 to 18 views, demonstrating that our approach effectively mitigates floater artifacts induced by noisy feed-forward ... | p. 7 (5.2. Experiment Results) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Experiment Setup - extractive body cue:** We uniformly sample 3, 6, 12, and 18 spatially distributed views across each scene to form the training sets, while randomly sampling 12 remaining views ...
- **p. 6 / 5.1. Experiment Setup - extractive body cue:** For consistency, all experiments use the downsampled resolution images provided by the datasets.
- **p. 7 / 5.2. Experiment Results - extractive body cue:** Quantitative results on the LLFF dataset.
- **p. 7 / 5.2. Experiment Results - extractive body cue:** Comparison of rendering time, PSNR, SSIM, and LPIPS on the MVImgNet dataset.
- **p. 8 / 5.3. Ablation Study - extractive body cue:** Convergence analysis on the MVImgNet dataset (12 views).
- **p. 8 / 5.3. Ablation Study - extractive body cue:** Shaded regions represent the variance across different scenes. strates notable improvements in both performance optimum and optimization dynamics.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Overview of BA-GS. Our method follows the classical Gaussian Splatting pipeline but introduces a Bayesian optimization stage that adaptively refines the Gaussian primitives ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the global initialization Bayesian model (VB-GMM). The initial Gaussian primitives from MASt3R are refined via a gradient- and density-guided variational clustering ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Detailed architecture of the local refinement-level Bayesian model. The Kalman filter fuses priors with measure- ments, where the noise covariance is adjusted by ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Comparison of rendering time, PSNR, SSIM, and LPIPS on the MVImgNet dataset. Our method delivers clearer details and better rendering quality, achieving lower ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Comparison of rendering time, PSNR, SSIM, and LPIPS on the Tanks and Temples dataset. Compared to MVImgNet, the overall rendering performance on this ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Quantitative results on the LLFF dataset. While overall metrics are relatively lower due to complex forward-facing scenes, MASt3R+BA-GS maintains leadership in PSNR and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Zoom-in comparison (18 views setting). Leftmost column: Ground Truth. Second and third columns: DropGaussian (full / cropped). Fourth and fifth columns: InstantSplat (full ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablation study evaluating the contribution of each module in our framework (12 views setting). We report rendering time and three perceptual metrics. Ablation ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We uniformly sample 3, 6, 12, and 18 spatially distributed views across each scene to form the training sets, while randomly sampling 12 remaining ... | embodiment, simulator version and control stack | p. 6 (5.1. Experiment Setup), p. 6 (5.1. Experiment Setup) |
| Task/environment | For consistency, all experiments use the downsampled resolution images provided by the datasets. | reset, timeout, object/scene variation | p. 6 (5.1. Experiment Setup), p. 7 (5.2. Experiment Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (4.3. Kalman Filtering for Position Denoising), p. 5 (4.3. Kalman Filtering for Position Denoising) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (4.3. Kalman Filtering for Position Denoising), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Shaded regions represent the variance across different scenes. strates notable improvements in both performance optimum and optimization dynamics. | definition/direction/unit from same section | p. 8 (5.3. Ablation Study) |
| Position filtering further improves pixel-level accuracy. | definition/direction/unit from same section | p. 7 (5.3. Ablation Study) |
| Notably, VGGT+BA-GS achieves the best LPIPS scores across 3 to 18 views, demonstrating that our approach effectively mitigates floater artifacts induced by noisy feed-forward ... | definition/direction/unit from same section | p. 7 (5.2. Experiment Results) |
| Figure 1. Overview of BA-GS. Our method follows the classical Gaussian Splatting pipeline but introduces a Bayesian optimization stage that adaptively refines the Gaussian ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| In the Kalman filter module, the base noise covariance R0 is initialized as 10-2, with βg and βd also set to 0.5. | definition/direction/unit from same section | p. 6 (5.1. Experiment Setup) |
| The results consistently outperform baselines in both numerical and perceptual metrics across most settings, indicating that the performance gain is attributable to the method ... | definition/direction/unit from same section | p. 6 (5.2. Experiment Results) |
| The baseline suffers from performance degradation and jittering in later stages. | definition/direction/unit from same section | p. 8 (5.3. Ablation Study) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in our quantitative results(3-12 views of NeRFmm data are from [8]), BA-GS outperforms both SfM-based and SfM-free baselines. | comparison identity and matched condition | p. 6 (5.2. Experiment Results) |
| The results consistently outperform baselines in both numerical and perceptual metrics across most settings, indicating that the performance gain is attributable to the method ... | comparison identity and matched condition | p. 6 (5.2. Experiment Results) |
| BA-GS achieves a higher performance ceiling and better stability compared to the baseline. | comparison identity and matched condition | p. 8 (5.3. Ablation Study) |
| While the fluctuation around 500 iterations is a transient effect of adaptive density control, BA-GS consistently maintains better metrics compared to the baseline. | comparison identity and matched condition | p. 8 (5.3. Ablation Study) |
| Table 2. Comparison of rendering time, PSNR, SSIM, and LPIPS on the Tanks and Temples dataset. Compared to MVImgNet, the overall rendering performance on ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| In contrast, VGGT+BAGS demonstrates remarkable robustness, outperforming VGGT+InstantSplat by a large margin (e.g., 2-3 dB in PSNR on Tanks and Temples). | comparison identity and matched condition | p. 7 (5.2. Experiment Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation Variant VB-GMM Adaptive Density Control Position Filtering Rendering Time (s) ↓ PSNR ↑ SSIM ↑ LPIPS ↓ Full (Ours) ✓ ✓ ✓ 153.88 ... | component/input/data sensitivity | p. 8 (5.3. Ablation Study) |
| Table 4. Ablation study evaluating the contribution of each module in our framework (12 views setting). We report rendering time and three perceptual metrics. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We conduct an ablation study on the Tanks and Temples dataset to evaluate the importance of key components such as position filtering and optimization ... | component/input/data sensitivity | p. 7 (5.3. Ablation Study) |
| In addition, by removing redundant or noisy primitives during initialization, our method significantly decreases the number of active primitives, therefore improves runtime efficiency while ... | component/input/data sensitivity | p. 6 (5.2. Experiment Results) |
| Removing it causes a severe drop in PSNR and degrades perceptual metrics, confirming that modeling the latent probabilistic distribution of primitives is essential for ... | component/input/data sensitivity | p. 7 (5.3. Ablation Study) |
| Figure 1. Overview of BA-GS. Our method follows the classical Gaussian Splatting pipeline but introduces a Bayesian optimization stage that adaptively refines the Gaussian ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Hence, we introduce a variational optimization scheme to obtain a cleaner and more structured initialization. | Figure 5. Convergence analysis on the MVImgNet dataset (12 views). BA-GS achieves a higher performance ceiling and bet- ter stability compared to the baseline. ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 6 (5.2. Experiment Results), p. 6 (5.2. Experiment Results), p. 7 (5.3. Ablation Study), p. 7 (5.2. Experiment Results), p. 2 (Figure/Table caption) |
| Primary metric/result | The results consistently outperform baselines in both numerical and perceptual metrics across most settings, indicating that the performance gain is attributable to the method ... | numeric claim only at cited anchor | p. 6 (5.2. Experiment Results) |

- Numeric sentences retained from the body:
- **p. 6 / 5.1. Experiment Setup - extractive body cue:** The mapping functions for the adaptive density control (ψ) and the adaptive noise covariance (ϕ) are instantiated as ψ(x) = 1 + λ(2x -1) and ...
- **p. 6 / 5.1. Experiment Setup - extractive body cue:** All experiments are conducted on an RTX 4080 GPU with CUDA version 11.8.
- **p. 6 / 4.3. Kalman Filtering for Position Denoising - extractive body cue:** Noise Covriance Matrix Proposed Adaptive Kalman Filter Optimization Loop Step t-1 Step t Step t+1 Gradient Density Position Prior Propagate State Noisy Position Element-wise Multiplication ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future works will explore richer priors, extending the Bayesian formulation to color and opacity estimation. | p. 8 (6. Conclusion) |
| body limitation/failure cue | Figure 2. Overview of the global initialization Bayesian model (VB-GMM). The initial Gaussian primitives from MASt3R are refined via a gradient- and density-guided variational ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | But the current formulation assumes Gaussian noise assumption and relies on density/gradient priors, which may not fully capture uncertainty in highly textureless or heavily ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | When replacing the globally-aligned MASt3R initialization with VGGT, the deterministic optimization of InstantSplat degrades severely due to its inability to handle positional noise. | p. 7 (5.2. Experiment Results) |
| body limitation/failure cue | Removing it causes a severe drop in PSNR and degrades perceptual metrics, confirming that modeling the latent probabilistic distribution of primitives is essential for ... | p. 7 (5.3. Ablation Study) |
| body limitation/failure cue | Figure 1. Overview of BA-GS. Our method follows the classical Gaussian Splatting pipeline but introduces a Bayesian optimization stage that adaptively refines the Gaussian ... | p. 2 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All experiments are conducted on an RTX 4080 GPU with CUDA version 11.8. | p. 6 (5.1. Experiment Setup) |
| By unifying variationbased clustering and adaptive denoising, our framework effectively filters out redundant primitives, improving both runtime efficiency and rendering quality. | p. 6 (5.2. Experiment Results) |
| 2, and the detailed pseudocode is provided in the supplementary material. | p. 4 (4.1. Variational Bayesian Initialization) |
| This allows the control mechanism to adapt to local geometric complexity rather than relying on a uniform hyperparameter. | p. 5 (4.2. Prior-Guided Adaptive Density Control) |
| Unlike the original ADC strategy in 3DGS [12], which applies a global, fixed threshold, our strategy computes a perprimitive threshold conditioned on local priors. | p. 5 (4.2. Prior-Guided Adaptive Density Control) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive body cue:** Future works will explore richer priors, extending the Bayesian formulation to color and opacity estimation.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the global initialization Bayesian model (VB-GMM). The initial Gaussian primitives from MASt3R are refined via a gradient- and density-guided variational clustering ...
- **p. 8 / 6. Conclusion - extractive body cue:** But the current formulation assumes Gaussian noise assumption and relies on density/gradient priors, which may not fully capture uncertainty in highly textureless or heavily occluded ...
- **p. 7 / 5.2. Experiment Results - extractive body cue:** When replacing the globally-aligned MASt3R initialization with VGGT, the deterministic optimization of InstantSplat degrades severely due to its inability to handle positional noise.
- **p. 7 / 5.3. Ablation Study - extractive body cue:** Removing it causes a severe drop in PSNR and degrades perceptual metrics, confirming that modeling the latent probabilistic distribution of primitives is essential for mitigating ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Overview of BA-GS. Our method follows the classical Gaussian Splatting pipeline but introduces a Bayesian optimization stage that adaptively refines the Gaussian primitives ...

- **Evidence anchors reviewed:** datasets p. 6 (5.1. Experiment Setup), p. 6 (5.1. Experiment Setup), p. 7 (5.2. Experiment Results), p. 7 (5.2. Experiment Results), p. 8 (5.3. Ablation Study), p. 8 (5.3. Ablation Study), metrics p. 8 (5.3. Ablation Study), p. 7 (5.3. Ablation Study), p. 7 (5.2. Experiment Results), p. 2 (Figure/Table caption), p. 6 (5.1. Experiment Setup), p. 6 (5.2. Experiment Results), baselines p. 6 (5.2. Experiment Results), p. 6 (5.2. Experiment Results), p. 8 (5.3. Ablation Study), p. 8 (5.3. Ablation Study), p. 7 (Figure/Table caption), p. 7 (5.2. Experiment Results), results p. 8 (Figure/Table caption), p. 6 (5.2. Experiment Results), p. 6 (5.2. Experiment Results), p. 7 (5.3. Ablation Study), p. 7 (5.2. Experiment Results), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
