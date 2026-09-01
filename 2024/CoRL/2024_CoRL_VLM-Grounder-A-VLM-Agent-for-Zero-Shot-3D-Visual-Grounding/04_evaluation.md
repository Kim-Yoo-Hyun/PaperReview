# Evaluation - VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/xu25c.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/xu25c/xu25c.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 8 (3 Methodology), p. 8 (3 Methodology), p. 19 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption)): Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves performance comparable to supervised learning baselines. * indica ...

## Evaluation Body Digest

- **p. 8 / 3 Methodology - extractive PDF cue:** We introduced a novel Visual-Retrieval benchmark to evaluate the impact of stitching operations on VLM's visual understanding.
- **p. 8 / 3 Methodology - extractive PDF cue:** Timeout 1 0 1.00 亡一－－的I；血勹匾96009511 I 400 c、l 0 ."贮E.....""．一．．比＂一·黯勺置星一·屙已』"· U,OO U O3 J ｀斗丘且矗诅U.O~L U 0乙U 0.99 、 I 寸 旨厦"'I'■，配切谭心1戎·""'.rl l 0 啊948 ...
- **p. 19 / Figure/Table caption - extractive PDF cue:** Table 10: Success rates of different modules. Query Analysis View Pre-Selection Image Selection by VLM OV-Detection 100% 96% 77%
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 3. This benchmark allows us to assess the extent of information loss caused by the stitching strategy through retrieval accuracy. We focus primarily on ...
- **p. 8 / 3 Methodology - extractive PDF cue:** Further discussions on limitations, error analysis, inferencing time, and qualitative results are provided in the supplementary material.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Comparison between LLM-based methods and VLM-Grounder. VLM's visual processing. Further, we propose a dynamic stitching strategy that dynamically uses the optimal layouts identified ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: An overview of VLM-Grounder. VLM-Grounder analyzes the user query and dynami- cally stitches image sequences for efficient VLM processing to locate the target ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves performance comparable to ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** B Visual-Retrieval Benchmark Settings (p. 13).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves performance comparable ... | p. 6 (Figure/Table caption) |
| 3 Methodology | SYSTEM / EVALUATION SCOPE UNRESOLVED | As shown in our results, the proposed dynamic stitching outperforms the others, demonstrating its efficacy. | p. 8 (3 Methodology) |
| 3 Methodology | SYSTEM / EVALUATION SCOPE UNRESOLVED | 5 shows a clear performance improvement with each additional component, confirming the importance and effectiveness of these operations. | p. 8 (3 Methodology) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 10: Success rates of different modules. Query Analysis View Pre-Selection Image Selection by VLM OV-Detection 100% 96% 77% | p. 19 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 1: Comparison between LLM-based methods and VLM-Grounder. VLM's visual processing. Further, we propose a dynamic stitching strategy that dynamically uses the optimal layouts ... | p. 2 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 3 Methodology - extractive PDF cue:** We introduced a novel Visual-Retrieval benchmark to evaluate the impact of stitching operations on VLM's visual understanding.
- **p. 8 / 3 Methodology - extractive PDF cue:** Timeout 1 0 1.00 亡一－－的I；血勹匾96009511 I 400 c、l 0 ."贮E.....""．一．．比＂一·黯勺置星一·屙已』"· U,OO U O3 J ｀斗丘且矗诅U.O~L U 0乙U 0.99 、 I 寸 旨厦"'I'■，配切谭心1戎·""'.rl l 0 啊948 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Comparison between LLM-based methods and VLM-Grounder. VLM's visual processing. Further, we propose a dynamic stitching strategy that dynamically uses the optimal layouts identified ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: An overview of VLM-Grounder. VLM-Grounder analyzes the user query and dynami- cally stitches image sequences for efficient VLM processing to locate the target ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves performance comparable to ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: 3D visual grounding results on Nr3D. VLM-Grounder surpasses the previous SOTA zero- shot method without requiring access to point clouds or ground-truth bounding ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: Visual-Retrieval benchmark. We randomly select 1,000 images from the ScanNet dataset, each annotated with a unique ID. Addition- ally, a block of random ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 3. This benchmark allows us to assess the extent of information loss caused by the stitching strategy through retrieval accuracy. We focus primarily on ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Benchmark accuracy and request time for different stitching layouts and image counts.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Stitching strategies. Strategy Acc@0.25 Fix (1, 1) N.A. Fix (8, 2) 48.4 Square

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We introduced a novel Visual-Retrieval benchmark to evaluate the impact of stitching operations on VLM's visual understanding. | embodiment, simulator version and control stack | p. 8 (3 Methodology), p. 8 (3 Methodology) |
| Task/environment | Timeout 1 0 1.00 亡一－－的I；血勹匾96009511 I 400 c、l 0 ."贮E.....""．一．．比＂一·黯勺置星一·屙已』"· U,OO U O3 J ｀斗丘且矗诅U.O~L U 0乙U 0.99 、 I 寸 旨厦"'I'■，配切谭心1戎·""'.rl l 0 ... | reset, timeout, object/scene variation | p. 8 (3 Methodology) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3 Methodology), p. 4 (3 Methodology) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 7 (3 Methodology), p. 7 (3 Methodology) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 10: Success rates of different modules. Query Analysis View Pre-Selection Image Selection by VLM OV-Detection 100% 96% 77% | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Fig. 3. This benchmark allows us to assess the extent of information loss caused by the stitching strategy through retrieval accuracy. We focus primarily ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 4: Benchmark accuracy and request time for different stitching layouts and image counts. | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Further discussions on limitations, error analysis, inferencing time, and qualitative results are provided in the supplementary material. | definition/direction/unit from same section | p. 8 (3 Methodology) |
| Figure 1: Comparison between LLM-based methods and VLM-Grounder. VLM's visual processing. Further, we propose a dynamic stitching strategy that dynamically uses the optimal layouts ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 2: An overview of VLM-Grounder. VLM-Grounder analyzes the user query and dynami- cally stitches image sequences for efficient VLM processing to locate the ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves performance comparable ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 3: Visual-Retrieval benchmark. We randomly select 1,000 images from the ScanNet dataset, each annotated with a unique ID. Addition- ally, a block of ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves performance comparable ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 5: Projection operations. Operations Acc@0.25 Baseline 40.8 +Morpho. Ops 45.2 +Point Filtering | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| As shown in our results, the proposed dynamic stitching outperforms the others, demonstrating its efficacy. | comparison identity and matched condition | p. 8 (3 Methodology) |
| Table 8: Baseline results on the selected 250 samples. Overall Unique Multiple Methods Acc@0.25 Acc@0.5 Acc@0.25 Acc@0.5 Acc@0.25 Acc@0.5 BUTD-DETR[28] 54.0 | comparison identity and matched condition | p. 18 (Figure/Table caption) |
| Table 2: 3D visual grounding results on Nr3D. VLM-Grounder surpasses the previous SOTA zero- shot method without requiring access to point clouds or ground-truth ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 1: Comparison between LLM-based methods and VLM-Grounder. VLM's visual processing. Further, we propose a dynamic stitching strategy that dynamically uses the optimal layouts ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Without stitching, the system often encounters timeouts and fails to complete the task, underscoring the necessity of an effective stitching strategy. | component/input/data sensitivity | p. 8 (3 Methodology) |
| Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves performance comparable ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 2: 3D visual grounding results on Nr3D. VLM-Grounder surpasses the previous SOTA zero- shot method without requiring access to point clouds or ground-truth ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Ops 45.2 +Point Filtering 48.4 +Multi-View 51.6 4.4 Ablation Studies Stitching strategies. | component/input/data sensitivity | p. 8 (3 Methodology) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| While these methods achieve strong performance, they use only objectcentric information and often miss detailed scene context, making it challenging to handle queries like ... | Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves performance comparable ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 8 (3 Methodology), p. 8 (3 Methodology), p. 19 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | As shown in our results, the proposed dynamic stitching outperforms the others, demonstrating its efficacy. | numeric claim only at cited anchor | p. 8 (3 Methodology) |

