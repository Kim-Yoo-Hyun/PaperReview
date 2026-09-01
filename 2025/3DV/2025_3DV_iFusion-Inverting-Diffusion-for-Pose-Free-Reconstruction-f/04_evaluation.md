# Evaluation - iFusion: Inverting Diffusion for Pose-Free Reconstruction from Sparse Views

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=W7vOFBCGPm&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.1. Experimental Setup), p. 6 (4.2. Experimental Result), p. 8 (4.3. Ablation Study), p. 5 (4.2. Experimental Result), p. 6 (4.2. Experimental Result), p. 7 (4.3. Ablation Study)): Evaluation results on pose estimation. iFusion achieves significant improvements for all metrics under 2 input views.

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** Datasets We conduct experiments using two publicly available object datasets: Google Scanned Object (GSO) [9] and OmniObject3D (OO3D) [73].
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** For pose estimation experiments, we render five views per object, accumulating 1, 400 views in total with their corresponding camera poses for each dataset.
- **p. 6 / 4.2. Experimental Result - extractive PDF cue:** In addition, iFusion clearly outperforms other noneoptimization-based methods Point-E [42] and Shape-E [21], which are trained on a large-scale private dataset.
- **p. 6 / 4.2. Experimental Result - extractive PDF cue:** Dataset Method PSNR↑ SSIM↑ LPIPS↓ GSO [9] FORGE [19] 10.45 0.673 0.449 LEAP [20] 12.51 0.751 0.312 Zero123 [31] 15.40 0.788 0.184 iFusion 18.73 0.836 ...
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** 3D Reconstruction We validate the proposed components contributing to reconstruction in Table 7, using DreamGaussian as the reconstruction module on the OO3D dataset.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** Sparse-view Fine-tuning Table 6 assesses the efficacy of the proposed fine-tuning stage for object-specific novel view synthesis.
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** Finally, fine-tuning via LoRA demonstrates an additional improvement in customizing the model for faithful reconstruction of the given object.
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** For 3D reconstruction, we report Chamfer Distances and volumetric IoU between ground truth shapes and reconstructed ones.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setup (p. 5); 4.2. Experimental Result (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Experimental Setup | EMPIRICAL / SOURCE-REPORTED EVALUATION | Evaluation results on pose estimation. iFusion achieves significant improvements for all metrics under 2 input views. | p. 5 (4.1. Experimental Setup) |
| 4.2. Experimental Result | EMPIRICAL / SOURCE-REPORTED EVALUATION | Moreover, iFusion significantly outperforms all methods on all metrics. | p. 6 (4.2. Experimental Result) |
| 4.3. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | Incorporating stochastic multi-view conditioning (MVC) further improves the performance, as evident in row (c). | p. 8 (4.3. Ablation Study) |
| 4.2. Experimental Result | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4, where all samples show several cameras on the opposite sides to the camera reference (red camera) and iFusion still achieves accurate estimations. | p. 5 (4.2. Experimental Result) |
| 4.2. Experimental Result | EMPIRICAL / SOURCE-REPORTED EVALUATION | In contrast, our iFusion improves novel views' image fidelity by conditioning on an additional pose-free view. | p. 6 (4.2. Experimental Result) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** Datasets We conduct experiments using two publicly available object datasets: Google Scanned Object (GSO) [9] and OmniObject3D (OO3D) [73].
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** For pose estimation experiments, we render five views per object, accumulating 1, 400 views in total with their corresponding camera poses for each dataset.
- **p. 6 / 4.2. Experimental Result - extractive PDF cue:** In addition, iFusion clearly outperforms other noneoptimization-based methods Point-E [42] and Shape-E [21], which are trained on a large-scale private dataset.
- **p. 6 / 4.2. Experimental Result - extractive PDF cue:** Dataset Method PSNR↑ SSIM↑ LPIPS↓ GSO [9] FORGE [19] 10.45 0.673 0.449 LEAP [20] 12.51 0.751 0.312 Zero123 [31] 15.40 0.788 0.184 iFusion 18.73 0.836 ...
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** 3D Reconstruction We validate the proposed components contributing to reconstruction in Table 7, using DreamGaussian as the reconstruction module on the OO3D dataset.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** Sparse-view Fine-tuning Table 6 assesses the efficacy of the proposed fine-tuning stage for object-specific novel view synthesis.
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** Finally, fine-tuning via LoRA demonstrates an additional improvement in customizing the model for faithful reconstruction of the given object.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Demonstration on real-world 3D reconstruction. With only two casually taken photos without camera poses, iFusion can reconstruct plausible 3D assets. The top row ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Zero123 vs. iFusion. Unlike Zero123 [31] (left), which synthesizes an object's novel view given an image and a transfor- mation T, iFusion (right) ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. iFusion framework. (a) Given as few as two pose-free images (xr, xq), we estimate the pose ˆTr→q from T0 to optimally recon- struct ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative results on pose estimation. We visualize the predicted poses (thin) alongside the ground truth (bold), using the same color, while the reference ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Evaluation results on pose estimation. iFusion achieves significant improvements for all metrics under 2 input views.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative examples on novel view synthesis. iFusion takes two unposed images and Zero123 [31] only conditions on the first view. We observe that ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Novel view synthesis results. iFusion performed signifi- cantly better than the original Zero123 and 3D-based methods.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Qualitative comparison of surface reconstruction. It is clear that iFusion significantly enhances existing reconstruction methods including Zero123-SDS [31], DreamGaussian [64], and Magic123 [48], ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Datasets We conduct experiments using two publicly available object datasets: Google Scanned Object (GSO) [9] and OmniObject3D (OO3D) [73]. | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Task/environment | For pose estimation experiments, we render five views per object, accumulating 1, 400 views in total with their corresponding camera poses for each dataset. | reset, timeout, object/scene variation | p. 5 (4.1. Experimental Setup), p. 6 (4.2. Experimental Result) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 4 (3.1. Diffusion as a Pose Estimator), p. 2 (1. Introduction) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 3 (2. Preliminary), p. 3 (3.1. Diffusion as a Pose Estimator) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For 3D reconstruction, we report Chamfer Distances and volumetric IoU between ground truth shapes and reconstructed ones. | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| For pose estimation, we report the median error in rotation and translation along with a recall evaluation with a 5◦threshold for both, i.e., we ... | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| Finally, row (e) underscores the potential for achieving higher-quality synthesis by incorporating more views. | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| Based on Table 4, we employed n = 4 initial poses for a better trade-off between speed and accuracy for all experiments unless otherwise ... | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| Table 6. Ablation of novel view synthesis on GSO [9]. Multi- view conditioning and LoRA [15] finetuning are validated. In- creased views also improve ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Ablation of t annealing for pose estimation on GSO [9]. n poses t annealing Recall ↑ 5◦ 10◦ 20◦ (a) 4 - 48.61 56.67 ... | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| 6, the incorporation of iFusion enhances the performance of all reconstruction modules by a large margin. | definition/direction/unit from same section | p. 6 (4.2. Experimental Result) |
| We observe that iFusion effectively leverages the additional images without camera poses and generates more faithful images. | definition/direction/unit from same section | p. 6 (4.2. Experimental Result) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Ablation of t annealing for pose estimation on GSO [9]. n poses t annealing Recall ↑ 5◦ 10◦ 20◦ (a) 4 - 48.61 56.67 ... | comparison identity and matched condition | p. 8 (4.3. Ablation Study) |
| Notably, COLMAP [55] cannot serve as a baseline in our evaluation due to the structural limitations of Structure-from-Motion, which requires a large number of ... | comparison identity and matched condition | p. 5 (4.2. Experimental Result) |
| Moreover, iFusion significantly outperforms all methods on all metrics. | comparison identity and matched condition | p. 6 (4.2. Experimental Result) |
| In addition, iFusion clearly outperforms other noneoptimization-based methods Point-E [42] and Shape-E [21], which are trained on a large-scale private dataset. | comparison identity and matched condition | p. 6 (4.2. Experimental Result) |
| Strong single-view reconstruction baselines are improved by iFusion consistently. | comparison identity and matched condition | p. 7 (4.2. Experimental Result) |
| Qualitative comparison of surface reconstruction. | comparison identity and matched condition | p. 7 (4.2. Experimental Result) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We observe that iFusion effectively leverages the additional images without camera poses and generates more faithful images. | component/input/data sensitivity | p. 6 (4.2. Experimental Result) |
| To conclude, when faithful reconstruction is desired, iFusion is extremely beneficial, requiring very few additional view that can be casually captured without knowing the ... | component/input/data sensitivity | p. 6 (4.2. Experimental Result) |
| It is clear that iFusion significantly enhances existing reconstruction methods including Zero123-SDS [31], DreamGaussian [64], and Magic123 [48], by adding an additional view without ... | component/input/data sensitivity | p. 7 (4.2. Experimental Result) |
| Ablation of t annealing for pose estimation on GSO [9]. n poses t annealing Recall ↑ 5◦ 10◦ 20◦ (a) 4 - 48.61 56.67 ... | component/input/data sensitivity | p. 8 (4.3. Ablation Study) |
| Ablation of the number of initial poses for pose estimation on GSO [9]. n poses Recall ↑ Time (s) ↓ 5◦ 10◦ 20◦ (a) ... | component/input/data sensitivity | p. 8 (4.3. Ablation Study) |
| Figure 1. Demonstration on real-world 3D reconstruction. With only two casually taken photos without camera poses, iFusion can reconstruct plausible 3D assets. The top ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we introduce iFusion, a novel framework that reconstructs diverse 3D objects with sparse, pose-free views. | Evaluation results on pose estimation. iFusion achieves significant improvements for all metrics under 2 input views. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.1. Experimental Setup), p. 6 (4.2. Experimental Result), p. 8 (4.3. Ablation Study), p. 5 (4.2. Experimental Result), p. 6 (4.2. Experimental Result), p. 7 (4.3. Ablation Study) |
| Primary metric/result | Moreover, iFusion significantly outperforms all methods on all metrics. | numeric claim only at cited anchor | p. 6 (4.2. Experimental Result) |

