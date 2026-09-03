# Evaluation - VoxFormer: Sparse Voxel Transformer for Camera-based 3D Semantic Scene Completion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2302.12251; PDF retrieval source: https://arxiv.org/pdf/2302.12251. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Performance), p. 6 (4.2. Performance), p. 6 (4.2. Performance), p. 7 (4.2. Performance), p. 8 (Figure/Table caption)): VoxFormer-T can achieve mIoU scores of 21.55 and 18.42 within 12.8 meters and 25.6 meters, which outperforms the state-of-the-art MonoScene by 75.92% and 50.74% respectively.

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** SemanticKITTI SSC benchmark is interested in a volume of 51.2m ahead of the car, 25.6m to left and right side, and 6.4m in height.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We verify VoxFormer on SemanticKITTI [5], which provides dense semantic annotations for each LiDAR sweep from the KITTI Odometry Benchmark [71] composed of 22 outdoor ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We report the results within different ranges on the validation set, and the results within the full range on the hidden test set are in ...
- **p. 7 / 4.2. Performance - extractive body cue:** VoxFormer shows a large advancement in completing small objects compared to the main baseline MonoScene such as the bicycle (0.07 →5.22), motorcycle (0.05 →2.98), bicyclist ...
- **p. 6 / 4.2. Performance - extractive body cue:** VoxFormer-S outperforms MonoScene by a large margin in terms of geometric completion (36.80 →44.02, 19.62%); see Table 1.
- **p. 7 / 4.2. Performance - extractive body cue:** Our superiority over others for small objects.
- **p. 6 / 4.2. Performance - extractive body cue:** Meanwhile, the semantic score is also improved by 9.29% without sacrificing IoU.
- **p. 7 / 4.2. Performance - extractive body cue:** For example, the IoU scores of building, parking, and terrain categories are respectively improved by 10.71%, 27.03%, and 10.35% inside the full volume because VoxFormer-S ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setup (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Performance | SYSTEM / EVALUATION SCOPE UNRESOLVED | VoxFormer-T can achieve mIoU scores of 21.55 and 18.42 within 12.8 meters and 25.6 meters, which outperforms the state-of-the-art MonoScene by 75.92% and 50.74% ... | p. 7 (4.2. Performance) |
| 4.2. Performance | SYSTEM / EVALUATION SCOPE UNRESOLVED | Meanwhile, the semantic score is also improved by 9.29% without sacrificing IoU. | p. 6 (4.2. Performance) |
| 4.2. Performance | SYSTEM / EVALUATION SCOPE UNRESOLVED | Despite the negligible difference in IoU, VoxFormer-T further improves the SSC performance over | p. 6 (4.2. Performance) |
| 4.2. Performance | SYSTEM / EVALUATION SCOPE UNRESOLVED | For example, the IoU scores of building, parking, and terrain categories are respectively improved by 10.71%, 27.03%, and 10.35% inside the full volume because ... | p. 7 (4.2. Performance) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 7. Ablation study for architecture. Temporal input. The ablation study for temporal infor- mation is shown in Table 5. The offline setting with ... | p. 8 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** SemanticKITTI SSC benchmark is interested in a volume of 51.2m ahead of the car, 25.6m to left and right side, and 6.4m in height.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We verify VoxFormer on SemanticKITTI [5], which provides dense semantic annotations for each LiDAR sweep from the KITTI Odometry Benchmark [71] composed of 22 outdoor ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We report the results within different ranges on the validation set, and the results within the full range on the hidden test set are in ...
- **p. 7 / 4.2. Performance - extractive body cue:** VoxFormer shows a large advancement in completing small objects compared to the main baseline MonoScene such as the bicycle (0.07 →5.22), motorcycle (0.05 →2.98), bicyclist ...
- **p. 6 / 4.2. Performance - extractive body cue:** VoxFormer-S outperforms MonoScene by a large margin in terms of geometric completion (36.80 →44.02, 19.62%); see Table 1.
- **p. 7 / 4.2. Performance - extractive body cue:** Our superiority over others for small objects.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (a) A diagram of VoxFormer for camera-based se- mantic scene completion that predicts complete 3D geometry and semantics given only 2D images. After ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overall framework of VoxFormer. Given RGB images, 2D features are extracted by ResNet50 [61] and the depth is estimated by an off-the-shelf depth ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparison against the state-of-the-art camera-based SSC methods. We report the performances inside three volumes, i.e., 12.8×12.8×6.4m3, 25.6×25.6×6.4m3, and 51.2×51.2×6.4m3. The first two ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results of our method and others. VoxFormer better captures the scene layout in large-scale self-driving scenarios. Meanwhile, VoxFormer shows satisfactory performances in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparison against the state-of-the-art LiDAR-based SSC methods. VoxFormer even performs on par with some LiDAR-based methods at close range. VoxFormer-S with temporal ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. For example, the IoU scores of building, park- ing, and terrain categories are respectively improved by 10.71%, 27.03%, and 10.35% inside the full ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation study for image depth. With monocular depth, VoxFormer-S performs better than MonoScene in geome- try (12.8m, 25.6m, and 51.2m) and semantics (12.8m ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablation study for query proposal. Our depth-based query proposal performs best. t

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | SemanticKITTI SSC benchmark is interested in a volume of 51.2m ahead of the car, 25.6m to left and right side, and 6.4m in height. | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Task/environment | We verify VoxFormer on SemanticKITTI [5], which provides dense semantic annotations for each LiDAR sweep from the KITTI Odometry Benchmark [71] composed of 22 ... | reset, timeout, object/scene variation | p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.3. Predefined Parameters), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Meanwhile, the semantic score is also improved by 9.29% without sacrificing IoU. | definition/direction/unit from same section | p. 6 (4.2. Performance) |
| For example, the IoU scores of building, parking, and terrain categories are respectively improved by 10.71%, 27.03%, and 10.35% inside the full volume because ... | definition/direction/unit from same section | p. 7 (4.2. Performance) |
| Despite the negligible difference in IoU, VoxFormer-T further improves the SSC performance over | definition/direction/unit from same section | p. 6 (4.2. Performance) |
| VoxFormer-T can achieve mIoU scores of 21.55 and 18.42 within 12.8 meters and 25.6 meters, which outperforms the state-of-the-art MonoScene by 75.92% and 50.74% ... | definition/direction/unit from same section | p. 7 (4.2. Performance) |
| Query Dense Random Occupancy Ratio (%) 100 90 80 70 60 50 40 30 20 10 10∼20 Memory (G) 18.5 18.2 17.6 17.3 16.8 ... | definition/direction/unit from same section | p. 8 (4.2. Performance) |
| Table 6. Ablation study for 2D image feature layers. Spatial resolution is relative to the input image size. Methods IoU (%) mIoU (%) Ours ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 1. (a) A diagram of VoxFormer for camera-based se- mantic scene completion that predicts complete 3D geometry and semantics given only 2D images. ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Such depth can help generate a pseudo-LiDAR point cloud at a much lower cost based solely on stereo images. | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare VoxFormer against the state-of-the-art SSC methods with public resources: (1) a camera-based SSC method MonoScene [4] based on 2D-to-3D feature projection, (2) ... | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| VoxFormer-T can achieve mIoU scores of 21.55 and 18.42 within 12.8 meters and 25.6 meters, which outperforms the state-of-the-art MonoScene by 75.92% and 50.74% ... | comparison identity and matched condition | p. 7 (4.2. Performance) |
| VoxFormer shows a large advancement in completing small objects compared to the main baseline MonoScene such as the bicycle (0.07 →5.22), motorcycle (0.05 →2.98), ... | comparison identity and matched condition | p. 7 (4.2. Performance) |
| Quantitative comparison against the state-of-the-art camera-based SSC methods. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| Figure 1. (a) A diagram of VoxFormer for camera-based se- mantic scene completion that predicts complete 3D geometry and semantics given only 2D images. ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Table 7. Ablation study for architecture. Temporal input. The ablation study for temporal infor- mation is shown in Table 5. The offline setting with ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Meanwhile, the semantic score is also improved by 9.29% without sacrificing IoU. | component/input/data sensitivity | p. 6 (4.2. Performance) |
| Table 3. Ablation study for image depth. With monocular depth, VoxFormer-S performs better than MonoScene in geome- try (12.8m, 25.6m, and 51.2m) and semantics ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 4. Ablation study for query proposal. Our depth-based query proposal performs best. t | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 6. Ablation study for 2D image feature layers. Spatial resolution is relative to the input image size. Methods IoU (%) mIoU (%) Ours ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions in this work can be summarized as follows: • A novel two-stage framework that lifts images into a complete 3D voxelized semantic ... | VoxFormer-T can achieve mIoU scores of 21.55 and 18.42 within 12.8 meters and 25.6 meters, which outperforms the state-of-the-art MonoScene by 75.92% and 50.74% ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Performance), p. 6 (4.2. Performance), p. 6 (4.2. Performance), p. 7 (4.2. Performance), p. 8 (Figure/Table caption) |
| Primary metric/result | Meanwhile, the semantic score is also improved by 9.29% without sacrificing IoU. | numeric claim only at cited anchor | p. 6 (4.2. Performance) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We directly utilize the depth predictor in [70], and we train an occupancy predictor from scratch, using as input a voxelized pseudo point cloud with ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Regarding stage-2, we crop RGB images of cam2 to size 1220×370 and employ ResNet50 [61] to extract image features, then the features in the 3rd ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We report the performances inside three volumes, i.e., 12.8×12.8×6.4m3, 25.6×25.6×6.4m3, and 51.2×51.2×6.4m3.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We train stage-1 and stage-2 separately with 24 epochs, a learning rate of 2×10-4.
- **p. 7 / 4.2. Performance - extractive body cue:** VoxFormer-T can achieve mIoU scores of 21.55 and 18.42 within 12.8 meters and 25.6 meters, which outperforms the state-of-the-art MonoScene by 75.92% and 50.74% respectively.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train stage-1 and stage-2 separately with 24 epochs, a learning rate of 2×10-4. | p. 6 (4.1. Experimental Setup) |
| Therefore, the loss can be computed by: L = - K X k=1 cM X c=c0 wcˆyk,clog( eyk,c P c eyk,c ), (6) where ... | p. 5 (3.6. Training Loss) |
| Besides, VoxFormer needs less than 16GB GPU memory during training. | p. 7 (4.2. Performance) |
| A more specific procedure is as follows: • Extract 2D features F2D t ∈Rb×c×d from RGB image It using ResNet-50 backbone [61], where b ... | p. 3 (3.2. Overall Architecture) |
| For efficiency, we utilize deformable attention [66], which interacts with local regions of interest, and only sample Ns points around the reference point to ... | p. 5 (3.3. Predefined Parameters) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Performance), p. 6 (4.2. Performance), p. 7 (4.2. Performance), metrics p. 6 (4.2. Performance), p. 7 (4.2. Performance), p. 6 (4.2. Performance), p. 7 (4.2. Performance), p. 8 (4.2. Performance), p. 8 (Figure/Table caption), baselines p. 6 (4.1. Experimental Setup), p. 7 (4.2. Performance), p. 7 (4.2. Performance), p. 6 (4.1. Experimental Setup), p. 1 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 7 (4.2. Performance), p. 6 (4.2. Performance), p. 6 (4.2. Performance), p. 7 (4.2. Performance), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