- Numeric sentences retained from the body:
- **p. 4 / 3 Methodology - extractive PDF cue:** For example, with n = 40 and L = 6, six stitched images using the (4, 1) layout are insufficient, so we use two (4, ...
- **p. 5 / 3 Methodology - extractive PDF cue:** For our experiments, we sample one frame from every 20 frames of the original ScanNet image sequences.
- **p. 5 / 3 Methodology - extractive PDF cue:** The retry limit is M = 3, the image count limit is L = 6, and the ensemble image number is N = 7.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 5: Failure cases of the VLM grounding module. 20 | p. 20 (Figure/Table caption) |
| body limitation/failure cue | Figure 8: A failure case of the projection module. 21 | p. 21 (Figure/Table caption) |
| body limitation/failure cue | Although our multi-view ensemble projection module helps mitigate this issue, it cannot entirely eliminate it. | p. 6 (3 Methodology) |
| body limitation/failure cue | 5 Conclusion and Limitations In this paper, we presented VLM-Grounder, a VLM agent that excels in zero-shot 3D visual grounding. | p. 8 (3 Methodology) |
| body limitation/failure cue | Further discussions on limitations, error analysis, inferencing time, and qualitative results are provided in the supplementary material. | p. 8 (3 Methodology) |
| body limitation/failure cue | VLM-Grounder does not need such priors for input, so we match our predicted box to the ground truth box with the closest center and ... | p. 5 (3 Methodology) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Pseudo-code for the dynamic stitching strategy is provided in the supplementary material. | p. 4 (3 Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 20 / Figure/Table caption - extractive PDF cue:** Figure 5: Failure cases of the VLM grounding module. 20
- **p. 21 / Figure/Table caption - extractive PDF cue:** Figure 8: A failure case of the projection module. 21
- **p. 6 / 3 Methodology - extractive PDF cue:** Although our multi-view ensemble projection module helps mitigate this issue, it cannot entirely eliminate it.
- **p. 8 / 3 Methodology - extractive PDF cue:** 5 Conclusion and Limitations In this paper, we presented VLM-Grounder, a VLM agent that excels in zero-shot 3D visual grounding.
- **p. 8 / 3 Methodology - extractive PDF cue:** Further discussions on limitations, error analysis, inferencing time, and qualitative results are provided in the supplementary material.
- **p. 5 / 3 Methodology - extractive PDF cue:** VLM-Grounder does not need such priors for input, so we match our predicted box to the ground truth box with the closest center and use ...

- **PDF anchors reviewed:** datasets p. 8 (3 Methodology), p. 8 (3 Methodology), metrics p. 19 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (3 Methodology), p. 2 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (3 Methodology), p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), results p. 6 (Figure/Table caption), p. 8 (3 Methodology), p. 8 (3 Methodology), p. 19 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
