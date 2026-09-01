# Evaluation - Geometry-Aware Cross-Modal Graph Alignment for Referring Segmentation in 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Tao_Geometry-Aware_Cross-Modal_Graph_Alignment_for_Referring_Segmentation_in_3D_Gaussian_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Tao_Geometry-Aware_Cross-Modal_Graph_Alignment_for_Referring_Segmentation_in_3D_Gaussian_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (6.2. Comparisons with State-of-the-Arts), p. 7 (6.2. Comparisons with State-of-the-Arts), p. 8 (6.3. Ablation Study), p. 8 (6.3. Ablation Study), p. 6 (Figure/Table caption), p. 6 (6. Experiments)): 3), where scenes are relatively clean and objects are easier to localize, GeoCGA still achieves the best performance across all categories and improves the overall average by +1.0%.

## Evaluation Body Digest

- **p. 7 / 6.2. Comparisons with State-of-the-Arts - extractive PDF cue:** 3), where scenes are relatively clean and objects are easier to localize, GeoCGA still achieves the best performance across all categories and improves the overall ...
- **p. 8 / 6.3. Ablation Study - extractive PDF cue:** (11)) provides additional gains ( +1.2 and +0.9 ) compared with pseudo-mask supervision, as it introduces clearer objectlevel constraints and stabilizes training in cluttered scenes.
- **p. 6 / 6. Experiments - extractive PDF cue:** We evaluate GeoCGA across multiple benchmarks and provide detailed analyses of its performance.
- **p. 6 / 6.1. Experimental Setting - extractive PDF cue:** LERF-OVS extends the 3D Gaussian Splatting framework to open-vocabulary segmentation across multiple scenes.
- **p. 7 / 6.1. Experimental Setting - extractive PDF cue:** Comparison results on the 3D-OVS dataset.
- **p. 8 / 6.4. Visualizations - extractive PDF cue:** (a) Input scene with different objects.
- **p. 6 / 6.1. Experimental Setting - extractive PDF cue:** Following the setting of ReferSplat [13], we employ the official data partitions and generate pseudo masks using the confidenceweighted IoU strategy.
- **p. 7 / 6.1. Experimental Setting - extractive PDF cue:** Given a query-view pair, the Intersection-over-Union between the predicted mask ˆY and the ground-truth mask Y is formulated as IoU(Y, ˆY ) = /Y ∩ˆY ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 6. Experiments (p. 6); 6.1. Experimental Setting (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 6.2. Comparisons with State-of-the-Arts | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3), where scenes are relatively clean and objects are easier to localize, GeoCGA still achieves the best performance across all categories and improves the ... | p. 7 (6.2. Comparisons with State-of-the-Arts) |
| 6.2. Comparisons with State-of-the-Arts | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2), GeoCGA continues to outperform prior methods with an average improvement of +5.7%. | p. 7 (6.2. Comparisons with State-of-the-Arts) |
| 6.3. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | (10)) further improves grounding accuracy ( +1.0 and +0.6 ) over relationimplicit matching, showing that aligning linguistic and geometric relations is essential for reliable ... | p. 8 (6.3. Ablation Study) |
| 6.3. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | First, incorporating edge-aware message passing improves performance over the Semantic GNN baseline ( +0.6 on Ramen and +1.2 on Kitchen ), indicating that explicitly ... | p. 8 (6.3. Ablation Study) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 1. Comparison on the Ref-LERF dataset with state-of-the- art methods in terms of mIoU (↑). Higher values are better. Bold values denote the ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 6.2. Comparisons with State-of-the-Arts - extractive PDF cue:** 3), where scenes are relatively clean and objects are easier to localize, GeoCGA still achieves the best performance across all categories and improves the overall ...
- **p. 8 / 6.3. Ablation Study - extractive PDF cue:** (11)) provides additional gains ( +1.2 and +0.9 ) compared with pseudo-mask supervision, as it introduces clearer objectlevel constraints and stabilizes training in cluttered scenes.
- **p. 6 / 6. Experiments - extractive PDF cue:** We evaluate GeoCGA across multiple benchmarks and provide detailed analyses of its performance.
- **p. 6 / 6.1. Experimental Setting - extractive PDF cue:** LERF-OVS extends the 3D Gaussian Splatting framework to open-vocabulary segmentation across multiple scenes.
- **p. 7 / 6.1. Experimental Setting - extractive PDF cue:** Comparison results on the 3D-OVS dataset.
- **p. 8 / 6.4. Visualizations - extractive PDF cue:** (a) Input scene with different objects.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Qualitative comparison between ReferSplat [13] and our GeoCGA on the Ramen and Waldo Kitchen scenes. ReferSplat often mislocalizes the target regions due to ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Method comparison. ReferSplat [13] (a) often pro- duces false masks, while ours (b) can accurately predict the mask. the underlying radiance field. GeoCGA ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Spatial awareness deficiency leads to incorrect localiza- tion in ReferSplat [13], while our method correctly grounds the target despite challenging spatial cues. ri ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Spatial reasoning deficiency leads to coarse segmenta- tion in ReferSplat [13], while our method produces precise masks. consistent segmentation under complex spatial cues. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. Overview of GeoCGA. Given a language query and a scene, Geometry-Aware Prompt Expansion (GAPE) constructs a semantic graph from the text, while a ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison on the Ref-LERF dataset with state-of-the- art methods in terms of mIoU (↑). Higher values are better. Bold values denote the best ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison results on the LERF-OVS dataset.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Comparison results on the 3D-OVS dataset.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 3), where scenes are relatively clean and objects are easier to localize, GeoCGA still achieves the best performance across all categories and improves the ... | embodiment, simulator version and control stack | p. 7 (6.2. Comparisons with State-of-the-Arts), p. 8 (6.3. Ablation Study) |
| Task/environment | (11)) provides additional gains ( +1.2 and +0.9 ) compared with pseudo-mask supervision, as it introduces clearer objectlevel constraints and stabilizes training in cluttered ... | reset, timeout, object/scene variation | p. 8 (6.3. Ablation Study), p. 6 (6. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (5.3. 3D Scene Graph Construction (3DSGC)), p. 3 (3. Problem Statement and Notations) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Following the setting of ReferSplat [13], we employ the official data partitions and generate pseudo masks using the confidenceweighted IoU strategy. | definition/direction/unit from same section | p. 6 (6.1. Experimental Setting) |
| Given a query-view pair, the Intersection-over-Union between the predicted mask ˆY and the ground-truth mask Y is formulated as IoU(Y, ˆY ) = /Y ... | definition/direction/unit from same section | p. 7 (6.1. Experimental Setting) |
| Despite being more lightweight, GeoCGA consistently improves accuracy across all three benchmarks, demonstrating that explicit geometry modeling enhances both effectiveness and efficiency. | definition/direction/unit from same section | p. 7 (6.2. Comparisons with State-of-the-Arts) |
| (10)) further improves grounding accuracy ( +1.0 and +0.6 ) over relationimplicit matching, showing that aligning linguistic and geometric relations is essential for reliable ... | definition/direction/unit from same section | p. 8 (6.3. Ablation Study) |
| Figure 6. Case study. The top row shows a successful grounding example. The bottom row illustrates typical failure modes where spatial ambiguity or relational ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We evaluate GeoCGA across multiple benchmarks and provide detailed analyses of its performance. | definition/direction/unit from same section | p. 6 (6. Experiments) |
| Figure 2. Method comparison. ReferSplat [13] (a) often pro- duces false masks, while ours (b) can accurately predict the mask. the underlying radiance field. ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Superscripts indicate absolute improvements over the baseline. | comparison identity and matched condition | p. 7 (6.2. Comparisons with State-of-the-Arts) |
| 2), GeoCGA continues to outperform prior methods with an average improvement of +5.7%. | comparison identity and matched condition | p. 7 (6.2. Comparisons with State-of-the-Arts) |
| (11)) provides additional gains ( +1.2 and +0.9 ) compared with pseudo-mask supervision, as it introduces clearer objectlevel constraints and stabilizes training in cluttered ... | comparison identity and matched condition | p. 8 (6.3. Ablation Study) |
| First, incorporating edge-aware message passing improves performance over the Semantic GNN baseline ( +0.6 on Ramen and +1.2 on Kitchen ), indicating that explicitly ... | comparison identity and matched condition | p. 8 (6.3. Ablation Study) |
| Our evaluation protocol follows LangSplat [33] and LangSplat-V2, using text-based category queries to ensure consistent comparison. | comparison identity and matched condition | p. 6 (6.1. Experimental Setting) |
| Figure 1. Qualitative comparison between ReferSplat [13] and our GeoCGA on the Ramen and Waldo Kitchen scenes. ReferSplat often mislocalizes the target regions due ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Comparative ablation results on Ramen and Kitchen. | component/input/data sensitivity | p. 7 (6.2. Comparisons with State-of-the-Arts) |
| Ablation study on Semantic Graph and Geometry Graph. | component/input/data sensitivity | p. 7 (6.2. Comparisons with State-of-the-Arts) |
| Overall, all components contribute positively, indicating that structured graph reasoning and explicit relation modeling jointly enhance the robustness of GeoCGA. | component/input/data sensitivity | p. 8 (6.3. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are: • We introduce a geometry-aware perspective for language grounding that embeds explicit spatial structure into linguistic features, enabling more accurate reasoning. ... | 3), where scenes are relatively clean and objects are easier to localize, GeoCGA still achieves the best performance across all categories and improves the ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (6.2. Comparisons with State-of-the-Arts), p. 7 (6.2. Comparisons with State-of-the-Arts), p. 8 (6.3. Ablation Study), p. 8 (6.3. Ablation Study), p. 6 (Figure/Table caption), p. 6 (6. Experiments) |
| Primary metric/result | 2), GeoCGA continues to outperform prior methods with an average improvement of +5.7%. | numeric claim only at cited anchor | p. 7 (6.2. Comparisons with State-of-the-Arts) |

