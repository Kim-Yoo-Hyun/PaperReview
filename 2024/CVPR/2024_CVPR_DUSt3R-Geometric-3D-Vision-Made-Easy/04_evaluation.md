# Evaluation - DUSt3R: Geometric 3D Vision Made Easy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2312.14132; PDF retrieval source: https://arxiv.org/pdf/2312.14132. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.4. Multi-view Depth), p. 7 (4.2. Multi-view Pose Estimation), p. 7 (4.1. Visual Localization), p. 9 (4.6. Ablations), p. 6 (4. Experiments with DUSt3R), p. 6 (4. Experiments with DUSt3R)): We observe in Table 3 that DUSt3R achieves stateof-the-art accuracy on ETH-3D and outperforms most recent state-of-the-art methods overall, even those using groundtruth camera poses.

## Evaluation Body Digest

- **p. 6 / 4. Experiments with DUSt3R - extractive body cue:** These datasets feature diverse scenes types: indoor, outdoor, synthetic, real-world, object-centric, etc.
- **p. 8 / 4.4. Multi-view Depth - extractive body cue:** This showcases the applicability of our method on a large variety of domains, either indoors, outdoors, small scale or large scale scenes, while not having ...
- **p. 6 / 4. Experiments with DUSt3R - extractive body cue:** In the remainder of this section, we benchmark DUSt3R on a representative set of classical 3D vision tasks, each time specifying datasets, metrics and comparing ...
- **p. 7 / 4.1. Visual Localization - extractive body cue:** We first evaluate DUSt3R for the task of absolute pose estimation on the 7Scenes [114] and Cambridge Landmarks datasets [49].
- **p. 7 / 4.3. Monocular Depth - extractive body cue:** We benchmark DUSt3R on two outdoor (DDAD [41], KITTI [35]) and three indoor (NYUv2 [115], BONN [80], TUM [119]) datasets.
- **p. 8 / 4.5. 3D Reconstruction - extractive body cue:** We evaluate our predictions on the DTU [1] dataset.
- **p. 9 / 15.6 51.5 17.4 (374.2) - extractive body cue:** Furthermore, best results on this task are usually obtained via sub-pixel accurate triangulation, requiring the use of explicit camera parameters, whereas our approach relies on ...
- **p. 7 / 4.3. Monocular Depth - extractive body cue:** We use two metrics commonly used in the monocular depth evaluations [6, 117]: the absolute relative error AbsRel between target y and prediction ˆy, AbsRel ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments with DUSt3R (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Multi-view Depth | EMPIRICAL / REAL-ROBOT OR HARDWARE | We observe in Table 3 that DUSt3R achieves stateof-the-art accuracy on ETH-3D and outperforms most recent state-of-the-art methods overall, even those using groundtruth camera ... | p. 8 (4.4. Multi-view Depth) |
| 4.2. Multi-view Pose Estimation | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 2, DUSt3R with global alignment achieves the best overall performance on the two datasets and significantly surpasses the state-of-the-art PoseDiffusion ... | p. 7 (4.2. Multi-view Pose Estimation) |
| 4.1. Visual Localization | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method obtains comparable accuracy compared to existing approaches, being feature-matching ones [101, 103] or end-to-end learningbased methods [11, 55, 102, 125, 152], even ... | p. 7 (4.1. Visual Localization) |
| 4.6. Ablations | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, the observed consistent improvements suggest the crucial role of pretraining and high resolution in modern data-driven approaches, as also noted by [78, 149]. | p. 9 (4.6. Ablations) |
| 4. Experiments with DUSt3R | EMPIRICAL / REAL-ROBOT OR HARDWARE | We emphasize that all results are obtained with the same DUSt3R model (our default model is denoted as ‘DUSt3R 512', other DUSt3R models serves ... | p. 6 (4. Experiments with DUSt3R) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiments with DUSt3R - extractive body cue:** These datasets feature diverse scenes types: indoor, outdoor, synthetic, real-world, object-centric, etc.
- **p. 8 / 4.4. Multi-view Depth - extractive body cue:** This showcases the applicability of our method on a large variety of domains, either indoors, outdoors, small scale or large scale scenes, while not having ...
- **p. 6 / 4. Experiments with DUSt3R - extractive body cue:** In the remainder of this section, we benchmark DUSt3R on a representative set of classical 3D vision tasks, each time specifying datasets, metrics and comparing ...
- **p. 7 / 4.1. Visual Localization - extractive body cue:** We first evaluate DUSt3R for the task of absolute pose estimation on the 7Scenes [114] and Cambridge Landmarks datasets [49].
- **p. 7 / 4.3. Monocular Depth - extractive body cue:** We benchmark DUSt3R on two outdoor (DDAD [41], KITTI [35]) and three indoor (NYUv2 [115], BONN [80], TUM [119]) datasets.
- **p. 8 / 4.5. 3D Reconstruction - extractive body cue:** We evaluate our predictions on the DTU [1] dataset.
- **p. 9 / 15.6 51.5 17.4 (374.2) - extractive body cue:** Furthermore, best results on this task are usually obtained via sub-pixel accurate triangulation, requiring the use of explicit camera parameters, whereas our approach relies on ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Overview: Given an unconstrained image collection, i.e. a set of photographs with unknown camera poses and intrinsics, our proposed method DUSt3R outputs a ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Architecture of the network F. Two views of a scene (I1, I2) are first encoded in a Siamese manner with a shared ViT ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Reconstruction examples on two scenes never seen during training. From left to right: RGB, depth map, confidence map, reconstruction. The left scene shows ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1. Absolute camera pose on 7Scenes [114] and Cambridge-Landmarks [49] datasets. We report the median translation and rotation errors (cm/◦) to feature matching (FM) ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Left: Monocular depth estimation on multiple benchmarks. D-Supervised, SS-Self-supervised, T-transfer (zero-shot). (Parentheses) refers to training on the same set. Right: Multi-view pose regression ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3. Multi-view depth evaluation with different settings: a) Classical approaches; b) with poses and depth range, without alignment; c) absolute scale evaluation with poses, ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4. MVS results on the DTU dataset, in mm. Traditional handcrafted methods (a) have been overcome by learning-based approaches (b) that train on this ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 4. Example of 3D reconstruction of an unseen MegaDepth scene from two images (top-left). Note this is the raw output of the network, i.e. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | These datasets feature diverse scenes types: indoor, outdoor, synthetic, real-world, object-centric, etc. | embodiment, simulator version and control stack | p. 6 (4. Experiments with DUSt3R), p. 8 (4.4. Multi-view Depth) |
| Task/environment | This showcases the applicability of our method on a large variety of domains, either indoors, outdoors, small scale or large scale scenes, while not ... | reset, timeout, object/scene variation | p. 8 (4.4. Multi-view Depth), p. 6 (4. Experiments with DUSt3R) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.1. Overview), p. 5 (3.2. Training Objective) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 4 (3.1. Overview) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use two metrics commonly used in the monocular depth evaluations [6, 117]: the absolute relative error AbsRel between target y and prediction ˆy, ... | definition/direction/unit from same section | p. 7 (4.3. Monocular Depth) |
| 4 we report the averaged accuracy, averaged completeness and overall averaged error metrics as provided by the authors of the benchmarks. | definition/direction/unit from same section | p. 8 (4.5. 3D Reconstruction) |
| The accuracy for a point of the reconstructed shape is defined as the smallest Euclidean distance to the ground-truth, and the completeness of a ... | definition/direction/unit from same section | p. 8 (4.5. 3D Reconstruction) |
| Yet, without prior knowledge about the cameras, we reach an average accuracy of 2.7mm, with a completeness of 0.8mm, for an overall average distance ... | definition/direction/unit from same section | p. 9 (15.6 51.5 17.4 (374.2)) |
| We report the median translation and rotation errors in (cm/◦), respectively. | definition/direction/unit from same section | p. 7 (4.1. Visual Localization) |
| We believe this level of accuracy to be of great use in practice, considering the plug-and-play nature of our approach. | definition/direction/unit from same section | p. 9 (15.6 51.5 17.4 (374.2)) |
| Cross-View completion (CroCo) is a recently proposed pretraining paradigm inspired by MAE [46] that has been shown to excel on various downstream 3D vision ... | definition/direction/unit from same section | p. 6 (4. Experiments with DUSt3R) |
| In the remainder of this section, we benchmark DUSt3R on a representative set of classical 3D vision tasks, each time specifying datasets, metrics and ... | definition/direction/unit from same section | p. 6 (4. Experiments with DUSt3R) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method obtains comparable accuracy compared to existing approaches, being feature-matching ones [101, 103] or end-to-end learningbased methods [11, 55, 102, 125, 152], even ... | comparison identity and matched condition | p. 7 (4.1. Visual Localization) |
| It outperforms the self-supervised baselines [6, 37, 121] and performs on-par with state-of-the-art supervised baselines [91, 174]. | comparison identity and matched condition | p. 7 (4.3. Monocular Depth) |
| We observe in Table 3 that DUSt3R achieves stateof-the-art accuracy on ETH-3D and outperforms most recent state-of-the-art methods overall, even those using groundtruth camera ... | comparison identity and matched condition | p. 8 (4.4. Multi-view Depth) |
| In the remainder of this section, we benchmark DUSt3R on a representative set of classical 3D vision tasks, each time specifying datasets, metrics and ... | comparison identity and matched condition | p. 6 (4. Experiments with DUSt3R) |
| (1.7) 21.1 65.6 108.4 31.0 0.82 MVS2D ScanNet [160] ✓ × ✓ × 73.4 0.0 (4.5) (54.1) 30.7 14.4 5.0 57.9 56.4 11.1 34.0 ... | comparison identity and matched condition | p. 9 (15.6 51.5 17.4 (374.2)) |
| We emphasize that all results are obtained with the same DUSt3R model (our default model is denoted as ‘DUSt3R 512', other DUSt3R models serves ... | comparison identity and matched condition | p. 6 (4. Experiments with DUSt3R) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We emphasize that all results are obtained with the same DUSt3R model (our default model is denoted as ‘DUSt3R 512', other DUSt3R models serves ... | component/input/data sensitivity | p. 6 (4. Experiments with DUSt3R) |
| For results obtained without using ground-truth intrinsics parameters, refer to the appendix in Sec. | component/input/data sensitivity | p. 7 (4.1. Visual Localization) |
| In other words, we simply use the raw pointmaps output from F(IQ, IB) without any refinement, where IQ is the query image and IB ... | component/input/data sensitivity | p. 7 (4.1. Visual Localization) |
| Yet, without prior knowledge about the cameras, we reach an average accuracy of 2.7mm, with a completeness of 0.8mm, for an overall average distance ... | component/input/data sensitivity | p. 9 (15.6 51.5 17.4 (374.2)) |
| Multi-view depth evaluation with different settings: a) Classical approaches; b) with poses and depth range, without alignment; c) absolute scale evaluation with poses, without ... | component/input/data sensitivity | p. 9 (15.6 51.5 17.4 (374.2)) |
| Figure 1. Overview: Given an unconstrained image collection, i.e. a set of photographs with unknown camera poses and intrinsics, our proposed method DUSt3R outputs ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Before delving into the details of our method, we introduce below the essential concept of pointmaps. | We observe in Table 3 that DUSt3R achieves stateof-the-art accuracy on ETH-3D and outperforms most recent state-of-the-art methods overall, even those using groundtruth camera ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.4. Multi-view Depth), p. 7 (4.2. Multi-view Pose Estimation), p. 7 (4.1. Visual Localization), p. 9 (4.6. Ablations), p. 6 (4. Experiments with DUSt3R), p. 6 (4. Experiments with DUSt3R) |
| Primary metric/result | As shown in Table 2, DUSt3R with global alignment achieves the best overall performance on the two datasets and significantly surpasses the state-of-the-art PoseDiffusion ... | numeric claim only at cited anchor | p. 7 (4.2. Multi-view Pose Estimation) |

