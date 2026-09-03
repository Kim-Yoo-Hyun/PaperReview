# Evaluation - How Do Images Align and Complement LiDAR? Towards a Harmonized Multi-modal 3D Panoptic Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=F7BOaYmWl7; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/167147. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.2. Benchmark Results), p. 8 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results), p. 9 (4.5. Qualitative Results and Discussion), p. 9 (4.5. Qualitative Results and Discussion), p. 7 (4.2. Benchmark Results)): As shown in Table 4, despite these constraints, our IAL achieves a 4.1% improvement in PQ over the state-of-the-art multi-modal baseline LCPS, demonstrating the robustness of our method even under ...

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setting - extractive body cue:** SemanticKITTI (Behley et al., 2019; 2021) is an outdoor dataset derived from KITTI Vision Benchmark (Geiger et al., 2012).
- **p. 6 / 4.1. Experimental Setting - extractive body cue:** Datasts. nuScenes (Caesar et al., 2020; Fong et al., 2022) is a large-scale, multi-modal dataset designed for autonomous driving, containing data from a 32-beam LiDAR, ...
- **p. 7 / 4.2. Benchmark Results - extractive body cue:** We present comprehensive comparison results for LiDAR panoptic segmentation performance on the nuScenes validation and test sets, as shown in Table 2 and Table 3.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** All experiments are conducted on the nuScenes validation set using the same hyper-parameters for fair comparison.
- **p. 9 / 4.5. Qualitative Results and Discussion - extractive body cue:** We present qualitative evaluations on nuScenes validation set.
- **p. 7 / 4.1. Experimental Setting - extractive body cue:** The training spans 80 epochs for nuScenes and 36 epochs for SemanticKITTI.
- **p. 8 / 4.2. Benchmark Results - extractive body cue:** In Table 3, IAL also demonstrates superior performance, achieving the highest scores across most metrics on the nuScenes leaderboard.
- **p. 9 / 4.5. Qualitative Results and Discussion - extractive body cue:** Furthermore, IAL outperforms its LiDAR branch in detecting remote objects (highlighted in the black boxes) and recognizing ambiguous classes (in yellow boxes), leveraging the assistance ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experimental Results (p. 6); 4.1. Experimental Setting (p. 6); 4.2. Benchmark Results (p. 7); 4.5. Qualitative Results and Discussion (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Benchmark Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 4, despite these constraints, our IAL achieves a 4.1% improvement in PQ over the state-of-the-art multi-modal baseline LCPS, demonstrating the ... | p. 8 (4.2. Benchmark Results) |
| 4.2. Benchmark Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared to the LiDAR-only baseline (using the same augmentation strategies as P3Former adopts), IAL achieves a 5.3% improvement, primarily due to a 7.5% increase ... | p. 8 (4.2. Benchmark Results) |
| 4.2. Benchmark Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notably, our method IAL achieves the best performance across all metrics on the validation set and ranks first or second on most metrics 7 | p. 7 (4.2. Benchmark Results) |
| 4.5. Qualitative Results and Discussion | EMPIRICAL / SOURCE-REPORTED EVALUATION | IAL showcases significant performance improvements in: (1) distinguishing multiple objects when they are clustered together (rows 1 and 2); (2) detecting distant objects (row ... | p. 9 (4.5. Qualitative Results and Discussion) |
| 4.5. Qualitative Results and Discussion | EMPIRICAL / SOURCE-REPORTED EVALUATION | Furthermore, IAL outperforms its LiDAR branch in detecting remote objects (highlighted in the black boxes) and recognizing ambiguous classes (in yellow boxes), leveraging the ... | p. 9 (4.5. Qualitative Results and Discussion) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setting - extractive body cue:** SemanticKITTI (Behley et al., 2019; 2021) is an outdoor dataset derived from KITTI Vision Benchmark (Geiger et al., 2012).
- **p. 6 / 4.1. Experimental Setting - extractive body cue:** Datasts. nuScenes (Caesar et al., 2020; Fong et al., 2022) is a large-scale, multi-modal dataset designed for autonomous driving, containing data from a 32-beam LiDAR, ...
- **p. 7 / 4.2. Benchmark Results - extractive body cue:** We present comprehensive comparison results for LiDAR panoptic segmentation performance on the nuScenes validation and test sets, as shown in Table 2 and Table 3.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** All experiments are conducted on the nuScenes validation set using the same hyper-parameters for fair comparison.
- **p. 9 / 4.5. Qualitative Results and Discussion - extractive body cue:** We present qualitative evaluations on nuScenes validation set.
- **p. 7 / 4.1. Experimental Setting - extractive body cue:** The training spans 80 epochs for nuScenes and 36 epochs for SemanticKITTI.
- **p. 8 / 4.2. Benchmark Results - extractive body cue:** In Table 3, IAL also demonstrates superior performance, achieving the highest scores across most metrics on the nuScenes leaderboard.
- **p. 9 / 4.5. Qualitative Results and Discussion - extractive body cue:** Furthermore, IAL outperforms its LiDAR branch in detecting remote objects (highlighted in the black boxes) and recognizing ambiguous classes (in yellow boxes), leveraging the assistance ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. The architecture overview of our Image-Assists-LiDAR (IAL) framework. We first voxelize the point cloud into cylindrical voxels. In PieAug, we synchronize augmentation by ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Motivation and implementation variants of PieAug. Each column illustrates the motivation for LiDAR-image syn- chronized augmentation. Each row displays a different pie-cut strategy. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. (a) and (b) illustrate two challenges in LiDAR-image fusion introduced by cylindrical voxelization. In (a), relying on a virtual voxel center can lead ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Preliminary study of positional embedding for objects of thing classes. We conduct the experiment on our LiDAR branch. "GT" denotes using the ground ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Comparison of panoptic segmentation performance on the nuScenes validation set. Top results are shown in bold. "M." indicates which modality (or modalities) each ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Comparison on the nuScenes test set. Top and runner-up results are marked in bold and underline, respectively. "*" indicates the use of additional ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Comparison of panoptic segmentation performance on the SemanticKITTI validation set. Top results are shown in bold.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Ablation study of the proposed modules in our framework. "PIE" denotes the PieAug module. PIE GTF PQG PQ PQ† RQ

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | SemanticKITTI (Behley et al., 2019; 2021) is an outdoor dataset derived from KITTI Vision Benchmark (Geiger et al., 2012). | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setting), p. 6 (4.1. Experimental Setting) |
| Task/environment | Datasts. nuScenes (Caesar et al., 2020; Fong et al., 2022) is a large-scale, multi-modal dataset designed for autonomous driving, containing data from a 32-beam ... | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setting), p. 7 (4.2. Benchmark Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (3.3. Prior-Based Query Generation), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In Table 3, IAL also demonstrates superior performance, achieving the highest scores across most metrics on the nuScenes leaderboard. | definition/direction/unit from same section | p. 8 (4.2. Benchmark Results) |
| As illustrated in the error maps in Fig. | definition/direction/unit from same section | p. 9 (4.5. Qualitative Results and Discussion) |
| Figure 3. (a) and (b) illustrate two challenges in LiDAR-image fusion introduced by cylindrical voxelization. In (a), relying on a virtual voxel center can ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Furthermore, our model demonstrates superior performance on both "thing" and "stuff" classes, achieving a 7.8% and 1.1% improvement in metrics compared to the latest ... | definition/direction/unit from same section | p. 8 (4.2. Benchmark Results) |
| Comparison of panoptic segmentation performance on the nuScenes validation set. | definition/direction/unit from same section | p. 7 (4.1. Experimental Setting) |
| We set the ratio of application for these three augmentation strategies to 0.4:0.05:0.05, respectively. | definition/direction/unit from same section | p. 7 (4.1. Experimental Setting) |
| IAL showcases significant performance improvements in: (1) distinguishing multiple objects when they are clustered together (rows 1 and 2); (2) detecting distant objects (row ... | definition/direction/unit from same section | p. 9 (4.5. Qualitative Results and Discussion) |
| Figure 1. The architecture overview of our Image-Assists-LiDAR (IAL) framework. We first voxelize the point cloud into cylindrical voxels. In PieAug, we synchronize augmentation ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in Table 5, compared to the baseline that uses only basic point cloud transformations (row 1), PieAug improves PQ by 2.7%, benefiting ... | comparison identity and matched condition | p. 8 (4.3. Ablation Studies) |
| As shown in Table 4, despite these constraints, our IAL achieves a 4.1% improvement in PQ over the state-of-the-art multi-modal baseline LCPS, demonstrating the ... | comparison identity and matched condition | p. 8 (4.2. Benchmark Results) |
| Qualitative comparison of our method with the preliminary multi-modal panoptic segmentation baseline, LCPS. | comparison identity and matched condition | p. 9 (4.4. Augmentation Methods Comparison) |
| 4, our method notably reduces false positives (red points) and false negatives (green points) compared to LCPS. | comparison identity and matched condition | p. 9 (4.5. Qualitative Results and Discussion) |
| Comparison on the nuScenes test set. | comparison identity and matched condition | p. 7 (4.1. Experimental Setting) |
| Our method is evaluated without test-time augmentation or ensembling. | comparison identity and matched condition | p. 7 (4.1. Experimental Setting) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To validate the effectiveness of our proposed components, we conduct comprehensive ablation studies on the overall proposal framework in Table 5 and provide detailed ... | component/input/data sensitivity | p. 8 (4.3. Ablation Studies) |
| Our method is evaluated without test-time augmentation or ensembling. | component/input/data sensitivity | p. 7 (4.1. Experimental Setting) |
| Ablation study of the proposed modules in our framework. "PIE" denotes the PieAug module. | component/input/data sensitivity | p. 8 (4.3. Ablation Studies) |
| Table 8. Ablation study of the GTF module. "Sel" and "PE" denote the designs for token selection and positional embedding, respectively. We evaluate different ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Figure 1. The architecture overview of our Image-Assists-LiDAR (IAL) framework. We first voxelize the point cloud into cylindrical voxels. In PieAug, we synchronize augmentation ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Figure 2. Motivation and implementation variants of PieAug. Each column illustrates the motivation for LiDAR-image syn- chronized augmentation. Each row displays a different pie-cut ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions can be summarized as: 1) We present IAL, a novel transformer-based multi-modal framework for multimodal 3D panoptic segmentation, eliminating the cumbersome post-processing ... | As shown in Table 4, despite these constraints, our IAL achieves a 4.1% improvement in PQ over the state-of-the-art multi-modal baseline LCPS, demonstrating the ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.2. Benchmark Results), p. 8 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results), p. 9 (4.5. Qualitative Results and Discussion), p. 9 (4.5. Qualitative Results and Discussion), p. 7 (4.2. Benchmark Results) |
| Primary metric/result | Compared to the LiDAR-only baseline (using the same augmentation strategies as P3Former adopts), IAL achieves a 5.3% improvement, primarily due to a 7.5% increase ... | numeric claim only at cited anchor | p. 8 (4.2. Benchmark Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setting - extractive body cue:** It includes 40,157 frames of outdoor scenes, with 34,149 frames labeled for training and validation, and the remaining reserved for testing.
- **p. 6 / 4.1. Experimental Setting - extractive body cue:** It includes data from a 64-beam LiDAR sensor and two front-view cameras, including 8 "thing" classes and 11 "stuff" classes, comprising 19,130 frames for training, ...
- **p. 7 / 4.1. Experimental Setting - extractive body cue:** The training spans 80 epochs for nuScenes and 36 epochs for SemanticKITTI.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Red circles highlight instances where the LiDAR branch fails to segment correctly, but our multi-modal method succeeds. | p. 9 (4.4. Augmentation Methods Comparison) |
| body limitation/failure cue | Table 1. Preliminary study of positional embedding for objects of thing classes. We conduct the experiment on our LiDAR branch. "GT" denotes using the ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | As shown in Table 4, despite these constraints, our IAL achieves a 4.1% improvement in PQ over the state-of-the-art multi-modal baseline LCPS, demonstrating the ... | p. 8 (4.2. Benchmark Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The initial learning rate is set to 0.0008 and decays by half at epochs [60,75] for nuScenes and [30,32] for SemanticKITTI, respectively. | p. 7 (4.1. Experimental Setting) |
| The entire model is trained from scratch with a batch size of 2, using 4 NVIDIA A40 GPUs. | p. 7 (4.1. Experimental Setting) |
| Motivation and implementation variants of PieAug. | p. 4 (3.1. Modality-Synchronized Augmentation) |
| Next, we use F3D and F2D to create tokens and queries for a transformer decoder, enabling cross-modal interaction. | p. 4 (3. Methodology) |
| All geometric-, texture-, and no-prior queries are concatenated and fed into the transformer decoder for "thing" class prediction, i.e., 3D instance segmentation. | p. 6 (3.3. Prior-Based Query Generation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4.4. Augmentation Methods Comparison - extractive body cue:** Red circles highlight instances where the LiDAR branch fails to segment correctly, but our multi-modal method succeeds.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Preliminary study of positional embedding for objects of thing classes. We conduct the experiment on our LiDAR branch. "GT" denotes using the ground ...
- **p. 8 / 4.2. Benchmark Results - extractive body cue:** As shown in Table 4, despite these constraints, our IAL achieves a 4.1% improvement in PQ over the state-of-the-art multi-modal baseline LCPS, demonstrating the robustness ...

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Experimental Setting), p. 6 (4.1. Experimental Setting), p. 7 (4.2. Benchmark Results), p. 8 (4.3. Ablation Studies), p. 9 (4.5. Qualitative Results and Discussion), p. 7 (4.1. Experimental Setting), metrics p. 8 (4.2. Benchmark Results), p. 9 (4.5. Qualitative Results and Discussion), p. 5 (Figure/Table caption), p. 8 (4.2. Benchmark Results), p. 7 (4.1. Experimental Setting), p. 7 (4.1. Experimental Setting), baselines p. 8 (4.3. Ablation Studies), p. 8 (4.2. Benchmark Results), p. 9 (4.4. Augmentation Methods Comparison), p. 9 (4.5. Qualitative Results and Discussion), p. 7 (4.1. Experimental Setting), p. 7 (4.1. Experimental Setting), results p. 8 (4.2. Benchmark Results), p. 8 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results), p. 9 (4.5. Qualitative Results and Discussion), p. 9 (4.5. Qualitative Results and Discussion), p. 7 (4.2. Benchmark Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
