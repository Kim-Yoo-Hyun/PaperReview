# Evaluation - Towards Learning to Complete Anything in Lidar

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vWPzKn6usZ; PDF retrieval source: https://openreview.net/pdf/8fbe2a59d85d4f1be15c6351679cc46349d858df.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.3. Pseudo-labeling engine analysis), p. 7 (4.2. Experimental results), p. 8 (4.2. Experimental results), p. 9 (4.3. Pseudo-labeling engine analysis), p. 9 (4.4. CAL model analysis), p. 7 (4.2. Experimental results)): While the best results are achieved with Tfw = 64, Tbw = 16, w = 1 (13.10 PQ†), we use the combination Tfw = 32 Tbw = 8, w = ...

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** We quantitatively assess CAL's zero-shot completion and recognition performance on Semantic Scene Completion (SSC) (Behley et al., 2019) and Panoptic Scene Completion (PSC) (Cao et ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** The hyperparameters used by our pseudo-labeling engine for each dataset are given in Appx.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** We evaluate our model's segmentation, completion, and recognition capabilities by specifying target classes (defined in each respective dataset) via prompts at test time (additional details ...
- **p. 7 / 4.2. Experimental results - extractive PDF cue:** Results reported on the SemanticKITTI dataset.
- **p. 7 / 4.2. Experimental results - extractive PDF cue:** 1 reports CAL results for SSC and PSC on the SemanticKITTI and SSCBench-KITTI360 datasets.
- **p. 8 / 4.3. Pseudo-labeling engine analysis - extractive PDF cue:** CRF refinement greatly improves pseudo-label quality on SemanticKITTI and SSCBench-KITTI360 datasets (Tab.
- **p. 8 / 4.2. Experimental results - extractive PDF cue:** Results show that CRF refinement significantly improves pseudo-label quality in both datasets and settings.
- **p. 9 / 4.4. CAL model analysis - extractive PDF cue:** Specifying C = 18 clusters (close to the number of annotated semantic groups in common datasets) yields the highest overall PQ.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setup (p. 5); 4.2. Experimental results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Pseudo-labeling engine analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | While the best results are achieved with Tfw = 64, Tbw = 16, w = 1 (13.10 PQ†), we use the combination Tfw = ... | p. 8 (4.3. Pseudo-labeling engine analysis) |
| 4.2. Experimental results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Specifically, we achieve 13.12 PQ† (49.51 % of PaSCo) and 13.09 mIoU (46.37 % of PaSCo) in the ZS setting on SemanticKITTI and further ... | p. 7 (4.2. Experimental results) |
| 4.2. Experimental results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Results show that CRF refinement significantly improves pseudo-label quality in both datasets and settings. | p. 8 (4.2. Experimental results) |
| 4.3. Pseudo-labeling engine analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Training with full coverage (Bfc o ) and Bs further improve performance. | p. 9 (4.3. Pseudo-labeling engine analysis) |
| 4.4. CAL model analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Introducing full coverage guidance (Bfc o ) and Bs improves performance in most settings. | p. 9 (4.4. CAL model analysis) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** We quantitatively assess CAL's zero-shot completion and recognition performance on Semantic Scene Completion (SSC) (Behley et al., 2019) and Panoptic Scene Completion (PSC) (Cao et ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** The hyperparameters used by our pseudo-labeling engine for each dataset are given in Appx.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** We evaluate our model's segmentation, completion, and recognition capabilities by specifying target classes (defined in each respective dataset) via prompts at test time (additional details ...
- **p. 7 / 4.2. Experimental results - extractive PDF cue:** Results reported on the SemanticKITTI dataset.
- **p. 7 / 4.2. Experimental results - extractive PDF cue:** 1 reports CAL results for SSC and PSC on the SemanticKITTI and SSCBench-KITTI360 datasets.
- **p. 8 / 4.3. Pseudo-labeling engine analysis - extractive PDF cue:** CRF refinement greatly improves pseudo-label quality on SemanticKITTI and SSCBench-KITTI360 datasets (Tab.
- **p. 8 / 4.2. Experimental results - extractive PDF cue:** Results show that CRF refinement significantly improves pseudo-label quality in both datasets and settings.
- **p. 9 / 4.4. CAL model analysis - extractive PDF cue:** Specifying C = 18 clusters (close to the number of annotated semantic groups in common datasets) yields the highest overall PQ.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Learning to Complete Anything in Lidar. Given a sparse Lidar point cloud, CAL (Complete Anything in Lidar) localizes, reconstructs, and, optionally, recognizes objects ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Pseudo-labeling engine. Given a calibrated RGB camera and Lidar sensor, 1⃝we use video-object segmentation models (Ravi et al., 2024) to localize object instances ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. CAL model architecture and training pipeline. The backbone consists of a sparse encoder and a dense 3D convolu- tional block. We estimate scene-level ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative results on SemanticKITTI. Given a single Lidar scan (1st col.), CAL completes object-level observations as a set of masks over the voxel ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Panoptic Scene Completion. We compare CAL against LMSCNet (Roldao et al., 2020) + MaskPLS (Marcuzzi et al., 2023), JS3CNet (Yan et al., 2021) ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Completion and amodal detection on KITTI-360. Given an input Lidar scan (left), CAL outputs a set of completed object shapes (middle). We visualize ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Panoptic scene completion results with zero-shot base- lines. We compare CAL against the zero-shot baselines we con- struct: LODE (Li et al., 2023b) ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6. Comparison to zero-shot baselines on SemanticKITTI. Given a single Lidar scan (1st col.), we compare CAL (4th col.) to zero-shot baselines (2nd and ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We quantitatively assess CAL's zero-shot completion and recognition performance on Semantic Scene Completion (SSC) (Behley et al., 2019) and Panoptic Scene Completion (PSC) (Cao ... | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Task/environment | The hyperparameters used by our pseudo-labeling engine for each dataset are given in Appx. | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2. Learning To Complete Objects), p. 3 (3. Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3.2. Learning To Complete Objects), p. 4 (3.1. Mining 3D Shape Priors From Unlabeled Data) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 15. Per-class performance analysis for Panoptic Scene Completion, evaluated on SemanticKITTI (Behley et al., 2019) dataset. Per-class scores for the baselines and class-frequencies ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| PQ† (Behley et al., 2021), and remove the minimum 0.5 IoU overlap requirement for stuff classes, as this can be too restrictive for regions ... | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| We visualize recognized objects (right) for queries ‘vehicle' (top), ‘car' (middle) and ‘tree' (bottom), and fit 3D bounding boxes to the identified object instances, ... | definition/direction/unit from same section | p. 7 (4.1. Experimental Setup) |
| We quantitatively assess CAL's zero-shot completion and recognition performance on Semantic Scene Completion (SSC) (Behley et al., 2019) and Panoptic Scene Completion (PSC) (Cao ... | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| This allows us to further decouple completion performance and semantic understanding. | definition/direction/unit from same section | p. 7 (4.1. Experimental Setup) |
| We observe similar performance with C ∈ {6, 18, 50, 100}, indicating general robustness to C. | definition/direction/unit from same section | p. 9 (4.4. CAL model analysis) |
| Table 10. Pseudo-label evaluation restricted to the areas in the voxel grid for which we have pseudo-labels. Analysis of the accuracy of pseudo-labels on ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Figure 8. Qualitative comparison to zero-shot baselines on SemanticKITTI. Given a single Lidar scan (1st col.), we compare our method (CAL, 4th col.) to ... | definition/direction/unit from same section | p. 25 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As there are no prior works tackling Lidar PSC in zero-shot setting, we construct two baselines adhering to the following criteria for a fair ... | comparison identity and matched condition | p. 7 (4.2. Experimental results) |
| 2, our method outperforms zero-shot baselines across nearly all metrics. | comparison identity and matched condition | p. 7 (4.2. Experimental results) |
| In contrast to baselines trained on ground-truth (GT) data, we use GT labels solely for evaluation and ablations. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| Pseudo-labeling engine ablations, semantic oracle (SO). | comparison identity and matched condition | p. 8 (4.2. Experimental results) |
| Given a single Lidar scan (1st col.), we compare CAL (4th col.) to zero-shot baselines (2nd and 3rd cols.) combining LiDiff (Nunes et al., ... | comparison identity and matched condition | p. 8 (4.2. Experimental results) |
| Training Components All Thing Stuff SSC Bpc o Bfc o S Bs PQ†↑PQ↑ SQ RQ PQ SQ RQ PQ SQ RQ mIoU↑ Semantic oracle ... | comparison identity and matched condition | p. 9 (4.3. Pseudo-labeling engine analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3. CRF refinement ablation. We evaluate pseudo-label quality with and without CRF refinement on SemanticKITTI and SSCBench- KITTI360. Results show that CRF refinement ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 12. Model ablations for data on SemanticKITTI. We train the CAL model using two different sets of data: pseudo-labels w/o CRF refinement, and ... | component/input/data sensitivity | p. 21 (Figure/Table caption) |
| 4.2), and ablations on design choices (Sec. | component/input/data sensitivity | p. 5 (4. Experiments) |
| (2024), we focus on the modified variant of PQ, i.e. | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| In contrast to baselines trained on ground-truth (GT) data, we use GT labels solely for evaluation and ablations. | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| We employ the LODE variant that does not use any semantic labels. | component/input/data sensitivity | p. 7 (4.2. Experimental results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose the first method for Zero-Shot Lidar Panoptic Scene Completion. | While the best results are achieved with Tfw = 64, Tbw = 16, w = 1 (13.10 PQ†), we use the combination Tfw = ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.3. Pseudo-labeling engine analysis), p. 7 (4.2. Experimental results), p. 8 (4.2. Experimental results), p. 9 (4.3. Pseudo-labeling engine analysis), p. 9 (4.4. CAL model analysis), p. 7 (4.2. Experimental results) |
| Primary metric/result | Specifically, we achieve 13.12 PQ† (49.51 % of PaSCo) and 13.09 mIoU (46.37 % of PaSCo) in the ZS setting on SemanticKITTI and further ... | numeric claim only at cited anchor | p. 7 (4.2. Experimental results) |

- Numeric sentences retained from the body:
- **p. 8 / 4.2. Experimental results - extractive PDF cue:** Pseudo-labels benefit from forward and backward propagation, with notable improvements up to Tfw = 32 and Tbw = 8 frames.
- **p. 3 / 3. Method - extractive PDF cue:** Semantic Scene Completion (SSC) (Behley et al., 2019) assumes input in the form of a single Lidar point cloud P = {pn}N n=1, pn ∈R4, ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We believe these are promising directions for future work. | p. 9 (5. Conclusion) |
| body limitation/failure cue | Table 7. Number of CLIP prototypes. We evaluate SSC/PSC performance on SemanticKITTI when varying the number of CLIP prototypes C. We observe similar performance ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | We employ the LODE variant that does not use any semantic labels. | p. 7 (4.2. Experimental results) |
| body limitation/failure cue | Fully supervised baselines have a clear advantage over CAL as they train on closed-set, noise-free annotations with full scene coverage. | p. 7 (4.2. Experimental results) |
| body limitation/failure cue | We observe no significant improvements between w = {1, 2} and a degradation in performance when increasing to w = 4 (10.97 PQ†) due ... | p. 8 (4.3. Pseudo-labeling engine analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4.3- 4.3) are discussed below, with further implementation details in the Appendix. | p. 5 (4. Experiments) |
| The hyperparameters used by our pseudo-labeling engine for each dataset are given in Appx. | p. 6 (4.1. Experimental Setup) |
| C.1) and assign labels based on cosine similarity between encoded text prompts and the predicted CLIP features fk. | p. 6 (4.1. Experimental Setup) |
| While the best results are achieved with Tfw = 64, Tbw = 16, w = 1 (13.10 PQ†), we use the combination Tfw = ... | p. 8 (4.3. Pseudo-labeling engine analysis) |
| We compute per-instance CLIP features following Ding et al. | p. 4 (3.1. Mining 3D Shape Priors From Unlabeled Data) |
| The backbone consists of a sparse feature encoder (●) (Choy et al., 2019) followed by a dense 3D convolutional block (●). | p. 4 (3.2. Learning To Complete Objects) |
| Further implementation details are provided in Appx. | p. 5 (3.2. Learning To Complete Objects) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5. Conclusion - extractive PDF cue:** We believe these are promising directions for future work.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 7. Number of CLIP prototypes. We evaluate SSC/PSC performance on SemanticKITTI when varying the number of CLIP prototypes C. We observe similar performance with ...
- **p. 7 / 4.2. Experimental results - extractive PDF cue:** We employ the LODE variant that does not use any semantic labels.
- **p. 7 / 4.2. Experimental results - extractive PDF cue:** Fully supervised baselines have a clear advantage over CAL as they train on closed-set, noise-free annotations with full scene coverage.
- **p. 8 / 4.3. Pseudo-labeling engine analysis - extractive PDF cue:** We observe no significant improvements between w = {1, 2} and a degradation in performance when increasing to w = 4 (10.97 PQ†) due to ...

- **PDF anchors reviewed:** datasets p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Experimental results), p. 7 (4.2. Experimental results), p. 8 (4.3. Pseudo-labeling engine analysis), metrics p. 23 (Figure/Table caption), p. 6 (4.1. Experimental Setup), p. 7 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 7 (4.1. Experimental Setup), p. 9 (4.4. CAL model analysis), baselines p. 7 (4.2. Experimental results), p. 7 (4.2. Experimental results), p. 6 (4.1. Experimental Setup), p. 8 (4.2. Experimental results), p. 8 (4.2. Experimental results), p. 9 (4.3. Pseudo-labeling engine analysis), results p. 8 (4.3. Pseudo-labeling engine analysis), p. 7 (4.2. Experimental results), p. 8 (4.2. Experimental results), p. 9 (4.3. Pseudo-labeling engine analysis), p. 9 (4.4. CAL model analysis), p. 7 (4.2. Experimental results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
