# Evaluation - EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Main Results), p. 7 (4.3. Main Results), p. 8 (4.4. Experimental Analysis), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption)): As shown in Table 1, the results indicate that our local refinement module outperforms ISO [56].

## Evaluation Body Digest

- **p. 6 / 4.1. EmbodiedOcc-ScanNet Benchmark - extractive PDF cue:** Apart from Occ-ScanNet and EmbodiedOcc-ScanNet datasets in the original scale, we sampled a small set from the EmbodiedOcc-ScanNet dataset as the EmbodiedOccScanNet-mini dataset which comprises ...
- **p. 6 / 4.1. EmbodiedOcc-ScanNet Benchmark - extractive PDF cue:** We sampled from the Occ-ScanNet dataset accordingly and obtained an Occ-ScanNet-mini2 dataset, which comprises 5504/2376 frames in the train/val splits.
- **p. 7 / 4.3. Main Results - extractive PDF cue:** We also implemented several state-of-the-art driving scene methods [11, 13, 46] on this benchmark and our local refinement module outperforms them by a large margin.
- **p. 7 / 4.3. Main Results - extractive PDF cue:** This is because they mainly focus on the coarse layout (e.g., positions of objects) while indoor scenes require modeling of the fine-grained structure (e.g., shapes ...
- **p. 8 / 4.4. Experimental Analysis - extractive PDF cue:** We present in Table 7 a runtime analysis on scene 0687-00 from the EmbodiedOcc-ScanNet dataset.
- **p. 5 / 4.1. EmbodiedOcc-ScanNet Benchmark - extractive PDF cue:** We trained and evaluated our local refinement module on the Occ-ScanNet dataset [56], which provides frames in 60\times 60\times 36 voxel grids (a 4.8m\times 4.8m\times ...
- **p. 8 / 4.4. Experimental Analysis - extractive PDF cue:** We analyze the effect of different Gaussian parameters in Table 6 using the Occ-ScanNet-mini2 and the EmbodiedOcc-ScanNet-mini datasets.
- **p. 5 / 4.1. EmbodiedOcc-ScanNet Benchmark - extractive PDF cue:** We conducted two tasks to evaluate our EmbodiedOcc framework: local occupancy prediction and embodied occupancy prediction.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. EmbodiedOcc-ScanNet Benchmark (p. 5); 4.2. Implementation Details (p. 6); 4.3. Main Results (p. 7); 4.4. Experimental Analysis (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Main Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 1, the results indicate that our local refinement module outperforms ISO [56]. | p. 7 (4.3. Main Results) |
| 4.3. Main Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | We spliced the local occupancy obtained from our local module to serve as the main baseline (referred to as SplicingOcc), as our local module ... | p. 7 (4.3. Main Results) |
| 4.4. Experimental Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our model demonstrates reasonable local perception ability and further achieves good online prediction with the Gaussian memory. | p. 8 (4.4. Experimental Analysis) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 8. Visualization of local occupancy prediction. Occ-ScanNet-mini2 and the EmbodiedOcc-ScanNet-mini datasets. We find that depth information will significantly benefit the local and embodied ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 1. Local Prediction Performance on the Occ-ScanNet dataset. | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. EmbodiedOcc-ScanNet Benchmark - extractive PDF cue:** Apart from Occ-ScanNet and EmbodiedOcc-ScanNet datasets in the original scale, we sampled a small set from the EmbodiedOcc-ScanNet dataset as the EmbodiedOccScanNet-mini dataset which comprises ...
- **p. 6 / 4.1. EmbodiedOcc-ScanNet Benchmark - extractive PDF cue:** We sampled from the Occ-ScanNet dataset accordingly and obtained an Occ-ScanNet-mini2 dataset, which comprises 5504/2376 frames in the train/val splits.
- **p. 7 / 4.3. Main Results - extractive PDF cue:** We also implemented several state-of-the-art driving scene methods [11, 13, 46] on this benchmark and our local refinement module outperforms them by a large margin.
- **p. 7 / 4.3. Main Results - extractive PDF cue:** This is because they mainly focus on the coarse layout (e.g., positions of objects) while indoor scenes require modeling of the fine-grained structure (e.g., shapes ...
- **p. 8 / 4.4. Experimental Analysis - extractive PDF cue:** We present in Table 7 a runtime analysis on scene 0687-00 from the EmbodiedOcc-ScanNet dataset.
- **p. 5 / 4.1. EmbodiedOcc-ScanNet Benchmark - extractive PDF cue:** We trained and evaluated our local refinement module on the Occ-ScanNet dataset [56], which provides frames in 60\times 60\times 36 voxel grids (a 4.8m\times 4.8m\times ...
- **p. 8 / 4.4. Experimental Analysis - extractive PDF cue:** We analyze the effect of different Gaussian parameters in Table 6 using the Occ-ScanNet-mini2 and the EmbodiedOcc-ScanNet-mini datasets.
- **p. 5 / 4.1. EmbodiedOcc-ScanNet Benchmark - extractive PDF cue:** We conducted two tasks to evaluate our EmbodiedOcc framework: local occupancy prediction and embodied occupancy prediction.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Given streaming monocular RGB inputs, our EmbodiedOcc conducts embodied occupancy prediction in an online manner for indoor scenes. Different from existing methods which ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Framework of our EmbodiedOcc for embodied 3D occupancy prediction. We maintain an explicit global memory of 3D Gaussians during the exploration of the ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Motivation of the depth-aware branch. Along a spe- cific ray, Gaussians distributed in front of the true depth point are likely to model ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Illustration of our Gaussian memory. During each update, the Gaussians within the current frustum are taken from the memory. Confidence values of those ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Local Prediction Performance on the Occ-ScanNet dataset.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Embodied Prediction Performance on the EmbodiedOcc-ScanNet dataset.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Look-Back Prediction vs First-Time Prediction. For \ protect \mathrm {K}= k, we simply select 0, 1, ..., \ m athrm {k-1}th frames to ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Performance with different stopping ratios. 50.78 41.45 41.05 40.80 50.15

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Apart from Occ-ScanNet and EmbodiedOcc-ScanNet datasets in the original scale, we sampled a small set from the EmbodiedOcc-ScanNet dataset as the EmbodiedOccScanNet-mini dataset which ... | embodiment, simulator version and control stack | p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark) |
| Task/environment | We sampled from the Occ-ScanNet dataset accordingly and obtained an Occ-ScanNet-mini2 dataset, which comprises 5504/2376 frames in the train/val splits. | reset, timeout, object/scene variation | p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 7 (4.3. Main Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 2 (3.1. Embodied 3D Occupancy Prediction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use mIoU and IoU as the evaluation metrics. | definition/direction/unit from same section | p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark) |
| For embodied occupancy prediction, we calculate the mIoU and IoU using the global occupancy of the current scene. | definition/direction/unit from same section | p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark) |
| The ground truth used here for calculating IoU and mIoU is the union occupancy of the 30 frustums in a global scene. | definition/direction/unit from same section | p. 7 (4.4. Experimental Analysis) |
| Method Gaussian Structure Memory Local Prediction Embodied Prediction IoU mIoU IoU mIoU EmbodiedOcc-Voxel × ✓ ✓ 47.50 38.12 37.53 26.99 EmbodiedOcc w/o memory ✓ ... | definition/direction/unit from same section | p. 7 (4.4. Experimental Analysis) |
| As the Gaussians transition from random to ordered, the occupancy of the current scene becomes more accurate and complete. | definition/direction/unit from same section | p. 8 (4.4. Experimental Analysis) |
| Our model demonstrates reasonable local perception ability and further achieves good online prediction with the Gaussian memory. | definition/direction/unit from same section | p. 8 (4.4. Experimental Analysis) |
| Figure 4. Illustration of our Gaussian memory. During each update, the Gaussians within the current frustum are taken from the memory. Confidence values of ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We also implemented several state-of-the-art driving scene methods [11, 13, 46] on this benchmark and our local refinement module outperforms them by a large ... | comparison identity and matched condition | p. 7 (4.3. Main Results) |
| The visual input at a certain step t during embodied occupancy prediction is still monocular, which is a more challenging setting compared with multi-view ... | comparison identity and matched condition | p. 5 (4.1. EmbodiedOcc-ScanNet Benchmark) |
| As shown in Table 1, the results indicate that our local refinement module outperforms ISO [56]. | comparison identity and matched condition | p. 7 (4.3. Main Results) |
| The results in the third row suggest that the depth-aware branch we employ is more reasonable compared to the naive method of directly initializing ... | comparison identity and matched condition | p. 8 (4.4. Experimental Analysis) |
| As shown in the second row, without the assistance of depth information, the performance of embodied occupancy prediction drops sharply. | comparison identity and matched condition | p. 8 (4.4. Experimental Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Effect of Continuous Online Updating. | component/input/data sensitivity | p. 7 (4.4. Experimental Analysis) |
| We analyze the effect of our depth-aware branch in Table 5 using the 26366 | component/input/data sensitivity | p. 7 (4.4. Experimental Analysis) |
| We analyze the effect of different Gaussian parameters in Table 6 using the Occ-ScanNet-mini2 and the EmbodiedOcc-ScanNet-mini datasets. | component/input/data sensitivity | p. 8 (4.4. Experimental Analysis) |
| Due to space limitations, we will use a more diverse set of samples to further show the visual effect of our EmbodiedOcc in the ... | component/input/data sensitivity | p. 8 (4.4. Experimental Analysis) |
| The depth prediction network used in the depth-aware branch is a fine-tuned DepthAnything-V2 model [51] that remains frozen during the training, and the depth-aware ... | component/input/data sensitivity | p. 6 (4.2. Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Specifically, we propose a structure-aware local refinement module to update the relevant Gaussians within the current frustum. | As shown in Table 1, the results indicate that our local refinement module outperforms ISO [56]. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Main Results), p. 7 (4.3. Main Results), p. 8 (4.4. Experimental Analysis), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Primary metric/result | We spliced the local occupancy obtained from our local module to serve as the main baseline (referred to as SplicingOcc), as our local module ... | numeric claim only at cited anchor | p. 7 (4.3. Main Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. EmbodiedOcc-ScanNet Benchmark - extractive PDF cue:** Our EmbodiedOcc-ScanNet comprises 537/137 scenes in the train/val splits.
- **p. 6 / 4.1. EmbodiedOcc-ScanNet Benchmark - extractive PDF cue:** Apart from Occ-ScanNet and EmbodiedOcc-ScanNet datasets in the original scale, we sampled a small set from the EmbodiedOcc-ScanNet dataset as the EmbodiedOccScanNet-mini dataset which comprises ...
- **p. 6 / 4.1. EmbodiedOcc-ScanNet Benchmark - extractive PDF cue:** We sampled from the Occ-ScanNet dataset accordingly and obtained an Occ-ScanNet-mini2 dataset, which comprises 5504/2376 frames in the train/val splits.
- **p. 6 / 4.1. EmbodiedOcc-ScanNet Benchmark - extractive PDF cue:** It is worth mentioning that the global occupancy used here is the union of the frustums corresponding to 30 frames of each scene, which represents ...
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** We train our local refinement module for 10 epochs using 8 NVIDIA GeForce RTX 4090 GPUs on the Occ-ScanNet dataset and 20 epochs on the ...
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** We train our EmbodiedOcc for 5 epochs using 8 NVIDIA GeForce RTX 4090 GPUs on the EmbodiedOcc-ScanNet dataset and 20 epochs using 4 NVIDIA GeForce ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Due to space limitations, we will use a more diverse set of samples to further show the visual effect of our EmbodiedOcc in the ... | p. 8 (4.4. Experimental Analysis) |
| body limitation/failure cue | Besides, we replaced DepthAnything-V2 with IndoorDepth [6] in the last row to prove that our depth-aware branch does not rely on a specific depth ... | p. 8 (4.4. Experimental Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The maximum value of the learning rate is set to 2e-4 using 8 GPUs and 1e-4 using 4 GPUs. | p. 6 (4.2. Implementation Details) |
| The learning rate warms up in the first 1000 iterations to a maximum value of 2e-4 and decreases according to a cosine schedule [25]. | p. 6 (4.2. Implementation Details) |
| 6.626 Occ head 39.635 Frame level (ms) Load memory 0.973 Depth aware 1.816 Img backbone 61.478 GS Encoder 14.761 Depthanything 34.687 Update memory 0.474 ... | p. 7 (4.4. Experimental Analysis) |
| We present in Table 7 a runtime analysis on scene 0687-00 from the EmbodiedOcc-ScanNet dataset. | p. 8 (4.4. Experimental Analysis) |
| The runtime decomposition details show that our method is efficient while the main bottleneck is the image and depth backbones, suggesting that the overall ... | p. 8 (4.4. Experimental Analysis) |
| Depth Aware Predicted Depth Map … … Input T-1 Input T … … … … Gaussian Memory T Gaussian Memory T-1 Occupancy T Occupancy ... | p. 3 (3.1. Embodied 3D Occupancy Prediction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.4. Experimental Analysis - extractive PDF cue:** Due to space limitations, we will use a more diverse set of samples to further show the visual effect of our EmbodiedOcc in the supplementary ...
- **p. 8 / 4.4. Experimental Analysis - extractive PDF cue:** Besides, we replaced DepthAnything-V2 with IndoorDepth [6] in the last row to prove that our depth-aware branch does not rely on a specific depth prediction ...

- **PDF anchors reviewed:** datasets p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 7 (4.3. Main Results), p. 7 (4.3. Main Results), p. 8 (4.4. Experimental Analysis), p. 5 (4.1. EmbodiedOcc-ScanNet Benchmark), metrics p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 7 (4.4. Experimental Analysis), p. 7 (4.4. Experimental Analysis), p. 8 (4.4. Experimental Analysis), p. 8 (4.4. Experimental Analysis), baselines p. 7 (4.3. Main Results), p. 5 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 7 (4.3. Main Results), p. 8 (4.4. Experimental Analysis), p. 8 (4.4. Experimental Analysis), results p. 7 (4.3. Main Results), p. 7 (4.3. Main Results), p. 8 (4.4. Experimental Analysis), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
