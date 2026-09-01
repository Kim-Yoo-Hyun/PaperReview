# Evaluation - CityGaussianV2: Efficient and Geometrically Accurate Reconstruction for Large-Scale Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=a3ptUbuzbW; PDF retrieval source: https://openreview.net/pdf/602b5d6d17415fb9e6df86e7df8a1fe5990406d7.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS)): For MatrixCity-Aerial, our method achieves the best surface quality among all algorithms, with the F1 score being twice that of 2DGS and outperforming CityGaussian by a significant margin.

## Evaluation Body Digest

- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Therefore, we utilize the realistic dataset GauU-Scene (Xiong et al., 2024) and the synthetic dataset MatrixCity (Li et al., 2023a).
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** The experiments are conducted on Residence scene of GauU-Scene dataset ((Xiong et al., 2024)).
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** We require datasets with accurate ground-truth point clouds.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** As shown, NeRF-based methods are more prone to failure due to the NaN outputs of the MLP or poor convergence under sparse supervision in large-scale ...
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Results on other scenes are included in Tab.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** On the challenging MatrixCity dataset, we evaluate performance from both aerial and street views.
- **p. 17 / C MORE IMPLEMENTATION DETAILS - extractive PDF cue:** The Residence scene of GauU-Scene is divided into 4×2 blocks, while Russian Building and Modern Building scenes are divided into 3×3 blocks.
- **p. 17 / C MORE IMPLEMENTATION DETAILS - extractive PDF cue:** For primitives and data partitioning, as well as parallel tuning, we follow the default parameter setting of CityGaussian (Liu et al., 2024) on both aerial ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 7); B ADDITIONAL QUANTITATIVE RESULTS (p. 15); C MORE IMPLEMENTATION DETAILS (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | For MatrixCity-Aerial, our method achieves the best surface quality among all algorithms, with the F1 score being twice that of 2DGS and outperforming CityGaussian ... | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | For GauU-Scene, our model significantly outperforms existing geometry-specialized methods in rendering quality. | p. 8 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1 shows that even without parallel tuning, our proposed optimization strategy enables our model to achieve significantly better 8 | p. 8 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared to CityGS, though 0.24 PSNR is sacrificed, our method gains around 11% F1-score improvement. | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | With parallel tuning, both rendering and geometry quality show substantial improvements, validating the success of scaling up. | p. 10 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Therefore, we utilize the realistic dataset GauU-Scene (Xiong et al., 2024) and the synthetic dataset MatrixCity (Li et al., 2023a).
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** The experiments are conducted on Residence scene of GauU-Scene dataset ((Xiong et al., 2024)).
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** We require datasets with accurate ground-truth point clouds.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** As shown, NeRF-based methods are more prone to failure due to the NaN outputs of the MLP or poor convergence under sparse supervision in large-scale ...
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Results on other scenes are included in Tab.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** On the challenging MatrixCity dataset, we evaluate performance from both aerial and street views.
- **p. 17 / C MORE IMPLEMENTATION DETAILS - extractive PDF cue:** The Residence scene of GauU-Scene is divided into 4×2 blocks, while Russian Building and Modern Building scenes are divided into 3×3 blocks.
- **p. 17 / C MORE IMPLEMENTATION DETAILS - extractive PDF cue:** For primitives and data partitioning, as well as parallel tuning, we follow the default parameter setting of CityGaussian (Liu et al., 2024) on both aerial ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Illustration of the superiority of CityGaussianV2. (a) Our method reconstructs large-scale complex scenes with accurate geometry from multi-view RGB images, restoring intricate structures ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Illustration of our optimization mechanism. We densify Gaussians exclusively according to the gradient of SSIM loss. This helps remove large and blurry Gaussians ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Illustration of the motivation and effectiveness of our Elongation Filter. We take the tuning of one block of Rubble (Turki et al., 2022) ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Illustration of pipeline modification. The pipeline of CityGS (Liu et al., 2024) (dashed boxes and arrows) is compared with ours. We successfully removed ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Illustration of the evaluation process. ever, there is still no universally accepted protocol for assessing geometric accuracy in large-scale scene reconstruction. Recently, GauU-Scene ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: Qualitative comparison of surface reconstruction quality. Here "Russian" and "Modern" denote the Russian Building and Modern Building scene of GauU-Scene, respectively. And "Aerial" ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 7: Qualitative comparison of rendering quality. Here "Russian" and "Modern" denote the Russian Building and Modern Building scene of GauU-Scene, respectively. "Aerial" denotes the ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison with SOTA reconstruction methods. "NaN" means no results due to NaN error. "FAIL" means the method fails to extract meaningful mesh due ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Therefore, we utilize the realistic dataset GauU-Scene (Xiong et al., 2024) and the synthetic dataset MatrixCity (Li et al., 2023a). | embodiment, simulator version and control stack | p. 7 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Task/environment | The experiments are conducted on Residence scene of GauU-Scene dataset ((Xiong et al., 2024)). | reset, timeout, object/scene variation | p. 10 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 7 (3 METHOD), p. 17 (C MORE IMPLEMENTATION DETAILS) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3 METHOD), p. 5 (3 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 1: Illustration of the superiority of CityGaussianV2. (a) Our method reconstructs large-scale complex scenes with accurate geometry from multi-view RGB images, restoring intricate ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| However, replacing the block partition with the one generated from 7,000 iterations of 2DGS results in a considerable drop in both the PSNR and ... | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| 2 demonstrates that our Decomposed Densification Gradient (DGD) strategy significantly accelerates convergence, improving 1.0 PSNR, 0.04 SSIM, and almost 0.02 F1 score. | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| Geometrically, our model outperforms 2DGS by 0.01 F1 score. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| Compared to CityGS, though 0.24 PSNR is sacrificed, our method gains around 11% F1-score improvement. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| For MatrixCity-Aerial, our method achieves the best surface quality among all algorithms, with the F1 score being twice that of 2DGS and outperforming CityGaussian ... | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| Figure 3: Illustration of the motivation and effectiveness of our Elongation Filter. We take the tuning of one block of Rubble (Turki et al., ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 5: Illustration of the evaluation process. ever, there is still no universally accepted protocol for assessing geometric accuracy in large-scale scene reconstruction. Recently, ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 5.2 COMPARISON WITH SOTA METHODS In this section, we compare CityGaussianV2 with state-of-the-art (SOTA) methods both quantitatively and qualitatively. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| Geometrically, our model outperforms 2DGS by 0.01 F1 score. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| Compared to CityGS, though 0.24 PSNR is sacrificed, our method gains around 11% F1-score improvement. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| For MatrixCity-Aerial, our method achieves the best surface quality among all algorithms, with the F1 score being twice that of 2DGS and outperforming CityGaussian ... | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| Here we take 2DGS ((Huang et al., 2024)) as our baseline. | comparison identity and matched condition | p. 10 (5 EXPERIMENTS) |
| Table 4: Detailed comparison among SOTA among parallel training methods. 2DGS* here means applying CityGS's training strategy to 2DGS without our proposed optimization mechanism. ... | comparison identity and matched condition | p. 16 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 10: Qualitative ablation of 7K iteration results among different methods. This section provides additional qualitative comparisons. As illustrated in Fig. 8, the mesh ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Published as a conference paper at ICLR 2025 Table 2: Ablation on model components. | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |
| Table 2: Ablation on model components. The experiments are conducted on Residence scene of GauU-Scene dataset ((Xiong et al., 2024)). Here we take 2DGS ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| 1 shows that even without parallel tuning, our proposed optimization strategy enables our model to achieve significantly better 8 | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| Figure 2: Illustration of our optimization mechanism. We densify Gaussians exclusively according to the gradient of SSIM loss. This helps remove large and blurry ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Figure 4: Illustration of pipeline modification. The pipeline of CityGS (Liu et al., 2024) (dashed boxes and arrows) is compared with ours. We successfully ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are four-fold: • A novel optimization strategy for 2DGS, that accelerates its convergence under large-scale scenes and enables it to ... | For MatrixCity-Aerial, our method achieves the best surface quality among all algorithms, with the F1 score being twice that of 2DGS and outperforming CityGaussian ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Primary metric/result | For GauU-Scene, our model significantly outperforms existing geometry-specialized methods in rendering quality. | numeric claim only at cited anchor | p. 8 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Besides, these methods generally take over 10 hours for training.
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** Additionally, by using the result from 7,000 iterations as a pre-train, the total training time decreases from 3 hours to 2 hours, with the model ...
- **p. 17 / C MORE IMPLEMENTATION DETAILS - extractive PDF cue:** The Residence scene of GauU-Scene is divided into 4×2 blocks, while Russian Building and Modern Building scenes are divided into 3×3 blocks.
- **p. 17 / C MORE IMPLEMENTATION DETAILS - extractive PDF cue:** The Residence scene of GauU-Scene is divided into 4×2 blocks, while Russian Building and Modern Building scenes are divided into 3×3 blocks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | As shown, NeRF-based methods are more prone to failure due to the NaN outputs of the MLP or poor convergence under sparse supervision in ... | p. 8 (5 EXPERIMENTS) |
| body limitation/failure cue | Published as a conference paper at ICLR 2025 Ours Ground-truth CityGS SuGaR GOF 2DGS Modern Russian Aerial Convergence Failure Residence Figure 6: Qualitative comparison ... | p. 8 (5 EXPERIMENTS) |
| body limitation/failure cue | Furthermore, GOF fails to complete training or extract meaningful meshes. | p. 9 (5 EXPERIMENTS) |
| body limitation/failure cue | Table 1: Comparison with SOTA reconstruction methods. "NaN" means no results due to NaN error. "FAIL" means the method fails to extract meaningful mesh ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | LightGaussian's (Fan et al., 2023) pruning strategy, however, falls short in preserving rendering quality. | p. 10 (5 EXPERIMENTS) |
| body limitation/failure cue | Table 5: Detailed geometry metrics on GauU-Scene datasets ((Xiong et al., 2024)). * means that the method fails to finish 60,000 iterations training and ... | p. 16 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We adhere to the default settings in CityGaussian (Liu et al., 2024) for the learning rate and densification schedule. | p. 8 (5 EXPERIMENTS) |
| The tiny version (ours-t) can even halve the training time. | p. 9 (5 EXPERIMENTS) |
| 2, the small version of CityGaussianV2 (ours-s) reduces training time by 25% and memory usage by over 50%, while delivering superior geometric performance and ... | p. 9 (5 EXPERIMENTS) |
| Additionally, by using the result from 7,000 iterations as a pre-train, the total training time decreases from 3 hours to 2 hours, with the ... | p. 10 (5 EXPERIMENTS) |
| The upper part ablates on pertaining, while the lower part ablates on fine-tuning. #GS, T, Size, Mem. are the number of Gaussians, total training ... | p. 10 (5 EXPERIMENTS) |
| When fine-tuning on GauU-Scene, the learning rate of position is reduced by 60%, while that of scaling is empirically reduced by 20%, as suggested ... | p. 17 (C MORE IMPLEMENTATION DETAILS) |
| To be specific, it applies lower learning rates during tuning compared to pertaining, and the street view is trained with a significantly lower learning ... | p. 17 (C MORE IMPLEMENTATION DETAILS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** As shown, NeRF-based methods are more prone to failure due to the NaN outputs of the MLP or poor convergence under sparse supervision in large-scale ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 Ours Ground-truth CityGS SuGaR GOF 2DGS Modern Russian Aerial Convergence Failure Residence Figure 6: Qualitative comparison of ...
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Furthermore, GOF fails to complete training or extract meaningful meshes.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison with SOTA reconstruction methods. "NaN" means no results due to NaN error. "FAIL" means the method fails to extract meaningful mesh due ...
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** LightGaussian's (Fan et al., 2023) pruning strategy, however, falls short in preserving rendering quality.
- **p. 16 / Figure/Table caption - extractive PDF cue:** Table 5: Detailed geometry metrics on GauU-Scene datasets ((Xiong et al., 2024)). * means that the method fails to finish 60,000 iterations training and therefore ...

- **PDF anchors reviewed:** datasets p. 7 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), metrics p. 1 (Figure/Table caption), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), baselines p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 16 (Figure/Table caption), results p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
