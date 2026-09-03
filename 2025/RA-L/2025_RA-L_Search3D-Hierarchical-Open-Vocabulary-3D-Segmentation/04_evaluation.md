# Evaluation - Search3D: Hierarchical Open-Vocabulary 3D Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2409.18431; PDF retrieval source: https://arxiv.org/pdf/2409.18431. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 2 (Figure/Table caption), p. 7 (V. EXPERIMENTS)): It demonstrates the strong open-vocabulary part-segmentation performance of our segment-level features, with at least + 13.8 AP improvement over baseline methods.

## Evaluation Body Digest

- **p. 7 / V. EXPERIMENTS - extractive body cue:** 3D Material Segmentation Next, we perform an analysis on 3D material segmentation task using the object-level material annotations from the 3RScan dataset [18].
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Lastly, our approach is limited to two explicit granularity levels (objects and parts), reflecting the lack of evaluation benchmarks for finer-grained segmentation.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** 3D Part Segmentation To evaluate our method's ability to handle queries beyond object-level descriptions, we introduce the task of scene-level 3D open-vocabulary part segmentation.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** IV-A), and the annotations we provide on the ScanNet++ [17] dataset (see Sec.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** 6 IEEE ROBOTICS AND AUTOMATION LETTERS.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** To evaluate this, we compare our method with existing open-vocabulary 3D instance segmentation methods using the standard benchmark on ScanNet200 [44] in Tab.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Additionally, averaging the objectlevel and part-level similarity scores yields slightly better results than using the maximum of these scores.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** II, where oracle mask experiment yields much higher AP scores than those with predicted part masks, indicating room for improvement in 3D part mask quality.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | It demonstrates the strong open-vocabulary part-segmentation performance of our segment-level features, with at least + 13.8 AP improvement over baseline methods. | p. 6 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | V, our method has very strong 3D instance segmentation performance, outperforming other counterparts that rely solely on 3D masks for identifying object-level instances. | p. 6 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | II, where oracle mask experiment yields much higher AP scores than those with predicted part masks, indicating room for improvement in 3D part mask ... | p. 7 (V. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. To achieve this, we construct a tree representation where nodes represent scenes, objects and part-entities. For each object and part node, we ... | p. 2 (Figure/Table caption) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | In contrast, our mask module can identify objects, which enables strong performance for both instance segmentation and part segmentation through the hierarchical search mechanism. | p. 7 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / V. EXPERIMENTS - extractive body cue:** 3D Material Segmentation Next, we perform an analysis on 3D material segmentation task using the object-level material annotations from the 3RScan dataset [18].
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Lastly, our approach is limited to two explicit granularity levels (objects and parts), reflecting the lack of evaluation benchmarks for finer-grained segmentation.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** 3D Part Segmentation To evaluate our method's ability to handle queries beyond object-level descriptions, we introduce the task of scene-level 3D open-vocabulary part segmentation.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** IV-A), and the annotations we provide on the ScanNet++ [17] dataset (see Sec.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** 6 IEEE ROBOTICS AND AUTOMATION LETTERS.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** To evaluate this, we compare our method with existing open-vocabulary 3D instance segmentation methods using the standard benchmark on ScanNet200 [44] in Tab.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose Search3D, a method for open-vocabulary 3D search at multiple levels of granularity. From posed RGB-D images and reconstructed geometry, we build ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. To achieve this, we construct a tree representation where nodes represent scenes, objects and part-entities. For each object and part node, we compute ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Search3D overview: 1⃝The inputs of our approach are posed RGB-D images of a 3D indoor scene along with its reconstructed 3D geometry. 2⃝computes ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Pixel-level features. OpenSeg [34], used in OpenScene, has a limited understanding of finer-grained object parts in the scene. We propose to obtain pixel-aligned ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: An example from our hierarchical object and part annotations on a selection of ScanNet++ [17] scenes. Methods Segments AP OpenScene [6] Oracle 31.4
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Heatmaps showing response to text queries of Search3D. Dark red means high similarity and dark blue means low similarity. OpenScene [6] Search3D (Ours) ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Similarity heatmaps between text queries and scene features. We compare OpenScene [6] per-point features with the segment features from our method. Dark red ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 3D Material Segmentation Next, we perform an analysis on 3D material segmentation task using the object-level material annotations from the 3RScan dataset [18]. | embodiment, simulator version and control stack | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Task/environment | Lastly, our approach is limited to two explicit granularity levels (objects and parts), reflecting the lack of evaluation benchmarks for finer-grained segmentation. | reset, timeout, object/scene variation | p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 3 (2) Computing open-vocabulary features for the scene repre) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Additionally, averaging the objectlevel and part-level similarity scores yields slightly better results than using the maximum of these scores. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| II, where oracle mask experiment yields much higher AP scores than those with predicted part masks, indicating room for improvement in 3D part mask ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| We use Intersection-over-Union (mIoU) and mean accuracy (Acc) to evaluate material class predictions obtained using query-similarity based assignments similar to the instance segmentation task. | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| It demonstrates the strong open-vocabulary part-segmentation performance of our segment-level features, with at least + 13.8 AP improvement over baseline methods. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| In the part-level instance segmentation experiments, we report the Average Precision metric evaluated at 50% (AP50), 25% (AP25) overlap thresholds, and the average over ... | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| First, we evaluate the quality of our segment features for identifying object parts using an oracle mask experiment, isolating feature quality from the effect ... | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| I shows the results from this oracle experiment. | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| (3) is a stronger baseline adapted from (2) using segment-level aggregation. | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| II, where oracle mask experiment yields much higher AP scores than those with predicted part masks, indicating room for improvement in 3D part mask ... | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| Fig. 4: An example from our hierarchical object and part annotations on a selection of ScanNet++ [17] scenes. Methods Segments AP OpenScene [6] Oracle ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| This is evident from the comparison between Tab. | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Aggr. search AP AP50 AP25 (1) Ours ✓ 4.7 8.2 17.6 (2) Ours ✓ ✓ 6.6 11.4 23.7 (3) Ours ✓ ✓ ✓(max.) 7.5 ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| First, we evaluate the quality of our segment features for identifying object parts using an oracle mask experiment, isolating feature quality from the effect ... | component/input/data sensitivity | p. 5 (V. EXPERIMENTS) |
| Additionally, we validate our design choices through corresponding ablation studies. | component/input/data sensitivity | p. 5 (V. EXPERIMENTS) |
| IV emphasize the importance of those components. | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize our key contributions: • We propose a hierarchical open-vocabulary 3D segmentation method capable of segmenting both entire objects and their parts given ... | It demonstrates the strong open-vocabulary part-segmentation performance of our segment-level features, with at least + 13.8 AP improvement over baseline methods. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 2 (Figure/Table caption), p. 7 (V. EXPERIMENTS) |
| Primary metric/result | V, our method has very strong 3D instance segmentation performance, outperforming other counterparts that rely solely on 3D masks for identifying object-level instances. | numeric claim only at cited anchor | p. 6 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Once this representation is built, inference 6⃝, i.e., 3D search based on user input queries can be performed at around 1-2 FPS.
- **p. 5 / IV. DATA - extractive body cue:** The adapted dataset we release, based on existing fine-grained annotations from MultiScan, includes 155 object and 15 part categories.
- **p. 5 / IV. DATA - extractive body cue:** To address this gap, our dataset includes 14 object and 20 part annotations across 8 ScanNet++ [17] scenes, along with open-vocabulary text descriptions.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Nevertheless, there are limitations to the geometrical segmentation method we employ for part segmentation, as it relies on surface normals. | p. 7 (V. EXPERIMENTS) |
| body limitation/failure cue | Discussion and Limitations One limitation of our work is the reliance on a simple geometrical over-segmentation method for identifying object parts. | p. 7 (V. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| VIII, we present a runtime analysis of our method. | p. 7 (V. EXPERIMENTS) |
| To assess the capabilities of our method on open-vocabulary segmentation with a focus on concepts other than object or part semantic categories, we present ... | p. 7 (V. EXPERIMENTS) |
| For each object and part node, we compute open-vocabulary features enabling 3D segmentation across all levels. | p. 2 (I. INTRODUCTION) |
| Object-centric open-vocabulary 3D segmentation methods typically first extract a set of class-agnostic 3D object instance masks and then compute a feature representation per object, ... | p. 2 (I. INTRODUCTION) |
| So far, we have computed scene entities hierarchically using a geometric representation of 3D object instances and their segments. | p. 3 (2) Computing open-vocabulary features for the scene repre) |
| Instead of segmenting the entire scene using this geometric segmentation approach, we use the previously computed object masks M to segment each instance individually. | p. 3 (2) Computing open-vocabulary features for the scene repre) |
| III-A, semantic features are explicitly computed at two levels: objects and part segments as illustrated in Fig. | p. 4 (2) Computing open-vocabulary features for the scene repre) |
| These crops are encoded into image embedding vectors of dimension D = 1152 using the SigLIP [32] image encoder (So-400m). | p. 4 (2) Computing open-vocabulary features for the scene repre) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / V. EXPERIMENTS - extractive body cue:** Nevertheless, there are limitations to the geometrical segmentation method we employ for part segmentation, as it relies on surface normals.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Discussion and Limitations One limitation of our work is the reliance on a simple geometrical over-segmentation method for identifying object parts.

- **Evidence anchors reviewed:** datasets p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), metrics p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), baselines p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 5 (Figure/Table caption), p. 7 (V. EXPERIMENTS), results p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 2 (Figure/Table caption), p. 7 (V. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
