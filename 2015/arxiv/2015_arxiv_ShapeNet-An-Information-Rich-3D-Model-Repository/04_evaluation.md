# Evaluation - ShapeNet: An Information-Rich 3D Model Repository

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1512.03012; PDF retrieval source: https://arxiv.org/pdf/1512.03012. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 5 (4. Annotation Acquisition and Validation), p. 6 (4.2. Hierarchical Rigid Alignment), p. 6 (4.1. Category Annotation), p. 7 (4.3. Parts and Keypoints)): Table 3. Total number of models for the top 100 ShapeNetSem categories (out of 270 categories). Each category is also linked to the corresponding WordNet synset, establishing the same linkage ...

## Evaluation Body Digest

- **p. 7 / 5.1. ShapeNetCore - extractive body cue:** The 12 object categories of PASCAL 3D+[35], a popular computer vision 3D benchmark dataset, are all covered by ShapeNetCore.
- **p. 6 / 4.1. Category Annotation - extractive body cue:** Through inspection, we identify and group 3D models into the following categories: single 3D models, 3D scenes, billboards, and big ground plane. • Single 3D ...
- **p. 6 / 4.1. Category Annotation - extractive body cue:** We manually verify these detections and mark scenes for future analysis. • Billboards: planes with a painted texture.
- **p. 7 / 5.1. ShapeNetCore - extractive body cue:** ShapeNetCore is a subset of the full ShapeNet dataset with single clean 3D models and manually verified category and alignment annotations.
- **p. 5 / 4. Annotation Acquisition and Validation - extractive body cue:** Our goal is to provide all annotations with high accuracy.
- **p. 6 / 4.1. Category Annotation - extractive body cue:** After we retrieve these models we use the popularity score of each model on the repository to sort models and ask human workers to verify ...
- **p. 5 / 4. Annotation Acquisition and Validation - extractive body cue:** In cases where full verification is not yet available, we aim to estimate a confidence metric for each annotation, as well as record its provenance.
- **p. 6 / 4.2. Hierarchical Rigid Alignment - extractive body cue:** With this strategy, we efficiently obtain consistent orientations.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Table 3. Total number of models for the top 100 ShapeNetSem categories (out of 270 categories). Each category is also linked to the corresponding ... | p. 9 (Figure/Table caption) |
| 4. Annotation Acquisition and Validation | BENCHMARK / DATASET | Our goal is to provide all annotations with high accuracy. | p. 5 (4. Annotation Acquisition and Validation) |
| 4.2. Hierarchical Rigid Alignment | BENCHMARK / DATASET | We explain by an example. "armchair", "chair" and "seat" are three categories in our taxonomy, each being a subcategory of its successor. | p. 6 (4.2. Hierarchical Rigid Alignment) |
| 4.1. Category Annotation | BENCHMARK / DATASET | After we retrieve these models we use the popularity score of each model on the repository to sort models and ask human workers to ... | p. 6 (4.1. Category Annotation) |
| 4.3. Parts and Keypoints | BENCHMARK / DATASET | models where further human annotation would be most informative, generate a new set of crowd-sourced annotation tasks, algorithmically propagate their results, and so on. | p. 7 (4.3. Parts and Keypoints) |

## Dataset / Benchmark Role

