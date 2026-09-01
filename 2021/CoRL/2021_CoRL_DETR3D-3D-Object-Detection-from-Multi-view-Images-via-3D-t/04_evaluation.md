# Evaluation - DETR3D: 3D Object Detection from Multi-view Images via 3D-to-2D Queries

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2110.06922; PDF retrieval source: https://arxiv.org/pdf/2110.06922. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 5 (4 Experiments), p. 3 (Figure/Table caption)): We also provide quantitative results in Table 5, which shows that iterative refinement indeed improves performance significantly.

## Evaluation Body Digest

- **p. 5 / 4 Experiments - extractive PDF cue:** We test our method on the nuScenes dataset [33]. nuScenes consists of 1,000 sequences; each sequence is roughly 20s long, with a sampling rate of ...
- **p. 5 / 4 Experiments - extractive PDF cue:** We present our results as follows: first, we detail the dataset, metrics, and implementation in §4.1; then we compare our method to existing works in ...
- **p. 7 / 4 Experiments - extractive PDF cue:** On the nuScenes dataset, there are no publicly available pseudo-LiDAR works for us to make a direct comparison.
- **p. 6 / 4 Experiments - extractive PDF cue:** For evaluation, we use the nuScenes evalutation toolkit.
- **p. 6 / 4 Experiments - extractive PDF cue:** Our method is robust to the usage of NMS. ∗: CenterNet uses a customized backbone DLA [38]. ‡: this model is trained with depth weight ...
- **p. 7 / 4 Experiments - extractive PDF cue:** We visualize bounding boxes decoded from the object queries in each layer.
- **p. 7 / 4 Experiments - extractive PDF cue:** One possible explanation is that pseudoLiDAR object detectors suffer from compounding errors introduced by inaccurate depth prediction, that in turn is known to overfit to ...
- **p. 5 / 4 Experiments - extractive PDF cue:** We evaluate average translation error (ATE), average scale error (ASE), average orientation error (AOE), average velocity error (AVE), and average attribute error (AAE).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We also provide quantitative results in Table 5, which shows that iterative refinement indeed improves performance significantly. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Furthermore, we provide ablations on the number of object queries in Table 6; increasing the number queries consistently improves the performance until it gets ... | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 1, our method outperforms these methods even though we do not use any post-processing. | p. 6 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | On the test set (Table 2), our method outperforms all existing methods as of 10/13/2021; our method uses the same backbone as DD3D [37] ... | p. 6 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We present our results as follows: first, we detail the dataset, metrics, and implementation in §4.1; then we compare our method to existing works ... | p. 5 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 4 Experiments - extractive PDF cue:** We test our method on the nuScenes dataset [33]. nuScenes consists of 1,000 sequences; each sequence is roughly 20s long, with a sampling rate of ...
- **p. 5 / 4 Experiments - extractive PDF cue:** We present our results as follows: first, we detail the dataset, metrics, and implementation in §4.1; then we compare our method to existing works in ...
- **p. 7 / 4 Experiments - extractive PDF cue:** On the nuScenes dataset, there are no publicly available pseudo-LiDAR works for us to make a direct comparison.
- **p. 6 / 4 Experiments - extractive PDF cue:** For evaluation, we use the nuScenes evalutation toolkit.
- **p. 6 / 4 Experiments - extractive PDF cue:** Our method is robust to the usage of NMS. ∗: CenterNet uses a customized backbone DLA [38]. ‡: this model is trained with depth weight ...
- **p. 7 / 4 Experiments - extractive PDF cue:** We visualize bounding boxes decoded from the object queries in each layer.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1: Overview of our method. The inputs to the model are a set of multi-view images, which are encoded by a ResNet and a ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Comparisons to recent works on the validation set. Our method is robust to the usage of NMS. ∗: CenterNet uses a customized backbone ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2: Comparisons to top-performing works on the test set from the leaderboard. #: initialized from a DD3D checkpoint. †: initialized from a backbone pre-trained ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3: Comparisons in Overlap Region. ‡: this model is trained with depth weight 1.0 and initial- ized from a FCOS3D checkpoint; the checkpoint is ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4: Comparisons to pseudo-LiDAR Methods.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5: Evaluation on detection results from different layers. Layer ↑ NDS ↑ mAP ↑ mATE ↓ mASE ↓ mAOE ↓ mAVE ↓
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 2: Detection results from layer 1 to layer 5 in the DETR3D head. We visualize the bounding boxes in the BEV and overlay the ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 6: Results with different number of queries. # queries 30 100 300 600 900 1200

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We test our method on the nuScenes dataset [33]. nuScenes consists of 1,000 sequences; each sequence is roughly 20s long, with a sampling rate ... | embodiment, simulator version and control stack | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Task/environment | We present our results as follows: first, we detail the dataset, metrics, and implementation in §4.1; then we compare our method to existing works ... | reset, timeout, object/scene variation | p. 5 (4 Experiments), p. 7 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| One possible explanation is that pseudoLiDAR object detectors suffer from compounding errors introduced by inaccurate depth prediction, that in turn is known to overfit ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| We evaluate average translation error (ATE), average scale error (ASE), average orientation error (AOE), average velocity error (AVE), and average attribute error (AAE). | definition/direction/unit from same section | p. 5 (4 Experiments) |
| To capture all aspects of the detection task, a consolidated scalar metric-the nuScenes Detection Score (NDS) [33]-is defined as NDS = 1 10[5mAP + ... | definition/direction/unit from same section | p. 5 (4 Experiments) |
| However, our method still exhibits substantial translation error (in line with results in Table 4.2): Although our model avoids explicit depth prediction, depth estimation ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Figure 2: Detection results from layer 1 to layer 5 in the DETR3D head. We visualize the bounding boxes in the BEV and overlay ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| This confirms that our integrated prediction approach is more effective. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| Also, FCOS3D uses disentangled heads for different bounding box parameters, which can increase performance. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| Figure 1: Overview of our method. The inputs to the model are a set of multi-view images, which are encoded by a ResNet and ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 4.2 Comparison to Existing Works We compare to previous state-of-the-art methods CenterNet [1] and FCOS3D [2]. | comparison identity and matched condition | p. 6 (4 Experiments) |
| On the test set (Table 2), our method outperforms all existing methods as of 10/13/2021; our method uses the same backbone as DD3D [37] ... | comparison identity and matched condition | p. 6 (4 Experiments) |
| Hence, we implement a baseline ourselves to verify that our approach is more effective than explicit depth prediction. | comparison identity and matched condition | p. 7 (4 Experiments) |
| We also experimented with a self-supervised PackNet model with velocity supervision (as in the original paper), but we found that ground-truth depth supervision yielded ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| Figure 1: Overview of our method. The inputs to the model are a set of multi-view images, which are encoded by a ResNet and ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| We present our results as follows: first, we detail the dataset, metrics, and implementation in §4.1; then we compare our method to existing works ... | comparison identity and matched condition | p. 5 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1: Overview of our method. The inputs to the model are a set of multi-view images, which are encoded by a ResNet and ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| We present our results as follows: first, we detail the dataset, metrics, and implementation in §4.1; then we compare our method to existing works ... | component/input/data sensitivity | p. 5 (4 Experiments) |
| To perform multi-view object detection, these methods have to process each image independently, and use both per-image and global NMS to remove redundant boxes ... | component/input/data sensitivity | p. 6 (4 Experiments) |
| Conceptually, this pipeline is a variant of pseudo-LiDAR [42]. | component/input/data sensitivity | p. 7 (4 Experiments) |
| 4.5 Ablation & Analysis We provide a visualization of object query refinement in Figure 2. | component/input/data sensitivity | p. 7 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We summarize our key contributions as follows: • We present a streamlined 3D object detection model from RGB images. | We also provide quantitative results in Table 5, which shows that iterative refinement indeed improves performance significantly. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 5 (4 Experiments), p. 3 (Figure/Table caption) |
| Primary metric/result | Furthermore, we provide ablations on the number of object queries in Table 6; increasing the number queries consistently improves the performance until it gets ... | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / 4 Experiments - extractive PDF cue:** We test our method on the nuScenes dataset [33]. nuScenes consists of 1,000 sequences; each sequence is roughly 20s long, with a sampling rate of ...
- **p. 5 / 4 Experiments - extractive PDF cue:** Camera parameters including intrinsics and extrinsics are available. nuScenes provides annotations every 0.5s; in total there are 28k, 6k, and 6k annotated samples for training, ...
- **p. 5 / 4 Experiments - extractive PDF cue:** The DETR3D detection head consists of 6 layers, where each layer is a combination of a feature refinement step and a multi-head attention layer.
- **p. 5 / 4 Experiments - extractive PDF cue:** The model is trained for 12 epochs in total on 8 RTX 3090 GPUs and the per-GPU batch size is 1.
- **p. 6 / 4 Experiments - extractive PDF cue:** Method NDS ↑ mAP ↑ mATE ↓ mASE ↓ mAOE ↓ mAVE ↓ mAAE ↓ NMS Mono3D 0.429 0.366 0.642 0.252 0.523 1.591 0.119 N/A ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Some failure cases include the far ahead car in CAM FRONT, that was not detected. | p. 9 (5 Conclusion) |
| body limitation/failure cue | To further demonstrate the advantages of fused inference, we calculate the metrics for boxes falling into the camera overlaps. | p. 6 (4 Experiments) |
| body limitation/failure cue | Furthermore, the new detection head is input-agnostic, and including other modalities such as LiDAR/RADAR would enhance performance and robustness. | p. 8 (5 Conclusion) |
| body limitation/failure cue | Our method is robust to the usage of NMS. ∗: CenterNet uses a customized backbone DLA [38]. ‡: this model is trained with depth ... | p. 6 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The model is trained for 12 epochs in total on 8 RTX 3090 GPUs and the per-GPU batch size is 1. | p. 5 (4 Experiments) |
| We use an initial learning rate 10-4, which is decreased to 10-5 and 10-6 at 8th and 11th epochs. | p. 5 (4 Experiments) |
| Our method is robust to the usage of NMS. ∗: CenterNet uses a customized backbone DLA [38]. ‡: this model is trained with depth ... | p. 6 (4 Experiments) |
| To compute the metrics, we select boxes whose 3D center is visible to multiple cameras. | p. 6 (4 Experiments) |
| We visualize bounding boxes decoded from the object queries in each layer. | p. 7 (4 Experiments) |
| These methods require several post-processing steps to fuse predictions across cameras and to remove redundant boxes, yielding a steep trade-off between efficiency and effectiveness. | p. 1 (1 Introduction) |
| In the camera overlap regions, our method outperforms others by a substantial margin. • We release our code to facilitate reproducibility and future research. | p. 2 (1 Introduction) |
| To gather scene-specific information, we back-project a set of reference points decoded from these object priors to each camera and fetch the corresponding image ... | p. 2 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5 Conclusion - extractive PDF cue:** Some failure cases include the far ahead car in CAM FRONT, that was not detected.
- **p. 6 / 4 Experiments - extractive PDF cue:** To further demonstrate the advantages of fused inference, we calculate the metrics for boxes falling into the camera overlaps.
- **p. 8 / 5 Conclusion - extractive PDF cue:** Furthermore, the new detection head is input-agnostic, and including other modalities such as LiDAR/RADAR would enhance performance and robustness.
- **p. 6 / 4 Experiments - extractive PDF cue:** Our method is robust to the usage of NMS. ∗: CenterNet uses a customized backbone DLA [38]. ‡: this model is trained with depth weight ...

- **PDF anchors reviewed:** datasets p. 5 (4 Experiments), p. 5 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), metrics p. 7 (4 Experiments), p. 5 (4 Experiments), p. 5 (4 Experiments), p. 7 (4 Experiments), p. 8 (Figure/Table caption), p. 6 (4 Experiments), baselines p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 3 (Figure/Table caption), p. 5 (4 Experiments), results p. 7 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 5 (4 Experiments), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
