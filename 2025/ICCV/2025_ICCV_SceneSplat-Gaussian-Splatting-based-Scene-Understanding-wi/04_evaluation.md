# Evaluation - SceneSplat: Gaussian Splatting-based Scene Understanding with Vision-Language Pretraining

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.2. Label-free 3DGS Pretraining), p. 7 (Figure/Table caption), p. 6 (5.1. Vision-Language Pretraining), p. 3 (Figure/Table caption), p. 7 (5.3. Further Statistical Evaluation), p. 8 (5.3. Further Statistical Evaluation)): Our method achieves a +0.1% improvement over supervised-only baselines on ScanNet20 and +0.5% on ScanNet200, while observing a performance drop on ScanNet++ primarily due to pretraining dataset quality variations 4966

## Evaluation Body Digest

- **p. 3 / 3. SceneSplat Dataset - extractive PDF cue:** The dataset contains about seven thousand scenes, including both real-world and synthetic environments.
- **p. 8 / 5.3. Further Statistical Evaluation - extractive PDF cue:** We evaluate SceneSplat using different number of nearest 3DGS neighbors for zero-shot task on ScanNet++ validation split.
- **p. 3 / 3. SceneSplat Dataset - extractive PDF cue:** We introduce SceneSplat-7K - a carefully curated dataset of 3D Gaussian Splats representing indoor scenes.
- **p. 4 / 3.2. Data Statistic - extractive PDF cue:** SceneSplat-7K dataset includes various 3D Gaussian Splatting datasets generated from ScanNet [5], ScanNet++ [57], ScanNet++ v2, Replica [46], Hypersim [43], 3RScan [49], ARKitScenes [1], and ...
- **p. 6 / 5.1. Vision-Language Pretraining - extractive PDF cue:** When trained on ScanNet, SceneSplat achieves state-of-the-art results, leading to 5.9% and 2.2% f-mIoU increases on the ScanNet200 and Matterport3D benchmarks.
- **p. 6 / 5.1. Vision-Language Pretraining - extractive PDF cue:** Given text queries and SceneSplat inference results for a 3DGS scene, we can effectively localize the corresponding splats in 3D (highlighted in red for queries ...
- **p. 7 / 5.3. Further Statistical Evaluation - extractive PDF cue:** SceneSplat here is trained on the single dataset respectively.
- **p. 7 / 5.3. Further Statistical Evaluation - extractive PDF cue:** Reported on the Matterport3D test split labeled in 21 semantic classes, the box plot shows a clear positive trend between the input 3DGS scene training ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3. SceneSplat Dataset (p. 3); 5. Experiments (p. 6); 5.3. Further Statistical Evaluation (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Label-free 3DGS Pretraining | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves a +0.1% improvement over supervised-only baselines on ScanNet20 and +0.5% on ScanNet200, while observing a performance drop on ScanNet++ primarily due ... | p. 6 (5.2. Label-free 3DGS Pretraining) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. Zero-Shot 3D Semantic Segmentation on the Fine-Grained ScanNet++ (100 classes) [57], Matterport3D (160 classes) [2] and ScanNet200 (200 classes) [5] Benchmarks. We ... | p. 7 (Figure/Table caption) |
| 5.1. Vision-Language Pretraining | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, [21] uses 8.32× training scenes to achieve its best results, Zero-Shot Prediction Ground Truth Figure 3. | p. 6 (5.1. Vision-Language Pretraining) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Dataset Statistics. The proposed SceneSplat-7K dataset includes various 3D Gaussian Splatting datasets generated from ScanNet [5], ScanNet++ [57], ScanNet++ v2, Replica[46], Hypersim[43], ... | p. 3 (Figure/Table caption) |
| 5.3. Further Statistical Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | This encourages the careful curation of the collected 3DGS scene dataset. outperforms the labels with a 4.2% increase in f-mIoU. | p. 7 (5.3. Further Statistical Evaluation) |

## Dataset / Benchmark Role

- **p. 3 / 3. SceneSplat Dataset - extractive PDF cue:** The dataset contains about seven thousand scenes, including both real-world and synthetic environments.
- **p. 8 / 5.3. Further Statistical Evaluation - extractive PDF cue:** We evaluate SceneSplat using different number of nearest 3DGS neighbors for zero-shot task on ScanNet++ validation split.
- **p. 3 / 3. SceneSplat Dataset - extractive PDF cue:** We introduce SceneSplat-7K - a carefully curated dataset of 3D Gaussian Splats representing indoor scenes.
- **p. 4 / 3.2. Data Statistic - extractive PDF cue:** SceneSplat-7K dataset includes various 3D Gaussian Splatting datasets generated from ScanNet [5], ScanNet++ [57], ScanNet++ v2, Replica [46], Hypersim [43], 3RScan [49], ARKitScenes [1], and ...
- **p. 6 / 5.1. Vision-Language Pretraining - extractive PDF cue:** When trained on ScanNet, SceneSplat achieves state-of-the-art results, leading to 5.9% and 2.2% f-mIoU increases on the ScanNet200 and Matterport3D benchmarks.
- **p. 6 / 5.1. Vision-Language Pretraining - extractive PDF cue:** Given text queries and SceneSplat inference results for a 3DGS scene, we can effectively localize the corresponding splats in 3D (highlighted in red for queries ...
- **p. 7 / 5.3. Further Statistical Evaluation - extractive PDF cue:** SceneSplat here is trained on the single dataset respectively.
- **p. 7 / 5.3. Further Statistical Evaluation - extractive PDF cue:** Reported on the Matterport3D test split labeled in 21 semantic classes, the box plot shows a clear positive trend between the input 3DGS scene training ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We present the 3DGS indoor dataset SceneSplat-7K which includes 7K scenes generated from ARKitScenes [1], Replica [46], ScanNet [5], ScanNet++ [57], Hypersim[43], 3RScan ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 1. Dataset Statistics. The proposed SceneSplat-7K dataset includes various 3D Gaussian Splatting datasets generated from ScanNet [5], ScanNet++ [57], ScanNet++ v2, Replica[46], Hypersim[43], 3RScan[49], ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2. SceneSplat Overview. The SceneSplat-7K dataset enables Vision-Language Pretraining and Self-Supervised Pretrain- ing. For vision-language pretraining, we associate each 3D Gaussian primitive with semantic ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative Results of Zero-Shot 3D Semantic Seg- mentation on ScanNet++. SceneSplat demonstrates competitive zero-shot performance, note how our model correctly annotate the regions ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Text-Based 3DGS Scene Query. Given text queries and SceneSplat inference results for a 3DGS scene, we can effec- tively localize the corresponding splats ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Tab. 3. Our method achieves a +0.1% improvement over supervised-only baselines on ScanNet20 and +0.5% on ScanNet200, while observing a performance drop on Scan- Net++ ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Zero-Shot 3D Semantic Segmentation on the Fine-Grained ScanNet++ (100 classes) [57], Matterport3D (160 classes) [2] and ScanNet200 (200 classes) [5] Benchmarks. We report ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. GaussianSSL Ablation Experiments. We adopt the pre- training on the SceneSplat-7K dataset and report fine-tuning mIoU and mAcc on indoor semantic segmentation tasks. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset contains about seven thousand scenes, including both real-world and synthetic environments. | embodiment, simulator version and control stack | p. 3 (3. SceneSplat Dataset), p. 8 (5.3. Further Statistical Evaluation) |
| Task/environment | We evaluate SceneSplat using different number of nearest 3DGS neighbors for zero-shot task on ScanNet++ validation split. | reset, timeout, object/scene variation | p. 8 (5.3. Further Statistical Evaluation), p. 3 (3. SceneSplat Dataset) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (4.3. Self Supervised Pretraining), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (4.2. Vision-Language 3DGS Pretraining), p. 5 (4.2. Vision-Language 3DGS Pretraining) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2. Zero-Shot 3D Semantic Segmentation on the Fine-Grained ScanNet++ (100 classes) [57], Matterport3D (160 classes) [2] and ScanNet200 (200 classes) [5] Benchmarks. We ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Overall mIoU increases with different class-wise relative IoU changes. | definition/direction/unit from same section | p. 8 (5.3. Further Statistical Evaluation) |
| Overall and Class-Wise IoU Changes w.r.t. to the Nearest Neighbor Number During Majority Voting. | definition/direction/unit from same section | p. 8 (5.3. Further Statistical Evaluation) |
| SceneSplat demonstrates competitive zero-shot performance, note how our model correctly annotate the regions lacking ground truth labels, e.g., desks on the top row. | definition/direction/unit from same section | p. 6 (5.1. Vision-Language Pretraining) |
| We demonstrate text-based queries on the inference results of the predicted language features in Fig. | definition/direction/unit from same section | p. 6 (5.1. Vision-Language Pretraining) |
| 5 compares the performance of SceneSplat inference features with the collected language labels. | definition/direction/unit from same section | p. 7 (5.3. Further Statistical Evaluation) |
| Figure 1. We present the 3DGS indoor dataset SceneSplat-7K which includes 7K scenes generated from ARKitScenes [1], Replica [46], ScanNet [5], ScanNet++ [57], Hypersim[43], ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| We introduce SceneSplat-7K - a carefully curated dataset of 3D Gaussian Splats representing indoor scenes. | definition/direction/unit from same section | p. 3 (3. SceneSplat Dataset) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 4. Supervised Semantic Segmentation Experiments. We report our best results from Tab. 3 comparing against the state-of- the-art Point Transformer method. (Tab. 1). ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 2. Zero-Shot 3D Semantic Segmentation on the Fine-Grained ScanNet++ (100 classes) [57], Matterport3D (160 classes) [2] and ScanNet200 (200 classes) [5] Benchmarks. We ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Our method achieves a +0.1% improvement over supervised-only baselines on ScanNet20 and +0.5% on ScanNet200, while observing a performance drop on ScanNet++ primarily due ... | comparison identity and matched condition | p. 6 (5.2. Label-free 3DGS Pretraining) |
| Effectiveness of Using 3DGS in Vision-Language Pretraining Compared to Point Clouds. | comparison identity and matched condition | p. 8 (5.3. Further Statistical Evaluation) |
| SceneSplat trained on 3DGS parameters consistently outperforms the variant trained on point cloud properties. | comparison identity and matched condition | p. 8 (5.3. Further Statistical Evaluation) |
| Figure 2. SceneSplat Overview. The SceneSplat-7K dataset enables Vision-Language Pretraining and Self-Supervised Pretrain- ing. For vision-language pretraining, we associate each 3D Gaussian primitive with ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation on Contrastive Loss in the Vision-Language Pretraining. | component/input/data sensitivity | p. 8 (5.3. Further Statistical Evaluation) |
| Ablation on Contrastive Loss During VisionLanguage Pretraining Using Subsets. | component/input/data sensitivity | p. 8 (5.3. Further Statistical Evaluation) |
| We further justify our design choices through ablation studies. | component/input/data sensitivity | p. 6 (5. Experiments) |
| Our visionlanguage pretraining enables the effective localization of complex objects within the scene. | component/input/data sensitivity | p. 6 (5.1. Vision-Language Pretraining) |
| Figure 2. SceneSplat Overview. The SceneSplat-7K dataset enables Vision-Language Pretraining and Self-Supervised Pretrain- ing. For vision-language pretraining, we associate each 3D Gaussian primitive with ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Table 3. GaussianSSL Ablation Experiments. We adopt the pre- training on the SceneSplat-7K dataset and report fine-tuning mIoU and mAcc on indoor semantic segmentation ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions can be summarized as follows: • We present SceneSplat-7K, a high-quality large-scale Gaussian splats dataset spanning 7K indoor scenes, which boosts 3DGS ... | Our method achieves a +0.1% improvement over supervised-only baselines on ScanNet20 and +0.5% on ScanNet200, while observing a performance drop on ScanNet++ primarily due ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.2. Label-free 3DGS Pretraining), p. 7 (Figure/Table caption), p. 6 (5.1. Vision-Language Pretraining), p. 3 (Figure/Table caption), p. 7 (5.3. Further Statistical Evaluation), p. 8 (5.3. Further Statistical Evaluation) |
| Primary metric/result | Table 2. Zero-Shot 3D Semantic Segmentation on the Fine-Grained ScanNet++ (100 classes) [57], Matterport3D (160 classes) [2] and ScanNet200 (200 classes) [5] Benchmarks. We ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 3 / 3.1. Data Processing - extractive PDF cue:** Starting with the training views, we select scenes with at least 400 frames to ensure sufficient multi-view coverage.
- **p. 8 / 5.3. Further Statistical Evaluation - extractive PDF cue:** Reported on the Matterport3D test split with 370 scenes, Fig.
- **p. 6 / 4.3. Self Supervised Pretraining - extractive PDF cue:** For a batch of Gaussian scenes {Gn}B n=1 (global/local views Gb g, Gb l), we extract tokenized bottleneck features z ∈RM×de, compute global representations ¯z ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Low PSNRs usually come out of blurry input images, poor Gaussian centers optimization, and insufficient scene coverage, where the 3DGS parameters cannot resolve the ... | p. 8 (5.3. Further Statistical Evaluation) |
| body limitation/failure cue | Although the collected labels are not perfect, large-scale pretraining can filter noise and learn meaningful patterns. | p. 7 (5.3. Further Statistical Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 6 presents scaling results Method Steps Required Runtime / Scene Occam's LGS 2D fusion + lifting 107 min SceneSplat single inference 0.24 min Table ... | p. 8 (5.3. Further Statistical Evaluation) |
| We first adapt the transformer encoder-decoder backbone from [51] to efficiently predict high-dimensional perprimitive features corresponding to collected 3DGS language labels. | p. 4 (4.2. Vision-Language 3DGS Pretraining) |
| Hence, we compute a cross-entropy loss in both directions: \mathca l | p. 5 (4.2. Vision-Language 3DGS Pretraining) |
| (4) The masked tokens T_{\text {m}} are processed using the 3D backbone gθ(·) to obtain ˆ Tm = hϕ(fφ(Tm)), where fφ(·) is the encoder ... | p. 5 (4.3. Self Supervised Pretraining) |
| The implementation details are provided in the supplement. | p. 6 (5. Experiments) |
| 4.2, the precomputed language feature enables effective knowledge distillation. | p. 6 (4.3. Self Supervised Pretraining) |
| Contrastive Loss ScanNet200 (200) ScanNet++ (100) f-mIoU f-mAcc f-mIoU f-mAcc w/o 13.7 22.5 19.6 34.4 always apply 13.2 23.4 23.2 39.3 last 75% epochs ... | p. 8 (5.3. Further Statistical Evaluation) |
| Constructing this dataset required an equivalent of 150 days of computation on an NVIDIA L4 GPU. | p. 4 (3.2. Data Statistic) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5.3. Further Statistical Evaluation - extractive PDF cue:** Low PSNRs usually come out of blurry input images, poor Gaussian centers optimization, and insufficient scene coverage, where the 3DGS parameters cannot resolve the scene ...
- **p. 7 / 5.3. Further Statistical Evaluation - extractive PDF cue:** Although the collected labels are not perfect, large-scale pretraining can filter noise and learn meaningful patterns.

- **PDF anchors reviewed:** datasets p. 3 (3. SceneSplat Dataset), p. 8 (5.3. Further Statistical Evaluation), p. 3 (3. SceneSplat Dataset), p. 4 (3.2. Data Statistic), p. 6 (5.1. Vision-Language Pretraining), p. 6 (5.1. Vision-Language Pretraining), metrics p. 7 (Figure/Table caption), p. 8 (5.3. Further Statistical Evaluation), p. 8 (5.3. Further Statistical Evaluation), p. 6 (5.1. Vision-Language Pretraining), p. 6 (5.1. Vision-Language Pretraining), p. 7 (5.3. Further Statistical Evaluation), baselines p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (5.2. Label-free 3DGS Pretraining), p. 8 (5.3. Further Statistical Evaluation), p. 8 (5.3. Further Statistical Evaluation), p. 5 (Figure/Table caption), results p. 6 (5.2. Label-free 3DGS Pretraining), p. 7 (Figure/Table caption), p. 6 (5.1. Vision-Language Pretraining), p. 3 (Figure/Table caption), p. 7 (5.3. Further Statistical Evaluation), p. 8 (5.3. Further Statistical Evaluation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
