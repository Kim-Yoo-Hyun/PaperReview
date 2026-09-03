# Evaluation - DiGA3D: Coarse-to-Fine Diffusional Propagation of Geometry and Appearance for Versatile 3D Inpainting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Experimental Setup), p. 8 (4.4. Ablation Study), p. 7 (4.3.1. Object Removal), p. 8 (4.4. Ablation Study), p. 7 (4.3.3. Object Replacement), p. 4 (Figure/Table caption)): Our method achieves clear improvements in PSNR and obtains better scores in most metrics.

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We evaluate our versatile 3D inpainting methods in three different datasets with multi-view images from feed-forward and 360 degrees: 1) SPIn-NeRF dataset [25] provide 10 ...
- **p. 7 / 4.3.1. Object Removal - extractive body cue:** 5 presents qualitative results across three scenes from the SPIn-NeRF dataset.
- **p. 7 / 4.3.2. Object Re-Texturing - extractive body cue:** For the CLIPdir scores, we averaged the scores across six scenes from the SPIn-NeRF [25] and MipNeRF360 [1] datasets.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** 1) For the object removal task, we evaluate our method using PSNR, SSIM, and LPIPS scores on the SPIn-NeRF dataset [25].
- **p. 8 / 4.3.3. Object Replacement - extractive body cue:** The quantitative ablation study of key components on the object removal task using SPIn-NeRF dataset [25].
- **p. 8 / 4.3.3. Object Replacement - extractive body cue:** The visualization of ablation study for key components on the object replacement task using LLFF dataset [22].
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Qualitative results of the object re-texturing task.
- **p. 6 / 4.3. Results - extractive body cue:** We primarily provide quantitative and qualitative comparisons of three inpainting tasks, i.e., object removal, object 16350

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiment (p. 5); 4.1. Experimental Setup (p. 5); 4.3. Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Experimental Setup | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method achieves clear improvements in PSNR and obtains better scores in most metrics. | p. 6 (4.1. Experimental Setup) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | By integrating DDIM inversion and AFP within the 2D inpainter, we achieve a notable 0.21 improvement in PSNR, indicating significant enhancements. | p. 8 (4.4. Ablation Study) |
| 4.3.1. Object Removal | EMPIRICAL / SOURCE-REPORTED EVALUATION | While our rendering results exhibit some limitations in the masked LPIPS compared to GScream, we achieve a comparable score in this metric and show ... | p. 7 (4.3.1. Object Removal) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | By employing AFP, we have significantly improved the issue of inconsistencies, although some artifacts and texture details still lack consistency. | p. 8 (4.4. Ablation Study) |
| 4.3.3. Object Replacement | EMPIRICAL / SOURCE-REPORTED EVALUATION | We find that our methods achieve relatively high scores compared to other approaches, demonstrating that they can generate more realistic and relevant objects with ... | p. 7 (4.3.3. Object Replacement) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We evaluate our versatile 3D inpainting methods in three different datasets with multi-view images from feed-forward and 360 degrees: 1) SPIn-NeRF dataset [25] provide 10 ...
- **p. 7 / 4.3.1. Object Removal - extractive body cue:** 5 presents qualitative results across three scenes from the SPIn-NeRF dataset.
- **p. 7 / 4.3.2. Object Re-Texturing - extractive body cue:** For the CLIPdir scores, we averaged the scores across six scenes from the SPIn-NeRF [25] and MipNeRF360 [1] datasets.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** 1) For the object removal task, we evaluate our method using PSNR, SSIM, and LPIPS scores on the SPIn-NeRF dataset [25].
- **p. 8 / 4.3.3. Object Replacement - extractive body cue:** The quantitative ablation study of key components on the object removal task using SPIn-NeRF dataset [25].
- **p. 8 / 4.3.3. Object Replacement - extractive body cue:** The visualization of ablation study for key components on the object replacement task using LLFF dataset [22].
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Qualitative results of the object re-texturing task.
- **p. 6 / 4.3. Results - extractive body cue:** We primarily provide quantitative and qualitative comparisons of three inpainting tasks, i.e., object removal, object 16350

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. DiGA3D is a versatile 3D inpainting framework guided by text prompts, supporting multiple inpainting tasks including ob- ject replacement, removal, and re-texturing, etc. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Our proposed framework. Before performing 3D inpainting, we first calculate the camera pose using COLMAP [32] and extract masks from mask prompts Tm. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. (a) The illustration of the proposed Attention Feature Propagation (AFP). The outputs of AFP are the inpainted image Ii and the depth map ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Illustration of the multi-view consistent image inpainting with DDIM inversion and the AFP module in Sec. 3.3. 3D Gaussians (see Sec. 3.3). In ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative results of the object removal task. For each scene, we present two novel views to compare the rendering quality and multi-view consistency ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Qualitative results of the object re-texturing task. For each scene, we present two novel views to compare the rendering quality and multi-view consistency ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative results of the object removal task. We compared our method with four baselines, i.e., SPIn-NeRF [25], NeRFiller [38], MVIP-NeRF [7], and GScream ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Quantitative results of object re-texturing and re- placement. We compared our method with three competitors, i.e., Instruct-NeRF2NeRF (IN2N) [12], GaussianEditor [8], and GaussCtrl ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our versatile 3D inpainting methods in three different datasets with multi-view images from feed-forward and 360 degrees: 1) SPIn-NeRF dataset [25] provide ... | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setup), p. 7 (4.3.1. Object Removal) |
| Task/environment | 5 presents qualitative results across three scenes from the SPIn-NeRF dataset. | reset, timeout, object/scene variation | p. 7 (4.3.1. Object Removal), p. 7 (4.3.2. Object Re-Texturing) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 3 (3.2. Problem formulation and overview), p. 3 (3.2. Problem formulation and overview) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 5 (3.4. Texture-Geometry Guided SDS Loss), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We find that our methods achieve relatively high scores compared to other approaches, demonstrating that they can generate more realistic and relevant objects with ... | definition/direction/unit from same section | p. 7 (4.3.3. Object Replacement) |
| 1) For the object removal task, we evaluate our method using PSNR, SSIM, and LPIPS scores on the SPIn-NeRF dataset [25]. | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| 2) For object re-texturing and replacement tasks, we follow established practices by calculating the CLIP score and 16349 | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| Our method achieves clear improvements in PSNR and obtains better scores in most metrics. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| 2 presents the CLIPdir scores and the results of the user study. | definition/direction/unit from same section | p. 7 (4.3.2. Object Re-Texturing) |
| Quantitative Analysis of Hyperparameter K in Refer- (a) Depth map (w/o TG-SDS loss) (b) Depth map (w/ TG-SDS loss) (c) Point cloud (w/o TG-SDS ... | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| Figure 9. Qualitative ablation study for the proposed TG-SDS op- timization loss on the SPIn-NeRF dataset [25]. ence View Selection. When using K-means for ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| To generate 2D masks for inpainting, we utilize Lang SAM [14] based on mask prompts. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compared our method with four baselines, i.e., SPIn-NeRF [25], NeRFiller [38], MVIP-NeRF [7], and GScream [37]. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| Quantitative and qualitative comparisons between our method and three baseline methods are illustrated in Tab. | comparison identity and matched condition | p. 7 (4.3.1. Object Removal) |
| We compared our method with three competitors, i.e., Instruct-NeRF2NeRF (IN2N) [12], GaussianEditor [8], and GaussCtrl [39]. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| The results indicate that our methods also exhibit advantages compared to other methods. | comparison identity and matched condition | p. 7 (4.3.2. Object Re-Texturing) |
| In the baseline, we solely utilize the 2D inpainter [42, 47] and depend on the convergence of 3D representations. | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |
| 3, we gradually assess our baseline (w/o AFP & TGSDS loss), coarse stage (w/o TG-SDS loss), and our fine stage (full model). | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The visualization of ablation study for key components on the object replacement task using LLFF dataset [22]. | component/input/data sensitivity | p. 8 (4.3.3. Object Replacement) |
| 8, we depict the visualizations of the ablation study on key components. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| We evaluate our versatile 3D inpainting methods in three different datasets with multi-view images from feed-forward and 360 degrees: 1) SPIn-NeRF dataset [25] provide ... | component/input/data sensitivity | p. 5 (4.1. Experimental Setup) |
| For each scene, we present two novel views to compare the rendering quality and multi-view consistency with the existing state-of-the-art methods. re-texturing, and object ... | component/input/data sensitivity | p. 7 (4.3. Results) |
| 2) For object re-texturing and replacement tasks, we follow established practices by calculating the CLIP score and 16349 | component/input/data sensitivity | p. 5 (4.1. Experimental Setup) |
| Quantitative results of object re-texturing and replacement. | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our key contributions can be outlined as follows: • We introduce DiGA3D, a versatile 3D inpainting pipeline that leverages diffusion models to ... | Our method achieves clear improvements in PSNR and obtains better scores in most metrics. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Experimental Setup), p. 8 (4.4. Ablation Study), p. 7 (4.3.1. Object Removal), p. 8 (4.4. Ablation Study), p. 7 (4.3.3. Object Replacement), p. 4 (Figure/Table caption) |
| Primary metric/result | By integrating DDIM inversion and AFP within the 2D inpainter, we achieve a notable 0.21 improvement in PSNR, indicating significant enhancements. | numeric claim only at cited anchor | p. 8 (4.4. Ablation Study) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We evaluate our versatile 3D inpainting methods in three different datasets with multi-view images from feed-forward and 360 degrees: 1) SPIn-NeRF dataset [25] provide 10 ...
- **p. 2 / 3.1. Preliminary - extractive body cue:** The Gaussian ellipse is calculated as G(x) = e-1 2 xT Σ-1x, where x is the displacement from the center µ.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While our rendering results exhibit some limitations in the masked LPIPS compared to GScream, we achieve a comparable score in this metric and show ... | p. 7 (4.3.1. Object Removal) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4, we achieve this balance by choosing K = 3 for our experiments on the SPIn-NeRF [25], which ensures both high performance and the ... | p. 8 (4.4. Ablation Study) |
| Our method is trained on a single NVIDIA 48GB A6000 GPU. | p. 6 (4.1. Experimental Setup) |
| We evaluate different values of K on Scene 1 of the SPIn-NeRF [25] dataset using a single A6000 GPU. | p. 8 (4.3.3. Object Replacement) |
| By rendering a random view through a differentiable renderer g(·), SDS updates the parameter θ by randomly selecting timesteps t ∼U(tmin, tmax) and forwarding ... | p. 3 (3.1. Preliminary) |
| Next, we decode inpainted latents to produce coarsely consistent inpainted results for training the 3D Gaussians. | p. 4 (3.3. Multi-view Consistent Image Inpainting) |
| To further assist in improving appearance consistency, we encode the already inpainted image Ip within the multi-view sequence using the CLIP Vision model [29] ... | p. 4 (3.3. Multi-view Consistent Image Inpainting) |
| After acquiring conditional images with both texture and geometry details, i.e., the texture maps and depth maps derived from texture-geometry warping, we employ them ... | p. 5 (3.4. Texture-Geometry Guided SDS Loss) |
| We then compute a wrapped pixel qRj→i as follows: \lab e l {eq: wa rp} q_ {{R_j} \rightarrow i} = \mathbf {K}\mathbf {P_i}\mathbf {P_{R_j}^{-1}}\mathbf ... | p. 5 (3.4. Texture-Geometry Guided SDS Loss) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.3.1. Object Removal - extractive body cue:** While our rendering results exhibit some limitations in the masked LPIPS compared to GScream, we achieve a comparable score in this metric and show significant ...

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Experimental Setup), p. 7 (4.3.1. Object Removal), p. 7 (4.3.2. Object Re-Texturing), p. 5 (4.1. Experimental Setup), p. 8 (4.3.3. Object Replacement), p. 8 (4.3.3. Object Replacement), metrics p. 7 (4.3.3. Object Replacement), p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.3.2. Object Re-Texturing), p. 8 (4.4. Ablation Study), baselines p. 6 (4.1. Experimental Setup), p. 7 (4.3.1. Object Removal), p. 6 (4.1. Experimental Setup), p. 7 (4.3.2. Object Re-Texturing), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), results p. 6 (4.1. Experimental Setup), p. 8 (4.4. Ablation Study), p. 7 (4.3.1. Object Removal), p. 8 (4.4. Ablation Study), p. 7 (4.3.3. Object Replacement), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
