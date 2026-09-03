# Evaluation - Digging Into Self-Supervised Monocular Depth Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1806.01260; PDF retrieval source: https://arxiv.org/pdf/1806.01260. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 5 (4. Experiments), p. 14 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption), p. 5 (4.1. KITTI Eigen Split)): Table 2. Ablation. Results for different variants of our model (Monodepth2) with monocular training on KITTI 2015 [13] using the Eigen split. (a) The baseline model, with none of our ...

## Evaluation Body Digest

- **p. 7 / 4.2. Additional Datasets - extractive body cue:** KITTI Depth Prediction Benchmark We also perform experiments on the recently introduced KITTI Depth Prediction Evaluation dataset [59], which features more accurate ground truth depth, ...
- **p. 7 / 4.2. Additional Datasets - extractive body cue:** We train models using this new benchmark split, and evaluate it using the online server [27], and provide results in supplementary Section D.3.
- **p. 5 / 4. Experiments - extractive body cue:** We evaluate our models, named Monodepth2, on the KITTI 2015 stereo dataset [13], to allow comparison with previously published monocular methods.
- **p. 5 / 4. Experiments - extractive body cue:** Here, we validate that (1) our reprojection loss helps with occluded pixels compared to existing pixel-averaging, (2) our auto-masking improves results, especially when training on ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4. Odometry results on the KITTI [13] odometry dataset. Results show the average absolute trajectory error, and standard deviation, in meters. † - newer ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 5. Auto-masking. We show auto-masks computed after one epoch, where black pixels are removed from the loss (i.e. µ = 0). The mask prevents ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 7. We present results for all other methods for which we have obtained predictions from the authors. We use the same error metrics from ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Overview. (a) Depth network: We use a standard, fully convolutional, U-Net to predict depth. (b) Pose network: Pose between a pair of frames ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.2. Additional Datasets (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2. Ablation. Results for different variants of our model (Monodepth2) with monocular training on KITTI 2015 [13] using the Eigen split. (a) The ... | p. 7 (Figure/Table caption) |
| 4. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Here, we validate that (1) our reprojection loss helps with occluded pixels compared to existing pixel-averaging, (2) our auto-masking improves results, especially when training ... | p. 5 (4. Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 7. We present results for all other methods for which we have obtained predictions from the authors. We use the same error metrics ... | p. 14 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 6. Qualitative Make3D results. All methods were trained on KITTI using monocular supervision. Further, in Table 2(a), we replace our auto-masking loss with ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 7. KITTI improved ground truth. Comparison to existing meth- ods on KITTI 2015 [13] using 93% of the Eigen split and the improved ... | p. 14 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4.2. Additional Datasets - extractive body cue:** KITTI Depth Prediction Benchmark We also perform experiments on the recently introduced KITTI Depth Prediction Evaluation dataset [59], which features more accurate ground truth depth, ...
- **p. 7 / 4.2. Additional Datasets - extractive body cue:** We train models using this new benchmark split, and evaluate it using the online server [27], and provide results in supplementary Section D.3.
- **p. 5 / 4. Experiments - extractive body cue:** We evaluate our models, named Monodepth2, on the KITTI 2015 stereo dataset [13], to allow comparison with previously published monocular methods.
- **p. 5 / 4. Experiments - extractive body cue:** Here, we validate that (1) our reprojection loss helps with occluded pixels compared to existing pixel-averaging, (2) our auto-masking improves results, especially when training on ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Depth from a single image. Our self-supervised model, Monodepth2, produces sharp, high quality depth maps, whether trained with monocular (M), stereo (S), or ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Moving objects. Monocular methods can fail to predict depth for objects that were often observed to be in motion dur- ing training e.g. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Overview. (a) Depth network: We use a standard, fully convolutional, U-Net to predict depth. (b) Pose network: Pose between a pair of frames ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Benefit of min. reprojection loss in MS training. Pix- els in the the circled region are occluded in IR so no loss is ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 5. Auto-masking. We show auto-masks computed after one epoch, where black pixels are removed from the loss (i.e. µ = 0). The mask prevents ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative results. Com- parison of our method to existing methods on KITTI 2015 [13] using the Eigen split. Best results in each category ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Ablation. Results for different variants of our model (Monodepth2) with monocular training on KITTI 2015 [13] using the Eigen split. (a) The baseline ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. Qualitative Make3D results. All methods were trained on KITTI using monocular supervision. Further, in Table 2(a), we replace our auto-masking loss with a ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | KITTI Depth Prediction Benchmark We also perform experiments on the recently introduced KITTI Depth Prediction Evaluation dataset [59], which features more accurate ground truth ... | embodiment, simulator version and control stack | p. 7 (4.2. Additional Datasets), p. 7 (4.2. Additional Datasets) |
| Task/environment | We train models using this new benchmark split, and evaluate it using the online server [27], and provide results in supplementary Section D.3. | reset, timeout, object/scene variation | p. 7 (4.2. Additional Datasets), p. 5 (4. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 5 (3.3. Additional Considerations) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 3 (3. Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Here, we validate that (1) our reprojection loss helps with occluded pixels compared to existing pixel-averaging, (2) our auto-masking improves results, especially when training ... | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Table 4. Odometry results on the KITTI [13] odometry dataset. Results show the average absolute trajectory error, and standard deviation, in meters. † - ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Figure 5. Auto-masking. We show auto-masks computed after one epoch, where black pixels are removed from the loss (i.e. µ = 0). The mask ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 7. We present results for all other methods for which we have obtained predictions from the authors. We use the same error metrics ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Figure 3. Overview. (a) Depth network: We use a standard, fully convolutional, U-Net to predict depth. (b) Pose network: Pose between a pair of ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 8. Failure cases. Top: Our self-supervised loss fails to learn good depths for distorted, reflective and color-saturated re- gions. Bottom: We can fail ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 11. Effect of varying resolutions on the KITTI Eigen split. All predicted disparity maps have been resized to the same size for visualization. ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Figure 2. Moving objects. Monocular methods can fail to predict depth for objects that were often observed to be in motion dur- ing training ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 12. Additional Wander results. We observe that our model (Ours M) results in fewer visual artifacts when compared to the the baseline (i.e. ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |
| Table 2. Ablation. Results for different variants of our model (Monodepth2) with monocular training on KITTI 2015 [13] using the Eigen split. (a) The ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 9. Qualitative ablation study. We can see that our model with all components added result in the smallest amount of depth artifacts. ‘Baseline ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| Here, we validate that (1) our reprojection loss helps with occluded pixels compared to existing pixel-averaging, (2) our auto-masking improves results, especially when training ... | comparison identity and matched condition | p. 5 (4. Experiments) |
| Table 7. KITTI improved ground truth. Comparison to existing meth- ods on KITTI 2015 [13] using 93% of the Eigen split and the improved ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| Figure 13. Additional KITTI Eigen split test results. We can see that our approaches in the last three rows produce the sharpest depth maps. ... | comparison identity and matched condition | p. 18 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2. Ablation. Results for different variants of our model (Monodepth2) with monocular training on KITTI 2015 [13] using the Eigen split. (a) The ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Except in ablation experiments, for training which uses monocular sequences (i.e. monocular and monocular plus stereo) we follow Zhou et al.'s [76] pre-processing to ... | component/input/data sensitivity | p. 5 (4.1. KITTI Eigen Split) |
| Figure 9. Qualitative ablation study. We can see that our model with all components added result in the smallest amount of depth artifacts. ‘Baseline ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Table 12. Ablation of the effect of pose networks on depth prediction. Results shown are on depth prediction on the KITTI dataset, when trained ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| Table 10. Effect of post-processing. We observe that post-processing, originally motivated only for stereo training, also brings consistent benefits to all our monocular-trained models. ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |
| Figure 11. Effect of varying resolutions on the KITTI Eigen split. All predicted disparity maps have been resized to the same size for visualization. ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method succeeds here where others, and our baseline with our contributions turned off, fail. motion is observed in monocular training. | Table 2. Ablation. Results for different variants of our model (Monodepth2) with monocular training on KITTI 2015 [13] using the Eigen split. (a) The ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 5 (4. Experiments), p. 14 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption), p. 5 (4.1. KITTI Eigen Split) |
| Primary metric/result | Here, we validate that (1) our reprojection loss helps with occluded pixels compared to existing pixel-averaging, (2) our auto-masking improves results, especially when training ... | numeric claim only at cited anchor | p. 5 (4. Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / 3.3. Additional Considerations - extractive body cue:** Our models are implemented in PyTorch [46], trained for 20 epochs using Adam [26], with a batch size of 12 and an input/output resolution of ...
- **p. 5 / 3.3. Additional Considerations - extractive body cue:** We use a learning rate of 10-4 for the first 15 epochs which is then dropped to 10-5 for the remainder.
- **p. 5 / 3.3. Additional Considerations - extractive body cue:** Training takes 8, 12, and 15 hours on a single Titan Xp, for the stereo (S), monocular (M), and monocular plus stereo models (MS).
- **p. 6 / Method - extractive body cue:** 200 epochs) and no use of postprocessing.
- **p. 7 / Method - extractive body cue:** We train these ‘w/o pretraining' models for 30 epochs to ensure convergence.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 8. Failure cases. Top: Our self-supervised loss fails to learn good depths for distorted, reflective and color-saturated re- gions. Bottom: We can fail ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Figure 10. Additional Make3D results. Our model (MD2 M) trained on KITTI results in plausible depths, predicting more detail than existing monocular methods. The ... | p. 15 (Figure/Table caption) |
| body limitation/failure cue | Figure 11. Effect of varying resolutions on the KITTI Eigen split. All predicted disparity maps have been resized to the same size for visualization. ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | Table 9. KITTI depth prediction benchmark. Comparison of our monocular plus stereo approaches to fully supervised methods on the KITTI depth prediction benchmark [27]. ... | p. 15 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. Moving objects. Monocular methods can fail to predict depth for objects that were often observed to be in motion dur- ing training ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 3. Overview. (a) Depth network: We use a standard, fully convolutional, U-Net to predict depth. (b) Pose network: Pose between a pair of ... | p. 3 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Similar to [12, 15, 76], we also formulate our problem as the minimization of a photometric reprojection error at training time. | p. 3 (3.1. Self-Supervised Training) |
| We use a learning rate of 10-4 for the first 15 epochs which is then dropped to 10-5 for the remainder. | p. 5 (3.3. Additional Considerations) |
| Our models are implemented in PyTorch [46], trained for 20 epochs using Adam [26], with a batch size of 12 and an input/output resolution ... | p. 5 (3.3. Additional Considerations) |
| These ‘no camera motion' sequences can cause problems for self-supervised monocular training, and as a result, they are typically excluded at training time using ... | p. 6 (Method) |
| For simplicity of notation we assume the pre-computed intrinsics K of all the views are identical, though they can be different. | p. 3 (3.1. Self-Supervised Training) |
| We achieve high accuracy despite using a lower resolution than [47]'s 1024 × 384, with substantially less training time (20 vs. | p. 6 (Method) |
| The mask is computed from the input frames and network predictions using Eqn. | p. 4 (3.2. Improved Self-Supervised Depth Estimation) |
| We show auto-masks computed after one epoch, where black pixels are removed from the loss (i.e. µ = 0). | p. 4 (3.2. Improved Self-Supervised Depth Estimation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8. Failure cases. Top: Our self-supervised loss fails to learn good depths for distorted, reflective and color-saturated re- gions. Bottom: We can fail to ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 10. Additional Make3D results. Our model (MD2 M) trained on KITTI results in plausible depths, predicting more detail than existing monocular methods. The last ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 11. Effect of varying resolutions on the KITTI Eigen split. All predicted disparity maps have been resized to the same size for visualization. Our ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 9. KITTI depth prediction benchmark. Comparison of our monocular plus stereo approaches to fully supervised methods on the KITTI depth prediction benchmark [27]. D ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Moving objects. Monocular methods can fail to predict depth for objects that were often observed to be in motion dur- ing training e.g. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Overview. (a) Depth network: We use a standard, fully convolutional, U-Net to predict depth. (b) Pose network: Pose between a pair of frames ...

- **Evidence anchors reviewed:** datasets p. 7 (4.2. Additional Datasets), p. 7 (4.2. Additional Datasets), p. 5 (4. Experiments), p. 5 (4. Experiments), metrics p. 5 (4. Experiments), p. 12 (Figure/Table caption), p. 4 (Figure/Table caption), p. 14 (Figure/Table caption), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 17 (Figure/Table caption), p. 7 (Figure/Table caption), p. 13 (Figure/Table caption), p. 5 (4. Experiments), p. 14 (Figure/Table caption), p. 18 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 5 (4. Experiments), p. 14 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption), p. 5 (4.1. KITTI Eigen Split).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
