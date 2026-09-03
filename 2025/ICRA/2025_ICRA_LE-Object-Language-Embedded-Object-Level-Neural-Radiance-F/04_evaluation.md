# Evaluation - LE-Object: Language Embedded Object-Level Neural Radiance Fields for Open-Vocabulary Scene

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2406.08009v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (Figure/Table caption), p. 4 (III. OPENOBJ), p. 7 (2) Are OpenObj's open-vocabulary object-level and part), p. 7 (2) Are OpenObj's open-vocabulary object-level and part), p. 2 (I. INTRODUCTION)): In this section, we aim to use experiments to validate OpenObj, through the following specific questions: 1) Without fine-tuning any model, can OpenObj achieve 2D and 3D segmentation of any ...

## Evaluation Body Digest

- **p. 7 / 2) Are OpenObj's open-vocabulary object-level and part - extractive body cue:** Datasets and Metrics: The experiments are conducted on four scenes in Replica [32], each featuring a diverse array of objects.
- **p. 6 / 2) Are OpenObj's open-vocabulary object-level and part - extractive body cue:** Datasets and Metrics: We select two commonly used indoor datasets: eight scenes from Replica [32] and six scenes from ScanNet [33].
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, Our contributions are summarized as follows: • We present OpenObj, the open-vocabulary object-level neural radiance fields with fine-grained understanding, supporting downstream tasks at ...
- **p. 3 / III. OPENOBJ - extractive body cue:** Object Segmentation and Understanding Vision, as the primary sense for both humans and robots to perceive the world, provides rich color and texture information essential ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** recognize scenes only at the object level and fail to provide a more granular understanding of internal structures.
- **p. 6 / 2) Are OpenObj's open-vocabulary object-level and part - extractive body cue:** Due to the lack of detailed 2D annotations in ScanNet, we opt to conduct 3D segmentation validation exclusively on the ScanNet dataset.
- **p. 7 / 2) Are OpenObj's open-vocabulary object-level and part - extractive body cue:** The user can issue a find object command to the robot, and the 7
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** In this section, we aim to use experiments to validate OpenObj, through the following specific questions: 1) Without fine-tuning any model, can OpenObj achieve 2D ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** IV. EXPERIMENTAL RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTAL RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | In this section, we aim to use experiments to validate OpenObj, through the following specific questions: 1) Without fine-tuning any model, can OpenObj achieve ... | p. 5 (IV. EXPERIMENTAL RESULTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 5: 2D & 3D zero-shot segmentation results. OpenObj's object-level NeRF and comprehensive understanding enable it to achieve clear boundaries and accurate semantics. | p. 6 (Figure/Table caption) |
| III. OPENOBJ | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the coarse clustering phase, a graph is constructed for all masks, and the Louvain algorithm is applied to achieve clustering. | p. 4 (III. OPENOBJ) |
| 2) Are OpenObj's open-vocabulary object-level and part | EMPIRICAL / SOURCE-REPORTED EVALUATION | OpenObj consistently outperforms ConceptGraphs across all types of retrieval tasks. | p. 7 (2) Are OpenObj's open-vocabulary object-level and part) |
| 2) Are OpenObj's open-vocabulary object-level and part | EMPIRICAL / SOURCE-REPORTED EVALUATION | In contrast, OpenObj adopts a two-stage mask clustering approach, which leads to a more optimal solution for global object segmentation, and combines object understanding ... | p. 7 (2) Are OpenObj's open-vocabulary object-level and part) |

## Dataset / Benchmark Role

