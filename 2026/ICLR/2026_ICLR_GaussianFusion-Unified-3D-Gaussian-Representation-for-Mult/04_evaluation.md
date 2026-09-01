# Evaluation - GaussianFusion: Unified 3D Gaussian Representation for Multi-Modal Fusion Perception

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=7jXxQ9bGoU; PDF retrieval source: https://openreview.net/pdf/78d270155a0832fed3175dbc6f35687fe7e3c822.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.1 DATASET), p. 9 (4.1 DATASET), p. 10 (4.1 DATASET), p. 9 (4.1 DATASET), p. 7 (4.1 DATASET), p. 7 (4.1 DATASET)): Experimental results show that, compared to BEVFusion4D (Liu et al., 2023b), our temporal variant GaussianFusion-T achieves significant improvements.

## Evaluation Body Digest

- **p. 7 / 4.1 DATASET - extractive PDF cue:** It is a large-scale multimodal dataset officially split into 700/150/150 scenes for training, validation, and testing, respectively.
- **p. 7 / 4.1 DATASET - extractive PDF cue:** The nuScenes dataset (Caesar et al., 2020) provides annotation data for tasks such as semantic segmentation, object detection, and 3D occupancy (Occ) prediction.
- **p. 8 / 4.1 DATASET - extractive PDF cue:** Published as a conference paper at ICLR 2026 Table 2: Comparisons with state-of-the-art 3D object detection methods on nuScenes dataset.
- **p. 9 / 4.1 DATASET - extractive PDF cue:** Published as a conference paper at ICLR 2026 Waymo Open Dataset Result.
- **p. 9 / 4.1 DATASET - extractive PDF cue:** We further conduct experiments on the Waymo Open Dataset (Sun et al., 2020) to evaluate the generalization capability of our approach.
- **p. 8 / 4.1 DATASET - extractive PDF cue:** All methods construct BEV-based feature maps instead of objectcentric fusion based on proposals, which means these methods can also be naturally used for semantic tasks.
- **p. 10 / 4.1 DATASET - extractive PDF cue:** Furthermore, UniTR exhibits significant object yaw errors (yellow marks).
- **p. 10 / 4.1 DATASET - extractive PDF cue:** For Occ, GaussianFusion-C produces sharper object boundaries (red marks) and better class separation (yellow marks) compared to GaussianFormer.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 7); 4.1 DATASET (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1 DATASET | SYSTEM / EVALUATION SCOPE UNRESOLVED | Experimental results show that, compared to BEVFusion4D (Liu et al., 2023b), our temporal variant GaussianFusion-T achieves significant improvements. | p. 8 (4.1 DATASET) |
| 4.1 DATASET | SYSTEM / EVALUATION SCOPE UNRESOLVED | More importantly, benefiting from our proposed Gaussian initialization strategy and iterative update mechanism, GaussianFusion-C achieves a 1.55 mIoU improvement and nearly 4.5! computational efficiency ... | p. 9 (4.1 DATASET) |
| 4.1 DATASET | SYSTEM / EVALUATION SCOPE UNRESOLVED | Results show that deformable attention with Gaussian priors outperforms the vanilla variant by +0.4 NDS, demonstrating that the shape prior encoded by Gaussians facilitates ... | p. 10 (4.1 DATASET) |
| 4.1 DATASET | SYSTEM / EVALUATION SCOPE UNRESOLVED | GaussianFusion outperforms the multi-modal SOTA method OccFusion (Ming et al., 2024), which is based on multi-scale voxel fusion, by +1.11 mIoU and significantly surpasses ... | p. 9 (4.1 DATASET) |
| 4.1 DATASET | SYSTEM / EVALUATION SCOPE UNRESOLVED | In addition, compared with recent SOTA fusion works, such as UniTR (Wang et al., 2023a), EA-LSS (Hu et al., 2023b), and FusionFormer-S (Hu et ... | p. 7 (4.1 DATASET) |

## Dataset / Benchmark Role

- **p. 7 / 4.1 DATASET - extractive PDF cue:** It is a large-scale multimodal dataset officially split into 700/150/150 scenes for training, validation, and testing, respectively.
- **p. 7 / 4.1 DATASET - extractive PDF cue:** The nuScenes dataset (Caesar et al., 2020) provides annotation data for tasks such as semantic segmentation, object detection, and 3D occupancy (Occ) prediction.
- **p. 8 / 4.1 DATASET - extractive PDF cue:** Published as a conference paper at ICLR 2026 Table 2: Comparisons with state-of-the-art 3D object detection methods on nuScenes dataset.
- **p. 9 / 4.1 DATASET - extractive PDF cue:** Published as a conference paper at ICLR 2026 Waymo Open Dataset Result.
- **p. 9 / 4.1 DATASET - extractive PDF cue:** We further conduct experiments on the Waymo Open Dataset (Sun et al., 2020) to evaluate the generalization capability of our approach.
- **p. 8 / 4.1 DATASET - extractive PDF cue:** All methods construct BEV-based feature maps instead of objectcentric fusion based on proposals, which means these methods can also be naturally used for semantic tasks.
- **p. 10 / 4.1 DATASET - extractive PDF cue:** Furthermore, UniTR exhibits significant object yaw errors (yellow marks).
- **p. 10 / 4.1 DATASET - extractive PDF cue:** For Occ, GaussianFusion-C produces sharper object boundaries (red marks) and better class separation (yellow marks) compared to GaussianFormer.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Table 1: Impact of BEV size on model performance
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Comparison of the discrete BEV repre- sentation fusion paradigm (Liu et al., 2023b) and our proposed continuous Gaussian representation fusion paradigm. B, G, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of the GaussianFusion framework. Initial Gaussians are refined by a shared encoder and fused in Gaussian space, followed by task-specific heads for ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Comparison of the vanilla deformable attention (Zhu et al., 2020) and our proposed deformable attention with Gaussian. Furthermore, we adopt deformable attention with ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Comparisons with state-of-the-art 3D object detection methods on nuScenes dataset. C denote Camera, L denote Lidar. All methods construct BEV-based feature maps instead ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Latency and performance on nuScenes val. set.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4: Comparison with temporal methods.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5: Semantic scene completion results on nuScenes (Wei et al., 2023; Caesar et al., 2020) val set. † represents trained on nuScenes. For Camera-only ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | It is a large-scale multimodal dataset officially split into 700/150/150 scenes for training, validation, and testing, respectively. | embodiment, simulator version and control stack | p. 7 (4.1 DATASET), p. 7 (4.1 DATASET) |
| Task/environment | The nuScenes dataset (Caesar et al., 2020) provides annotation data for tasks such as semantic segmentation, object detection, and 3D occupancy (Occ) prediction. | reset, timeout, object/scene variation | p. 7 (4.1 DATASET), p. 8 (4.1 DATASET) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (ABSTRACT), p. 2 (20560 M) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (20560 M), p. 3 (20560 M) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We utilize the official evaluation metric nuScenes Detection Score (NDS) and mean Average Precision (mAP) for 3D detection. | definition/direction/unit from same section | p. 7 (4.1 DATASET) |
| Method Latency → Memory → NDS ↑ mAP ↑ BEVFusion 156 ms 5140 M 71.4 68.5 GaussianFusion 132 ms 4271 M 74.0 71.7 Additionally, ... | definition/direction/unit from same section | p. 8 (4.1 DATASET) |
| We report the Intersection-over-Union (IoU) of occupied voxels as the evaluation metric of the class-agnostic scene completion task and the mIoU of all semantic ... | definition/direction/unit from same section | p. 9 (4.1 DATASET) |
| Furthermore, UniTR exhibits significant object yaw errors (yellow marks). | definition/direction/unit from same section | p. 10 (4.1 DATASET) |
| 4, in BEV object detection, compared to previous BEV-based SOTA methods like UniTR (Wang et al., 2023a) and BEVFusion(Liu et al., 2023b), GaussianFusion achieve ... | definition/direction/unit from same section | p. 10 (4.1 DATASET) |
| In addition, compared with recent SOTA fusion works, such as UniTR (Wang et al., 2023a), EA-LSS (Hu et al., 2023b), and FusionFormer-S (Hu et ... | definition/direction/unit from same section | p. 7 (4.1 DATASET) |
| Benefiting from the unified architecture, it achieves an excellent performance of 71.7 mAP while maintaining lower inference latency (132 ms) and memory consumption (4271 ... | definition/direction/unit from same section | p. 8 (4.1 DATASET) |
| The forward projection and Lidar projection strategies show comparable performance (74.0 NDS v.s 73.6 NDS), both outperforming the backward projection method (72.4 NDS). | definition/direction/unit from same section | p. 9 (4.1 DATASET) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In addition, compared with recent SOTA fusion works, such as UniTR (Wang et al., 2023a), EA-LSS (Hu et al., 2023b), and FusionFormer-S (Hu et ... | comparison identity and matched condition | p. 7 (4.1 DATASET) |
| Method Latency → Memory → NDS ↑ mAP ↑ BEVFusion 156 ms 5140 M 71.4 68.5 GaussianFusion 132 ms 4271 M 74.0 71.7 Additionally, ... | comparison identity and matched condition | p. 8 (4.1 DATASET) |
| As shown in Table 2, GaussianFusion achieves SOTA results compared to previous discrete BEV representation multimodal fusion methods(Liu et al., 2023b; Ge et al., ... | comparison identity and matched condition | p. 7 (4.1 DATASET) |
| Published as a conference paper at ICLR 2026 Table 2: Comparisons with state-of-the-art 3D object detection methods on nuScenes dataset. | comparison identity and matched condition | p. 8 (4.1 DATASET) |
| GaussianFusion outperforms the multi-modal SOTA method OccFusion (Ming et al., 2024), which is based on multi-scale voxel fusion, by +1.11 mIoU and significantly surpasses ... | comparison identity and matched condition | p. 9 (4.1 DATASET) |
| 4, in BEV object detection, compared to previous BEV-based SOTA methods like UniTR (Wang et al., 2023a) and BEVFusion(Liu et al., 2023b), GaussianFusion achieve ... | comparison identity and matched condition | p. 10 (4.1 DATASET) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Share Separate DA.G PE Offset NDS mAP ↭ ↭ ↭ ↭ 74.0 71.7 ↭ ↭ ↭ 73.6 71.1 ↭ ↭ ↭ ↭ 73.4 71.0 ... | component/input/data sensitivity | p. 9 (4.1 DATASET) |
| To highlight the effect of Gaussian representation, we only compare the BEV-based method. | component/input/data sensitivity | p. 7 (4.1 DATASET) |
| Experimental results show that, compared to BEVFusion4D (Liu et al., 2023b), our temporal variant GaussianFusion-T achieves significant improvements. | component/input/data sensitivity | p. 8 (4.1 DATASET) |
| Moreover, even without sophisticated temporal modeling, GaussianFusion-T achieves competitive NDS against advanced temporal fusion methods such as SparseLIF-T (Zhang et al., 2024a). | component/input/data sensitivity | p. 8 (4.1 DATASET) |
| Gaussian Initialization NDS mAP Random Initialization 71.2 68.3 Backward Projection 72.4 70.0 Lidar Projection 73.6 71.1 Forward Projection 74.0 71.7 Table 9: Ablation of ... | component/input/data sensitivity | p. 9 (4.1 DATASET) |
| We then conduct an ablation study on the deformable attention module. | component/input/data sensitivity | p. 10 (4.1 DATASET) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Main contributions are as follows: • We propose the first unified 3D Gaussian representation multi-modal fusion framework, where cross-view and cross-modal Gaussian representations are ... | Experimental results show that, compared to BEVFusion4D (Liu et al., 2023b), our temporal variant GaussianFusion-T achieves significant improvements. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.1 DATASET), p. 9 (4.1 DATASET), p. 10 (4.1 DATASET), p. 9 (4.1 DATASET), p. 7 (4.1 DATASET), p. 7 (4.1 DATASET) |
| Primary metric/result | More importantly, benefiting from our proposed Gaussian initialization strategy and iterative update mechanism, GaussianFusion-C achieves a 1.55 mIoU improvement and nearly 4.5! computational efficiency ... | numeric claim only at cited anchor | p. 9 (4.1 DATASET) |

- Numeric sentences retained from the body:
- **p. 7 / 4.1 DATASET - extractive PDF cue:** It is a large-scale multimodal dataset officially split into 700/150/150 scenes for training, validation, and testing, respectively.
- **p. 7 / 4.1 DATASET - extractive PDF cue:** Both BEV object detection and 3D semantic occupancy prediction are trained for 20 epochs, following the same settings as BEVFusion and GaussianFormer (H et al., ...
- **p. 8 / 4.1 DATASET - extractive PDF cue:** Method Latency → Memory → NDS ↑ mAP ↑ BEVFusion 156 ms 5140 M 71.4 68.5 GaussianFusion 132 ms 4271 M 74.0 71.7 Additionally, we ...
- **p. 8 / 4.1 DATASET - extractive PDF cue:** Benefiting from the unified architecture, it achieves an excellent performance of 71.7 mAP while maintaining lower inference latency (132 ms) and memory consumption (4271 MB) ...
- **p. 9 / 4.1 DATASET - extractive PDF cue:** Gaussians mIoU ↑ Latency → GaussianFormer 140,000 19.10 475 ms GaussianFusion-C 43,296 20.65 105 ms Results.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 4.7 LIMITATIONS Several approaches-covering both detection (Wang et al., 2023b) and Occ (Zhang et al., 2024b)-employ carefully designed temporal fusion modules to enhance performance. | p. 10 (4.1 DATASET) |
| body limitation/failure cue | A promising direction for future work is to explore motion-aware Gaussian updates, for instance by predicting velocity-guided offsets, enabling more coherent 4D scene modeling ... | p. 10 (4.1 DATASET) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We adopt the one-cycle learning rate policy (Smith, 2017) with a maximum learning rate of 2e↔4. | p. 7 (4.1 DATASET) |
| We set Gaussian Encoder blocks to 4, see the Appendix for experiments. | p. 7 (4.1 DATASET) |
| In Table 9, we first compare the shared and separate Gaussian Encoders. | p. 9 (4.1 DATASET) |
| We find that the shared Gaussian Encoder provides a performance improvement of +0.7 9 | p. 9 (4.1 DATASET) |
| This validates the effectiveness of the Gaussian encoder. | p. 10 (4.1 DATASET) |
| Results show that deformable attention with Gaussian priors outperforms the vanilla variant by +0.4 NDS, demonstrating that the shape prior encoded by Gaussians facilitates ... | p. 10 (4.1 DATASET) |
| For a Gaussian (GL ↓QL) associated with LiDAR feature QL ↔R3, the feature response at a 3D point p = (x, y, z) within ... | p. 5 (6 Cameras) |
| To achieve this, we design a novel forward-projection-based multi-modal Gaussian initialization module and a shared cross-modal Gaussian encoder that iteratively updates Gaussian properties based ... | p. 1 (ABSTRACT) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 4.1 DATASET - extractive PDF cue:** 4.7 LIMITATIONS Several approaches-covering both detection (Wang et al., 2023b) and Occ (Zhang et al., 2024b)-employ carefully designed temporal fusion modules to enhance performance.
- **p. 10 / 4.1 DATASET - extractive PDF cue:** A promising direction for future work is to explore motion-aware Gaussian updates, for instance by predicting velocity-guided offsets, enabling more coherent 4D scene modeling over ...

- **PDF anchors reviewed:** datasets p. 7 (4.1 DATASET), p. 7 (4.1 DATASET), p. 8 (4.1 DATASET), p. 9 (4.1 DATASET), p. 9 (4.1 DATASET), p. 8 (4.1 DATASET), metrics p. 7 (4.1 DATASET), p. 8 (4.1 DATASET), p. 9 (4.1 DATASET), p. 10 (4.1 DATASET), p. 10 (4.1 DATASET), p. 7 (4.1 DATASET), baselines p. 7 (4.1 DATASET), p. 8 (4.1 DATASET), p. 7 (4.1 DATASET), p. 8 (4.1 DATASET), p. 9 (4.1 DATASET), p. 10 (4.1 DATASET), results p. 8 (4.1 DATASET), p. 9 (4.1 DATASET), p. 10 (4.1 DATASET), p. 9 (4.1 DATASET), p. 7 (4.1 DATASET), p. 7 (4.1 DATASET).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
