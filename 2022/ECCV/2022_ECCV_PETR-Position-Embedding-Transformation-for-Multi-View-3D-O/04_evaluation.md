# Evaluation - PETR: Position Embedding Transformation for Multi-View 3D Object Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.05625; PDF retrieval source: https://arxiv.org/pdf/2203.05625. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments)): Our method also achieves the best performance on both NDS and mAP.

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive body cue:** 4.1 Datasets and Metrics We validate our method on nuScenes benchmark [3].
- **p. 8 / 4 Experiments - extractive body cue:** The dataset has 1000 scenes and is officially divided into 700/150/150 scenes for training/validation/testing, respectively.
- **p. 9 / 4 Experiments - extractive body cue:** 2 shows the performance comparison on nuScenes test set.
- **p. 9 / 4 Experiments - extractive body cue:** Position Embedding Transformation for Multi-View 3D Object Detection 9 Table 1: Comparison of recent works on the nuScenes val set.
- **p. 10 / 4 Experiments - extractive body cue:** We guess the reason is that PETR learns the 3D correlation through global attention while DETR3D [51] perceives the 3D scene within local regions.
- **p. 11 / 4 Experiments - extractive body cue:** It indicates that 3D PE provides a strong position prior to perceive the 3D scene.
- **p. 12 / 4 Experiments - extractive body cue:** Original DETR ("None") directly employs a set of learnable parameters as object queries without anchor points.
- **p. 12 / 4 Experiments - extractive body cue:** The global feature of object query fail to make the model converge. "Fix-BEV" is the fixed anchor points are generated with the number of 39×39 ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method also achieves the best performance on both NDS and mAP. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | It shows that PETR achieves the best performance on both NDS and mAP metrics. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | PETR converges relatively slower than DETR3D [51] within the first 12 epochs and finally achieves much better detection performance. | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | In addition, the performance can be improved when we combine the 3D PE with both 2D PE and multi-view prior. | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The concatenation operation achieves similar performance compared to addition while surpassing the multiply fusion. | p. 12 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive body cue:** 4.1 Datasets and Metrics We validate our method on nuScenes benchmark [3].
- **p. 8 / 4 Experiments - extractive body cue:** The dataset has 1000 scenes and is officially divided into 700/150/150 scenes for training/validation/testing, respectively.
- **p. 9 / 4 Experiments - extractive body cue:** 2 shows the performance comparison on nuScenes test set.
- **p. 9 / 4 Experiments - extractive body cue:** Position Embedding Transformation for Multi-View 3D Object Detection 9 Table 1: Comparison of recent works on the nuScenes val set.
- **p. 10 / 4 Experiments - extractive body cue:** We guess the reason is that PETR learns the 3D correlation through global attention while DETR3D [51] perceives the 3D scene within local regions.
- **p. 11 / 4 Experiments - extractive body cue:** It indicates that 3D PE provides a strong position prior to perceive the 3D scene.
- **p. 12 / 4 Experiments - extractive body cue:** Original DETR ("None") directly employs a set of learnable parameters as object queries without anchor points.
- **p. 12 / 4 Experiments - extractive body cue:** The global feature of object query fail to make the model converge. "Fix-BEV" is the fixed anchor points are generated with the number of 39×39 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Comparison of DETR, DETR3D, and our proposed PETR. (a) In DETR, the object queries interact with 2D features to perform 2D detection. (b) ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2: The architecture of the proposed PETR paradigm. The multi-view images are input to the backbone network (e.g. ResNet) to extract the multi-view 2D ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Illustration of the proposed 3D Position Encoder. The multi-view 2D im- age features are input to a 1 × 1 convolution layer for ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: 3D position embedding similarity. The red points are selected positions in the front view. We calculated the similarity between the position embedding of ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Comparison of recent works on the nuScenes val set. The results of FCOS3D and PGD are fine-tuned and tested with test time augmentation. ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 5: Convergence and speed analysis on PETR. (a) The convergence compar- ison between PETR and DETR3D [51]. PETR converges slower at initial stage and ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: Comparison of recent works on the nuScenes test set. ∗are trained with external data. ‡ is test time augmentation. Methods Backbone NDS↑mAP↑mATE↓mASE↓mAOE↓mAVE↓mAAE↓ FCOS3D‡ ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 3: The impact of 3D Position Embedding. 2D PE is the common position embedding used in DETR. MV is multi-view position embedding to distinguish ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.1 Datasets and Metrics We validate our method on nuScenes benchmark [3]. | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Task/environment | The dataset has 1000 scenes and is officially divided into 700/150/150 scenes for training/validation/testing, respectively. | reset, timeout, object/scene variation | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3 Method), p. 5 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (3 Method), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Consistent with official evaluation metrics, we report nuScenes Detection Score (NDS) and mean Average Precision (mAP), along with mean Average Translation Error (mATE), mean ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| The score threshold is 0.25, while the backbone is ResNet-101. | definition/direction/unit from same section | p. 13 (4 Experiments) |
| Our method also achieves the best performance on both NDS and mAP. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| It shows that PETR achieves the best performance on both NDS and mAP metrics. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| When only using the 3D PE generated by 3D coordinates, PETR can directly achieve 30.5% mAP. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| 5(a) that the network with a simple MLP can improve the performance by 4.8% and 5.3% on NDS and mAP compared to the baseline ... | definition/direction/unit from same section | p. 12 (4 Experiments) |
| PE Networks NDS↑mAP↑mATE↓ None 0.311 0.256 1.00 1×1 ReLU 1×1 0.359 0.309 0.839 3×3 ReLU 3×3 0.017 0.000 1.054 (a) The network to generate ... | definition/direction/unit from same section | p. 12 (4 Experiments) |
| Fig. 7: Visualization of attention maps, generated from an object query (corre- sponding to the truck) on multi-view images. Both front-left and back-left views ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| It achieves state-of-the-art performance and can serve as a strong baseline for future research. | comparison identity and matched condition | p. 14 (4 Experiments) |
| 5(a) that the network with a simple MLP can improve the performance by 4.8% and 5.3% on NDS and mAP compared to the baseline ... | comparison identity and matched condition | p. 12 (4 Experiments) |
| Our method outperforms them 0.8% and 1.4% in NDS, respectively. | comparison identity and matched condition | p. 9 (4 Experiments) |
| 1, we first compare the performance with state-of-the-art methods on nuScenes val set. | comparison identity and matched condition | p. 9 (4 Experiments) |
| For the same image size (e.g., 1056×384), our PETR infers with 10.7 FPS compared to the BEVDet [18] with 4.2 FPS. | comparison identity and matched condition | p. 10 (4 Experiments) |
| The Uniform discretization (UD) shows similar performance compared to the linear-increasing discretization (LID). | comparison identity and matched condition | p. 12 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Depth Range (xmin, ymin, zmin, xmax, ymax, zmax) UD LID NDS↑mAP↑mATE↓ (1,51.2) (-51.2, -51.2, -10.0, 51.2, 51.2, 10.0) ✓ 0.352 0.303 0.862 (1,51.2) (-51.2, ... | component/input/data sensitivity | p. 11 (4 Experiments) |
| 5(c) shows the effect of different anchor points to generate queries. | component/input/data sensitivity | p. 12 (4 Experiments) |
| Here we first explore the effect of the multi-layer perception (MLP) that converts the 3D coordinates into 3D position embedding. | component/input/data sensitivity | p. 12 (4 Experiments) |
| All the experiments are conducted using single-level C5 feature of ResNet-50 backbone without the CBGS [57]. | component/input/data sensitivity | p. 11 (4 Experiments) |
| The results of FCOS3D and PGD are fine-tuned and tested with test time augmentation. | component/input/data sensitivity | p. 9 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our contributions are: - We propose a simple and elegant framework, termed PETR, for multi-view 3D object detection. | Our method also achieves the best performance on both NDS and mAP. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments) |
| Primary metric/result | It shows that PETR achieves the best performance on both NDS and mAP metrics. | numeric claim only at cited anchor | p. 9 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / 4 Experiments - extractive body cue:** The dataset has 1000 scenes and is officially divided into 700/150/150 scenes for training/validation/testing, respectively.
- **p. 8 / 4 Experiments - extractive body cue:** Each scene has 20s video frames and is fully annotated with 3D bounding boxes every 0.5s.
- **p. 8 / 4 Experiments - extractive body cue:** For 3D coordinates generation, we sample 64 points along the depth axis following the linear-increasing discretization (LID) in CaDDN [38].
- **p. 8 / 4 Experiments - extractive body cue:** All experiments are trained for 24 epochs (2x schedule) on 8 Tesla V100 GPUs with a batch size of 8.
- **p. 9 / 4 Experiments - extractive body cue:** For fair comparison with BEVDet [18], PETR with Swin-S backbone is also trained with an image size of 2112×768.
- **p. 10 / 4 Experiments - extractive body cue:** PETR converges relatively slower than DETR3D [51] within the first 12 epochs and finally achieves much better detection performance.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Finally, we provide some failure cases (see Fig. | p. 14 (4 Experiments) |
| body limitation/failure cue | We mark the failure cases by red and green circles. | p. 14 (4 Experiments) |
| body limitation/failure cue | The global feature of object query fail to make the model converge. "Fix-BEV" is the fixed anchor points are generated with the number of ... | p. 12 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All experiments are trained for 24 epochs (2x schedule) on 8 Tesla V100 GPUs with a batch size of 8. | p. 8 (4 Experiments) |
| The learning rate is initialized with 2.0 × 10-4 and decayed with cosine annealing policy [28]. | p. 8 (4 Experiments) |
| The FPS is measured on a single Tesla V100 GPU. | p. 10 (4 Experiments) |
| PETR converges relatively slower than DETR3D [51] within the first 12 epochs and finally achieves much better detection performance. | p. 10 (4 Experiments) |
| The 3D position encoder is used to encode the 3D position into the 2D features. | p. 12 (4 Experiments) |
| Fusion Ways NDS↑mAP↑mATE↓ Add 0.359 0.309 0.839 Concat 0.358 0.309 0.832 Multiply 0.357 0.303 0.848 (b) Different ways to fuse the 2D multiview features ... | p. 12 (4 Experiments) |
| The 3D features are further input to the transformer decoder and interact with the object queries, generated from query generator. | p. 4 (3 Method) |
| The 3D coordinates together with the 2D multiview features are input to the 3D position encoder, producing the 3D positionaware features F 3d = ... | p. 4 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 4 Experiments - extractive body cue:** Finally, we provide some failure cases (see Fig.
- **p. 14 / 4 Experiments - extractive body cue:** We mark the failure cases by red and green circles.
- **p. 12 / 4 Experiments - extractive body cue:** The global feature of object query fail to make the model converge. "Fix-BEV" is the fixed anchor points are generated with the number of 39×39 ...

- **Evidence anchors reviewed:** datasets p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), metrics p. 8 (4 Experiments), p. 13 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), baselines p. 14 (4 Experiments), p. 12 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 12 (4 Experiments), results p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
