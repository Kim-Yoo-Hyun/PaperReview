# Evaluation - PointPillars: Fast Encoders for Object Detection from Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1812.05784; PDF retrieval source: https://arxiv.org/pdf/1812.05784. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Figure/Table caption), p. 6 (5. Results), p. 6 (5. Results), p. 8 (Figure/Table caption), p. 5 (4.2. Settings), p. 4 (Figure/Table caption)): Figure 1. Bird's eye view performance vs speed for our proposed PointPillars, PP method on the KITTI [5] test set. Lidar-only methods drawn as blue circles; lidar & vision methods ...

## Evaluation Body Digest

- **p. 5 / 4.1. Dataset - extractive body cue:** All experiments use the KITTI object detection benchmark dataset [5], which consists of samples that have both lidar point clouds and images.
- **p. 5 / 4.1. Dataset - extractive body cue:** The KITTI benchmark requires detections of cars, pedestrians, and cyclists.
- **p. 6 / 5. Results - extractive body cue:** The KITTI dataset is stratified into easy, moderate, and hard difficulties, and the official KITTI leaderboard is ranked by performance on moderate.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Bird's eye view performance vs speed for our proposed PointPillars, PP method on the KITTI [5] test set. Lidar-only methods drawn as blue ...
- **p. 5 / 4.2. Settings - extractive body cue:** Anchors are matched to ground truth using the 2D IoU with the following rules.
- **p. 5 / 4.2. Settings - extractive body cue:** At inference time we apply axis aligned non maximum suppression (NMS) with an overlap threshold of 0.5 IoU.
- **p. 6 / 5. Results - extractive body cue:** As shown in Table 1 and Table 2, PointPillars outperforms all published methods with respect to mean average precision (mAP).
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Encoder performance evaluation. To fairly compare en- coders, the same network architecture and training procedure was used and only the encoder and xy ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3. Implementation Details (p. 4); 4. Experimental setup (p. 5); 4.1. Dataset (p. 5); 5. Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. Bird's eye view performance vs speed for our proposed PointPillars, PP method on the KITTI [5] test set. Lidar-only methods drawn as ... | p. 1 (Figure/Table caption) |
| 5. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared to lidar-only methods, PointPillars achieves better results across all classes and difficulty strata except for the easy car stratum. | p. 6 (5. Results) |
| 5. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | It also outperforms fusion based methods on cars and cyclists. | p. 6 (5. Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5. BEV detection performance (mAP) vs speed (Hz) on the KITTI [5] val set across pedestrians, bicycles and cars. Blue cir- cles indicate ... | p. 8 (Figure/Table caption) |
| 4.2. Settings | EMPIRICAL / SOURCE-REPORTED EVALUATION | This provides similar performance compared to rotational NMS, but is much faster. | p. 5 (4.2. Settings) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Dataset - extractive body cue:** All experiments use the KITTI object detection benchmark dataset [5], which consists of samples that have both lidar point clouds and images.
- **p. 5 / 4.1. Dataset - extractive body cue:** The KITTI benchmark requires detections of cars, pedestrians, and cyclists.
- **p. 6 / 5. Results - extractive body cue:** The KITTI dataset is stratified into easy, moderate, and hard difficulties, and the official KITTI leaderboard is ranked by performance on moderate.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Bird's eye view performance vs speed for our proposed PointPillars, PP method on the KITTI [5] test set. Lidar-only methods drawn as blue ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Network overview. The main components of the network are a Pillar Feature Network, Backbone, and SSD Detection Head. See Section 2 for more ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative analysis of KITTI results. We show a bird's-eye view of the lidar point cloud (top), as well as the 3D bounding boxes ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Failure cases on KITTI. Same visualize setup from Figure 3 but focusing on several common failure modes. Next, we use a simplified version ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Results on the KITTI test BEV detection benchmark.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Results on the KITTI test 3D detection benchmark.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Results on the KITTI test average orientation similarity (AOS) detection benchmark. SubCNN is the best performing image only method, while AVOD-FPN, SECOND, and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. BEV detection performance (mAP) vs speed (Hz) on the KITTI [5] val set across pedestrians, bicycles and cars. Blue cir- cles indicate lidar ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | All experiments use the KITTI object detection benchmark dataset [5], which consists of samples that have both lidar point clouds and images. | embodiment, simulator version and control stack | p. 5 (4.1. Dataset), p. 5 (4.1. Dataset) |
| Task/environment | The KITTI benchmark requires detections of cars, pedestrians, and cyclists. | reset, timeout, object/scene variation | p. 5 (4.1. Dataset), p. 6 (5. Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 7 (Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (4.3. Data Augmentation), p. 6 (4.3. Data Augmentation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 1. Bird's eye view performance vs speed for our proposed PointPillars, PP method on the KITTI [5] test set. Lidar-only methods drawn as ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Anchors are matched to ground truth using the 2D IoU with the following rules. | definition/direction/unit from same section | p. 5 (4.2. Settings) |
| At inference time we apply axis aligned non maximum suppression (NMS) with an overlap threshold of 0.5 IoU. | definition/direction/unit from same section | p. 5 (4.2. Settings) |
| As shown in Table 1 and Table 2, PointPillars outperforms all published methods with respect to mean average precision (mAP). | definition/direction/unit from same section | p. 6 (5. Results) |
| The KITTI dataset is stratified into easy, moderate, and hard difficulties, and the official KITTI leaderboard is ranked by performance on moderate. | definition/direction/unit from same section | p. 6 (5. Results) |
| Table 4. Encoder performance evaluation. To fairly compare en- coders, the same network architecture and training procedure was used and only the encoder and ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 5. BEV detection performance (mAP) vs speed (Hz) on the KITTI [5] val set across pedestrians, bicycles and cars. Blue cir- cles indicate ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| In this section we describe our network parameters and the loss function that we optimize for. | definition/direction/unit from same section | p. 4 (3. Implementation Details) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| This provides similar performance compared to rotational NMS, but is much faster. | comparison identity and matched condition | p. 5 (4.2. Settings) |
| It also outperforms fusion based methods on cars and cyclists. | comparison identity and matched condition | p. 6 (5. Results) |
| Despite this, PointPillars moderate cyclist AOS of 68.16 outperforms the best image based method [27]. | comparison identity and matched condition | p. 6 (5. Results) |
| Figure 1. Bird's eye view performance vs speed for our proposed PointPillars, PP method on the KITTI [5] test set. Lidar-only methods drawn as ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 2. Network overview. The main components of the network are a Pillar Feature Network, Backbone, and SSD Detection Head. See Section 2 for ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Both network consists of three blocks, Block1(S, 4, C), Block2(2S, 6, 2C), and Block3(4S, 6, 4C). | Figure 1. Bird's eye view performance vs speed for our proposed PointPillars, PP method on the KITTI [5] test set. Lidar-only methods drawn as ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Figure/Table caption), p. 6 (5. Results), p. 6 (5. Results), p. 8 (Figure/Table caption), p. 5 (4.2. Settings), p. 4 (Figure/Table caption) |
| Primary metric/result | Compared to lidar-only methods, PointPillars achieves better results across all classes and difficulty strata except for the easy car stratum. | numeric claim only at cited anchor | p. 6 (5. Results) |

- Numeric sentences retained from the body:
- **p. 5 / 3.1. Network - extractive body cue:** Both network consists of three blocks, Block1(S, 4, C), Block2(2S, 6, 2C), and Block3(4S, 6, 4C).
- **p. 5 / 3.1. Network - extractive body cue:** Each block is upsampled by the following upsampling steps: Up1(S, S, 2C), Up2(2S, S, 2C) and Up3(4S, S, 2C).
- **p. 5 / 3.2. Loss - extractive body cue:** To optimize the loss function we use the Adam optimizer with an initial learning rate of 2 ∗10-4 and decay the learning rate by a ...
- **p. 5 / 4.1. Dataset - extractive body cue:** For experimental studies we split the official training into 3712 training samples and 3769 validation samples [1], while for our test submission we created a ...
- **p. 5 / 4.2. Settings - extractive body cue:** Each class anchor is described by a width, length, height, and z center, and is applied at two orientations: 0 and 90 degrees.
- **p. 5 / 4.2. Settings - extractive body cue:** The pedestrian anchor has width, length, and height of (0.6, 0.8, 1.73) meters with a z center of -0.6 meters, while the cyclist anchor has ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 4. Failure cases on KITTI. Same visualize setup from Figure 3 but focusing on several common failure modes. Next, we use a simplified ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | The total localization loss is: Lloc = X b∈(x,y,z,w,l,h,θ) SmoothL1 (∆b) Since the angle localization loss cannot distinguish flipped boxes, we use a softmax ... | p. 5 (3.2. Loss) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To optimize the loss function we use the Adam optimizer with an initial learning rate of 2 ∗10-4 and decay the learning rate by ... | p. 5 (3.2. Loss) |
| We use a batch size of 2 for validation set and 4 for our test submission. | p. 5 (3.2. Loss) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Failure cases on KITTI. Same visualize setup from Figure 3 but focusing on several common failure modes. Next, we use a simplified version ...
- **p. 5 / 3.2. Loss - extractive body cue:** The total localization loss is: Lloc = X b∈(x,y,z,w,l,h,θ) SmoothL1 (∆b) Since the angle localization loss cannot distinguish flipped boxes, we use a softmax classification ...

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Dataset), p. 5 (4.1. Dataset), p. 6 (5. Results), metrics p. 1 (Figure/Table caption), p. 5 (4.2. Settings), p. 5 (4.2. Settings), p. 6 (5. Results), p. 6 (5. Results), p. 8 (Figure/Table caption), baselines p. 5 (4.2. Settings), p. 6 (5. Results), p. 6 (5. Results), p. 1 (Figure/Table caption), results p. 1 (Figure/Table caption), p. 6 (5. Results), p. 6 (5. Results), p. 8 (Figure/Table caption), p. 5 (4.2. Settings), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
