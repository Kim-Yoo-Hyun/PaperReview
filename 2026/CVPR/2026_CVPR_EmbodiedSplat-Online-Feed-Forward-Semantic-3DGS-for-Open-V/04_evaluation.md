# Evaluation - EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 8 (5.2. Ablation Studies), p. 7 (5.1. Experimental Results), p. 7 (5.2. Ablation Studies), p. 8 (5.2. Ablation Studies), p. 6 (5. Experiments)): Table 1. Quantitative comparisons on 3D Semantic Segmentation across ScanNet [6], ScanNet200 [38] and ScanNet++ [53]. We compare the performance of our EmbodiedSplat with existing semantic 3DGS methods on 3D ...

## Evaluation Body Digest

- **p. 7 / 5.1. Experimental Results - extractive body cue:** Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to the per-scene optimization ...
- **p. 6 / 5. Experiments - extractive body cue:** ScanNet++ [53] is a high-quality indoor dataset with 450 indoor scenes.
- **p. 6 / 5. Experiments - extractive body cue:** ScanNetv2 [6] is a large-scale RGB-D and point clouds dataset with 1,513 indoor scenes which also provides semantic annotations for 20 classes.
- **p. 7 / 5.1. Experimental Results - extractive body cue:** 1 shows the evaluation on 3D semantic segmentation across three real-world indoor datasets with varying number of classes.
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** The experiment is conducted on scene0000 01 of the ScanNet dataset, where our EmbodiedSplat produces M = 3.2M number of Gaussians while the global codebook ...
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** The experiment is conducted on scene0000 01 of ScanNet dataset and the total memory consumption is estimated by summing the sizes of the compressor components ...
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** For each time step, we prune top L -1 indices by the confidence scores as described in Algorithm.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparisons on 3D Semantic Segmentation across ScanNet [6], ScanNet200 [38] and ScanNet++ [53]. We compare the performance of our EmbodiedSplat with existing ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Experimental Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Quantitative comparisons on 3D Semantic Segmentation across ScanNet [6], ScanNet200 [38] and ScanNet++ [53]. We compare the performance of our EmbodiedSplat with ... | p. 6 (Figure/Table caption) |
| 5.2. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4, our codebook-based cosine similarity (2nd row) significantly improves efficiency, achieving nearly 14× faster processing speed compared to the naive per-Gaussian cosine similarity computation ... | p. 8 (5.2. Ablation Studies) |
| 5.1. Experimental Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Nevertheless, our model achieves performance comparable to clustering-based baselines [28, 48]. | p. 7 (5.1. Experimental Results) |
| 5.2. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3 demonstrates the effectiveness of combining 3D geometric-aware CLIP features ˆgT g , where it leads to performance improvement in 23780 | p. 7 (5.2. Ablation Studies) |
| 5.2. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | Aggregating the multiple instance features from multi-view images leads to performance improvement (L = 2 vs L = 4, 6, 11). | p. 8 (5.2. Ablation Studies) |

## Dataset / Benchmark Role

