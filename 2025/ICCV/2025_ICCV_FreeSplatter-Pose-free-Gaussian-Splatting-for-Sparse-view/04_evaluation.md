# Evaluation - FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Xu_FreeSplatter_Pose-free_Gaussian_Splatting_for_Sparse-view_3D_Reconstruction_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Xu_FreeSplatter_Pose-free_Gaussian_Splatting_for_Sparse-view_3D_Reconstruction_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 5 (4. Experiments), p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption)): Table 5. Ablation Study on Model Architecture. The results are evaluated on the GSO dataset with FreeSplatter-O. uate pose estimation performance using both rotation and translation metrics: relative rotation error ...

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Settings - extractive body cue:** FreeSplatterS leverages a diverse training set comprising BlendedMVS [61], ScanNet++[62], and CO3Dv2[37]-a subset of DUSt3R's [51] training data encompassing outdoor scenes, indoor environments, and real-world ...
- **p. 5 / 4. Experiments - extractive body cue:** We evaluate our method on both sparse-view reconstruction (Section 4.2) and camera pose estimation (Section 4.3) tasks, including object-centric and scene-level scenarios.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** Scene-level performance is assessed on the test splits of ScanNet++[62] and CO3Dv2 [37].
- **p. 6 / 4.2. Sparse-view Reconstruction - extractive body cue:** Prior pose-free object reconstruction approaches like LEAP [26] exhibits limited generalization due to its small-scale training, while PF-LRM [49] is highly relevant and serves as ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Ablation Study on Model Architecture. The results are evaluated on the GSO dataset with FreeSplatter-O. uate pose estimation performance using both rotation and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Camera Pose Estimation on PF-LRM's Eval Data. scene-level reconstruction with real-world imagery, com- plete pixel alignment is necessary to handle complex back- grounds. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 6. Ablation Study on Pixel-alignment Loss. The results on GSO and ScanNet++ are evaluated with FreeSplatter-O and FreeSplatter-S, respectively. Number of Input Views. We ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. FreeSplatter reconstructs high-fidelity 3D Gaussians and estimates accurate camera poses from uncalibrated sparse-view images in a feed-forward manner, handling both object-centric (1st row) ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Settings (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5. Ablation Study on Model Architecture. The results are evaluated on the GSO dataset with FreeSplatter-O. uate pose estimation performance using both rotation ... | p. 8 (Figure/Table caption) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Please refer to the supplementary material for additional implementation details and experimental results. | p. 5 (4. Experiments) |
| 4.1. Experimental Settings | EMPIRICAL / REAL-ROBOT OR HARDWARE | Scene-level performance is assessed on the test splits of ScanNet++[62] and CO3Dv2 [37]. | p. 6 (4.1. Experimental Settings) |
| 4.1. Experimental Settings | EMPIRICAL / REAL-ROBOT OR HARDWARE | Sparse-view Reconstruction on ScanNet++ (top) and CO3Dv2 (bottom). * indicates that ground truth camera poses are used as input. ference results. | p. 6 (4.1. Experimental Settings) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4. Camera Pose Estimation on Object-centric and Scene- level Datasets. To be noted, Re10K is outside the training dataset. methods (pixelSplat, MVSplat) on ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Settings - extractive body cue:** FreeSplatterS leverages a diverse training set comprising BlendedMVS [61], ScanNet++[62], and CO3Dv2[37]-a subset of DUSt3R's [51] training data encompassing outdoor scenes, indoor environments, and real-world ...
- **p. 5 / 4. Experiments - extractive body cue:** We evaluate our method on both sparse-view reconstruction (Section 4.2) and camera pose estimation (Section 4.3) tasks, including object-centric and scene-level scenarios.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** Scene-level performance is assessed on the test splits of ScanNet++[62] and CO3Dv2 [37].
- **p. 6 / 4.2. Sparse-view Reconstruction - extractive body cue:** Prior pose-free object reconstruction approaches like LEAP [26] exhibits limited generalization due to its small-scale training, while PF-LRM [49] is highly relevant and serves as ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. FreeSplatter reconstructs high-fidelity 3D Gaussians and estimates accurate camera poses from uncalibrated sparse-view images in a feed-forward manner, handling both object-centric (1st row) ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. FreeSplatter Pipeline. Given N uncalibrated input views without any known camera extrinsics or intrinsics, we first patchify each image into tokens and feed ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Sparse-view Reconstruction on PF-LRM's Evaluation Datasets. FreeSplatter-O synthesizes significantly better visual details than PF-LRM. The 1st row is from the GSO dataset, while ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Sparse-view Reconstruction on GSO dataset. * indi- cates that ground truth camera poses are used as input. at other pixels remain unconstrained. Besides, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Sparse-view Reconstruction on PF-LRM's Eval Data.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Camera Pose Estimation on PF-LRM's Eval Data. scene-level reconstruction with real-world imagery, com- plete pixel alignment is necessary to handle complex back- grounds. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Sparse-view Reconstruction on ScanNet++ (top) and CO3Dv2 (bottom). * indicates that ground truth camera poses are used as input. ference results. Scene-level performance ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Sparse-view Reconstruction on Object-centric and Scene-level Datasets. We did not test pixelSplat/MVSplat on CO3Dv2 due to the significant domain gap. * indicates that ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | FreeSplatterS leverages a diverse training set comprising BlendedMVS [61], ScanNet++[62], and CO3Dv2[37]-a subset of DUSt3R's [51] training data encompassing outdoor scenes, indoor environments, and ... | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Settings), p. 5 (4. Experiments) |
| Task/environment | We evaluate our method on both sparse-view reconstruction (Section 4.2) and camera pose estimation (Section 4.3) tasks, including object-centric and scene-level scenarios. | reset, timeout, object/scene variation | p. 5 (4. Experiments), p. 6 (4.1. Experimental Settings) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2. Model Architecture), p. 8 (4.5. Applications in 3D AIGC) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.2. Model Architecture), p. 3 (3. Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 5. Ablation Study on Model Architecture. The results are evaluated on the GSO dataset with FreeSplatter-O. uate pose estimation performance using both rotation ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Scene-level performance is assessed on the test splits of ScanNet++[62] and CO3Dv2 [37]. | definition/direction/unit from same section | p. 6 (4.1. Experimental Settings) |
| Table 2. Camera Pose Estimation on PF-LRM's Eval Data. scene-level reconstruction with real-world imagery, com- plete pixel alignment is necessary to handle complex back- ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 6. Ablation Study on Pixel-alignment Loss. The results on GSO and ScanNet++ are evaluated with FreeSplatter-O and FreeSplatter-S, respectively. Number of Input Views. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 1. FreeSplatter reconstructs high-fidelity 3D Gaussians and estimates accurate camera poses from uncalibrated sparse-view images in a feed-forward manner, handling both object-centric (1st ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. FreeSplatter Pipeline. Given N uncalibrated input views without any known camera extrinsics or intrinsics, we first patchify each image into tokens and ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 4. Sparse-view Reconstruction on GSO dataset. * indi- cates that ground truth camera poses are used as input. at other pixels remain unconstrained. ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 4. Camera Pose Estimation on Object-centric and Scene- level Datasets. To be noted, Re10K is outside the training dataset. methods (pixelSplat, MVSplat) on ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Prior pose-free object reconstruction approaches like LEAP [26] exhibits limited generalization due to its small-scale training, while PF-LRM [49] is highly relevant and serves ... | comparison identity and matched condition | p. 6 (4.2. Sparse-view Reconstruction) |
| In addition, we also use the GSO/OmniObject3D evaluation data provided by PF-LRM for comparison, since we can only access its in25446 | comparison identity and matched condition | p. 5 (4.1. Experimental Settings) |
| Figure 2. FreeSplatter Pipeline. Given N uncalibrated input views without any known camera extrinsics or intrinsics, we first patchify each image into tokens and ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Table 6. Ablation Study on Pixel-alignment Loss. The results on GSO and ScanNet++ are evaluated with FreeSplatter-O and FreeSplatter-S, respectively. Number of Input Views. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 5. Ablation Study on Model Architecture. The results are evaluated on the GSO dataset with FreeSplatter-O. uate pose estimation performance using both rotation ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 2. FreeSplatter Pipeline. Given N uncalibrated input views without any known camera extrinsics or intrinsics, we first patchify each image into tokens and ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Table 6. Ablation Study on Pixel-alignment Loss. The results on GSO and ScanNet++ are evaluated with FreeSplatter-O and FreeSplatter-S, respectively. Number of Input Views. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 5. Ablation Study on Model Architecture. The results are evaluated on the GSO dataset with FreeSplatter-O. uate pose estimation performance using both rotation ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 3. Sparse-view Reconstruction on Object-centric and Scene-level Datasets. We did not test pixelSplat/MVSplat on CO3Dv2 due to the significant domain gap. * indicates ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce FreeSplatter, a feed-forward reconstruction framework that jointly predicts pixel-wise Gaussians from uncalibrated sparse-view images and estimates their camera parameters. | Table 5. Ablation Study on Model Architecture. The results are evaluated on the GSO dataset with FreeSplatter-O. uate pose estimation performance using both rotation ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 5 (4. Experiments), p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | Please refer to the supplementary material for additional implementation details and experimental results. | numeric claim only at cited anchor | p. 5 (4. Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Settings - extractive body cue:** Each 3D asset is normalized to a [-1, 1]3 cube, with 32 randomly sampled views (with diverse camera intrinsics, i.e., focal lengths) and corresponding depth ...
- **p. 5 / 4.1. Experimental Settings - extractive body cue:** For object-level experiments, we utilize Google Scanned Objects (GSO)[13] and OmniObject3D [56] (chosen 300 objects across 30 categories).
- **p. 3 / 3. Method - extractive body cue:** Given N input images {In / n = 1, . . . , N} without known camera parameters, FreeSplatter performs joint scene reconstruction and camera ...
- **p. 3 / 3. Method - extractive body cue:** The pipeline is formulated as: \ mG , \ m P ^ 1 , \ldots , \ m P ^ N , f = \operatorname ...
- **p. 3 / 3.2. Model Architecture - extractive body cue:** For input images {In / n = 1, . . . , N}, the model patchifies them into tokens {en,m / n = 1, . ...
- **p. 3 / 3.2. Model Architecture - extractive body cue:** The model processes N input images  In ∈RH×W ×3 / n = 1, . . . , N

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 3. Sparse-view Reconstruction on PF-LRM's Evaluation Datasets. FreeSplatter-O synthesizes significantly better visual details than PF-LRM. The 1st row is from the GSO dataset, ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Figure 4. Sparse-view Reconstruction on GSO dataset. * indi- cates that ground truth camera poses are used as input. at other pixels remain unconstrained. ... | p. 5 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In our implementation, we set λa = 1.0, λp = 10.0, Tmax = 105. | p. 5 (3.3. Training Details) |
| Please refer to the supplementary material for additional implementation details and experimental results. | p. 5 (4. Experiments) |
| Each token en,m is enhanced with position and view embeddings: \v e ^{n , m} = \ ve ^{n,m} + \ve ^m_{\mathrm {pos}} + ... | p. 3 (3.2. Model Architecture) |
| For input images {In / n = 1, . . . , N}, the model patchifies them into tokens {en,m / n = 1, ... | p. 3 (3.2. Model Architecture) |
| Given the n-th view's Gaussian location map Xn ∈RH×W ×3 (first 3 channels of Gn), corresponding pixel coordinate map Y n ∈RH×W ×2, and ... | p. 4 (3.2. Model Architecture) |
| Due to the lack of code, we benchmark against PF-LRM using their provided evaluation datasets and inference results. | p. 7 (0.027 Method) |
| It is important to note that the TE metric is scaleinvariant: we first compute the relative translations between views for both ground truth and ... | p. 8 (4.3. Camera Pose Estimation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Sparse-view Reconstruction on PF-LRM's Evaluation Datasets. FreeSplatter-O synthesizes significantly better visual details than PF-LRM. The 1st row is from the GSO dataset, while ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Sparse-view Reconstruction on GSO dataset. * indi- cates that ground truth camera poses are used as input. at other pixels remain unconstrained. Besides, ...

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Experimental Settings), p. 5 (4. Experiments), p. 6 (4.1. Experimental Settings), p. 6 (4.2. Sparse-view Reconstruction), metrics p. 8 (Figure/Table caption), p. 6 (4.1. Experimental Settings), p. 5 (Figure/Table caption), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 6 (4.2. Sparse-view Reconstruction), p. 5 (4.1. Experimental Settings), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 5 (4. Experiments), p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
