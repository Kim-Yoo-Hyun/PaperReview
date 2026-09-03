# Evaluation - BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.17270; PDF retrieval source: https://arxiv.org/pdf/2203.17270. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (Figure/Table caption), p. 11 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 11 (Figure/Table caption), p. 9 (Figure/Table caption)): Figure 3: The detection results of subsets with different visibilities. We divide the nuScenes val set into four subsets based on the visibility that {0-40%, 40-60%, 60-80%, 80-100%} of objects ...

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive body cue:** The nuScenes dataset [4] contains 1000 scenes of roughly 20s duration each, and the key samples are annotated at 2Hz.
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Datasets We conduct experiments on two challenging public autonomous driving datasets, namely nuScenes dataset [4] and Waymo open dataset [40].
- **p. 17 / A.4 Spatial Cross-Attention - extractive body cue:** 0.517 0.511 0.494 0.471 0.443 0.508 0.505 0.494 0.479 0.463 0.448 0.442 0.424 0.402 0.380 0.404 0.400 0.397 0.392 0.388 0.423 0.414 0.395 0.373 0.350 ...
- **p. 16 / A.2 VPN and Lift-Splat - extractive body cue:** The backbone and the task heads are the same as the BEVFomer for fair comparisons.
- **p. 16 / A.3 Task Heads - extractive body cue:** Following [47], we use 900 object queries and keep 300 predicted boxes with highest confidence scores during inference.
- **p. 7 / 4 Experiments - extractive body cue:** The mean average precision (mAP) of nuScenes is computed using the center distance on the ground plane rather than the 3D Intersection over Union (IoU) ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 3: The detection results of subsets with different visibilities. We divide the nuScenes val set into four subsets based on the visibility that {0-40%, ...
- **p. 7 / 4 Experiments - extractive body cue:** We use the thresholds of 0.5 and 0.7 for 3D IoU to compute the mAP on Waymo dataset.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7); A Implementation Details (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 3: The detection results of subsets with different visibilities. We divide the nuScenes val set into four subsets based on the visibility that ... | p. 10 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 4: Visualization results of BEVFormer on nuScenes val set. We show the 3D bboxes predictions in multi-camera images and the bird's-eye-view. predicted boxes ... | p. 11 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | On the test set, our model achieves 56.9% NDS without bells and whistles, 9.0 points 7 | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method outperforms previous best method DETR3D [47] over 9.2 points on val set (51.7% NDS vs. | p. 7 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Tab. 6. We ablate the scales of BEVFormer in three aspects, including whether to use multi-scale view features, the shape of BEV queries, and ... | p. 11 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive body cue:** The nuScenes dataset [4] contains 1000 scenes of roughly 20s duration each, and the key samples are annotated at 2Hz.
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Datasets We conduct experiments on two challenging public autonomous driving datasets, namely nuScenes dataset [4] and Waymo open dataset [40].
- **p. 17 / A.4 Spatial Cross-Attention - extractive body cue:** 0.517 0.511 0.494 0.471 0.443 0.508 0.505 0.494 0.479 0.463 0.448 0.442 0.424 0.402 0.380 0.404 0.400 0.397 0.392 0.388 0.423 0.414 0.395 0.373 0.350 ...
- **p. 16 / A.2 VPN and Lift-Splat - extractive body cue:** The backbone and the task heads are the same as the BEVFomer for fair comparisons.
- **p. 16 / A.3 Task Heads - extractive body cue:** Following [47], we use 900 object queries and keep 300 predicted boxes with highest confidence scores during inference.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We propose BEVFormer, a paradigm for autonomous driving that applies both Transformer and Temporal structure to generate bird's-eye-view (BEV) features from multi-camera inputs. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overall architecture of BEVFormer. (a) The encoder layer of BEVFormer contains grid-shaped BEV queries, temporal self-attention, and spatial cross-attention. (b) In spatial cross- ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: 3D detection results on nuScenes test set. ∗notes that VoVNet-99 (V2-99) [21] was pre-trained on the depth estimation task with extra data [31]. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: 3D detection results on nuScenes val set. "C" indicates Camera.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: 3D detection results on Waymo val set under Waymo evaluation metric and nuScenes evaluation metric. "L1" and "L2" refer "LEVEL_1" and "LEVEL_2" difficulties ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: 3D detection and map segmentation results on nuScenes val set. Comparison of training segmentation and detection tasks jointly or not. *: We use ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 5: The detection results of different methods with various BEV encoders on nuScenes val set. "Memory" is the consumed GPU memory during training. *: ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 3: The detection results of subsets with different visibilities. We divide the nuScenes val set into four subsets based on the visibility that {0-40%, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The nuScenes dataset [4] contains 1000 scenes of roughly 20s duration each, and the key samples are annotated at 2Hz. | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | 4.1 Datasets We conduct experiments on two challenging public autonomous driving datasets, namely nuScenes dataset [4] and Waymo open dataset [40]. | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 17 (A.4 Spatial Cross-Attention) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (1 Introduction), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The mean average precision (mAP) of nuScenes is computed using the center distance on the ground plane rather than the 3D Intersection over Union ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Figure 3: The detection results of subsets with different visibilities. We divide the nuScenes val set into four subsets based on the visibility that ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| We use the thresholds of 0.5 and 0.7 for 3D IoU to compute the mAP on Waymo dataset. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Following [47], we use 900 object queries and keep 300 predicted boxes with highest confidence scores during inference. | definition/direction/unit from same section | p. 16 (A.3 Task Heads) |
| Table 3: 3D detection results on Waymo val set under Waymo evaluation metric and nuScenes evaluation metric. "L1" and "L2" refer "LEVEL_1" and "LEVEL_2" ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Method Modality Backbone NDS↑mAP↑mATE↓mASE↓mAOE↓mAVE↓mAAE↓ SSN [55] L - 0.569 0.463 - - - - - CenterPoint-Voxel [52] L - 0.655 0.580 - - - ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Figure 4: Visualization results of BEVFormer on nuScenes val set. We show the 3D bboxes predictions in multi-camera images and the bird's-eye-view. predicted boxes ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| 5, for each class of the semantic map, we follow the mask decoder in [22] to use one learnable query to represent this class, ... | definition/direction/unit from same section | p. 16 (A.3 Task Heads) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method outperforms previous best method DETR3D [47] over 9.2 points on val set (51.7% NDS vs. | comparison identity and matched condition | p. 7 (4 Experiments) |
| 4.3 3D Object Detection Results We train our model on the detection task with the detection head only for fairly comparing with previous state-of-the-art ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| Figure 3: The detection results of subsets with different visibilities. We divide the nuScenes val set into four subsets based on the visibility that ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| Figure 4: Visualization results of BEVFormer on nuScenes val set. We show the 3D bboxes predictions in multi-camera images and the bird's-eye-view. predicted boxes ... | comparison identity and matched condition | p. 11 (Figure/Table caption) |
| Tab. 6. We ablate the scales of BEVFormer in three aspects, including whether to use multi-scale view features, the shape of BEV queries, and ... | comparison identity and matched condition | p. 11 (Figure/Table caption) |
| We use VPN [30] and Lift-Splat [32] as two baselines in this work. | comparison identity and matched condition | p. 16 (A.2 VPN and Lift-Splat) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To eliminate the effect of task heads and compare other BEV generating methods fairly, we use VPN [30] and Lift-Splat [32] to replace our ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| On the test set, our model achieves 56.9% NDS without bells and whistles, 9.0 points 7 | component/input/data sensitivity | p. 7 (4 Experiments) |
| Table 8: Ablation Experiments on nuScenes val set. "A." indicates aligning history BEV fea- tures with ego-motion. "R." indicates randomly sampling 4 frames from ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |
| Table 5: The detection results of different methods with various BEV encoders on nuScenes val set. "Memory" is the consumed GPU memory during training. ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| Table 4: 3D detection and map segmentation results on nuScenes val set. Comparison of training segmentation and detection tasks jointly or not. *: We ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are as follows: • We propose BEVFormer, a spatiotemporal transformer encoder that projects multi-camera and/or timestamp input to BEV representations. | Figure 3: The detection results of subsets with different visibilities. We divide the nuScenes val set into four subsets based on the visibility that ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (Figure/Table caption), p. 11 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 11 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Primary metric/result | Figure 4: Visualization results of BEVFormer on nuScenes val set. We show the 3D bboxes predictions in multi-camera images and the bird's-eye-view. predicted boxes ... | numeric claim only at cited anchor | p. 11 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** The nuScenes dataset [4] contains 1000 scenes of roughly 20s duration each, and the key samples are annotated at 2Hz.
- **p. 7 / 4 Experiments - extractive body cue:** For experiments on nuScenes, the default size of BEV queries is 200×200, the perception ranges are [-51.2m, 51.2m] for the X and Y axis and ...
- **p. 7 / 4 Experiments - extractive body cue:** For each local query, during the spatial cross-attention module implemented by deformable attention mechanism, it corresponds to Nref =4 target points with different heights in ...
- **p. 7 / 4 Experiments - extractive body cue:** By default, we train our models with 24 epochs, a learning rate of 2×10-4.
- **p. 7 / 4 Experiments - extractive body cue:** Due to the camera system of Waymo can not capture the whole scene around the ego car [40], the default spatial shape of BEV queries ...
- **p. 7 / 4 Experiments - extractive body cue:** Our method outperforms previous best method DETR3D [47] over 9.2 points on val set (51.7% NDS vs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 1: 3D detection results on nuScenes test set. ∗notes that VoVNet-99 (V2-99) [21] was pre-trained on the depth estimation task with extra data ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | However, the jointly trained model does not perform as well as individually trained models for road and lane segmentation, which is a common phenomenon ... | p. 9 (C R101) |
| body limitation/failure cue | Temporal information does not work to benefit an object's scale prediction. attention significantly outperforms other attention mechanisms under a comparable model scale. | p. 10 (C R101) |
| body limitation/failure cue | The most straightforward way to employ global attention is making each BEV query interact with all multi-camera features, and this conceptual implementation does not ... | p. 16 (A.4 Spatial Cross-Attention) |
| body limitation/failure cue | To evaluate the performance of BEVFormer on objects with different occlusion levels, we divide the validation set of nuScenes into four subsets according to ... | p. 10 (C R101) |
| body limitation/failure cue | Notably, compared to other attention mechanisms that rely on precise camera intrinsic and extrinsic, global attention is more robust to camera calibration. | p. 16 (A.4 Spatial Cross-Attention) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Following previous methods [47, 56], we train all models with 24 epochs, a batch size of 1 (containing 6 view images) per GPU, a ... | p. 16 (A.1 Traning Strategy) |
| We use the thresholds of 0.5 and 0.7 for 3D IoU to compute the mAP on Waymo dataset. | p. 7 (4 Experiments) |
| The input BEV features Bt-1 for each encoder layer are the same and require no gradients. | p. 7 (4 Experiments) |
| We employ the official codes1 in this work. | p. 16 (A.2 VPN and Lift-Splat) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: 3D detection results on nuScenes test set. ∗notes that VoVNet-99 (V2-99) [21] was pre-trained on the depth estimation task with extra data [31]. ...
- **p. 9 / C R101 - extractive body cue:** However, the jointly trained model does not perform as well as individually trained models for road and lane segmentation, which is a common phenomenon called ...
- **p. 10 / C R101 - extractive body cue:** Temporal information does not work to benefit an object's scale prediction. attention significantly outperforms other attention mechanisms under a comparable model scale.
- **p. 16 / A.4 Spatial Cross-Attention - extractive body cue:** The most straightforward way to employ global attention is making each BEV query interact with all multi-camera features, and this conceptual implementation does not require ...
- **p. 10 / C R101 - extractive body cue:** To evaluate the performance of BEVFormer on objects with different occlusion levels, we divide the validation set of nuScenes into four subsets according to the ...
- **p. 16 / A.4 Spatial Cross-Attention - extractive body cue:** Notably, compared to other attention mechanisms that rely on precise camera intrinsic and extrinsic, global attention is more robust to camera calibration.

- **Evidence anchors reviewed:** datasets p. 7 (4 Experiments), p. 7 (4 Experiments), p. 17 (A.4 Spatial Cross-Attention), p. 16 (A.2 VPN and Lift-Splat), p. 16 (A.3 Task Heads), metrics p. 7 (4 Experiments), p. 10 (Figure/Table caption), p. 7 (4 Experiments), p. 16 (A.3 Task Heads), p. 9 (Figure/Table caption), p. 8 (4 Experiments), baselines p. 7 (4 Experiments), p. 7 (4 Experiments), p. 10 (Figure/Table caption), p. 11 (Figure/Table caption), p. 11 (Figure/Table caption), p. 16 (A.2 VPN and Lift-Splat), results p. 10 (Figure/Table caption), p. 11 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 11 (Figure/Table caption), p. 9 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
