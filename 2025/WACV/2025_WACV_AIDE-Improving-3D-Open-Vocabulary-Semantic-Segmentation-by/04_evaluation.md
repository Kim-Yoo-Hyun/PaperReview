# Evaluation - AIDE: Improving 3D Open-Vocabulary Semantic Segmentation by Aligned Vision-Language Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.4. Qualitative Results-Generalization), p. 7 (Figure/Table caption), p. 7 (4.3. Ablation Studies), p. 6 (4.2. Quantative Results), p. 6 (4.2. Quantative Results), p. 8 (4.4. Qualitative Results-Generalization)): Qualitative results of segmentation compared between baseline and AIDE. achieves significant improvements in all metrics, with hIoU, mIoUB, and mIoUN increasing from 32.1, 31.6, and 32.6 to 35.9, 39.9, and ...

## Evaluation Body Digest

- **p. 5 / 4. Experiments - extractive PDF cue:** To validate the effectiveness of AIDE, we conducted extensive experiments on three popular 3D benchmarks: ScanNet [20], S3DIS [2], and one outdoor dataset (nuScenes [7]).
- **p. 6 / 4.2. Quantative Results - extractive PDF cue:** Improvements can also be observed on the outdoor dataset, nuScenes, as AIDE improves the hIoU from 47.7 and 24.3 to 62.2 and 48.4 on two ...
- **p. 5 / 4. Experiments - extractive PDF cue:** Benchmarks, Baselines, and Implementation Benchmarks and category partitions.
- **p. 6 / 4. Experiments - extractive PDF cue:** Results on S3DIS and nuScenes. ‡ refers to numbers copied from Ding et al.
- **p. 8 / 4.4. Qualitative Results-Generalization - extractive PDF cue:** Train Dataset Metrics (Baseline/AIDE) hIoU mIoUB mIoUN Test Dataset: S3DIS (B8/N4) ScanNet (B15/N4) 32.1/35.9 31.6/39.9 32.6/33.8 ScanNet (B12/N7) 22.2/25.8 25.0/23.3 19.9/28.9 ScanNet (B10/N9) 24.7/31.0 30.5/38.9 ...
- **p. 8 / 4.4. Qualitative Results-Generalization - extractive PDF cue:** To better understand how our AIDE excels at segmenting seen and unseen objects, we visualize segmentation results in Figs.
- **p. 8 / 4.4. Qualitative Results-Generalization - extractive PDF cue:** These results underscore the importance of the CLIP-rewarded alignment and adaptive segmentation modules in enhancing open-vocabulary segmentation models' transferability to novel categories and scenarios.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Table 1. Performance of Semantic Segmentation on ScanNet (B15/N4 Split) [20] using PLA [23]. Metrics include harmonic IoU (hIoU), mIoU on base categories (mIoUB), and ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.2. Quantative Results (p. 6); 4.4. Qualitative Results-Generalization (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Qualitative Results-Generalization | EMPIRICAL / SOURCE-REPORTED EVALUATION | Qualitative results of segmentation compared between baseline and AIDE. achieves significant improvements in all metrics, with hIoU, mIoUB, and mIoUN increasing from 32.1, 31.6, ... | p. 8 (4.4. Qualitative Results-Generalization) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 5. Ablation studies on different numbers of learnable tokens of AIDE on ScanNet (B15/N4). conduct a series of experiments as shown in Tab. ... | p. 7 (Figure/Table caption) |
| 4.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | Also, we observe consistent improvement when increasing the number of samples from 1 to 30, underscoring the value of leveraging more descriptive and diverse ... | p. 7 (4.3. Ablation Studies) |
| 4.2. Quantative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared to our baseline, PLA, AIDE improves hIoU by 7.6 and 4.0 for each split. | p. 6 (4.2. Quantative Results) |
| 4.2. Quantative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | This represents a significant improvement over PLA (Baseline), with increases of 7.5, 14.5, and 11.9 in hIoU. | p. 6 (4.2. Quantative Results) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments - extractive PDF cue:** To validate the effectiveness of AIDE, we conducted extensive experiments on three popular 3D benchmarks: ScanNet [20], S3DIS [2], and one outdoor dataset (nuScenes [7]).
- **p. 6 / 4.2. Quantative Results - extractive PDF cue:** Improvements can also be observed on the outdoor dataset, nuScenes, as AIDE improves the hIoU from 47.7 and 24.3 to 62.2 and 48.4 on two ...
- **p. 5 / 4. Experiments - extractive PDF cue:** Benchmarks, Baselines, and Implementation Benchmarks and category partitions.
- **p. 6 / 4. Experiments - extractive PDF cue:** Results on S3DIS and nuScenes. ‡ refers to numbers copied from Ding et al.
- **p. 8 / 4.4. Qualitative Results-Generalization - extractive PDF cue:** Train Dataset Metrics (Baseline/AIDE) hIoU mIoUB mIoUN Test Dataset: S3DIS (B8/N4) ScanNet (B15/N4) 32.1/35.9 31.6/39.9 32.6/33.8 ScanNet (B12/N7) 22.2/25.8 25.0/23.3 19.9/28.9 ScanNet (B10/N9) 24.7/31.0 30.5/38.9 ...
- **p. 8 / 4.4. Qualitative Results-Generalization - extractive PDF cue:** To better understand how our AIDE excels at segmenting seen and unseen objects, we visualize segmentation results in Figs.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Previous methods use misaligned paired data (e.g., image/point cloud 1 is closest to text 2) and freeze the text encoder trained on 2D ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Table 1. Performance of Semantic Segmentation on ScanNet (B15/N4 Split) [20] using PLA [23]. Metrics include harmonic IoU (hIoU), mIoU on base categories (mIoUB), and ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The illustration of our AIDE with two proposed modules, i.e., CLIP-rewarded alignment module (Sec. 3.3) for enhancing the quality of 3D-text data pairs ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Results on ScanNet. † and ‡ refer to numbers copied from He et al. [32] and Ding et al. [23]. Best in Bold. ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Results on S3DIS and nuScenes. ‡ refers to numbers copied from Ding et al. [23]. Best in Bold. image encoders (ftext and fimg) ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation studies on different modules of AIDE. "Adap- tive Segmentation" refers to the adaptive segmentation mod- ule. "Caption Selection" and "Caption Sampling" refer ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5. Ablation studies on different numbers of learnable tokens of AIDE on ScanNet (B15/N4). conduct a series of experiments as shown in Tab. 5. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 6. Ablation studies on different numbers of captions of AIDE for each temperature. Text Encoder ScanNet (B15/N4) hIoU mIoUB mIoUN

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To validate the effectiveness of AIDE, we conducted extensive experiments on three popular 3D benchmarks: ScanNet [20], S3DIS [2], and one outdoor dataset (nuScenes ... | embodiment, simulator version and control stack | p. 5 (4. Experiments), p. 6 (4.2. Quantative Results) |
| Task/environment | Improvements can also be observed on the outdoor dataset, nuScenes, as AIDE improves the hIoU from 47.7 and 24.3 to 62.2 and 48.4 on ... | reset, timeout, object/scene variation | p. 6 (4.2. Quantative Results), p. 5 (4. Experiments) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 5 (3.4. Adaptive Segmentation-Text Modeling), p. 4 (3.1. Problem Definition) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (3.1. Problem Definition), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| These results underscore the importance of the CLIP-rewarded alignment and adaptive segmentation modules in enhancing open-vocabulary segmentation models' transferability to novel categories and scenarios. | definition/direction/unit from same section | p. 8 (4.4. Qualitative Results-Generalization) |
| Table 1. Performance of Semantic Segmentation on ScanNet (B15/N4 Split) [20] using PLA [23]. Metrics include harmonic IoU (hIoU), mIoU on base categories (mIoUB), ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 3. Qualitative results of segmentation compared between baseline and AIDE. achieves significant improvements in all metrics, with hIoU, mIoUB, and mIoUN increasing from ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 2. The illustration of our AIDE with two proposed modules, i.e., CLIP-rewarded alignment module (Sec. 3.3) for enhancing the quality of 3D-text data ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 1. Previous methods use misaligned paired data (e.g., image/point cloud 1 is closest to text 2) and freeze the text encoder trained on ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Following previous methods [23, 77, 79], we employ the commonly used 3D segmentation metric mean Intersection over Union for both base and novel categories ... | definition/direction/unit from same section | p. 5 (4. Experiments) |
| It underscores the importance of well-designed captioning techniques in improving alignment with the text encoder. | definition/direction/unit from same section | p. 6 (4.3. Ablation Studies) |
| Notably, the introduction of adaptive segmentation module alone improves hIoU from 65.3 to 66.3, and mIoUB from 68.3 to 70.2, illustrating the efficacy in ... | definition/direction/unit from same section | p. 6 (4.3. Ablation Studies) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to our baseline, PLA, AIDE improves hIoU by 7.6 and 4.0 for each split. | comparison identity and matched condition | p. 6 (4.2. Quantative Results) |
| In every setting, AIDE consistently outperforms the baseline on hIoU, underscoring its superior generalization capability. | comparison identity and matched condition | p. 8 (4.4. Qualitative Results-Generalization) |
| It is obvious that, on both the seen and unseen classes (chair and toilet), AIDE better segments them from other objects compared with the ... | comparison identity and matched condition | p. 8 (4.4. Qualitative Results-Generalization) |
| Ablation studies on different modules of AIDE. "Adaptive Segmentation" refers to the adaptive segmentation module. "Caption Selection" and "Caption Sampling" refer to using temperature-based ... | comparison identity and matched condition | p. 7 (4.3. Ablation Studies) |
| Benchmarks, Baselines, and Implementation Benchmarks and category partitions. | comparison identity and matched condition | p. 5 (4. Experiments) |
| Following PLA [23], which is also our baseline, we employ the sparse-convolution-based UNet [29] with a base hidden dimension of 16 as our 3D ... | comparison identity and matched condition | p. 5 (4. Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In this part, we present the ablation studies on the effects of two proposed modules (Tab. | component/input/data sensitivity | p. 6 (4.3. Ablation Studies) |
| Table 7. Ablation studies on using different text encoders of AIDE on ScanNet (B15/N4). this phenomenon. As generating over 30 captions per tem- perature ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Due to the space limitation, ablation studies on the choice of temperatures (Tab. | component/input/data sensitivity | p. 6 (4.3. Ablation Studies) |
| Ablation studies on different numbers of learnable tokens of AIDE on ScanNet (B15/N4). conduct a series of experiments as shown in Tab. | component/input/data sensitivity | p. 7 (4.3. Ablation Studies) |
| Figure 1. Previous methods use misaligned paired data (e.g., image/point cloud 1 is closest to text 2) and freeze the text encoder trained on ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these issues, we propose a novel AlIgned 3D Open-Vocabulary SEmantic Segmentation framework, called AIDE. | Qualitative results of segmentation compared between baseline and AIDE. achieves significant improvements in all metrics, with hIoU, mIoUB, and mIoUN increasing from 32.1, 31.6, ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.4. Qualitative Results-Generalization), p. 7 (Figure/Table caption), p. 7 (4.3. Ablation Studies), p. 6 (4.2. Quantative Results), p. 6 (4.2. Quantative Results), p. 8 (4.4. Qualitative Results-Generalization) |
| Primary metric/result | Table 5. Ablation studies on different numbers of learnable tokens of AIDE on ScanNet (B15/N4). conduct a series of experiments as shown in Tab. ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Due to space limitations, the details of benchmarks and partitions are deferred to Appendix C.1. | p. 5 (4. Experiments) |
| body limitation/failure cue | Due to the space limitation, ablation studies on the choice of temperatures (Tab. | p. 6 (4.3. Ablation Studies) |
| body limitation/failure cue | Table 7. Ablation studies on using different text encoders of AIDE on ScanNet (B15/N4). this phenomenon. As generating over 30 captions per tem- perature ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | On the other side, AIDE still maintains a lead over the baseline, demonstrating its robustness to variations in vocabulary. | p. 8 (4.4. Qualitative Results-Generalization) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Benchmarks, Baselines, and Implementation Benchmarks and category partitions. | p. 5 (4. Experiments) |
| 5 and 6), and the choice of text encoders (Tab. | p. 6 (4.3. Ablation Studies) |
| Four trainable tokens are used in adapting text encoders. | p. 6 (4. Experiments) |
| One possible solution is fine-tuning VLMs to handle 3D data for better alignment between text encoders of VLMs and 3D models. | p. 5 (3.4. Adaptive Segmentation-Text Modeling) |
| Parameters and throughput comparison. | p. 8 (4.4. Qualitative Results-Generalization) |
| We also include a parameter and throughput analysis in Tab. | p. 8 (4.4. Qualitative Results-Generalization) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4. Experiments - extractive PDF cue:** Due to space limitations, the details of benchmarks and partitions are deferred to Appendix C.1.
- **p. 6 / 4.3. Ablation Studies - extractive PDF cue:** Due to the space limitation, ablation studies on the choice of temperatures (Tab.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 7. Ablation studies on using different text encoders of AIDE on ScanNet (B15/N4). this phenomenon. As generating over 30 captions per tem- perature will ...
- **p. 8 / 4.4. Qualitative Results-Generalization - extractive PDF cue:** On the other side, AIDE still maintains a lead over the baseline, demonstrating its robustness to variations in vocabulary.

- **PDF anchors reviewed:** datasets p. 5 (4. Experiments), p. 6 (4.2. Quantative Results), p. 5 (4. Experiments), p. 6 (4. Experiments), p. 8 (4.4. Qualitative Results-Generalization), p. 8 (4.4. Qualitative Results-Generalization), metrics p. 8 (4.4. Qualitative Results-Generalization), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption), p. 4 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (4. Experiments), baselines p. 6 (4.2. Quantative Results), p. 8 (4.4. Qualitative Results-Generalization), p. 8 (4.4. Qualitative Results-Generalization), p. 7 (4.3. Ablation Studies), p. 5 (4. Experiments), p. 5 (4. Experiments), results p. 8 (4.4. Qualitative Results-Generalization), p. 7 (Figure/Table caption), p. 7 (4.3. Ablation Studies), p. 6 (4.2. Quantative Results), p. 6 (4.2. Quantative Results), p. 8 (4.4. Qualitative Results-Generalization).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