- Numeric sentences retained from the body:
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** The reported computation time was measured on a single Nvidia 3090 GPU.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** Based on Table 4, we employed n = 4 initial poses for a better trade-off between speed and accuracy for all experiments unless otherwise specified.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Notably, COLMAP [55] cannot serve as a baseline in our evaluation due to the structural limitations of Structure-from-Motion, which requires a large number of ... | p. 5 (4.2. Experimental Result) |
| body limitation/failure cue | We found that by leveraging the diffusion model [31], iFusion excels at handling diverse objects thanks to its strong prior knowledge learned during pre-training, ... | p. 5 (4.2. Experimental Result) |
| body limitation/failure cue | Row (c) highlights the substantial improvement from the stochastic re-sampling of multiview conditions at each timestep, providing more robust outcomes than row (b). | p. 7 (4.3. Ablation Study) |
| body limitation/failure cue | Figure 8. More qualitative results on pose estimation. The predicted poses (thin) and their corresponding ground truth (bold), are plotted in the same color, ... | p. 13 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The reported computation time was measured on a single Nvidia 3090 GPU. | p. 7 (4.3. Ablation Study) |
| Finally, we compute the residuals for backpropagation of the transformation's gradient ∇ˆTr→q. | p. 3 (3.1. Diffusion as a Pose Estimator) |
| For above steps, the LoRA model and MVC are also employed. | p. 5 (3.3. From Sparse Views to 3D Reconstruction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4.2. Experimental Result - extractive PDF cue:** Notably, COLMAP [55] cannot serve as a baseline in our evaluation due to the structural limitations of Structure-from-Motion, which requires a large number of views ...
- **p. 5 / 4.2. Experimental Result - extractive PDF cue:** We found that by leveraging the diffusion model [31], iFusion excels at handling diverse objects thanks to its strong prior knowledge learned during pre-training, whereas ...
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** Row (c) highlights the substantial improvement from the stochastic re-sampling of multiview conditions at each timestep, providing more robust outcomes than row (b).
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 8. More qualitative results on pose estimation. The predicted poses (thin) and their corresponding ground truth (bold), are plotted in the same color, while ...

- **PDF anchors reviewed:** datasets p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Experimental Result), p. 6 (4.2. Experimental Result), p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), metrics p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 8 (Figure/Table caption), p. 8 (4.3. Ablation Study), baselines p. 8 (4.3. Ablation Study), p. 5 (4.2. Experimental Result), p. 6 (4.2. Experimental Result), p. 6 (4.2. Experimental Result), p. 7 (4.2. Experimental Result), p. 7 (4.2. Experimental Result), results p. 5 (4.1. Experimental Setup), p. 6 (4.2. Experimental Result), p. 8 (4.3. Ablation Study), p. 5 (4.2. Experimental Result), p. 6 (4.2. Experimental Result), p. 7 (4.3. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
