# Evaluation - MR-COGraphs: Communication-efficient Multi-Robot Open-vocabulary Mapping System via 3D Scene Graphs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2412.18381; PDF retrieval source: https://arxiv.org/pdf/2412.18381. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS)): Compared to baseline methods, our approach not only maintains high accuracy and query success rates but also ensures realtime performance in the mapping system.

## Evaluation Body Digest

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Map Merging Evaluation 1) Dataset: Since the Replica dataset lacks multi-room scenes suitable for collaborative mapping [22] (only apartment2 is available), we construct two additional ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Open-vocabulary 3D Scene Graphs Evaluation 1) Dataset: The Replica dataset [32] has been widely used in studies related to 3D scene reconstruction and object retrieval.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** It comprises 18 indoor environments, from which we select three representative scenes (room0, office2, and apartment2) due to their substantial size and rich semantic diversity.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** demonstrate that our feature compression process does not compromise the object finding rate and query success rate across the three evaluated scenes.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** 7b, our real-world environment is 9m × 9m in size with 3 rooms.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Additional real-world demonstrations are available on our website.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Compared to baseline methods, our approach not only maintains high accuracy and query success rates but also ensures realtime performance in the mapping system.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** The topk score is calculated by querying all the 100 semantic texts and averaging the success rate that each image's true annotation is among the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to baseline methods, our approach not only maintains high accuracy and query success rates but also ensures realtime performance in the mapping system. | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show that both domainencode and general-encode achieve performance comparable to raw-clip. domain-encode performs the same with raw-clip when k = 1 while ... | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2) Metrics: We evaluate the accuracy of 3D Scene Graphs using the object finding rate Robj [13], which measures the proportion of object nodes ... | p. 5 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1. Overview of the MR-COGraphs Framework. to the classes of objects annotated in the training datasets [6]. In contrast, open-vocabulary maps are not ... | p. 1 (Figure/Table caption) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This metric evaluates object retrieval capability by considering the top-k most likely objects in 3D Scene Graphs, with the retrieval counted successful if the ... | p. 5 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Map Merging Evaluation 1) Dataset: Since the Replica dataset lacks multi-room scenes suitable for collaborative mapping [22] (only apartment2 is available), we construct two additional ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Open-vocabulary 3D Scene Graphs Evaluation 1) Dataset: The Replica dataset [32] has been widely used in studies related to 3D scene reconstruction and object retrieval.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** It comprises 18 indoor environments, from which we select three representative scenes (room0, office2, and apartment2) due to their substantial size and rich semantic diversity.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** demonstrate that our feature compression process does not compromise the object finding rate and query success rate across the three evaluated scenes.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** 7b, our real-world environment is 9m × 9m in size with 3 rooms.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Additional real-world demonstrations are available on our website.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Overview of the MR-COGraphs Framework. to the classes of objects annotated in the training datasets [6]. In contrast, open-vocabulary maps are not constrained ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. The Generation Process of COGraphs. projecting 2D semantic features onto 3D points and then encoding features into points [7] [8], instances [12] [28], ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Comparison of the original and decoded features when the encoder and decoder are trained on household-related images from ImageNet. same way as existing ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. COGraphs Merging. is functional for downstream tasks, the precision of the merging method is not a critical requirement. 1) Place Recognition: The feature ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. Feature Compression Evaluation. As illustrated in Fig. 5a, we compare the performance of the three encoding configurations with raw-clip, which directly uses the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. Cosine Similarity between Text Features and Image Features (before feature encoding and after feature decoding). TABLE III MAP MERGING EVALUATION Scene Dimension Pose ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7. Experiment Environments and Visualization of the COGraph. TABLE IV

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Map Merging Evaluation 1) Dataset: Since the Replica dataset lacks multi-room scenes suitable for collaborative mapping [22] (only apartment2 is available), we construct two ... | embodiment, simulator version and control stack | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | Open-vocabulary 3D Scene Graphs Evaluation 1) Dataset: The Replica dataset [32] has been widely used in studies related to 3D scene reconstruction and object ... | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Compared to baseline methods, our approach not only maintains high accuracy and query success rates but also ensures realtime performance in the mapping system. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| The topk score is calculated by querying all the 100 semantic texts and averaging the success rate that each image's true annotation is among ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| 2) Metrics: We evaluate the accuracy of 3D Scene Graphs using the object finding rate Robj [13], which measures the proportion of object nodes ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| In this section, we 1) conduct experimental evaluations comparing our approach with state-of-the-art methods (Section IVA), 2) analyze the open-vocabulary capabilities and design insights ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 3. Comparison of the original and decoded features when the encoder and decoder are trained on household-related images from ImageNet. same way as ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 6. Cosine Similarity between Text Features and Image Features (before feature encoding and after feature decoding). TABLE III MAP MERGING EVALUATION Scene Dimension ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Real-world Performance Evaluation As illustrated in Fig. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Fig. 2. The Generation Process of COGraphs. projecting 2D semantic features onto 3D points and then encoding features into points [7] [8], instances [12] ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to baseline methods, our approach not only maintains high accuracy and query success rates but also ensures realtime performance in the mapping system. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Compared to a merging approach without feature compression, the increase in translation estimation error is minimal. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| 3) Baselines: We compare our approach with ConceptGraphs [9] and HOV-SG [11]. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| It is worth noting that our lightweight feature compression model has a size of only 1.61 MB, which is substantially smaller than the map ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| This demonstrates that our method effectively reduces communication data volume without compromising mapping performance. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| Fig. 1. Overview of the MR-COGraphs Framework. to the classes of objects annotated in the training datasets [6]. In contrast, open-vocabulary maps are not ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We also test COGraph-512, a variant of our method without feature compression. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| This demonstrates that our method effectively reduces communication data volume without compromising mapping performance. | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |
| Since our text queries do not include complex negation or multi-step affordances, we run ConceptGraphs without GPT. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Compared to a merging approach without feature compression, the increase in translation estimation error is minimal. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| 5a, we compare the performance of the three encoding configurations with raw-clip, which directly uses the 512-dimensional CLIP feature without encoding and decoding process. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| Fig. 1. Overview of the MR-COGraphs Framework. to the classes of objects annotated in the training datasets [6]. In contrast, open-vocabulary maps are not ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To fulfill the requirements above, we propose a Communication-efficient Multi-Robot Open-vocabulary 3D Scene Graphs-based Mapping (MR-COGraphs) System with the following contributions: • A data-efficient ... | Compared to baseline methods, our approach not only maintains high accuracy and query success rates but also ensures realtime performance in the mapping system. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Primary metric/result | The results show that both domainencode and general-encode achieve performance comparable to raw-clip. domain-encode performs the same with raw-clip when k = 1 while ... | numeric claim only at cited anchor | p. 6 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Experiments in Section IV are conducted on a desktop PC equipped with an Intel I7-13700 CPU and an Nvidia RTX 4080 GPU.
- **p. 4 / III. METHOD - extractive body cue:** To address this, we compress the features into 3 dimensions using a lightweight feature encoder.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | demonstrate that our feature compression process does not compromise the object finding rate and query success rate across the three evaluated scenes. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | 2) Metrics: Unlike multi-robot SLAM, our localization module relies on a ready-made SLAM algorithm, and the graph-structured map does not require high geometric precision. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | Fig. 3. Comparison of the original and decoded features when the encoder and decoder are trained on household-related images from ImageNet. same way as ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | In this section, we 1) conduct experimental evaluations comparing our approach with state-of-the-art methods (Section IVA), 2) analyze the open-vocabulary capabilities and design insights ... | p. 5 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The training parameters are set as follows: epochs = 5000, batch size = 1920, and learning rate = 0.0001. | p. 6 (IV. EXPERIMENTS) |
| Experiments in Section IV are conducted on a desktop PC equipped with an Intel I7-13700 CPU and an Nvidia RTX 4080 GPU. | p. 5 (IV. EXPERIMENTS) |
| To compute this metric, we evaluate the encoder and decoder on the Replica dataset by collecting 568 images annotated with 100 semantic categories. | p. 6 (IV. EXPERIMENTS) |
| Additionally, we record the average runtime per frame (tpf), and the total map volume. | p. 5 (IV. EXPERIMENTS) |
| 6b illustrates the matching results of the image features before and after applying the encoder and decoder. | p. 7 (IV. EXPERIMENTS) |
| We run our framework on the desktop PC (mentioned in Section IV-A) and we also test it on the Nvidia Orin NX platform. | p. 7 (IV. EXPERIMENTS) |
| The loss function combines L2 loss and cosine similarity loss between the original feature f raw i,512 and the reconstructed 512-dimensional features f decode ... | p. 4 (III. METHOD) |
| 2, given a sequence of RGB-D images, we run an open-vocabulary segmentation model to obtain the segmented objects in each frame. | p. 3 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** demonstrate that our feature compression process does not compromise the object finding rate and query success rate across the three evaluated scenes.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** 2) Metrics: Unlike multi-robot SLAM, our localization module relies on a ready-made SLAM algorithm, and the graph-structured map does not require high geometric precision.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Comparison of the original and decoded features when the encoder and decoder are trained on household-related images from ImageNet. same way as existing ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In this section, we 1) conduct experimental evaluations comparing our approach with state-of-the-art methods (Section IVA), 2) analyze the open-vocabulary capabilities and design insights of ...

- **Evidence anchors reviewed:** datasets p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), metrics p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 1 (Figure/Table caption), results p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
