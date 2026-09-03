# Evaluation - Context Graph-based Visual-Language Place Recognition

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2410.19341v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption)): Fig. 5. Correspondence Matching. The results of correspondence matching are visualized as follows: (a) matching results based on ORB features and (b) matching results based on our method. on the ...

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The dataset was acquired using a stereo camera mounted on a moving vehicle and includes real-world image data captured from urban, rural, and motorway scenes.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** These datasets contain numerous dynamic objects, such as cars and pedestrians, as well as changes in illumination and viewpoint.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** A query image is considered accurately localized when at least one of the top N database images returned by the proposed method is within d ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** They were chosen to demonstrate the robustness of our approach in dynamic environments.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. System Overview. The pre-trained text encoder of LSeg is used to generate text embeddings from a pre-defined label set. The visual encoder of ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Context Graph. Each circle represents the centroid of a cluster and serves as a node in the context graph. The graph visualizes the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. Correspondence Matching. The results of correspondence matching are visualized as follows: (a) matching results based on ORB features and (b) matching results based ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** IVB, the quantitative results in Sec.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5. Correspondence Matching. The results of correspondence matching are visualized as follows: (a) matching results based on ORB features and (b) matching results ... | p. 6 (Figure/Table caption) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | IVB, the quantitative results in Sec. | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | IV-C.1 and the qualitative results in Sec. | p. 5 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1. The language-driven semantic segmentation is based on a pre- defined label set. The segmentation results on the KITTI dataset were obtained by ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The dataset was acquired using a stereo camera mounted on a moving vehicle and includes real-world image data captured from urban, rural, and motorway scenes.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** These datasets contain numerous dynamic objects, such as cars and pedestrians, as well as changes in illumination and viewpoint.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. The language-driven semantic segmentation is based on a pre- defined label set. The segmentation results on the KITTI dataset were obtained by correlating ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. System Overview. The pre-trained text encoder of LSeg is used to generate text embeddings from a pre-defined label set. The visual encoder of ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Context Graph. Each circle represents the centroid of a cluster and serves as a node in the context graph. The graph visualizes the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4. Feature Extraction. (a) In the case of using ORB features, keypoints are extracted even from pixels corresponding to dynamic objects such as cars. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. Correspondence Matching. The results of correspondence matching are visualized as follows: (a) matching results based on ORB features and (b) matching results based ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset was acquired using a stereo camera mounted on a moving vehicle and includes real-world image data captured from urban, rural, and motorway ... | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | These datasets contain numerous dynamic objects, such as cars and pedestrians, as well as changes in illumination and viewpoint. | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (III. METHODS), p. 4 (III. METHODS) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (III. METHODS), p. 4 (III. METHODS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| A query image is considered accurately localized when at least one of the top N database images returned by the proposed method is within ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| They were chosen to demonstrate the robustness of our approach in dynamic environments. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 2. System Overview. The pre-trained text encoder of LSeg is used to generate text embeddings from a pre-defined label set. The visual encoder ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 3. Context Graph. Each circle represents the centroid of a cluster and serves as a node in the context graph. The graph visualizes ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1) Quantitative evaluation: We compared our method with the state-of-the-art appearance-based localization approach, NetVLAD [2]. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| Fig. 4. Feature Extraction. (a) In the case of using ORB features, keypoints are extracted even from pixels corresponding to dynamic objects such as ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| Fig. 5. Correspondence Matching. The results of correspondence matching are visualized as follows: (a) matching results based on ORB features and (b) matching results ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

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
| The main contributions of this paper are as follows: • Visual-language vocabulary-based place recognition system: We introduce the concept of Visual-Language Vocabulary to generate ... | Fig. 5. Correspondence Matching. The results of correspondence matching are visualized as follows: (a) matching results based on ORB features and (b) matching results ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption) |
| Primary metric/result | IVB, the quantitative results in Sec. | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We trained a k-nearest neighbors (kNN) model using the coordinates of the database data and calculated distances to query images to find the nearest neighbors ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** A query image is considered accurately localized when at least one of the top N database images returned by the proposed method is within d ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In this paper, we calculated recall for N = 1, 5, 10, 20.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Using the segmentation results, we can filter out dynamic objects that could potentially degrade VPR performance by predefining such categories. | p. 4 (III. METHODS) |
| body limitation/failure cue | They were chosen to demonstrate the robustness of our approach in dynamic environments. | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | 4 illustrates the difference between the prior approach and ours, where our approach filters out dynamic objects, such as cars, that can degrade the ... | p. 5 (III. METHODS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The percentage of correctly localized queries is computed based on the top N database images. | p. 5 (IV. EXPERIMENTS) |
| For the experiments, a subset of this dataset was randomly sampled, and the evaluation code was made publicly available. | p. 5 (IV. EXPERIMENTS) |
| The text encoder embeds the given label set into a vector space, extracting embedding vectors. | p. 3 (III. METHODS) |
| Next, pixel-level embeddings are extracted from the input RGB image using the pre-trained visual encoder of LSeg. | p. 3 (III. METHODS) |
| These are qualitative results showing that the context graph demonstrates greater similarity among visually similar images. embedding vectors T1, ..., TN is computed. | p. 4 (III. METHODS) |
| Additionally, our method uses fewer features compared to ORB, demonstrating an advantage in terms of computing efficiency. of codewords from the generated vocabulary allows ... | p. 4 (III. METHODS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / III. METHODS - extractive body cue:** Using the segmentation results, we can filter out dynamic objects that could potentially degrade VPR performance by predefining such categories.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** They were chosen to demonstrate the robustness of our approach in dynamic environments.
- **p. 5 / III. METHODS - extractive body cue:** 4 illustrates the difference between the prior approach and ours, where our approach filters out dynamic objects, such as cars, that can degrade the performance ...

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), metrics p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 5 (IV. EXPERIMENTS), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption), results p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
