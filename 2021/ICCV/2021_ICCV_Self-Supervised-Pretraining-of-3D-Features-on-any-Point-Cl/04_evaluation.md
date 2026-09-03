# Evaluation - Self-Supervised Pretraining of 3D Features on any Point-Cloud

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2101.02691; PDF retrieval source: https://arxiv.org/pdf/2101.02691. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.2. Pretraining with Point Input Format), p. 1 (Figure/Table caption), p. 6 (4.2. Pretraining with Point Input Format), p. 6 (4.2. Pretraining with Point Input Format), p. 4 (4. Experiments), p. 5 (4.2. Pretraining with Point Input Format)): DepthContrast outperforms training from scratch on all the four datasets, and improves performance by 12.1% mAP on the small S3DIS dataset that has only 200 labeled training samples.

## Evaluation Body Digest

- **p. 5 / 4.1. Transfer Datasets and Tasks - extractive body cue:** We use diverse downstream datasets - full scenes/object centric; using different 3D sensors; single/multi-view; real/synthetic; indoor/outdoor.
- **p. 5 / 4. Experiments - extractive body cue:** DepthContrast outperforms the scratch model on all benchmarks and is better than the detection-specific supervised pretraining on two datasets.
- **p. 4 / 4. Experiments - extractive body cue:** We evaluate DepthContrast pretraining by transfer learning, i.e., fine-tuning on downstream tasks and datasets.
- **p. 7 / 4.2. Pretraining with Point Input Format - extractive body cue:** Fig 4 shows the gain of our pretrained model over the scratch model across object classes on the SUNRGBD dataset.
- **p. 7 / 4.2. Pretraining with Point Input Format - extractive body cue:** This suggests that DepthContrast pretraining can partially address the long tailed label distributions of current 3D scene understanding benchmarks.
- **p. 6 / 4.2. Pretraining with Point Input Format - extractive body cue:** Overfitting is more pronounced on small datasets like S3DIS.
- **p. 6 / 4.2. Pretraining with Point Input Format - extractive body cue:** In Table 2, we observe that small labeled datasets benefit more from pretraining.
- **p. 8 / 5.3. Generalization to Outdoor LiDAR data - extractive body cue:** For transfer learning, we use the standard KITTI [26] object detection benchmark, and PointRCNN [80] and Part-A2 [81] for down-stream models.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3.5. Implementation Details (p. 4); 4. Experiments (p. 4); 4.1. Transfer Datasets and Tasks (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Pretraining with Point Input Format | EMPIRICAL / SOURCE-REPORTED EVALUATION | DepthContrast outperforms training from scratch on all the four datasets, and improves performance by 12.1% mAP on the small S3DIS dataset that has only ... | p. 5 (4.2. Pretraining with Point Input Format) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1: Label-efficiency of our self-supervised pretraining. We finetune detection models from scratch or using our pretraining as initialization. Our pretraining which uses unlabeled ... | p. 1 (Figure/Table caption) |
| 4.2. Pretraining with Point Input Format | EMPIRICAL / SOURCE-REPORTED EVALUATION | DepthContrast's performance improves significantly when using both large data and large models. | p. 6 (4.2. Pretraining with Point Input Format) |
| 4.2. Pretraining with Point Input Format | EMPIRICAL / SOURCE-REPORTED EVALUATION | The detection results in Table 3 show that our pretrained model achieves state-of-the-art performance on SUNRGBD and ScanNet. | p. 6 (4.2. Pretraining with Point Input Format) |
| 4. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We first study a single input 3D format and a single network architecture in § 4.2 showing that DepthContrast's performance improves with large data ... | p. 4 (4. Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Transfer Datasets and Tasks - extractive body cue:** We use diverse downstream datasets - full scenes/object centric; using different 3D sensors; single/multi-view; real/synthetic; indoor/outdoor.
- **p. 5 / 4. Experiments - extractive body cue:** DepthContrast outperforms the scratch model on all benchmarks and is better than the detection-specific supervised pretraining on two datasets.
- **p. 4 / 4. Experiments - extractive body cue:** We evaluate DepthContrast pretraining by transfer learning, i.e., fine-tuning on downstream tasks and datasets.
- **p. 7 / 4.2. Pretraining with Point Input Format - extractive body cue:** Fig 4 shows the gain of our pretrained model over the scratch model across object classes on the SUNRGBD dataset.
- **p. 7 / 4.2. Pretraining with Point Input Format - extractive body cue:** This suggests that DepthContrast pretraining can partially address the long tailed label distributions of current 3D scene understanding benchmarks.
- **p. 6 / 4.2. Pretraining with Point Input Format - extractive body cue:** Overfitting is more pronounced on small datasets like S3DIS.
- **p. 6 / 4.2. Pretraining with Point Input Format - extractive body cue:** In Table 2, we observe that small labeled datasets benefit more from pretraining.
- **p. 8 / 5.3. Generalization to Outdoor LiDAR data - extractive body cue:** For transfer learning, we use the standard KITTI [26] object detection benchmark, and PointRCNN [80] and Part-A2 [81] for down-stream models.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Label-efficiency of our self-supervised pretraining. We finetune detection models from scratch or using our pretraining as initialization. Our pretraining which uses unlabeled single-view ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Approach Overview. We propose DepthContrast - a simple 3D representation learning method that uses large amounts of unprocessed single/multi-view depth maps. Given a ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Pretraining datasets and transfer tasks used in this paper. We use two different pretraining datasets without post-processing like 3D registration, camera calibration. We ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2: Detection AP25 using VoteNet [67]. We evaluate differ- ent pretrained models - random initialization, supervised VoteNet on ScanNet, and our self-supervised DepthContrast using ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 3: Transfer using state-of-the-art detection frameworks. We use our pretrained model (PointNet++ 3× on Redwood-vid +ScanNet-vid) and transfer it using two state-of-the-art detection frameworks ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Scaling the model size and pretraining data. We increase the model capacity of the PointNet++ model by increasing the width by {2×, 3×, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Pretraining benefits long tail classes. We analyze the gain of our pretraining across different classes for SUNRGBD object detection. The training data has ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4: Multiple input formats. We study the importance of training 3D representations jointly using multiple input formats - points and voxels. We vary the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We use diverse downstream datasets - full scenes/object centric; using different 3D sensors; single/multi-view; real/synthetic; indoor/outdoor. | embodiment, simulator version and control stack | p. 5 (4.1. Transfer Datasets and Tasks), p. 5 (4. Experiments) |
| Task/environment | DepthContrast outperforms the scratch model on all benchmarks and is better than the detection-specific supervised pretraining on two datasets. | reset, timeout, object/scene variation | p. 5 (4. Experiments), p. 4 (4. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.4. Data Augmentation for 3D), p. 3 (3.1. Instance Discrimination) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3. Approach), p. 2 (3. Approach) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use the implementation of [67] for finetuning and report the detection performance using the mean Average Precision at IoU=0.25 (AP25) metric. | definition/direction/unit from same section | p. 5 (4.2. Pretraining with Point Input Format) |
| In particular, as the gains are larger on stricter mAP at IoU=0.5, our pretrained models result in detection models that are better at localization. | definition/direction/unit from same section | p. 6 (4.2. Pretraining with Point Input Format) |
| Cuboid Drop ModelNet Linear (Accuracy) 80.6 85.4 85.0 SUNRGBD Detection (mAP) 58.6 59.5 60.7 Table 5: Data augmentation. | definition/direction/unit from same section | p. 7 (4.3. Pretraining with Multiple Input Formats) |
| Our augmentations lead to both a better feature representation: a gain of 5% accuracy on ModelNet classification, and a better pretrained model: 2% mAP ... | definition/direction/unit from same section | p. 8 (5.1. Importance of Data Augmentation) |
| Pretraining Task Scratch ScanNet ScanNet-vid Redwood-vid (Multi-view) (Single-view) (Single-view) ModelNet Linear (Accuracy) 50.7 85.1 85.0 86.4 SUNRGBD Detection (mAP) 57.4 60.5 60.7 60.4 Table ... | definition/direction/unit from same section | p. 8 (5.1. Importance of Data Augmentation) |
| DepthContrast outperforms training from scratch on all the four datasets, and improves performance by 12.1% mAP on the small S3DIS dataset that has only ... | definition/direction/unit from same section | p. 5 (4.2. Pretraining with Point Input Format) |
| Our joint loss gives the best performance. instances, while classes like chair have over 9000 instances. | definition/direction/unit from same section | p. 7 (4.2. Pretraining with Point Input Format) |
| We use single-view depth map videos 4 | definition/direction/unit from same section | p. 4 (4. Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 3: Transfer using state-of-the-art detection frameworks. We use our pretrained model (PointNet++ 3× on Redwood-vid +ScanNet-vid) and transfer it using two state-of-the-art detection ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Since the supervised baseline is pretrained specifically on object detection, it serves as a strong baseline. | comparison identity and matched condition | p. 5 (4.2. Pretraining with Point Input Format) |
| The detection results in Table 3 show that our pretrained model achieves state-of-the-art performance on SUNRGBD and ScanNet. | comparison identity and matched condition | p. 6 (4.2. Pretraining with Point Input Format) |
| Compared to training from scratch, the within format pretraining only provides a benefit for the point input format PointNet++ models. | comparison identity and matched condition | p. 7 (4.3. Pretraining with Multiple Input Formats) |
| Figure 1: Label-efficiency of our self-supervised pretraining. We finetune detection models from scratch or using our pretraining as initialization. Our pretraining which uses unlabeled ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| All the DepthContrast models outperform the scratch model. | comparison identity and matched condition | p. 8 (5.2. Impact of Single-view or Multi-view 3D Data) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To analyze which of these loss terms matter for pretraining, we consider three variants - (1) Within format which independently trains format-specific models for ... | component/input/data sensitivity | p. 7 (4.3. Pretraining with Multiple Input Formats) |
| Thus, we analyze the effect of our proposed augmentations from § 3.4 on transfer performance. | component/input/data sensitivity | p. 7 (5.1. Importance of Data Augmentation) |
| Our self-supervised method does not make assumptions on the input data and can use single-view depth maps without 3D preprocessing as input. | component/input/data sensitivity | p. 8 (5.2. Impact of Single-view or Multi-view 3D Data) |
| Table 1: Pretraining datasets and transfer tasks used in this paper. We use two different pretraining datasets without post-processing like 3D registration, camera calibration. ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| We evaluate DepthContrast pretraining by transfer learning, i.e., fine-tuning on downstream tasks and datasets. | component/input/data sensitivity | p. 4 (4. Experiments) |
| This suggests that pretraining is crucial for training large 3D detection models. | component/input/data sensitivity | p. 5 (4.2. Pretraining with Point Input Format) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions can be summarized as follows: • We show that single view 3D depth scans can be used to learn powerful feature representations ... | DepthContrast outperforms training from scratch on all the four datasets, and improves performance by 12.1% mAP on the small S3DIS dataset that has only ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.2. Pretraining with Point Input Format), p. 1 (Figure/Table caption), p. 6 (4.2. Pretraining with Point Input Format), p. 6 (4.2. Pretraining with Point Input Format), p. 4 (4. Experiments), p. 5 (4.2. Pretraining with Point Input Format) |
| Primary metric/result | Figure 1: Label-efficiency of our self-supervised pretraining. We finetune detection models from scratch or using our pretraining as initialization. Our pretraining which uses unlabeled ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 4 / 3.5. Implementation Details - extractive body cue:** We use a standard SGD optimizer with momentum 0.9, cosine learning rate scheduler [53] starting from 0.12 to 0.00012 and train the model for 1000 ...
- **p. 5 / 4. Experiments - extractive body cue:** Following the train/val split from [67], we extract around 190K RGB-D scans (one frame every 15 frames) from about 1200 video sequences in the train ...
- **p. 8 / 5.3. Generalization to Outdoor LiDAR data - extractive body cue:** 5x fewer labels Figure 5: Using outdoor LiDAR data.
- **p. 3 / 3.1. Instance Discrimination - extractive body cue:** As using a large number of negatives is important for contrastive learning [13, 36, 59, 107], we 1Points in a depth map are a set, ...
- **p. 4 / 3.3. Model Architecture - extractive body cue:** The network's final layer produces C dimensional per-point features for 1024 points after aggregation.
- **p. 4 / 3.5. Implementation Details - extractive body cue:** We use a standard SGD optimizer with momentum 0.9, cosine learning rate scheduler [53] starting from 0.12 to 0.00012 and train the model for 1000 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | More importantly, the Redwood-vid dataset does not contain camera extrinsic parameters and thus cannot be registered to get a multi-view dataset which is a ... | p. 6 (4.2. Pretraining with Point Input Format) |
| body limitation/failure cue | We hope DepthContrast helps future work in 3D self-supervised learning. | p. 8 (6. Conclusion) |
| body limitation/failure cue | We observe overfitting on the small datasets like S3DIS where increasing the model capacity does not improve performance. | p. 5 (4.2. Pretraining with Point Input Format) |
| body limitation/failure cue | For the voxel models, this pretraining does not improve consistently over training from scratch, which is in line with observations from recent work [109]. | p. 7 (4.3. Pretraining with Multiple Input Formats) |
| body limitation/failure cue | This is not surprising given that our objective does not rely on multi-view information. | p. 8 (5.2. Impact of Single-view or Multi-view 3D Data) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use a standard SGD optimizer with momentum 0.9, cosine learning rate scheduler [53] starting from 0.12 to 0.00012 and train the model for ... | p. 4 (3.5. Implementation Details) |
| We use 130K negatives for contrastive learning in Eq 3 and a momentum of 0.9 for the momentum encoder following [36]. | p. 4 (3.5. Implementation Details) |
| We use the implementation of [67] for finetuning and report the detection performance using the mean Average Precision at IoU=0.25 (AP25) metric. | p. 5 (4.2. Pretraining with Point Input Format) |
| We pretrain DepthContrast using both the point and voxel input formats and use two format-specific encoders - PointNet++ for points and UNet for voxels. | p. 7 (4.3. Pretraining with Multiple Input Formats) |
| This allows us to use a large number K of negative samples without increasing the training batch size. | p. 3 (3.1. Instance Discrimination) |
| We describe the model architecture used for our input format-specific encoders. | p. 3 (3.3. Model Architecture) |
| We use the standard LiDAR-specific model architectures as our format-specific encoders - PointnetMSG [80] for point clouds and SpconvSame perf. | p. 8 (5.3. Generalization to Outdoor LiDAR data) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.2. Pretraining with Point Input Format - extractive body cue:** More importantly, the Redwood-vid dataset does not contain camera extrinsic parameters and thus cannot be registered to get a multi-view dataset which is a necessity ...
- **p. 8 / 6. Conclusion - extractive body cue:** We hope DepthContrast helps future work in 3D self-supervised learning.
- **p. 5 / 4.2. Pretraining with Point Input Format - extractive body cue:** We observe overfitting on the small datasets like S3DIS where increasing the model capacity does not improve performance.
- **p. 7 / 4.3. Pretraining with Multiple Input Formats - extractive body cue:** For the voxel models, this pretraining does not improve consistently over training from scratch, which is in line with observations from recent work [109].
- **p. 8 / 5.2. Impact of Single-view or Multi-view 3D Data - extractive body cue:** This is not surprising given that our objective does not rely on multi-view information.

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Transfer Datasets and Tasks), p. 5 (4. Experiments), p. 4 (4. Experiments), p. 7 (4.2. Pretraining with Point Input Format), p. 7 (4.2. Pretraining with Point Input Format), p. 6 (4.2. Pretraining with Point Input Format), metrics p. 5 (4.2. Pretraining with Point Input Format), p. 6 (4.2. Pretraining with Point Input Format), p. 7 (4.3. Pretraining with Multiple Input Formats), p. 8 (5.1. Importance of Data Augmentation), p. 8 (5.1. Importance of Data Augmentation), p. 5 (4.2. Pretraining with Point Input Format), baselines p. 5 (Figure/Table caption), p. 5 (4.2. Pretraining with Point Input Format), p. 6 (4.2. Pretraining with Point Input Format), p. 7 (4.3. Pretraining with Multiple Input Formats), p. 1 (Figure/Table caption), p. 8 (5.2. Impact of Single-view or Multi-view 3D Data), results p. 5 (4.2. Pretraining with Point Input Format), p. 1 (Figure/Table caption), p. 6 (4.2. Pretraining with Point Input Format), p. 6 (4.2. Pretraining with Point Input Format), p. 4 (4. Experiments), p. 5 (4.2. Pretraining with Point Input Format).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