- Numeric sentences retained from the body:
- **p. 6 / 4. Experiments with DUSt3R - extractive body cue:** To mitigate the high cost associated with such input, we train our network sequentially, first on 224×224 images and then on larger 512-pixel images.
- **p. 7 / 4.1. Visual Localization - extractive body cue:** We first evaluate DUSt3R for the task of absolute pose estimation on the 7Scenes [114] and Cambridge Landmarks datasets [49].
- **p. 7 / 4.1. Visual Localization - extractive body cue:** 7Scenes contains 7 indoor scenes with RGB-D images from videos and their 6-DOF camera poses.
- **p. 7 / 4.1. Visual Localization - extractive body cue:** We use the top 20 retrieved images for Cambridge-Landmarks and top 1 for 7Scenes and leverage the known query intrinsics.
- **p. 7 / 4.2. Multi-view Pose Estimation - extractive body cue:** CO3Dv2 contains 6 million frames extracted from approximately 37k videos, covering 51 MS-COCO categories.
- **p. 7 / 4.2. Multi-view Pose Estimation - extractive body cue:** The ground-truth camera poses are annotated using COLMAP from 200 frames in each video.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our method does not reach the accuracy levels of the best methods. | p. 8 (4.5. 3D Reconstruction) |
| body limitation/failure cue | (1.7) 21.1 65.6 108.4 31.0 0.82 MVS2D ScanNet [160] ✓ × ✓ × 73.4 0.0 (4.5) (54.1) 30.7 14.4 5.0 57.9 56.4 11.1 34.0 ... | p. 9 (15.6 51.5 17.4 (374.2)) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our network architecture comprises a Vit-Large for the encoder [27], a ViT-Base for the decoder and a DPT head [91]. | p. 6 (4. Experiments with DUSt3R) |
| To compute camera poses in world coordinates, we use DUSt3R as a 2D-2D pixel matcher (see Section 3.3) between a query and the most ... | p. 7 (4.1. Visual Localization) |
| The optimization is carried out using standard gradient descent and typically converges after a few hundred steps, requiring mere seconds on a standard GPU. | p. 6 (3.4. Global Alignment) |
| The network then reasons over both of them jointly in the decoder. | p. 4 (3.1. Overview) |
| Two views of a scene (I1, I2) are first encoded in a Siamese manner with a shared ViT encoder. | p. 4 (3. Method) |
| To that aim, we either use existing off-the-shelf image retrieval methods, or we pass all pairs through network F (inference takes ≈40ms on a ... | p. 5 (3.4. Global Alignment) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.5. 3D Reconstruction - extractive body cue:** Our method does not reach the accuracy levels of the best methods.
- **p. 9 / 15.6 51.5 17.4 (374.2) - extractive body cue:** (1.7) 21.1 65.6 108.4 31.0 0.82 MVS2D ScanNet [160] ✓ × ✓ × 73.4 0.0 (4.5) (54.1) 30.7 14.4 5.0 57.9 56.4 11.1 34.0 27.5 ...

- **Evidence anchors reviewed:** datasets p. 6 (4. Experiments with DUSt3R), p. 8 (4.4. Multi-view Depth), p. 6 (4. Experiments with DUSt3R), p. 7 (4.1. Visual Localization), p. 7 (4.3. Monocular Depth), p. 8 (4.5. 3D Reconstruction), metrics p. 7 (4.3. Monocular Depth), p. 8 (4.5. 3D Reconstruction), p. 8 (4.5. 3D Reconstruction), p. 9 (15.6 51.5 17.4 (374.2)), p. 7 (4.1. Visual Localization), p. 9 (15.6 51.5 17.4 (374.2)), baselines p. 7 (4.1. Visual Localization), p. 7 (4.3. Monocular Depth), p. 8 (4.4. Multi-view Depth), p. 6 (4. Experiments with DUSt3R), p. 9 (15.6 51.5 17.4 (374.2)), p. 6 (4. Experiments with DUSt3R), results p. 8 (4.4. Multi-view Depth), p. 7 (4.2. Multi-view Pose Estimation), p. 7 (4.1. Visual Localization), p. 9 (4.6. Ablations), p. 6 (4. Experiments with DUSt3R), p. 6 (4. Experiments with DUSt3R).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Our method obtains comparable accuracy compared to existing approaches, being feature-matching ones [101, 103] or end-to-end learningbased methods [11, 55, 102, 125, 152], even managing to outperform strong baselines like ... (p. 7, 4.1. Visual Localization).
- **Metric evidence:** Cross-View completion (CroCo) is a recently proposed pretraining paradigm inspired by MAE [46] that has been shown to excel on various downstream 3D vision tasks, and is thus particularly suited ... (p. 6, 4. Experiments with DUSt3R).
- **Baseline/ablation evidence:** It outperforms the self-supervised baselines [6, 37, 121] and performs on-par with state-of-the-art supervised baselines [91, 174]. (p. 7, 4.3. Monocular Depth).
- **Failure/negative evidence:** Procrustes alignment is, unfortunately, sensitive to noise and outliers. (p. 5, 3.3. Downstream Applications).
