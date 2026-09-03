# Evaluation - SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=CHavqrN1X9; PDF retrieval source: https://openreview.net/pdf/04fc204cb3233c6ac9f5867e72c861a9e835bc65.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Figure/Table caption), p. 7 (4.2.1. SPATIAL PERCEPTION), p. 7 (4.3. Evaluation on General Capabilities), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption), p. 22 (Figure/Table caption)): Figure 1. We propose SpatioLM, a parameter-efficient framework that improves spatial intelligence in VLMs without extra 3D prior inputs or external spatial encoders. SpatioLM achieves SOTA performance on both spatial ...

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** To ensure rigorous evaluation and prevent data leakage, all training samples are strictly sourced from the official training splits of the respective datasets, reserving the ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** To systematically enhance the spatial intelligence of SpatioLM, we construct a comprehensive training corpus that unifies low-level spatial perception with high-level spatial understanding, spanning diverse ...
- **p. 7 / 4.3. Evaluation on General Capabilities - extractive body cue:** In contrast, SpatialMLLM exhibits a substantial decline in general benchmarks, with reductions ranging from 23% to 67%.
- **p. 7 / 4.3. Evaluation on General Capabilities - extractive body cue:** Its overall performance remains on par with the baseline and even improves on certain benchmarks (e.g., +12% on VideoMMMU).
- **p. 7 / 4.2.2. SPATIAL UNDERSTANDING - extractive body cue:** ScanQA is evaluated with BLEU-1 (B1), BLEU-4 (B4), METEOR (M), ROUGE-L (R), and CIDEr (C), while SQA3D uses exact match accuracy (E1) and its refined ...
- **p. 7 / 4.2.1. SPATIAL PERCEPTION - extractive body cue:** It significantly outperforms strong baselines on both single-image and multi-image metric depth, attains the highest accuracy on DA-2K, and demonstrates more stable generalization on a ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Evaluation results on LIBERO benchmark across 4 suites. P.T: pretraining on large-scale robot manipulation data; A.T: action type (D: discrete, C: continuous). SenseNovaSI-VLA0 ...
- **p. 19 / Figure/Table caption - extractive body cue:** Table 11. Detailed evaluation results on DA-2K benchmark. We shuffle the answer choices and report the average accuracy. The best and runner-up results are bolded ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 15 Datasets (p. 1); 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6); 4.3. Evaluation on General Capabilities (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. We propose SpatioLM, a parameter-efficient framework that improves spatial intelligence in VLMs without extra 3D prior inputs or external spatial encoders. SpatioLM ... | p. 1 (Figure/Table caption) |
| 4.2.1. SPATIAL PERCEPTION | EMPIRICAL / REAL-ROBOT OR HARDWARE | It significantly outperforms strong baselines on both single-image and multi-image metric depth, attains the highest accuracy on DA-2K, and demonstrates more stable generalization on ... | p. 7 (4.2.1. SPATIAL PERCEPTION) |
| 4.3. Evaluation on General Capabilities | EMPIRICAL / REAL-ROBOT OR HARDWARE | Its overall performance remains on par with the baseline and even improves on certain benchmarks (e.g., +12% on VideoMMMU). | p. 7 (4.3. Evaluation on General Capabilities) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4. Evaluation results on LIBERO benchmark across 4 suites. P.T: pretraining on large-scale robot manipulation data; A.T: action type (D: discrete, C: continuous). ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 11. Detailed evaluation results on DA-2K benchmark. We shuffle the answer choices and report the average accuracy. The best and runner-up results are ... | p. 19 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** To ensure rigorous evaluation and prevent data leakage, all training samples are strictly sourced from the official training splits of the respective datasets, reserving the ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** To systematically enhance the spatial intelligence of SpatioLM, we construct a comprehensive training corpus that unifies low-level spatial perception with high-level spatial understanding, spanning diverse ...
- **p. 7 / 4.3. Evaluation on General Capabilities - extractive body cue:** In contrast, SpatialMLLM exhibits a substantial decline in general benchmarks, with reductions ranging from 23% to 67%.
- **p. 7 / 4.3. Evaluation on General Capabilities - extractive body cue:** Its overall performance remains on par with the baseline and even improves on certain benchmarks (e.g., +12% on VideoMMMU).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We propose SpatioLM, a parameter-efficient framework that improves spatial intelligence in VLMs without extra 3D prior inputs or external spatial encoders. SpatioLM achieves ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. (a) Methods that explicitly leverage 3D priors, such as depth maps, point clouds, or camera parameters. (b) Methods that introduce an additional spatial ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Overview of SpatioLM. SpatioLM augments a frozen VLM with a plug-and-play Spatio-Vision Module. The Spatio-Vision Module elicits geometry-aware features from visual tokens and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative depth-tasks on the MD-S, MD- M, DA-2K, and DR benchmarks.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Overall evaluation results on depth benchmarks. Metric depth estimation for single-image (MD-S) and multi-images (MD-M) settings measured by δ < 1.25 ↑, relative ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative tasks on VSI-Bench.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Evaluation results on VSI-bench. The best and runner-up results are bolded and underlined, respectively. Methods Avg. Obj. Cht. Abs. Dist. Obj.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Evaluation results on ScanQA and SQA3D. ScanQA is evaluated with BLEU-1 (B1), BLEU-4 (B4), METEOR (M), ROUGE-L (R), and CIDEr (C), while SQA3D ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To ensure rigorous evaluation and prevent data leakage, all training samples are strictly sourced from the official training splits of the respective datasets, reserving ... | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Task/environment | To systematically enhance the spatial intelligence of SpatioLM, we construct a comprehensive training corpus that unifies low-level spatial perception with high-level spatial understanding, spanning ... | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 7 (4.3. Evaluation on General Capabilities) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Problem definition and notation), p. 4 (3.2. Spatio-Vision Module) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3.1. Problem definition and notation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| ScanQA is evaluated with BLEU-1 (B1), BLEU-4 (B4), METEOR (M), ROUGE-L (R), and CIDEr (C), while SQA3D uses exact match accuracy (E1) and its ... | definition/direction/unit from same section | p. 7 (4.2.2. SPATIAL UNDERSTANDING) |
| It significantly outperforms strong baselines on both single-image and multi-image metric depth, attains the highest accuracy on DA-2K, and demonstrates more stable generalization on ... | definition/direction/unit from same section | p. 7 (4.2.1. SPATIAL PERCEPTION) |
| Table 4. Evaluation results on LIBERO benchmark across 4 suites. P.T: pretraining on large-scale robot manipulation data; A.T: action type (D: discrete, C: continuous). ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 11. Detailed evaluation results on DA-2K benchmark. We shuffle the answer choices and report the average accuracy. The best and runner-up results are ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Table 16. Detailed MVBench subtask results. ∆denotes the score change from the base model to SpatioLM on the same backbone. Category Subtask InternVL3.5-8B SenseNovaSI-8B ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| All models are trained on 64 NVIDIA H200 GPUs using AdamW (β1 = 0.9, β2 = 0.95, weight decay = 0.1), with a cosine ... | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| Figure 1. We propose SpatioLM, a parameter-efficient framework that improves spatial intelligence in VLMs without extra 3D prior inputs or external spatial encoders. SpatioLM ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 3. Overview of SpatioLM. SpatioLM augments a frozen VLM with a plug-and-play Spatio-Vision Module. The Spatio-Vision Module elicits geometry-aware features from visual tokens ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| It significantly outperforms strong baselines on both single-image and multi-image metric depth, attains the highest accuracy on DA-2K, and demonstrates more stable generalization on ... | comparison identity and matched condition | p. 7 (4.2.1. SPATIAL PERCEPTION) |
| We compare against three groups of baselines: proprietary closed-source, open-source, and spatialspecialized models. | comparison identity and matched condition | p. 7 (4.2.1. SPATIAL PERCEPTION) |
| Table 4. Evaluation results on LIBERO benchmark across 4 suites. P.T: pretraining on large-scale robot manipulation data; A.T: action type (D: discrete, C: continuous). ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 1. We propose SpatioLM, a parameter-efficient framework that improves spatial intelligence in VLMs without extra 3D prior inputs or external spatial encoders. SpatioLM ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Figure 2. (a) Methods that explicitly leverage 3D priors, such as depth maps, point clouds, or camera parameters. (b) Methods that introduce an additional ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Table 5. Ablation study on the SV-Module, VTS, and DGS. SV-Module VTS DGS MD-S DA-2K VSI-Bench ✗ ✗ ✗ 52.6 71.8 68.7 | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1. We propose SpatioLM, a parameter-efficient framework that improves spatial intelligence in VLMs without extra 3D prior inputs or external spatial encoders. SpatioLM ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| During evaluation, the Dual DPT Head can be removed. | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| ScanQA is evaluated with BLEU-1 (B1), BLEU-4 (B4), METEOR (M), ROUGE-L (R), and CIDEr (C), while SQA3D uses exact match accuracy (E1) and its ... | component/input/data sensitivity | p. 7 (4.2.2. SPATIAL UNDERSTANDING) |
| Figure 2. (a) Methods that explicitly leverage 3D priors, such as depth maps, point clouds, or camera parameters. (b) Methods that introduce an additional ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Table 5. Ablation study on the SV-Module, VTS, and DGS. SV-Module VTS DGS MD-S DA-2K VSI-Bench ✗ ✗ ✗ 52.6 71.8 68.7 | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 6. Sensitivity analysis on loss weights. α β γ VSI-Bench ScanQA(C) SQA3D(ER1) 0.4 | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are summarized as follows: • We propose SpatioLM, a purely 2D vision-language framework that elicits implicit 3D geometric structure from pretrained ... | Figure 1. We propose SpatioLM, a parameter-efficient framework that improves spatial intelligence in VLMs without extra 3D prior inputs or external spatial encoders. SpatioLM ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Figure/Table caption), p. 7 (4.2.1. SPATIAL PERCEPTION), p. 7 (4.3. Evaluation on General Capabilities), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption), p. 22 (Figure/Table caption) |
| Primary metric/result | It significantly outperforms strong baselines on both single-image and multi-image metric depth, attains the highest accuracy on DA-2K, and demonstrates more stable generalization on ... | numeric claim only at cited anchor | p. 7 (4.2.1. SPATIAL PERCEPTION) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Training is conducted for 600 epochs on spatial perception tasks and 2 epochs on spatial understanding tasks.
- **p. 6 / 3.3. Loss Design - extractive body cue:** Answer: 211 Object size Question: Measuring from the closest point of each object, what is the distance between the toilet and the bed (in meters)?

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Despite the effectiveness of SpatioLM, several limitations remain. | p. 9 (5. Conclusion) |
| body limitation/failure cue | Impact Statement Addressing the critical limitation of multimodal large models in visual spatial reasoning, this work proposes SpatioLM, a parameter-efficient spatial VLMs that enhances ... | p. 9 (5. Conclusion) |
| body limitation/failure cue | Table 15. Failure consistency analysis on VSI-Bench. Consistency denotes the ratio of shared failures over SpatioLM failures. Task Type Ours Fail Base Fail Shared ... | p. 21 (Figure/Table caption) |
| body limitation/failure cue | Results indicate that, despite large-scale training targeted at spatial intelligence, the performance degradation of SpatioLM on general tasks is considerably smaller than that of ... | p. 7 (4.3. Evaluation on General Capabilities) |
| body limitation/failure cue | Figure 8. Visualization samples of our spatial perception benchmarks. The first row shows ground-truth single-image metric depth (MD-S), and the second row shows multi-image ... | p. 16 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All models are trained on 64 NVIDIA H200 GPUs using AdamW (β1 = 0.9, β2 = 0.95, weight decay = 0.1), with a cosine ... | p. 6 (4.1. Experimental Setup) |
| Training is conducted for 600 epochs on spatial perception tasks and 2 epochs on spatial understanding tasks. | p. 6 (4.1. Experimental Setup) |
| We compare against Spatial-MLLM (Wu et al., 2025), a representative method that enhances spatial intelligence via an external spatial encoder; the results are summarized ... | p. 7 (4.3. Evaluation on General Capabilities) |
| We employ a pretrained VLM constructed with a vision encoder and an LLM, in which all parameters of the vision encoder and the LLM ... | p. 3 (3.2. Spatio-Vision Module) |
| Given the visual input Xv, the vision tokens generated by the vision encoder are mathematically denoted as: Hv 0 = Ev(Xv), Hv 0 ∈RT ... | p. 3 (3.2. Spatio-Vision Module) |
| Importantly, this alternating attention is applied exclusively inside the SV-Block and does not modify the causal self-attention mechanism of the frozen LLM decoder. | p. 5 (3.2. Spatio-Vision Module) |
| By supervising these dense geometric predictions, the injected features are encouraged to encode camera-aware 3D priors that are crucial for downstream spatial tasks. | p. 5 (3.2. Spatio-Vision Module) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5. Conclusion - extractive body cue:** Despite the effectiveness of SpatioLM, several limitations remain.
- **p. 9 / 5. Conclusion - extractive body cue:** Impact Statement Addressing the critical limitation of multimodal large models in visual spatial reasoning, this work proposes SpatioLM, a parameter-efficient spatial VLMs that enhances spatial ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 15. Failure consistency analysis on VSI-Bench. Consistency denotes the ratio of shared failures over SpatioLM failures. Task Type Ours Fail Base Fail Shared Consistency ...
- **p. 7 / 4.3. Evaluation on General Capabilities - extractive body cue:** Results indicate that, despite large-scale training targeted at spatial intelligence, the performance degradation of SpatioLM on general tasks is considerably smaller than that of baseline ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 8. Visualization samples of our spatial perception benchmarks. The first row shows ground-truth single-image metric depth (MD-S), and the second row shows multi-image metric ...

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.3. Evaluation on General Capabilities), p. 7 (4.3. Evaluation on General Capabilities), metrics p. 7 (4.2.2. SPATIAL UNDERSTANDING), p. 7 (4.2.1. SPATIAL PERCEPTION), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption), p. 22 (Figure/Table caption), p. 6 (4.1. Experimental Setup), baselines p. 7 (4.2.1. SPATIAL PERCEPTION), p. 7 (4.2.1. SPATIAL PERCEPTION), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 1 (Figure/Table caption), p. 7 (4.2.1. SPATIAL PERCEPTION), p. 7 (4.3. Evaluation on General Capabilities), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption), p. 22 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