- **p. 7 / 2) Are OpenObj's open-vocabulary object-level and part - extractive body cue:** Datasets and Metrics: The experiments are conducted on four scenes in Replica [32], each featuring a diverse array of objects.
- **p. 6 / 2) Are OpenObj's open-vocabulary object-level and part - extractive body cue:** Datasets and Metrics: We select two commonly used indoor datasets: eight scenes from Replica [32] and six scenes from ScanNet [33].
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, Our contributions are summarized as follows: • We present OpenObj, the open-vocabulary object-level neural radiance fields with fine-grained understanding, supporting downstream tasks at ...
- **p. 3 / III. OPENOBJ - extractive body cue:** Object Segmentation and Understanding Vision, as the primary sense for both humans and robots to perceive the world, provides rich color and texture information essential ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** recognize scenes only at the object level and fail to provide a more granular understanding of internal structures.
- **p. 6 / 2) Are OpenObj's open-vocabulary object-level and part - extractive body cue:** Due to the lack of detailed 2D annotations in ScanNet, we opt to conduct 3D segmentation validation exclusively on the ScanNet dataset.
- **p. 7 / 2) Are OpenObj's open-vocabulary object-level and part - extractive body cue:** The user can issue a find object command to the robot, and the 7
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** In this section, we aim to use experiments to validate OpenObj, through the following specific questions: 1) Without fine-tuning any model, can OpenObj achieve 2D ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We introduce OpenObj, a framework of open-vocabulary object-level neural radiance fields with fine-grained understanding. OpenObj facilitates various downstream tasks, including open-vocabulary object retrieval, ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The framework of OpenObj consists of four main modules: Object Segmentation and Understanding, Mask Clustering, Part-level Fine-Grained Feature Extraction, and Hierarchical Graph Representation ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Two-stage mask clustering. In the coarse clustering phase, a graph is constructed for all masks, and the Louvain algorithm is applied to achieve ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Part-level fine-grained feature extraction process: The mask mpart t,j extracted by SAM is dense and may be nested. The dense masks are visually ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: 2D & 3D zero-shot segmentation results. OpenObj's object-level NeRF and comprehensive understanding enable it to achieve clear boundaries and accurate semantics.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: A selection of results from open-vocabulary retrieval. OpenObj correctly and clearly highlights the most relevant instance in each query. more comprehensive and robust ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: OpenObj's multi-granularity scene understanding sup- ports multi-granularity downstream tasks, including object-oriented global movement and part-oriented local manipulation. a marked advantage in handling patterns, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Datasets and Metrics: The experiments are conducted on four scenes in Replica [32], each featuring a diverse array of objects. | embodiment, simulator version and control stack | p. 7 (2) Are OpenObj's open-vocabulary object-level and part), p. 6 (2) Are OpenObj's open-vocabulary object-level and part) |
| Task/environment | Datasets and Metrics: We select two commonly used indoor datasets: eight scenes from Replica [32] and six scenes from ScanNet [33]. | reset, timeout, object/scene variation | p. 6 (2) Are OpenObj's open-vocabulary object-level and part), p. 2 (I. INTRODUCTION) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (III. OPENOBJ), p. 3 (III. OPENOBJ) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (III. OPENOBJ), p. 4 (III. OPENOBJ) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For the evaluation metrics, we use mean IoU (mIoU) and mean accuracy (mAcc). | definition/direction/unit from same section | p. 6 (2) Are OpenObj's open-vocabulary object-level and part) |
| To facilitate fast matrix computation, we take the bounding box Intersection over Union (IoU) of the point cloud as Spc. | definition/direction/unit from same section | p. 4 (III. OPENOBJ) |
| Fig. 2: The framework of OpenObj consists of four main modules: Object Segmentation and Understanding, Mask Clustering, Part-level Fine-Grained Feature Extraction, and Hierarchical Graph ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| The coverage rate indicates the proportion of matched points (with distances less than the threshold) among the lesser set. | definition/direction/unit from same section | p. 4 (III. OPENOBJ) |
| To evaluate the performance, we measure the recall at the top-1, top-2, and top-3 levels. | definition/direction/unit from same section | p. 7 (2) Are OpenObj's open-vocabulary object-level and part) |
| The question then arises: What is the effective granularity of an open-vocabulary map representation? | definition/direction/unit from same section | p. 2 (I. INTRODUCTION) |
| In this way, the resulting map representation offers multi-granularity understanding and watertight reconstruction. | definition/direction/unit from same section | p. 2 (I. INTRODUCTION) |
| The framework of OpenObj, illustrated in Fig. | definition/direction/unit from same section | p. 3 (III. OPENOBJ) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 2D & 3D Zero-shot Semantic Segmentation Baseline: For 2D semantic segmentation, we compare OpenObj with the language-driven image segmentation method LSeg [31], as well ... | comparison identity and matched condition | p. 6 (2) Are OpenObj's open-vocabulary object-level and part) |
| For 3D semantic segmentation, we add ConceptGraphs [12] as a baseline to LERF and 3D-OVS, an open-vocabulary object-level point cloud map construction method. | comparison identity and matched condition | p. 6 (2) Are OpenObj's open-vocabulary object-level and part) |
| OpenObj consistently outperforms ConceptGraphs across all types of retrieval tasks. | comparison identity and matched condition | p. 7 (2) Are OpenObj's open-vocabulary object-level and part) |
| Multi-granularity Open-vocabulary Retrieval Baseline: For the retrieval experiments, only ConceptGraphs [12] with object-level concepts is kept as a baseline. | comparison identity and matched condition | p. 7 (2) Are OpenObj's open-vocabulary object-level and part) |
| In this section, we aim to use experiments to validate OpenObj, through the following specific questions: 1) Without fine-tuning any model, can OpenObj achieve ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTAL RESULTS) |
| Fig. 2: The framework of OpenObj consists of four main modules: Object Segmentation and Understanding, Mask Clustering, Part-level Fine-Grained Feature Extraction, and Hierarchical Graph ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In this section, we aim to use experiments to validate OpenObj, through the following specific questions: 1) Without fine-tuning any model, can OpenObj achieve ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTAL RESULTS) |
| Fig. 2: The framework of OpenObj consists of four main modules: Object Segmentation and Understanding, Mask Clustering, Part-level Fine-Grained Feature Extraction, and Hierarchical Graph ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| However, this sensitivity comes at the cost of losing the capacity to recover complex concepts. | component/input/data sensitivity | p. 6 (2) Are OpenObj's open-vocabulary object-level and part) |
| Upon closer observation, they then derive a detailed description of the individual components of specific objects (e.g., ‘this cup has a square handle and ... | component/input/data sensitivity | p. 2 (I. INTRODUCTION) |
| LSeg, as a fine-tuned model of CLIP, TABLE II: 3D Zero-shot Segmentation Results mIoU mAcc Scene LERF 3DOVS Con.G. | component/input/data sensitivity | p. 6 (2) Are OpenObj's open-vocabulary object-level and part) |
| 7: OpenObj's multi-granularity scene understanding supports multi-granularity downstream tasks, including object-oriented global movement and part-oriented local manipulation. a marked advantage in handling patterns, components, ... | component/input/data sensitivity | p. 7 (2) Are OpenObj's open-vocabulary object-level and part) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, Our contributions are summarized as follows: • We present OpenObj, the open-vocabulary object-level neural radiance fields with fine-grained understanding, supporting downstream tasks ... | In this section, we aim to use experiments to validate OpenObj, through the following specific questions: 1) Without fine-tuning any model, can OpenObj achieve ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (Figure/Table caption), p. 4 (III. OPENOBJ), p. 7 (2) Are OpenObj's open-vocabulary object-level and part), p. 7 (2) Are OpenObj's open-vocabulary object-level and part), p. 2 (I. INTRODUCTION) |
| Primary metric/result | Fig. 5: 2D & 3D zero-shot segmentation results. OpenObj's object-level NeRF and comprehensive understanding enable it to achieve clear boundaries and accurate semantics. | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This approach helps to mitigate the effects of outliers caused by poor observation viewpoints or model failures. | p. 5 (III. OPENOBJ) |
| body limitation/failure cue | Fig. 1: We introduce OpenObj, a framework of open-vocabulary object-level neural radiance fields with fine-grained understanding. OpenObj facilitates various downstream tasks, including open-vocabulary object ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Additionally, we apply another method to compensate for the limitations of VLM features f clip t,i in semantic reasoning. | p. 3 (III. OPENOBJ) |
| body limitation/failure cue | Since this method does not distinguish between the sources of the masks, it can effectively correlate masks across different frames and within the same ... | p. 4 (III. OPENOBJ) |
| body limitation/failure cue | recognize scenes only at the object level and fail to provide a more granular understanding of internal structures. | p. 2 (I. INTRODUCTION) |
| body limitation/failure cue | OpenObj correctly and clearly highlights the most relevant instance in each query. more comprehensive and robust understanding of objects. | p. 7 (2) Are OpenObj's open-vocabulary object-level and part) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In this paper, we use the visual encoder of CLIP [4] to encode images cropped according to the mask mobj t,i as VLM feature ... | p. 3 (III. OPENOBJ) |
| Given the strong advantages of LLMs in natural language processing tasks, we encode these captions using LLMs to obtain their caption features f cap ... | p. 3 (III. OPENOBJ) |
| Dense Mask Feature Image VLM Encoder VLM Encoder VLM Encoder Fig. | p. 4 (III. OPENOBJ) |
| We then compute the matched points coverage rate and the similarity of color histograms between two clustered point clouds. | p. 4 (III. OPENOBJ) |
| These labels are encoded to obtain textual features. | p. 6 (2) Are OpenObj's open-vocabulary object-level and part) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / III. OPENOBJ - extractive body cue:** This approach helps to mitigate the effects of outliers caused by poor observation viewpoints or model failures.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We introduce OpenObj, a framework of open-vocabulary object-level neural radiance fields with fine-grained understanding. OpenObj facilitates various downstream tasks, including open-vocabulary object retrieval, ...
- **p. 3 / III. OPENOBJ - extractive body cue:** Additionally, we apply another method to compensate for the limitations of VLM features f clip t,i in semantic reasoning.
- **p. 4 / III. OPENOBJ - extractive body cue:** Since this method does not distinguish between the sources of the masks, it can effectively correlate masks across different frames and within the same frame, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** recognize scenes only at the object level and fail to provide a more granular understanding of internal structures.
- **p. 7 / 2) Are OpenObj's open-vocabulary object-level and part - extractive body cue:** OpenObj correctly and clearly highlights the most relevant instance in each query. more comprehensive and robust understanding of objects.

