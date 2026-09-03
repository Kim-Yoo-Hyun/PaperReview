# Evaluation - ReferIt3D: Neural Listeners for Fine-Grained 3D Object Identification in Real-World Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://referit3d.github.io/; PDF retrieval source: https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (Figure/Table caption), p. 12 (VI SD), p. 13 (Figure/Table caption), p. 11 (VI SD), p. 14 (Figure/Table caption), p. 11 (Figure/Table caption)): Table 2. ReferIt3DNet performance on Nr3D with/out Sr3D. The first row contains the achieved accuracy on the Nr3D testing data for a listener trained solely with the Nr3D training set; ...

## Evaluation Body Digest

- **p. 13 / VI SD - extractive body cue:** This demonstrates the contribution of adding a synthetically generated dataset to a human one.
- **p. 13 / VI SD - extractive body cue:** In Table 2, we observe how combining the two datasets provides a consistent boost in performance.
- **p. 11 / VI SD - extractive body cue:** Scene-Discoverable (SD): does the utterance explicitly refer to the target's object class (or a synonym), hence permitting object-identification among all objects of the scene?
- **p. 12 / VI SD - extractive body cue:** This enables the inspection of non-structured context when solving the reference task (PointNet++ is applied on a nonsegmented scene point cloud).
- **p. 12 / VI SD - extractive body cue:** Vision + Language + Holistic Context (V + L + C): Similar to the above, but also fuses a PointNet++ scene-feature with each object's visual ...
- **p. 11 / VI SD - extractive body cue:** Given an utterance we use the text-clf to predict the referred object-class.
- **p. 11 / VI SD - extractive body cue:** 5 Experiments and Analysis We explore different listening architectures 4 and report the listening accuracy; each test utterance receives a binary score (1 if the ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3. Listening performance of various ablated models. The first two columns contain the obtained accuracy when no auxiliary losses are used, and the last ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2. ReferIt3DNet performance on Nr3D with/out Sr3D. The first row contains the achieved accuracy on the Nr3D testing data for a listener trained ... | p. 12 (Figure/Table caption) |
| VI SD | SYSTEM / EVALUATION SCOPE UNRESOLVED | We observe the following main trends5: i) using the visual and linguistic auxiliary classification losses improves performance; ii) Simplified language (Sr3D) makes identification easier; ... | p. 12 (VI SD) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 4. ScanRefer performance with/out Sr3D. MeanIoU improvements when combining Sr3D data with ScanRefer's data during training. | p. 13 (Figure/Table caption) |
| VI SD | SYSTEM / EVALUATION SCOPE UNRESOLVED | 5 Experiments and Analysis We explore different listening architectures 4 and report the listening accuracy; each test utterance receives a binary score (1 if ... | p. 11 (VI SD) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 6. Qualitative results. Success cases are in the top four images and Failure in the bottom two. Targets are shown in green boxes ... | p. 14 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 13 / VI SD - extractive body cue:** This demonstrates the contribution of adding a synthetically generated dataset to a human one.
- **p. 13 / VI SD - extractive body cue:** In Table 2, we observe how combining the two datasets provides a consistent boost in performance.
- **p. 11 / VI SD - extractive body cue:** Scene-Discoverable (SD): does the utterance explicitly refer to the target's object class (or a synonym), hence permitting object-identification among all objects of the scene?
- **p. 12 / VI SD - extractive body cue:** This enables the inspection of non-structured context when solving the reference task (PointNet++ is applied on a nonsegmented scene point cloud).
- **p. 12 / VI SD - extractive body cue:** Vision + Language + Holistic Context (V + L + C): Similar to the above, but also fuses a PointNet++ scene-feature with each object's visual ...
- **p. 11 / VI SD - extractive body cue:** Given an utterance we use the text-clf to predict the referred object-class.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Examples of natural free-form utterances. Each color-coded utterance distinguishes the corresponding object (marked with same color) against a distracting object in the underlying ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 2. Examples of spatial reference types of Sr3D. In the left image, there are exam- ples of "horizontal proximity", "between", and "support" relations; the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Statistics of Sr3D. The first row contains the number of distinct commu- nication contexts yielded by each reference-type. The second row contains the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 3. Vocabulary histogram. was asked to select the referred object among its distractors. The game is struc- tured such that both ‘speaker' and ‘lis- ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 4. The ReferIt3DNet neural listener. A visual encoder processes (via a shared PointNet++) each 3D object of a given scene that is represented by ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 5. Easy vs. Hard communication contexts and examples of natural utterances with attributes that affect a navigating/listening agent. Scene-Discoverable (SD): does the utterance explicitly ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 2. ReferIt3DNet performance on Nr3D with/out Sr3D. The first row contains the achieved accuracy on the Nr3D testing data for a listener trained solely ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3. Listening performance of various ablated models. The first two columns contain the obtained accuracy when no auxiliary losses are used, and the last ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This demonstrates the contribution of adding a synthetically generated dataset to a human one. | embodiment, simulator version and control stack | p. 13 (VI SD), p. 13 (VI SD) |
| Task/environment | In Table 2, we observe how combining the two datasets provides a consistent boost in performance. | reset, timeout, object/scene variation | p. 13 (VI SD), p. 11 (VI SD) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1 Introduction), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 5 Experiments and Analysis We explore different listening architectures 4 and report the listening accuracy; each test utterance receives a binary score (1 if ... | definition/direction/unit from same section | p. 11 (VI SD) |
| Table 3. Listening performance of various ablated models. The first two columns contain the obtained accuracy when no auxiliary losses are used, and the ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Table 2. ReferIt3DNet performance on Nr3D with/out Sr3D. The first row contains the achieved accuracy on the Nr3D testing data for a listener trained ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Fig. 3. Vocabulary histogram. was asked to select the referred object among its distractors. The game is struc- tured such that both ‘speaker' and ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Fig. 5. Easy vs. Hard communication contexts and examples of natural utterances with attributes that affect a navigating/listening agent. Scene-Discoverable (SD): does the utterance ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Fig. 6. Qualitative results. Success cases are in the top four images and Failure in the bottom two. Targets are shown in green boxes ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Table 1. Statistics of Sr3D. The first row contains the number of distinct commu- nication contexts yielded by each reference-type. The second row contains ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| This demonstrates the contribution of adding a synthetically generated dataset to a human one. | definition/direction/unit from same section | p. 13 (VI SD) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Decoupled approach: This is a baseline listener consisting of a text classifier and an (FG) object classifier that are trained separately. | comparison identity and matched condition | p. 11 (VI SD) |
| This baseline can encode visual properties of an object beyond its FG class enabling rich (context-free) distinctions (e.g.,"very small, or yellow colored chair"). | comparison identity and matched condition | p. 11 (VI SD) |
| Comparisons for the above models are presented in Table 3. | comparison identity and matched condition | p. 12 (VI SD) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The first row contains the achieved accuracy on the Nr3D testing data for a listener trained solely with the Nr3D training set; the other ... | component/input/data sensitivity | p. 12 (VI SD) |
| Vision + Language + Graph (structured) Context (ReferIt3DNet): This is our proposed listener and comes in three variants that differ w.r.t. where we fuse ... | component/input/data sensitivity | p. 12 (VI SD) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| For Sr3D we propose a simple but effective methodology for building template-based and spatially-oriented object referential language in 3D scenes. | Table 2. ReferIt3DNet performance on Nr3D with/out Sr3D. The first row contains the achieved accuracy on the Nr3D testing data for a listener trained ... | PDF body cue; verify exact table/figure and matched conditions | p. 12 (Figure/Table caption), p. 12 (VI SD), p. 13 (Figure/Table caption), p. 11 (VI SD), p. 14 (Figure/Table caption), p. 11 (Figure/Table caption) |
| Primary metric/result | We observe the following main trends5: i) using the visual and linguistic auxiliary classification losses improves performance; ii) Simplified language (Sr3D) makes identification easier; ... | numeric claim only at cited anchor | p. 12 (VI SD) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Success cases are in the top four images and Failure in the bottom two. | p. 14 (6 Conclusion) |
| body limitation/failure cue | Finally, the last row shows two challenging failure cases of our model. | p. 13 (VI SD) |
| body limitation/failure cue | This does not come as a surprise, since the network has naturally more work to do to comprehend nuances related to viewing the scene ... | p. 13 (VI SD) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each color-coded utterance distinguishes the corresponding object (marked with same color) against a distracting object in the underlying scene; contrasting two simple chairs (left) ... | p. 2 (1 Introduction) |
| This baseline can encode visual properties of an object beyond its FG class enabling rich (context-free) distinctions (e.g.,"very small, or yellow colored chair"). | p. 11 (VI SD) |
| Referring to this particular trashcan among other similar ones requires both spatial reasoning and 5 In all results mean accuracies and standard errors across ... | p. 12 (VI SD) |
| We performed this experiment following the implementation in [17]. | p. 13 (VI SD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 6 Conclusion - extractive body cue:** Success cases are in the top four images and Failure in the bottom two.
- **p. 13 / VI SD - extractive body cue:** Finally, the last row shows two challenging failure cases of our model.
- **p. 13 / VI SD - extractive body cue:** This does not come as a surprise, since the network has naturally more work to do to comprehend nuances related to viewing the scene w.r.t. ...

- **Evidence anchors reviewed:** datasets p. 13 (VI SD), p. 13 (VI SD), p. 11 (VI SD), p. 12 (VI SD), p. 12 (VI SD), p. 11 (VI SD), metrics p. 11 (VI SD), p. 12 (Figure/Table caption), p. 12 (Figure/Table caption), p. 8 (Figure/Table caption), p. 11 (Figure/Table caption), p. 14 (Figure/Table caption), baselines p. 11 (VI SD), p. 11 (VI SD), p. 12 (VI SD), results p. 12 (Figure/Table caption), p. 12 (VI SD), p. 13 (Figure/Table caption), p. 11 (VI SD), p. 14 (Figure/Table caption), p. 11 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
