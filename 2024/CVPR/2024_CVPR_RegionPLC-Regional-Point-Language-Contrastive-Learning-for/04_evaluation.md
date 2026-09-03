# Evaluation - RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Yang_RegionPLC_Regional_Point-Language_Contrastive_Learning_for_Open-World_3D_Scene_Understanding_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_RegionPLC_Regional_Point-Language_Contrastive_Learning_for_Open-World_3D_Scene_Understanding_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (3.3. Benchmark and Analysis on Regional 3D), p. 4 (3.3. Benchmark and Analysis on Regional 3D), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption)): As shown in the upper of Table 1, no single type of 3D-language source consistently outperforms others in all settings, and each association has its own merits.

## Evaluation Body Digest

- **p. 4 / 3.3. Benchmark and Analysis on Regional 3D - extractive body cue:** Hence, we benchmark them on ScanNet [6] semantic segmentation tasks with different novel categories and 2D image quantities (25K vs.
- **p. 4 / 3.3. Benchmark and Analysis on Regional 3D - extractive body cue:** Our benchmark encompasses two settings: i) the B12/N7 setting including 12 annotated base categories and 7 unannotated novel categories, which requires a strong comprehension of ...
- **p. 5 / 4.1. Basic Setups - extractive body cue:** To test the effectiveness of RegionPLC, we evaluate it on three popular datasets: 19827
- **p. 4 / 3.3. Benchmark and Analysis on Regional 3D - extractive body cue:** Nevertheless, the performance lift across different settings is not consistent or only shows incremental increases, which suggests the need for a more dedicated fusion strategy ...
- **p. 4 / 3.3. Benchmark and Analysis on Regional 3D - extractive body cue:** Hence, we examine their synergy effect for better performance.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 6. Component analysis on ScanNet. tv+e and tr denotes the combination of view and entity language supervision [7] and best region-level language supervision, respectively. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. Overview of our regional point-language contrastive learning framework. For regional 3D-language association, We develop a 3D-aware SFusion strategy effectively combining 3D vision-language pairs ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 7. SFusion results for zero-shot semantic segmentation con- sidering caption sources, overlap thresholds, and ratios. SFusion. We also study the effectiveness of our SFusion ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 3.3. Benchmark and Analysis on Regional 3D (p. 4); 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3.3. Benchmark and Analysis on Regional 3D | SYSTEM / EVALUATION SCOPE UNRESOLVED | As shown in the upper of Table 1, no single type of 3D-language source consistently outperforms others in all settings, and each association has ... | p. 4 (3.3. Benchmark and Analysis on Regional 3D) |
| 3.3. Benchmark and Analysis on Regional 3D | SYSTEM / EVALUATION SCOPE UNRESOLVED | Hence, we examine their synergy effect for better performance. | p. 4 (3.3. Benchmark and Analysis on Regional 3D) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 3. Results for open-world 3D instance segmentation on ScanNet in terms of hAP50 / mAPB 50 / mAPN 50. 3D Instance Segmentation. As ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2. Results for open-world 3D semantic segmentation on ScanNet, nuScenes and ScanNet200 in terms of hIoU / mIoUB / mIoUN . Best open-world ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 7. SFusion results for zero-shot semantic segmentation con- sidering caption sources, overlap thresholds, and ratios. SFusion. We also study the effectiveness of our ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / 3.3. Benchmark and Analysis on Regional 3D - extractive body cue:** Hence, we benchmark them on ScanNet [6] semantic segmentation tasks with different novel categories and 2D image quantities (25K vs.
- **p. 4 / 3.3. Benchmark and Analysis on Regional 3D - extractive body cue:** Our benchmark encompasses two settings: i) the B12/N7 setting including 12 annotated base categories and 7 unannotated novel categories, which requires a strong comprehension of ...
- **p. 5 / 4.1. Basic Setups - extractive body cue:** To test the effectiveness of RegionPLC, we evaluate it on three popular datasets: 19827

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. Overview of our regional point-language contrastive learning framework. For regional 3D-language association, We develop a 3D-aware SFusion strategy effectively combining 3D vision-language pairs ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Comparisons of different advanced manners for extract- ing regional language descriptions with 2D foundation models. prompts such as boxes and then caption these ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1. Results of regional caption fusion on base-annotated (hIoU / mIoUB / mIoUN ) and annotation-free (mIoU† (mAcc†), tested on foreground classes only) 3D ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Results for open-world 3D semantic segmentation on ScanNet, nuScenes and ScanNet200 in terms of hIoU / mIoUB / mIoUN . Best open-world results ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Results for open-world 3D instance segmentation on ScanNet in terms of hAP50 / mAPB 50 / mAPN 50. 3D Instance Segmentation. As our ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Annotation-free 3D semantic segmentation on ScanNet. ‡ and ♯mean results reproduced by us and Uni3D, independently. learning from sparse language supervision instead of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Annotation-free open-world semantic segmentation on ScanNet200 [26] in terms of mIoU† (mAcc†). Long-tail Scenario. As shown in Table 5, we set up com- ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 6. Component analysis on ScanNet. tv+e and tr denotes the combination of view and entity language supervision [7] and best region-level language supervision, respectively. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Hence, we benchmark them on ScanNet [6] semantic segmentation tasks with different novel categories and 2D image quantities (25K vs. | embodiment, simulator version and control stack | p. 4 (3.3. Benchmark and Analysis on Regional 3D), p. 4 (3.3. Benchmark and Analysis on Regional 3D) |
| Task/environment | Our benchmark encompasses two settings: i) the B12/N7 setting including 12 annotated base categories and 7 unannotated novel categories, which requires a strong comprehension ... | reset, timeout, object/scene variation | p. 4 (3.3. Benchmark and Analysis on Regional 3D), p. 5 (4.1. Basic Setups) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 6 (4.3. Annotation-free Open World), p. 4 (3.4. Boost Synergy of Diverse 3D-language Sources) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 6 (4.2. Base-annotated Open World), p. 5 (3.5. Region-aware Point-discriminative Contrastive) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Nevertheless, the performance lift across different settings is not consistent or only shows incremental increases, which suggests the need for a more dedicated fusion ... | definition/direction/unit from same section | p. 4 (3.3. Benchmark and Analysis on Regional 3D) |
| Hence, we examine their synergy effect for better performance. | definition/direction/unit from same section | p. 4 (3.3. Benchmark and Analysis on Regional 3D) |
| Table 6. Component analysis on ScanNet. tv+e and tr denotes the combination of view and entity language supervision [7] and best region-level language supervision, ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 1. Overview of our regional point-language contrastive learning framework. For regional 3D-language association, We develop a 3D-aware SFusion strategy effectively combining 3D vision-language ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Table 7. SFusion results for zero-shot semantic segmentation con- sidering caption sources, overlap thresholds, and ratios. SFusion. We also study the effectiveness of our ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 4. (a) Visualizations of RegionGR that integrates LLM for open-ended grounded 3D reasoning. (b) Demonstrating the versa- tility of RegionGR via more examples ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in the upper of Table 1, no single type of 3D-language source consistently outperforms others in all settings, and each association has ... | comparison identity and matched condition | p. 4 (3.3. Benchmark and Analysis on Regional 3D) |
| Table 4. Annotation-free 3D semantic segmentation on ScanNet. ‡ and ♯mean results reproduced by us and Uni3D, independently. learning from sparse language supervision instead ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 4. (a) Visualizations of RegionGR that integrates LLM for open-ended grounded 3D reasoning. (b) Demonstrating the versa- tility of RegionGR via more examples ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 2. Comparisons of different advanced manners for extract- ing regional language descriptions with 2D foundation models. prompts such as boxes and then caption ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 6. Component analysis on ScanNet. tv+e and tr denotes the combination of view and entity language supervision [7] and best region-level language supervision, ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we propose a holistic Regional Point Language Contrastive learning framework, named RegionPLC. | As shown in the upper of Table 1, no single type of 3D-language source consistently outperforms others in all settings, and each association has ... | PDF body cue; verify exact table/figure and matched conditions | p. 4 (3.3. Benchmark and Analysis on Regional 3D), p. 4 (3.3. Benchmark and Analysis on Regional 3D), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | Hence, we examine their synergy effect for better performance. | numeric claim only at cited anchor | p. 4 (3.3. Benchmark and Analysis on Regional 3D) |

