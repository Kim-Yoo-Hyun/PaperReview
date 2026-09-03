# Evaluation - Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.14365; PDF retrieval source: https://arxiv.org/pdf/2304.14365. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (6 Experiments), p. 10 (6 Experiments), p. 18 (Figure/Table caption), p. 8 (6 Experiments), p. 9 (6 Experiments), p. 9 (6 Experiments)): For token selection, uncertain selection and top-k selection are on par and they significantly outperform the random selection as expected.

## Evaluation Body Digest

- **p. 8 / 6 Experiments - extractive body cue:** To benchmark our proposed Occ3D datasets and our CTF-Occ model, we evaluate existing 3D occupancy prediction methods on Occ3D-nuScenes and Occ3D-Waymo.
- **p. 9 / 6 Experiments - extractive body cue:** The resolution of the z-axis in each stage for the Occ3D-nuScenes dataset is 8 and 16 for the two pyramid stages.
- **p. 8 / 6 Experiments - extractive body cue:** Occ3D-nuScenes contains 700 training scenes and 150 validation scenes.
- **p. 9 / 6 Experiments - extractive body cue:** We also evaluate three existing 3D occupancy prediction methods - MonoScene [5], TPVFormer [16], and OccFormer [53] on our proposed Occ3D datasets.
- **p. 10 / 6 Experiments - extractive body cue:** 6.2 Comparing with previous methods Occ3D-nuScenes.
- **p. 10 / 6 Experiments - extractive body cue:** The observations are consistent with those in the Occ3D-Waymo dataset.
- **p. 10 / 6 Experiments - extractive body cue:** OHEM Loss Token Selection Strategy IoU mIoU random uncertain top-k PED CC ✓ 4.16 10.03 14.06 ✓ ✓ 5.07 12.95 16.62 ✓ ✓ 6.27 13.85 ...
- **p. 8 / 6 Experiments - extractive body cue:** We adopt the metrics of Intersection-over-Union (IoU) and mean Intersection-over-Union(mIoU) to evaluate performance.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 6 Experiments (p. 8); A Occ3D Dataset (p. 14); 46. When will the dataset be distributed? (p. 23); 2. If you are including theoretical results (p. 24); 3. If you ran experiments (e.g. for benchmarks) (p. 24).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 6 Experiments | BENCHMARK / DATASET | For token selection, uncertain selection and top-k selection are on par and they significantly outperform the random selection as expected. | p. 10 (6 Experiments) |
| 6 Experiments | BENCHMARK / DATASET | Both techniques improve performance. | p. 10 (6 Experiments) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 8: Occlusion reasoning and camera visibility. Grey voxels are unobserved in the LiDAR view and red voxels are observed in the accumulative LiDAR ... | p. 18 (Figure/Table caption) |
| 6 Experiments | BENCHMARK / DATASET | We adopt the metrics of Intersection-over-Union (IoU) and mean Intersection-over-Union(mIoU) to evaluate performance. | p. 8 (6 Experiments) |
| 6 Experiments | BENCHMARK / DATASET | Each stage contains one SCA layer and an incremental token selection module to choose K non-empty voxels with the highest scores. | p. 9 (6 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 6 Experiments - extractive body cue:** To benchmark our proposed Occ3D datasets and our CTF-Occ model, we evaluate existing 3D occupancy prediction methods on Occ3D-nuScenes and Occ3D-Waymo.
- **p. 9 / 6 Experiments - extractive body cue:** The resolution of the z-axis in each stage for the Occ3D-nuScenes dataset is 8 and 16 for the two pyramid stages.
- **p. 8 / 6 Experiments - extractive body cue:** Occ3D-nuScenes contains 700 training scenes and 150 validation scenes.
- **p. 9 / 6 Experiments - extractive body cue:** We also evaluate three existing 3D occupancy prediction methods - MonoScene [5], TPVFormer [16], and OccFormer [53] on our proposed Occ3D datasets.
- **p. 10 / 6 Experiments - extractive body cue:** 6.2 Comparing with previous methods Occ3D-nuScenes.
- **p. 10 / 6 Experiments - extractive body cue:** The observations are consistent with those in the Occ3D-Waymo dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Our Occ3D dataset demonstrates rich semantic and geometric expressiveness. (a) Diversity of scenes in the Occ3D dataset; (b) Out-of-vocabulary objects, also known as ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: (1) 3D bounding box representation erases the geometric details of objects, a construction vehicle has a mechanical arm that protrudes from the main ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1: Dataset comparison. Comparing Occ3D Datasets with other occupancy prediction datasets. Surround = ✓represents surround-view image inputs. C, D, L denote camera, depth and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of the label generation pipeline. The pipeline consists of three main steps: voxel densification, occlusion reasoning, and image-guided voxel refinement.Voxel densification consists ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Initially, in voxel densification, we increase the density of the point clouds by performing multi-frame aggregation for both static and dynamic objects separately. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Visibility and refinement. (a) LiDAR visibility: a voxel is "occupied" if it reflects LiDAR (red voxels), or "free" if it is traversed through ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: 3D-2D consistency (a) 2D ROI within single-frame LiDAR scan range. (b) Semantic labels of a single image within the 2D ROI. (c) The ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Quantitative results for design choices. SFP, single frame points; MFP, aggregating points from unlabeled frames; VS, short for voxel size; Mesh, showcasing mesh ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To benchmark our proposed Occ3D datasets and our CTF-Occ model, we evaluate existing 3D occupancy prediction methods on Occ3D-nuScenes and Occ3D-Waymo. | embodiment, simulator version and control stack | p. 8 (6 Experiments), p. 9 (6 Experiments) |
| Task/environment | The resolution of the z-axis in each stage for the Occ3D-nuScenes dataset is 8 and 16 for the two pyramid stages. | reset, timeout, object/scene variation | p. 9 (6 Experiments), p. 8 (6 Experiments) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 1 (Abstract) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 2 (1 Introduction), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| OHEM Loss Token Selection Strategy IoU mIoU random uncertain top-k PED CC ✓ 4.16 10.03 14.06 ✓ ✓ 5.07 12.95 16.62 ✓ ✓ 6.27 ... | definition/direction/unit from same section | p. 10 (6 Experiments) |
| We adopt the metrics of Intersection-over-Union (IoU) and mean Intersection-over-Union(mIoU) to evaluate performance. | definition/direction/unit from same section | p. 8 (6 Experiments) |
| Table 2: Quantitative results for design choices. SFP, single frame points; MFP, aggregating points from unlabeled frames; VS, short for voxel size; Mesh, showcasing ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 5: The architecture of CTF-Occ network. CTF-Occ consists of an image backbone, a coarse-to-fine voxel encoder, and an implicit occupancy decoder. in a ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Each stage contains one SCA layer and an incremental token selection module to choose K non-empty voxels with the highest scores. | definition/direction/unit from same section | p. 9 (6 Experiments) |
| It can be observed that our method performs better in all classes than previous baseline methods under the IoU metric. | definition/direction/unit from same section | p. 10 (6 Experiments) |
| Figure 8: Occlusion reasoning and camera visibility. Grey voxels are unobserved in the LiDAR view and red voxels are observed in the accumulative LiDAR ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Figure 2: Overview of the label generation pipeline. The pipeline consists of three main steps: voxel densification, occlusion reasoning, and image-guided voxel refinement.Voxel densification ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method outperforms previous methods by remarkable margins, increasing the mIoU by 1.97. | comparison identity and matched condition | p. 10 (6 Experiments) |
| It can be observed that our method performs better in all classes than previous baseline methods under the IoU metric. | comparison identity and matched condition | p. 10 (6 Experiments) |
| The voxel embedding will first pass through four encoder layers without token selection. | comparison identity and matched condition | p. 9 (6 Experiments) |
| Table 1: Dataset comparison. Comparing Occ3D Datasets with other occupancy prediction datasets. Surround = ✓represents surround-view image inputs. C, D, L denote camera, depth ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Figure 5: The architecture of CTF-Occ network. CTF-Occ consists of an image backbone, a coarse-to-fine voxel encoder, and an implicit occupancy decoder. in a ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The voxel embedding will first pass through four encoder layers without token selection. | component/input/data sensitivity | p. 9 (6 Experiments) |
| Without the OHEM loss, we only get 14.06 mIoU. | component/input/data sensitivity | p. 10 (6 Experiments) |
| 6.3 Ablation study In this section, we ablate the choices of incremental token selection and OHEM loss. | component/input/data sensitivity | p. 10 (6 Experiments) |
| Figure 5: The architecture of CTF-Occ network. CTF-Occ consists of an image backbone, a coarse-to-fine voxel encoder, and an implicit occupancy decoder. in a ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We replace their original detection decoders with the occupancy decoder adopted in our CTF-Occ network and remain their BEV feature encoders. | component/input/data sensitivity | p. 9 (6 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contributions of this work are as follows: (1) We introduce Occ3D, a high-quality 3D occupancy prediction benchmark to facilitate research in this emerging ... | For token selection, uncertain selection and top-k selection are on par and they significantly outperform the random selection as expected. | PDF body cue; verify exact table/figure and matched conditions | p. 10 (6 Experiments), p. 10 (6 Experiments), p. 18 (Figure/Table caption), p. 8 (6 Experiments), p. 9 (6 Experiments), p. 9 (6 Experiments) |
| Primary metric/result | Both techniques improve performance. | numeric claim only at cited anchor | p. 10 (6 Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / 6 Experiments - extractive body cue:** Occ3D-Waymo contains 1,000 publicly available sequences in total, where 798 scenes are for training and 202 scenes are for validation.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1: (1) 3D bounding box representation erases the geometric details of objects, a construction vehicle has a mechanical arm that protrudes from the ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 1: Our Occ3D dataset demonstrates rich semantic and geometric expressiveness. (a) Diversity of scenes in the Occ3D dataset; (b) Out-of-vocabulary objects, also known ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: Overview of the label generation pipeline. The pipeline consists of three main steps: voxel densification, occlusion reasoning, and image-guided voxel refinement.Voxel densification ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. Initially, in voxel densification, we increase the density of the point clouds by performing multi-frame aggregation for both static and dynamic objects ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Figure 8: Occlusion reasoning and camera visibility. Grey voxels are unobserved in the LiDAR view and red voxels are observed in the accumulative LiDAR ... | p. 18 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The voxel embedding will first pass through four encoder layers without token selection. | p. 9 (6 Experiments) |
| We replace their original detection decoders with the occupancy decoder adopted in our CTF-Occ network and remain their BEV feature encoders. | p. 9 (6 Experiments) |
| The results indicate the effectiveness of our coarse-to-fine voxel encoder. | p. 10 (6 Experiments) |
| We focus on CC and PED to verify the effectiveness of our implementation on small objects. | p. 10 (6 Experiments) |
| To overcome these hurdles, we create a semi-automatic label generation pipeline that consists of three steps: voxel densification, occlusion reasoning, and image-guided voxel refinement. | p. 2 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: (1) 3D bounding box representation erases the geometric details of objects, a construction vehicle has a mechanical arm that protrudes from the main ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Our Occ3D dataset demonstrates rich semantic and geometric expressiveness. (a) Diversity of scenes in the Occ3D dataset; (b) Out-of-vocabulary objects, also known as ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of the label generation pipeline. The pipeline consists of three main steps: voxel densification, occlusion reasoning, and image-guided voxel refinement.Voxel densification consists ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Initially, in voxel densification, we increase the density of the point clouds by performing multi-frame aggregation for both static and dynamic objects separately. ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 8: Occlusion reasoning and camera visibility. Grey voxels are unobserved in the LiDAR view and red voxels are observed in the accumulative LiDAR view ...

- **Evidence anchors reviewed:** datasets p. 8 (6 Experiments), p. 9 (6 Experiments), p. 8 (6 Experiments), p. 9 (6 Experiments), p. 10 (6 Experiments), p. 10 (6 Experiments), metrics p. 10 (6 Experiments), p. 8 (6 Experiments), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (6 Experiments), p. 10 (6 Experiments), baselines p. 10 (6 Experiments), p. 10 (6 Experiments), p. 9 (6 Experiments), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 10 (6 Experiments), p. 10 (6 Experiments), p. 18 (Figure/Table caption), p. 8 (6 Experiments), p. 9 (6 Experiments), p. 9 (6 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
