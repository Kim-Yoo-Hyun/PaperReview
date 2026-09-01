# Evaluation - IRef-VLA: A Benchmark for Interactive Referential Grounding with Imperfect Language in 3D Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2503.17406v1. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (I. INTRODUCTION), p. 5 (Figure/Table caption), p. 1 (I. INTRODUCTION), p. 3 (Figure/Table caption)): An agent that can 1) similarly solve such a problem, 2) handle imperfect or ambiguous language, and 3) interact with humans to achieve the intended goal would be valuable in ...

## Evaluation Body Digest

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** First, we provide the largest real-world dataset based on 3D scenes from a diverse set of existing indoor scans.
- **p. 1 / Abstract - extractive PDF cue:** To address this challenge, we curate a benchmark dataset, IRef-VLA, for Interactive Referential Vision and Language-guided Action in 3D Scenes with imperfect references.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Despite impressive recent advancements with foundation models, such problems remain difficult when applied to robotics as current methods fail to offer the accuracy and robustness ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. Breakdown of regions from each data source heavily on original user intent and preferences. Thus, human- labeled scores may better quantify quality, though ...
- **p. 1 / Abstract - extractive PDF cue:** We verify the generalizability of our dataset by evaluating with state-of-the-art models to obtain a performance baseline and also develop a graphsearch baseline to demonstrate ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 5. A comparison between heuristically generated statements describing a binary spatial relation from Sr3D, Nr3D [14], SceneVerse [16], and IRef- VLA. Both chairs are ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6. Pipeline for graph-search and alternative generation baseline through a simple two-layer MLP and trained with a cross- entropy loss. The additional referential losses ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** An agent that can 1) similarly solve such a problem, 2) handle imperfect or ambiguous language, and 3) interact with humans to achieve the intended ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** IV. DATASET CREATION (p. 3); V. BASELINE EVALUATION (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| I. INTRODUCTION | BENCHMARK / DATASET | An agent that can 1) similarly solve such a problem, 2) handle imperfect or ambiguous language, and 3) interact with humans to achieve the ... | p. 1 (I. INTRODUCTION) |
| Figure/Table caption | BENCHMARK / DATASET | Fig. 5. A comparison between heuristically generated statements describing a binary spatial relation from Sr3D, Nr3D [14], SceneVerse [16], and IRef- VLA. Both chairs ... | p. 5 (Figure/Table caption) |
| I. INTRODUCTION | BENCHMARK / DATASET | Third, the scale of available visionlanguage data in the 3D space pales in comparison to the amount of 2D data, which was crucial to ... | p. 1 (I. INTRODUCTION) |
| Figure/Table caption | BENCHMARK / DATASET | Fig. 2. Breakdown of regions from each data source heavily on original user intent and preferences. Thus, human- labeled scores may better quantify quality, ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** First, we provide the largest real-world dataset based on 3D scenes from a diverse set of existing indoor scans.
- **p. 1 / Abstract - extractive PDF cue:** To address this challenge, we curate a benchmark dataset, IRef-VLA, for Interactive Referential Vision and Language-guided Action in 3D Scenes with imperfect references.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1. Sample region from the dataset visualized with (a) a scene graph and (b) a corresponding referential statement . The pursuit of such agents ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. Breakdown of regions from each data source heavily on original user intent and preferences. Thus, human- labeled scores may better quantify quality, though ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3. Number of statements per relation type from each dataset processed TABLE I SUMMARY OF SEMANTIC RELATIONSHIP TYPES IN IREF-VLA Relation Definition Synonyms Properties
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4. Data processing pipeline consisting of: 3D Scan Processing, Scene Graph Generation, and Language Generation
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 5. A comparison between heuristically generated statements describing a binary spatial relation from Sr3D, Nr3D [14], SceneVerse [16], and IRef- VLA. Both chairs are ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6. Pipeline for graph-search and alternative generation baseline through a simple two-layer MLP and trained with a cross- entropy loss. The additional referential losses ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | First, we provide the largest real-world dataset based on 3D scenes from a diverse set of existing indoor scans. | embodiment, simulator version and control stack | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Task/environment | To address this challenge, we curate a benchmark dataset, IRef-VLA, for Interactive Referential Vision and Language-guided Action in 3D Scenes with imperfect references. | reset, timeout, object/scene variation | p. 1 (Abstract) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | 본문 anchor 없음 |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Despite impressive recent advancements with foundation models, such problems remain difficult when applied to robotics as current methods fail to offer the accuracy and ... | definition/direction/unit from same section | p. 1 (I. INTRODUCTION) |
| Fig. 2. Breakdown of regions from each data source heavily on original user intent and preferences. Thus, human- labeled scores may better quantify quality, ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| We verify the generalizability of our dataset by evaluating with state-of-the-art models to obtain a performance baseline and also develop a graphsearch baseline to ... | definition/direction/unit from same section | p. 1 (Abstract) |
| Fig. 5. A comparison between heuristically generated statements describing a binary spatial relation from Sr3D, Nr3D [14], SceneVerse [16], and IRef- VLA. Both chairs ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 6. Pipeline for graph-search and alternative generation baseline through a simple two-layer MLP and trained with a cross- entropy loss. The additional referential ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We verify the generalizability of our dataset by evaluating with state-of-the-art models to obtain a performance baseline and also develop a graphsearch baseline to ... | comparison identity and matched condition | p. 1 (Abstract) |
| Fig. 5. A comparison between heuristically generated statements describing a binary spatial relation from Sr3D, Nr3D [14], SceneVerse [16], and IRef- VLA. Both chairs ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Fig. 6. Pipeline for graph-search and alternative generation baseline through a simple two-layer MLP and trained with a cross- entropy loss. The additional referential ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Third, the scale of available visionlanguage data in the 3D space pales in comparison to the amount of 2D data, which was crucial to ... | comparison identity and matched condition | p. 1 (I. INTRODUCTION) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To advance the path towards more intelligent interaction in natural language navigation, we propose the IRef-VLA dataset as a benchmark for both the referential ... | An agent that can 1) similarly solve such a problem, 2) handle imperfect or ambiguous language, and 3) interact with humans to achieve the ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (I. INTRODUCTION), p. 5 (Figure/Table caption), p. 1 (I. INTRODUCTION), p. 3 (Figure/Table caption) |
| Primary metric/result | Fig. 5. A comparison between heuristically generated statements describing a binary spatial relation from Sr3D, Nr3D [14], SceneVerse [16], and IRef- VLA. Both chairs ... | numeric claim only at cited anchor | p. 5 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Despite impressive recent advancements with foundation models, such problems remain difficult when applied to robotics as current methods fail to offer the accuracy and ... | p. 1 (I. INTRODUCTION) |
| body limitation/failure cue | Second, human referential language often involves spatial reasoning, implicit and explicit affordances, open-vocabulary language, and may even be incorrect or refer to something that ... | p. 1 (I. INTRODUCTION) |
| body limitation/failure cue | Fig. 6. Pipeline for graph-search and alternative generation baseline through a simple two-layer MLP and trained with a cross- entropy loss. The additional referential ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The dataset and all source code is publicly released1. | p. 1 (Abstract) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Despite impressive recent advancements with foundation models, such problems remain difficult when applied to robotics as current methods fail to offer the accuracy and robustness ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Second, human referential language often involves spatial reasoning, implicit and explicit affordances, open-vocabulary language, and may even be incorrect or refer to something that does ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6. Pipeline for graph-search and alternative generation baseline through a simple two-layer MLP and trained with a cross- entropy loss. The additional referential losses ...

- **PDF anchors reviewed:** datasets p. 1 (I. INTRODUCTION), p. 1 (Abstract), metrics p. 1 (I. INTRODUCTION), p. 3 (Figure/Table caption), p. 1 (Abstract), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), baselines p. 1 (Abstract), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 1 (I. INTRODUCTION), results p. 1 (I. INTRODUCTION), p. 5 (Figure/Table caption), p. 1 (I. INTRODUCTION), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
