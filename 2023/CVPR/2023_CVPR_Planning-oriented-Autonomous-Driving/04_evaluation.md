# Evaluation - Planning-oriented Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2212.10156; PDF retrieval source: https://arxiv.org/pdf/2212.10156. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (3.3. Qualitative Results), p. 6 (Figure/Table caption), p. 6 (3.2. Modular Results), p. 7 (3.3. Qualitative Results), p. 21 (Figure/Table caption), p. 8 (Figure/Table caption)): UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, verifying the safety of our system.

## Evaluation Body Digest

- **p. 6 / 3. Experiments - extractive body cue:** We conduct experiments on the challenging nuScenes dataset [6].
- **p. 6 / 3.2. Modular Results - extractive body cue:** Following the sequential order of perception-predictionplanning, we report the performance of each task module in comparison to prior state-of-the-arts on the nuScenes validation set.
- **p. 7 / 3.3. Qualitative Results - extractive body cue:** In the Supplementary, we show more visualizations of challenging scenarios and one promising case for the planning-oriented design, that inaccurate results occur in prior modules ...
- **p. 7 / 3.3. Qualitative Results - extractive body cue:** 3 visualizes the results of all tasks for one complex scene.
- **p. 7 / 3.3. Qualitative Results - extractive body cue:** UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, verifying the safety ...
- **p. 7 / 3.3. Qualitative Results - extractive body cue:** Anch." denotes rotated scene-level anchors. "Goal Inter." means the agent-goal point interaction. "Ego Q" represents the egovehicle query and "NLO." is the non-linear optimization strategy. ...
- **p. 6 / 3.2. Modular Results - extractive body cue:** Moreover, UniAD achieves the lowest ID switch score, showing its temporal consistency for each tracklet.
- **p. 6 / 3.2. Modular Results - extractive body cue:** For online mapping in Table 4, UniAD performs well on segmenting lanes (+7.4 IoU(%) compared to BEVFormer), which is crucial for downstream agentroad interaction in ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3. Experiments (p. 6); 3.1. Joint Results (p. 6); 3.2. Modular Results (p. 6); 3.3. Qualitative Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3.3. Qualitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, verifying the ... | p. 7 (3.3. Qualitative Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2. Detailed ablations on the effectiveness of each task. We can conclude that two perception sub-tasks greatly help motion forecasting, and prediction performance ... | p. 6 (Figure/Table caption) |
| 3.2. Modular Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Moreover, UniAD achieves the lowest ID switch score, showing its temporal consistency for each tracklet. | p. 6 (3.2. Modular Results) |
| 3.3. Qualitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | UniAD gets significant improvement in nearby areas, which are more critical for planning. "n." and "f." indicates near (30×30m) and far (50×50m) evaluation ranges ... | p. 7 (3.3. Qualitative Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 13. Computational complexity and runtime with different modules incorporated. ID.1 is similar to original BEVFormer [55], and ID. 0 (BEVerse-Tiny) [105] is an ... | p. 21 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 3. Experiments - extractive body cue:** We conduct experiments on the challenging nuScenes dataset [6].
- **p. 6 / 3.2. Modular Results - extractive body cue:** Following the sequential order of perception-predictionplanning, we report the performance of each task module in comparison to prior state-of-the-arts on the nuScenes validation set.
- **p. 7 / 3.3. Qualitative Results - extractive body cue:** In the Supplementary, we show more visualizations of challenging scenarios and one promising case for the planning-oriented design, that inaccurate results occur in prior modules ...
- **p. 7 / 3.3. Qualitative Results - extractive body cue:** 3 visualizes the results of all tasks for one complex scene.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison on the various designs of autonomous driving framework. (a) Most industrial solutions deploy separate models for different tasks. (b) The multi-task learning ...
- **p. 2 / Figure/Table caption - extractive body cue:** Table 1. Tasks comparison and taxonomy. "Design" column is classified as in Fig. 1. "Det." denotes 3D object detection, "Map" stands for online mapping, and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Pipeline of Unified Autonomous Driving (UniAD). It is exquisitely devised following planning-oriented philosophy. Instead of a simple stack of tasks, we investigate the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Detailed ablations on the effectiveness of each task. We can conclude that two perception sub-tasks greatly help motion forecasting, and prediction performance also ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Multi-object tracking. UniAD outperforms previ- ous end-to-end MOT techniques (with image inputs only) on all metrics. †: Tracking-by-detection method with post-association, reimplemented with ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Online mapping. UniAD achieves competitive perfor- mance against state-of-the-art perception-oriented methods, with comprehensive road semantics. We report segmentation IoU (%). †: Reimplemented with ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Motion forecasting. UniAD remarkably outperforms previous vision-based end-to-end methods. We also report two settings of modeling vehicles with constant positions or velocities as ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 6. Occupancy prediction. UniAD gets significant improve- ment in nearby areas, which are more critical for planning. "n." and "f." indicates near (30×30m) and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct experiments on the challenging nuScenes dataset [6]. | embodiment, simulator version and control stack | p. 6 (3. Experiments), p. 6 (3.2. Modular Results) |
| Task/environment | Following the sequential order of perception-predictionplanning, we report the performance of each task module in comparison to prior state-of-the-arts on the nuScenes validation set. | reset, timeout, object/scene variation | p. 6 (3.2. Modular Results), p. 7 (3.3. Qualitative Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (2. Methodology), p. 3 (2. Methodology) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (2. Methodology), p. 2 (2. Methodology) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, verifying the ... | definition/direction/unit from same section | p. 7 (3.3. Qualitative Results) |
| Anch." denotes rotated scene-level anchors. "Goal Inter." means the agent-goal point interaction. "Ego Q" represents the egovehicle query and "NLO." is the non-linear optimization ... | definition/direction/unit from same section | p. 7 (3.3. Qualitative Results) |
| Moreover, UniAD achieves the lowest ID switch score, showing its temporal consistency for each tracklet. | definition/direction/unit from same section | p. 6 (3.2. Modular Results) |
| For online mapping in Table 4, UniAD performs well on segmenting lanes (+7.4 IoU(%) compared to BEVFormer), which is crucial for downstream agentroad interaction ... | definition/direction/unit from same section | p. 6 (3.2. Modular Results) |
| Table 13. Computational complexity and runtime with different modules incorporated. ID.1 is similar to original BEVFormer [55], and ID. 0 (BEVerse-Tiny) [105] is an ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Table 10. Ablation for designs in the planning module. Results demonstrate the necessity of each preceding task. "BEV Att." in- dicates attending to BEV ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 12. Visualization for planning recovering from perception failures. We show an interesting case where inaccurate results occur in prior modules while the later ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Figure 8. Effectiveness of navigation command and attention mask visualization. Here we demonstrate how attention is paid in accordance with the navigation command. We ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The first row (ID-0) serves as a vanilla multi-task baseline with separate task heads for comparison. | comparison identity and matched condition | p. 6 (3.1. Joint Results) |
| Following the sequential order of perception-predictionplanning, we report the performance of each task module in comparison to prior state-of-the-arts on the nuScenes validation set. | comparison identity and matched condition | p. 6 (3.2. Modular Results) |
| UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, verifying the ... | comparison identity and matched condition | p. 7 (3.3. Qualitative Results) |
| Table 3. Multi-object tracking. UniAD outperforms previ- ous end-to-end MOT techniques (with image inputs only) on all metrics. †: Tracking-by-detection method with post-association, reimplemented ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 1. Comparison on the various designs of autonomous driving framework. (a) Most industrial solutions deploy separate models for different tasks. (b) The multi-task ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Table 1. Tasks comparison and taxonomy. "Design" column is classified as in Fig. 1. "Det." denotes 3D object detection, "Map" stands for online mapping, ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct extensive ablations as shown in Table 2 to prove the effectiveness and necessity of preceding tasks in the end-to-end pipeline. | component/input/data sensitivity | p. 6 (3.1. Joint Results) |
| In this section, we validate the effectiveness of our design in three aspects: joint results revealing the advantage of task coordination and its effect ... | component/input/data sensitivity | p. 6 (3. Experiments) |
| Table 8. Ablation for designs in the motion forecasting module. All components contribute to the ultimate performance. "Scene- l. Anch." denotes rotated scene-level anchors. ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 2. Pipeline of Unified Autonomous Driving (UniAD). It is exquisitely devised following planning-oriented philosophy. Instead of a simple stack of tasks, we investigate ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Table 9. Ablation for designs in the occupancy prediction mod- ule. Cross-attention with masks and the reuse of mask feature helps improve the prediction. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 10. Ablation for designs in the planning module. Results demonstrate the necessity of each preceding task. "BEV Att." in- dicates attending to BEV ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address this, we present OccFormer to incorporate both scene-level and agent-level semantics in two aspects: (1) a dense scene feature acquires agent-level features ... | UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, verifying the ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (3.3. Qualitative Results), p. 6 (Figure/Table caption), p. 6 (3.2. Modular Results), p. 7 (3.3. Qualitative Results), p. 21 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | Table 2. Detailed ablations on the effectiveness of each task. We can conclude that two perception sub-tasks greatly help motion forecasting, and prediction performance ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 3.3. Qualitative Results - extractive body cue:** UniAD gets significant improvement in nearby areas, which are more critical for planning. "n." and "f." indicates near (30×30m) and far (50×50m) evaluation ranges respectively. ...
- **p. 5 / 2.5. Learning - extractive body cue:** We first jointly train perception parts, i.e., the tracking and mapping modules, for a few epochs (6 in our experiments), and then train the model ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 14. Failure cases 2. In this case, the planner is over-cautious about the incoming vehicle in the narrow street. The dark environment is ... | p. 24 (Figure/Table caption) |
| body limitation/failure cue | Figure 13. Failure cases 1. Here we present a long-tail scenario, where a large trailer with a white container occupies the entire road. We ... | p. 24 (Figure/Table caption) |
| body limitation/failure cue | Besides, we analyze that failure cases of UniAD are mainly under some long-tail scenarios such as large trucks and trailers, shown in the Supplementary ... | p. 7 (3.3. Qualitative Results) |
| body limitation/failure cue | In Exp.1012, only when the two tasks are introduced simultaneously (Exp.12), both metrics of the planning L2 and collision rate achieve the best results, ... | p. 6 (3.1. Joint Results) |
| body limitation/failure cue | UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, verifying the ... | p. 7 (3.3. Qualitative Results) |
| body limitation/failure cue | Table 10. Ablation for designs in the planning module. Results demonstrate the necessity of each preceding task. "BEV Att." in- dicates attending to BEV ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 2, UniAD comprises four transformer decoder-based perception and prediction modules and one planner in the end. | p. 2 (2. Methodology) |
| Note that UniAD is not confined to a specific BEV encoder, and one can utilize other alternatives to extract richer BEV representations with long-term ... | p. 2 (2. Methodology) |
| We sparsely represent road elements as map queries to help downstream motion forecasting, with location and structure knowledge encoded. | p. 3 (2. Methodology) |
| All perception and prediction modules are designed in a transformer decoder structure, with task queries as interfaces connecting each node. | p. 3 (2. Methodology) |
| Then, Qctx is sent to the successive layer for refinement or decoded as prediction results at the last layer. | p. 4 (2. Methodology) |
| &\text {MLP}(\text {PE}(I^s)) + \text {MLP}(\text {PE}(I^a)) \\ +\ &\text {MLP}(\text {PE}(\hat {\mathbf {x}}_0)) + \text {MLP}(\text {PE}(\hat {\mathbf {x}}_T^{l-1})). \end {aligned} (3) Here ... | p. 4 (2. Methodology) |
| (11) Here λcoord, λobs, and σ are hyperparameters, and t indexes a timestep of future horizons. | p. 5 (2.4. Planning) |
| We attend plan query to BEV features B to make it aware of surroundings, and then decode it to future waypoints ˆτ. | p. 5 (2.4. Planning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 24 / Figure/Table caption - extractive body cue:** Figure 14. Failure cases 2. In this case, the planner is over-cautious about the incoming vehicle in the narrow street. The dark environment is one ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 13. Failure cases 1. Here we present a long-tail scenario, where a large trailer with a white container occupies the entire road. We can ...
- **p. 7 / 3.3. Qualitative Results - extractive body cue:** Besides, we analyze that failure cases of UniAD are mainly under some long-tail scenarios such as large trucks and trailers, shown in the Supplementary as ...
- **p. 6 / 3.1. Joint Results - extractive body cue:** In Exp.1012, only when the two tasks are introduced simultaneously (Exp.12), both metrics of the planning L2 and collision rate achieve the best results, compared ...
- **p. 7 / 3.3. Qualitative Results - extractive body cue:** UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, verifying the safety ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 10. Ablation for designs in the planning module. Results demonstrate the necessity of each preceding task. "BEV Att." in- dicates attending to BEV feature. ...

- **Evidence anchors reviewed:** datasets p. 6 (3. Experiments), p. 6 (3.2. Modular Results), p. 7 (3.3. Qualitative Results), p. 7 (3.3. Qualitative Results), metrics p. 7 (3.3. Qualitative Results), p. 7 (3.3. Qualitative Results), p. 6 (3.2. Modular Results), p. 6 (3.2. Modular Results), p. 21 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 6 (3.1. Joint Results), p. 6 (3.2. Modular Results), p. 7 (3.3. Qualitative Results), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption), results p. 7 (3.3. Qualitative Results), p. 6 (Figure/Table caption), p. 6 (3.2. Modular Results), p. 7 (3.3. Qualitative Results), p. 21 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
