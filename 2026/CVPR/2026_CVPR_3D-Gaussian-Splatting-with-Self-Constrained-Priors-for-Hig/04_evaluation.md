# Evaluation - 3D Gaussian Splatting with Self-Constrained Priors for High Fidelity Surface Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Noda_3D_Gaussian_Splatting_with_Self-Constrained_Priors_for_High_Fidelity_Surface_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Noda_3D_Gaussian_Splatting_with_Self-Constrained_Priors_for_High_Fidelity_Surface_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.2. Results and Evaluation), p. 6 (4.2. Results and Evaluation), p. 6 (4.2. Results and Evaluation), p. 5 (4.2. Results and Evaluation), p. 7 (4.2. Results and Evaluation), p. 2 (Figure/Table caption)): 2, our method achieves the best results across scenes.

## Evaluation Body Digest

- **p. 5 / 4.1. Experiment Setup - extractive PDF cue:** We evaluate our method on four datasets with synthetic and real scanned scenes, including: NeRF-Synthetic [41], DTU [24], Tanks and Temples (TNT) [28], and Mip-NeRF ...
- **p. 6 / 4.2. Results and Evaluation - extractive PDF cue:** We evaluate the robustness of our method on large-scale scenes in Tanks and Temples (TNT) dataset.
- **p. 5 / 4.2. Results and Evaluation - extractive PDF cue:** 2, our method achieves the best results across scenes.
- **p. 6 / 4.2. Results and Evaluation - extractive PDF cue:** Visual comparison of reconstruction on DTU dataset.
- **p. 7 / 4.2. Results and Evaluation - extractive PDF cue:** We further evaluate our method on the Mip-NeRF 360 dataset to validate the performance in novel view synthesis.
- **p. 7 / 4.2. Results and Evaluation - extractive PDF cue:** 9, GOF[60] and GS-Pull [64] achieve high completeness on surfaces but struggle to recover local details in indoor scenes.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. Overview of our method. Given 3D Gaussians g, we employ a distance field specified by a fused TSDF grid as our prior f ...
- **p. 6 / 4.2. Results and Evaluation - extractive PDF cue:** The error map indicates the distance to the ground truth surface.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experiment Setup (p. 5); 4.2. Results and Evaluation (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Results and Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2, our method achieves the best results across scenes. | p. 5 (4.2. Results and Evaluation) |
| 4.2. Results and Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3 shows that our method achieves the best reconstruction performance among all baselines. | p. 6 (4.2. Results and Evaluation) |
| 4.2. Results and Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | GOF [60] combines Gaussians with opacity fields to improve performance, but constrained by complex opacity modeling. | p. 6 (4.2. Results and Evaluation) |
| 4.2. Results and Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, our method outperforms all baselines in both CD and PSNR metrics. | p. 5 (4.2. Results and Evaluation) |
| 4.2. Results and Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | 9, GOF[60] and GS-Pull [64] achieve high completeness on surfaces but struggle to recover local details in indoor scenes. | p. 7 (4.2. Results and Evaluation) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experiment Setup - extractive PDF cue:** We evaluate our method on four datasets with synthetic and real scanned scenes, including: NeRF-Synthetic [41], DTU [24], Tanks and Temples (TNT) [28], and Mip-NeRF ...
- **p. 6 / 4.2. Results and Evaluation - extractive PDF cue:** We evaluate the robustness of our method on large-scale scenes in Tanks and Temples (TNT) dataset.
- **p. 5 / 4.2. Results and Evaluation - extractive PDF cue:** 2, our method achieves the best results across scenes.
- **p. 6 / 4.2. Results and Evaluation - extractive PDF cue:** Visual comparison of reconstruction on DTU dataset.
- **p. 7 / 4.2. Results and Evaluation - extractive PDF cue:** We further evaluate our method on the Mip-NeRF 360 dataset to validate the performance in novel view synthesis.
- **p. 7 / 4.2. Results and Evaluation - extractive PDF cue:** 9, GOF[60] and GS-Pull [64] achieve high completeness on surfaces but struggle to recover local details in indoor scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. Overview of our method. Given 3D Gaussians g, we employ a distance field specified by a fused TSDF grid as our prior f ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Illustration of band- width and the range of opacity control. camera coordinate sys- tem specified by
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Visualization of periodical update on our prior.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 4. Visualization of Gaussian centers with each constraint. The error map indicates the distance to the ground truth surface. the depth fusion operation F, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. Visual comparison of reconstruction on NeRF-Synthetic dataset.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparisons in terms of CDL1 (×100) and PSNR on the NeRF-Synthetic dataset. Class
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 6. Error map comparison of rendering on NeRF-Synthetic. our method extracts stable implicit priors from depth maps for more stable geometry inference. The comparisons ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative comparisons in terms of CD on the DTU dataset. Class Methods 24 37 40 55 63

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our method on four datasets with synthetic and real scanned scenes, including: NeRF-Synthetic [41], DTU [24], Tanks and Temples (TNT) [28], and ... | embodiment, simulator version and control stack | p. 5 (4.1. Experiment Setup), p. 6 (4.2. Results and Evaluation) |
| Task/environment | We evaluate the robustness of our method on large-scale scenes in Tanks and Temples (TNT) dataset. | reset, timeout, object/scene variation | p. 6 (4.2. Results and Evaluation), p. 5 (4.2. Results and Evaluation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3. Method), p. 4 (3.3. Loss Functions) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. Learning Self-Constrained Priors), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 1. Overview of our method. Given 3D Gaussians g, we employ a distance field specified by a fused TSDF grid as our prior ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| The error map indicates the distance to the ground truth surface. | definition/direction/unit from same section | p. 6 (4.2. Results and Evaluation) |
| 6 also demonstrate that our method produces smaller errors in challenging regions. | definition/direction/unit from same section | p. 5 (4.2. Results and Evaluation) |
| For TNT, we report the F1-score to measure the alignment between the predicted surface and the ground-truth point cloud. | definition/direction/unit from same section | p. 5 (4.1. Experiment Setup) |
| Quantitative comparisons in terms of F1-Score on the TNT dataset. | definition/direction/unit from same section | p. 6 (4.2. Results and Evaluation) |
| Visual comparison of reconstruction on Mip-NerF 360 dataset, the color indicates the normal direction. rate surface alignment, while GS-Pull loses local details and exhibits ... | definition/direction/unit from same section | p. 7 (4.2. Results and Evaluation) |
| We further evaluate our method on the Mip-NeRF 360 dataset to validate the performance in novel view synthesis. | definition/direction/unit from same section | p. 7 (4.2. Results and Evaluation) |
| Figure 11. Effect of periodical update on our prior. ticeable increase in CD. Visual results in Fig. 10 further demonstrate that learning Gaussian representations ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1, our method outperforms all baselines in both CD and PSNR metrics. | comparison identity and matched condition | p. 5 (4.2. Results and Evaluation) |
| We also validate our method on the real-scanned dataset compared with state-of-the-art approaches. | comparison identity and matched condition | p. 5 (4.2. Results and Evaluation) |
| 3 shows that our method achieves the best reconstruction performance among all baselines. | comparison identity and matched condition | p. 6 (4.2. Results and Evaluation) |
| Figure 1. Overview of our method. Given 3D Gaussians g, we employ a distance field specified by a fused TSDF grid as our prior ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Figure 11. Effect of periodical update on our prior. ticeable increase in CD. Visual results in Fig. 10 further demonstrate that learning Gaussian representations ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| We further provide visual comparisons in Fig.8. | comparison identity and matched condition | p. 6 (4.2. Results and Evaluation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 12. Effect of Gaussian Removal and Projection. ity arrangement term LSCP , we remove it (denoted as w/o LSCP ) and optimize the ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 10. Effect of the self-constrained prior. | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are listed below, • We propose a self-constrained prior to impose constraints on the learning of 3D Gaussians in a geometry-aware manner. | 2, our method achieves the best results across scenes. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.2. Results and Evaluation), p. 6 (4.2. Results and Evaluation), p. 6 (4.2. Results and Evaluation), p. 5 (4.2. Results and Evaluation), p. 7 (4.2. Results and Evaluation), p. 2 (Figure/Table caption) |
| Primary metric/result | 3 shows that our method achieves the best reconstruction performance among all baselines. | numeric claim only at cited anchor | p. 6 (4.2. Results and Evaluation) |

