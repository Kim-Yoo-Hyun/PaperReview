# Evaluation - SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Evaluation), p. 5 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (5.2. Evaluation), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption)): Furthermore, under a fair comparison using the identical Qwen2.5 base model, SpatialStack significantly outperforms other concurrent geometry-aware MLLMs, such as Spatial-MLLM [45], VG-LLM [53], and Cambrian-S [48].

## Evaluation Body Digest

- **p. 7 / 5.1. Training - extractive body cue:** VLM-3R reformulates spatial question-answer pairs in a VSI-Bench-style format, producing diverse reasoning tasks such as relative direction, object counting, and absolute distance estimation from real-world ...
- **p. 7 / 5.2. Evaluation - extractive body cue:** These benchmarks cover a wide range of tasks, such as depth and distance estimation, object-relation reasoning, and videobased spatial understanding.
- **p. 6 / 5. Experiments - extractive body cue:** We describe our training setup in Sec.
- **p. 7 / 5.2. Evaluation - extractive body cue:** Following the official protocol, we report mean MCA accuracy and Mean Relative Accuracy for NA across confidence thresholds C = 0.5, 0.55, . . . ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Cross-benchmark Ablation. SpatialStack achieves the best cross-task transfer ability, obtaining the highest scores on VSI-Bench, SPAR-Bench, CV-Bench, and the overall aver- age, while ...
- **p. 7 / 5.1. Training - extractive body cue:** We fine-tune the model using the standard language modeling cross-entropy loss.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 7. Geometry-Language Fusion Order Ablation. Com- parison of our progressive hierarchical alignment against a reverse fusion strategy and baseline models. deep features. Tab. 6 ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. SpatialStack: Layered Geometry-Language Fusion. Conventional VLMs (a) fuse only a single deep geometry feature with vision tokens, which limits both fine-grained spatial understanding ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.2. Evaluation (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Furthermore, under a fair comparison using the identical Qwen2.5 base model, SpatialStack significantly outperforms other concurrent geometry-aware MLLMs, such as Spatial-MLLM [45], VG-LLM [53], ... | p. 7 (5.2. Evaluation) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4. Effect of Geometry Injection Layers on Spatial Tasks. Deeper layers improve high-level tasks, while low-level tasks peak at layer 11 and decline ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Ablation Results on Geometry Token Fusion Depth. Simply fusing multi-layer geometry features to the visual features yields suboptimal performance, while selecting an ... | p. 5 (Figure/Table caption) |
| 5.2. Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Applying our framework to both Qwen2.5 [2] and Qwen3.5 [38] yields substantial improvements over their untuned base models. | p. 7 (5.2. Evaluation) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. Cross-benchmark Ablation. SpatialStack achieves the best cross-task transfer ability, obtaining the highest scores on VSI-Bench, SPAR-Bench, CV-Bench, and the overall aver- age, ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 5.1. Training - extractive body cue:** VLM-3R reformulates spatial question-answer pairs in a VSI-Bench-style format, producing diverse reasoning tasks such as relative direction, object counting, and absolute distance estimation from real-world ...
- **p. 7 / 5.2. Evaluation - extractive body cue:** These benchmarks cover a wide range of tasks, such as depth and distance estimation, object-relation reasoning, and videobased spatial understanding.
- **p. 6 / 5. Experiments - extractive body cue:** We describe our training setup in Sec.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. SpatialStack: Layered Geometry-Language Fusion. Conventional VLMs (a) fuse only a single deep geometry feature with vision tokens, which limits both fine-grained spatial understanding ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Architecture of SpatialStack. A standard VLM backbone is coupled with a multi-view geometry encoder whose layer-wise features are processed by layer-specific projectors and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Examples of spatial tasks at different levels. The left example (Low-Level Task) targets fine-grained geometric percep- tion, such as determining which of two ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Effect of Geometry Injection Layers on Spatial Tasks. Deeper layers improve high-level tasks, while low-level tasks peak at layer 11 and decline at ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Ablation Results on Geometry Token Fusion Depth. Simply fusing multi-layer geometry features to the visual features yields suboptimal performance, while selecting an appropriate ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Cross-benchmark Ablation. SpatialStack achieves the best cross-task transfer ability, obtaining the highest scores on VSI-Bench, SPAR-Bench, CV-Bench, and the overall aver- age, while ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Evaluation on VSI-Bench. Dark orange cells denote the best open-source result in each column, while light orange cells denote the second-best open-source result. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Comparison on CV-Bench. Built on Qwen2.5, SpatialStack-4B outperforms its base model alongside VG-LLM and Cambrian-S. Scaling to Qwen3.5, SpatialStack-5B further im- proves upon ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | VLM-3R reformulates spatial question-answer pairs in a VSI-Bench-style format, producing diverse reasoning tasks such as relative direction, object counting, and absolute distance estimation from ... | embodiment, simulator version and control stack | p. 7 (5.1. Training), p. 7 (5.2. Evaluation) |
| Task/environment | These benchmarks cover a wide range of tasks, such as depth and distance estimation, object-relation reasoning, and videobased spatial understanding. | reset, timeout, object/scene variation | p. 7 (5.2. Evaluation), p. 6 (5. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Following the official protocol, we report mean MCA accuracy and Mean Relative Accuracy for NA across confidence thresholds C = 0.5, 0.55, . . ... | definition/direction/unit from same section | p. 7 (5.2. Evaluation) |
| Table 2. Cross-benchmark Ablation. SpatialStack achieves the best cross-task transfer ability, obtaining the highest scores on VSI-Bench, SPAR-Bench, CV-Bench, and the overall aver- age, ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| We fine-tune the model using the standard language modeling cross-entropy loss. | definition/direction/unit from same section | p. 7 (5.1. Training) |
| Table 7. Geometry-Language Fusion Order Ablation. Com- parison of our progressive hierarchical alignment against a reverse fusion strategy and baseline models. deep features. Tab. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 1. SpatialStack: Layered Geometry-Language Fusion. Conventional VLMs (a) fuse only a single deep geometry feature with vision tokens, which limits both fine-grained spatial ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 3. Examples of spatial tasks at different levels. The left example (Low-Level Task) targets fine-grained geometric percep- tion, such as determining which of ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 1. Ablation Results on Geometry Token Fusion Depth. Simply fusing multi-layer geometry features to the visual features yields suboptimal performance, while selecting an ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 4. Effect of Geometry Injection Layers on Spatial Tasks. Deeper layers improve high-level tasks, while low-level tasks peak at layer 11 and decline ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 4. Comparison on CV-Bench. Built on Qwen2.5, SpatialStack-4B outperforms its base model alongside VG-LLM and Cambrian-S. Scaling to Qwen3.5, SpatialStack-5B further im- proves ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Furthermore, under a fair comparison using the identical Qwen2.5 base model, SpatialStack significantly outperforms other concurrent geometry-aware MLLMs, such as Spatial-MLLM [45], VG-LLM [53], ... | comparison identity and matched condition | p. 7 (5.2. Evaluation) |
| 5.1, evaluate VLMSpatialStack against state-of-the-art methods in Sec. | comparison identity and matched condition | p. 6 (5. Experiments) |
| Ultimately, our latest SpatialStack-5B (based on Qwen3.5) establishes a new state-of-the-art among all evaluated open-source models. | comparison identity and matched condition | p. 7 (5.2. Evaluation) |
| Table 2. Cross-benchmark Ablation. SpatialStack achieves the best cross-task transfer ability, obtaining the highest scores on VSI-Bench, SPAR-Bench, CV-Bench, and the overall aver- age, ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 7. Geometry-Language Fusion Order Ablation. Com- parison of our progressive hierarchical alignment against a reverse fusion strategy and baseline models. deep features. Tab. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 5.2, and provide extensive ablation studies in Sec. | component/input/data sensitivity | p. 6 (5. Experiments) |
| Figure 4. Effect of Geometry Injection Layers on Spatial Tasks. Deeper layers improve high-level tasks, while low-level tasks peak at layer 11 and decline ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Table 1. Ablation Results on Geometry Token Fusion Depth. Simply fusing multi-layer geometry features to the visual features yields suboptimal performance, while selecting an ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Table 2. Cross-benchmark Ablation. SpatialStack achieves the best cross-task transfer ability, obtaining the highest scores on VSI-Bench, SPAR-Bench, CV-Bench, and the overall aver- age, ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 6. Layer Selection Ablation. Performance comparison of extracting geometry features from different deep VGGT lay- ers (L21, L22, L23) and their multi-layer combinations. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 7. Geometry-Language Fusion Order Ablation. Com- parison of our progressive hierarchical alignment against a reverse fusion strategy and baseline models. deep features. Tab. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We summarize our contributions as follows: • We present the first systematic analysis of how fusion layers across vision encoders, geometry encoders, and LLM ... | Furthermore, under a fair comparison using the identical Qwen2.5 base model, SpatialStack significantly outperforms other concurrent geometry-aware MLLMs, such as Spatial-MLLM [45], VG-LLM [53], ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Evaluation), p. 5 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (5.2. Evaluation), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | Figure 4. Effect of Geometry Injection Layers on Spatial Tasks. Deeper layers improve high-level tasks, while low-level tasks peak at layer 11 and decline ... | numeric claim only at cited anchor | p. 5 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We introduced SpatialStack, a hierarchical fusion framework bridging the gap between vision, geometry, and language for robust 3D spatial reasoning. | p. 8 (6. Conclusion) |
| body limitation/failure cue | Notably, despite lacking route-planning data during training, it still surpasses all open-source systems on this task, demonstrating robust zero-shot generalization for highlevel spatial reasoning. | p. 7 (5.2. Evaluation) |
| body limitation/failure cue | Table 5. General Capabilities Evaluation. Our SpatialStack-5B maintains robust general multimodal and spatial-temporal reason- ing capabilities, demonstrating no catastrophic forgetting. Evaluation on CV-Bench. To ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training is performed with a batch size of 64 and a learning rate of 1 × 10-5, optimized using the AdamW optimizer with a ... | p. 7 (5.1. Training) |
| During instruction tuning, the geometry encoder (VGGT) and the vision encoder are kept frozen, while the geometry token merger modules and the LLM decoder ... | p. 7 (5.1. Training) |
| (%) Proprietary Models (API) GPT-4o [14] 74.8 83.0 78.9 Open-source Models Mini-Gemini-HD-34B [22] 71.5 79.2 75.4 LLaVA-NeXT-34B [19] 73.0 74.8 73.9 Cambrian-1-34B [40] 74.0 ... | p. 8 (Model) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive body cue:** We introduced SpatialStack, a hierarchical fusion framework bridging the gap between vision, geometry, and language for robust 3D spatial reasoning.
- **p. 7 / 5.2. Evaluation - extractive body cue:** Notably, despite lacking route-planning data during training, it still surpasses all open-source systems on this task, demonstrating robust zero-shot generalization for highlevel spatial reasoning.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. General Capabilities Evaluation. Our SpatialStack-5B maintains robust general multimodal and spatial-temporal reason- ing capabilities, demonstrating no catastrophic forgetting. Evaluation on CV-Bench. To assess ...

- **Evidence anchors reviewed:** datasets p. 7 (5.1. Training), p. 7 (5.2. Evaluation), p. 6 (5. Experiments), metrics p. 7 (5.2. Evaluation), p. 6 (Figure/Table caption), p. 7 (5.1. Training), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 8 (Figure/Table caption), p. 7 (5.2. Evaluation), p. 6 (5. Experiments), p. 7 (5.2. Evaluation), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 7 (5.2. Evaluation), p. 5 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (5.2. Evaluation), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
