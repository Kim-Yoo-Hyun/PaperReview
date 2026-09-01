# Evaluation - MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_MGSR_2D3D_Mutual-boosted_Gaussian_Splatting_for_High-fidelity_Surface_Reconstruction_under_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_MGSR_2D3D_Mutual-boosted_Gaussian_Splatting_for_High-fidelity_Surface_Reconstruction_under_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (Figure/Table caption), p. 8 (4.2. Results), p. 7 (4.2. Results), p. 6 (Figure/Table caption), p. 6 (4.1. Datasets and evaluation metrics), p. 7 (4.1. Datasets and evaluation metrics)): Figure 1. MGSR achieves strong NVS and SR results compared with methods based on 2DGS [6] and 3DGS [24]. The input consists of multi-view images captured from various camera positions ...

## Evaluation Body Digest

- **p. 6 / 4.1. Datasets and evaluation metrics - extractive PDF cue:** DTU [7] is a large MVS dataset, where some scenes feature unfavorable light conditions for surface reconstruction, such as overexposure, underexposure, and metallic reflections.
- **p. 7 / 4.1. Datasets and evaluation metrics - extractive PDF cue:** Visual comparisons on Ref-NeRF Real Captured Scenes dataset (Sedan) [21] and TnT dataset (Truck) [7].
- **p. 8 / 4.2. Results - extractive PDF cue:** Ablations of loss weights (Models A-F), iterations of mutual-boosted optimization (Models G-J), bidrectional BP and auto-stop warm-up strategy (Models K-L) on OmniObject3D dataset.
- **p. 6 / 4.1. Datasets and evaluation metrics - extractive PDF cue:** RefNeRF Real Captured Scenes [21] consists of three in-thewild scenes with strong reflections.
- **p. 7 / 4.1. Datasets and evaluation metrics - extractive PDF cue:** Since GT mesh is unavailable for real-world data, only visual comparisons are provided.
- **p. 8 / 4.2. Results - extractive PDF cue:** Instance-level Normal Consistency results of SR on DTU dataset.
- **p. 6 / 4.1. Datasets and evaluation metrics - extractive PDF cue:** We utilize SSIM and PSNR to evaluate the rendering quality, while reconstruction accuracy is validated by 10K sampled points with Normal Consistency (NC) and Chamfer ...
- **p. 7 / 4.2. Results - extractive PDF cue:** MGSR visually outperforms all baselines, resulting in the best NC, with smooth surfaces and accurate color modeling.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Datasets and evaluation metrics (p. 6); 4.2. Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. MGSR achieves strong NVS and SR results compared with methods based on 2DGS [6] and 3DGS [24]. The input consists of multi-view ... | p. 2 (Figure/Table caption) |
| 4.2. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | MGSR, supported by an auto-stop warm-up strategy, outperforms GOF and achieves a comparable speed with 2DGS. | p. 8 (4.2. Results) |
| 4.2. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | MGSR visually outperforms all baselines, resulting in the best NC, with smooth surfaces and accurate color modeling. | p. 7 (4.2. Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5. Visual comparisons on the Shiny Blender dataset [21]. other hand, a depth loss between 2DGS and 3DGS branches is introduced to improve ... | p. 6 (Figure/Table caption) |
| 4.1. Datasets and evaluation metrics | EMPIRICAL / REAL-ROBOT OR HARDWARE | We utilize SSIM and PSNR to evaluate the rendering quality, while reconstruction accuracy is validated by 10K sampled points with Normal Consistency (NC) and ... | p. 6 (4.1. Datasets and evaluation metrics) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Datasets and evaluation metrics - extractive PDF cue:** DTU [7] is a large MVS dataset, where some scenes feature unfavorable light conditions for surface reconstruction, such as overexposure, underexposure, and metallic reflections.
- **p. 7 / 4.1. Datasets and evaluation metrics - extractive PDF cue:** Visual comparisons on Ref-NeRF Real Captured Scenes dataset (Sedan) [21] and TnT dataset (Truck) [7].
- **p. 8 / 4.2. Results - extractive PDF cue:** Ablations of loss weights (Models A-F), iterations of mutual-boosted optimization (Models G-J), bidrectional BP and auto-stop warm-up strategy (Models K-L) on OmniObject3D dataset.
- **p. 6 / 4.1. Datasets and evaluation metrics - extractive PDF cue:** RefNeRF Real Captured Scenes [21] consists of three in-thewild scenes with strong reflections.
- **p. 7 / 4.1. Datasets and evaluation metrics - extractive PDF cue:** Since GT mesh is unavailable for real-world data, only visual comparisons are provided.
- **p. 8 / 4.2. Results - extractive PDF cue:** Instance-level Normal Consistency results of SR on DTU dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. MGSR achieves strong NVS and SR results compared with methods based on 2DGS [6] and 3DGS [24]. The input consists of multi-view images ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. MGSR is a 2D/3D mutual-boosted framework with two branches: 2DGS branch (upper) for SR and 3DGS branch (bottom) for NVS. Each branch is ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Geometry enhancement in 3DGS branch for realistic rendering through our mutual-boosted optimization. information for the 3DGS branch for better illumination de- composition. Specifically, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Visual comparisons on the OmniObject3D dataset [22]. Input images NeuS2 2D-GS GOF MGSR (Ours) Coffee MuscleCar
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Visual comparisons on the Shiny Blender dataset [21]. other hand, a depth loss between 2DGS and 3DGS branches is introduced to improve the ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. NVS results on Shiny Blender and OmniObject3D. The instance-level metrics are listed in Appendix. Methods Shiny Blender OmniObject3D SSIM↑ PSNR↑ SSIM↑
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Visual comparisons on DTU dataset [7]. Truck Sedan Input images MGSR (Ours) GOF 2D-GS
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 7. Visual comparisons on Ref-NeRF Real Captured Scenes dataset (Sedan) [21] and TnT dataset (Truck) [7].

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | DTU [7] is a large MVS dataset, where some scenes feature unfavorable light conditions for surface reconstruction, such as overexposure, underexposure, and metallic reflections. | embodiment, simulator version and control stack | p. 6 (4.1. Datasets and evaluation metrics), p. 7 (4.1. Datasets and evaluation metrics) |
| Task/environment | Visual comparisons on Ref-NeRF Real Captured Scenes dataset (Sedan) [21] and TnT dataset (Truck) [7]. | reset, timeout, object/scene variation | p. 7 (4.1. Datasets and evaluation metrics), p. 8 (4.2. Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2. Illumination decomposition with 3DGS), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We utilize SSIM and PSNR to evaluate the rendering quality, while reconstruction accuracy is validated by 10K sampled points with Normal Consistency (NC) and ... | definition/direction/unit from same section | p. 6 (4.1. Datasets and evaluation metrics) |
| Ablations of loss weights (Models A-F), iterations of mutual-boosted optimization (Models G-J), bidrectional BP and auto-stop warm-up strategy (Models K-L) on OmniObject3D dataset. | definition/direction/unit from same section | p. 8 (4.2. Results) |
| MGSR visually outperforms all baselines, resulting in the best NC, with smooth surfaces and accurate color modeling. | definition/direction/unit from same section | p. 7 (4.2. Results) |
| Under varying light conditions, MGSR successfully reconstructs realistic and intact surfaces compared to 2DGS and GOF. | definition/direction/unit from same section | p. 7 (4.2. Results) |
| MGSR, supported by an auto-stop warm-up strategy, outperforms GOF and achieves a comparable speed with 2DGS. | definition/direction/unit from same section | p. 8 (4.2. Results) |
| Figure 1. MGSR achieves strong NVS and SR results compared with methods based on 2DGS [6] and 3DGS [24]. The input consists of multi-view ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 2. MGSR is a 2D/3D mutual-boosted framework with two branches: 2DGS branch (upper) for SR and 3DGS branch (bottom) for NVS. Each branch ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 5. Visual comparisons on the Shiny Blender dataset [21]. other hand, a depth loss between 2DGS and 3DGS branches is introduced to improve ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| MGSR visually outperforms all baselines, resulting in the best NC, with smooth surfaces and accurate color modeling. | comparison identity and matched condition | p. 7 (4.2. Results) |
| Similar to previous baselines [6, 24], we utilized the same 15 scans from the DTU dataset to validate our approach. | comparison identity and matched condition | p. 6 (4.1. Datasets and evaluation metrics) |
| MGSR surpasses all baselines in terms of the PSNR metric for NVS and the NC metric for SR. | comparison identity and matched condition | p. 7 (4.2. Results) |
| In Table 1 and Table 2, we additionally present the optimization time for all compared methods. | comparison identity and matched condition | p. 8 (4.2. Results) |
| By eliminating the dependence on BRDF, MGSR is faster than all illumination decomposition baselines. | comparison identity and matched condition | p. 8 (4.2. Results) |
| Figure 1. MGSR achieves strong NVS and SR results compared with methods based on 2DGS [6] and 3DGS [24]. The input consists of multi-view ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 2. MGSR is a 2D/3D mutual-boosted framework with two branches: 2DGS branch (upper) for SR and 3DGS branch (bottom) for NVS. Each branch ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| The best-performing model in each ablation study is highlighted. | component/input/data sensitivity | p. 8 (4.2. Results) |
| Ablations of loss weights (Models A-F), iterations of mutual-boosted optimization (Models G-J), bidrectional BP and auto-stop warm-up strategy (Models K-L) on OmniObject3D dataset. | component/input/data sensitivity | p. 8 (4.2. Results) |
| Figure 3. Geometry enhancement in 3DGS branch for realistic rendering through our mutual-boosted optimization. information for the 3DGS branch for better illumination de- composition. ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To solve these contradictions, we propose MGSR, a 2D/3D Mutual-boosted Gaussian splatting for Surface Reconstruction that enhances both rendering quality and 3D reconstruction accuracy ... | Figure 1. MGSR achieves strong NVS and SR results compared with methods based on 2DGS [6] and 3DGS [24]. The input consists of multi-view ... | PDF body cue; verify exact table/figure and matched conditions | p. 2 (Figure/Table caption), p. 8 (4.2. Results), p. 7 (4.2. Results), p. 6 (Figure/Table caption), p. 6 (4.1. Datasets and evaluation metrics), p. 7 (4.1. Datasets and evaluation metrics) |
| Primary metric/result | MGSR, supported by an auto-stop warm-up strategy, outperforms GOF and achieves a comparable speed with 2DGS. | numeric claim only at cited anchor | p. 8 (4.2. Results) |

- Numeric sentences retained from the body:
- **p. 7 / 4.2. Results - extractive PDF cue:** Three objects from the Shiny Blender with reflections and 30 objects from OmniObject3D with highlights are conducted on all methods for comparison.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | To address this issue, NC is introduced as an evaluation metric for reconstruction, overcoming the limitations of CDs, which fail to capture surface holes ... | p. 7 (4.2. Results) |
| body limitation/failure cue | A possible way for addressing this issue is to incorporate exposure compensation for input images, which we will investigate as a future work. | p. 8 (6. Conclusion) |
| body limitation/failure cue | Due to the limitation of CD, we mainly focus on NC metric, which aligns better 27300 | p. 6 (4.1. Datasets and evaluation metrics) |
| body limitation/failure cue | Previous GS-based methods fail to effectively reconstruct glass or mirror surfaces, resulting in damaged and inaccurate surfaces. | p. 7 (4.2. Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Lrender = λ1L1(C, CGT) + (1 -λ1)LD-SSIM(C, CGT), (5) where λ1 represents to the balance coefficient, L1 computes the absolute error, while LD-SSIM refers ... | p. 4 (3.2. Illumination decomposition with 3DGS) |
| As an initial estimate, the rendering depth map Z is computed as a weighted sum of the normalized intersected depths z, as depicted in: ... | p. 4 (3.3. Surface reconstruction with 2DGS) |
| Lmutual denotes the rendering loss between the 2DGS branch rendered images and the transmitted images from the 3DGS branch, L2D-render is the rendering loss ... | p. 5 (3.4. Alternating optimization of 2D & 3D Gaussians) |
| The normals of the 2D splats are encouraged to be aligned with the gradients of the depth maps, as shown in: Ln = X ... | p. 5 (3.3. Surface reconstruction with 2DGS) |
| The depth loss LZ is computed by: LZ = γL2(Z2D, Z3D), (14) where L2 denotes the L2 loss, and Z2D is the estimated depth ... | p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.2. Results - extractive PDF cue:** To address this issue, NC is introduced as an evaluation metric for reconstruction, overcoming the limitations of CDs, which fail to capture surface holes or ...
- **p. 8 / 6. Conclusion - extractive PDF cue:** A possible way for addressing this issue is to incorporate exposure compensation for input images, which we will investigate as a future work.
- **p. 6 / 4.1. Datasets and evaluation metrics - extractive PDF cue:** Due to the limitation of CD, we mainly focus on NC metric, which aligns better 27300
- **p. 7 / 4.2. Results - extractive PDF cue:** Previous GS-based methods fail to effectively reconstruct glass or mirror surfaces, resulting in damaged and inaccurate surfaces.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Datasets and evaluation metrics), p. 7 (4.1. Datasets and evaluation metrics), p. 8 (4.2. Results), p. 6 (4.1. Datasets and evaluation metrics), p. 7 (4.1. Datasets and evaluation metrics), p. 8 (4.2. Results), metrics p. 6 (4.1. Datasets and evaluation metrics), p. 8 (4.2. Results), p. 7 (4.2. Results), p. 7 (4.2. Results), p. 8 (4.2. Results), p. 2 (Figure/Table caption), baselines p. 7 (4.2. Results), p. 6 (4.1. Datasets and evaluation metrics), p. 7 (4.2. Results), p. 8 (4.2. Results), p. 8 (4.2. Results), p. 2 (Figure/Table caption), results p. 2 (Figure/Table caption), p. 8 (4.2. Results), p. 7 (4.2. Results), p. 6 (Figure/Table caption), p. 6 (4.1. Datasets and evaluation metrics), p. 7 (4.1. Datasets and evaluation metrics).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