- **p. 7 / 5.1. Experimental Results - extractive body cue:** Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to the per-scene optimization ...
- **p. 6 / 5. Experiments - extractive body cue:** ScanNet++ [53] is a high-quality indoor dataset with 450 indoor scenes.
- **p. 6 / 5. Experiments - extractive body cue:** ScanNetv2 [6] is a large-scale RGB-D and point clouds dataset with 1,513 indoor scenes which also provides semantic annotations for 20 classes.
- **p. 7 / 5.1. Experimental Results - extractive body cue:** 1 shows the evaluation on 3D semantic segmentation across three real-world indoor datasets with varying number of classes.
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** The experiment is conducted on scene0000 01 of the ScanNet dataset, where our EmbodiedSplat produces M = 3.2M number of Gaussians while the global codebook ...
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** The experiment is conducted on scene0000 01 of ScanNet dataset and the total memory consumption is estimated by summing the sizes of the compressor components ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Build and understand at Once. By taking over 300 streaming images, our EmbodiedSplat reconstructs whole-scene open- vocabulary 3DGS in online manner at up ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overall framework of our EmbodiedSplat. We endow feed-forward 3DGS with semantic understanding capabilities by binding the two types of CLIP features: 1) 2D ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparisons on 3D Semantic Segmentation across ScanNet [6], ScanNet200 [38] and ScanNet++ [53]. We compare the performance of our EmbodiedSplat with existing ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Quantitative comparisons on 3D semantic segmentation. sign the labels to ground-truth point clouds by aggregating the contribution of individual Gaussians to each 3D ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparisons on cross-domain 3D se- mantic segmentation across ScanNet [6], ScanNet++ [53] and Replica [41]. domain segmentation setting, where the model is ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablations on 3D CLIP features ˆgT g Cosine similarity Time (ms) Complexity Note Per-Gaussian 14.35
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablations on codebook-based cosine similarity Methods Type / Feature dimension Size (MB) pretraining information loss LangSplat [35] Auto-encoder / 3
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Comparisons on memory size for semantic features. mIoU across all indoor benchmarks (3rd row). The 2D CLIP feature sT g preserves rich semantic ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to the per-scene ... | embodiment, simulator version and control stack | p. 7 (5.1. Experimental Results), p. 6 (5. Experiments) |
| Task/environment | ScanNet++ [53] is a high-quality indoor dataset with 450 indoor scenes. | reset, timeout, object/scene variation | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 3 (3. Preliminaries) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3. Preliminaries), p. 4 (4.1. EmbodiedSplat) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For each time step, we prune top L -1 indices by the confidence scores as described in Algorithm. | definition/direction/unit from same section | p. 8 (5.2. Ablation Studies) |
| Table 1. Quantitative comparisons on 3D Semantic Segmentation across ScanNet [6], ScanNet200 [38] and ScanNet++ [53]. We compare the performance of our EmbodiedSplat with ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| 3 demonstrates the effectiveness of combining 3D geometric-aware CLIP features ˆgT g , where it leads to performance improvement in 23780 | definition/direction/unit from same section | p. 7 (5.2. Ablation Studies) |
| 2) Our EmbodiedSplat demonstrates the best performance across all benchmarks with the shortest reconstruction time due to the feed-forward design. | definition/direction/unit from same section | p. 7 (5.1. Experimental Results) |
| Following [18], we modify their inference strategy to support direct 3D referring operation without rendering 2D feature maps. | definition/direction/unit from same section | p. 6 (5. Experiments) |
| Aggregating the multiple instance features from multi-view images leads to performance improvement (L = 2 vs L = 4, 6, 11). | definition/direction/unit from same section | p. 8 (5.2. Ablation Studies) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our EmbodiedSplat demonstrates better segmentation quality compared to the baselines, while combining the ground-truth depths (EmbodiedSplat-D) further enhances the quality of the visualization. | comparison identity and matched condition | p. 7 (5.1. Experimental Results) |
| Figure 2. Overall framework of our EmbodiedSplat. We endow feed-forward 3DGS with semantic understanding capabilities by binding the two types of CLIP features: 1) ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| We formulate the baselines with semantic 3DGS methods in two categories. | comparison identity and matched condition | p. 6 (5. Experiments) |
| We name this baseline as 2D methods where LangSplat [35], LEGaussians [40] and Online-LangSplat [19] are chosen for this category. | comparison identity and matched condition | p. 6 (5. Experiments) |
| Nevertheless, our model achieves performance comparable to clustering-based baselines [28, 48]. | comparison identity and matched condition | p. 7 (5.1. Experimental Results) |
| 4, our codebook-based cosine similarity (2nd row) significantly improves efficiency, achieving nearly 14× faster processing speed compared to the naive per-Gaussian cosine similarity computation ... | comparison identity and matched condition | p. 8 (5.2. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 5. Online 3D reasoning for class "Bed". tures to each Gaussian, but incurs heavy memory overhead (2295 MB) due to the high dimensionality ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Ablations on codebook-based cosine similarity Methods Type / Feature dimension Size (MB) pretraining information loss LangSplat [35] Auto-encoder / 3 30 ✓ ✓ Dr. | component/input/data sensitivity | p. 8 (5.2. Ablation Studies) |
| Specifically, the model is trained for 50,000 iterations without memory adapter. | component/input/data sensitivity | p. 6 (5. Experiments) |
| Following [18], we modify their inference strategy to support direct 3D referring operation without rendering 2D feature maps. | component/input/data sensitivity | p. 6 (5. Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are as follows: • Novel framework for embodied 3D perception which enables online, whole-scene reconstruction for languageembedded 3DGS with up to 5-6 ... | Table 1. Quantitative comparisons on 3D Semantic Segmentation across ScanNet [6], ScanNet200 [38] and ScanNet++ [53]. We compare the performance of our EmbodiedSplat with ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 8 (5.2. Ablation Studies), p. 7 (5.1. Experimental Results), p. 7 (5.2. Ablation Studies), p. 8 (5.2. Ablation Studies), p. 6 (5. Experiments) |
| Primary metric/result | 4, our codebook-based cosine similarity (2nd row) significantly improves efficiency, achieving nearly 14× faster processing speed compared to the naive per-Gaussian cosine similarity computation ... | numeric claim only at cited anchor | p. 8 (5.2. Ablation Studies) |

- Numeric sentences retained from the body:
- **p. 6 / 5. Experiments - extractive body cue:** By following [43, 44], we use 100 scenes for training and sample 10 scenes for testing.
- **p. 6 / 5. Experiments - extractive body cue:** We use the official training split for the training and select 4 scenes for the evaluation.
- **p. 6 / 5. Experiments - extractive body cue:** Following [26], we evaluate on 8 scenes in Replica for open-set semantic segmentation.
- **p. 7 / 5.1. Experimental Results - extractive body cue:** 4) By combining the real-time 2D models, our EmbodiedSplat-fast shows nearly real-time reconstruction speed that is 5-6 FPS of per-frame processing time.
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** However, it still requires heavy per-scene optimization, failing to achieve real-time semantic reconstruction (< 2FPS).
- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** To enable near real-time inference speed, we further propose the faster variant of our EmbodiedSplat, which achieves 5-6 FPS of processing time.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to the per-scene ... | p. 7 (5.1. Experimental Results) |
| body limitation/failure cue | Splat [18] shares the same limitations. | p. 8 (5.2. Ablation Studies) |
| body limitation/failure cue | Our model shows strong semantics generalizability in ScanNet++ →ScanNet transfer with performance degradation remaining below 1 mIoU compared to ScanNet →ScanNet setting in Tab. | p. 7 (5.1. Experimental Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To avoid GPU OOM, all inputs are resized to 384 × 512 and batch size is set to 1. | p. 6 (5. Experiments) |
| All experiments are conducted on single NVIDIA RTX 6000 Ada GPU. | p. 6 (5. Experiments) |
| Ablations on codebook-based cosine similarity. | p. 8 (5.2. Ablation Studies) |
| L = 2 denotes that each Gaussian only select one instance CLIP feature with the highest weight from the codebook. | p. 8 (5.2. Ablation Studies) |
| It accumulates related codebook indices and weights over the time steps for each Gaussian (Lines 1-4) while the weights are updated based on the ... | p. 4 (4.1. EmbodiedSplat) |
| To this end, we propose a novel Online Sparse Coefficient Field with CLIP Global Codebook which stores per-Gaussian semantics in a memory-efficient manner. | p. 2 (1) They require per-scene optimization that cannot be gen) |
| In contrast to existing memory-compression methods such as Auto-encoder [35], Product Quantization (PQ) Index [18] and per-scene optimized codebook [28, 48], our approach requires ... | p. 2 (1) They require per-scene optimization that cannot be gen) |
| Further implementation details of Algorithm. | p. 4 (4.1. EmbodiedSplat) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5.1. Experimental Results - extractive body cue:** Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the best results compared to the per-scene optimization ...
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** Splat [18] shares the same limitations.
- **p. 7 / 5.1. Experimental Results - extractive body cue:** Our model shows strong semantics generalizability in ScanNet++ →ScanNet transfer with performance degradation remaining below 1 mIoU compared to ScanNet →ScanNet setting in Tab.

- **Evidence anchors reviewed:** datasets p. 7 (5.1. Experimental Results), p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5.1. Experimental Results), p. 8 (5.2. Ablation Studies), p. 8 (5.2. Ablation Studies), metrics p. 8 (5.2. Ablation Studies), p. 6 (Figure/Table caption), p. 7 (5.2. Ablation Studies), p. 7 (5.1. Experimental Results), p. 6 (5. Experiments), p. 8 (5.2. Ablation Studies), baselines p. 7 (5.1. Experimental Results), p. 3 (Figure/Table caption), p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5.1. Experimental Results), p. 8 (5.2. Ablation Studies), results p. 6 (Figure/Table caption), p. 8 (5.2. Ablation Studies), p. 7 (5.1. Experimental Results), p. 7 (5.2. Ablation Studies), p. 8 (5.2. Ablation Studies), p. 6 (5. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
