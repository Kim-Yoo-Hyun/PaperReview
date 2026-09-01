# Evaluation - RIOcc: Efficient Cross-Modal Fusion Transformer with Collaborative Feature Refinement for 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fan_RIOcc_Efficient_Cross-Modal_Fusion_Transformer_with_Collaborative_Feature_Refinement_for_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fan_RIOcc_Efficient_Cross-Modal_Fusion_Transformer_with_Collaborative_Feature_Refinement_for_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption), p. 5 (Figure/Table caption), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption)): Figure 1. Comparison between OpenOccupancy and the pro- posed RIOcc. Instead of processing voxel features like OpenOc- cupancy, we choose BEV features to achieve higher computational efficiency. Additionally, we extracted ...

## Evaluation Body Digest

- **p. 6 / 4.1. Dataset and Metrics - extractive PDF cue:** Both datasets inherit the data format of nuScenes, containing 700 training scenes and 150 validation scenes, with annotations for 17 categories.
- **p. 6 / 4.1. Dataset and Metrics - extractive PDF cue:** Similar to previous works [29, 31, 47, 52], we conducted extensive experiments based on the nuScenes dataset.
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** For the LiDAR branch, we voxelize 10 LiDAR sweeps and employ a voxel encoder for the nuScenes dataset.
- **p. 7 / 4.1. Dataset and Metrics - extractive PDF cue:** RIOcc Images LiDAR GT M-CONet 可视化：OCC3D-nuScenes F F_L F_R
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Detailed structure diagram of the wavelet encoder. The input BEV features undergo DWT and IWT to obtain richer structure and details. noise impact, ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. The additional qualitative comparisons results between RIOcc and M-CONet. The red box highlights the effectiveness in dealing with distant and occluded targets. discretization ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. The overall framework of RIOcc. This framework includes three main branches: LiDAR, Camera, and Interaction Branch. The LiDAR Branch processes LiDAR points through ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. Overview of Deformable Dual-Attention (DDA), which reduces the disparity between LiDAR and Camera BEV fea- tures and enhances scene understanding. features and utilizes ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiment (p. 6); 4.1. Dataset and Metrics (p. 6); 4.2. Implementation Details (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 1. Comparison between OpenOccupancy and the pro- posed RIOcc. Instead of processing voxel features like OpenOc- cupancy, we choose BEV features to achieve ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 2. The overall framework of RIOcc. This framework includes three main branches: LiDAR, Camera, and Interaction Branch. The LiDAR Branch processes LiDAR points ... | p. 3 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 3. The schema of Dual-branch Pooling (DBP). LiDAR feature representation is improved by adaptively highlighting im- portant semantic channels and significant geometric regions. ... | p. 4 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 5. Overview of Deformable Dual-Attention (DDA), which reduces the disparity between LiDAR and Camera BEV fea- tures and enhances scene understanding. features and ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 4. Detailed structure diagram of the wavelet encoder. The input BEV features undergo DWT and IWT to obtain richer structure and details. noise ... | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Dataset and Metrics - extractive PDF cue:** Both datasets inherit the data format of nuScenes, containing 700 training scenes and 150 validation scenes, with annotations for 17 categories.
- **p. 6 / 4.1. Dataset and Metrics - extractive PDF cue:** Similar to previous works [29, 31, 47, 52], we conducted extensive experiments based on the nuScenes dataset.
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** For the LiDAR branch, we voxelize 10 LiDAR sweeps and employ a voxel encoder for the nuScenes dataset.
- **p. 7 / 4.1. Dataset and Metrics - extractive PDF cue:** RIOcc Images LiDAR GT M-CONet 可视化：OCC3D-nuScenes F F_L F_R

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Comparison between OpenOccupancy and the pro- posed RIOcc. Instead of processing voxel features like OpenOc- cupancy, we choose BEV features to achieve higher ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. The overall framework of RIOcc. This framework includes three main branches: LiDAR, Camera, and Interaction Branch. The LiDAR Branch processes LiDAR points through ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. The schema of Dual-branch Pooling (DBP). LiDAR feature representation is improved by adaptively highlighting im- portant semantic channels and significant geometric regions. hance ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Detailed structure diagram of the wavelet encoder. The input BEV features undergo DWT and IWT to obtain richer structure and details. noise impact, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. Overview of Deformable Dual-Attention (DDA), which reduces the disparity between LiDAR and Camera BEV fea- tures and enhances scene understanding. features and utilizes ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. 3D Occupancy prediction performance on the Occ3D-nuScenes dataset. * means the performance using the camera mask during training. C, L, and R represent ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. 3D Occupancy prediction performance on nuScenes-Occupancy validation set. C represents camera and L represents LiDAR.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. The additional qualitative comparisons results between RIOcc and M-CONet. The red box highlights the effectiveness in dealing with distant and occluded targets. discretization ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Both datasets inherit the data format of nuScenes, containing 700 training scenes and 150 validation scenes, with annotations for 17 categories. | embodiment, simulator version and control stack | p. 6 (4.1. Dataset and Metrics), p. 6 (4.1. Dataset and Metrics) |
| Task/environment | Similar to previous works [29, 31, 47, 52], we conducted extensive experiments based on the nuScenes dataset. | reset, timeout, object/scene variation | p. 6 (4.1. Dataset and Metrics), p. 7 (4.2. Implementation Details) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.2. Features Extraction), p. 4 (3.3. Dual-branch Pooling) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. Overall Architecture), p. 6 (3.7. Loss) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4. Detailed structure diagram of the wavelet encoder. The input BEV features undergo DWT and IWT to obtain richer structure and details. noise ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 6. The additional qualitative comparisons results between RIOcc and M-CONet. The red box highlights the effectiveness in dealing with distant and occluded targets. ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 2. The overall framework of RIOcc. This framework includes three main branches: LiDAR, Camera, and Interaction Branch. The LiDAR Branch processes LiDAR points ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 5. Overview of Deformable Dual-Attention (DDA), which reduces the disparity between LiDAR and Camera BEV fea- tures and enhances scene understanding. features and ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 2. 3D Occupancy prediction performance on nuScenes-Occupancy validation set. C represents camera and L represents LiDAR. | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| During training, we use the AdamW optimizer, set the weight decay to 0.01, and an initial learning rate of 1e-4, with a multi-step learning ... | definition/direction/unit from same section | p. 7 (4.2. Implementation Details) |
| Table 6. Ablation Study of Aggregation Region Size. # Strategy mIoU 1 Addition 46.58 2 | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 7. Ablation study of the Dual-BEV fusion strategy. representation and improving scene understanding. Feature Alignment on Heatmaps. To demonstrate that our model effectively ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In comparison, the data coverage for Occ3D-nuScenes is [-40 m, 40 m] in the X and Y directions, and [-1 m, 5.4 m] in ... | comparison identity and matched condition | p. 6 (4.1. Dataset and Metrics) |
| Figure 1. Comparison between OpenOccupancy and the pro- posed RIOcc. Instead of processing voxel features like OpenOc- cupancy, we choose BEV features to achieve ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Figure 6. The additional qualitative comparisons results between RIOcc and M-CONet. The red box highlights the effectiveness in dealing with distant and occluded targets. ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 6. Ablation Study of Aggregation Region Size. # Strategy mIoU 1 Addition 46.58 2 | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 3. Ablation study of downsampling layer. # Semantic mIoU w/ Wavelet 53.32 ✓ 54.21 | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 7. Ablation study of the Dual-BEV fusion strategy. representation and improving scene understanding. Feature Alignment on Heatmaps. To demonstrate that our model effectively ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 6. Ablation Study of Aggregation Region Size. # Strategy mIoU 1 Addition 46.58 2 | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| For the camera branch, we use ResNet50 pretrained on ImageNet as the image backbone, and the input image size is cropped to 256×704. | component/input/data sensitivity | p. 7 (4.2. Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: • We propose a novel multi-modal 3D semantic occupancy prediction framework, RIOcc. | Figure 1. Comparison between OpenOccupancy and the pro- posed RIOcc. Instead of processing voxel features like OpenOc- cupancy, we choose BEV features to achieve ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption), p. 5 (Figure/Table caption), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Primary metric/result | Figure 2. The overall framework of RIOcc. This framework includes three main branches: LiDAR, Camera, and Interaction Branch. The LiDAR Branch processes LiDAR points ... | numeric claim only at cited anchor | p. 3 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Dataset and Metrics - extractive PDF cue:** The evaluation range for OpenOccupancy is [-51.2 m, 51.2 m] in the X and Y directions, and [-3 m, 5 m] in the Z direction, ...
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** For the camera branch, we use ResNet50 pretrained on ImageNet as the image backbone, and the input image size is cropped to 256×704.
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** Training is conducted on four NVIDIA 3090 GPUs with a batch size of 4, for a total of 24 epochs.
- **p. 4 / 3.3. Dual-branch Pooling - extractive PDF cue:** The features outputted from the Grid-wise Attention can be represented as: F_{ g rid}=\si gma ( R eLU{ ( f ^{7 \times 7}(F_{A v g}^{\prime ...
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** For the camera branch, we use ResNet50 pretrained on ImageNet as the image backbone, and the input image size is cropped to 256×704.
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** Training is conducted on four NVIDIA 3090 GPUs with a batch size of 4, for a total of 24 epochs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 4. Detailed structure diagram of the wavelet encoder. The input BEV features undergo DWT and IWT to obtain richer structure and details. noise ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training is conducted on four NVIDIA 3090 GPUs with a batch size of 4, for a total of 24 epochs. | p. 7 (4.2. Implementation Details) |
| During training, we use the AdamW optimizer, set the weight decay to 0.01, and an initial learning rate of 1e-4, with a multi-step learning ... | p. 7 (4.2. Implementation Details) |
| For the LiDAR stream, we specially compute the distance dr from each LiDAR point to the sensor and encode it using a Gaussian function ... | p. 5 (3.5. Deformable Dual-Attention) |
| The Semantic Encoder is used to enrich semantic information, improving the understanding of the scene (Sec 3.4). | p. 3 (3.1. Overall Architecture) |
| During the feature extraction stage, we design LiDAR and camera branches to encode multi-modal input, following the BEVFusion [25] setup. | p. 3 (3.2. Features Extraction) |
| Detailed structure diagram of the wavelet encoder. | p. 4 (3.4.1. Wavelet Encoder) |
| The Semantic Encoder first downsamples the input BEV features to capture global contextual information. | p. 4 (3.4.2. Semantic Encoder) |
| Additionally, we introduce an Auxiliary Semantic Loss Laux to optimize the refined semantic features extracted by the semantic encoder. | p. 6 (3.7. Loss) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Detailed structure diagram of the wavelet encoder. The input BEV features undergo DWT and IWT to obtain richer structure and details. noise impact, ...

- **PDF anchors reviewed:** datasets p. 6 (4.1. Dataset and Metrics), p. 6 (4.1. Dataset and Metrics), p. 7 (4.2. Implementation Details), p. 7 (4.1. Dataset and Metrics), metrics p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 3 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (4.2. Implementation Details), baselines p. 6 (4.1. Dataset and Metrics), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption), p. 5 (Figure/Table caption), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
