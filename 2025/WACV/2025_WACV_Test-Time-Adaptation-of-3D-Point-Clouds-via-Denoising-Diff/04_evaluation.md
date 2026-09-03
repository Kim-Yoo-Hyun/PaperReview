# Evaluation - Test-Time Adaptation of 3D Point Clouds via Denoising Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Dastmalchi_Test-Time_Adaptation_of_3D_Point_Clouds_via_Denoising_Diffusion_Models_WACV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Dastmalchi_Test-Time_Adaptation_of_3D_Point_Clouds_via_Denoising_Diffusion_Models_WACV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.3. Results), p. 6 (4.3. Results), p. 7 (4.3. Results), p. 7 (4.3. Results), p. 5 (Figure/Table caption), p. 8 (4.4. Ablation Study)): In addition, our 3DD-TTA outperforms other TTA frameworks on density-based corruptions such as cut-out and density increase.

## Evaluation Body Digest

- **p. 6 / 4.1. Datasets and Corruption Methods - extractive body cue:** ScanObjectNN-c: ScanObjectNN [44], a real-world point cloud dataset with 15 categories, is corrupted using the same open-source code as ModelNet40-c [40], introducing 15 corruptions into ...
- **p. 7 / 4.3. Results - extractive body cue:** We also conducted experiments on the corrupted version of the real-world ScanObjectNN dataset [44], which inherently suffers from noise, background issues, and occlusion.
- **p. 6 / 4.1. Datasets and Corruption Methods - extractive body cue:** We refer to this dataset as ScanObjectNN-c.
- **p. 7 / 4.3. Results - extractive body cue:** To validate this, we conduct experiments on the ModelNet40-c and ScanObjectNN-c datasets.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Classification accuracies on ScanObjectNN-c dataset.
- **p. 6 / 4.3. Results - extractive body cue:** Notably, 3DD-TTA dramatically boosts the source classifier's performance on background noise, raising accuracy from 15.0% to 77.6%.
- **p. 7 / 4.3. Results - extractive body cue:** The highest accuracy is in bold, while the second-best is underlined.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Based on this, we selected 100 DDIM steps to balance adaptation time and accuracy.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Datasets and Corruption Methods (p. 6); 4.3. Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | In addition, our 3DD-TTA outperforms other TTA frameworks on density-based corruptions such as cut-out and density increase. | p. 6 (4.3. Results) |
| 4.3. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | The table clearly shows that the 3DD-TTA method outperforms the other methods by a significant margin in most corruption types. | p. 6 (4.3. Results) |
| 4.3. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3DD-TTA boosts Point-MAE (source) in most corruption types, showing improved robustness across different corruptions. | p. 7 (4.3. Results) |
| 4.3. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Similarly, the model outperforms other methods in addressing densityrelated corruptions but is less effective for transformationbased corruptions, ranking second or third for these deformations. | p. 7 (4.3. Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3. Given a corrupted test point cloud ˜x, we adapt it to the source domain to improve classifier pc. Using the LION model ... | p. 5 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Datasets and Corruption Methods - extractive body cue:** ScanObjectNN-c: ScanObjectNN [44], a real-world point cloud dataset with 15 categories, is corrupted using the same open-source code as ModelNet40-c [40], introducing 15 corruptions into ...
- **p. 7 / 4.3. Results - extractive body cue:** We also conducted experiments on the corrupted version of the real-world ScanObjectNN dataset [44], which inherently suffers from noise, background issues, and occlusion.
- **p. 6 / 4.1. Datasets and Corruption Methods - extractive body cue:** We refer to this dataset as ScanObjectNN-c.
- **p. 7 / 4.3. Results - extractive body cue:** To validate this, we conduct experiments on the ModelNet40-c and ScanObjectNN-c datasets.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Classification accuracies on ScanObjectNN-c dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Reconstruction of corrupted point clouds using the pro- posed 3DD-TTA method. between training and testing samples is minimal. However, real-world scenarios often feature ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. In the TTA setting, the source model encounters corrupted 3D point clouds with an unknown distribution shift, requiring adaptation without prior knowledge of ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Given a corrupted test point cloud ˜x, we adapt it to the source domain to improve classifier pc. Using the LION model [45], ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Classification accuracies on ShapeNet-c. Point-MAE [24], as trained in [22], serves as the source classifier denoted as src. The highest accuracy is in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative assessment of the proposed test-time adaptation across various corruptions.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Classification accuracies on ModelNet40-c. Point-MAE [24], as trained in [22], serves as the source classifier denoted as src. The highest accuracy is in ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Classification accuracies on ScanObjectNN-c dataset. Corruptions: uni gauss back impu ups rbf rbf-i den-d den-i shear rot cut
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. (left) Accuracy of the source classifier after adaptation using different numbers of denoising steps. (right) Performance of the model across different numbers of ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | ScanObjectNN-c: ScanObjectNN [44], a real-world point cloud dataset with 15 categories, is corrupted using the same open-source code as ModelNet40-c [40], introducing 15 corruptions ... | embodiment, simulator version and control stack | p. 6 (4.1. Datasets and Corruption Methods), p. 7 (4.3. Results) |
| Task/environment | We also conducted experiments on the corrupted version of the real-world ScanObjectNN dataset [44], which inherently suffers from noise, background issues, and occlusion. | reset, timeout, object/scene variation | p. 7 (4.3. Results), p. 6 (4.1. Datasets and Corruption Methods) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 5 (3.3. Denoising Diffusion-based Adaption Method), p. 4 (3.1. Preliminaries) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 4 (3.1. Preliminaries), p. 5 (3.3. Denoising Diffusion-based Adaption Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Notably, 3DD-TTA dramatically boosts the source classifier's performance on background noise, raising accuracy from 15.0% to 77.6%. | definition/direction/unit from same section | p. 6 (4.3. Results) |
| The highest accuracy is in bold, while the second-best is underlined. | definition/direction/unit from same section | p. 7 (4.3. Results) |
| Based on this, we selected 100 DDIM steps to balance adaptation time and accuracy. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| (left) Accuracy of the source classifier after adaptation using different numbers of denoising steps. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| The model successfully restores the point clouds, thereby improving the performance of the source classifier. | definition/direction/unit from same section | p. 6 (4.3. Results) |
| 3DD-TTA boosts Point-MAE (source) in most corruption types, showing improved robustness across different corruptions. | definition/direction/unit from same section | p. 7 (4.3. Results) |
| Figure 1. Reconstruction of corrupted point clouds using the pro- posed 3DD-TTA method. between training and testing samples is minimal. However, real-world scenarios often ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. In the TTA setting, the source model encounters corrupted 3D point clouds with an unknown distribution shift, requiring adaptation without prior knowledge ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In addition, our 3DD-TTA outperforms other TTA frameworks on density-based corruptions such as cut-out and density increase. | comparison identity and matched condition | p. 6 (4.3. Results) |
| The table clearly shows that the 3DD-TTA method outperforms the other methods by a significant margin in most corruption types. | comparison identity and matched condition | p. 6 (4.3. Results) |
| Similarly, the model outperforms other methods in addressing densityrelated corruptions but is less effective for transformationbased corruptions, ranking second or third for these deformations. | comparison identity and matched condition | p. 7 (4.3. Results) |
| Number of Denoising Steps for Reconstruction: While the denoising diffusion network in the original LION [45] model was trained with 1000 time steps, we ... | comparison identity and matched condition | p. 7 (4.4. Ablation Study) |
| Figure 2. In the TTA setting, the source model encounters corrupted 3D point clouds with an unknown distribution shift, requiring adaptation without prior knowledge ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This limitation is due to the trainingfree nature of the model, making it challenging to reverse transformations to their original shape without additional training. | component/input/data sensitivity | p. 6 (4.3. Results) |
| Number of Denoising Steps for Reconstruction: While the denoising diffusion network in the original LION [45] model was trained with 1000 time steps, we ... | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| The baselines include: (1) SHOT [17], which minimizes output entropy; (2) T3A [14], which learns class-specific prototypes to replace the pre-trained classifier; (3) TENT ... | component/input/data sensitivity | p. 6 (4.2. Baselines) |
| Figure 2. In the TTA setting, the source model encounters corrupted 3D point clouds with an unknown distribution shift, requiring adaptation without prior knowledge ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we introduce a novel, training-free test-time adaptation method called 3D Denoising Diffusion TestTime Adaptation (3DD-TTA). | In addition, our 3DD-TTA outperforms other TTA frameworks on density-based corruptions such as cut-out and density increase. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.3. Results), p. 6 (4.3. Results), p. 7 (4.3. Results), p. 7 (4.3. Results), p. 5 (Figure/Table caption), p. 8 (4.4. Ablation Study) |
| Primary metric/result | The table clearly shows that the 3DD-TTA method outperforms the other methods by a significant margin in most corruption types. | numeric claim only at cited anchor | p. 6 (4.3. Results) |

- Numeric sentences retained from the body:
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Our analysis in Figure 5 (left) shows five steps suffice for most corruption types, but extreme outliers, like background noise, require up to 35 steps.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** The adaptation time grows linearly with the number of denoising steps, ranging from 12 ms for 1 step to 290 ms for 40 steps.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** As only 5 denoising steps (taking 40 ms) are sufficient for most corruptions, the proposed method is efficient, making it suitable for time-sensitive applications.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Adaptation time (ms) for different numbers of denoising steps in the 3DD-TTA method. # Denoising Steps: 1 5 10 20 30 40 Time Duration (ms) ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** However, severe outliers, such as background noise, may require up to 35 steps, increasing processing time for these cases.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1. Reconstruction of corrupted point clouds using the pro- posed 3DD-TTA method. between training and testing samples is minimal. However, real-world scenarios often ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | However, the model faces limitations in addressing the transformation-based deformations like shear and rotation. | p. 6 (4.3. Results) |
| body limitation/failure cue | This limitation is due to the trainingfree nature of the model, making it challenging to reverse transformations to their original shape without additional training. | p. 6 (4.3. Results) |
| body limitation/failure cue | Limitation: Our model performs well with just five denoising steps for most types of corruption, making it efficient and suitable for time-sensitive applications. | p. 8 (4.4. Ablation Study) |
| body limitation/failure cue | Incorporating the proposed updating strategy based on the gradient of the Selective Chamfer Distance (SCD) ensures the generation of highfidelity, noise-free test samples. | p. 8 (5. Conclusion) |
| body limitation/failure cue | We also conducted experiments on the corrupted version of the real-world ScanObjectNN dataset [44], which inherently suffers from noise, background issues, and occlusion. | p. 7 (4.3. Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Shape Latent Encoder 𝑞𝑧 Latent Point Encoder 𝑞ℎ Decoder 𝑝𝑑 Denoising Diffusion Network tw + 𝐳0 𝐡tw 𝐡𝟎 𝐫 𝛆 ෤𝐱 𝐱 𝐡0 ∇𝐡tlcd ... | p. 5 (3.3. Denoising Diffusion-based Adaption Method) |
| 1: Input: Corrupted point cloud ˜x, shape encoder qz(.), latent point encoder qh(.), decoder pd(.), diffusion prior ϵh(.), and source classifier pc(.) 2: z0 ... | p. 5 (3.3. Denoising Diffusion-based Adaption Method) |
| All experiments were conducted on a single NVIDIA A6000 GPU. | p. 6 (4. Experiments) |
| We employed the deterministic DDIM [38] process over 100 total time steps to accelerate the denoising process. | p. 6 (4. Experiments) |
| Number of Denoising Steps: Table 4 shows the time duration required for test-time adaptation using our method as the number of denoising steps 1572 | p. 7 (4.4. Ablation Study) |
| In our first experiment, we fixed DDIM steps at 100 and investigated the optimal number of denoising steps for reconstructing corrupted point clouds. | p. 7 (4.4. Ablation Study) |
| Based on this, we selected 100 DDIM steps to balance adaptation time and accuracy. | p. 8 (4.4. Ablation Study) |
| (right) Performance of the model across different numbers of total DDIM steps. increases. | p. 8 (4.4. Ablation Study) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Reconstruction of corrupted point clouds using the pro- posed 3DD-TTA method. between training and testing samples is minimal. However, real-world scenarios often feature ...
- **p. 6 / 4.3. Results - extractive body cue:** However, the model faces limitations in addressing the transformation-based deformations like shear and rotation.
- **p. 6 / 4.3. Results - extractive body cue:** This limitation is due to the trainingfree nature of the model, making it challenging to reverse transformations to their original shape without additional training.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Limitation: Our model performs well with just five denoising steps for most types of corruption, making it efficient and suitable for time-sensitive applications.
- **p. 8 / 5. Conclusion - extractive body cue:** Incorporating the proposed updating strategy based on the gradient of the Selective Chamfer Distance (SCD) ensures the generation of highfidelity, noise-free test samples.
- **p. 7 / 4.3. Results - extractive body cue:** We also conducted experiments on the corrupted version of the real-world ScanObjectNN dataset [44], which inherently suffers from noise, background issues, and occlusion.

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Datasets and Corruption Methods), p. 7 (4.3. Results), p. 6 (4.1. Datasets and Corruption Methods), p. 7 (4.3. Results), p. 8 (4.4. Ablation Study), metrics p. 6 (4.3. Results), p. 7 (4.3. Results), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 6 (4.3. Results), p. 7 (4.3. Results), baselines p. 6 (4.3. Results), p. 6 (4.3. Results), p. 7 (4.3. Results), p. 7 (4.4. Ablation Study), p. 2 (Figure/Table caption), results p. 6 (4.3. Results), p. 6 (4.3. Results), p. 7 (4.3. Results), p. 7 (4.3. Results), p. 5 (Figure/Table caption), p. 8 (4.4. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
