# Evaluation - MonoScene: Monocular 3D Semantic Scene Completion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.00726; PDF retrieval source: https://arxiv.org/pdf/2112.00726. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2.1 Evaluation), p. 5 (4.2.1 Evaluation), p. 5 (4. Experiments), p. 6 (4.2.1 Evaluation), p. 7 (4.3. Ablation studies), p. 7 (4.3. Ablation studies)): Despite the various indoor and outdoor setups, we significantly outperform other RGB-inferred baselines, in both mIoU and IoU.

## Evaluation Body Digest

- **p. 4 / 4. Experiments - extractive PDF cue:** We evaluate MonoScene on popular real-world SSC datasets being, indoor NYUv2 [58] and outdoor Se4
- **p. 5 / 4.2.1 Evaluation - extractive PDF cue:** 1 reports performance of MonoScene and RGBinferred baselines for NYUv2 (test set) and SemanticKITTI official benchmark (hidden test set).
- **p. 5 / 4.2.1 Evaluation - extractive PDF cue:** On individual classes, MonoScene performs either best or second, excelling on large structural classes for both datasets (e.g. floor, wall ; road, building).
- **p. 7 / 4.2.1 Evaluation - extractive PDF cue:** MonoScene better captures the scene layout on both datasets.
- **p. 7 / 4.2.1 Evaluation - extractive PDF cue:** In both, the input is shown left and the camera viewing frustum is shown in the ground truth (rightmost) with darker colors being parts of ...
- **p. 8 / 4.3. Ablation studies - extractive PDF cue:** Outputs of MonoScene when trained on Sem.KITTI having horizontal FOV of 82◦, and tested on datasets with decreasing (left) or increasing (right) FOV. when compared ...
- **p. 6 / 4.2.1 Evaluation - extractive PDF cue:** SC SSC Method Input IoU ■ceiling (1.37%) ■floor (17.58%) ■wall (15.26%) ■window (1.99%) ■chair (3.01%) ■bed (7.08%) ■sofa (4.70%) ■table (4.31%) ■tvs (0.47%) ■furniture (30.04%) ...
- **p. 6 / 4.2.1 Evaluation - extractive PDF cue:** 2b), the baselines clearly surpass us in all metrics which relates both to the lidar-originated 3D input having a much wider horizontal FOV than the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 4); 4.2.1 Evaluation (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2.1 Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Despite the various indoor and outdoor setups, we significantly outperform other RGB-inferred baselines, in both mIoU and IoU. | p. 6 (4.2.1 Evaluation) |
| 4.2.1 Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | On both datasets we outperform all methods by a significant mIoU margin of +4.03 on NYUv2 (Tab. | p. 5 (4.2.1 Evaluation) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Note the strong interaction between IoU and mIoU since better geometry estimation (i.e. high IoU) can be achieved by invalidating semantic labels (i.e. low ... | p. 5 (4. Experiments) |
| 4.2.1 Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3DSketch, using RGB + TSDF, outperforms us on both mIoU and IoU showing the benefit of TSDF for SSC as mentioned in [56]. | p. 6 (4.2.1 Evaluation) |
| 4.3. Ablation studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | In NYUv2 only, Lsem scal harms IoU (-0.31) but improves the same metric on SemanticKITTI (+0.34). | p. 7 (4.3. Ablation studies) |

## Dataset / Benchmark Role

- **p. 4 / 4. Experiments - extractive PDF cue:** We evaluate MonoScene on popular real-world SSC datasets being, indoor NYUv2 [58] and outdoor Se4
- **p. 5 / 4.2.1 Evaluation - extractive PDF cue:** 1 reports performance of MonoScene and RGBinferred baselines for NYUv2 (test set) and SemanticKITTI official benchmark (hidden test set).
- **p. 5 / 4.2.1 Evaluation - extractive PDF cue:** On individual classes, MonoScene performs either best or second, excelling on large structural classes for both datasets (e.g. floor, wall ; road, building).
- **p. 7 / 4.2.1 Evaluation - extractive PDF cue:** MonoScene better captures the scene layout on both datasets.
- **p. 7 / 4.2.1 Evaluation - extractive PDF cue:** In both, the input is shown left and the camera viewing frustum is shown in the ground truth (rightmost) with darker colors being parts of ...
- **p. 8 / 4.3. Ablation studies - extractive PDF cue:** Outputs of MonoScene when trained on Sem.KITTI having horizontal FOV of 82◦, and tested on datasets with decreasing (left) or increasing (right) FOV. when compared ...
- **p. 6 / 4.2.1 Evaluation - extractive PDF cue:** SC SSC Method Input IoU ■ceiling (1.37%) ■floor (17.58%) ■wall (15.26%) ■window (1.99%) ■chair (3.01%) ■bed (7.08%) ■sofa (4.70%) ■table (4.31%) ■tvs (0.47%) ■furniture (30.04%) ...
- **p. 6 / 4.2.1 Evaluation - extractive PDF cue:** 2b), the baselines clearly surpass us in all metrics which relates both to the lidar-originated 3D input having a much wider horizontal FOV than the ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. RGB Semantic Scene Completion with MonoScene. Our framework infers dense semantic scenes, hallucinating scenery outside the field of view of the image (dark ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. MonoScene framework. We infer 3D SSC from a single RGB image, leveraging 2D and 3D UNets, bridged by our Features Line of Sight ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Features Line of Sight Projection (FLoSP). We project multi-scale 2D features F1:s 2D (here, s ∈{1, 2, 4, 8}) along their line of ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 4. 2D illustration of 4-way relations. (a) We consider voxel↔voxel relations whether one is free or both are occupied, and if their semantics is ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 5. 3D Context Relation Prior (3D CRP). We infer re- lation matrices ˆAm (here, 4), where each encodes a unique re- lation m ∈M ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 6. Frustum Proportion Loss. Considering an image di- vided into same-size 2D patches (here, 2×2), each corresponds to a 3D frustum in the scene, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Performance on (a) NYUv2 [58] and (b) SemanticKITTI [3]. We report the performance on semantic scene completion (SSC - mIoU) and scene completion ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. 2.5/3D input baselines. Despite a single RGB, MonoScene still outperforms the mIoU of some indoor baselines. cars in rows 1-3 having better shapes. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate MonoScene on popular real-world SSC datasets being, indoor NYUv2 [58] and outdoor Se4 | embodiment, simulator version and control stack | p. 4 (4. Experiments), p. 5 (4.2.1 Evaluation) |
| Task/environment | 1 reports performance of MonoScene and RGBinferred baselines for NYUv2 (test set) and SemanticKITTI official benchmark (hidden test set). | reset, timeout, object/scene variation | p. 5 (4.2.1 Evaluation), p. 5 (4.2.1 Evaluation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Features Line of Sight Projection (FLoSP)), p. 2 (3. Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (3. Method), p. 3 (3.2. 3D Context Relation Prior (3D CRP)) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the performance on semantic scene completion (SSC - mIoU) and scene completion (SC - IoU) for RGB-inferred baselines and our method. | definition/direction/unit from same section | p. 6 (4.2.1 Evaluation) |
| Importantly, the IoU is improved or on par (+3.87 and +0.16) which demonstrates our network captures the scene geometry while avoiding naively increasing the ... | definition/direction/unit from same section | p. 5 (4.2.1 Evaluation) |
| Following common practices, we report the intersection over union (IoU) of occupied voxels, regardless of their semantic class, for the scene completion (SC) task ... | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Our components boost performance on NYUv2 [58] (test set) and SemanticKitti [3] (val. set). a comfortable margin (+6.48 and +3.17), but with a lower ... | definition/direction/unit from same section | p. 6 (4.2.1 Evaluation) |
| More 2D scales boosts IoU and mIoU consistently and leans to lower variance - showing (1,2,4,8) projections are indeed best. | definition/direction/unit from same section | p. 7 (4.3. Ablation studies) |
| Pool & Deconv E D Ours-light FLoSP E D (a) Architectures (2D or 3D) IoU ↑ mIoU ↑ CoReNet (1,2,4) 30.60 ±0.46 17.34 ±0.37 ... | definition/direction/unit from same section | p. 8 (4.3. Ablation studies) |
| As ℓ×ℓincreases, all metrics increase accordingly, showing the loss benefit, especially NYUv2 SemanticKITTI ℓ×ℓ IoU ↑ mIoU ↑ IoU ↑ mIoU ↑ 8 × ... | definition/direction/unit from same section | p. 8 (4.3. Ablation studies) |
| 3.2) contributes equally to IoU (in [+0.77,+1.12]) and mIoU (in [+0.54, +1.33]). | definition/direction/unit from same section | p. 7 (4.3. Ablation studies) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 7b), compared to baselines, MonoScene evidently captures better the scene layout, e.g. cross-roads (rows 1,3). | comparison identity and matched condition | p. 5 (4.2.1 Evaluation) |
| Despite a single RGB, MonoScene still outperforms the mIoU of some indoor baselines. cars in rows 1-3 having better shapes. | comparison identity and matched condition | p. 6 (4.2.1 Evaluation) |
| Despite the various indoor and outdoor setups, we significantly outperform other RGB-inferred baselines, in both mIoU and IoU. | comparison identity and matched condition | p. 6 (4.2.1 Evaluation) |
| For fair comparison, we adapt main baselines to infer their 3D inputs directly from the 2D image (xrgb) - relying on the best found ... | comparison identity and matched condition | p. 5 (4.1. Baselines) |
| Outputs of MonoScene when trained on Sem.KITTI having horizontal FOV of 82◦, and tested on datasets with decreasing (left) or increasing (right) FOV. when ... | comparison identity and matched condition | p. 8 (4.3. Ablation studies) |
| Table 6. Performance on SemanticKITTI [3] (validation set). We report the performance on semantic scene completion (SSC - mIoU) and scene completion (SC - ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To properly evaluate only the effect of features projection, we remove our other components, producing a light version (‘Ours-light') with the same 2D encoder ... | component/input/data sensitivity | p. 8 (4.3. Ablation studies) |
| Figure 8. Type of 2D-3D features projections. (a) Comparing our FLoSP and ‘Ray-traced skip connections' from CoReNet [52] (cf. text) shows in (b) we ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We now study in-depth the effect of FLoSP (Sec. | component/input/data sensitivity | p. 7 (4.3. Ablation studies) |
| Main results are from the hidden test set (online server), and ablations are from the validation set. | component/input/data sensitivity | p. 5 (4. Experiments) |
| Table 3. Architecture ablation. Our components boost perfor- mance on NYUv2 [58] (test set) and SemanticKitti [3] (val. set). a comfortable margin (+6.48 and ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| We use the pretrained AdaBin [4] to infer a depth map (ˆxdepth) serving as input for AICNetrgb. | component/input/data sensitivity | p. 5 (4.1. Baselines) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our framework infers dense semantic scenes, hallucinating scenery outside the field of view of the image (dark voxels, right). and outdoor scenes. | Despite the various indoor and outdoor setups, we significantly outperform other RGB-inferred baselines, in both mIoU and IoU. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2.1 Evaluation), p. 5 (4.2.1 Evaluation), p. 5 (4. Experiments), p. 6 (4.2.1 Evaluation), p. 7 (4.3. Ablation studies), p. 7 (4.3. Ablation studies) |
| Primary metric/result | On both datasets we outperform all methods by a significant mIoU margin of +4.03 on NYUv2 (Tab. | numeric claim only at cited anchor | p. 5 (4.2.1 Evaluation) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experiments - extractive PDF cue:** We use RGB image of cam2 of size 1226x370, left cropped to 1220×370.
- **p. 5 / 4. Experiments - extractive PDF cue:** Unless otherwise mentioned, we use FLoSP at scales (1,2,4,8), 4 supervised relations for 3D CRP (i.e. n=4, with Lrel), and ℓ×ℓ=8×8 frustums for Lfp.
- **p. 5 / 4. Experiments - extractive PDF cue:** We train 30 epochs with an AdamW [46] optimizer, a batch size of 4 and a weight decay of 1e-4.
- **p. 6 / 4.2.1 Evaluation - extractive PDF cue:** 2a) we still beat the recent LMSCNet and AICNet in mIoU by NYUv2 SemanticKITTI IoU ↑ mIoU ↑ IoU ↑ mIoU ↑ Ours 42.51 ±0.15 ...
- **p. 8 / 4.3. Ablation studies - extractive PDF cue:** 2D scales (S) IoU ↑ mIoU ↑ 1, 2, 4, 8 42.51 ±0.15 26.94 ±0.10 1, 2, 4 42.08 ±0.69 26.28 ±0.24 1, 2 41.56 ...
- **p. 8 / 4.3. Ablation studies - extractive PDF cue:** Pool & Deconv E D Ours-light FLoSP E D (a) Architectures (2D or 3D) IoU ↑ mIoU ↑ CoReNet (1,2,4) 30.60 ±0.46 17.34 ±0.37 Ours-light ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Compared to the Whole Scene, the in-FOV performance is higher since it considers visible surfaces, whereas the out-FOV performance is significantly lower since the ... | p. 9 (5. Discussion) |
| body limitation/failure cue | Due to the single viewpoint, occlusion artefacts such as distortions are visible along the line of sight in outdoor scenes. | p. 8 (5. Discussion) |
| body limitation/failure cue | Figure 2. MonoScene framework. We infer 3D SSC from a single RGB image, leveraging 2D and 3D UNets, bridged by our Features Line of ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 6. Frustum Proportion Loss. Considering an image di- vided into same-size 2D patches (here, 2×2), each corresponds to a 3D frustum in the ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train 30 epochs with an AdamW [46] optimizer, a batch size of 4 and a weight decay of 1e-4. | p. 5 (4. Experiments) |
| The learning rate is 1e-4, divided by 10 at epoch 20/25 for NYUv2/SemanticKITTI. | p. 5 (4. Experiments) |
| (9) Because real-world data comes with sparse ground truth y due to occlusions, the losses are computed only where y is defined [45, 56, ... | p. 4 (3.4. Training strategy) |
| For ‘w/o FLoSP', we instead interpolate and convolve the 2D decoder features to the required 3D UNet input size. | p. 7 (4.3. Ablation studies) |
| To properly evaluate only the effect of features projection, we remove our other components, producing a light version (‘Ours-light') with the same 2D encoder ... | p. 8 (4.3. Ablation studies) |
| 3.2) inserted between the 3D encoder and decoder. | p. 2 (3. Method) |
| The 3D UNet is a custom shallow encoderdecoder with 2 layers. | p. 2 (3. Method) |
| sample sample sample 2D decoder 1x1 conv 1x1 conv 1x1 conv Figure 3. | p. 3 (3.1. Features Line of Sight Projection (FLoSP)) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5. Discussion - extractive PDF cue:** Compared to the Whole Scene, the in-FOV performance is higher since it considers visible surfaces, whereas the out-FOV performance is significantly lower since the image ...
- **p. 8 / 5. Discussion - extractive PDF cue:** Due to the single viewpoint, occlusion artefacts such as distortions are visible along the line of sight in outdoor scenes.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. MonoScene framework. We infer 3D SSC from a single RGB image, leveraging 2D and 3D UNets, bridged by our Features Line of Sight ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 6. Frustum Proportion Loss. Considering an image di- vided into same-size 2D patches (here, 2×2), each corresponds to a 3D frustum in the scene, ...

- **PDF anchors reviewed:** datasets p. 4 (4. Experiments), p. 5 (4.2.1 Evaluation), p. 5 (4.2.1 Evaluation), p. 7 (4.2.1 Evaluation), p. 7 (4.2.1 Evaluation), p. 8 (4.3. Ablation studies), metrics p. 6 (4.2.1 Evaluation), p. 5 (4.2.1 Evaluation), p. 5 (4. Experiments), p. 6 (4.2.1 Evaluation), p. 7 (4.3. Ablation studies), p. 8 (4.3. Ablation studies), baselines p. 5 (4.2.1 Evaluation), p. 6 (4.2.1 Evaluation), p. 6 (4.2.1 Evaluation), p. 5 (4.1. Baselines), p. 8 (4.3. Ablation studies), p. 10 (Figure/Table caption), results p. 6 (4.2.1 Evaluation), p. 5 (4.2.1 Evaluation), p. 5 (4. Experiments), p. 6 (4.2.1 Evaluation), p. 7 (4.3. Ablation studies), p. 7 (4.3. Ablation studies).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
