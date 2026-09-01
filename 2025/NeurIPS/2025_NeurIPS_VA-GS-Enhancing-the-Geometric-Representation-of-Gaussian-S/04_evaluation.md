# Evaluation - VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via View Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ZnsR3waLUo; PDF retrieval source: https://openreview.net/pdf/74577aad9a08ae8d5d8bdf6091974f7d026891a3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments), p. 9 (5 Experiments), p. 9 (5 Experiments), p. 6 (5 Experiments)): Although our method is slightly slower than 3DGS [21] and 2DGS [16] due to the use of multi-view alignment, it achieves significant improvements in reconstruction quality over these earlier Gaussian-based ...

## Evaluation Body Digest

- **p. 6 / 5 Experiments - extractive PDF cue:** Following prior works [16, 55, 4, 56], we use 15 scenes from the DTU dataset and 6 scenes from the TNT dataset for evaluation.
- **p. 6 / 5 Experiments - extractive PDF cue:** For novel view synthesis, we use the Mip-NeRF 360 dataset [2], which contains large-scale indoor and outdoor scenes with complex lighting and fine-grained geometric details.
- **p. 9 / 5 Experiments - extractive PDF cue:** Consistent with our observations on the TNT dataset, our method recovers more accurate and complete surfaces in both foreground and background regions, whereas other methods ...
- **p. 7 / 5 Experiments - extractive PDF cue:** As shown in Table 1, our method achieves the lowest average Chamfer distance and ranks best across most scenes.
- **p. 7 / 5 Experiments - extractive PDF cue:** 2DGS GOF PGSR RaDe-GS Ours GS-Pull Figure 3: Visual comparison of surface reconstruction results on the TNT dataset.
- **p. 8 / 5 Experiments - extractive PDF cue:** We further evaluate our method on the TNT dataset [22], comparing it against both implicit and explicit surface reconstruction baselines.
- **p. 9 / 5 Experiments - extractive PDF cue:** 5.2 Ablation Studies Table 4: Ablations on the TNT dataset.
- **p. 8 / 5 Experiments - extractive PDF cue:** For example, GS-Pull [58] only reconstructs foreground objects and often generates overly smooth surfaces.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Although our method is slightly slower than 3DGS [21] and 2DGS [16] due to the use of multi-view alignment, it achieves significant improvements in ... | p. 8 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 2, our method achieves the best reconstruction performance among all competing approaches, including both implicit and explicit methods. | p. 8 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 1, our method achieves the lowest average Chamfer distance and ranks best across most scenes. | p. 7 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notably, the Mip-NeRF 360 itself achieves the highest average PSNR on indoor scenes but lags on SSIM and LPIPS. | p. 9 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method outperforms competitors on most metrics, demonstrating superior image fitting and generalization to unseen viewpoints. | p. 9 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 5 Experiments - extractive PDF cue:** Following prior works [16, 55, 4, 56], we use 15 scenes from the DTU dataset and 6 scenes from the TNT dataset for evaluation.
- **p. 6 / 5 Experiments - extractive PDF cue:** For novel view synthesis, we use the Mip-NeRF 360 dataset [2], which contains large-scale indoor and outdoor scenes with complex lighting and fine-grained geometric details.
- **p. 9 / 5 Experiments - extractive PDF cue:** Consistent with our observations on the TNT dataset, our method recovers more accurate and complete surfaces in both foreground and background regions, whereas other methods ...
- **p. 7 / 5 Experiments - extractive PDF cue:** As shown in Table 1, our method achieves the lowest average Chamfer distance and ranks best across most scenes.
- **p. 7 / 5 Experiments - extractive PDF cue:** 2DGS GOF PGSR RaDe-GS Ours GS-Pull Figure 3: Visual comparison of surface reconstruction results on the TNT dataset.
- **p. 8 / 5 Experiments - extractive PDF cue:** We further evaluate our method on the TNT dataset [22], comparing it against both implicit and explicit surface reconstruction baselines.
- **p. 9 / 5 Experiments - extractive PDF cue:** 5.2 Ablation Studies Table 4: Ablations on the TNT dataset.
- **p. 8 / 5 Experiments - extractive PDF cue:** For example, GS-Pull [58] only reconstructs foreground objects and often generates overly smooth surfaces.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Our method addresses illumination and boundary artifacts that previous methods fail to resolve. In this work, we propose a novel method for accurate ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of our method. The training includes five loss functions: LI, Lnc, Lns, Lp and Lf. The occlusion weight ω, visibility item υ ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: Visual comparison of surface reconstruction results on the TNT dataset. Our method can handle shadows and large indoor flat regions. GS-Pull reconstructs only ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Visual comparison of surface reconstruction results on the Mip-NeRF 360 dataset. Our approach effectively handles the challenges posed by cluttered lighting and boundaries. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative comparison of Chamfer distances on the DTU dataset. The best results are highlighted as 1st , 2nd and 3rd . ∗means that ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Quantitative comparison of F1-scores on the TNT dataset. The best results are highlighted as 1st , 2nd and 3rd . ∗means that the ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Quantitative comparison on the Mip-NeRF 360 dataset. The best results are highlighted as 1st , 2nd and 3rd . Outdoor scenes Indoor scenes ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 4: Ablations on the TNT dataset. Precision ↑Recall ↑F1-score ↑ Only LI 0.09 0.23 0.13 w/o edge item 0.49

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Following prior works [16, 55, 4, 56], we use 15 scenes from the DTU dataset and 6 scenes from the TNT dataset for evaluation. | embodiment, simulator version and control stack | p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Task/environment | For novel view synthesis, we use the Mip-NeRF 360 dataset [2], which contains large-scale indoor and outdoor scenes with complex lighting and fine-grained geometric ... | reset, timeout, object/scene variation | p. 6 (5 Experiments), p. 9 (5 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (4 Method), p. 5 (4 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1 Introduction), p. 5 (4 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Precision ↑Recall ↑F1-score ↑ Only LI 0.09 0.23 0.13 w/o edge item 0.49 0.59 0.53 w/o weight δ 0.50 0.59 0.53 w/o Lnc 0.48 ... | definition/direction/unit from same section | p. 9 (5 Experiments) |
| In addition to the F1-score, we also report Precision and Recall to provide a more comprehensive evaluation. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| Following established protocols [16, 55, 4, 56], we report Chamfer distance for surface reconstruction on the DTU dataset and F1-score for the TNT dataset. | definition/direction/unit from same section | p. 6 (5 Experiments) |
| Notably, while several Gaussian-based methods require less optimization time, they tend to produce results with much lower accuracy. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| Table 2: Quantitative comparison of F1-scores on the TNT dataset. The best results are highlighted as 1st , 2nd and 3rd . ∗means that ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Our overall pipeline, training strategy, and hyperparameter settings generally follow 3DGS [21]. | definition/direction/unit from same section | p. 6 (5 Experiments) |
| 5.1 Performance Evaluation Comparisons on DTU. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Then, we incorporate our image edge item and normal-based geometry alignment into the training. | definition/direction/unit from same section | p. 7 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We first compare our method with state-of-the-art implicit and explicit surface reconstruction approaches on the DTU dataset [18]. | comparison identity and matched condition | p. 7 (5 Experiments) |
| We further evaluate our method on the TNT dataset [22], comparing it against both implicit and explicit surface reconstruction baselines. | comparison identity and matched condition | p. 8 (5 Experiments) |
| It also effectively mitigates the impact of shadows, whereas baseline methods often yield noisy meshes or fail to capture geometric details. | comparison identity and matched condition | p. 8 (5 Experiments) |
| Our method outperforms competitors on most metrics, demonstrating superior image fitting and generalization to unseen viewpoints. | comparison identity and matched condition | p. 9 (5 Experiments) |
| Following prior works [16, 55, 4, 56], we use 15 scenes from the DTU dataset and 6 scenes from the TNT dataset for evaluation. | comparison identity and matched condition | p. 6 (5 Experiments) |
| 5.1 Performance Evaluation Comparisons on DTU. | comparison identity and matched condition | p. 7 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Our ablation results in Table 4 further confirm that flattening 3D Gaussians into planar Gaussian disks is ineffective for our framework. | component/input/data sensitivity | p. 9 (5 Experiments) |
| Precision ↑Recall ↑F1-score ↑ Only LI 0.09 0.23 0.13 w/o edge item 0.49 0.59 0.53 w/o weight δ 0.50 0.59 0.53 w/o Lnc 0.48 ... | component/input/data sensitivity | p. 9 (5 Experiments) |
| Figure 4: Visual comparison of surface reconstruction results on the Mip-NeRF 360 dataset. Our approach effectively handles the challenges posed by cluttered lighting and ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 2: Overview of our method. The training includes five loss functions: LI, Lnc, Lns, Lp and Lf. The occlusion weight ω, visibility item ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows. • Incorporating edge information and visibility-aware multi-view alignment to enhance surface boundary delineation and improve geometric consistency. • ... | Although our method is slightly slower than 3DGS [21] and 2DGS [16] due to the use of multi-view alignment, it achieves significant improvements in ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments), p. 9 (5 Experiments), p. 9 (5 Experiments), p. 6 (5 Experiments) |
| Primary metric/result | As shown in Table 2, our method achieves the best reconstruction performance among all competing approaches, including both implicit and explicit methods. | numeric claim only at cited anchor | p. 8 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 5 Experiments - extractive PDF cue:** Following prior works [16, 55, 4, 56], we use 15 scenes from the DTU dataset and 6 scenes from the TNT dataset for evaluation.
- **p. 6 / 5 Experiments - extractive PDF cue:** We set the number of source views to N = 3, the threshold in Lns 6
- **p. 7 / 5 Experiments - extractive PDF cue:** Our approach effectively handles the challenges posed by cluttered lighting and boundaries. to τ = 0.01, and the patch size in Lp to 7×7.
- **p. 7 / 5 Experiments - extractive PDF cue:** We first pretrain the model using only the color loss for 7,000 steps to obtain a coarse geometric initialization, which provides a stable foundation for ...
- **p. 7 / 5 Experiments - extractive PDF cue:** For novel view synthesis, we continue training for an additional 10,000 steps to optimize rendering quality.
- **p. 7 / 5 Experiments - extractive PDF cue:** All experiments are conducted on a single NVIDIA RTX 4090 GPU.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1: Our method addresses illumination and boundary artifacts that previous methods fail to resolve. In this work, we propose a novel method for ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | The definitions of υrs(pr) and ω(pr) are detailed in the following. • Due to viewpoint changes, a 2D pixel pr in the reference view ... | p. 5 (4 Method) |
| body limitation/failure cue | To address these limitations, we introduce a multi-view feature alignment loss. | p. 6 (4 Method) |
| body limitation/failure cue | Figure 2: Overview of our method. The training includes five loss functions: LI, Lnc, Lns, Lp and Lf. The occlusion weight ω, visibility item ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | However, image-based losses are susceptible to noise, blur, and low-texture regions. | p. 6 (4 Method) |
| body limitation/failure cue | It also effectively mitigates the impact of shadows, whereas baseline methods often yield noisy meshes or fail to capture geometric details. | p. 8 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our overall pipeline, training strategy, and hyperparameter settings generally follow 3DGS [21]. | p. 6 (5 Experiments) |
| All experiments are conducted on a single NVIDIA RTX 4090 GPU. | p. 7 (5 Experiments) |
| For novel view synthesis, we continue training for an additional 10,000 steps to optimize rendering quality. | p. 7 (5 Experiments) |
| The best results are highlighted as 1st , 2nd and 3rd . ∗means that the source code is not available. | p. 8 (5 Experiments) |
| To compute normal ˆ N, we first project four neighboring depth samples into 3D points in the camera coordinate system. | p. 5 (4 Method) |
| Given a pixel pr with rendered depth zr, its corresponding 3D point xr and projected pixel coordinate p′ s in the source view are ... | p. 6 (4 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Our method addresses illumination and boundary artifacts that previous methods fail to resolve. In this work, we propose a novel method for accurate ...
- **p. 5 / 4 Method - extractive PDF cue:** The definitions of υrs(pr) and ω(pr) are detailed in the following. • Due to viewpoint changes, a 2D pixel pr in the reference view may ...
- **p. 6 / 4 Method - extractive PDF cue:** To address these limitations, we introduce a multi-view feature alignment loss.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of our method. The training includes five loss functions: LI, Lnc, Lns, Lp and Lf. The occlusion weight ω, visibility item υ ...
- **p. 6 / 4 Method - extractive PDF cue:** However, image-based losses are susceptible to noise, blur, and low-texture regions.
- **p. 8 / 5 Experiments - extractive PDF cue:** It also effectively mitigates the impact of shadows, whereas baseline methods often yield noisy meshes or fail to capture geometric details.

- **PDF anchors reviewed:** datasets p. 6 (5 Experiments), p. 6 (5 Experiments), p. 9 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), metrics p. 9 (5 Experiments), p. 9 (5 Experiments), p. 6 (5 Experiments), p. 8 (5 Experiments), p. 8 (Figure/Table caption), p. 6 (5 Experiments), baselines p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), results p. 8 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments), p. 9 (5 Experiments), p. 9 (5 Experiments), p. 6 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