- Numeric sentences retained from the body:
- **p. 4 / 3.2. Constraints with a Self-Constrained Prior - extractive PDF cue:** For each Gaussian gj, we first interpolate the signed distance sj at the center µj, and calculate its gradient ∇f t(µj) using finite difference in ...
- **p. 4 / 3.3. Loss Functions - extractive PDF cue:** Based on that, to learn a consistent surface from multiview depth maps, we also leverage LDepth to make the perray depth distribution thinner and more ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Compared with implicit methods, our method does not need to learn SDF or priors, which balances both accuracy and efficiency. | p. 5 (4.2. Results and Evaluation) |
| body limitation/failure cue | We evaluate the robustness of our method on large-scale scenes in Tanks and Temples (TNT) dataset. | p. 6 (4.2. Results and Evaluation) |
| body limitation/failure cue | Visual comparison of reconstruction on Mip-NerF 360 dataset, the color indicates the normal direction. rate surface alignment, while GS-Pull loses local details and exhibits ... | p. 7 (4.2. Results and Evaluation) |
| body limitation/failure cue | Figure 12. Effect of Gaussian Removal and Projection. ity arrangement term LSCP , we remove it (denoted as w/o LSCP ) and optimize the ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| no implementation/reproducibility sentence selected | verify appendix and code/project |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4.2. Results and Evaluation - extractive PDF cue:** Compared with implicit methods, our method does not need to learn SDF or priors, which balances both accuracy and efficiency.
- **p. 6 / 4.2. Results and Evaluation - extractive PDF cue:** We evaluate the robustness of our method on large-scale scenes in Tanks and Temples (TNT) dataset.
- **p. 7 / 4.2. Results and Evaluation - extractive PDF cue:** Visual comparison of reconstruction on Mip-NerF 360 dataset, the color indicates the normal direction. rate surface alignment, while GS-Pull loses local details and exhibits normal ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 12. Effect of Gaussian Removal and Projection. ity arrangement term LSCP , we remove it (denoted as w/o LSCP ) and optimize the Gaussian ...

- **PDF anchors reviewed:** datasets p. 5 (4.1. Experiment Setup), p. 6 (4.2. Results and Evaluation), p. 5 (4.2. Results and Evaluation), p. 6 (4.2. Results and Evaluation), p. 7 (4.2. Results and Evaluation), p. 7 (4.2. Results and Evaluation), metrics p. 2 (Figure/Table caption), p. 6 (4.2. Results and Evaluation), p. 5 (4.2. Results and Evaluation), p. 5 (4.1. Experiment Setup), p. 6 (4.2. Results and Evaluation), p. 7 (4.2. Results and Evaluation), baselines p. 5 (4.2. Results and Evaluation), p. 5 (4.2. Results and Evaluation), p. 6 (4.2. Results and Evaluation), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4.2. Results and Evaluation), results p. 5 (4.2. Results and Evaluation), p. 6 (4.2. Results and Evaluation), p. 6 (4.2. Results and Evaluation), p. 5 (4.2. Results and Evaluation), p. 7 (4.2. Results and Evaluation), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
