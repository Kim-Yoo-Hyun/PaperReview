# Evaluation - SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=o1sF4XaFdY; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247825. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 16 (A.3 EXTENDED RESULTS AT HIGHER RESOLUTION), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT)): Since using more primitives generally improves performance, we focus our core comparisons on the latter group to ensure a fair comparison.

## Evaluation Body Digest

- **p. 7 / 4 EXPERIMENT - extractive body cue:** Both datasets provide precomputed camera poses and we adhere to the official train-test splits used in prior work.
- **p. 7 / 4 EXPERIMENT - extractive body cue:** (2014) dataset following MVSplat Chen et al.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** 4.1 MAIN RESULTS Table 1: Novel view synthesis performance on the RealEstate10k dataset.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** We report quantitative comparison on the RE10K dataset in Table 1 and on the ACID dataset in Table 2.
- **p. 9 / 4 EXPERIMENT - extractive body cue:** 4.2 ABLATION AND ANALYSIS Figure 5: Ablation study: Visualization of reconstructed 3D scenes.
- **p. 9 / 4 EXPERIMENT - extractive body cue:** To assess cross-dataset generalization, we train our model on RE10K and directly conduct evaluation on DTU, DL3DV, and ScanNet datasets.
- **p. 10 / 4 EXPERIMENT - extractive body cue:** Metric pixelSplat HiSplat MVSplat TransSplat DepthSplat Ours PSNR ↑ 24.082 22.780 17.966 19.545 16.066 24.411 SSIM ↑ 0.755 0.765 0.645 0.679 0.600 0.788 LPIPS ↓ ...
- **p. 17 / A.3 EXTENDED RESULTS AT HIGHER RESOLUTION - extractive body cue:** As the resolution increases, our model preserves coherent geometry and appearance, revealing finer details of the scene.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENT (p. 7); A.3 EXTENDED RESULTS AT HIGHER RESOLUTION (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | Since using more primitives generally improves performance, we focus our core comparisons on the latter group to ensure a fair comparison. | p. 8 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | Interestingly, this variant still achieves competitive novel view synthesis (NVS) performance at the original resolution, despite producing visually noisy and discontinuous surfaces. | p. 9 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | From this comparison, we observe that our method produces more geometrically consistent results, highlighting the improved geometric coherence induced by the surface continuity prior. | p. 10 (4 EXPERIMENT) |
| A.3 EXTENDED RESULTS AT HIGHER RESOLUTION | EMPIRICAL / SOURCE-REPORTED EVALUATION | Quantitative results are summarized in Table 7, showing consistent improvements across standard and high-resolution metrics. | p. 16 (A.3 EXTENDED RESULTS AT HIGHER RESOLUTION) |
| 4 EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our proposed SurfSplat method consistently outperforms previous stateof-the-art methods across various metrics and datasets, especially under high-resolution rendering settings. | p. 8 (4 EXPERIMENT) |

## Dataset / Benchmark Role

- **p. 7 / 4 EXPERIMENT - extractive body cue:** Both datasets provide precomputed camera poses and we adhere to the official train-test splits used in prior work.
- **p. 7 / 4 EXPERIMENT - extractive body cue:** (2014) dataset following MVSplat Chen et al.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** 4.1 MAIN RESULTS Table 1: Novel view synthesis performance on the RealEstate10k dataset.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** We report quantitative comparison on the RE10K dataset in Table 1 and on the ACID dataset in Table 2.
- **p. 9 / 4 EXPERIMENT - extractive body cue:** 4.2 ABLATION AND ANALYSIS Figure 5: Ablation study: Visualization of reconstructed 3D scenes.
- **p. 9 / 4 EXPERIMENT - extractive body cue:** To assess cross-dataset generalization, we train our model on RE10K and directly conduct evaluation on DTU, DL3DV, and ScanNet datasets.
- **p. 10 / 4 EXPERIMENT - extractive body cue:** Metric pixelSplat HiSplat MVSplat TransSplat DepthSplat Ours PSNR ↑ 24.082 22.780 17.966 19.545 16.066 24.411 SSIM ↑ 0.755 0.765 0.645 0.679 0.600 0.788 LPIPS ↓ ...
- **p. 17 / A.3 EXTENDED RESULTS AT HIGHER RESOLUTION - extractive body cue:** As the resolution increases, our model preserves coherent geometry and appearance, revealing finer details of the scene.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: SurfSplat is a feedforward network that predicts a 3D scene representation from sparse images input. Previous methods often produce sparse, color-biased pointclouds that ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Illustration for model architecture. Given sparse input images, our dual-path encoder processes them through both single-view and multi-view branches. The fused features are ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Illustration for Gaussian processor. We visualize how image-space neighboring pixels are transformed into Gaussians aligned on a continuous surface via the surface continuity ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Multi-resolution rendering of 3D scenes. We visualize rendered images and depth maps at three resolutions: ×1 (blue box), ×2 (green box), and ×4 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Novel view synthesis performance on the RealEstate10k dataset. 256×256 (Standard) 512×512 (HRRC) 1024×1024 (HRRC) Average
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Novel view synthesis performance on the ACID dataset. 256×256 (Standard) 512×512 (HRRC) 1024×1024 (HRRC) Average
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Cross datasets performance. Scannet DL3DV DTU Average
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Ablations study on various components. 256×256 (Standard) 512×512 (HRRC) 1024×1024 (HRRC) Average

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Both datasets provide precomputed camera poses and we adhere to the official train-test splits used in prior work. | embodiment, simulator version and control stack | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |
| Task/environment | (2014) dataset following MVSplat Chen et al. | reset, timeout, object/scene variation | p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This observation highlights a key limitation of conventional NVS metrics and underscores the value of our proposed HRRC metric, which drops significantly when surface ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENT) |
| This demonstrates the robustness of our learned geometric prior and the general applicability of our representation even under domain shift. | definition/direction/unit from same section | p. 9 (4 EXPERIMENT) |
| Note that yellow corresponds to near surfaces and blue denotes distant regions in depth map visualization. | definition/direction/unit from same section | p. 7 (4 EXPERIMENT) |
| All other layers are trained with a learning rate of 2 × 10-4. | definition/direction/unit from same section | p. 8 (4 EXPERIMENT) |
| 4.1 MAIN RESULTS Table 1: Novel view synthesis performance on the RealEstate10k dataset. | definition/direction/unit from same section | p. 8 (4 EXPERIMENT) |
| Across these experiments, the relative performance rankings remained fully consistent with those observed under HRRC evaluation, even without any bicubic upsampling. | definition/direction/unit from same section | p. 10 (4 EXPERIMENT) |
| 4.4 NORMAL AND MESH COMPARISON Since our method naturally predicts a surface orientation for each 2DGS, we additionally generate the corresponding normal maps and ... | definition/direction/unit from same section | p. 10 (4 EXPERIMENT) |
| To further demonstrate the scalability and generalization capability of our model, we train and evaluate an extended version at higher input resolution (256 × ... | definition/direction/unit from same section | p. 16 (A.3 EXTENDED RESULTS AT HIGHER RESOLUTION) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare our method to state-of-the-art sparse-view generalizable methods for novel view synthesis, including PixelSplat Charatan et al. | comparison identity and matched condition | p. 8 (4 EXPERIMENT) |
| Our proposed SurfSplat method consistently outperforms previous stateof-the-art methods across various metrics and datasets, especially under high-resolution rendering settings. | comparison identity and matched condition | p. 8 (4 EXPERIMENT) |
| Both datasets provide precomputed camera poses and we adhere to the official train-test splits used in prior work. | comparison identity and matched condition | p. 7 (4 EXPERIMENT) |
| We also train a variant with the surface continuity prior but without forced alpha blending. | comparison identity and matched condition | p. 9 (4 EXPERIMENT) |
| 4.2 ABLATION AND ANALYSIS Figure 5: Ablation study: Visualization of reconstructed 3D scenes. | comparison identity and matched condition | p. 9 (4 EXPERIMENT) |
| We provide a comparison with DepthSplat Yang et al. | comparison identity and matched condition | p. 10 (4 EXPERIMENT) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 5: Ablation study: Visualization of recon- structed 3D scenes. Our full model yields contin- uous and coherent surfaces, while ablated variants exhibit visible ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| We also train a variant with the surface continuity prior but without forced alpha blending. | component/input/data sensitivity | p. 9 (4 EXPERIMENT) |
| Table 6: Ablations study on hyperparameter sensitivity. 256×256 (Standard) 512×512 (HRRC) 1024×1024 (HRRC) Average | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| Across these experiments, the relative performance rankings remained fully consistent with those observed under HRRC evaluation, even without any bicubic upsampling. | component/input/data sensitivity | p. 10 (4 EXPERIMENT) |
| (2024b), but use a lower learning rate of 2 × 10-6 for the pretrained Depth Anything V2 backbone. | component/input/data sensitivity | p. 8 (4 EXPERIMENT) |
| Figure 2: Illustration for model architecture. Given sparse input images, our dual-path encoder processes them through both single-view and multi-view branches. The fused features ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the main contributions of this work are as follows: • We propose SurfSplat, a feedforward network that reconstructs 3D scenes using 2D ... | Since using more primitives generally improves performance, we focus our core comparisons on the latter group to ensure a fair comparison. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 16 (A.3 EXTENDED RESULTS AT HIGHER RESOLUTION), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT) |
| Primary metric/result | Interestingly, this variant still achieves competitive novel view synthesis (NVS) performance at the original resolution, despite producing visually noisy and discontinuous surfaces. | numeric claim only at cited anchor | p. 9 (4 EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 8 / 4 EXPERIMENT - extractive body cue:** 256×256 (Standard) 512×512 (HRRC) 1024×1024 (HRRC) Average Method PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ pixelSplat 26.049 0.862 0.137 25.782 ...
- **p. 8 / 4 EXPERIMENT - extractive body cue:** 256×256 (Standard) 512×512 (HRRC) 1024×1024 (HRRC) Average Method PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ pixelSplat 28.284 0.842 0.146 27.687 ...
- **p. 9 / 4 EXPERIMENT - extractive body cue:** 256×256 (Standard) 512×512 (HRRC) 1024×1024 (HRRC) Average Method PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ w/o FAB, SCP 26.925 0.880 ...
- **p. 16 / A.3 EXTENDED RESULTS AT HIGHER RESOLUTION - extractive body cue:** 256×448(Standard) 512×896(HRRC) 1024×1792(HRRC) Average Method PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ Ours-B 26.190 0.871 0.134 25.553 0.861 0.234 24.197 ...
- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** To address this, we adopt a coarse scale estimate based on image-space distances between neighboring pixels: ¯σ2 u, ¯σ2 v = t2 1x + t2 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | These limitations open opportunities for future research on joint pose elimination and compact, adaptive representations. | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | By introducing a surface continuity prior and a forced alpha blending strategy, our method addresses key limitations of previous approaches, eliminating surface discontinuities and ... | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | These artifacts reveal the limitations of previous feedforward 3DGS 8 | p. 8 (4 EXPERIMENT) |
| body limitation/failure cue | This observation highlights a key limitation of conventional NVS metrics and underscores the value of our proposed HRRC metric, which drops significantly when surface ... | p. 9 (4 EXPERIMENT) |
| body limitation/failure cue | Notably, DepthSplat, despite using the same encoder backbone as our method, fails to generate coherent geometry or consistent surface details, which highlights the effectiveness ... | p. 9 (4 EXPERIMENT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All other layers are trained with a learning rate of 2 × 10-4. | p. 8 (4 EXPERIMENT) |
| (2019) and optimized using AdamW Loshchilov & Hutter (2017) with a cosine learning rate schedule. | p. 8 (4 EXPERIMENT) |
| Both datasets provide precomputed camera poses and we adhere to the official train-test splits used in prior work. | p. 7 (4 EXPERIMENT) |
| Notably, DepthSplat, despite using the same encoder backbone as our method, fails to generate coherent geometry or consistent surface details, which highlights the effectiveness ... | p. 9 (4 EXPERIMENT) |
| We use a combination of mean squared error (MSE) and perceptual similarity (LPIPS): Lgs = M X m=1  MSE  Im render, Im gt  ... | p. 6 (3.1 PRELIMINARIES) |
| Given sparse input images, our dual-path encoder processes them through both single-view and multi-view branches. | p. 4 (3.1 PRELIMINARIES) |
| The local surface normal n ∈R3 is then computed as their cross product: n = t1 × t2 ∥t1 × t2∥. | p. 5 (3.1 PRELIMINARIES) |
| To define anisotropic scale S = diag(σu, σv, σw), we compute the variance of projected neighboring points along the rotated tangent axes tu, tv. | p. 5 (3.1 PRELIMINARIES) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5 CONCLUSION - extractive body cue:** These limitations open opportunities for future research on joint pose elimination and compact, adaptive representations.
- **p. 10 / 5 CONCLUSION - extractive body cue:** By introducing a surface continuity prior and a forced alpha blending strategy, our method addresses key limitations of previous approaches, eliminating surface discontinuities and overcoming ...
- **p. 8 / 4 EXPERIMENT - extractive body cue:** These artifacts reveal the limitations of previous feedforward 3DGS 8
- **p. 9 / 4 EXPERIMENT - extractive body cue:** This observation highlights a key limitation of conventional NVS metrics and underscores the value of our proposed HRRC metric, which drops significantly when surface continuity ...
- **p. 9 / 4 EXPERIMENT - extractive body cue:** Notably, DepthSplat, despite using the same encoder backbone as our method, fails to generate coherent geometry or consistent surface details, which highlights the effectiveness of ...

- **Evidence anchors reviewed:** datasets p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), metrics p. 9 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), baselines p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), results p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 16 (A.3 EXTENDED RESULTS AT HIGHER RESOLUTION), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
