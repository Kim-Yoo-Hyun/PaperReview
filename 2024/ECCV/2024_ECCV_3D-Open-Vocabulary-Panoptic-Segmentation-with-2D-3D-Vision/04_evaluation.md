# Evaluation - 3D Open-Vocabulary Panoptic Segmentation with 2D-3D Vision-Language Distillation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5642_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (4 Experiments), p. 11 (4 Experiments), p. 13 (Figure/Table caption), p. 12 (Figure/Table caption), p. 9 (4 Experiments), p. 9 (4 Experiments)): Our method significantly outperforms

## Evaluation Body Digest

- **p. 9 / 4 Experiments - extractive body cue:** The nuScenes dataset [4] is a public benchmark for autonomous driving.
- **p. 9 / 4 Experiments - extractive body cue:** Both the nuScenes and SemanticKITTI datasets do not provide official base and novel class splits.
- **p. 10 / 4 Experiments - extractive body cue:** Comparisons on the nuScenes and SemanticKITTI datasets are shown in Tab.
- **p. 10 / 4 Experiments - extractive body cue:** 3: Open-vocabulary panoptic segmentation results from PFC and our method on nuScenes.
- **p. 11 / 4 Experiments - extractive body cue:** Model Type Supervision PQ PQT h N PQSt N RQ RQT h N RQSt N SQ SQT h N SQSt N mIoU P3Former [47] closed-set ...
- **p. 11 / 4 Experiments - extractive body cue:** We show that this is due to lack of supervision of the whole scene as P3Former achieves similar performance when only trained on base categories.
- **p. 9 / 4 Experiments - extractive body cue:** During inference, if there are multiple labels for one class, we derive the class score by getting the maximum scores among these labels.
- **p. 9 / 4 Experiments - extractive body cue:** \u nderbrace {\frac {\sum _{\TP } \text {IoU}} {/\TP /}}_{\text {SQ}} \times \underbrace {\frac {/\TP /}{/\TP / + \frac {1}{2} /\FP / + \frac {1}{2} ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method significantly outperforms | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We show that this is due to lack of supervision of the whole scene as P3Former achieves similar performance when only trained on base ... | p. 11 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 5: Performance on a different split. We compare the performance with a split with 5 novel classes (B11/N5). The novel things classes are ... | p. 13 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 4: Impact of each component. We evaluate the impact of each component using the base/novel split in Tab. 1. We observe that each ... | p. 12 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | During inference, if there are multiple labels for one class, we derive the class score by getting the maximum scores among these labels. | p. 9 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 9 / 4 Experiments - extractive body cue:** The nuScenes dataset [4] is a public benchmark for autonomous driving.
- **p. 9 / 4 Experiments - extractive body cue:** Both the nuScenes and SemanticKITTI datasets do not provide official base and novel class splits.
- **p. 10 / 4 Experiments - extractive body cue:** Comparisons on the nuScenes and SemanticKITTI datasets are shown in Tab.
- **p. 10 / 4 Experiments - extractive body cue:** 3: Open-vocabulary panoptic segmentation results from PFC and our method on nuScenes.
- **p. 11 / 4 Experiments - extractive body cue:** Model Type Supervision PQ PQT h N PQSt N RQ RQT h N RQSt N SQ SQT h N SQSt N mIoU P3Former [47] closed-set ...
- **p. 11 / 4 Experiments - extractive body cue:** We show that this is due to lack of supervision of the whole scene as P3Former achieves similar performance when only trained on base categories.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of our method. Given a LiDAR point cloud and the corresponding camera images, LiDAR features are extracted with a learnable LiDAR encoder, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 2: (a) the proposed object-level distillation loss, and (b) the proposed voxel-level distillation loss. 3.3
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 3: Open-vocabulary panoptic segmentation results from PFC and our method on nuScenes. PFC predicts inaccurate category and masks for the novel pedestrian (red), bus ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 1: Quantitative results of panoptic segmentation on nuScenes. We compare the performance of open-vocabulary and fully supervised models. All open vocabulary models share the ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 2: Performance for base classes on nuScenes. We report the performance on base classes for models in Tab. 1. A gap still exists between ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3: Quantitative results of panoptic segmentation on SemanticKITTI. We compare the performance different models. All open vocabulary models share the same randomly picked base/novel ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Impact of each component. We evaluate the impact of each component using the base/novel split in Tab. 1. We observe that each component ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 5: Performance on a different split. We compare the performance with a split with 5 novel classes (B11/N5). The novel things classes are bicycle, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The nuScenes dataset [4] is a public benchmark for autonomous driving. | embodiment, simulator version and control stack | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Task/environment | Both the nuScenes and SemanticKITTI datasets do not provide official base and novel class splits. | reset, timeout, object/scene variation | p. 9 (4 Experiments), p. 10 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3 Method), p. 5 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (3 Method), p. 6 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| During inference, if there are multiple labels for one class, we derive the class score by getting the maximum scores among these labels. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| \u nderbrace {\frac {\sum _{\TP } \text {IoU}} {/\TP /}}_{\text {SQ}} \times \underbrace {\frac {/\TP /}{/\TP / + \frac {1}{2} /\FP / + \frac ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| In summary, this baseline provides a comparison against our proposed method without the multimodal feature fusion module, the unified segmentation head, and the distillation ... | definition/direction/unit from same section | p. 10 (4 Experiments) |
| PFC predicts inaccurate category and masks for the novel pedestrian (red), bus (yellow) and vegetation (green), while ours makes correct predictions. report PQ, RQ, ... | definition/direction/unit from same section | p. 10 (4 Experiments) |
| We report the performance on base classes for models in Tab. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| We compare the performance of open-vocabulary and fully supervised models. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Fig. 2: (a) the proposed object-level distillation loss, and (b) the proposed voxel-level distillation loss. 3.3 | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 5: Performance on a different split. We compare the performance with a split with 5 novel classes (B11/N5). The novel things classes are ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 4.3 Main Results Since there are no existing methods for the 3D open-vocabulary panoptic segmentation task, we mainly compare with three methods to demonstrate ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| In summary, this baseline provides a comparison against our proposed method without the multimodal feature fusion module, the unified segmentation head, and the distillation ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| Table 5: Performance on a different split. We compare the performance with a split with 5 novel classes (B11/N5). The novel things classes are ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| 4.1 Experimental Setting Following the state-of-the-art closed-set 3D panoptic segmentation work [27,40, 42,47,52,58], we conduct experiments and ablation studies on the nuScenes [4] and ... | comparison identity and matched condition | p. 9 (4 Experiments) |
| Following the most recent state-of-the-art model P3Former [47], we evaluate the models on the validation set(6019 frames). | comparison identity and matched condition | p. 9 (4 Experiments) |
| Table 4: Impact of each component. We evaluate the impact of each component using the base/novel split in Tab. 1. We observe that each ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We use the same splits in the main comparison with prior methods, and provide the results of more variations in the ablation studies and ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| 4.1 Experimental Setting Following the state-of-the-art closed-set 3D panoptic segmentation work [27,40, 42,47,52,58], we conduct experiments and ablation studies on the nuScenes [4] and ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| In summary, this baseline provides a comparison against our proposed method without the multimodal feature fusion module, the unified segmentation head, and the distillation ... | component/input/data sensitivity | p. 10 (4 Experiments) |
| Table 4: Impact of each component. We evaluate the impact of each component using the base/novel split in Tab. 1. We observe that each ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: - We present the first approach for 3D open-vocabulary panoptic segmentation in autonomous driving. - We propose two ... | Our method significantly outperforms | PDF body cue; verify exact table/figure and matched conditions | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 13 (Figure/Table caption), p. 12 (Figure/Table caption), p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Primary metric/result | We show that this is due to lack of supervision of the whole scene as P3Former achieves similar performance when only trained on base ... | numeric claim only at cited anchor | p. 11 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 9 / 4 Experiments - extractive body cue:** We use all key frames with panoptic labels in the training set(28130 frames) to train the model.
- **p. 9 / 4 Experiments - extractive body cue:** Following the most recent state-of-the-art model P3Former [47], we evaluate the models on the validation set(6019 frames).
- **p. 9 / 4 Experiments - extractive body cue:** The models are trained for 40 epochs, and we use the checkpoint of the last epoch for evaluation.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We experimentally verified that simply extending the 2D open-vocabulary segmentation method into 3D does not yield good performance, and demonstrated that our proposed model ... | p. 14 (5 Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The models are trained for 40 epochs, and we use the checkpoint of the last epoch for evaluation. | p. 9 (4 Experiments) |
| We set the initial learning rate as 0.0008 with a multi-step decay schedule. | p. 9 (4 Experiments) |
| 3.4 Implementation Details For the LiDAR encoder and segmentation head, we follow the implementation of the state-of-the-art closed-set 3D panoptic segmentation method P3Former [47]. | p. 8 (3 Method) |
| More implementation details for this baseline can be found in the supplementary material. | p. 5 (3 Method) |
| The LiDAR encoder is a model which takes an unordered set of points as input and extracts per-point features. | p. 5 (3 Method) |
| Finally, the learned per-voxel LiDAR features and frozen per-voxel vision CLIP features are concatenated together to be used as input into the transformer decoder ... | p. 6 (3 Method) |
| The predicted class logits are then computed from the cosine similarity between the predicted class embedding and the text embedding of every category name ... | p. 6 (3 Method) |
| For the Text CLIP encoder, we use CLIP [39] with ViT-L/14 [45] backbone, following other state-of-the-art open vocabulary works [35]. | p. 8 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 5 Conclusion - extractive body cue:** We experimentally verified that simply extending the 2D open-vocabulary segmentation method into 3D does not yield good performance, and demonstrated that our proposed model design ...

- **Evidence anchors reviewed:** datasets p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), metrics p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), baselines p. 10 (4 Experiments), p. 10 (4 Experiments), p. 13 (Figure/Table caption), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 12 (Figure/Table caption), results p. 10 (4 Experiments), p. 11 (4 Experiments), p. 13 (Figure/Table caption), p. 12 (Figure/Table caption), p. 9 (4 Experiments), p. 9 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
