# Evaluation - Rethinking Temporal Fusion with a Unified Gradient Descent View for 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Rethinking_Temporal_Fusion_with_a_Unified_Gradient_Descent_View_for_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_Rethinking_Temporal_Fusion_with_a_Unified_Gradient_Descent_View_for_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption)): Table 4. Ablations on different temporal cues. B, G, V, S, and M represent baseline, temporal geometry fusion, voxel-level fusion, scene-level fusion, and temporal motion fusion, respectively. ALOcc) using official ...

## Evaluation Body Digest

- **p. 6 / 5. Experiment - extractive PDF cue:** This dataset comprises 1,000 scenes in total, with 700 designated for 1510
- **p. 6 / 5. Experiment - extractive PDF cue:** Our experiments are based on the nuScenes dataset [3], which provides extensive data to develop and evaluate essential 3D perception algorithms.
- **p. 3 / 3.2. Temporal Cue Analysis and Formulation - extractive PDF cue:** The environment evolves continuously over short time spans, implying exploitable scene consistency priors.
- **p. 4 / 3.2. Temporal Cue Analysis and Formulation - extractive PDF cue:** Occupancy 2D-to-3D Lifting Task Head Scene-Adaptive Network Temporal Geometry Fusion ۵௧ ۶௚௧ିଵ ۶௩௧ିଵ ܄௧ Voxel-Level Temporal Fusion Images: Time t Fused Volume Feature Temporal Motion ...
- **p. 3 / 3.2. Temporal Cue Analysis and Formulation - extractive PDF cue:** Inspired by testtime adaptation [6, 39, 40], we introduce additional sceneadaptive network parameters St (Sec.
- **p. 4 / 3.2. Temporal Cue Analysis and Formulation - extractive PDF cue:** Ideally, this should handle dynamic object motion and camera pose estimation errors.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison of 3D semantic occupancy prediction performance on the Occ3D dataset, evaluated with mIoUD, mIoU, and IoU metrics. Relative improvements are highlighted with ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. Motivation behind the proposed temporal fusion. (a): VisionOcc pipeline. (b): Proposed temporal cues, showing historical motion and geometric data enhancing current viewpoints, with ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiment (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 4. Ablations on different temporal cues. B, G, V, S, and M represent baseline, temporal geometry fusion, voxel-level fusion, scene-level fusion, and temporal ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 4. Comparison of our GDFusion and SOLOFusion w.r.t. memory consumption. SOLOFusion boosts performance with longer sequences but increases inference memory, while GDFu- sion ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1. Comparison of 3D semantic occupancy prediction performance on the Occ3D dataset, evaluated with mIoUD, mIoU, and IoU metrics. Relative improvements are highlighted ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 1. Motivation behind the proposed temporal fusion. (a): VisionOcc pipeline. (b): Proposed temporal cues, showing historical motion and geometric data enhancing current viewpoints, ... | p. 2 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 5. Runtime analysis of key components, vs. SOLOFusion (16 frames). AutoGrad refers to PyTorch's automatic differentia- tion; Custom Matmul is our custom matrix ... | p. 8 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5. Experiment - extractive PDF cue:** This dataset comprises 1,000 scenes in total, with 700 designated for 1510
- **p. 6 / 5. Experiment - extractive PDF cue:** Our experiments are based on the nuScenes dataset [3], which provides extensive data to develop and evaluate essential 3D perception algorithms.
- **p. 3 / 3.2. Temporal Cue Analysis and Formulation - extractive PDF cue:** The environment evolves continuously over short time spans, implying exploitable scene consistency priors.
- **p. 4 / 3.2. Temporal Cue Analysis and Formulation - extractive PDF cue:** Occupancy 2D-to-3D Lifting Task Head Scene-Adaptive Network Temporal Geometry Fusion ۵௧ ۶௚௧ିଵ ۶௩௧ିଵ ܄௧ Voxel-Level Temporal Fusion Images: Time t Fused Volume Feature Temporal Motion ...
- **p. 3 / 3.2. Temporal Cue Analysis and Formulation - extractive PDF cue:** Inspired by testtime adaptation [6, 39, 40], we introduce additional sceneadaptive network parameters St (Sec.
- **p. 4 / 3.2. Temporal Cue Analysis and Formulation - extractive PDF cue:** Ideally, this should handle dynamic object motion and camera pose estimation errors.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. Motivation behind the proposed temporal fusion. (a): VisionOcc pipeline. (b): Proposed temporal cues, showing historical motion and geometric data enhancing current viewpoints, with ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Multi-level temporal fusion in the VisionOcc pipeline. Volume features Vt, geometry Gt, motion Mt, and scene-adaptive parameters St are enhanced through RNN-style temporal ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Update dynamics of gradient descent-based temporal fusion pipeline. f t denotes the (geometry, motion, voxel-level, scene-level) feature of the current frame. Ht-1 and ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Comparison of our GDFusion and SOLOFusion w.r.t. memory consumption. SOLOFusion boosts performance with longer sequences but increases inference memory, while GDFu- sion achieves ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 2. Since Gt is predicted as discrete probabilities along the camera's line of sight, we seek to preserve its normal- ized probabilistic distribution. To ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison of 3D semantic occupancy prediction performance on the Occ3D dataset, evaluated with mIoUD, mIoU, and IoU metrics. Relative improvements are highlighted with ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Scaling-up experiment of 3D semantic occupancy pre- diction on the Occ3D dataset. The top three rows feature an input size of 900 × ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablations on improving RNN-based voxel-level fusion. epochs using CBGS [34] with a learning rate of 2 × 10-4 and a global batch size ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This dataset comprises 1,000 scenes in total, with 700 designated for 1510 | embodiment, simulator version and control stack | p. 6 (5. Experiment), p. 6 (5. Experiment) |
| Task/environment | Our experiments are based on the nuScenes dataset [3], which provides extensive data to develop and evaluate essential 3D perception algorithms. | reset, timeout, object/scene variation | p. 6 (5. Experiment), p. 3 (3.2. Temporal Cue Analysis and Formulation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 7 (5.1. Memory Consumption) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 7 (Method), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1. Comparison of 3D semantic occupancy prediction performance on the Occ3D dataset, evaluated with mIoUD, mIoU, and IoU metrics. Relative improvements are highlighted ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 1. Motivation behind the proposed temporal fusion. (a): VisionOcc pipeline. (b): Proposed temporal cues, showing historical motion and geometric data enhancing current viewpoints, ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Ideally, this should handle dynamic object motion and camera pose estimation errors. | definition/direction/unit from same section | p. 4 (3.2. Temporal Cue Analysis and Formulation) |
| The term Mt represents the offset intended to account for potential motion compensation and pose estimation error correction. | definition/direction/unit from same section | p. 4 (3.2. Temporal Cue Analysis and Formulation) |
| Figure 4. Comparison of our GDFusion and SOLOFusion w.r.t. memory consumption. SOLOFusion boosts performance with longer sequences but increases inference memory, while GDFu- sion ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Within the VisionOcc pipeline, we propose three distinct types of temporal information, each serving a unique role, as illustrated in Fig. | definition/direction/unit from same section | p. 3 (3.2. Temporal Cue Analysis and Formulation) |
| Figure 3. Update dynamics of gradient descent-based temporal fusion pipeline. f t denotes the (geometry, motion, voxel-level, scene-level) feature of the current frame. Ht-1 ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 3. Ablations on improving RNN-based voxel-level fusion. epochs using CBGS [34] with a learning rate of 2 × 10-4 and a global batch ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 4. Ablations on different temporal cues. B, G, V, S, and M represent baseline, temporal geometry fusion, voxel-level fusion, scene-level fusion, and temporal ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 4. Comparison of our GDFusion and SOLOFusion w.r.t. memory consumption. SOLOFusion boosts performance with longer sequences but increases inference memory, while GDFu- sion ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 1. Comparison of 3D semantic occupancy prediction performance on the Occ3D dataset, evaluated with mIoUD, mIoU, and IoU metrics. Relative improvements are highlighted ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 3. Ablations on improving RNN-based voxel-level fusion. epochs using CBGS [34] with a learning rate of 2 × 10-4 and a global batch ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3. Ablations on improving RNN-based voxel-level fusion. epochs using CBGS [34] with a learning rate of 2 × 10-4 and a global batch ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 4. Ablations on different temporal cues. B, G, V, S, and M represent baseline, temporal geometry fusion, voxel-level fusion, scene-level fusion, and temporal ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 5. Runtime analysis of key components, vs. SOLOFusion (16 frames). AutoGrad refers to PyTorch's automatic differentia- tion; Custom Matmul is our custom matrix ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This allows the RNN to operate on a wide array of diverse representation forms. iii) Through this reinterpretation, we propose a unified RNN-style temporal ... | Table 4. Ablations on different temporal cues. B, G, V, S, and M represent baseline, temporal geometry fusion, voxel-level fusion, scene-level fusion, and temporal ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | Figure 4. Comparison of our GDFusion and SOLOFusion w.r.t. memory consumption. SOLOFusion boosts performance with longer sequences but increases inference memory, while GDFu- sion ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 4 / 3.2. Temporal Cue Analysis and Formulation - extractive PDF cue:** Single-frame-sized historical states Ht-1 v , Ht-1 g , Ht-1 m , and Ht-1 s are stored in memory and updated frame-by-frame. information.
- **p. 6 / 5. Experiment - extractive PDF cue:** This dataset comprises 1,000 scenes in total, with 700 designated for 1510
- **p. 4 / 3.2. Temporal Cue Analysis and Formulation - extractive PDF cue:** Single-frame-sized historical states Ht-1 v , Ht-1 g , Ht-1 m , and Ht-1 s are stored in memory and updated frame-by-frame. information.
- **p. 7 / Method - extractive PDF cue:** It includes 18 semantic categories: 17 object classes plus an empty class for unoccupied regions.
- **p. 8 / 5.4. Wall-Clock Time - extractive PDF cue:** Each temporal fusion component consumes less than 6% of the total inference time (146.6ms), demonstrating the efficiency of GDFusion.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Thus, we propose temporal geometry fusion to yield a more robust geometric prior, detailed in Sec. | p. 4 (3.2. Temporal Cue Analysis and Formulation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Ablations on improving RNN-based voxel-level fusion. epochs using CBGS [34] with a learning rate of 2 × 10-4 and a global batch size of ... | p. 7 (Method) |
| Applying gradient descent with learning rate η: ht = ht-1 -η · 2A⊤(Aht-1 -Bxt). | p. 4 (4.1. Modeling RNN Dynamics via Gradient Descent) |
| Each temporal fusion component consumes less than 6% of the total inference time (146.6ms), demonstrating the efficiency of GDFusion. | p. 8 (5.4. Wall-Clock Time) |
| Accordingly, we design scene-level information to encode global properties, such as lighting, weather, and road characteristics. | p. 3 (3.2. Temporal Cue Analysis and Formulation) |
| To unify temporal fusion, we reinterpret standard RNN updates as gradient descent steps to minimize discrepancies between current and historical information. | p. 4 (4.1. Modeling RNN Dynamics via Gradient Descent) |
| The image and BEV augmentation strategies are the same as in the original BEVDet codebase [19]. | p. 7 (Method) |
| We conduct a runtime analysis of key components in GDFusion. | p. 8 (5.4. Wall-Clock Time) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / 3.2. Temporal Cue Analysis and Formulation - extractive PDF cue:** Thus, we propose temporal geometry fusion to yield a more robust geometric prior, detailed in Sec.

- **PDF anchors reviewed:** datasets p. 6 (5. Experiment), p. 6 (5. Experiment), p. 3 (3.2. Temporal Cue Analysis and Formulation), p. 4 (3.2. Temporal Cue Analysis and Formulation), p. 3 (3.2. Temporal Cue Analysis and Formulation), p. 4 (3.2. Temporal Cue Analysis and Formulation), metrics p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 4 (3.2. Temporal Cue Analysis and Formulation), p. 4 (3.2. Temporal Cue Analysis and Formulation), p. 6 (Figure/Table caption), p. 3 (3.2. Temporal Cue Analysis and Formulation), baselines p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