- Numeric sentences retained from the body:
- **p. 7 / Method - extractive body cue:** Network mIoU† mAcc† Multi-view Infer GT Instance Mask Train Hours Extra Storage Latency MaskCLIP‡ [43] CLIP [25] 23.1 40.9 ✓ × - - 1.7 s ...
- **p. 7 / 5.5 G - extractive body cue:** 0.10 s RegionPLC + OpenScene-3D‡ SparseUNet16 [11] 60.1 74.4 × × 25.9 h
- **p. 7 / 122.8 G - extractive body cue:** 0.08 s RegionPLC + OpenScene-3D‡ SparseUNet32 [11] 63.6 80.3 × × 26.4 h

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Furthermore, our region-aware pointdiscriminative contrastive loss aids in learning distinctive and robust features from regional captions. | p. 8 (7. Conclusion) |
| body limitation/failure cue | Figure 1. Overview of our regional point-language contrastive learning framework. For regional 3D-language association, We develop a 3D-aware SFusion strategy effectively combining 3D vision-language ... | p. 3 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We run all experiments with a batch size of 32 on 8 NVIDIA V100 or A100 (see Suppl. for more details). | p. 6 (Method) |
| Notably, our method is training-efficient, requiring less disk storage and training time compared to OpenScene. | p. 7 (122.8 G) |
| Specifically, for each regional 3D-language pair, instead of aggregating point features into an averaged region-level feature, our Lpdc directly computes the similarity between point-wise ... | p. 5 (3.5. Region-aware Point-discriminative Contrastive) |
| We then pool the logarithm of predicted point-wise probability within ˆp to compute the cross-entropy loss regarding one-hot label yt as follows, z = ... | p. 5 (3.5. Region-aware Point-discriminative Contrastive) |
| We adopt the sparse-convolutionbased UNet [11] as the 3D encoder with CLIP [25] text encoder as the final classifier for 3D semantic segmentation, and ... | p. 6 (Method) |
| Annotation-free 3D semantic segmentation on ScanNet. ‡ and ♯mean results reproduced by us and Uni3D, independently. learning from sparse language supervision instead of pixelaligned ... | p. 7 (122.8 G) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 7. Conclusion - extractive body cue:** Furthermore, our region-aware pointdiscriminative contrastive loss aids in learning distinctive and robust features from regional captions.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. Overview of our regional point-language contrastive learning framework. For regional 3D-language association, We develop a 3D-aware SFusion strategy effectively combining 3D vision-language pairs ...

- **Evidence anchors reviewed:** datasets p. 4 (3.3. Benchmark and Analysis on Regional 3D), p. 4 (3.3. Benchmark and Analysis on Regional 3D), p. 5 (4.1. Basic Setups), metrics p. 4 (3.3. Benchmark and Analysis on Regional 3D), p. 4 (3.3. Benchmark and Analysis on Regional 3D), p. 7 (Figure/Table caption), p. 3 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 4 (3.3. Benchmark and Analysis on Regional 3D), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 3 (Figure/Table caption), results p. 4 (3.3. Benchmark and Analysis on Regional 3D), p. 4 (3.3. Benchmark and Analysis on Regional 3D), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