- Numeric sentences retained from the body:
- **p. 7 / 6.1. Experimental Setting - extractive PDF cue:** All experiments are conducted on one RTX 5090 GPU using PyTorch.
- **p. 7 / 6.1. Experimental Setting - extractive PDF cue:** We train GeoCGA for 4 epochs per scene with AdamW (learning rate 1 × 10-4, weight decay 1 × 10-2).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The bottom row illustrates typical failure modes where spatial ambiguity or relational confusion leads to incorrect (ReferSplat [13]) or incomplete (Ours) segmentation. mentary perspectives. | p. 8 (6.3. Ablation Study) |
| body limitation/failure cue | Future work may explore end-to-end differentiable object discovery to reduce reliance on pretrained representations, as well as richer geometric priors and more scalable graph ... | p. 8 (7. Conclusion and Discussion) |
| body limitation/failure cue | Figure 4. Spatial reasoning deficiency leads to coarse segmenta- tion in ReferSplat [13], while our method produces precise masks. consistent segmentation under complex spatial ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Ref-LERF emphasizes fine-grained referring understanding within individual scenes that involve intricate spatial layouts and strong occlusions. | p. 6 (6.1. Experimental Setting) |
| body limitation/failure cue | Combining both modules yields the best performance (+3.8 and +10.2), confirming that explicit linguistic structure and geometric topology are complementary and jointly essential for ... | p. 7 (6.3. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train GeoCGA for 4 epochs per scene with AdamW (learning rate 1 × 10-4, weight decay 1 × 10-2). | p. 7 (6.1. Experimental Setting) |
| All experiments are conducted on one RTX 5090 GPU using PyTorch. | p. 7 (6.1. Experimental Setting) |
| The enriched embeddings encode higher-order spatial configurations and geometric context. | p. 5 (5.3. 3D Scene Graph Construction (3DSGC)) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6.3. Ablation Study - extractive PDF cue:** The bottom row illustrates typical failure modes where spatial ambiguity or relational confusion leads to incorrect (ReferSplat [13]) or incomplete (Ours) segmentation. mentary perspectives.
- **p. 8 / 7. Conclusion and Discussion - extractive PDF cue:** Future work may explore end-to-end differentiable object discovery to reduce reliance on pretrained representations, as well as richer geometric priors and more scalable graph matching ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Spatial reasoning deficiency leads to coarse segmenta- tion in ReferSplat [13], while our method produces precise masks. consistent segmentation under complex spatial cues. ...
- **p. 6 / 6.1. Experimental Setting - extractive PDF cue:** Ref-LERF emphasizes fine-grained referring understanding within individual scenes that involve intricate spatial layouts and strong occlusions.
- **p. 7 / 6.3. Ablation Study - extractive PDF cue:** Combining both modules yields the best performance (+3.8 and +10.2), confirming that explicit linguistic structure and geometric topology are complementary and jointly essential for robust ...

- **PDF anchors reviewed:** datasets p. 7 (6.2. Comparisons with State-of-the-Arts), p. 8 (6.3. Ablation Study), p. 6 (6. Experiments), p. 6 (6.1. Experimental Setting), p. 7 (6.1. Experimental Setting), p. 8 (6.4. Visualizations), metrics p. 6 (6.1. Experimental Setting), p. 7 (6.1. Experimental Setting), p. 7 (6.2. Comparisons with State-of-the-Arts), p. 8 (6.3. Ablation Study), p. 8 (Figure/Table caption), p. 6 (6. Experiments), baselines p. 7 (6.2. Comparisons with State-of-the-Arts), p. 7 (6.2. Comparisons with State-of-the-Arts), p. 8 (6.3. Ablation Study), p. 8 (6.3. Ablation Study), p. 6 (6.1. Experimental Setting), p. 1 (Figure/Table caption), results p. 7 (6.2. Comparisons with State-of-the-Arts), p. 7 (6.2. Comparisons with State-of-the-Arts), p. 8 (6.3. Ablation Study), p. 8 (6.3. Ablation Study), p. 6 (Figure/Table caption), p. 6 (6. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
