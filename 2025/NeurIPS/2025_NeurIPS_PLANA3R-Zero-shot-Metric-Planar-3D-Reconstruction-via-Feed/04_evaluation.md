# Evaluation - PLANA3R: Zero-shot Metric Planar 3D Reconstruction via Feed-forward Planar Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=YTwRZP8mNO; PDF retrieval source: https://arxiv.org/pdf/2510.18714. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 Experiment), p. 7 (4 Experiment), p. 9 (4 Experiment), p. 14 (A.1 Extra Results), p. 14 (A.1 Extra Results), p. 16 (Figure/Table caption)): 1, both MASt3R and our PLANA3R significantly outperform prior learning-based planar reconstruction methods [28, 11, 1] in terms of pose estimation accuracy.

## Evaluation Body Digest

- **p. 6 / 4 Experiment - extractive body cue:** 4.2 Datasets Since PLANA3R targets structured indoor scenes, we train it on a combination of four public indoorscene datasets: ScanNetV2 [4], ScanNet++ [39], ARKitScenes [5], ...
- **p. 7 / 4 Experiment - extractive body cue:** Since our PLANA3R has never seen the scenes of NYUv2 during training, this dataset can well demonstrate the generalization ability of our model for out-of-domain ...
- **p. 8 / 4 Experiment - extractive body cue:** We present more visualization results in the supplementary materials and conduct tests on the 7-Scenes [25] dataset.
- **p. 7 / 4 Experiment - extractive body cue:** For ScanNetV2, we follow the training and testing splits defined by NOPE-SAC [28], evaluating 4051 image pairs from 303 scenes.
- **p. 8 / 4 Experiment - extractive body cue:** Following PlaneRCNN [16], we generate 3D plane GT labels on the Replica dataset [26] by first fitting planes to the GT mesh using RANSAC [8], ...
- **p. 6 / 4 Experiment - extractive body cue:** Among these test sets, except for ScanNetV2, the remaining three datasets demonstrate the generalization capability of our model across different datasets.
- **p. 14 / A.1 Extra Results - extractive body cue:** Although the 7-Scenes dataset is a widely used indoor dataset and is very suitable for out-of-domain evaluation, it does not provide official plane segmentation masks.
- **p. 14 / A.1 Extra Results - extractive body cue:** To further demonstrate the zeroshot generalization capability of our method in out-of-domain scenes, we evaluate single-view reconstruction and planar segmentation on the 7-Scenes dataset [25].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiment (p. 6); A.1 Extra Results (p. 14); A.2 Implementation Details (p. 14).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, both MASt3R and our PLANA3R significantly outperform prior learning-based planar reconstruction methods [28, 11, 1] in terms of pose estimation accuracy. | p. 7 (4 Experiment) |
| 4 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, PLANA3R achieves SOTA performance on ScanNetV2. | p. 7 (4 Experiment) |
| 4 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | 5, using approximately half the number of high-resolution primitives achieves performance comparable to using the full high-resolution set. | p. 9 (4 Experiment) |
| A.1 Extra Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 8 to show that PLANA3R achieves much better performance than NOPE-SAC. | p. 14 (A.1 Extra Results) |
| A.1 Extra Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 7, our method achieves much better planar segmentation and reconstruction performance than PlaneRecTR. | p. 14 (A.1 Extra Results) |

## Dataset / Benchmark Role

