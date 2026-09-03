# Evaluation - Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=nI7wKr4eop; PDF retrieval source: https://arxiv.org/pdf/2506.04789. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption), p. 7 (4 Experiments), p. 20 (Figure/Table caption)): While Object-X achieves lower SSIM and PSNR compared to 3DGS (12V), it significantly outperforms all methods in geometric accuracy.

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive body cue:** Since the test set lacks such annotations, we reorganized the original validation split, allocating 34 scenes (17 rooms) for validation and 123 scenes (30 rooms) ...
- **p. 7 / 4 Experiments - extractive body cue:** The dataset provides semantically annotated 3D point clouds, with certain scenes captured over extended periods to reflect environmental changes.
- **p. 8 / 4 Experiments - extractive body cue:** Since we train on 3RScan, comparisons on this dataset may be unfavorable to DepthSplat.
- **p. 8 / 4 Experiments - extractive body cue:** Note that we did not train our model on this dataset and used the model trained on 3RScan.
- **p. 6 / 4 Experiments - extractive body cue:** Next, we will provide experiments on various tasks benefiting from Object-X.
- **p. 7 / 4 Experiments - extractive body cue:** We report NVS scores (SSIM, PSNR, LPIPS), geometric accuracy (Accuracy, Completion, and F1 score at a 0.05 m threshold), per-object run-time (secs), and storage (MB).
- **p. 8 / 4 Experiments - extractive body cue:** Additionally, we report standard geometric metrics: accuracy, completeness, and F1 score.
- **p. 7 / 4 Experiments - extractive body cue:** This allows us to assess robustness to errors in 3D instance segmentation in the practical setting.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 6); A.4 Evaluation Summary (p. 21).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | While Object-X achieves lower SSIM and PSNR compared to 3DGS (12V), it significantly outperforms all methods in geometric accuracy. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Object-X produces significantly smoother renderings and higher-quality meshes, whereas meshes reconstructed by baselines exhibit strong artifacts and fail to achieve accurate geometry. | p. 8 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5: Comparison of (a) object reconstruction and (b) coarse localization performance using 3DGS and Object-X across tasks and input modalities. highest geometric accuracy ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3: Full-scene composition on 3RScan [27]. We compare Object-X to 3DGS [28] optimized on all unmasked images, and two 12-view baselines: 3DGS (12V) ... | p. 10 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We report NVS scores (SSIM, PSNR, LPIPS), geometric accuracy (Accuracy, Completion, and F1 score at a 0.05 m threshold), per-object run-time (secs), and storage ... | p. 7 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive body cue:** Since the test set lacks such annotations, we reorganized the original validation split, allocating 34 scenes (17 rooms) for validation and 123 scenes (30 rooms) ...
- **p. 7 / 4 Experiments - extractive body cue:** The dataset provides semantically annotated 3D point clouds, with certain scenes captured over extended periods to reflect environmental changes.
- **p. 8 / 4 Experiments - extractive body cue:** Since we train on 3RScan, comparisons on this dataset may be unfavorable to DepthSplat.
- **p. 8 / 4 Experiments - extractive body cue:** Note that we did not train our model on this dataset and used the model trained on 3RScan.
- **p. 6 / 4 Experiments - extractive body cue:** Next, we will provide experiments on various tasks benefiting from Object-X.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Object-X learns object-centric embeddings from an input object segmentation of a 3D scene reconstruction. The embeddings learned from multi-modal data (e.g., mesh, images, ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Overview of Object-X, learning object embeddings to reconstruct 3D Gaussians and support other tasks such as visual localization [14]. (a) The method takes ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: The proposed Object-X learns per-object embeddings that are beneficial for a number of downstream tasks, besides object-wise 3DGS reconstruction, such as cross-modal visual ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Object reconstructions. Each row shows an input object (left) and its reconstruction obtained by, from left to right: (i) 3DGS [28] optimized on ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: 3DGS Object reconstruction photometric quality, geometric accuracy, runtime, and storage efficiency on 3RScan [27] and ScanNet [4]. We compare Object-X with baselines that ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Comparison of (a) object reconstruction and (b) coarse localization performance using 3DGS and Object-X across tasks and input modalities. highest geometric accuracy by ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Comparison with MIDI [8] on a subset of 3RScan. Metrics are computed at a 5 cm threshold. Methods marked with * use automatic ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 3: Full-scene composition on 3RScan [27]. We compare Object-X to 3DGS [28] optimized on all unmasked images, and two 12-view baselines: 3DGS (12V) and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Since the test set lacks such annotations, we reorganized the original validation split, allocating 34 scenes (17 rooms) for validation and 123 scenes (30 ... | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | The dataset provides semantically annotated 3D point clouds, with certain scenes captured over extended periods to reflect environmental changes. | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (1 Introduction), p. 4 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1 Introduction), p. 9 (Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report NVS scores (SSIM, PSNR, LPIPS), geometric accuracy (Accuracy, Completion, and F1 score at a 0.05 m threshold), per-object run-time (secs), and storage ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Additionally, we report standard geometric metrics: accuracy, completeness, and F1 score. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| This allows us to assess robustness to errors in 3D instance segmentation in the practical setting. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Figure 2: Overview of Object-X, learning object embeddings to reconstruct 3D Gaussians and support other tasks such as visual localization [14]. (a) The method ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 5: Comparison of (a) object reconstruction and (b) coarse localization performance using 3DGS and Object-X across tasks and input modalities. highest geometric accuracy ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| To evaluate the geometric accuracy, we extract a triangle mesh from the optimized 3D Gaussians, following the procedure from 2DGS [41]. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| Object-X substantially outperforms all baselines in geometric accuracy. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Table 3: Full-scene composition on 3RScan [27]. We compare Object-X to 3DGS [28] optimized on all unmasked images, and two 12-view baselines: 3DGS (12V) ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Even without training, we achieve the highest novel view synthesis scores compared to the baselines, being the closest to the reference 3DGS reconstruction. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Our geometric accuracy significantly outperforms all baselines. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Figure 8: Qualitative comparison for full-scene composition. We compare the proposed Object-X to standard 3DGS [28] optimized on all unmasked scene images, and two ... | comparison identity and matched condition | p. 23 (Figure/Table caption) |
| Ablation studies, more visuals, and detailed descriptions of baselines are provided in the supplementary material. | comparison identity and matched condition | p. 6 (4 Experiments) |
| 3DGS [10] serves as a high-fidelity baseline, representing each object as a set of 3D Gaussians. | comparison identity and matched condition | p. 7 (4 Experiments) |
| Compared to 3RScan, ScanNet captures RGB-D sequences at a higher frame rate with minimal motion between consecutive frames. | comparison identity and matched condition | p. 7 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Objects without available images were removed to ensure a consistent evaluation. | component/input/data sensitivity | p. 7 (4 Experiments) |
| Table 7: Ablation study on occlusion. Before encoding an object, we randomly select a point on its surface and remove all parts within a ... | component/input/data sensitivity | p. 26 (Figure/Table caption) |
| Table 6: Ablation study on latent dimensions. Mean and median LPIPS and PSNR on a subset of scans from the test set. We compare ... | component/input/data sensitivity | p. 26 (Figure/Table caption) |
| Ablation studies, more visuals, and detailed descriptions of baselines are provided in the supplementary material. | component/input/data sensitivity | p. 6 (4 Experiments) |
| As in 3RScan, objects without associated images are discarded. | component/input/data sensitivity | p. 7 (4 Experiments) |
| Even without training, we achieve the highest novel view synthesis scores compared to the baselines, being the closest to the reference 3DGS reconstruction. | component/input/data sensitivity | p. 8 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 3 Learning Versatile Object Embeddings We propose Object-X, taking a reconstructed scene with a 3D object segmentation as input and learning a compact and ... | While Object-X achieves lower SSIM and PSNR compared to 3DGS (12V), it significantly outperforms all methods in geometric accuracy. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption), p. 7 (4 Experiments), p. 20 (Figure/Table caption) |
| Primary metric/result | Object-X produces significantly smoother renderings and higher-quality meshes, whereas meshes reconstructed by baselines exhibit strong artifacts and fail to achieve accurate geometry. | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** The 3RScan dataset [27] consists of 1,335 annotated indoor scenes covering 432 distinct spaces, with 1,178 scenes (385 rooms) used for training and 157 scenes ...
- **p. 7 / 4 Experiments - extractive body cue:** Since the test set lacks such annotations, we reorganized the original validation split, allocating 34 scenes (17 rooms) for validation and 123 scenes (30 rooms) ...
- **p. 7 / 4 Experiments - extractive body cue:** To ensure diverse viewpoints, we sample one image every 25 frames.
- **p. 8 / 4 Experiments - extractive body cue:** We are four orders of magnitude faster than 3DGS (4V) and 2DGS (4V) requiring 3 ms to reconstruct an object on average.
- **p. 9 / Method - extractive body cue:** Following the protocol from SceneGraphLoc [14], we evaluate on 123 scenes from 30 rooms in the test set.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Despite these advances, Object-X has limitations. | p. 10 (5 Conclusion) |
| body limitation/failure cue | Furthermore, while promising in zero-shot scenarios for tasks like single-image object reconstruction, performance does not yet consistently match that of optimized task-specific methods. | p. 10 (5 Conclusion) |
| body limitation/failure cue | Scenes, where SceneGraphFusion fails to generate annotations, are excluded. | p. 7 (4 Experiments) |
| body limitation/failure cue | Since ScanNet does not provide scene graph annotations, we apply SceneGraphFusion [30] on RGB-D sequences to generate 3D instance segmentations and object relationships (used ... | p. 7 (4 Experiments) |
| body limitation/failure cue | We omit geometric results for DepthSplat [32], which failed to produce reasonable geometry. | p. 8 (4 Experiments) |
| body limitation/failure cue | This reduces storage compared to full 3DGS but introduces a trade-off: reconstruction takes longer, and the quality may be slightly degraded. | p. 8 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All experiments are conducted on a machine with an A100 GPU with 80GB of RAM. | p. 6 (4 Experiments) |
| First, we evaluate the Object-X decoder in terms of storage efficiency, geometric fidelity, and visual quality on the object reconstruction task. | p. 7 (4 Experiments) |
| We report NVS scores (SSIM, PSNR, LPIPS), geometric accuracy (Accuracy, Completion, and F1 score at a 0.05 m threshold), per-object run-time (secs), and storage ... | p. 7 (4 Experiments) |
| Our runtime is three orders of magnitude faster than methods relying on optimization. | p. 8 (4 Experiments) |
| This demonstrates that the proposed U-3DGS embeddings effectively capture object geometry, accurately recovered by the Object-X decoder. | p. 8 (4 Experiments) |
| Metrics are computed at a 5 cm threshold. | p. 9 (Method) |
| Runtime remains comparable to the 12-view baselines, and significantly faster than full-scene 3DGS optimization. | p. 9 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5 Conclusion - extractive body cue:** Despite these advances, Object-X has limitations.
- **p. 10 / 5 Conclusion - extractive body cue:** Furthermore, while promising in zero-shot scenarios for tasks like single-image object reconstruction, performance does not yet consistently match that of optimized task-specific methods.
- **p. 7 / 4 Experiments - extractive body cue:** Scenes, where SceneGraphFusion fails to generate annotations, are excluded.
- **p. 7 / 4 Experiments - extractive body cue:** Since ScanNet does not provide scene graph annotations, we apply SceneGraphFusion [30] on RGB-D sequences to generate 3D instance segmentations and object relationships (used for ...
- **p. 8 / 4 Experiments - extractive body cue:** We omit geometric results for DepthSplat [32], which failed to produce reasonable geometry.
- **p. 8 / 4 Experiments - extractive body cue:** This reduces storage compared to full 3DGS but introduces a trade-off: reconstruction takes longer, and the quality may be slightly degraded.

- **Evidence anchors reviewed:** datasets p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), metrics p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 3 (Figure/Table caption), p. 9 (Figure/Table caption), p. 6 (4 Experiments), baselines p. 8 (4 Experiments), p. 8 (4 Experiments), p. 23 (Figure/Table caption), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), results p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption), p. 7 (4 Experiments), p. 20 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
