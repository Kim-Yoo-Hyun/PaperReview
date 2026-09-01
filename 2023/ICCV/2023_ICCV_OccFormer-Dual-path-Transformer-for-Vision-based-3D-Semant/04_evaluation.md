# Evaluation - OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.05316; PDF retrieval source: https://arxiv.org/pdf/2304.05316. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Datasets), p. 7 (4.4. Main Results), p. 8 (4.5. Ablation Studies), p. 8 (4.6. Qualitative Results), p. 7 (4.5. Ablation Studies), p. 5 (Figure/Table caption)): The proposed OccFormer outperforms the only vision-based method TPVFormer [21] and achieves comparable performance with LiDAR-based methods.

## Evaluation Body Digest

- **p. 5 / 4.1. Datasets - extractive PDF cue:** The SemanticKITTI dataset [2] is based on the popular KITTI Odometry Benchmark [16] and focuses on the semantic scene understanding with LiDAR points and front ...
- **p. 6 / 4.1. Datasets - extractive PDF cue:** The dataset includes 1000 driving sequences from various scenes.
- **p. 6 / 4.1. Datasets - extractive PDF cue:** The nuScenes dataset [3] is a large-scale autonomous driving dataset, collected in Boston and Singapore.
- **p. 7 / 4.4. Main Results - extractive PDF cue:** The results on nuScenes validation set is included in Appendix A.1.
- **p. 8 / 4.5. Ablation Studies - extractive PDF cue:** (GT) Occupancy (TPVFormer) Occupancy (Ours) Figure 4: Qualitative results on nuScenes validation set.
- **p. 5 / 4.1. Datasets - extractive PDF cue:** OccFormer is evaluated by its task of semantic scene completion, but with the monocular left camera as input following MonoScene [4].
- **p. 7 / 4.4. Main Results - extractive PDF cue:** Method Layer params GFLOPs IoU↑mIoU↑ MsDeAttn3D 3 2.74M 329.3 35.74 13.22 MsDeAttn3D 6 4.07M 379.2 36.50 13.46 FPN-3D [32] - 4.35M 307.0 36.12 12.89 performs ...
- **p. 8 / 4.6. Qualitative Results - extractive PDF cue:** 3, we visualize the predicted results of semantic scene completion on SemanticKITTI validation set from MonoScene [4] and our proposed OccFormer.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Datasets (p. 5); 4.2. Implementation Details (p. 6); 4.4. Main Results (p. 6); 4.6. Qualitative Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Datasets | EMPIRICAL / SOURCE-REPORTED EVALUATION | The proposed OccFormer outperforms the only vision-based method TPVFormer [21] and achieves comparable performance with LiDAR-based methods. | p. 6 (4.1. Datasets) |
| 4.4. Main Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | OccFormer achieves comparable IoU for scene completion and significantly better performance for the SSC mIoU. | p. 7 (4.4. Main Results) |
| 4.5. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | On the other hand, the proposed class-guided sampling significantly outperforms the default uniform sampling because it can better adapt to the task of 3D ... | p. 8 (4.5. Ablation Studies) |
| 4.6. Qualitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Nonetheless, OccFormer still achieves more accurate results on LiDAR segmentation. | p. 8 (4.6. Qualitative Results) |
| 4.5. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | Also, our dual-path transformer encoder achieves a better trade-off than the vanilla 3D convolution and the 3D windowed attention proposed in [36]. | p. 7 (4.5. Ablation Studies) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Datasets - extractive PDF cue:** The SemanticKITTI dataset [2] is based on the popular KITTI Odometry Benchmark [16] and focuses on the semantic scene understanding with LiDAR points and front ...
- **p. 6 / 4.1. Datasets - extractive PDF cue:** The dataset includes 1000 driving sequences from various scenes.
- **p. 6 / 4.1. Datasets - extractive PDF cue:** The nuScenes dataset [3] is a large-scale autonomous driving dataset, collected in Boston and Singapore.
- **p. 7 / 4.4. Main Results - extractive PDF cue:** The results on nuScenes validation set is included in Appendix A.1.
- **p. 8 / 4.5. Ablation Studies - extractive PDF cue:** (GT) Occupancy (TPVFormer) Occupancy (Ours) Figure 4: Qualitative results on nuScenes validation set.
- **p. 5 / 4.1. Datasets - extractive PDF cue:** OccFormer is evaluated by its task of semantic scene completion, but with the monocular left camera as input following MonoScene [4].
- **p. 7 / 4.4. Main Results - extractive PDF cue:** Method Layer params GFLOPs IoU↑mIoU↑ MsDeAttn3D 3 2.74M 329.3 35.74 13.22 MsDeAttn3D 6 4.07M 379.2 36.50 13.46 FPN-3D [32] - 4.35M 307.0 36.12 12.89 performs ...
- **p. 8 / 4.6. Qualitative Results - extractive PDF cue:** 3, we visualize the predicted results of semantic scene completion on SemanticKITTI validation set from MonoScene [4] and our proposed OccFormer.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1: The framework of the proposed OccFormer for camera-based 3D semantic occupancy prediction. The pipeline consists of the image encoder for extracting multi-scale 2D ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Illustration of the dual-path transformer block. The local path processes the 3D feature by applying the shared windowed attention to each horizontal slice, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1: Semantic scene completion results on SemanticKITTI test set. * represents these methods are adapted for the RGB inputs, which are implemented and reported ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 2: Semantic scene completion results on SemanticKITTI [2] validation set. * represents these methods are adapted for the RGB inputs, which are implemented and ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3: LiDAR segmentation results on nuScenes test set. The proposed OccFormer outperforms the only vision-based method TPVFormer [21] and achieves comparable performance with LiDAR-based ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation study on the dual-path encoder. Local Global Params GFLOPs IoU↑mIoU↑  74.1M 494.2 36.42
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: Qualitative results on SemanticKITTI validation set. The input monocular image is shown on the left and the 3D semantic occupancy results from MonoScene ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5: Ablation study on the pixel decoder.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The SemanticKITTI dataset [2] is based on the popular KITTI Odometry Benchmark [16] and focuses on the semantic scene understanding with LiDAR points and ... | embodiment, simulator version and control stack | p. 5 (4.1. Datasets), p. 6 (4.1. Datasets) |
| Task/environment | The dataset includes 1000 driving sequences from various scenes. | reset, timeout, object/scene variation | p. 6 (4.1. Datasets), p. 6 (4.1. Datasets) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (3.1. Overview), p. 3 (3.1. Overview) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (3.1. Overview) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| OccFormer achieves comparable IoU for scene completion and significantly better performance for the SSC mIoU. | definition/direction/unit from same section | p. 7 (4.4. Main Results) |
| Also, the intersection over union (IoU) for the class-agnostic scene completion (SC) task is reported. | definition/direction/unit from same section | p. 6 (4.3. Metrics) |
| Method Layer params GFLOPs IoU↑mIoU↑ MsDeAttn3D 3 2.74M 329.3 35.74 13.22 MsDeAttn3D 6 4.07M 379.2 36.50 13.46 FPN-3D [32] - 4.35M 307.0 36.12 12.89 ... | definition/direction/unit from same section | p. 7 (4.4. Main Results) |
| Local Global Params GFLOPs IoU↑mIoU↑  74.1M 494.2 36.42 12.95  81.4M 407.4 36.37 12.93   81.4M 515.3 36.50 13.46 3D ResNet-16 [18] ... | definition/direction/unit from same section | p. 6 (4.2. Implementation Details) |
| Table 1: Semantic scene completion results on SemanticKITTI test set. * represents these methods are adapted for the RGB inputs, which are implemented and ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 8: Detailed Comparison between sampling methods on SemanticKITTI [2] validation set. SC SSC Sampling Method IoU ■road (15.30%) ■sidewalk (11.13%) ■parking (1.12%) | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Table 10: Ablation study on augmentations. Image Aug. 3D Aug. IoU↑mIoU↑  36.37 12.72  35.73 12.94   | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| OccFormer is evaluated by its task of semantic scene completion, but with the monocular left camera as input following MonoScene [4]. | definition/direction/unit from same section | p. 5 (4.1. Datasets) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 3, our method outperforms the only vision-based method TPVFormer and achieves comparable performance with the state-of-the-art LiDAR-based methods. | comparison identity and matched condition | p. 7 (4.4. Main Results) |
| Considering the image backbone network, we adopt EfficientNetB7 [4] on SemanticKITTI and ResNet-101 [18] on nuScenes, following the compared methods [4, 21]. | comparison identity and matched condition | p. 6 (4.2. Implementation Details) |
| 4, we ablate the dual-path design for the 3D feature extraction and compare it with other baseline methods. | comparison identity and matched condition | p. 7 (4.5. Ablation Studies) |
| Compared with MonoScene, our method can better understand the scene-level semantic layout and hallucinate the invisible regions. | comparison identity and matched condition | p. 8 (4.6. Qualitative Results) |
| Compared with the tri-linear interpolation, we employ the max-pooling to preserve the fine-grained 3D predictions during downsampling, which achieves a boost of about 0.5 ... | comparison identity and matched condition | p. 8 (4.5. Ablation Studies) |
| Table 1: Semantic scene completion results on SemanticKITTI test set. * represents these methods are adapted for the RGB inputs, which are implemented and ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The ablation is conducted on SemanticKITTI validation set and from three perspectives: the dual-path encoder, the pixel decoder, and the transformer decoder. | component/input/data sensitivity | p. 7 (4.5. Ablation Studies) |
| Table 4: Ablation study on the dual-path encoder. Local Global Params GFLOPs IoU↑mIoU↑  74.1M 494.2 36.42 | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 5: Ablation study on the pixel decoder. | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 4: Qualitative results on nuScenes validation set. The leftmost column shows the input surrounding images, the following three columns visualize the LiDAR segmentation ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 10: Ablation study on augmentations. Image Aug. 3D Aug. IoU↑mIoU↑  36.37 12.72  35.73 12.94   | component/input/data sensitivity | p. 10 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| For the encoder part, we propose the dual-path transformer block to unleash the capacity of selfattention while limiting the quadratic complexity. | The proposed OccFormer outperforms the only vision-based method TPVFormer [21] and achieves comparable performance with LiDAR-based methods. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Datasets), p. 7 (4.4. Main Results), p. 8 (4.5. Ablation Studies), p. 8 (4.6. Qualitative Results), p. 7 (4.5. Ablation Studies), p. 5 (Figure/Table caption) |
| Primary metric/result | OccFormer achieves comparable IoU for scene completion and significantly better performance for the SSC mIoU. | numeric claim only at cited anchor | p. 7 (4.4. Main Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Datasets - extractive PDF cue:** Each sequence lasts for around 20 seconds and the key-frames are annotated at 2Hz with 3D bounding boxes.
- **p. 6 / 4.1. Datasets - extractive PDF cue:** We follow the official protocol to split the total scenes into train/val/test splits with 700/150/150 scenes.
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** The view transformer creates the 3D feature volume of size 128×128×16, with 128 channels.
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** The generated multi-scale 3D features are projected to 192 channels and processed the multiscale deformable self-attention with 6 layers.
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** The predicted occupancy is upsampled 2× to 256×256×32 for full-scale evaluation.
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** Unless specified, we train the model for 30 epochs on SemanticKITTI dataset and 24 epochs on nuScenes dataset.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | It indicates that the predicted semantic occupancy from TPVFormer, despite reasonable visualizations, fails to contain accurate 3D positions. | p. 9 (5. Conclusion) |
| body limitation/failure cue | Note that our method requires only one model to perform both the LiDAR segmentation and the semantic occupancy prediction, while the TPVFormer [21] model ... | p. 7 (4.4. Main Results) |
| body limitation/failure cue | Second, we remove the windowed attention in the global path, whose weights are shared with the local path, and observe a degradation of around ... | p. 9 (5. Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The transformer decoder mainly follows the implementation from Mask2Former [9]. | p. 6 (4.2. Implementation Details) |
| The learning rate is decayed by a multi-step scheduler. | p. 6 (4.2. Implementation Details) |
| 5, we compare different structures for the pixel decoder, which aims to fuse multi-scale features and generate the per-voxel mask embeddings. | p. 7 (4.5. Ablation Studies) |
| Also, our dual-path transformer encoder achieves a better trade-off than the vanilla 3D convolution and the 3D windowed attention proposed in [36]. | p. 7 (4.5. Ablation Studies) |
| Ablation on the Transformer Decoder. | p. 8 (4.5. Ablation Studies) |
| Therefore, we utilize the 6-layer multi-scale 3D deformable attention as the pixel decoder for OccFormer. | p. 8 (4.5. Ablation Studies) |
| Finally, the transformer occupancy decoder (Sec. | p. 2 (3.1. Overview) |
| The 3D feature is further processed by the dual-path transformer encoder (Sec. | p. 2 (3.1. Overview) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5. Conclusion - extractive PDF cue:** It indicates that the predicted semantic occupancy from TPVFormer, despite reasonable visualizations, fails to contain accurate 3D positions.
- **p. 7 / 4.4. Main Results - extractive PDF cue:** Note that our method requires only one model to perform both the LiDAR segmentation and the semantic occupancy prediction, while the TPVFormer [21] model trained ...
- **p. 9 / 5. Conclusion - extractive PDF cue:** Second, we remove the windowed attention in the global path, whose weights are shared with the local path, and observe a degradation of around 0.5 ...

- **PDF anchors reviewed:** datasets p. 5 (4.1. Datasets), p. 6 (4.1. Datasets), p. 6 (4.1. Datasets), p. 7 (4.4. Main Results), p. 8 (4.5. Ablation Studies), p. 5 (4.1. Datasets), metrics p. 7 (4.4. Main Results), p. 6 (4.3. Metrics), p. 7 (4.4. Main Results), p. 6 (4.2. Implementation Details), p. 5 (Figure/Table caption), p. 9 (Figure/Table caption), baselines p. 7 (4.4. Main Results), p. 6 (4.2. Implementation Details), p. 7 (4.5. Ablation Studies), p. 8 (4.6. Qualitative Results), p. 8 (4.5. Ablation Studies), p. 5 (Figure/Table caption), results p. 6 (4.1. Datasets), p. 7 (4.4. Main Results), p. 8 (4.5. Ablation Studies), p. 8 (4.6. Qualitative Results), p. 7 (4.5. Ablation Studies), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
