# Evaluation - GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=0fib2BYc0L; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247573. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (3 EXPERIMENTS), p. 9 (Figure/Table caption), p. 6 (3 EXPERIMENTS), p. 19 (Figure/Table caption), p. 5 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS)): In terms of specific metrics, models fine-tuned using the GPT4Scene framework (based on the ScanAlign dataset) show outstanding performance: Qwen2-VL-7B (GPT4Scene) achieves a BLEU-1 score of 44.4 and a CIDEr ...

## Evaluation Body Digest

- **p. 9 / 3 EXPERIMENTS - extractive body cue:** The experiments are conducted across two different datasets, ScanNet ("S") and ARKitScenes ("NS"), to test the framework's robustness in various types of 3D environments.
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** Using the ScanRefer (single/multi-object grounding) and Multi3DRef (combinatorial multi-object grounding) benchmarks, this analysis validates the enhancement of spatial localization capabilities in Vision Language Models (VLMs) ...
- **p. 5 / 3 EXPERIMENTS - extractive body cue:** (2017a) dataset and includes three tasks: 3D question answering (ScanQA Azuma et al.
- **p. 5 / 3 EXPERIMENTS - extractive body cue:** 3.1 IMPLEMENTATION DETAILS Our 3D scene understanding benchmark is based on the ScanNet Dai et al.
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** (2025) ✗ ✓ 47.1 16.2 19.8 - 102.1 58.6 - InternVL3-8B (GPT4Scene) ✗ ✓ 45.1 16.2 19.5 47.8 96.8 61.9 64.5 Qwen2-VL-7B (GPT4Scene) ✗ ✓ ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** For our comparison, we selected a total of 1,000 questions from the ScanQA dataset, distributed across six distinct categories: Spatial Relationship, Object Attribute, Existence & ...
- **p. 9 / 3 EXPERIMENTS - extractive body cue:** The key results visualized in the chart show that models integrated with GPT4Scene consistently outperform their baseline counterparts across both datasets.
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** The evaluation revealed a clear pattern: GPT4Scene demonstrates a significant performance advantage in object-centric categories, particularly excelling in tasks related to Relational Refer and Existence ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3 EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | In terms of specific metrics, models fine-tuned using the GPT4Scene framework (based on the ScanAlign dataset) show outstanding performance: Qwen2-VL-7B (GPT4Scene) achieves a BLEU-1 ... | p. 5 (3 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5: GPT-Score evaluation. GPT4Scene holds an advantage on object-level tasks than Chat-scene. minimal improvements for the 3D QA task, which involves more general ... | p. 9 (Figure/Table caption) |
| 3 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | These models not only significantly outperform the untuned baseline VLMs but also comprehensively outperform the previous SOTA models in the 3D point cloud LLM ... | p. 6 (3 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 14: Full Evaluation of 3D Dense Caption on Scan2Cap Chen et al. (2021). Scan2Cap Chen et al. (2021), while Table 15 and Table ... | p. 19 (Figure/Table caption) |
| 3 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | (2025b), and Qwen2.5-VL 8B Team (2024d), and ultimately achieved state-of-the-art (SOTA) results. | p. 5 (3 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 9 / 3 EXPERIMENTS - extractive body cue:** The experiments are conducted across two different datasets, ScanNet ("S") and ARKitScenes ("NS"), to test the framework's robustness in various types of 3D environments.
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** Using the ScanRefer (single/multi-object grounding) and Multi3DRef (combinatorial multi-object grounding) benchmarks, this analysis validates the enhancement of spatial localization capabilities in Vision Language Models (VLMs) ...
- **p. 5 / 3 EXPERIMENTS - extractive body cue:** (2017a) dataset and includes three tasks: 3D question answering (ScanQA Azuma et al.
- **p. 5 / 3 EXPERIMENTS - extractive body cue:** 3.1 IMPLEMENTATION DETAILS Our 3D scene understanding benchmark is based on the ScanNet Dai et al.
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** (2025) ✗ ✓ 47.1 16.2 19.8 - 102.1 58.6 - InternVL3-8B (GPT4Scene) ✗ ✓ 45.1 16.2 19.5 47.8 96.8 61.9 64.5 Qwen2-VL-7B (GPT4Scene) ✗ ✓ ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** For our comparison, we selected a total of 1,000 questions from the ScanQA dataset, distributed across six distinct categories: Spatial Relationship, Object Attribute, Existence & ...
- **p. 9 / 3 EXPERIMENTS - extractive body cue:** The key results visualized in the chart show that models integrated with GPT4Scene consistently outperform their baseline counterparts across both datasets.
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** The evaluation revealed a clear pattern: GPT4Scene demonstrates a significant performance advantage in object-centric categories, particularly excelling in tasks related to Relational Refer and Existence ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of GPT4Scene. GPT4Scene understands 3D scenes and performs tasks like 3D question answering, dense captioning, and visual grounding using only video input. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: The framework of GPT4Scene. A scene video is processed by sampling frames, reconstructing a point cloud, and generating a BEV image. Object locations ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: The zero-shot capability of GPT4Scene. Video + GPT4Scene Inference without Fine-tuning. Zero-shot 3D QA ROUGE@ScanQA EM-1@SQA3D VID +4Scene VID +4Scene 3D LLM Based ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2: ScanAlign: Datasets used for training GPT4Scene (Supervised Fine-Tuning), Source Data Type Task Type Samples Overall Scene-Level ScanQA
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3: Evaluation of 3D question answer on ScanQA Azuma et al. (2022) & SQA3D Ma et al. (2023). 3D Question Answering Point Encoder Vision ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4: Evaluation of 3D dense caption on Scan2Cap Chen et al. (2021). Our results outper- form those of existing 3D LLM based models. 3D ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 6: Ablation study on the Efficacy of GPT4Scene. (1) on fully fine-tuned models with GPT4Scene; (2) on pure-video fine-tuned models; (3) in a zero-shot ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 7: Ablation Study on BEV Reconstruction Quality. The quality of BEV reconstruction has a negligible impact on QA performance, since the BEV mainly offers ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The experiments are conducted across two different datasets, ScanNet ("S") and ARKitScenes ("NS"), to test the framework's robustness in various types of 3D environments. | embodiment, simulator version and control stack | p. 9 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS) |
| Task/environment | Using the ScanRefer (single/multi-object grounding) and Multi3DRef (combinatorial multi-object grounding) benchmarks, this analysis validates the enhancement of spatial localization capabilities in Vision Language Models ... | reset, timeout, object/scene variation | p. 6 (3 EXPERIMENTS), p. 5 (3 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (2 METHODOLOGY), p. 3 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In terms of specific metrics, models fine-tuned using the GPT4Scene framework (based on the ScanAlign dataset) show outstanding performance: Qwen2-VL-7B (GPT4Scene) achieves a BLEU-1 ... | definition/direction/unit from same section | p. 5 (3 EXPERIMENTS) |
| This strongly confirms that the GPT4Scene framework is robust to the geometric precision of the BEV map, depending on it for overall layout rather ... | definition/direction/unit from same section | p. 8 (3 EXPERIMENTS) |
| (2025) ✗ ✓ 47.1 16.2 19.8 - 102.1 58.6 - InternVL3-8B (GPT4Scene) ✗ ✓ 45.1 16.2 19.5 47.8 96.8 61.9 64.5 Qwen2-VL-7B (GPT4Scene) ✗ ... | definition/direction/unit from same section | p. 6 (3 EXPERIMENTS) |
| Figure 5: GPT-Score evaluation. GPT4Scene holds an advantage on object-level tasks than Chat-scene. minimal improvements for the 3D QA task, which involves more general ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| We propose a novel GPT Score for 3D QA assessment, using the state-of-the-art 3D LLM Chat-scene Huang et al. | definition/direction/unit from same section | p. 7 (3 EXPERIMENTS) |
| Furthermore, our improved Qwen2.5-VL-7B (GPT4Scene) model sets a new state-of-the-art, elevating these scores to 65.6 and 67.3. | definition/direction/unit from same section | p. 7 (3 EXPERIMENTS) |
| Table 13: Full Evaluation of 3D Question Answering on SQA3D Ma et al. (2023). Methods IoU@0.25 IoU@0.5 CIDEr BLEU-4 METEOR ROUGE | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Our GPT4Scene-integrated Visual LLMs, including Qwen2-VL-7B (GPT4Scene) and Qwen2.5-VL-7B (GPT4Scene), achieve breakthrough performance using only visual inputs (video + BEV images). | definition/direction/unit from same section | p. 6 (3 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| These models not only significantly outperform the untuned baseline VLMs but also comprehensively outperform the previous SOTA models in the 3D point cloud LLM ... | comparison identity and matched condition | p. 6 (3 EXPERIMENTS) |
| The experiment compared various reconstruction methods (e.g., the baseline BundleFusion, SLAM3R at different frame rates) on the ScanQA and SQA3D benchmarks. | comparison identity and matched condition | p. 8 (3 EXPERIMENTS) |
| The key results visualized in the chart show that models integrated with GPT4Scene consistently outperform their baseline counterparts across both datasets. | comparison identity and matched condition | p. 9 (3 EXPERIMENTS) |
| Consequently, the VLM can precisely ground textual descriptions in 3D scene details without requiring 3D point cloud data, thereby establishing a new state-of-the-art (SOTA) ... | comparison identity and matched condition | p. 6 (3 EXPERIMENTS) |
| Nevertheless, the model maintains a strong baseline performance even on small objects, confirming the overall effectiveness and robustness of the GPT4Scene framework across various ... | comparison identity and matched condition | p. 8 (3 EXPERIMENTS) |
| (2025b), and Qwen2.5-VL 8B Team (2024d), and ultimately achieved state-of-the-art (SOTA) results. | comparison identity and matched condition | p. 5 (3 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Finally, Subsection 3.3 details the ablation study, demonstrating the effectiveness of individual components. | component/input/data sensitivity | p. 5 (3 EXPERIMENTS) |
| Table 6: Ablation study on the Efficacy of GPT4Scene. (1) on fully fine-tuned models with GPT4Scene; (2) on pure-video fine-tuned models; (3) in a ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 6. First, we remove the regularized formatting from the answers. Next, we clean the answers by addressing singular/plural forms and case sensitivity. This ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| 3.3 ABLATION STUDY In this section, we conduct ablation studies to validate the effectiveness of GPT4Scene. | component/input/data sensitivity | p. 7 (3 EXPERIMENTS) |
| Our experimental analysis demonstrates that the baseline Qwen2-VL-7B model without fine-tuning shows constrained capability in 3D QA scenarios. | component/input/data sensitivity | p. 5 (3 EXPERIMENTS) |
| Next, we perform module-wise ablation to assess individual components. | component/input/data sensitivity | p. 7 (3 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our paper makes these major contributions: • We introduce GPT4Scene, a framework that enhances Vision-Language Models (VLMs) to comprehend 3D scenes directly from pure ... | In terms of specific metrics, models fine-tuned using the GPT4Scene framework (based on the ScanAlign dataset) show outstanding performance: Qwen2-VL-7B (GPT4Scene) achieves a BLEU-1 ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (3 EXPERIMENTS), p. 9 (Figure/Table caption), p. 6 (3 EXPERIMENTS), p. 19 (Figure/Table caption), p. 5 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS) |
| Primary metric/result | Figure 5: GPT-Score evaluation. GPT4Scene holds an advantage on object-level tasks than Chat-scene. minimal improvements for the 3D QA task, which involves more general ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 3 EXPERIMENTS - extractive body cue:** For the experiment, we sample N=32 frames per video (512×490 resolution) for all models.
- **p. 5 / 3 EXPERIMENTS - extractive body cue:** Training is done for one epoch with a base learning rate of 5e-6 and cosine annealing, completing in about 6 hours on 8×A100 GPUs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 12: Failure Cases of GPT4Scene. 26 | p. 26 (Figure/Table caption) |
| body limitation/failure cue | Despite relying on point cloud annotations for marker generation due to benchmark constraints, we aim to address this by generating STO-markers from video segmentation ... | p. 9 (4 CONCLUSION) |
| body limitation/failure cue | By providing global scene context through BEV images and establishing spatio-temporal consistency with STO-markers, the framework successfully empowers VLMs to overcome their previous limitations, ... | p. 9 (3 EXPERIMENTS) |
| body limitation/failure cue | First, we evaluate its robustness, including performance on small objects, followed by analyzing the robustness of STO-markers and reconstruction quality. | p. 7 (3 EXPERIMENTS) |
| body limitation/failure cue | This strongly confirms that the GPT4Scene framework is robust to the geometric precision of the BEV map, depending on it for overall layout rather ... | p. 8 (3 EXPERIMENTS) |
| body limitation/failure cue | Nevertheless, the model maintains a strong baseline performance even on small objects, confirming the overall effectiveness and robustness of the GPT4Scene framework across various ... | p. 8 (3 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training is done for one epoch with a base learning rate of 5e-6 and cosine annealing, completing in about 6 hours on 8×A100 GPUs. | p. 5 (3 EXPERIMENTS) |
| 3.1 IMPLEMENTATION DETAILS Our 3D scene understanding benchmark is based on the ScanNet Dai et al. | p. 5 (3 EXPERIMENTS) |
| 3D Question Answering Point Encoder Vision Encoder ScanQA (val) SQA3D (val) Methods BLEU-1 BLEU-4 METEOR ROUGE CIDEr EM-1 EM-R1 Task-Specific Model ScanQA Azuma et ... | p. 6 (3 EXPERIMENTS) |
| Their visual encoders and cross-modal fusion capabilities are consequently weaker. | p. 4 (2 METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 26 / Figure/Table caption - extractive body cue:** Figure 12: Failure Cases of GPT4Scene. 26
- **p. 9 / 4 CONCLUSION - extractive body cue:** Despite relying on point cloud annotations for marker generation due to benchmark constraints, we aim to address this by generating STO-markers from video segmentation in ...
- **p. 9 / 3 EXPERIMENTS - extractive body cue:** By providing global scene context through BEV images and establishing spatio-temporal consistency with STO-markers, the framework successfully empowers VLMs to overcome their previous limitations, thereby ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** First, we evaluate its robustness, including performance on small objects, followed by analyzing the robustness of STO-markers and reconstruction quality.
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** This strongly confirms that the GPT4Scene framework is robust to the geometric precision of the BEV map, depending on it for overall layout rather than ...
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** Nevertheless, the model maintains a strong baseline performance even on small objects, confirming the overall effectiveness and robustness of the GPT4Scene framework across various object ...

- **Evidence anchors reviewed:** datasets p. 9 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 5 (3 EXPERIMENTS), p. 5 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), metrics p. 5 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 9 (Figure/Table caption), p. 7 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), baselines p. 6 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 9 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 5 (3 EXPERIMENTS), results p. 5 (3 EXPERIMENTS), p. 9 (Figure/Table caption), p. 6 (3 EXPERIMENTS), p. 19 (Figure/Table caption), p. 5 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