- **p. 7 / 5.1. ShapeNetCore - extractive body cue:** The 12 object categories of PASCAL 3D+[35], a popular computer vision 3D benchmark dataset, are all covered by ShapeNetCore.
- **p. 6 / 4.1. Category Annotation - extractive body cue:** Through inspection, we identify and group 3D models into the following categories: single 3D models, 3D scenes, billboards, and big ground plane. • Single 3D ...
- **p. 6 / 4.1. Category Annotation - extractive body cue:** We manually verify these detections and mark scenes for future analysis. • Billboards: planes with a painted texture.
- **p. 7 / 5.1. ShapeNetCore - extractive body cue:** ShapeNetCore is a subset of the full ShapeNet dataset with single clean 3D models and manually verified category and alignment annotations.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Source datasets from SHREC 2014: Princeton Shape Benchmark (PSB) [27], SHREC 2012 generic Shape Benchmark (SHREC12GTB) [16], Toyohashi Shape Benchmark (TSB) [29], Konstanz ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. Screenshot of the online ShapeNet taxonomy view, or- ganizing contained 3D models under WordNet synsets. shapes from a broad set of object and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. ShapeNet annotations illustrated for an example chair model. Left: links to the WordNet taxonomy provide definitions of objects, is-a and has-a relations, and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Examples of aligned models in the chair, laptop, bench, and airplane synsets. the concept of an upright orientation still applies throughout most levels ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Plots of the distribution of ShapeNet models over WordNet synsets at multiple levels of the taxonomy (only the top few children synsets are ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Statistics of ShapeNetCore synsets. ID corresponds to WordNet synset offset, which is aligned with ImageNet. 8
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3. Total number of models for the top 100 ShapeNetSem categories (out of 270 categories). Each category is also linked to the corresponding WordNet ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The 12 object categories of PASCAL 3D+[35], a popular computer vision 3D benchmark dataset, are all covered by ShapeNetCore. | embodiment, simulator version and control stack | p. 7 (5.1. ShapeNetCore), p. 6 (4.1. Category Annotation) |
| Task/environment | Through inspection, we identify and group 3D models into the following categories: single 3D models, 3D scenes, billboards, and big ground plane. • Single ... | reset, timeout, object/scene variation | p. 6 (4.1. Category Annotation), p. 6 (4.1. Category Annotation) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Our goal is to provide all annotations with high accuracy. | definition/direction/unit from same section | p. 5 (4. Annotation Acquisition and Validation) |
| After we retrieve these models we use the popularity score of each model on the repository to sort models and ask human workers to ... | definition/direction/unit from same section | p. 6 (4.1. Category Annotation) |
| In cases where full verification is not yet available, we aim to estimate a confidence metric for each annotation, as well as record its ... | definition/direction/unit from same section | p. 5 (4. Annotation Acquisition and Validation) |
| With this strategy, we efficiently obtain consistent orientations. | definition/direction/unit from same section | p. 6 (4.2. Hierarchical Rigid Alignment) |
| More specifically, we generate all combinations of pairs of vertices from the mesh. | definition/direction/unit from same section | p. 7 (4.4. Symmetry Estimation) |
| More details about the acquisition of these physical attribute annotations are available separately [26]. | definition/direction/unit from same section | p. 7 (4.5. Physical Property Estimation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We estimate the absolute dimensions of models using prior work in size estimation [25], followed by manual verification. | comparison identity and matched condition | p. 7 (4.5. Physical Property Estimation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Although we do not currently use these models, the plane can easily be identified and removed through simple geometric analysis. | component/input/data sensitivity | p. 6 (4.1. Category Annotation) |
| Through inspection, we identify and group 3D models into the following categories: single 3D models, 3D scenes, billboards, and big ground plane. • Single ... | component/input/data sensitivity | p. 6 (4.1. Category Annotation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Motivated by the far-reaching impact of dataset efforts such as the Penn Treebank [20], WordNet [21] and ImageNet [4], which collectively have tens of ... | Table 3. Total number of models for the top 100 ShapeNetSem categories (out of 270 categories). Each category is also linked to the corresponding ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 5 (4. Annotation Acquisition and Validation), p. 6 (4.2. Hierarchical Rigid Alignment), p. 6 (4.1. Category Annotation), p. 7 (4.3. Parts and Keypoints) |
| Primary metric/result | Our goal is to provide all annotations with high accuracy. | numeric claim only at cited anchor | p. 5 (4. Annotation Acquisition and Validation) |

- Numeric sentences retained from the body:
- **p. 7 / 5.1. ShapeNetCore - extractive body cue:** The 12 object categories of PASCAL 3D+[35], a popular computer vision 3D benchmark dataset, are all covered by ShapeNetCore.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Mirroring this pattern, recent work in computer graphics has also applied similar approaches to specific problems in the synthesis of new shape variations [10] ... | p. 1 (1. Introduction) |
| Annotations are made available through a public web-based interface to enable data visualization of object attributes, promote data-driven geometric analysis, and provide a large-scale ... | p. 1 (Abstract) |
| Achieving these goals and providing the resulting dataset to the community will enable many advances and applications in computer graphics and vision. | p. 2 (1. Introduction) |
| With the given absolute dimensions, we now compute the total solid volume of each model through filled-in voxelization. | p. 7 (4.5. Physical Property Estimation) |
| The 12 object categories of PASCAL 3D+[35], a popular computer vision 3D benchmark dataset, are all covered by ShapeNetCore. | p. 7 (5.1. ShapeNetCore) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **Evidence anchors reviewed:** datasets p. 7 (5.1. ShapeNetCore), p. 6 (4.1. Category Annotation), p. 6 (4.1. Category Annotation), p. 7 (5.1. ShapeNetCore), metrics p. 5 (4. Annotation Acquisition and Validation), p. 6 (4.1. Category Annotation), p. 5 (4. Annotation Acquisition and Validation), p. 6 (4.2. Hierarchical Rigid Alignment), p. 7 (4.4. Symmetry Estimation), p. 7 (4.5. Physical Property Estimation), baselines p. 7 (4.5. Physical Property Estimation), results p. 9 (Figure/Table caption), p. 5 (4. Annotation Acquisition and Validation), p. 6 (4.2. Hierarchical Rigid Alignment), p. 6 (4.1. Category Annotation), p. 7 (4.3. Parts and Keypoints).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