- **p. 6 / 4 Experiment - extractive body cue:** 4.2 Datasets Since PLANA3R targets structured indoor scenes, we train it on a combination of four public indoorscene datasets: ScanNetV2 [4], ScanNet++ [39], ARKitScenes [5], ...
- **p. 7 / 4 Experiment - extractive body cue:** Since our PLANA3R has never seen the scenes of NYUv2 during training, this dataset can well demonstrate the generalization ability of our model for out-of-domain ...
- **p. 8 / 4 Experiment - extractive body cue:** We present more visualization results in the supplementary materials and conduct tests on the 7-Scenes [25] dataset.
- **p. 7 / 4 Experiment - extractive body cue:** For ScanNetV2, we follow the training and testing splits defined by NOPE-SAC [28], evaluating 4051 image pairs from 303 scenes.
- **p. 8 / 4 Experiment - extractive body cue:** Following PlaneRCNN [16], we generate 3D plane GT labels on the Replica dataset [26] by first fitting planes to the GT mesh using RANSAC [8], ...
- **p. 6 / 4 Experiment - extractive body cue:** Among these test sets, except for ScanNetV2, the remaining three datasets demonstrate the generalization capability of our model across different datasets.
- **p. 14 / A.1 Extra Results - extractive body cue:** Although the 7-Scenes dataset is a widely used indoor dataset and is very suitable for out-of-domain evaluation, it does not provide official plane segmentation masks.
- **p. 14 / A.1 Extra Results - extractive body cue:** To further demonstrate the zeroshot generalization capability of our method in out-of-domain scenes, we evaluate single-view reconstruction and planar segmentation on the 7-Scenes dataset [25].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Our proposed PLANA3R learns to predict planar 3D primitives and metric-scale relative poses, providing a compact 3D representation of two-view input images with ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of our PLANA3R. Given two images captured from the same scene, PLANA3R outputs a set of 3D planar primitives and 6-DoF relative ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Comparisons of two-view 3D planar reconstruction on the ScanNetV2 [4] (the first row) and the Matterport3D [2] (the last two rows) datasets. 4.3.2 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Quantitative comparison of two-view planar reconstruction and relative camera pose estimation. The best results are in bold.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Quantitative comparison of metric monocular depth estimation on the NYUv2 dataset. The best results are in bold.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Quantitative comparison of single-view planar reconstruction on the Replica dataset [26]. The best results are in bold.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Comparisons of single-view plane segmentation and 3D reconstruction on the Replica [26]. Input Image 1 Input Image 2 NOPE-SAC Ours Ground Truth
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Comparisons of two-view 3D plane segmentation on the Matterport3D [2] (the first two rows) and the ScanNetV2 [4] (the last row) datasets. 4.4 ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.2 Datasets Since PLANA3R targets structured indoor scenes, we train it on a combination of four public indoorscene datasets: ScanNetV2 [4], ScanNet++ [39], ARKitScenes ... | embodiment, simulator version and control stack | p. 6 (4 Experiment), p. 7 (4 Experiment) |
| Task/environment | Since our PLANA3R has never seen the scenes of NYUv2 during training, this dataset can well demonstrate the generalization ability of our model for ... | reset, timeout, object/scene variation | p. 7 (4 Experiment), p. 8 (4 Experiment) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3 Method), p. 4 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3 Method), p. 5 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Pose accuracy is measured by the metric translation error (in meters) and rotation error (in degrees). | definition/direction/unit from same section | p. 7 (4 Experiment) |
| demonstrate our method's superior performance in both geometric accuracy (metric 3D reconstruction, depth estimation, and two-view relative pose estimation) and semantic understanding (plane segmentation). | definition/direction/unit from same section | p. 7 (4 Experiment) |
| Method PlaneNet [15] PlaneAE [40] PlaneRCNN [16] PlaneTR [27] PlaneRecTR [24] MASt3R [14] Ours Rel ↓ 0.239 0.205 0.183 0.195 0.157 0.152 0.132 log10 ... | definition/direction/unit from same section | p. 8 (4 Experiment) |
| Method Translation (m) Rotation (◦) Chamfer↓ F-score↑ Med. | definition/direction/unit from same section | p. 8 (4 Experiment) |
| In contrast, relying solely on low-resolution primitives results in a significant drop in accuracy. | definition/direction/unit from same section | p. 9 (4 Experiment) |
| ScanNetV2 Reconstruction NYUv2 Depth Estimation Metrics Chamfer↓ F-score↑ Avg. # primitives RMSE↓ δ1↑ Avg. # primitives Ours (0) 0.10 93.10 3072 0.45 86.8 3072 ... | definition/direction/unit from same section | p. 10 (4 Experiment) |
| Table 5: Ablation study on the gradient threshold (gth). We show the relationship between the number of per-view primitives and performance. ScanNetV2 Reconstruction NYUv2 ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Figure 9: Supplement comparisons of two-view 3D plane reconstruction on the ScanNetV2 [4] (the first two rows) and Matterport3D [2] (the last three rows). ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 4.3 Baselines and Evaluation Metrics We evaluate our PLANA3R against state-of-the-art (SOTA) planar reconstruction methods across multiple tasks, including 3D reconstruction, pose estimation, depth ... | comparison identity and matched condition | p. 6 (4 Experiment) |
| For a fair comparison, we employed MASt3R also in a pairwise manner as the baseline. | comparison identity and matched condition | p. 9 (4 Experiment) |
| 1, both MASt3R and our PLANA3R significantly outperform prior learning-based planar reconstruction methods [28, 11, 1] in terms of pose estimation accuracy. | comparison identity and matched condition | p. 7 (4 Experiment) |
| Remarkably, despite never being trained on Matterport3D, PLANA3R outperforms prior planar reconstruction methods [11, 24, 28] that were specifically trained on this dataset, highlighting ... | comparison identity and matched condition | p. 7 (4 Experiment) |
| Here, we show that PLANA3R can perform zero-shot plane-level semantic segmentation without plane annotations. | comparison identity and matched condition | p. 8 (4 Experiment) |
| Input Image 1 Input Image 2 NOPE-SAC Ours Ground Truth Figure 5: Comparisons of two-view 3D plane segmentation on the Matterport3D [2] (the first ... | comparison identity and matched condition | p. 9 (4 Experiment) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Here, we show that PLANA3R can perform zero-shot plane-level semantic segmentation without plane annotations. | component/input/data sensitivity | p. 8 (4 Experiment) |
| Table 5: Ablation study on the gradient threshold (gth). We show the relationship between the number of per-view primitives and performance. ScanNetV2 Reconstruction NYUv2 ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| Data means training without 0.57M nonoverlapping image pairs). | component/input/data sensitivity | p. 14 (A.2 Implementation Details) |
| We also conduct an additional ablation study to evaluate the impact of incorporating the 0.57M non-overlapping image pairs on model performance during training. | component/input/data sensitivity | p. 15 (A.2 Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these challenges and facilitate training, we introduce a patch loss designed to stabilize primitive positioning and orientation: Lpatch ∗ = α1 | 1, both MASt3R and our PLANA3R significantly outperform prior learning-based planar reconstruction methods [28, 11, 1] in terms of pose estimation accuracy. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 Experiment), p. 7 (4 Experiment), p. 9 (4 Experiment), p. 14 (A.1 Extra Results), p. 14 (A.1 Extra Results), p. 16 (Figure/Table caption) |
| Primary metric/result | 1, PLANA3R achieves SOTA performance on ScanNetV2. | numeric claim only at cited anchor | p. 7 (4 Experiment) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiment - extractive body cue:** The model is trained for a total of 256 GPU-days on NVIDIA H20 GPUs, with a per-GPU batch size of 6.
- **p. 6 / 4 Experiment - extractive body cue:** (5), followed by 10 epochs incorporating all three losses at an input resolution of 512 × 384.
- **p. 6 / 4 Experiment - extractive body cue:** We also evaluate on 7Scenes [25] in Sec.
- **p. 7 / 4 Experiment - extractive body cue:** For ScanNetV2, we follow the training and testing splits defined by NOPE-SAC [28], evaluating 4051 image pairs from 303 scenes.
- **p. 9 / 4 Experiment - extractive body cue:** To evaluate this capability, we tested PLANA3R on 50 eight-view samples, sampled every 20 frames from the ScanNetV2 dataset.
- **p. 10 / 4 Experiment - extractive body cue:** We show the input 8 frames and planar 3D reconstruction.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While this represents a limitation in our current analysis, it also highlights the urgent need for better benchmarks in this field. | p. 18 (A.5 Limitations) |
| body limitation/failure cue | Figure 2: Overview of our PLANA3R. Given two images captured from the same scene, PLANA3R outputs a set of 3D planar primitives and 6-DoF ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | This process does not require merging the primitives and can be performed with a single feed-forward pass. | p. 7 (4 Experiment) |
| body limitation/failure cue | 4.4 Multi-view Reconstruction with More Than Two Views PLANA3R currently supports multi-view reconstruction in a pairwise manner, but does not support a single forward ... | p. 9 (4 Experiment) |
| body limitation/failure cue | Although the 7-Scenes dataset is a widely used indoor dataset and is very suitable for out-of-domain evaluation, it does not provide official plane segmentation ... | p. 14 (A.1 Extra Results) |
| body limitation/failure cue | Furthermore, we observe that as the overlap ratio in the test set decreases, the model's accuracy consistently degrades. | p. 16 (A.2 Implementation Details) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The model is trained for a total of 256 GPU-days on NVIDIA H20 GPUs, with a per-GPU batch size of 6. | p. 6 (4 Experiment) |
| 4.1 Implementation Details We initialize the ViT encoder and the transformer decoder's part of PLANA3R model with DUSt3R's pre-trained 512-DPT weights. | p. 6 (4 Experiment) |
| Datasets Type N Pairs ScanNetV2 [4] Indoor/Real 610K ScanNet++ [39] Indoor/Real 810K ARKitScenes [5] Indoor/Real 2400K Habitat [23] Indoor/Synthetic 120k Hyperparameters. | p. 17 (A.2 Implementation Details) |
| We evaluate the inference runtime of our PLANA3R using an NVIDIA RTX 3090 GPU. | p. 18 (A.3 Runtime Analysis) |
| Input images {Ii}i=1,2 are first encoded in a Siamese fashion using a ViT encoder [7], producing feature maps {F i}i=1,2 ∈R H 16 × ... | p. 4 (3 Method) |
| Instead, it employs a deconvolution network to predict primitives at two distinct resolutions, based on the patch divisions from the ViT encoder. | p. 4 (3 Method) |
| We compute the gradient magnitude for each pixel in the low-resolution predicted normal patches Npatch low of size H 16 × W 16 , ... | p. 5 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 18 / A.5 Limitations - extractive body cue:** While this represents a limitation in our current analysis, it also highlights the urgent need for better benchmarks in this field.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of our PLANA3R. Given two images captured from the same scene, PLANA3R outputs a set of 3D planar primitives and 6-DoF relative ...
- **p. 7 / 4 Experiment - extractive body cue:** This process does not require merging the primitives and can be performed with a single feed-forward pass.
- **p. 9 / 4 Experiment - extractive body cue:** 4.4 Multi-view Reconstruction with More Than Two Views PLANA3R currently supports multi-view reconstruction in a pairwise manner, but does not support a single forward pass ...
- **p. 14 / A.1 Extra Results - extractive body cue:** Although the 7-Scenes dataset is a widely used indoor dataset and is very suitable for out-of-domain evaluation, it does not provide official plane segmentation masks.
- **p. 16 / A.2 Implementation Details - extractive body cue:** Furthermore, we observe that as the overlap ratio in the test set decreases, the model's accuracy consistently degrades.

- **Evidence anchors reviewed:** datasets p. 6 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 6 (4 Experiment), metrics p. 7 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 8 (4 Experiment), p. 9 (4 Experiment), p. 10 (4 Experiment), baselines p. 6 (4 Experiment), p. 9 (4 Experiment), p. 7 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 9 (4 Experiment), results p. 7 (4 Experiment), p. 7 (4 Experiment), p. 9 (4 Experiment), p. 14 (A.1 Extra Results), p. 14 (A.1 Extra Results), p. 16 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
