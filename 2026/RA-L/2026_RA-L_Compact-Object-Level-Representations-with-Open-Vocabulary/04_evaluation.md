# Evaluation - Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.24767; PDF retrieval source: https://arxiv.org/pdf/2606.24767. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS)): V, it can be seen that our method can still outperform GoReloc in both success rate and accuracy.

## Evaluation Body Digest

- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Experiments on these two datasets illustrate the capability of our system in handling complex real-world scenes, boosting the practicality of object-level camera relocalization.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** In the single-room case, we utilize two real-world RGB-D indoor datasets: ScanNet [9] and ScanNet++ [10].
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** This table shows average metrics over multi-room/floor scenes of the Synthetic dataset.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** They contain rich object categories and diverse scenes without temporal changes, but only provide sequential frames with high visual overlap.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** These ScanNet and ScanNet++ scenes are captured from the real world, where rich object diversity falls beyond the closed-vocabulary scope of GoReloc.
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Scenes used in our experiments all exhibit a long-tail object distribution.
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** As such, it does not demand strict realtime performance but places greater emphasis on success rate and accuracy.
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Unlike GoReloc, which excessively prioritizes high efficiency at the cost of system performance, ours and PixLoc strike a more balanced trade-off among success rate, accuracy, ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | V, it can be seen that our method can still outperform GoReloc in both success rate and accuracy. | p. 6 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 6: Open-vocabulary Object Matching. Open-vocabulary object-level mapping allows us to recognize diverse objects. methods achieve comparable efficiency. The relocalization module typically serves as ... | p. 7 (Figure/Table caption) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In this section, we describe our experimental setup and validate that our system can achieve significant improvements in relocalization performance. | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Unlike GoReloc, which excessively prioritizes high efficiency at the cost of system performance, ours and PixLoc strike a more balanced trade-off among success rate, ... | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Similarly, our system still achieves better relocalization performance, and the high-quality sensor data in ScanNet++ further facilitates higher pose accuracy (MTE and MRE) of ... | p. 6 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Experiments on these two datasets illustrate the capability of our system in handling complex real-world scenes, boosting the practicality of object-level camera relocalization.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** In the single-room case, we utilize two real-world RGB-D indoor datasets: ScanNet [9] and ScanNet++ [10].
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** This table shows average metrics over multi-room/floor scenes of the Synthetic dataset.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** They contain rich object categories and diverse scenes without temporal changes, but only provide sequential frames with high visual overlap.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** These ScanNet and ScanNet++ scenes are captured from the real world, where rich object diversity falls beyond the closed-vocabulary scope of GoReloc.
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Scenes used in our experiments all exhibit a long-tail object distribution.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: OpenReLoc, an open-vocabulary visual relocalization system, can achieve robust and accurate relocalization performance on various indoor scenes, based on an object-level map. As ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: System Overview. Our system includes three main steps: (1) Object-oriented Mapping. We construct an object-level map from an RGB-D sequence and its 2D ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3: Subgraph Similarity. We seek an assignment among all possible neighbor pairs to maximize the total matching score as the subgraph similarity. negatively impacting ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4: DIOU Metric. (Left) DIOU calculation. (Right) A case illustrates the intention behind the DIOU metric. where bq and br represent 2D bounding box ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 5: Qualitative visualization. We qualitatively show relocalization poses and their ground truth on various scenes. TABLE III: Recall and Accuracy on Synthetic. Each cell ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 6: Open-vocabulary Object Matching. Open-vocabulary object-level mapping allows us to recognize diverse objects. methods achieve comparable efficiency. The relocalization module typically serves as an ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 7: Lighting Variation. We display the scene appearance under progressive illumination decay. Et: 0.06m Er: 1.44° Et: 0.18m Er: 4.76° Et: 0.21m Er: 4.41° ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 8: Object Displacement. We displaced several objects in synthetic scenes and evaluated quantitative metrics. F. Robustness Analysis Object-level approaches are inherently robust to environ- ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Experiments on these two datasets illustrate the capability of our system in handling complex real-world scenes, boosting the practicality of object-level camera relocalization. | embodiment, simulator version and control stack | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | In the single-room case, we utilize two real-world RGB-D indoor datasets: ScanNet [9] and ScanNet++ [10]. | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| As such, it does not demand strict realtime performance but places greater emphasis on success rate and accuracy. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Unlike GoReloc, which excessively prioritizes high efficiency at the cost of system performance, ours and PixLoc strike a more balanced trade-off among success rate, ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| A relocalization system is most concerned about its success rate and pose accuracy. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| V, it can be seen that our method can still outperform GoReloc in both success rate and accuracy. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| It is clear that our system surpasses all other baselines with a notable margin in both success rate and accuracy. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Fig. 1: OpenReLoc, an open-vocabulary visual relocalization system, can achieve robust and accurate relocalization performance on various indoor scenes, based on an object-level map. ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| With respect to success rate, we count the percentage of correctly relocalized query images within given translation thresholds: 50cm and 25cm, i.e., Recall[%] at ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 3: Subgraph Similarity. We seek an assignment among all possible neighbor pairs to maximize the total matching score as the subgraph similarity. negatively ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Therefore, our main comparison is to GoReloc [6], an open-source and SOTA object-level baseline, which shares the most relevant problem formulation with ours. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| Additionally, we also include several low-level vision methods [1]-[4] as additional baselines for completeness. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| III, our system exhibits robustness in this large-scale setting, excelling all baselines. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| V, it can be seen that our method can still outperform GoReloc in both success rate and accuracy. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Map Size Analysis We also report the map memory consumption of different baselines on the ScanNet ‘0568' scene in Tab. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| VII, where object-level methods (GoReloc [6] and Ours) can construct a more compact map compared to low-level vision methods. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| They contain rich object categories and diverse scenes without temporal changes, but only provide sequential frames with high visual overlap. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Ablation Study To verify the rationality of our main module designs, we conduct ablation studies on different datasets in Tab. | component/input/data sensitivity | p. 7 (3.5 MB) |
| Removing either stage inevitably degrades performance, highlighting contributions and complementary roles of these two stages. | component/input/data sensitivity | p. 7 (3.5 MB) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Overall, our contributions can be summarized as follows: • We introduce a multi-modal landmark association module that combines open-vocabulary object descriptors with a global ... | V, it can be seen that our method can still outperform GoReloc in both success rate and accuracy. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Primary metric/result | Fig. 6: Open-vocabulary Object Matching. Open-vocabulary object-level mapping allows us to recognize diverse objects. methods achieve comparable efficiency. The relocalization module typically serves as ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We run our system on a desktop equipped with an NVIDIA RTX 4090 GPU.
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Metric PixLoc Ours Object Detection GPT Analysis CLIP Encoding Coarse-to-fine Pose Total Runtime ≈4.5s ≈0.3s ≈4.1s ≈0.2s ≈0.5s ≈5.1s " Gray Toy Dolphin" " Red ...
- **p. 4 / III. METHOD - extractive PDF cue:** Top-k patches with maximal visibility are input into a CLIP visual encoder and an average pooling layer to obtain a multiview CLIP feature f 3d: ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 6: Open-vocabulary Object Matching. Open-vocabulary object-level mapping allows us to recognize diverse objects. methods achieve comparable efficiency. The relocalization module typically serves as ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Such a distribution falls beyond the scope of closed-vocabulary methods, leading to their failure. | p. 7 (IV. EXPERIMENTS) |
| body limitation/failure cue | IV show that ORB-SLAM2 experienced failure, succeeding on very few frames, despite achieving better accuracy. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | As a result, GoReloc fails to identify valid matching objects in many observations. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | Fig. 1: OpenReLoc, an open-vocabulary visual relocalization system, can achieve robust and accurate relocalization performance on various indoor scenes, based on an object-level map. ... | p. 2 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We run our system on a desktop equipped with an NVIDIA RTX 4090 GPU. | p. 5 (IV. EXPERIMENTS) |
| We set the learning rate of {q, T} to {0.025, 0.025} in the refined pose optimization. | p. 5 (IV. EXPERIMENTS) |
| We compare per-frame runtime with PixLoc and report our runtime breakdown in Tab. | p. 6 (IV. EXPERIMENTS) |
| Per-frame runtime and a detailed breakdown of ours at different stages. | p. 7 (IV. EXPERIMENTS) |
| Metric PixLoc Ours Object Detection GPT Analysis CLIP Encoding Coarse-to-fine Pose Total Runtime ≈4.5s ≈0.3s ≈4.1s ≈0.2s ≈0.5s ≈5.1s " Gray Toy Dolphin" " ... | p. 7 (IV. EXPERIMENTS) |
| Then, as in [15], we predict 2D mask proposals on RGB images as nodes and compute their multi-view consensus as edge affinity. | p. 3 (III. METHOD) |
| They are considered invalid or even negative and should be discarded in subsequent steps. | p. 4 (III. METHOD) |
| Recent progress suggested that the advanced CLIP model can work as an effective object descriptor encoder [7]. | p. 4 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 6: Open-vocabulary Object Matching. Open-vocabulary object-level mapping allows us to recognize diverse objects. methods achieve comparable efficiency. The relocalization module typically serves as an ...
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Such a distribution falls beyond the scope of closed-vocabulary methods, leading to their failure.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** IV show that ORB-SLAM2 experienced failure, succeeding on very few frames, despite achieving better accuracy.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** As a result, GoReloc fails to identify valid matching objects in many observations.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: OpenReLoc, an open-vocabulary visual relocalization system, can achieve robust and accurate relocalization performance on various indoor scenes, based on an object-level map. As ...

- **PDF anchors reviewed:** datasets p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), metrics p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), baselines p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), results p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
