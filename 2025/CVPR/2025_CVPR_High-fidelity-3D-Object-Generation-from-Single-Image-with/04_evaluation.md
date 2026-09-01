# Evaluation - High-fidelity 3D Object Generation from Single Image with RGBN-Volume Gaussian Reconstruction Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.2. Novel View Synthesis), p. 8 (Figure/Table caption), p. 7 (4.4. Runtime Efficiency), p. 6 (4.2. Novel View Synthesis), p. 6 (4.2. Novel View Synthesis), p. 7 (4.5. Ablation study)): Our method significantly outperforms all recent methods by a large margin 21562

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** For evaluation, We adopt the most widely used Google Scanned Objects (GSO) dataset [13].
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** Following [27, 70], our model is trained on the Objaverse-LVIS dataset [11] that contains 46K diverse 3D objects in 1156 categories.
- **p. 6 / 4.2. Novel View Synthesis - extractive PDF cue:** Qualitative comparisons of novel view synthesis between GS-RGBN and other methods on the GSO dataset.
- **p. 6 / 4.2. Novel View Synthesis - extractive PDF cue:** Quantitative comparison on the GSO dataset, in terms of PSNR, SSIM, LPIPS, Chamfer Distance (CD) ×10-3 and runtime efficiency.
- **p. 7 / 4.3. Single View Reconstruction - extractive PDF cue:** Ablation study on the different loss functions and normal fusion strategies on the GSO dataset. planeGaussian [70] can generate shapes that exhibit rough alignment with ...
- **p. 7 / 4.5. Ablation study - extractive PDF cue:** It means that all additional loss functions significantly enhance the overall quality of the reconstructed 3D object.
- **p. 8 / 4.5. Ablation study - extractive PDF cue:** Our full model achieves the best 3D object reconstruction with consistent details.
- **p. 7 / 4.5. Ablation study - extractive PDF cue:** The model performance decreases when the LPIPS, depth, and regularization loss terms are successively removed, as demonstrated in Table 2.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiment (p. 5); 4.1. Experimental Settings (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Novel View Synthesis | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our method significantly outperforms all recent methods by a large margin 21562 | p. 5 (4.2. Novel View Synthesis) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 6. Ablation study of different training models. Our full model achieves the best 3D object reconstruction with consistent details. Gaussian-based methods due to ... | p. 8 (Figure/Table caption) |
| 4.4. Runtime Efficiency | SYSTEM / EVALUATION SCOPE UNRESOLVED | Given the superior performance achieved, it is deemed acceptable for our method to allocate additional time towards establishing a structured 3D voxel grid and ... | p. 7 (4.4. Runtime Efficiency) |
| 4.2. Novel View Synthesis | SYSTEM / EVALUATION SCOPE UNRESOLVED | The PSNR, SSIM, and LPIPS metrics for novel view synthesis on the GSO dataset are improved by 5.59dB, 0.063, and 0.064, respectively, compared to ... | p. 6 (4.2. Novel View Synthesis) |
| 4.2. Novel View Synthesis | SYSTEM / EVALUATION SCOPE UNRESOLVED | Existing methods lack 3D spatial structures to effectively regulate the spatial distribution of 3D Gaussians, thereby limiting their ability to achieve a higher level ... | p. 6 (4.2. Novel View Synthesis) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** For evaluation, We adopt the most widely used Google Scanned Objects (GSO) dataset [13].
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** Following [27, 70], our model is trained on the Objaverse-LVIS dataset [11] that contains 46K diverse 3D objects in 1156 categories.
- **p. 6 / 4.2. Novel View Synthesis - extractive PDF cue:** Qualitative comparisons of novel view synthesis between GS-RGBN and other methods on the GSO dataset.
- **p. 6 / 4.2. Novel View Synthesis - extractive PDF cue:** Quantitative comparison on the GSO dataset, in terms of PSNR, SSIM, LPIPS, Chamfer Distance (CD) ×10-3 and runtime efficiency.
- **p. 7 / 4.3. Single View Reconstruction - extractive PDF cue:** Ablation study on the different loss functions and normal fusion strategies on the GSO dataset. planeGaussian [70] can generate shapes that exhibit rough alignment with ...
- **p. 7 / 4.5. Ablation study - extractive PDF cue:** It means that all additional loss functions significantly enhance the overall quality of the reconstructed 3D object.
- **p. 8 / 4.5. Ablation study - extractive PDF cue:** Our full model achieves the best 3D object reconstruction with consistent details.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. GS-RGBN is an RGBN-volume Gaussian reconstruction model that generates high-quality 2D Gaussians (middle) using a single image (left). The textured meshes can be ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. The overview of our paradigm. Given a single image of a 3D object, we first input it into an off-the-shelf multi-view diffusion model ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. The illustration of the structure of the cross-volume fu- sion (CVF) module. 4 and 5). Therefore, we propose a hybrid Voxel-Gaussian model that ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative comparisons of novel view synthesis between GS-RGBN and other methods on the GSO dataset. It can be observed that the 3D objects ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparison on the GSO dataset, in terms of PSNR, SSIM, LPIPS, Chamfer Distance (CD) ×10-3 and runtime efficiency. Notably, Time(g) and Time(r) ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative comparisons of single view reconstruction between GS-RGBN and other methods on the GSO dataset. Design PSNR↑ SSIM↑ LPIPS↓ Image-Gaussian 18.82 0.831
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation study on the different loss functions and normal fusion strategies on the GSO dataset. planeGaussian [70] can generate shapes that exhibit rough ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6. Ablation study of different training models. Our full model achieves the best 3D object reconstruction with consistent details. Gaussian-based methods due to varying ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For evaluation, We adopt the most widely used Google Scanned Objects (GSO) dataset [13]. | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings) |
| Task/environment | Following [27, 70], our model is trained on the Objaverse-LVIS dataset [11] that contains 46K diverse 3D objects in 1156 categories. | reset, timeout, object/scene variation | p. 5 (4.1. Experimental Settings), p. 6 (4.2. Novel View Synthesis) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 3 (3. Method), p. 2 (1. Introduction) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3.1. Hybrid Voxel-Gaussian) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The model performance decreases when the LPIPS, depth, and regularization loss terms are successively removed, as demonstrated in Table 2. | definition/direction/unit from same section | p. 7 (4.5. Ablation study) |
| These inconsistencies once again underscore the importance of effectively integrating RGB and normal images for the recovery of both geometric and semantic details. | definition/direction/unit from same section | p. 6 (4.2. Novel View Synthesis) |
| In particular, GS-RGBN demonstrates outstanding performance while still maintaining acceptable efficiency. | definition/direction/unit from same section | p. 7 (4.4. Runtime Efficiency) |
| The model performance demonstrates a decline when reducing the number of VRBs from 3 to 1 or substituting them with 3D CNNs, owing to ... | definition/direction/unit from same section | p. 8 (4.5. Ablation study) |
| Besides, we adopt the Chamfer Distances (CD) to evaluate the quality of reconstructed geometries. | definition/direction/unit from same section | p. 5 (4.1. Experimental Settings) |
| The optimization is performed using AdamW [33], with an initial learning rate of 1 × 10-5 and subsequently following a cosine annealing schedule with ... | definition/direction/unit from same section | p. 5 (4.1. Experimental Settings) |
| For example, LGM [54] and TriplaneGaussian [70] may generate the flattened laptop (first row) and thick castle (second row). | definition/direction/unit from same section | p. 6 (4.2. Novel View Synthesis) |
| We observe a very significant performance drop, indicating that the CVF module offers an effective way of fusing RGB and normal information. | definition/direction/unit from same section | p. 8 (4.5. Ablation study) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method significantly outperforms all recent methods by a large margin 21562 | comparison identity and matched condition | p. 5 (4.2. Novel View Synthesis) |
| We evaluate the novel view synthesis quality of rendered per-view images compared with other methods. | comparison identity and matched condition | p. 5 (4.2. Novel View Synthesis) |
| It can be observed that the baseline methods usually yield inconsistent and irrational results. | comparison identity and matched condition | p. 6 (4.2. Novel View Synthesis) |
| The PSNR, SSIM, and LPIPS metrics for novel view synthesis on the GSO dataset are improved by 5.59dB, 0.063, and 0.064, respectively, compared to ... | comparison identity and matched condition | p. 6 (4.2. Novel View Synthesis) |
| Given the superior performance achieved, it is deemed acceptable for our method to allocate additional time towards establishing a structured 3D voxel grid and ... | comparison identity and matched condition | p. 7 (4.4. Runtime Efficiency) |
| 1, Gaussianbased feed-forward methods (TriplaneGaussian [70], LGM [54] and GS-RGBN) exhibit significantly reduced rendering time compared to traditional approaches (Wonder3D [31] and One-2-3-45 [27]) ... | comparison identity and matched condition | p. 7 (4.4. Runtime Efficiency) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 6. Ablation study of different training models. Our full model achieves the best 3D object reconstruction with consistent details. Gaussian-based methods due to ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| The whole paradigm can be supervised by employing only the L1 loss between RGB and alpha images to ensure a fundamental training process, while ... | component/input/data sensitivity | p. 7 (4.5. Ablation study) |
| The model performance decreases when the LPIPS, depth, and regularization loss terms are successively removed, as demonstrated in Table 2. | component/input/data sensitivity | p. 7 (4.5. Ablation study) |
| As shown in Table 2, we first remove the whole CVF module and directly concatenate RGB and normal volumetric features into MLPs. | component/input/data sensitivity | p. 8 (4.5. Ablation study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • We propose a novel RGBN-volume Gaussian reconstruction model, called GS-RGBN, to generate high-quality 3D assets from ... | Our method significantly outperforms all recent methods by a large margin 21562 | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.2. Novel View Synthesis), p. 8 (Figure/Table caption), p. 7 (4.4. Runtime Efficiency), p. 6 (4.2. Novel View Synthesis), p. 6 (4.2. Novel View Synthesis), p. 7 (4.5. Ablation study) |
| Primary metric/result | Figure 6. Ablation study of different training models. Our full model achieves the best 3D object reconstruction with consistent details. Gaussian-based methods due to ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** The optimization is performed using AdamW [33], with an initial learning rate of 1 × 10-5 and subsequently following a cosine annealing schedule with a ...
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** Similar to previous methods [27, 54, 61, 67, 70], we randomly choose approximately 200 objects to render two single images (i.e., Front and side of ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Besides, voxels cannot be directly used for representing large-scale scenes. | p. 8 (5. Conclusion and Limitations) |
| body limitation/failure cue | Especially, the depth and regularization loss functions, which cannot be achieved by 3D 21564 | p. 7 (4.5. Ablation study) |
| body limitation/failure cue | The performance degradation occurs when the MVD models generate images with a higher level of view inconsistency. | p. 8 (5. Conclusion and Limitations) |
| body limitation/failure cue | These inconsistencies once again underscore the importance of effectively integrating RGB and normal images for the recovery of both geometric and semantic details. | p. 6 (4.2. Novel View Synthesis) |
| body limitation/failure cue | Ablation study on the different loss functions and normal fusion strategies on the GSO dataset. planeGaussian [70] can generate shapes that exhibit rough alignment ... | p. 7 (4.3. Single View Reconstruction) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The optimization is performed using AdamW [33], with an initial learning rate of 1 × 10-5 and subsequently following a cosine annealing schedule with ... | p. 5 (4.1. Experimental Settings) |
| Our model is trained on four A100 (40G) GPUs for approximately 6.5 days, employing a batch size of four per GPU with bfloat16 precision, ... | p. 5 (4.1. Experimental Settings) |
| Quantitative comparison on the GSO dataset, in terms of PSNR, SSIM, LPIPS, Chamfer Distance (CD) ×10-3 and runtime efficiency. | p. 6 (4.2. Novel View Synthesis) |
| We assess the runtime efficiency of GS-RGBN in comparison with other methods. | p. 7 (4.4. Runtime Efficiency) |
| Notably, the total runtime of DreamGaussian [53] and TriplaneGaussian [70] only contains Time(r). | p. 7 (4.4. Runtime Efficiency) |
| The model performance demonstrates a decline when reducing the number of VRBs from 3 to 1 or substituting them with 3D CNNs, owing to ... | p. 8 (4.5. Ablation study) |
| Next, we describe how to decode the RGBN volume to generate high-quality 2D Gaussians for novel view rendering and high-quality shape reconstruction (Sec. | p. 3 (3. Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion and Limitations - extractive PDF cue:** Besides, voxels cannot be directly used for representing large-scale scenes.
- **p. 7 / 4.5. Ablation study - extractive PDF cue:** Especially, the depth and regularization loss functions, which cannot be achieved by 3D 21564
- **p. 8 / 5. Conclusion and Limitations - extractive PDF cue:** The performance degradation occurs when the MVD models generate images with a higher level of view inconsistency.
- **p. 6 / 4.2. Novel View Synthesis - extractive PDF cue:** These inconsistencies once again underscore the importance of effectively integrating RGB and normal images for the recovery of both geometric and semantic details.
- **p. 7 / 4.3. Single View Reconstruction - extractive PDF cue:** Ablation study on the different loss functions and normal fusion strategies on the GSO dataset. planeGaussian [70] can generate shapes that exhibit rough alignment with ...

- **PDF anchors reviewed:** datasets p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings), p. 6 (4.2. Novel View Synthesis), p. 6 (4.2. Novel View Synthesis), p. 7 (4.3. Single View Reconstruction), p. 7 (4.5. Ablation study), metrics p. 7 (4.5. Ablation study), p. 6 (4.2. Novel View Synthesis), p. 7 (4.4. Runtime Efficiency), p. 8 (4.5. Ablation study), p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings), baselines p. 5 (4.2. Novel View Synthesis), p. 5 (4.2. Novel View Synthesis), p. 6 (4.2. Novel View Synthesis), p. 6 (4.2. Novel View Synthesis), p. 7 (4.4. Runtime Efficiency), p. 7 (4.4. Runtime Efficiency), results p. 5 (4.2. Novel View Synthesis), p. 8 (Figure/Table caption), p. 7 (4.4. Runtime Efficiency), p. 6 (4.2. Novel View Synthesis), p. 6 (4.2. Novel View Synthesis), p. 7 (4.5. Ablation study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
