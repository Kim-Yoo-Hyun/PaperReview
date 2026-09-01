# Evaluation - QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=eZNdkwJYbN; PDF retrieval source: https://openreview.net/pdf/cc6e0a2d054469a238a6da05b30dce8f439f11f3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 3 (Figure/Table caption), p. 10 (Figure/Table caption)): The results demonstrate that increasing the crop & split number consistently improves performance.

## Evaluation Body Digest

- **p. 6 / 4 Experiments - extractive PDF cue:** The dataset is officially split into 700 sequences for training, 150 for validation, and 150 for testing.
- **p. 6 / 4 Experiments - extractive PDF cue:** 4.1 Datasets and Metrics nuScenes [3] comprises 1,000 urban driving sequences collected in Boston and Singapore.
- **p. 8 / 4 Experiments - extractive PDF cue:** We report the performance of our QuadricFormer on nuScenes dataset [3] in Table 1.
- **p. 7 / 4 Experiments - extractive PDF cue:** We employ ResNet101-DCN [13] with FCOS3D checkpoint [42] for nuScenes [3], and ResNet50 [13] pretrained on ImageNet [11] 7
- **p. 7 / 4 Experiments - extractive PDF cue:** The official split contains 7 sequences for training, 1 for validation, and 1 for testing, corresponding to 8487, 1812, and 2566 key frames, respectively.
- **p. 8 / 4 Experiments - extractive PDF cue:** We train our model for 20 epochs on nuScenes and KITTI-360 with a batch of 8.
- **p. 9 / 4 Experiments - extractive PDF cue:** FRONT_LEFT FRONT FRONT_RIGHT BACK_RIGHT BACK BACK_LEFT 3D Superquadrics Occupancy Prediction Occupancy Ground Truth barrier construction vehicle motorcycle traffic cone trailer bicycle bus car pedestrian truck ...
- **p. 16 / C Additional Implementation Details - extractive PDF cue:** Prunning-and-Splitting Module: During experiments, we observed that some superquadrics in Q contribute little to scene modeling, which are usually located in empty regions with very ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 6); B Additional Experiments (p. 15); C Additional Implementation Details (p. 16); 4. Experimental result reproducibility (p. 18); 7. Experiment statistical significance (p. 19); 8. Experiments compute resources (p. 20).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results demonstrate that increasing the crop & split number consistently improves performance. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method achieves state-of-the-art performance. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our model is able to predict high-fidelity shapes and achieves comprehensive occupancy results. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | QuadricFormer consistently outperforms prior methods in both 3D semantic occupancy prediction and computational efficiency. | p. 8 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2: Comparisons between different representations. (a) Quadric-based method represents the same object with a smaller number of primitives and greater shape expressiveness. (b) ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4 Experiments - extractive PDF cue:** The dataset is officially split into 700 sequences for training, 150 for validation, and 150 for testing.
- **p. 6 / 4 Experiments - extractive PDF cue:** 4.1 Datasets and Metrics nuScenes [3] comprises 1,000 urban driving sequences collected in Boston and Singapore.
- **p. 8 / 4 Experiments - extractive PDF cue:** We report the performance of our QuadricFormer on nuScenes dataset [3] in Table 1.
- **p. 7 / 4 Experiments - extractive PDF cue:** We employ ResNet101-DCN [13] with FCOS3D checkpoint [42] for nuScenes [3], and ResNet50 [13] pretrained on ImageNet [11] 7
- **p. 7 / 4 Experiments - extractive PDF cue:** The official split contains 7 sequences for training, 1 for validation, and 1 for testing, corresponding to 8487, 1812, and 2566 key frames, respectively.
- **p. 8 / 4 Experiments - extractive PDF cue:** We train our model for 20 epochs on nuScenes and KITTI-360 with a batch of 8.
- **p. 9 / 4 Experiments - extractive PDF cue:** FRONT_LEFT FRONT FRONT_RIGHT BACK_RIGHT BACK BACK_LEFT 3D Superquadrics Occupancy Prediction Occupancy Ground Truth barrier construction vehicle motorcycle traffic cone trailer bicycle bus car pedestrian truck ...
- **p. 16 / C Additional Implementation Details - extractive PDF cue:** Prunning-and-Splitting Module: During experiments, we observed that some superquadrics in Q contribute little to scene modeling, which are usually located in empty regions with very ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Considering the ellipsoidal shape prior of Gaussians, we propose leveraging expressive superquadrics to build an efficient and powerful object-centric representation. Our QuadricFormer achieves ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Comparisons between different representations. (a) Quadric-based method represents the same object with a smaller number of primitives and greater shape expressiveness. (b) Quadric-based ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Overall Framework of QuadricFormer. We use several quadric-encoder blocks to update superquadrics, and employ a pruning-and-splitting module to further enhance modeling efficiency. position ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: 3D semantic occupancy prediction results on nuScenes. * means supervised by dense occupancy annotations as opposed to original LiDAR segmentation labels. Sq. denotes ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Monocular 3D semantic occupancy prediction results on SSCBench-KITTI-360. Num of Prims. denotes the number of primitives in the model. Our method achieves comparable ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Performance and efficiency comparison with Gaussian-based methods. The latency and memory are tested on an NVIDIA 4090 GPU with batch size one during ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 4: 3D Superquadrics and occupancy visualizations on nuScenes. Our model is able to predict high-fidelity shapes and achieves comprehensive occupancy results.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 4: Effect of the ϵ range. Range of ϵ mIoU IoU (0.01, 2) 20.39 31.13 (0.01, 5)

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset is officially split into 700 sequences for training, 150 for validation, and 150 for testing. | embodiment, simulator version and control stack | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Task/environment | 4.1 Datasets and Metrics nuScenes [3] comprises 1,000 urban driving sequences collected in Boston and Singapore. | reset, timeout, object/scene variation | p. 6 (4 Experiments), p. 8 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | 본문 anchor 없음 |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The evaluation metrics adhere to common practice, namely mean Intersection-over-Union (mIoU) and Intersection-over-Union (IoU): mIoU = 1 /C′/ X i∈C′ TPi TPi + FPi ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| We observe that setting the range of (0.1, 2) yields the best results, achieving the highest mIoU (20.51) and IoU (31.25). | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Specifically, our method achieves the highest mIoU (up to 21.11) and IoU (up to 32.13), surpassing all Gaussian-based approaches. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Range of ϵ mIoU IoU (0.01, 2) 20.39 31.13 (0.01, 5) 20.25 30.63 (0.1, 2) 20.51 31.25 (0.1, 5) 19.86 30.65 Table 5: Effect ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Crop & Split Number mIoU IoU 0 19.41 39.77 200 19.65 30.35 400 19.90 30.67 800 20.12 31.22 4.5 Visualizations We present visualizations of ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Figure 2: Comparisons between different representations. (a) Quadric-based method represents the same object with a smaller number of primitives and greater shape expressiveness. (b) ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Our method achieves state-of-the-art performance. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Figure 3: Overall Framework of QuadricFormer. We use several quadric-encoder blocks to update superquadrics, and employ a pruning-and-splitting module to further enhance modeling efficiency. ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to other methods, our approach achieves state-of-the-art performance. | comparison identity and matched condition | p. 8 (4 Experiments) |
| QuadricFormer consistently outperforms prior methods in both 3D semantic occupancy prediction and computational efficiency. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Moreover, our method achieves high-quality performance using only 1600 superquadrics, compared to 6400 Gaussians. | comparison identity and matched condition | p. 9 (4 Experiments) |
| Compared to GaussianFormer-2 [15], our QuadricFormer exhibits enhanced modeling capability for complex objects and road surfaces. | comparison identity and matched condition | p. 9 (4 Experiments) |
| Figure 2: Comparisons between different representations. (a) Quadric-based method represents the same object with a smaller number of primitives and greater shape expressiveness. (b) ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Figure 1: Considering the ellipsoidal shape prior of Gaussians, we propose leveraging expressive superquadrics to build an efficient and powerful object-centric representation. Our QuadricFormer ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.4 Ablation Study Effect of the ϵ Range. | component/input/data sensitivity | p. 8 (4 Experiments) |
| We conduct ablation studies on the effect of the pruningsplitting module, as shown in Table 5. | component/input/data sensitivity | p. 8 (4 Experiments) |
| Range of ϵ mIoU IoU (0.01, 2) 20.39 31.13 (0.01, 5) 20.25 30.63 (0.1, 2) 20.51 31.25 (0.1, 5) 19.86 30.65 Table 5: Effect ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| To clarify, we take the QuadricFormer with N superquadrics as an example and describe the process as follows: Initial Training: We first train a ... | component/input/data sensitivity | p. 16 (C Additional Implementation Details) |
| We employ ResNet101-DCN [13] with FCOS3D checkpoint [42] for nuScenes [3], and ResNet50 [13] pretrained on ImageNet [11] 7 | component/input/data sensitivity | p. 7 (4 Experiments) |
| At this stage, we load the pretrained model parameters and continue training for 10 more epochs. | component/input/data sensitivity | p. 16 (C Additional Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose an efficient and expressive object-centric 3D representation using superquadrics [1] as scene primitives. | The results demonstrate that increasing the crop & split number consistently improves performance. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 3 (Figure/Table caption), p. 10 (Figure/Table caption) |
| Primary metric/result | Our method achieves state-of-the-art performance. | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiments - extractive PDF cue:** Each sequence spans a duration of 20 seconds with RGB images captured by 6 surrounding cameras, and the key frames are annotated at a 2 ...
- **p. 7 / 4 Experiments - extractive PDF cue:** 4.2 Implementation Details The input images are at resolutions of 900×1600 for nuScenes and 376×1408 for KITTI-360 [27] with random flipping and photometric distortion augmentations.
- **p. 8 / 4 Experiments - extractive PDF cue:** The latency and memory are tested on an NVIDIA 4090 GPU with batch size one during inference, in accordance with Gaussian-based methods [18, 15].
- **p. 8 / 4 Experiments - extractive PDF cue:** We train our model for 20 epochs on nuScenes and KITTI-360 with a batch of 8.
- **p. 8 / 4 Experiments - extractive PDF cue:** For similar or even fewer primitives (e.g., 1600 or 3200), our method achieves a latency as low as 162 ms and 2554 MB memory consumption, ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | With random initialization, QuadricFormer cannot fully learn accurate superquadric positions, leaving some superquadrics in empty regions and reducing representation efficiency. | p. 9 (5 Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The latency and memory are tested on an NVIDIA 4090 GPU with batch size one during inference, in accordance with Gaussian-based methods [18, 15]. | p. 8 (4 Experiments) |
| For optimization, we train our model using AdamW with weight decay of 0.01, and maximum learning rate of 4 × 10-4, which decays with ... | p. 8 (4 Experiments) |
| We employ ResNet101-DCN [13] with FCOS3D checkpoint [42] for nuScenes [3], and ResNet50 [13] pretrained on ImageNet [11] 7 | p. 7 (4 Experiments) |
| 4.2 Implementation Details The input images are at resolutions of 900×1600 for nuScenes and 376×1408 for KITTI-360 [27] with random flipping and photometric distortion ... | p. 7 (4 Experiments) |
| We provide implementation details of the prunning-and-splitting module. | p. 16 (C Additional Implementation Details) |
| At this stage, we load the pretrained model parameters and continue training for 10 more epochs. | p. 16 (C Additional Implementation Details) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5 Conclusion - extractive PDF cue:** With random initialization, QuadricFormer cannot fully learn accurate superquadric positions, leaving some superquadrics in empty regions and reducing representation efficiency.

- **PDF anchors reviewed:** datasets p. 6 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), metrics p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 3 (Figure/Table caption), baselines p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 3 (Figure/Table caption), p. 1 (Figure/Table caption), results p. 8 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 3 (Figure/Table caption), p. 10 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
