# Evaluation - SPARS3R: Semantic Prior Alignment and Regularization for Sparse 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Tang_SPARS3R_Semantic_Prior_Alignment_and_Regularization_for_Sparse_3D_Reconstruction_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_SPARS3R_Semantic_Prior_Alignment_and_Regularization_for_Sparse_3D_Reconstruction_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.1. Sparse NVS Evaluation), p. 6 (4.2. Ablation Studies), p. 5 (4.1. Sparse NVS Evaluation), p. 6 (4.2. Ablation Studies), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption)): 1, these two improvements enhance camera alignment accuracy in both rotation and translation.

## Evaluation Body Digest

- **p. 7 / 4.3. Quantitative and Visual Evaluation - extractive body cue:** Quantitative comparison of different NVS methods on 12 views on three popular benchmark datasets, totaling 24 scenes.
- **p. 5 / 4. Experiments - extractive body cue:** MVImgNet [60] is an object-centric dataset that consists of 7 scenes.
- **p. 5 / 4. Experiments - extractive body cue:** For this dataset, we follow the test set outlined in MipNeRF360 [2] and uniformly sample 12 images from the original training set to construct a ...
- **p. 6 / 4.2. Ablation Studies - extractive body cue:** For scenes that do not have significant depth discrepancies, Global Fusion Alignment works well.
- **p. 6 / 4.2. Ablation Studies - extractive body cue:** Quantitative evaluation of pose accuracy across three datasets, Relative Translation Error (RPEt) and Relative Rotation Error (RPEr) [62] are calculated based on the normalized poses.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. SPARS3R combines a prior dense point cloud χ and a sparse SfM point cloud sX. The prior χ often has inferior depth accuracy ...
- **p. 6 / 4.2. Ablation Studies - extractive body cue:** While it brings down the errors in some cases, such training pose optimization strategy does not work as well in more challenging datasets like Mip-NeRF ...
- **p. 5 / 4.1. Sparse NVS Evaluation - extractive body cue:** Beyond accurate camera pose alignment, test pose optimization can also be applied between rendered and ground-truth images to minimize the pose error; however, such process ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Sparse NVS Evaluation (p. 5); 4.3. Quantitative and Visual Evaluation (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Sparse NVS Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, these two improvements enhance camera alignment accuracy in both rotation and translation. | p. 5 (4.1. Sparse NVS Evaluation) |
| 4.2. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | InstantSplat [14] uses DUSt3R's [52] dense point cloud and pose estimation and attempts to improve accuracy through a training pose optimization approach similar to ... | p. 6 (4.2. Ablation Studies) |
| 4.1. Sparse NVS Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Improvements over Procrustes Alignment baseline in average rotation error ER and translation error ET . | p. 5 (4.1. Sparse NVS Evaluation) |
| 4.2. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | Quantitatively, we observe a 1.4 dB improvement on the Bonsai scene. | p. 6 (4.2. Ablation Studies) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2. SPARS3R combines a prior dense point cloud χ and a sparse SfM point cloud sX. The prior χ often has inferior depth ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4.3. Quantitative and Visual Evaluation - extractive body cue:** Quantitative comparison of different NVS methods on 12 views on three popular benchmark datasets, totaling 24 scenes.
- **p. 5 / 4. Experiments - extractive body cue:** MVImgNet [60] is an object-centric dataset that consists of 7 scenes.
- **p. 5 / 4. Experiments - extractive body cue:** For this dataset, we follow the test set outlined in MipNeRF360 [2] and uniformly sample 12 images from the original training set to construct a ...
- **p. 6 / 4.2. Ablation Studies - extractive body cue:** For scenes that do not have significant depth discrepancies, Global Fusion Alignment works well.
- **p. 6 / 4.2. Ablation Studies - extractive body cue:** Quantitative evaluation of pose accuracy across three datasets, Relative Translation Error (RPEt) and Relative Rotation Error (RPEr) [62] are calculated based on the normalized poses.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. A visualization of SPARS3R in comparison to cur- rent SoTA. Without additional prior, sparse NVS leads to incor- rect geometry by Instant-NGP [36]. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. SPARS3R combines a prior dense point cloud χ and a sparse SfM point cloud sX. The prior χ often has inferior depth accuracy ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Improvements over Procrustes Alignment baseline in av- erage rotation error ER and translation error ET . Incorporating rotation points further minimizes the overall ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Ablation on key components of SPARS3R. The results are shown using PSNR, SSIM, LPIPS and DSIM based on the Mip- NeRF 360 [2]. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Visual comparison of SPARS3R with and without SOA. While the dense bonsai in the foreground is aligned with the sparse point cloud, depth ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Quantitative evaluation of pose accuracy across three datasets, Relative Translation Error (RPEt) and Relative Rotation Error (RPEr) [62] are calculated based on the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Quantitative comparison of different NVS methods on 12 views on three popular benchmark datasets, totaling 24 scenes. All methods are run on the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Quantitative comparison of 3 and 6 views on Tanks & Temples and MVImgNet datasets. implicit and explicit scene representations. Specifically, 3DGS leverages SfM ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Quantitative comparison of different NVS methods on 12 views on three popular benchmark datasets, totaling 24 scenes. | embodiment, simulator version and control stack | p. 7 (4.3. Quantitative and Visual Evaluation), p. 5 (4. Experiments) |
| Task/environment | MVImgNet [60] is an object-centric dataset that consists of 7 scenes. | reset, timeout, object/scene variation | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Preliminary), p. 2 (3.1. Preliminary) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. Preliminary), p. 4 (3.2.2. Semantic Outlier Alignment) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Quantitative evaluation of pose accuracy across three datasets, Relative Translation Error (RPEt) and Relative Rotation Error (RPEr) [62] are calculated based on the normalized ... | definition/direction/unit from same section | p. 6 (4.2. Ablation Studies) |
| Figure 2. SPARS3R combines a prior dense point cloud χ and a sparse SfM point cloud sX. The prior χ often has inferior depth ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| While it brings down the errors in some cases, such training pose optimization strategy does not work as well in more challenging datasets like ... | definition/direction/unit from same section | p. 6 (4.2. Ablation Studies) |
| Beyond accurate camera pose alignment, test pose optimization can also be applied between rendered and ground-truth images to minimize the pose error; however, such ... | definition/direction/unit from same section | p. 5 (4.1. Sparse NVS Evaluation) |
| Incorporating rotation points further minimizes the overall error. | definition/direction/unit from same section | p. 5 (4.1. Sparse NVS Evaluation) |
| Figure 4. Visual comparisons of different NVS methods on 12 views on Mip-NeRF 360 [2] dataset. Zooming in on the visualizations is recommended to ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 4. Visual comparisons of different NVS methods on 12 views on Mip-NeRF 360 [2] dataset. Zooming in on the visualizations is recommended to ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| For fair implementation and comparison, we employ test pose optimization for all baselines and SPARS3R for 500 steps to maximally remove the effect of ... | comparison identity and matched condition | p. 6 (4.1. Sparse NVS Evaluation) |
| Improvements over Procrustes Alignment baseline in average rotation error ER and translation error ET . | comparison identity and matched condition | p. 5 (4.1. Sparse NVS Evaluation) |
| All baselines are run until convergence. | comparison identity and matched condition | p. 6 (4.1. Sparse NVS Evaluation) |
| Figure 1. A visualization of SPARS3R in comparison to cur- rent SoTA. Without additional prior, sparse NVS leads to incor- rect geometry by Instant-NGP ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Figure 2. SPARS3R combines a prior dense point cloud χ and a sparse SfM point cloud sX. The prior χ often has inferior depth ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For fair implementation and comparison, we employ test pose optimization for all baselines and SPARS3R for 500 steps to maximally remove the effect of ... | component/input/data sensitivity | p. 6 (4.1. Sparse NVS Evaluation) |
| Ablation on key components of SPARS3R. | component/input/data sensitivity | p. 6 (4.2. Ablation Studies) |
| Figure 1. A visualization of SPARS3R in comparison to cur- rent SoTA. Without additional prior, sparse NVS leads to incor- rect geometry by Instant-NGP ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method, SPARS3R, can reliably render details in the foreground and background with accurate poses. | 1, these two improvements enhance camera alignment accuracy in both rotation and translation. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.1. Sparse NVS Evaluation), p. 6 (4.2. Ablation Studies), p. 5 (4.1. Sparse NVS Evaluation), p. 6 (4.2. Ablation Studies), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | InstantSplat [14] uses DUSt3R's [52] dense point cloud and pose estimation and attempts to improve accuracy through a training pose optimization approach similar to ... | numeric claim only at cited anchor | p. 6 (4.2. Ablation Studies) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experiments - extractive body cue:** Tanks and Temples [27] contains 8 scenes captured in video format.
- **p. 5 / 4. Experiments - extractive body cue:** MVImgNet [60] is an object-centric dataset that consists of 7 scenes.
- **p. 5 / 4. Experiments - extractive body cue:** Mip-NeRF 360 [2] comprises of 9 scenes with 360° views and greater pose variation between the scenes, including diverse heights and distances.
- **p. 6 / 4.1. Sparse NVS Evaluation - extractive body cue:** For fair implementation and comparison, we employ test pose optimization for all baselines and SPARS3R for 500 steps to maximally remove the effect of shifted ...
- **p. 7 / 4.3. Quantitative and Visual Evaluation - extractive body cue:** Quantitative comparison of different NVS methods on 12 views on three popular benchmark datasets, totaling 24 scenes.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While SPARS3R significantly improves upon previous SoTA, there are also several limitations worth noting. | p. 8 (4.4. Limitations) |
| body limitation/failure cue | We also introduce several improvements in the evaluation process to better represent the practical limitations in sparse-view registration and reconstruction. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Since sparse-view registration can be unstable due to limited pairs, we perform multiple SfMs and pick the outcome that maximizes successful triangulation per image. | p. 5 (4. Experiments) |
| body limitation/failure cue | While it brings down the errors in some cases, such training pose optimization strategy does not work as well in more challenging datasets like ... | p. 6 (4.2. Ablation Studies) |
| body limitation/failure cue | Table 5. Quantitative comparison of 3 and 6 views on Tanks & Temples and MVImgNet datasets. implicit and explicit scene representations. Specifically, 3DGS leverages ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Notably, it provides a robust assessment of rendering image quality under moderate pose shift, which frequently occurs in the realistic sparse-view 26814 | p. 5 (4.1. Sparse NVS Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For fair implementation and comparison, we employ test pose optimization for all baselines and SPARS3R for 500 steps to maximally remove the effect of ... | p. 6 (4.1. Sparse NVS Evaluation) |
| All baselines are run until convergence. | p. 6 (4.1. Sparse NVS Evaluation) |
| All methods are run on the same registrations and updated with test pose optimization. | p. 7 (4.3. Quantitative and Visual Evaluation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.4. Limitations - extractive body cue:** While SPARS3R significantly improves upon previous SoTA, there are also several limitations worth noting.
- **p. 8 / 5. Conclusion - extractive body cue:** We also introduce several improvements in the evaluation process to better represent the practical limitations in sparse-view registration and reconstruction.
- **p. 5 / 4. Experiments - extractive body cue:** Since sparse-view registration can be unstable due to limited pairs, we perform multiple SfMs and pick the outcome that maximizes successful triangulation per image.
- **p. 6 / 4.2. Ablation Studies - extractive body cue:** While it brings down the errors in some cases, such training pose optimization strategy does not work as well in more challenging datasets like Mip-NeRF ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Quantitative comparison of 3 and 6 views on Tanks & Temples and MVImgNet datasets. implicit and explicit scene representations. Specifically, 3DGS leverages SfM ...
- **p. 5 / 4.1. Sparse NVS Evaluation - extractive body cue:** Notably, it provides a robust assessment of rendering image quality under moderate pose shift, which frequently occurs in the realistic sparse-view 26814

- **Evidence anchors reviewed:** datasets p. 7 (4.3. Quantitative and Visual Evaluation), p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4.2. Ablation Studies), p. 6 (4.2. Ablation Studies), metrics p. 6 (4.2. Ablation Studies), p. 3 (Figure/Table caption), p. 6 (4.2. Ablation Studies), p. 5 (4.1. Sparse NVS Evaluation), p. 5 (4.1. Sparse NVS Evaluation), p. 8 (Figure/Table caption), baselines p. 8 (Figure/Table caption), p. 6 (4.1. Sparse NVS Evaluation), p. 5 (4.1. Sparse NVS Evaluation), p. 6 (4.1. Sparse NVS Evaluation), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), results p. 5 (4.1. Sparse NVS Evaluation), p. 6 (4.2. Ablation Studies), p. 5 (4.1. Sparse NVS Evaluation), p. 6 (4.2. Ablation Studies), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
