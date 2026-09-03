# Evaluation - GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3958_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03958.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (4 Experiments), p. 14 (Figure/Table caption), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 13 (Figure/Table caption), p. 12 (Figure/Table caption)): Our GaussianFormer achieves notable improvements over methods based on planar representations, such as BEVFormer [27] and TPVFormer [17].

## Evaluation Body Digest

- **p. 9 / 4 Experiments - extractive body cue:** 4.1 Datasets NuScenes [3] consists of 1000 sequences of various driving scenes collected in Boston and Singapore, which are officially split into 700/150/150 sequences for ...
- **p. 9 / 4 Experiments - extractive body cue:** We conducted experiments on the nuScenes [3] dataset and the KITTI-360 [30] dataset for 3D semantic occupancy prediction with surrounding and monocular cameras, respectively.
- **p. 10 / 4 Experiments - extractive body cue:** This is because the 3D Gaussian representation better exploits the sparse nature of the driving scenes and the diversity of object scales with flexible properties ...
- **p. 10 / 4 Experiments - extractive body cue:** In Table 1, we present a comprehensive quantitative comparison of various methods for multi-view 3D semantic occupancy prediction on nuScenes validation set, with dense annotations ...
- **p. 11 / 4 Experiments - extractive body cue:** We provide the efficiency comparisons of different scene representations in Table 3.
- **p. 11 / 4 Experiments - extractive body cue:** Furthermore, the flexibility of 3D Gaussians also benefits the predictions for general objects (i.e. categories with other- prefix) which often have distinct shapes and appearances ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 5: Ablation on the number of Gaussians. The latency and memory are tested on an NVIDIA 4090 GPU with batch size one during inference. ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Ablation on the components of GaussianFormer. Deep Supervision represents supervising the output of each refinement module. Residual Refine means on which properties of ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our GaussianFormer achieves notable improvements over methods based on planar representations, such as BEVFormer [27] and TPVFormer [17]. | p. 10 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 5: Visualization results for 3D semantic occupancy prediction on nuScenes. We visualize the 3D Gaussians by treating them as ellipsoids centered at the ... | p. 14 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method achieves comparable performance with state-of-the-art methods. | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notably, GaussianFormer achieves comparable performance with state-of-the-art models, excelling at some smaller categories such as motorcycle and general categories such as othervehicle. | p. 11 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 5: Ablation on the number of Gaussians. The latency and memory are tested on an NVIDIA 4090 GPU with batch size one during ... | p. 13 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 9 / 4 Experiments - extractive body cue:** 4.1 Datasets NuScenes [3] consists of 1000 sequences of various driving scenes collected in Boston and Singapore, which are officially split into 700/150/150 sequences for ...
- **p. 9 / 4 Experiments - extractive body cue:** We conducted experiments on the nuScenes [3] dataset and the KITTI-360 [30] dataset for 3D semantic occupancy prediction with surrounding and monocular cameras, respectively.
- **p. 10 / 4 Experiments - extractive body cue:** This is because the 3D Gaussian representation better exploits the sparse nature of the driving scenes and the diversity of object scales with flexible properties ...
- **p. 10 / 4 Experiments - extractive body cue:** In Table 1, we present a comprehensive quantitative comparison of various methods for multi-view 3D semantic occupancy prediction on nuScenes validation set, with dense annotations ...
- **p. 11 / 4 Experiments - extractive body cue:** We provide the efficiency comparisons of different scene representations in Table 3.
- **p. 11 / 4 Experiments - extractive body cue:** Furthermore, the flexibility of 3D Gaussians also benefits the predictions for general objects (i.e. categories with other- prefix) which often have distinct shapes and appearances ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Considering the universal approximating ability of Gaussian mixture [9, 12], we propose an object-centric 3D semantic Gaussian representation to describe the fine- grained ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2: Comparisions of the proposed 3D Gaussian representation with ex- iting grid-based scene representations (figures from TPVFormer [17]). The voxel representation [24, 51] assigns ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Framework of our GaussianFormer for 3D semantic occupancy pre- diction. We first extract multi-scale (M.S.) features from image inputs using an image backbone. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: Illustration of the Gaussian-to-voxel splatting method in 2D. We first voxelize the 3D Gaussians and record the affected voxels of each 3D Gaussian ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 1: 3D semantic occupancy prediction results on nuScenes validation set. While the original TPVFormer [17] is trained with LiDAR segmentation labels, TPVFormer* is supervised ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 2: 3D semantic occupancy prediction results on SSCBench-KITTI- 360 validation set. Our method achieves performance on par with state-of-the-art methods, excelling at some smaller ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3: Efficiency comparison of different representations on nuScenes. The latency and memory consumption for GaussianFormer are tested on one NVIDIA 4090 GPU with batch ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Ablation on the components of GaussianFormer. Deep Supervision represents supervising the output of each refinement module. Residual Refine means on which properties of ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.1 Datasets NuScenes [3] consists of 1000 sequences of various driving scenes collected in Boston and Singapore, which are officially split into 700/150/150 sequences ... | embodiment, simulator version and control stack | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Task/environment | We conducted experiments on the nuScenes [3] dataset and the KITTI-360 [30] dataset for 3D semantic occupancy prediction with surrounding and monocular cameras, respectively. | reset, timeout, object/scene variation | p. 9 (4 Experiments), p. 10 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (1 Introduction), p. 1 (Body text (section not recovered)) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 5: Ablation on the number of Gaussians. The latency and memory are tested on an NVIDIA 4090 GPU with batch size one during ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Table 4: Ablation on the components of GaussianFormer. Deep Supervision represents supervising the output of each refinement module. Residual Refine means on which properties ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Fig. 1: Considering the universal approximating ability of Gaussian mixture [9, 12], we propose an object-centric 3D semantic Gaussian representation to describe the fine- ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| We use the feature pyramid network [31] (FPN) to generate multi-scale image features with downsample rates of 4, 8, 16 and 32. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| The learning rate warms up in the first 500 iterations to a maximum value of 2e-4 and decreases according to a cosine schedule. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Our method achieves comparable performance with state-of-the-art methods. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Notably, GaussianFormer achieves comparable performance with state-of-the-art models, excelling at some smaller categories such as motorcycle and general categories such as othervehicle. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Our method demonstrates significantly reduced memory usage compared to other representations. | definition/direction/unit from same section | p. 12 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Even compared with dense grid representations, GaussianFormer performs on par with OccFormer [58] and SurroundOcc [51]. | comparison identity and matched condition | p. 10 (4 Experiments) |
| Our method achieves comparable performance with state-of-the-art methods. | comparison identity and matched condition | p. 11 (4 Experiments) |
| Notably, GaussianFormer achieves comparable performance with state-of-the-art models, excelling at some smaller categories such as motorcycle and general categories such as othervehicle. | comparison identity and matched condition | p. 11 (4 Experiments) |
| Our method demonstrates significantly reduced memory usage compared to other representations. | comparison identity and matched condition | p. 12 (4 Experiments) |
| In Table 1, we present a comprehensive quantitative comparison of various methods for multi-view 3D semantic occupancy prediction on nuScenes validation set, with dense ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| Fig. 1: Considering the universal approximating ability of Gaussian mixture [9, 12], we propose an object-centric 3D semantic Gaussian representation to describe the fine- ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 4: Ablation on the components of GaussianFormer. Deep Supervision represents supervising the output of each refinement module. Residual Refine means on which properties ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Fig. 1: Considering the universal approximating ability of Gaussian mixture [9, 12], we propose an object-centric 3D semantic Gaussian representation to describe the fine- ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Table 5: Ablation on the number of Gaussians. The latency and memory are tested on an NVIDIA 4090 GPU with batch size one during ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Fig. 5: Visualization results for 3D semantic occupancy prediction on nuScenes. We visualize the 3D Gaussians by treating them as ellipsoids centered at the ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| We employ ResNet101-DCN [13] initialized from FCOS3D [48] checkpoint as the image backbone for nuScenes and ResNet50 [13] pretrained with ImageNet [10] for KITTI-360. | component/input/data sensitivity | p. 10 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose a GaussianFormer model to effectively obtain 3D semantic Gaussians from image inputs. | Our GaussianFormer achieves notable improvements over methods based on planar representations, such as BEVFormer [27] and TPVFormer [17]. | PDF body cue; verify exact table/figure and matched conditions | p. 10 (4 Experiments), p. 14 (Figure/Table caption), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 13 (Figure/Table caption), p. 12 (Figure/Table caption) |
| Primary metric/result | Fig. 5: Visualization results for 3D semantic occupancy prediction on nuScenes. We visualize the 3D Gaussians by treating them as ellipsoids centered at the ... | numeric claim only at cited anchor | p. 14 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 10 / 4 Experiments - extractive body cue:** Zheng et al. with RGB images collected by 6 surrounding cameras, and the keyframes are annotated at 2Hz.
- **p. 10 / 4 Experiments - extractive body cue:** We train our models for 20 epochs with a batch size of 8, and employ random flip and photometric distortion augmentations.
- **p. 12 / 4 Experiments - extractive body cue:** The latency and memory consumption for GaussianFormer are tested on one NVIDIA 4090 GPU with batch size one, while the results for other methods are ...
- **p. 12 / 4 Experiments - extractive body cue:** Methods Query Form Query Resolution Latency ↓Memory ↓ BEVFormer [27] 2D BEV 200×200 302 ms

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This is because the positions of Gaussians are sensitive to noise which quickly converge to a trivial solution without regularization for coherence during refinement. | p. 12 (26500 M) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train our models for 20 epochs with a batch size of 8, and employ random flip and photometric distortion augmentations. | p. 10 (4 Experiments) |
| The latency and memory consumption for GaussianFormer are tested on one NVIDIA 4090 GPU with batch size one, while the results for other methods ... | p. 12 (4 Experiments) |
| The learning rate warms up in the first 500 iterations to a maximum value of 2e-4 and decreases according to a cosine schedule. | p. 10 (4 Experiments) |
| We then decode the properties of 3D semantic Gaussians from the updated queries as the scene representation. | p. 3 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / 26500 M - extractive body cue:** This is because the positions of Gaussians are sensitive to noise which quickly converge to a trivial solution without regularization for coherence during refinement.

- **Evidence anchors reviewed:** datasets p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), metrics p. 13 (Figure/Table caption), p. 12 (Figure/Table caption), p. 1 (Figure/Table caption), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), baselines p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 10 (4 Experiments), p. 1 (Figure/Table caption), results p. 10 (4 Experiments), p. 14 (Figure/Table caption), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 13 (Figure/Table caption), p. 12 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
