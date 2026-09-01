# Evaluation - SpatialSplat: Efficient Semantic 3D from Sparse Unposed Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Experimental Setup), p. 6 (4.2. Results and Analysis), p. 7 (4.2. Results and Analysis), p. 7 (4.2. Results and Analysis), p. 8 (4.3. Ablations and Analysis), p. 8 (4.3. Ablations and Analysis)): In challenging cases where LSM fails, such as the table legs in the first two rows and the corners in the last two rows, our method achieves significantly better results.

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** We filter out bad scenes and those with incomplete extrinsic parameters, resulting in a training dataset of approximately 1,500 scenes.
- **p. 8 / 25.58 MB - extractive PDF cue:** Notably, since Replica is a synthetic dataset with a different data modality from our training set, this underscores the strong generalization ability of our approach.
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** For evaluation, we follow LSM and select 40 unseen scenes from ScanNet to assess our model's performance.
- **p. 8 / 25.58 MB - extractive PDF cue:** Model efficiency comparison. "-Lite": the model replaces LSeg with CLIP ViT-B/16. unseen Replica dataset in both novel view synthesis and open-vocabulary segmentation.
- **p. 6 / 4.2. Results and Analysis - extractive PDF cue:** We observe that LSM struggles in certain scenes due to its reliance on accurate depth for aligning views during training as shown in Fig.
- **p. 7 / 4.2. Results and Analysis - extractive PDF cue:** Results of Cross-Dataset Generalization.
- **p. 7 / 4.2. Results and Analysis - extractive PDF cue:** Following LSM's approach, we map category labels from the Scannet dataset into common categories: Wall, Floor, Ceiling, Chair, Table, Bed, Sofa, Others.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** SpatialSplat generalizes well on OOD data. and NeRF-DFF [23], pre-scene optimization methods for semantic 3D reconstruction based on 3DGS [19] and NeRF [29], respectively.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiment (p. 5); 4.1. Experimental Setup (p. 5); 4.2. Results and Analysis (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Experimental Setup | EMPIRICAL / SOURCE-REPORTED EVALUATION | In challenging cases where LSM fails, such as the table legs in the first two rows and the corners in the last two rows, ... | p. 6 (4.1. Experimental Setup) |
| 4.2. Results and Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, SpatialSplat significantly outperforms latest SOTA method LSM. | p. 6 (4.2. Results and Analysis) |
| 4.2. Results and Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | SpatialSplat achieves sharper and more precise segmentation results compared to previous methods. | p. 7 (4.2. Results and Analysis) |
| 4.2. Results and Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, SpatialSplat outperforms all compared methods, even surpassing L-Seg, which provides semantic feature supervision GT LSM LSM Ours Ours Figure 6. | p. 7 (4.2. Results and Analysis) |
| 4.3. Ablations and Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | (2) Does the improved scene understanding stem from the proposed dual-field architecture? | p. 8 (4.3. Ablations and Analysis) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** We filter out bad scenes and those with incomplete extrinsic parameters, resulting in a training dataset of approximately 1,500 scenes.
- **p. 8 / 25.58 MB - extractive PDF cue:** Notably, since Replica is a synthetic dataset with a different data modality from our training set, this underscores the strong generalization ability of our approach.
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** For evaluation, we follow LSM and select 40 unseen scenes from ScanNet to assess our model's performance.
- **p. 8 / 25.58 MB - extractive PDF cue:** Model efficiency comparison. "-Lite": the model replaces LSeg with CLIP ViT-B/16. unseen Replica dataset in both novel view synthesis and open-vocabulary segmentation.
- **p. 6 / 4.2. Results and Analysis - extractive PDF cue:** We observe that LSM struggles in certain scenes due to its reliance on accurate depth for aligning views during training as shown in Fig.
- **p. 7 / 4.2. Results and Analysis - extractive PDF cue:** Results of Cross-Dataset Generalization.
- **p. 7 / 4.2. Results and Analysis - extractive PDF cue:** Following LSM's approach, we map category labels from the Scannet dataset into common categories: Wall, Floor, Ceiling, Chair, Table, Bed, Sofa, Others.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** SpatialSplat generalizes well on OOD data. and NeRF-DFF [23], pre-scene optimization methods for semantic 3D reconstruction based on 3DGS [19] and NeRF [29], respectively.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Comparison between previous methods and our SpatialSplat. (a): Previous methods predict pixel-wise Gaussians, associating each primitive with compressed semantic feature. (b): Our SpatialSplat ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Pipeline of SpatialSplat. The SpatialSplat processes unposed images along with their intrinsics through a 3D geometry trans- former. The extracted features from the ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative Comparison in 3D Tasks on Scannet dataset. Our method outperforms both the latest SOTA semantic-aware feed-forward approach and per-scene optimization methods. "-Lite": ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative comparison in NVS. SpatialSplat can synthesize realistic novel views. In challenging cases where LSM fails, such as the table legs in the ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Out-of-distribution (OOD) comparison on Replica dataset. SpatialSplat generalizes well on OOD data. and NeRF-DFF [23], pre-scene optimization methods for semantic 3D reconstruction based ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative comparison in OVS. SpatialSplat achieves sharper and more precise segmentation results compared to previous methods. Notably, our method excels in challenging details, ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. The rendered instance features. SpatialSplat predicts clear and consistent instance features across different views. cent SOTA methods designed specifically for novel view synthesis. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Qualitative results of cross-dataset generalization. Zoom out for clearer visualization. for other compared methods. As illustrated in Fig. 4, Spa- tialSplat produces sharp ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We filter out bad scenes and those with incomplete extrinsic parameters, resulting in a training dataset of approximately 1,500 scenes. | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setup), p. 8 (25.58 MB) |
| Task/environment | Notably, since Replica is a synthetic dataset with a different data modality from our training set, this underscores the strong generalization ability of our ... | reset, timeout, object/scene variation | p. 8 (25.58 MB), p. 5 (4.1. Experimental Setup) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. 3D Geometry Prediction), p. 4 (3.1. 3D Geometry Prediction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. 3D Geometry Prediction), p. 4 (3.3. Dual-field Architecture) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For OVS, we evaluate performance using class-wise intersection over union (mIoU) and average pixel accuracy (mAcc). | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| The importance score threshold τ is set to 0.5, the downsampling ratio to 8, the instance feature dimension N to 8, and the semantic ... | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| (a) and (b) Qualitative results of importance score prediction, with red color indicating an importance score of 1 and blue indicating 0. | definition/direction/unit from same section | p. 8 (4.2. Results and Analysis) |
| Notably, since Replica is a synthetic dataset with a different data modality from our training set, this underscores the strong generalization ability of our ... | definition/direction/unit from same section | p. 8 (25.58 MB) |
| Although NeRF-DFF uses more images for training, our method still outperforms it and even demonstrates competitive performance with very re26409 | definition/direction/unit from same section | p. 6 (4.2. Results and Analysis) |
| For evaluation, we follow LSM and select 40 unseen scenes from ScanNet to assess our model's performance. | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| Following LSM's approach, we map category labels from the Scannet dataset into common categories: Wall, Floor, Ceiling, Chair, Table, Bed, Sofa, Others. | definition/direction/unit from same section | p. 7 (4.2. Results and Analysis) |
| This is achieved by lifting both 2D instance and uncompressed semantic into 3D space, enabling more efficient semantic learning while mitigating the blurred contours ... | definition/direction/unit from same section | p. 7 (4.2. Results and Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1, SpatialSplat outperforms all compared methods, even surpassing L-Seg, which provides semantic feature supervision GT LSM LSM Ours Ours Figure 6. | comparison identity and matched condition | p. 7 (4.2. Results and Analysis) |
| We primarily compare our method with LSM [15], the latest state-of-the-art (SOTA) approach for generalizable semantic 3D reconstruction. | comparison identity and matched condition | p. 5 (4.1. Experimental Setup) |
| 1, SpatialSplat significantly outperforms latest SOTA method LSM. | comparison identity and matched condition | p. 6 (4.2. Results and Analysis) |
| For a fair comparison, we train the model at a resolution of 256 × 256, consistent with our baseline. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| Our experiments primarily focus on two-view settings to ensure a fair comparison with our baseline. | comparison identity and matched condition | p. 8 (4.3. Ablations and Analysis) |
| Figure 1. Comparison between previous methods and our SpatialSplat. (a): Previous methods predict pixel-wise Gaussians, associating each primitive with compressed semantic feature. (b): Our ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We perform ablations to answer the following questions: (1) Are the primitives removed by our selective Gaussian mechanism truly redundant? | component/input/data sensitivity | p. 8 (4.3. Ablations and Analysis) |
| Figure 7. Qualitative results of ablations. (a) and (b) Qualitative results of importance score prediction, with red color indicating an importance score of 1 ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 1. Quantitative Comparison in 3D Tasks on Scannet dataset. Our method outperforms both the latest SOTA semantic-aware feed-forward approach and per-scene optimization methods. ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Figure 2. Pipeline of SpatialSplat. The SpatialSplat processes unposed images along with their intrinsics through a 3D geometry trans- former. The extracted features from ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Additionally, we introduce a Selective Gaussian Mechanism (SGM) to eliminate redundancy in overlapping areas caused by pixelwise representations, along with a novel loss function ... | In challenging cases where LSM fails, such as the table legs in the first two rows and the corners in the last two rows, ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Experimental Setup), p. 6 (4.2. Results and Analysis), p. 7 (4.2. Results and Analysis), p. 7 (4.2. Results and Analysis), p. 8 (4.3. Ablations and Analysis), p. 8 (4.3. Ablations and Analysis) |
| Primary metric/result | 1, SpatialSplat significantly outperforms latest SOTA method LSM. | numeric claim only at cited anchor | p. 6 (4.2. Results and Analysis) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** We filter out bad scenes and those with incomplete extrinsic parameters, resulting in a training dataset of approximately 1,500 scenes.
- **p. 8 / 4.2. Results and Analysis - extractive PDF cue:** Method Latency↓ Gaussian Size ↓ Num. ↓ Feature-3DGS [52] 1069 s

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In challenging cases where LSM fails, such as the table legs in the first two rows and the corners in the last two rows, ... | p. 6 (4.1. Experimental Setup) |
| body limitation/failure cue | The primary issue is that per-primitive semantic learning struggles to maintain accurate semantics and fails to preserve clear instance boundaries, as illustrated in Fig. | p. 8 (4.3. Ablations and Analysis) |
| body limitation/failure cue | Furthermore, as our method does not rely on dense semantic supervision, we leverage a lightweight pretrained 2D model, significantly accelerating inference speed. | p. 8 (25.58 MB) |
| body limitation/failure cue | Out-of-distribution (OOD) comparison on Replica dataset. | p. 6 (4.1. Experimental Setup) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To save training time, the instance masks M are generated by SAM [21] prior to training, while the semantic feature map ˆ F S ... | p. 5 (3.4. Training Objective) |
| For the 3D geometry prediction module, we use ViT-Large with a patch size of 16 as the encoder and ViT-Base as the decoder, both ... | p. 6 (4.1. Experimental Setup) |
| The encoder weights are shared across different input views. | p. 3 (3.1. 3D Geometry Prediction) |
| Both the encoder and decoder in our geometric prediction module are built on pure ViT structures, requiring no geometric priors as in previous methods ... | p. 3 (3.1. 3D Geometry Prediction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** In challenging cases where LSM fails, such as the table legs in the first two rows and the corners in the last two rows, our ...
- **p. 8 / 4.3. Ablations and Analysis - extractive PDF cue:** The primary issue is that per-primitive semantic learning struggles to maintain accurate semantics and fails to preserve clear instance boundaries, as illustrated in Fig.
- **p. 8 / 25.58 MB - extractive PDF cue:** Furthermore, as our method does not rely on dense semantic supervision, we leverage a lightweight pretrained 2D model, significantly accelerating inference speed.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Out-of-distribution (OOD) comparison on Replica dataset.

- **PDF anchors reviewed:** datasets p. 5 (4.1. Experimental Setup), p. 8 (25.58 MB), p. 5 (4.1. Experimental Setup), p. 8 (25.58 MB), p. 6 (4.2. Results and Analysis), p. 7 (4.2. Results and Analysis), metrics p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 8 (4.2. Results and Analysis), p. 8 (25.58 MB), p. 6 (4.2. Results and Analysis), p. 5 (4.1. Experimental Setup), baselines p. 7 (4.2. Results and Analysis), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Results and Analysis), p. 6 (4.1. Experimental Setup), p. 8 (4.3. Ablations and Analysis), p. 1 (Figure/Table caption), results p. 6 (4.1. Experimental Setup), p. 6 (4.2. Results and Analysis), p. 7 (4.2. Results and Analysis), p. 7 (4.2. Results and Analysis), p. 8 (4.3. Ablations and Analysis), p. 8 (4.3. Ablations and Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