- **Evidence anchors reviewed:** datasets p. 7 (2) Are OpenObj's open-vocabulary object-level and part), p. 6 (2) Are OpenObj's open-vocabulary object-level and part), p. 2 (I. INTRODUCTION), p. 3 (III. OPENOBJ), p. 2 (I. INTRODUCTION), p. 6 (2) Are OpenObj's open-vocabulary object-level and part), metrics p. 6 (2) Are OpenObj's open-vocabulary object-level and part), p. 4 (III. OPENOBJ), p. 3 (Figure/Table caption), p. 4 (III. OPENOBJ), p. 7 (2) Are OpenObj's open-vocabulary object-level and part), p. 2 (I. INTRODUCTION), baselines p. 6 (2) Are OpenObj's open-vocabulary object-level and part), p. 6 (2) Are OpenObj's open-vocabulary object-level and part), p. 7 (2) Are OpenObj's open-vocabulary object-level and part), p. 7 (2) Are OpenObj's open-vocabulary object-level and part), p. 5 (IV. EXPERIMENTAL RESULTS), p. 3 (Figure/Table caption), results p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (Figure/Table caption), p. 4 (III. OPENOBJ), p. 7 (2) Are OpenObj's open-vocabulary object-level and part), p. 7 (2) Are OpenObj's open-vocabulary object-level and part), p. 2 (I. INTRODUCTION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
