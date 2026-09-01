# Evaluation - UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_UniPre3D_Unified_Pre-training_of_3D_Point_Cloud_Models_with_Cross-Modal_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_UniPre3D_Unified_Pre-training_of_3D_Point_Cloud_Models_with_Cross-Modal_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2.1. Object-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning), p. 8 (4.3. Ablation Studies), p. 5 (4.1. Pre-training), p. 6 (4.2.1. Object-level Fine-tuning)): For part segmentation in Table 2, UniPre3D achieves the best performance on the mIoUC metric and competitive results with TAP on mIoUI.

## Evaluation Body Digest

- **p. 5 / 4.1. Pre-training - extractive PDF cue:** For scene-level pre-training, we utilize the real-world ScanNetV2 dataset [10] with more than 1,500 scans of indoor scenes.
- **p. 6 / 4.2.1. Object-level Fine-tuning - extractive PDF cue:** When fine-tuning object models for classification, we experiment on the real-world ScanObjectNN [47] dataset, which comprises 15 categories and includes three splits: OBJ BG, OBJ ...
- **p. 7 / 4.2.2. Scene-level Fine-tuning - extractive PDF cue:** Model Pre-train mIoUC mIoUI PointNet [34] ✗ 80.4 83.7 PointNet++ [35] ✗ 81.9 85.1 DGCNN [55] ✗ 82.3 85.2 KPConv [45] ✗ 85.1 86.4 Standard ...
- **p. 5 / 4.1. Pre-training - extractive PDF cue:** For object-level pre-training, we adhere to established practices [31, 67] to use the synthetic ShapeNet dataset [2].
- **p. 6 / 4.2.2. Scene-level Fine-tuning - extractive PDF cue:** When fine-tuning on scene-level segmentation, we first assess the pre-training dataset itself, ScanNetV2 [10], which comprises 20 classes.
- **p. 7 / 4.2.2. Scene-level Fine-tuning - extractive PDF cue:** Semantic segmentation results on the scene-level datasets.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Furthermore, point fusion proves to be more effective for scene pre-training than feature fusion, with optimal fine-tuning results across all datasets achieved when fusing 2D ...
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** The ablation results confirm our findings from object pre-training, that supplementary image knowledge is essential for enhancing our pre-training pipeline, particularly on the challenging long-tail ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2.1. Object-level Fine-tuning | EMPIRICAL / REAL-ROBOT OR HARDWARE | For part segmentation in Table 2, UniPre3D achieves the best performance on the mIoUC metric and competitive results with TAP on mIoUI. | p. 6 (4.2.1. Object-level Fine-tuning) |
| 4.2.2. Scene-level Fine-tuning | EMPIRICAL / REAL-ROBOT OR HARDWARE | For instance segmentation in Table 4, UniPre3D also achieves state-ofthe-art performance across most benchmarks, with particularly strong results on ScanNet200. | p. 7 (4.2.2. Scene-level Fine-tuning) |
| 4.2.2. Scene-level Fine-tuning | EMPIRICAL / REAL-ROBOT OR HARDWARE | When compared to prior scene pre-training approaches with the SparseUNet backbone, UniPre3D also achieves the best results on ScanNet20 and ScanNet200. | p. 7 (4.2.2. Scene-level Fine-tuning) |
| 4.3. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | Furthermore, point fusion proves to be more effective for scene pre-training than feature fusion, with optimal fine-tuning results across all datasets achieved when fusing ... | p. 8 (4.3. Ablation Studies) |
| 4.1. Pre-training | EMPIRICAL / REAL-ROBOT OR HARDWARE | Additionally, we use the advanced PointTransformerV3 [59] as the backbone, which demonstrates significantly higher baseline performance than SparseUNet, to show that UniPre3D remains effective ... | p. 5 (4.1. Pre-training) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Pre-training - extractive PDF cue:** For scene-level pre-training, we utilize the real-world ScanNetV2 dataset [10] with more than 1,500 scans of indoor scenes.
- **p. 6 / 4.2.1. Object-level Fine-tuning - extractive PDF cue:** When fine-tuning object models for classification, we experiment on the real-world ScanObjectNN [47] dataset, which comprises 15 categories and includes three splits: OBJ BG, OBJ ...
- **p. 7 / 4.2.2. Scene-level Fine-tuning - extractive PDF cue:** Model Pre-train mIoUC mIoUI PointNet [34] ✗ 80.4 83.7 PointNet++ [35] ✗ 81.9 85.1 DGCNN [55] ✗ 82.3 85.2 KPConv [45] ✗ 85.1 86.4 Standard ...
- **p. 5 / 4.1. Pre-training - extractive PDF cue:** For object-level pre-training, we adhere to established practices [31, 67] to use the synthetic ShapeNet dataset [2].
- **p. 6 / 4.2.2. Scene-level Fine-tuning - extractive PDF cue:** When fine-tuning on scene-level segmentation, we first assess the pre-training dataset itself, ScanNetV2 [10], which comprises 20 classes.
- **p. 7 / 4.2.2. Scene-level Fine-tuning - extractive PDF cue:** Semantic segmentation results on the scene-level datasets.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Furthermore, point fusion proves to be more effective for scene pre-training than feature fusion, with optimal fine-tuning results across all datasets achieved when fusing 2D ...
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** The ablation results confirm our findings from object pre-training, that supplementary image knowledge is essential for enhancing our pre-training pipeline, particularly on the challenging long-tail ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Pre-training paradigm comparison. Existing object- level pre-training methods usually follow a generative masked auto-encoding (MAE) paradigm. Their scene-level counterparts mostly leverage the contrastive ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. UniPre3D pre-training pipeline. Our proposed pre- training task involves predicting Gaussian parameters from the in- put point cloud. The 3D backbone network is ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 6. Our analysis suggests that this is primarily due to the sparsity of the scene point cloud and the exponential in- crease in complexity ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Visualization of UniPre3D pre-training outputs. The first row presents the input point clouds, followed by the reference view images in the second row. ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Classification results on the ScanObjectNN dataset. We report the overall accuracy (%) on three data splits.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Part segmentation results on the ShapeNetPart dataset. We report the mean IoU across all part categories mIoUC, and the mean IoU across all ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Semantic segmentation results on the scene-level datasets. We report the mean IoU on the validation set. The Standard Transformer results are from PCP-MAE ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Instance segmentation results on the scene-level datasets. We use PointGroup [19] as the baseline model, follow- ing previous papers. We report the mean ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For scene-level pre-training, we utilize the real-world ScanNetV2 dataset [10] with more than 1,500 scans of indoor scenes. | embodiment, simulator version and control stack | p. 5 (4.1. Pre-training), p. 6 (4.2.1. Object-level Fine-tuning) |
| Task/environment | When fine-tuning object models for classification, we experiment on the real-world ScanObjectNN [47] dataset, which comprises 15 categories and includes three splits: OBJ BG, ... | reset, timeout, object/scene variation | p. 6 (4.2.1. Object-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.2. Overall Pipeline), p. 4 (3.3. Scale-Adaptive Cross-Modal Fusion) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.2. Overall Pipeline), p. 4 (3.3. Scale-Adaptive Cross-Modal Fusion) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Across more advanced models [14, 29, 71], UniPre3D delivers consistent and substantial performance gains, even on Mamba3D [14] with already high accuracy. | definition/direction/unit from same section | p. 6 (4.2.1. Object-level Fine-tuning) |
| We report the overall accuracy (%) on three data splits. | definition/direction/unit from same section | p. 6 (4.2.1. Object-level Fine-tuning) |
| We report the mean IoU on the validation set. | definition/direction/unit from same section | p. 7 (4.2.2. Scene-level Fine-tuning) |
| We report the mean IoU across all part categories mIoUC, and the mean IoU across all instances mIoUI. | definition/direction/unit from same section | p. 7 (4.2.2. Scene-level Fine-tuning) |
| Table 6. Ablation studies on cross-modal feature fusion strate- gies. We report the PSNR metric for the pre-training stage and the mean IoU for ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Additionally, we use the advanced PointTransformerV3 [59] as the backbone, which demonstrates significantly higher baseline performance than SparseUNet, to show that UniPre3D remains effective ... | definition/direction/unit from same section | p. 5 (4.1. Pre-training) |
| For scene models, we use the AdamW optimizer [27] with a weight decay of 0.01 and an initial learning rate of 10-4. | definition/direction/unit from same section | p. 5 (4.1. Pre-training) |
| We report the mean average precision. | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Additionally, we use the advanced PointTransformerV3 [59] as the backbone, which demonstrates significantly higher baseline performance than SparseUNet, to show that UniPre3D remains effective ... | comparison identity and matched condition | p. 5 (4.1. Pre-training) |
| For object classification in Table 1, UniPre3D with the standard Transformer backbone [48] outperforms others on the challenging PB T50 RS benchmark. | comparison identity and matched condition | p. 6 (4.2.1. Object-level Fine-tuning) |
| For each backbone, the first row presents its baseline results, while the second row indicates pre-training with only the 3D branch. | comparison identity and matched condition | p. 7 (4.3. Ablation Studies) |
| For semantic segmentation in Table 3, UniPre3D outperforms previous object pre-training methods using the standard Transformer backbone on S3DIS. | comparison identity and matched condition | p. 7 (4.2.2. Scene-level Fine-tuning) |
| We use PointGroup [19] as the baseline model, following previous papers. | comparison identity and matched condition | p. 8 (4.3. Ablation Studies) |
| Additionally, the requirement for both point clouds and images adds data curation burden compared with other point-only pre-training methods. | comparison identity and matched condition | p. 8 (4.4. Limitations) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Furthermore, point fusion proves to be more effective for scene pre-training than feature fusion, with optimal fine-tuning results across all datasets achieved when fusing ... | component/input/data sensitivity | p. 8 (4.3. Ablation Studies) |
| The ablation results confirm our findings from object pre-training, that supplementary image knowledge is essential for enhancing our pre-training pipeline, particularly on the challenging ... | component/input/data sensitivity | p. 8 (4.3. Ablation Studies) |
| For object-level pre-training, we begin with the standard Transformer architecture [48], ensuring a fair comparison with previous MAE-based pretraining methods [24, 31, 40, 67]. | component/input/data sensitivity | p. 5 (4.1. Pre-training) |
| When fine-tuning on scene-level segmentation, we first assess the pre-training dataset itself, ScanNetV2 [10], which comprises 20 classes. | component/input/data sensitivity | p. 6 (4.2.2. Scene-level Fine-tuning) |
| Subsequently, we fine-tune on the ScanNet200 [43] dataset, which shares the same 2D and 3D data with ScanNetV2 but features more fine-grained annotations covering ... | component/input/data sensitivity | p. 6 (4.2.2. Scene-level Fine-tuning) |
| For object-level pre-training, we ablate on the integration layer with classification fine-tuning on ScanObjectNN (PB T50 RS), shown in Table 5. | component/input/data sensitivity | p. 7 (4.3. Ablation Studies) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In conclusion, the contributions of our paper are as follows: (1) We propose UniPre3D, the first unified pretraining method for point clouds of any ... | For part segmentation in Table 2, UniPre3D achieves the best performance on the mIoUC metric and competitive results with TAP on mIoUI. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2.1. Object-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning), p. 8 (4.3. Ablation Studies), p. 5 (4.1. Pre-training), p. 6 (4.2.1. Object-level Fine-tuning) |
| Primary metric/result | For instance segmentation in Table 4, UniPre3D also achieves state-ofthe-art performance across most benchmarks, with particularly strong results on ScanNet200. | numeric claim only at cited anchor | p. 7 (4.2.2. Scene-level Fine-tuning) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Pre-training - extractive PDF cue:** ShapeNet contains over 50,000 CAD models, from each of which we randomly sample point clouds of 1,024 points and evenly render 36 images via DISN ...
- **p. 5 / 4.1. Pre-training - extractive PDF cue:** Each scene contains a point cloud of over 100,000 points and hundreds of associated projected images.
- **p. 5 / 4.1. Pre-training - extractive PDF cue:** Object models are pre-trained for 50 epochs with the Adam optimizer [21] and a StepLR learning rate scheduler, set to an initial learning rate of ...
- **p. 5 / 4.1. Pre-training - extractive PDF cue:** The model is pre-trained for 100 epochs and the batch size is set to 8, with each point cloud taking eight input images and supervised ...
- **p. 6 / 4.2.1. Object-level Fine-tuning - extractive PDF cue:** For part segmentation fine-tuning, we utilize the ShapeNetPart [66] dataset that contains over 16,000 samples across 16 classes, featuring fine-grained part annotations for 50 categories.
- **p. 6 / 4.2.1. Object-level Fine-tuning - extractive PDF cue:** Model Pre-train OBJ BG OBJ ONLY PB T50 RS Standard Transformer [48] ✗ 79.86 80.55 77.24 OcCo [51] 84.85 85.54 78.79 Point-BERT [67] 87.43 88.12 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Even though we make an effective effort towards unified pre-training, there are still some limitations to be resolved in future research. | p. 8 (4.4. Limitations) |
| body limitation/failure cue | However, the application of pointbased models has been limited to S3DIS, and their performance still falls short of voxel-based models. | p. 7 (4.2.2. Scene-level Fine-tuning) |
| body limitation/failure cue | Our unified approach consistently outperforms prior scale-specific pre-training methods on most benchmarks, underscoring its robustness and adaptability. | p. 8 (5. Conclusion) |
| body limitation/failure cue | However, UniPre3D accurately predicts both geometry and color for other perspectives, demonstrating the 3D backbone is pre-trained to extract robust geometric features. | p. 6 (4.1. Pre-training) |
| body limitation/failure cue | Model Pre-train ScanNet20 ScanNet200 S3DIS Point-based Model PointNet [34] ✗ - - 41.1 PointNet++ [35] ✗ - - 53.5 PointNeXt [39] ✗ 71.5 - ... | p. 7 (4.2.2. Scene-level Fine-tuning) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The model is pre-trained for 100 epochs and the batch size is set to 8, with each point cloud taking eight input images and ... | p. 5 (4.1. Pre-training) |
| Object models are pre-trained for 50 epochs with the Adam optimizer [21] and a StepLR learning rate scheduler, set to an initial learning rate ... | p. 5 (4.1. Pre-training) |
| Results for PTv3 on S3DIS are omitted, as the official implementation requires disabling flash-attention, which significantly increases CUDA memory usage beyond the capacity of ... | p. 7 (4.2.2. Scene-level Fine-tuning) |
| The fourth and fifth rows examine the implementation layer options for the point fusion strategy, where Enc denotes fusion after the first layer of ... | p. 8 (4.3. Ablation Studies) |
| Decoder-Last denotes fusion only at the final decoder layer. | p. 7 (4.3. Ablation Studies) |
| Furthermore, point fusion proves to be more effective for scene pre-training than feature fusion, with optimal fine-tuning results across all datasets achieved when fusing ... | p. 8 (4.3. Ablation Studies) |
| Subsequently, we integrate the 3D feature F3D ∈RN×C3D from the final decoder layer of the backbone with ˆF2D: F_\ m athrm {fuse} = \mathrm ... | p. 4 (3.3. Scale-Adaptive Cross-Modal Fusion) |
| These 2D features are then encoded into the 3D domain using a learnable but lightweight adaptation block A, followed by back-projection to the 3D ... | p. 4 (3.2. Overall Pipeline) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.4. Limitations - extractive PDF cue:** Even though we make an effective effort towards unified pre-training, there are still some limitations to be resolved in future research.
- **p. 7 / 4.2.2. Scene-level Fine-tuning - extractive PDF cue:** However, the application of pointbased models has been limited to S3DIS, and their performance still falls short of voxel-based models.
- **p. 8 / 5. Conclusion - extractive PDF cue:** Our unified approach consistently outperforms prior scale-specific pre-training methods on most benchmarks, underscoring its robustness and adaptability.
- **p. 6 / 4.1. Pre-training - extractive PDF cue:** However, UniPre3D accurately predicts both geometry and color for other perspectives, demonstrating the 3D backbone is pre-trained to extract robust geometric features.
- **p. 7 / 4.2.2. Scene-level Fine-tuning - extractive PDF cue:** Model Pre-train ScanNet20 ScanNet200 S3DIS Point-based Model PointNet [34] ✗ - - 41.1 PointNet++ [35] ✗ - - 53.5 PointNeXt [39] ✗ 71.5 - 70.5 ...

- **PDF anchors reviewed:** datasets p. 5 (4.1. Pre-training), p. 6 (4.2.1. Object-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning), p. 5 (4.1. Pre-training), p. 6 (4.2.2. Scene-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning), metrics p. 6 (4.2.1. Object-level Fine-tuning), p. 6 (4.2.1. Object-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning), p. 8 (Figure/Table caption), p. 5 (4.1. Pre-training), baselines p. 5 (4.1. Pre-training), p. 6 (4.2.1. Object-level Fine-tuning), p. 7 (4.3. Ablation Studies), p. 7 (4.2.2. Scene-level Fine-tuning), p. 8 (4.3. Ablation Studies), p. 8 (4.4. Limitations), results p. 6 (4.2.1. Object-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning), p. 7 (4.2.2. Scene-level Fine-tuning), p. 8 (4.3. Ablation Studies), p. 5 (4.1. Pre-training), p. 6 (4.2.1. Object-level Fine-tuning).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
