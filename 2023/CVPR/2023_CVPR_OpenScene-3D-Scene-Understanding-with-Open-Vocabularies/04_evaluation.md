# Evaluation - OpenScene: 3D Scene Understanding with Open Vocabularies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2211.15654; PDF retrieval source: https://arxiv.org/pdf/2211.15654. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.1. Comparisons), p. 5 (4. Experiments), p. 6 (4.1. Comparisons), p. 6 (4.1. Comparisons), p. 3 (Figure/Table caption), p. 7 (Figure/Table caption)): Again, we outperform the zero-shot baseline (MSeg Voting) on both mIoU and mAcc metrics all three datasets.

## Evaluation Body Digest

- **p. 4 / 4. Experiments - extractive body cue:** To test our method in a variety of settings, we evaluate on three popular public benchmarks: ScanNet [11,46], Matterport3D [4], and nuScenes Lidarseg [3].
- **p. 4 / 4. Experiments - extractive body cue:** These three datasets span a broad gamut of situations - the first two provide RGBD images and 3D meshes of indoor scenes, and the last ...
- **p. 5 / 4.1. Comparisons - extractive body cue:** We compare our method with both zero-shot and fully-supervised baselines for semantic segmentation of one outdoor dataset (nuScenes) and two indoor datasets (ScanNet and Matterport).
- **p. 5 / 4.1. Comparisons - extractive body cue:** In Table 2 we compare our approach with both fullysupervised and zero-shot methods on all classes of the nuScenes [3] validation set, ScanNet [11] validation ...
- **p. 6 / 4.1. Comparisons - extractive body cue:** Images of 3D semantic segmentation results on public indoor and outdoor benchmarks.
- **p. 6 / 4.1. Comparisons - extractive body cue:** ScanNet [11] Matterport3D [4] nuScenes [3] Input Fully supervised [10] MSeg Voting [29] Ours GT Segmentation Figure 4.
- **p. 6 / 4.1. Comparisons - extractive body cue:** Comparison of semantic segmentation performance of different 3D features computed by our method. the mean accuracy for groups of 20 classes ranked by frequency.
- **p. 6 / 4.2. Ablation Studies & Analysis - extractive body cue:** In most experiments, we found the accuracy and generalizability of OpenSeg features to be better than LSeg (Table 1, Table 2, and Table 4), so ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 4); C. Full Results of Open-vocabulary Object Re (p. 13).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Comparisons | EMPIRICAL / SOURCE-REPORTED EVALUATION | Again, we outperform the zero-shot baseline (MSeg Voting) on both mIoU and mAcc metrics all three datasets. | p. 5 (4.1. Comparisons) |
| 4. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Still, both of our variants show significantly better performance in both mIoU and mAcc. detailed scenes, and thus provides the opportunity to stress open-vocabulary ... | p. 5 (4. Experiments) |
| 4.1. Comparisons | EMPIRICAL / SOURCE-REPORTED EVALUATION | Comparison of semantic segmentation performance of different 3D features computed by our method. the mean accuracy for groups of 20 classes ranked by frequency. | p. 6 (4.1. Comparisons) |
| 4.1. Comparisons | EMPIRICAL / SOURCE-REPORTED EVALUATION | Images of 3D semantic segmentation results on public indoor and outdoor benchmarks. | p. 6 (4.1. Comparisons) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 3. Method Overview. Given a 3D model (mesh or point cloud) and a set of posed images, we train a 3D network E3D ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / 4. Experiments - extractive body cue:** To test our method in a variety of settings, we evaluate on three popular public benchmarks: ScanNet [11,46], Matterport3D [4], and nuScenes Lidarseg [3].
- **p. 4 / 4. Experiments - extractive body cue:** These three datasets span a broad gamut of situations - the first two provide RGBD images and 3D meshes of indoor scenes, and the last ...
- **p. 5 / 4.1. Comparisons - extractive body cue:** We compare our method with both zero-shot and fully-supervised baselines for semantic segmentation of one outdoor dataset (nuScenes) and two indoor datasets (ScanNet and Matterport).
- **p. 5 / 4.1. Comparisons - extractive body cue:** In Table 2 we compare our approach with both fullysupervised and zero-shot methods on all classes of the nuScenes [3] validation set, ScanNet [11] validation ...
- **p. 6 / 4.1. Comparisons - extractive body cue:** Images of 3D semantic segmentation results on public indoor and outdoor benchmarks.
- **p. 6 / 4.1. Comparisons - extractive body cue:** ScanNet [11] Matterport3D [4] nuScenes [3] Input Fully supervised [10] MSeg Voting [29] Ours GT Segmentation Figure 4.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Open-vocabulary 3D Scene Understanding. We propose OpenScene, a zero-shot approach to 3D scene understanding that co-embeds dense 3D point features with image pixels ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Key idea. We co-embed 3D points with text and im- age pixels in the CLIP feature space (visualized with T-SNE [52]) which has ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Method Overview. Given a 3D model (mesh or point cloud) and a set of posed images, we train a 3D network E3D to ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Comparison on Zero-shot 3D Semantic Segmentation. We show quantitative comparison between our method and the most recent zero-shot 3D segmentation approach [39] and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Comparisons on Indoor and Outdoor Benchmarks. We compare our method with both zero-shot and fully-supervised baselines for semantic segmentation of one outdoor dataset ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative comparisons. Images of 3D semantic segmentation results on public indoor and outdoor benchmarks. K = 21 K = 40 K = 80 ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Impact of Increasing the Number of Object Classes. Here we show (a) mAcc on Matterport3D [4] with different num- bers of classes K, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4. Ablation Study. Comparison of semantic segmentation performance of different 3D features computed by our method. the mean accuracy for groups of 20 classes ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To test our method in a variety of settings, we evaluate on three popular public benchmarks: ScanNet [11,46], Matterport3D [4], and nuScenes Lidarseg [3]. | embodiment, simulator version and control stack | p. 4 (4. Experiments), p. 4 (4. Experiments) |
| Task/environment | These three datasets span a broad gamut of situations - the first two provide RGBD images and 3D meshes of indoor scenes, and the ... | reset, timeout, object/scene variation | p. 4 (4. Experiments), p. 5 (4.1. Comparisons) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (3.2. 3D Distillation), p. 3 (3. Method) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (3.2. 3D Distillation), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Comparison of semantic segmentation performance of different 3D features computed by our method. the mean accuracy for groups of 20 classes ranked by frequency. | definition/direction/unit from same section | p. 6 (4.1. Comparisons) |
| In most experiments, we found the accuracy and generalizability of OpenSeg features to be better than LSeg (Table 1, Table 2, and Table 4), ... | definition/direction/unit from same section | p. 6 (4.2. Ablation Studies & Analysis) |
| Figure 3. Method Overview. Given a 3D model (mesh or point cloud) and a set of posed images, we train a 3D network E3D ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| We start by evaluating on traditional closedset 3D semantic segmentation benchmarks (in order to be able to compare to previous work), and later demonstrate ... | definition/direction/unit from same section | p. 4 (4. Experiments) |
| For the baseline, we train a separate MinkowskiNet for each K. | definition/direction/unit from same section | p. 5 (4.1. Comparisons) |
| 4, we successfully segment the picture on the wall, while the GT misses it. | definition/direction/unit from same section | p. 5 (4.1. Comparisons) |
| Table 6. Open-vocabulary 3D Search Results. Each row depicts a search of the Matterport3D test set for a class given as a text query. ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Again, we outperform the zero-shot baseline (MSeg Voting) on both mIoU and mAcc metrics all three datasets. | comparison identity and matched condition | p. 5 (4.1. Comparisons) |
| We show quantitative comparison between our method and the most recent zero-shot 3D segmentation approach [39] and a multi-view fusion baseline utilizing MSeg [29]. | comparison identity and matched condition | p. 5 (4. Experiments) |
| Comparison of semantic segmentation performance of different 3D features computed by our method. the mean accuracy for groups of 20 classes ranked by frequency. | comparison identity and matched condition | p. 6 (4.1. Comparisons) |
| Figure 1. Open-vocabulary 3D Scene Understanding. We propose OpenScene, a zero-shot approach to 3D scene understanding that co-embeds dense 3D point features with image ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Figure 4. Qualitative comparisons. Images of 3D semantic segmentation results on public indoor and outdoor benchmarks. K = 21 K = 40 K = ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Still, both of our variants show significantly better performance in both mIoU and mAcc. detailed scenes, and thus provides the opportunity to stress open-vocabulary ... | component/input/data sensitivity | p. 5 (4. Experiments) |
| Figure 1. Open-vocabulary 3D Scene Understanding. We propose OpenScene, a zero-shot approach to 3D scene understanding that co-embeds dense 3D point features with image ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Table 4. Ablation Study. Comparison of semantic segmentation performance of different 3D features computed by our method. the mean accuracy for groups of 20 ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Overall, our contributions are summarized as follows: • We introduce open vocabulary 3D scene understanding tasks where arbitrary text queries are used for semantic ... | Again, we outperform the zero-shot baseline (MSeg Voting) on both mIoU and mAcc metrics all three datasets. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.1. Comparisons), p. 5 (4. Experiments), p. 6 (4.1. Comparisons), p. 6 (4.1. Comparisons), p. 3 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | Still, both of our variants show significantly better performance in both mIoU and mAcc. detailed scenes, and thus provides the opportunity to stress open-vocabulary ... | numeric claim only at cited anchor | p. 5 (4. Experiments) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | There are several limitations of our work and still much to do to realize the full potential of the proposed approach. | p. 8 (6. Limitations and Future Work) |
| body limitation/failure cue | In future work, it will be interesting to design experiments to quantify the success of open vocabulary queries for tasks where ground truth is ... | p. 8 (6. Limitations and Future Work) |
| body limitation/failure cue | Unlike [39], which requires training on 16 seen classes, our approach does not train with any 2D or 3D ground labels on any classes. | p. 5 (4. Experiments) |
| body limitation/failure cue | Our results on those classes is significantly better than [39] (7.7% vs 62.8% mIoU), even though 3DGenz [39] utilizes ground truth data for 16 ... | p. 5 (4.1. Comparisons) |
| body limitation/failure cue | In contrast, we are more robust to such rare objects since we do not rely upon any 3D labeled data. | p. 6 (4.1. Comparisons) |
| body limitation/failure cue | This suggests that leveraging patterns in both 2D and 3D domains makes the ensemble features more robust and descriptive. | p. 6 (4.2. Ablation Studies & Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Comparison of semantic segmentation performance of different 3D features computed by our method. the mean accuracy for groups of 20 classes ranked by frequency. | p. 6 (4.1. Comparisons) |
| We first compute the embeddings for all the text prompts using the CLIP [43] text encoder Etext, denoted as T = {t1, · · ... | p. 4 (3.3. 2D-3D Feature Ensemble) |
| We first compute per-pixel features for every image using a model pre-trained for open-vocabulary 2D semantic segmentation. | p. 3 (3. Method) |
| Given RGB images with a resolution of H × W, we can simply compute the per-pixel embeddings from the (frozen) segmentation model E2D, denoted ... | p. 3 (3.1. Image Feature Fusion) |
| For example, for the zero-shot 3D semantic segmentation using 2D-3D ensemble features, the final segmentation for each 3D point is computed point-wise by argmax ... | p. 4 (3.4. Inference) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Limitations and Future Work - extractive body cue:** There are several limitations of our work and still much to do to realize the full potential of the proposed approach.
- **p. 8 / 6. Limitations and Future Work - extractive body cue:** In future work, it will be interesting to design experiments to quantify the success of open vocabulary queries for tasks where ground truth is not ...
- **p. 5 / 4. Experiments - extractive body cue:** Unlike [39], which requires training on 16 seen classes, our approach does not train with any 2D or 3D ground labels on any classes.
- **p. 5 / 4.1. Comparisons - extractive body cue:** Our results on those classes is significantly better than [39] (7.7% vs 62.8% mIoU), even though 3DGenz [39] utilizes ground truth data for 16 seen ...
- **p. 6 / 4.1. Comparisons - extractive body cue:** In contrast, we are more robust to such rare objects since we do not rely upon any 3D labeled data.
- **p. 6 / 4.2. Ablation Studies & Analysis - extractive body cue:** This suggests that leveraging patterns in both 2D and 3D domains makes the ensemble features more robust and descriptive.

- **Evidence anchors reviewed:** datasets p. 4 (4. Experiments), p. 4 (4. Experiments), p. 5 (4.1. Comparisons), p. 5 (4.1. Comparisons), p. 6 (4.1. Comparisons), p. 6 (4.1. Comparisons), metrics p. 6 (4.1. Comparisons), p. 6 (4.2. Ablation Studies & Analysis), p. 3 (Figure/Table caption), p. 4 (4. Experiments), p. 5 (4.1. Comparisons), p. 5 (4.1. Comparisons), baselines p. 5 (4.1. Comparisons), p. 5 (4. Experiments), p. 6 (4.1. Comparisons), p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), results p. 5 (4.1. Comparisons), p. 5 (4. Experiments), p. 6 (4.1. Comparisons), p. 6 (4.1. Comparisons), p. 3 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
