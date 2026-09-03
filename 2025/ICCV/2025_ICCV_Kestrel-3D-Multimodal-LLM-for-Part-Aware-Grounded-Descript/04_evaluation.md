# Evaluation - Kestrel: 3D Multimodal LLM for Part-Aware Grounded Description

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Ahmed_Kestrel_3D_Multimodal_LLM_for_Part-Aware_Grounded_Description_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Ahmed_Kestrel_3D_Multimodal_LLM_for_Part-Aware_Grounded_Description_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (5. Experiments), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption)): 5.2 investigates the performance of Kestrel in single-part grounding from both direct segmentation (3DCoMPaT-GrIn and PartNetMobility [63]) and reasoning segmentation perspectives (3DCoMPaT-GrIn and RPSeg3D [26]).

## Evaluation Body Digest

- **p. 5 / 5. Experiments - extractive body cue:** 5.4, we showcase the robustness and potential applications of Kestrel when the point cloud distribution deviates from the training data, including scenarios where the point ...
- **p. 5 / 5. Experiments - extractive body cue:** 5.1, part-aware point grounded description evaluates the ability of Kestrel for comprehensive 3D object interpretation in terms of both language understanding and segmentation grounding.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. 3D Composition-Aware Language Comprehension (3D-CALC). Part, material, and composition understanding eval- uated based on accuracy on 3DCoMPaT-GrIn. ing. We pretrain Kestrel on PointLLM's ...
- **p. 5 / 5. Experiments - extractive body cue:** We conduct ablation experiments on our training strategy and Kestrel to explore the effects of design choices, as detailed in Sec.
- **p. 5 / 5. Experiments - extractive body cue:** 5.2 investigates the performance of Kestrel in single-part grounding from both direct segmentation (3DCoMPaT-GrIn and PartNetMobility [63]) and reasoning segmentation perspectives (3DCoMPaT-GrIn and RPSeg3D [26]).
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Out-of-Domain Generalization. Kestrel demonstrates robustness when there is a domain shift from 3DCoMPaT-GrIn to Objaverse, as well as the input distribution offsets from ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Part-Aware Point Grounded Description. Given an input point cloud, the model is tasked with predicting a grounded description - text that provides a ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Kestrel: A Part-Aware Point Grounding MLLM. The Kestrel model incorporates a point encoder and an LLM to construct a 3D MLLM, designed to ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 5.2 investigates the performance of Kestrel in single-part grounding from both direct segmentation (3DCoMPaT-GrIn and PartNetMobility [63]) and reasoning segmentation perspectives (3DCoMPaT-GrIn and RPSeg3D ... | p. 5 (5. Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3. Qualitative results of Kestrel on Part-Aware Point Grounded Description, Reasoning and Direct Segmentation. The results show that Kestrel is capable of detailed ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. Results marked with ! indicate metrics for the ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. 3D Composition-Aware Language Comprehension (3D-CALC). Part, material, and composition understanding eval- uated based on accuracy on 3DCoMPaT-GrIn. ing. We pretrain Kestrel on ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3. Single-Part Grounding Results. Evaluates model per- formance on implicit grounding and grounded reasoning tasks. | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 5. Experiments - extractive body cue:** 5.4, we showcase the robustness and potential applications of Kestrel when the point cloud distribution deviates from the training data, including scenarios where the point ...
- **p. 5 / 5. Experiments - extractive body cue:** 5.1, part-aware point grounded description evaluates the ability of Kestrel for comprehensive 3D object interpretation in terms of both language understanding and segmentation grounding.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Part-Aware Point Grounded Description. Given an input point cloud, the model is tasked with predicting a grounded description - text that provides a ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Kestrel: A Part-Aware Point Grounding MLLM. The Kestrel model incorporates a point encoder and an LLM to construct a 3D MLLM, designed to ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results of Kestrel on Part-Aware Point Grounded Description, Reasoning and Direct Segmentation. The results show that Kestrel is capable of detailed 3D ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. Results marked with ! indicate metrics for the model ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. 3D Composition-Aware Language Comprehension (3D-CALC). Part, material, and composition understanding eval- uated based on accuracy on 3DCoMPaT-GrIn. ing. We pretrain Kestrel on PointLLM's ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Single-Part Grounding Results. Evaluates model per- formance on implicit grounding and grounded reasoning tasks.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Perfomance on RPSeg3D further validate Kestrel's effectiveness, we report its perfor- mance on PartNet-Mobility [63]. The results in Appendix C demonstrate that Kestrel ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Out-of-Domain Generalization. Kestrel demonstrates robustness when there is a domain shift from 3DCoMPaT-GrIn to Objaverse, as well as the input distribution offsets from ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 5.4, we showcase the robustness and potential applications of Kestrel when the point cloud distribution deviates from the training data, including scenarios where the ... | embodiment, simulator version and control stack | p. 5 (5. Experiments), p. 5 (5. Experiments) |
| Task/environment | 5.1, part-aware point grounded description evaluates the ability of Kestrel for comprehensive 3D object interpretation in terms of both language understanding and segmentation grounding. | reset, timeout, object/scene variation | p. 5 (5. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (4.1. Kestrel), p. 4 (4. Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2. 3D Composition-Aware Language Comprehension (3D-CALC). Part, material, and composition understanding eval- uated based on accuracy on 3DCoMPaT-GrIn. ing. We pretrain Kestrel on ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| We conduct ablation experiments on our training strategy and Kestrel to explore the effects of design choices, as detailed in Sec. | definition/direction/unit from same section | p. 5 (5. Experiments) |
| 5.2 investigates the performance of Kestrel in single-part grounding from both direct segmentation (3DCoMPaT-GrIn and PartNetMobility [63]) and reasoning segmentation perspectives (3DCoMPaT-GrIn and RPSeg3D ... | definition/direction/unit from same section | p. 5 (5. Experiments) |
| Figure 4. Out-of-Domain Generalization. Kestrel demonstrates robustness when there is a domain shift from 3DCoMPaT-GrIn to Objaverse, as well as the input distribution offsets ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 1. Part-Aware Point Grounded Description. Given an input point cloud, the model is tasked with predicting a grounded description - text that provides ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Kestrel: A Part-Aware Point Grounding MLLM. The Kestrel model incorporates a point encoder and an LLM to construct a 3D MLLM, designed ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 4. Perfomance on RPSeg3D further validate Kestrel's effectiveness, we report its perfor- mance on PartNet-Mobility [63]. The results in Appendix C demonstrate that ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 5. Real-Word Demos. Kestrel shows a certain degree of robustness to noisy and incomplete real-world inputs. # Refinement Levels Grounded Desc. Direct Segmentation ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We conduct ablation experiments on our training strategy and Kestrel to explore the effects of design choices, as detailed in Sec. | comparison identity and matched condition | p. 5 (5. Experiments) |
| Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. Results marked with ! indicate metrics for the ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 2. 3D Composition-Aware Language Comprehension (3D-CALC). Part, material, and composition understanding eval- uated based on accuracy on 3DCoMPaT-GrIn. ing. We pretrain Kestrel on ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 5. Ablation on the query refinement levels. Evaluates the effect of changing the number of query refinement stages on the mIoU performance of ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 5. Ablation on the query refinement levels. Evaluates the effect of changing the number of query refinement stages on the mIoU performance of ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We conduct ablation experiments on our training strategy and Kestrel to explore the effects of design choices, as detailed in Sec. | component/input/data sensitivity | p. 5 (5. Experiments) |
| Table 2. 3D Composition-Aware Language Comprehension (3D-CALC). Part, material, and composition understanding eval- uated based on accuracy on 3DCoMPaT-GrIn. ing. We pretrain Kestrel on ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • We introduce Part-Aware Point Grounded Description (PaPGD), a novel task that challenges 3D MLLMs to achieve ... | 5.2 investigates the performance of Kestrel in single-part grounding from both direct segmentation (3DCoMPaT-GrIn and PartNetMobility [63]) and reasoning segmentation perspectives (3DCoMPaT-GrIn and RPSeg3D ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (5. Experiments), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | Figure 3. Qualitative results of Kestrel on Part-Aware Point Grounded Description, Reasoning and Direct Segmentation. The results show that Kestrel is capable of detailed ... | numeric claim only at cited anchor | p. 5 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / Model - extractive body cue:** The training is done on 4 A100 GPUs for 5 epochs for all experiments with a batch size of 16.
- **p. 6 / 5.1. Part-Aware Point Grounded Description - extractive body cue:** We fine-tune Kestrel on the proposed 3DCoMPaT-GrIn for 5 epochs, using approximately 111K point cloud grounded description pairs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. Results marked with ! indicate metrics for the ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Our work establishes a robust benchmark for part-aware 3D vision-language understanding, paving the way for future research in finegrained 3D object interaction and grounding. | p. 8 (6. Conclusion) |
| body limitation/failure cue | 5.4, we showcase the robustness and potential applications of Kestrel when the point cloud distribution deviates from the training data, including scenarios where the ... | p. 5 (5. Experiments) |
| body limitation/failure cue | Figure 5. Real-Word Demos. Kestrel shows a certain degree of robustness to noisy and incomplete real-world inputs. # Refinement Levels Grounded Desc. Direct Segmentation ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The training is done on 4 A100 GPUs for 5 epochs for all experiments with a batch size of 16. | p. 6 (Model) |
| We use Vicuna 7B checkpoint as our LLM along with Uni3d-g[67] for point cloud encod8977 | p. 5 (5. Experiments) |
| Models marked with * denote our implementations due to unavailable original code. | p. 6 (Model) |
| [SEG] [SEG] Point Encoder ℰ Projector "! | p. 4 (4. Method) |
| The point feature propagation module (PFPM) encodes multi-level point features fp. | p. 4 (4. Method) |
| Each score is computed as an average of 5 evaluations with GPT-4o to account for the variations in the score response. | p. 7 (5.1. Part-Aware Point Grounded Description) |
| We evaluate Kestrel's ability to generalize to new domains by testing it on Objaverse using a checkpoint trained only on 3DCoMPaT-GrIn. | p. 7 (5.4. Application) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. Results marked with ! indicate metrics for the model ...
- **p. 8 / 6. Conclusion - extractive body cue:** Our work establishes a robust benchmark for part-aware 3D vision-language understanding, paving the way for future research in finegrained 3D object interaction and grounding.
- **p. 5 / 5. Experiments - extractive body cue:** 5.4, we showcase the robustness and potential applications of Kestrel when the point cloud distribution deviates from the training data, including scenarios where the point ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Real-Word Demos. Kestrel shows a certain degree of robustness to noisy and incomplete real-world inputs. # Refinement Levels Grounded Desc. Direct Segmentation Reasoning ...

- **Evidence anchors reviewed:** datasets p. 5 (5. Experiments), p. 5 (5. Experiments), metrics p. 6 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 5 (5. Experiments), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 5 (5. Experiments), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
