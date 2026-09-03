# Evaluation - AutoOcc: Automatic Open-Ended Semantic Occupancy Annotation via Vision-Language Guided Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_AutoOcc_Automatic_Open-Ended_Semantic_Occupancy_Annotation_via_Vision-Language_Guided_Gaussian_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_AutoOcc_Automatic_Open-Ended_Semantic_Occupancy_Annotation_via_Vision-Language_Guided_Gaussian_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption), p. 6 (4.2. Performance Evaluation and Analysis)): As shown in Table 2, our vision-centric method outperforms these pipelines that utilize LiDAR point clouds.

## Evaluation Body Digest

- **p. 6 / 4.1. Implementation Details - extractive body cue:** We use two benchmarks for evaluation: Occ3D-nuScenes, which is used to compare the performance of our method with other occupancy annotation methods for specific categories, ...
- **p. 7 / 4.2. Performance Evaluation and Analysis - extractive body cue:** Novel class refers to entirely new, unseen semantics in nuScenes, while base class includes those seen during training.
- **p. 7 / 4.2. Performance Evaluation and Analysis - extractive body cue:** Our method enables high-quality annotation of semantic 3D occupancy, capturing fine-grained geometry, structurally challenging regions, and dynamic objects across complex scenes. demonstrates better performance, based ...
- **p. 6 / 4.1. Implementation Details - extractive body cue:** We set the resolutions of images as 900 × 1600 for Occ3D-nuScenes and 370 × 1226 for SemanticKITTI.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Semantic occupancy annotation on Occ3D-nuScenes [46]. C represents camera, and L denotes LiDAR. "cons. veh." and "drive. surf." stand for construction vehicles and ...
- **p. 6 / 4.2. Performance Evaluation and Analysis - extractive body cue:** Undoubtedly, this strategy leads to the loss of crucial details and misalignment between semantics and representations.
- **p. 7 / 4.2. Performance Evaluation and Analysis - extractive body cue:** Zero-shot cross-dataset performance on SemanticKITTI [2].
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overall pipeline of our method. AutoOcc is a vision-centric automated pipeline for semantic occupancy annotation. Our method starts with multi-view image inputs (optionally ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Implementation Details (p. 6); 4.2. Performance Evaluation and Analysis (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Performance Evaluation and Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 2, our vision-centric method outperforms these pipelines that utilize LiDAR point clouds. | p. 6 (4.2. Performance Evaluation and Analysis) |
| 4.2. Performance Evaluation and Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 2, using pure visual input, our method outperforms GaussianOcc [13], which utilizes vanilla GS as an intermediate representation. | p. 7 (4.2. Performance Evaluation and Analysis) |
| 4.2. Performance Evaluation and Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | In extreme weather conditions (e.g., rain and nighttime), our method maintains robust performance, achieving annotation results comparable to or even surpassing manually labeled ground ... | p. 7 (4.2. Performance Evaluation and Analysis) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. AutoOcc is a fully automatic, vision-centric pipeline for open-ended semantic 3D occupancy annotation. Our method achieves more efficient and effective semantic occupancy ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 1. Comparisons between AutoOcc and existing semantic occupancy annotation pipelines. The definitions of closed-set, open- set, and open-ended are introduced in Section 2. ... | p. 2 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Implementation Details - extractive body cue:** We use two benchmarks for evaluation: Occ3D-nuScenes, which is used to compare the performance of our method with other occupancy annotation methods for specific categories, ...
- **p. 7 / 4.2. Performance Evaluation and Analysis - extractive body cue:** Novel class refers to entirely new, unseen semantics in nuScenes, while base class includes those seen during training.
- **p. 7 / 4.2. Performance Evaluation and Analysis - extractive body cue:** Our method enables high-quality annotation of semantic 3D occupancy, capturing fine-grained geometry, structurally challenging regions, and dynamic objects across complex scenes. demonstrates better performance, based ...
- **p. 6 / 4.1. Implementation Details - extractive body cue:** We set the resolutions of images as 900 × 1600 for Occ3D-nuScenes and 370 × 1226 for SemanticKITTI.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. AutoOcc is a fully automatic, vision-centric pipeline for open-ended semantic 3D occupancy annotation. Our method achieves more efficient and effective semantic occupancy auto-labeling ...
- **p. 2 / Figure/Table caption - extractive body cue:** Table 1. Comparisons between AutoOcc and existing semantic occupancy annotation pipelines. The definitions of closed-set, open- set, and open-ended are introduced in Section 2. Our ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overall pipeline of our method. AutoOcc is a vision-centric automated pipeline for semantic occupancy annotation. Our method starts with multi-view image inputs (optionally ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Vision-Language Guided Gaussian Splatting (VL- GS) efficiently reconstructs semantic instances using a scalable strategy guided by semantic attention maps from VLMs. Addi- tionally, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Semantic occupancy annotation on Occ3D-nuScenes [46]. C represents camera, and L denotes LiDAR. "cons. veh." and "drive. surf." stand for construction vehicles and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Zero-shot cross-dataset performance on SemanticKITTI [2]. Novel class refers to entirely new, unseen semantics in nuScenes, while base class includes those seen during ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative results of semantic occupancy annotation on Occ3D-nuScenes [46]. Our method enables high-quality annotation of semantic 3D occupancy, capturing fine-grained geometry, structurally challenging ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Comparisons of annotation efficiency. Open-ended stands for the annotation capability for undefined classes. Label-free means training without any human-labeled annotations. † indicates the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We use two benchmarks for evaluation: Occ3D-nuScenes, which is used to compare the performance of our method with other occupancy annotation methods for specific ... | embodiment, simulator version and control stack | p. 6 (4.1. Implementation Details), p. 7 (4.2. Performance Evaluation and Analysis) |
| Task/environment | Novel class refers to entirely new, unseen semantics in nuScenes, while base class includes those seen during training. | reset, timeout, object/scene variation | p. 7 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (3. Method), p. 4 (3.1. Vision-Language Guidance) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 6 (3.2. VL-GS), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2. Semantic occupancy annotation on Occ3D-nuScenes [46]. C represents camera, and L denotes LiDAR. "cons. veh." and "drive. surf." stand for construction vehicles ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Undoubtedly, this strategy leads to the loss of crucial details and misalignment between semantics and representations. | definition/direction/unit from same section | p. 6 (4.2. Performance Evaluation and Analysis) |
| Our method enables high-quality annotation of semantic 3D occupancy, capturing fine-grained geometry, structurally challenging regions, and dynamic objects across complex scenes. demonstrates better performance, ... | definition/direction/unit from same section | p. 7 (4.2. Performance Evaluation and Analysis) |
| Zero-shot cross-dataset performance on SemanticKITTI [2]. | definition/direction/unit from same section | p. 7 (4.2. Performance Evaluation and Analysis) |
| Figure 2. Overall pipeline of our method. AutoOcc is a vision-centric automated pipeline for semantic occupancy annotation. Our method starts with multi-view image inputs ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 3. Vision-Language Guided Gaussian Splatting (VL- GS) efficiently reconstructs semantic instances using a scalable strategy guided by semantic attention maps from VLMs. Addi- ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 6. Semantic occupancy of dynamics. AutoOcc accurately annotates the semantic occupancy of dynamic objects, maintains spatiotemporal consistency, and infers occluded parts. | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We evaluate our method against the state-of-the-art (SOTA) methods for automatic semantic occupancy annotation, including offline methods [32, 49, 51] and self-supervised online methods ... | comparison identity and matched condition | p. 6 (4.2. Performance Evaluation and Analysis) |
| Compared with 2D-to-3D projection methods. | comparison identity and matched condition | p. 6 (4.2. Performance Evaluation and Analysis) |
| All compared methods are trained on Occ3D-nuScenes and evaluated on SemanticKITTI. | comparison identity and matched condition | p. 7 (4.2. Performance Evaluation and Analysis) |
| As shown in Table 2, using pure visual input, our method outperforms GaussianOcc [13], which utilizes vanilla GS as an intermediate representation. | comparison identity and matched condition | p. 7 (4.2. Performance Evaluation and Analysis) |
| Table 1. Comparisons between AutoOcc and existing semantic occupancy annotation pipelines. The definitions of closed-set, open- set, and open-ended are introduced in Section 2. ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Comparisons of annotation efficiency. | comparison identity and matched condition | p. 8 (4.3. Zero-shot and Generalization Ability) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1. AutoOcc is a fully automatic, vision-centric pipeline for open-ended semantic 3D occupancy annotation. Our method achieves more efficient and effective semantic occupancy ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Similar to [59, 66], we evaluate without the "other" and "other flat" classes. | component/input/data sensitivity | p. 6 (4.1. Implementation Details) |
| Selfsupervised methods enable occupancy estimation from image features without relying on manual annotations. | component/input/data sensitivity | p. 7 (4.2. Performance Evaluation and Analysis) |
| Label-free means training without any human-labeled annotations. † indicates the use of VLMs to obtain 2D semantics instead of human labeling. | component/input/data sensitivity | p. 8 (4.3. Zero-shot and Generalization Ability) |
| Table 5. The effect of each module in our method. SFM is short for the self-estimated flow module, and SSG denotes the employ- ment ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 1. Comparisons between AutoOcc and existing semantic occupancy annotation pipelines. The definitions of closed-set, open- set, and open-ended are introduced in Section 2. ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions include: • We present AutoOcc, a vision-centric automatic annotation pipeline that supports open-ended semantic 3D occupancy label generation, based on vision-language ... | As shown in Table 2, our vision-centric method outperforms these pipelines that utilize LiDAR point clouds. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption), p. 6 (4.2. Performance Evaluation and Analysis) |
| Primary metric/result | As shown in Table 2, using pure visual input, our method outperforms GaussianOcc [13], which utilizes vanilla GS as an intermediate representation. | numeric claim only at cited anchor | p. 7 (4.2. Performance Evaluation and Analysis) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Implementation Details - extractive body cue:** During optimization, we scale the image size to 225 × 400 and double it every 300 steps until reaching the original resolution.
- **p. 6 / 4.1. Implementation Details - extractive body cue:** The learning rate for the position parameters decays every 250 steps with a decay rate of 0.98.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In extreme weather conditions (e.g., rain and nighttime), our method maintains robust performance, achieving annotation results comparable to or even surpassing manually labeled ground ... | p. 7 (4.2. Performance Evaluation and Analysis) |
| body limitation/failure cue | While the aforementioned approaches do not require additional supervision, they struggle with efficiently modeling semantic geometry and neglect dynamic objects, leading to performance degradation. | p. 7 (4.2. Performance Evaluation and Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The learning rate for the position parameters decays every 250 steps with a decay rate of 0.98. | p. 6 (4.1. Implementation Details) |
| We use the AdamW optimizer for optimization with an initial learning rate of 0.005. | p. 6 (4.1. Implementation Details) |
| Metric mIoU-base denotes the mIoU computed solely on base classes from Occ3D-nuScenes. | p. 7 (4.2. Performance Evaluation and Analysis) |
| Specifically, we use the attention map generation method [1, 29] to compute and aggregate the attentions from transformer decoder, with N output tokens S ... | p. 4 (3.1. Vision-Language Guidance) |
| We aggregate the multi-frame of LiDAR points over time and compute the anchor centers pc = (xi c, yi c, zi c). | p. 5 (3.2. VL-GS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.2. Performance Evaluation and Analysis - extractive body cue:** In extreme weather conditions (e.g., rain and nighttime), our method maintains robust performance, achieving annotation results comparable to or even surpassing manually labeled ground truth.
- **p. 7 / 4.2. Performance Evaluation and Analysis - extractive body cue:** While the aforementioned approaches do not require additional supervision, they struggle with efficiently modeling semantic geometry and neglect dynamic objects, leading to performance degradation.

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Implementation Details), p. 7 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis), p. 6 (4.1. Implementation Details), metrics p. 6 (Figure/Table caption), p. 6 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis), p. 3 (Figure/Table caption), p. 5 (Figure/Table caption), baselines p. 6 (4.2. Performance Evaluation and Analysis), p. 6 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis), p. 2 (Figure/Table caption), p. 8 (4.3. Zero-shot and Generalization Ability), results p. 6 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption), p. 6 (4.2. Performance Evaluation and Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
