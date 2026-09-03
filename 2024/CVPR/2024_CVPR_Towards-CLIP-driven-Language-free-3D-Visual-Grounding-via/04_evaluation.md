# Evaluation - Towards CLIP-driven Language-free 3D Visual Grounding via 2D-3D Relational Enhancement and Consistency

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Towards_CLIP-driven_Language-free_3D_Visual_Grounding_via_2D-3D_Relational_Enhancement_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_Towards_CLIP-driven_Language-free_3D_Visual_Grounding_via_2D-3D_Relational_Enhancement_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 6 (4.3. Compared Methods), p. 7 (4.3. Compared Methods), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption)): Table 1. Quantitative comparison of language-free (LF) 3DVG on ScanRefer [4] dataset. Results of relevant fully supervised (Fully) meth- ods are also provided. Accuracy (Acc) under 0.25 and 0.5 IoU ...

## Evaluation Body Digest

- **p. 5 / 4.1. Datasets - extractive body cue:** We follow the ScanRefer benchmark to divide our dataset into the train/val/test set with 36,655, 9,508, and 5,410 samples respectively, and utilize val set to ...
- **p. 5 / 4.1. Datasets - extractive body cue:** This dataset comprises 51,583 manually crafted descriptions for 11,046 objects across 800 scenes from the ScanNet [8].
- **p. 6 / 4.3. Compared Methods - extractive body cue:** Given its ability to perform 3DVG without text-based training, akin to our proposed paradigm, OpenScene serves as a benchmark for comparison.
- **p. 6 / 4.2. Implementation Details - extractive body cue:** Quantitative comparison of language-free (LF) 3DVG on ScanRefer [4] dataset.
- **p. 7 / 4.3. Compared Methods - extractive body cue:** Given its independence from textual training data, LLM-Grounder is utilized as a comparative benchmark to our method.
- **p. 7 / 4.3. Compared Methods - extractive body cue:** [18], to locate objects within a 3D scene.
- **p. 6 / 4.2. Implementation Details - extractive body cue:** Accuracy (Acc) under 0.25 and 0.5 IoU thresholds in "Unique", "Multiple", and "Overall" is reported respectively.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparison of language-free 3DVG on Nr3D and Sr3D [1] datasets. We report accuracy (Acc) for the IoU@m (m ∈{0.25, 0.5}) metrics in ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Datasets (p. 5); 4.2. Implementation Details (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1. Quantitative comparison of language-free (LF) 3DVG on ScanRefer [4] dataset. Results of relevant fully supervised (Fully) meth- ods are also provided. Accuracy ... | p. 6 (Figure/Table caption) |
| 4.3. Compared Methods | SYSTEM / EVALUATION SCOPE UNRESOLVED | Pseudo-Q [16] is currently a method that has achieved good performance in 2D language-free grounding. | p. 6 (4.3. Compared Methods) |
| 4.3. Compared Methods | SYSTEM / EVALUATION SCOPE UNRESOLVED | Qualitative results from Pseudo-Q [16], Zero-shot-RIS [40] and our method. | p. 7 (4.3. Compared Methods) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 4. Comparison on different 3D visual grounding baseline methods. We only report the "overall" results. | p. 8 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 3. Ablation study on main components of our method. We report the "overall" results in terms of Acc@0.25 and Acc@0.5. PFG Relation Acc@0.25 ... | p. 8 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Datasets - extractive body cue:** We follow the ScanRefer benchmark to divide our dataset into the train/val/test set with 36,655, 9,508, and 5,410 samples respectively, and utilize val set to ...
- **p. 5 / 4.1. Datasets - extractive body cue:** This dataset comprises 51,583 manually crafted descriptions for 11,046 objects across 800 scenes from the ScanNet [8].
- **p. 6 / 4.3. Compared Methods - extractive body cue:** Given its ability to perform 3DVG without text-based training, akin to our proposed paradigm, OpenScene serves as a benchmark for comparison.
- **p. 6 / 4.2. Implementation Details - extractive body cue:** Quantitative comparison of language-free (LF) 3DVG on ScanRefer [4] dataset.
- **p. 7 / 4.3. Compared Methods - extractive body cue:** Given its independence from textual training data, LLM-Grounder is utilized as a comparative benchmark to our method.
- **p. 7 / 4.3. Compared Methods - extractive body cue:** [18], to locate objects within a 3D scene.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (a) Comparison of fully-supervised and our language- free training paradigm. (b) Based on CLIP embedding space, our language-free training method uses multi-view images ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The overview of our method. During training, we first encode 3D point cloud and multi-view images with point cloud encoder and CLIP visual ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparison of language-free (LF) 3DVG on ScanRefer [4] dataset. Results of relevant fully supervised (Fully) meth- ods are also provided. Accuracy (Acc) ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparison of language-free 3DVG on Nr3D and Sr3D [1] datasets. We report accuracy (Acc) for the IoU@m (m ∈{0.25, 0.5}) metrics in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results from Pseudo-Q [16], Zero-shot-RIS [40] and our method. The GT boxes are marked in green. Boxes predicted by Pseudo-Q, Zero-shot-RIS, and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation study on main components of our method. We report the "overall" results in terms of Acc@0.25 and Acc@0.5. PFG Relation Acc@0.25 Acc@0.5 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Comparison on different 3D visual grounding baseline methods. We only report the "overall" results.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Ablation study on different numbers (k) of neighboring objects in the NRM module. Here A refers to Acc. k Unique Multiple Overall A@0.25 ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We follow the ScanRefer benchmark to divide our dataset into the train/val/test set with 36,655, 9,508, and 5,410 samples respectively, and utilize val set ... | embodiment, simulator version and control stack | p. 5 (4.1. Datasets), p. 5 (4.1. Datasets) |
| Task/environment | This dataset comprises 51,583 manually crafted descriptions for 11,046 objects across 800 scenes from the ScanNet [8]. | reset, timeout, object/scene variation | p. 5 (4.1. Datasets), p. 6 (4.3. Compared Methods) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Overview), p. 3 (3.1. Overview) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3.4. Training and Inference), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Accuracy (Acc) under 0.25 and 0.5 IoU thresholds in "Unique", "Multiple", and "Overall" is reported respectively. | definition/direction/unit from same section | p. 6 (4.2. Implementation Details) |
| Table 2. Quantitative comparison of language-free 3DVG on Nr3D and Sr3D [1] datasets. We report accuracy (Acc) for the IoU@m (m ∈{0.25, 0.5}) metrics ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| The learning rates for proposed Neighboring Relation-aware Modeling and Cross-modality Relation Consistency are empirically set at 2e-3. | definition/direction/unit from same section | p. 5 (4.2. Implementation Details) |
| For the voting & grouping module, detection head, and cross-modal fusion module, the learning rates are set as 2e-3, 1e-4, and 5e-4, respectively, following ... | definition/direction/unit from same section | p. 5 (4.2. Implementation Details) |
| Figure 2. The overview of our method. During training, we first encode 3D point cloud and multi-view images with point cloud encoder and CLIP ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Without language supervision, our method significantly outperforms previous methods. † indicates our re-implemented method on 3D. | comparison identity and matched condition | p. 6 (4.2. Implementation Details) |
| During the training stage, we initially train our baseline model on the ScanNet [8] dataset for 200 epochs, followed by a further 50 epochs ... | comparison identity and matched condition | p. 5 (4.2. Implementation Details) |
| Due to its capability to capture both the target object's attributes and its environmental context, we adapt this method to 3D as a baseline ... | comparison identity and matched condition | p. 7 (4.3. Compared Methods) |
| Table 4. Comparison on different 3D visual grounding baseline methods. We only report the "overall" results. | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Given its ability to perform 3DVG without text-based training, akin to our proposed paradigm, OpenScene serves as a benchmark for comparison. | comparison identity and matched condition | p. 6 (4.3. Compared Methods) |
| We show quantitative comparisons of our 3DLFVG and aforementioned methods on ScanRefer [4] and Nr3D/Sr3D [1] in Tab. | comparison identity and matched condition | p. 7 (4.4. Quantitative Comparison) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Without language supervision, our method significantly outperforms previous methods. † indicates our re-implemented method on 3D. | component/input/data sensitivity | p. 6 (4.2. Implementation Details) |
| Given its ability to perform 3DVG without text-based training, akin to our proposed paradigm, OpenScene serves as a benchmark for comparison. | component/input/data sensitivity | p. 6 (4.3. Compared Methods) |
| Table 3. Ablation study on main components of our method. We report the "overall" results in terms of Acc@0.25 and Acc@0.5. PFG Relation Acc@0.25 ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 5. Ablation study on different numbers (k) of neighboring objects in the NRM module. Here A refers to Acc. k Unique Multiple Overall ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Overall, our contributions can be summarized as follows: • We introduce a CLIP-driven language-free 3DVG framework, which requires no manually annotated texts to effectively ... | Table 1. Quantitative comparison of language-free (LF) 3DVG on ScanRefer [4] dataset. Results of relevant fully supervised (Fully) meth- ods are also provided. Accuracy ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 6 (4.3. Compared Methods), p. 7 (4.3. Compared Methods), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | Pseudo-Q [16] is currently a method that has achieved good performance in 2D language-free grounding. | numeric claim only at cited anchor | p. 6 (4.3. Compared Methods) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Datasets - extractive body cue:** This dataset comprises 51,583 manually crafted descriptions for 11,046 objects across 800 scenes from the ScanNet [8].
- **p. 5 / 4.1. Datasets - extractive body cue:** On average, each scene features approximately 13.81 objects, each accompanied by 64.48 annotations.
- **p. 5 / 4.1. Datasets - extractive body cue:** We follow the ScanRefer benchmark to divide our dataset into the train/val/test set with 36,655, 9,508, and 5,410 samples respectively, and utilize val set to ...
- **p. 5 / 4.1. Datasets - extractive body cue:** Specifically, Nr3D is composed of 41,503 samples obtained through ReferItGame, while Sr3D encompasses 83,572 samples created using synthetic templates.
- **p. 5 / 4.2. Implementation Details - extractive body cue:** During the training stage, we initially train our baseline model on the ScanNet [8] dataset for 200 epochs, followed by a further 50 epochs to ...
- **p. 5 / 3.3. Relation Injection - extractive body cue:** The relational features of the 3D proposal corresponding to the target object indicated by a 2D mask should align with the 2D mask's relational features: ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Extensive experiments conducted on mainstream datasets demonstrate the robustness and efficiency of our approach. | p. 8 (5. Conclusion) |
| body limitation/failure cue | It does not have a red chair near it. | p. 7 (4.3. Compared Methods) |
| body limitation/failure cue | Table 3. Ablation study on main components of our method. We report the "overall" results in terms of Acc@0.25 and Acc@0.5. PFG Relation Acc@0.25 ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The model is trained with the AdamW [24] optimizer and a batch size of 8. | p. 5 (4.2. Implementation Details) |
| The learning rates for proposed Neighboring Relation-aware Modeling and Cross-modality Relation Consistency are empirically set at 2e-3. | p. 5 (4.2. Implementation Details) |
| Overall m=0.25 m=0.5 m=0.25 m=0.5 m=0.25 m=0.5 m=0.25 m=0.5 m=0.25 m=0.5 Nr3D Random 6.70 2.40 6.34 2.75 6.59 2.91 6.47 2.41 6.51 2.59 Pseudo-Q† ... | p. 6 (4.2. Implementation Details) |
| (d) This is a brown table with three computer monitors on it. | p. 7 (4.3. Compared Methods) |
| This approach employs CLIP to encode local-global context features for images and text descriptions respectively. | p. 7 (4.3. Compared Methods) |
| By comparing these with the 2D mask relations, relation matching scores can be computed. | p. 4 (3.1. Overview) |
| So, it ensures an efficient implementation of 3DVG given the texts during the inference phase. | p. 4 (3.1. Overview) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** Extensive experiments conducted on mainstream datasets demonstrate the robustness and efficiency of our approach.
- **p. 7 / 4.3. Compared Methods - extractive body cue:** It does not have a red chair near it.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation study on main components of our method. We report the "overall" results in terms of Acc@0.25 and Acc@0.5. PFG Relation Acc@0.25 Acc@0.5 ...

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Datasets), p. 5 (4.1. Datasets), p. 6 (4.3. Compared Methods), p. 6 (4.2. Implementation Details), p. 7 (4.3. Compared Methods), p. 7 (4.3. Compared Methods), metrics p. 6 (4.2. Implementation Details), p. 6 (Figure/Table caption), p. 5 (4.2. Implementation Details), p. 5 (4.2. Implementation Details), p. 3 (Figure/Table caption), baselines p. 6 (4.2. Implementation Details), p. 5 (4.2. Implementation Details), p. 7 (4.3. Compared Methods), p. 8 (Figure/Table caption), p. 6 (4.3. Compared Methods), p. 7 (4.4. Quantitative Comparison), results p. 6 (Figure/Table caption), p. 6 (4.3. Compared Methods), p. 7 (4.3. Compared Methods), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
