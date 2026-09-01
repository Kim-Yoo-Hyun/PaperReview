# Evaluation - Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v87/florence18a.html; PDF retrieval source: https://proceedings.mlr.press/v87/florence18a.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5 Results), p. 6 (5 Results), p. 7 (5 Results), p. 6 (5 Results), p. 3 (Figure/Table caption)): For the most part, 3dimensional descriptor spaces were sufficient to achieve saturated (did not improve with higher-dimension) correspondence precision for single objects, yet this is often not the case for ...

## Evaluation Body Digest

- **p. 6 / 5 Results - extractive body cue:** The dataset used for (a) is of three objects, 4 scenes each.
- **p. 8 / 5 Results - extractive body cue:** For instance-specificity (iv) trained with specific and augmented with synthetic multi object scenes (3.3.iii), the robot grasps this point on the specific instance even in ...
- **p. 6 / 5 Results - extractive body cue:** (b) shows that for a dataset containing 10 scenes of a drill, learned descriptors are inconsistent without background and orientation randomization during training (middle), but ...
- **p. 8 / 5 Results - extractive body cue:** Now the robot has the ability to autonomously identify the corresponding point in new scenes via Equation 6.
- **p. 5 / 5 Results - extractive body cue:** Objects used • 47 objects total • 275 scenes 8 hats
- **p. 7 / 5 Results - extractive body cue:** All networks were trained on the same 3 object dataset.
- **p. 7 / 5 Results - extractive body cue:** 5.4 Example Applications to Robotic Manipulation: Grasping Specific Points Here we demonstrate a variety of manipulation applications in grasping specific points on objects, where the ...
- **p. 5 / 5 Results - extractive body cue:** Our object set is also summarized (right).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 Results (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | For the most part, 3dimensional descriptor spaces were sufficient to achieve saturated (did not improve with higher-dimension) correspondence precision for single objects, yet this ... | p. 7 (5 Results) |
| 5 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our new standard single-object training procedure (standard-SO) performs significantly better than our implementation of prior work's training procedures (Schmidt), and we isolate and measure ... | p. 6 (5 Results) |
| 5 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Given that we can separate objects in descriptor space, we next investigate: does the introduction of object distinctness significantly limit the ability of the ... | p. 7 (5 Results) |
| 5 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | The techniques in Section 3.2 provide significant improvement in both (a) qualitative consistency over a wide variety of viewpoints, and (b) quantitative precision in ... | p. 6 (5 Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1: Overview of the data collection and training procedure. (a) automated collection with a robot arm. (b) change detection using the dense 3D ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5 Results - extractive body cue:** The dataset used for (a) is of three objects, 4 scenes each.
- **p. 8 / 5 Results - extractive body cue:** For instance-specificity (iv) trained with specific and augmented with synthetic multi object scenes (3.3.iii), the robot grasps this point on the specific instance even in ...
- **p. 6 / 5 Results - extractive body cue:** (b) shows that for a dataset containing 10 scenes of a drill, learned descriptors are inconsistent without background and orientation randomization during training (middle), but ...
- **p. 8 / 5 Results - extractive body cue:** Now the robot has the ability to autonomously identify the corresponding point in new scenes via Equation 6.
- **p. 5 / 5 Results - extractive body cue:** Objects used • 47 objects total • 275 scenes 8 hats
- **p. 7 / 5 Results - extractive body cue:** All networks were trained on the same 3 object dataset.
- **p. 7 / 5 Results - extractive body cue:** 5.4 Example Applications to Robotic Manipulation: Grasping Specific Points Here we demonstrate a variety of manipulation applications in grasping specific points on objects, where the ...
- **p. 5 / 5 Results - extractive body cue:** Our object set is also summarized (right).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: Overview of the data collection and training procedure. (a) automated collection with a robot arm. (b) change detection using the dense 3D reconstruction. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Learned object descriptors can be consistent across significant deformation (a) and, if desired, across object classes (b-d). Shown for each (a) and (b-d) ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: (a) table describing the network training procedures referenced in experiments. (standard-SO = "standard single object". standard-SO-P is detailed in Appendix D.1). (b) Plots ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (a), with same axes as Figure 3b, compares standard-SO with without-DR, for which the only difference is that without-DR used no background domain ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Comparison of training without any distinct object loss (a) vs. using cross-object loss (b). In (b), 50% of training iterations applied cross-object loss ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Depiction of "grasp specific point" demonstrations. For each the user specifies a pixel in a single reference image, and the robot automatically grasps ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 7: (a) Kuka IIWA LRB robot arm. (b) Schunk WSG 50 gripper with Primesense Carmine 1.09 attached Appendix A Experimental Hardware All of our ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset used for (a) is of three objects, 4 scenes each. | embodiment, simulator version and control stack | p. 6 (5 Results), p. 8 (5 Results) |
| Task/environment | For instance-specificity (iv) trained with specific and augmented with synthetic multi object scenes (3.3.iii), the robot grasps this point on the specific instance even ... | reset, timeout, object/scene variation | p. 8 (5 Results), p. 6 (5 Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3 Methodology), p. 5 (3 Methodology) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3 Methodology), p. 3 (3 Methodology) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| By applying cross-object loss (Section 3.3.i, training mode specific in Figure 3a), we can convincingly separate multiple objects such that they each occupy distinct ... | definition/direction/unit from same section | p. 7 (5 Results) |
| Given that we can separate objects in descriptor space, we next investigate: does the introduction of object distinctness significantly limit the ability of the ... | definition/direction/unit from same section | p. 7 (5 Results) |
| The variety of objects includes moderately deformable objects such as soft plush toys, shoes, mugs, and hats, and can include very low-texture objects (Figure ... | definition/direction/unit from same section | p. 5 (5 Results) |
| Accordingly we sought to answer the question of whether or not we could separate these objects into unique parts of descriptor space. | definition/direction/unit from same section | p. 6 (5 Results) |
| The techniques in Section 3.2 provide significant improvement in both (a) qualitative consistency over a wide variety of viewpoints, and (b) quantitative precision in ... | definition/direction/unit from same section | p. 6 (5 Results) |
| Figure 7: (a) Kuka IIWA LRB robot arm. (b) Schunk WSG 50 gripper with Primesense Carmine 1.09 attached Appendix A Experimental Hardware All of ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| without cross-object loss with cross-object loss (a) (b) (c) Figure 5: Comparison of training without any distinct object loss (a) vs. using cross-object loss ... | comparison identity and matched condition | p. 7 (5 Results) |
| Our new standard single-object training procedure (standard-SO) performs significantly better than our implementation of prior work's training procedures (Schmidt), and we isolate and measure ... | comparison identity and matched condition | p. 6 (5 Results) |
| (b) shows that for a dataset containing 10 scenes of a drill, learned descriptors are inconsistent without background and orientation randomization during training (middle), ... | comparison identity and matched condition | p. 6 (5 Results) |
| Networks with a number label were trained with cross object loss and the number denotes the descriptor dimension. no-cross-object is a network trained without ... | comparison identity and matched condition | p. 7 (5 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 5.1 Single-Object Dense Descriptors We observe that with our training procedures described in Section 3.2, for a wide variety of objects we can acquire ... | component/input/data sensitivity | p. 5 (5 Results) |
| (b) shows that for a dataset containing 10 scenes of a drill, learned descriptors are inconsistent without background and orientation randomization during training (middle), ... | component/input/data sensitivity | p. 6 (5 Results) |
| Image #1 (cropped) (i) Without orientation and background randomization Image #2 (cropped) (ii) standard-SO inconsistent consistent (a) (b) Figure 4: (a), with same axes ... | component/input/data sensitivity | p. 6 (5 Results) |
| without cross-object loss with cross-object loss (a) (b) (c) Figure 5: Comparison of training without any distinct object loss (a) vs. using cross-object loss ... | component/input/data sensitivity | p. 7 (5 Results) |
| Networks with a number label were trained with cross object loss and the number denotes the descriptor dimension. no-cross-object is a network trained without ... | component/input/data sensitivity | p. 7 (5 Results) |
| The particular novel components of these manipulation demonstrations are in grasping the visual corresponding points for arbitrary pixels that are either in different (potentially ... | component/input/data sensitivity | p. 8 (5 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We believe our largest contribution is that we introduce dense descriptors as a representation useful for robotic manipulation. | For the most part, 3dimensional descriptor spaces were sufficient to achieve saturated (did not improve with higher-dimension) correspondence precision for single objects, yet this ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5 Results), p. 6 (5 Results), p. 7 (5 Results), p. 6 (5 Results), p. 3 (Figure/Table caption) |
| Primary metric/result | Our new standard single-object training procedure (standard-SO) performs significantly better than our implementation of prior work's training procedures (Schmidt), and we isolate and measure ... | numeric claim only at cited anchor | p. 6 (5 Results) |

- Numeric sentences retained from the body:
- **p. 5 / 5 Results - extractive body cue:** Objects used • 47 objects total • 275 scenes 8 hats
- **p. 6 / 5 Results - extractive body cue:** (b) Plots the cdf of the L2 pixel distance (normalized by image diagonal, 800 for a 640 x 480 image) between the best match ˆub ...
- **p. 6 / 5 Results - extractive body cue:** The dataset used for (a) is of three objects, 4 scenes each.
- **p. 6 / 5 Results - extractive body cue:** (b) shows that for a dataset containing 10 scenes of a drill, learned descriptors are inconsistent without background and orientation randomization during training (middle), but ...
- **p. 7 / 5 Results - extractive body cue:** All networks were trained on the same 3 object dataset.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The generalization extends to instances that a priori we thought would be failure modes: we expected the boot (Figure 6h) to be a failure ... | p. 7 (5 Results) |
| body limitation/failure cue | In future work we are interested to explore new approaches to solving manipulation problems that exploit the dense visual information that learned dense descriptors ... | p. 8 (6 Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our new standard single-object training procedure (standard-SO) performs significantly better than our implementation of prior work's training procedures (Schmidt), and we isolate and measure ... | p. 6 (5 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5 Results - extractive body cue:** The generalization extends to instances that a priori we thought would be failure modes: we expected the boot (Figure 6h) to be a failure mode ...
- **p. 8 / 6 Conclusion - extractive body cue:** In future work we are interested to explore new approaches to solving manipulation problems that exploit the dense visual information that learned dense descriptors provide, ...

- **PDF anchors reviewed:** datasets p. 6 (5 Results), p. 8 (5 Results), p. 6 (5 Results), p. 8 (5 Results), p. 5 (5 Results), p. 7 (5 Results), metrics p. 7 (5 Results), p. 7 (5 Results), p. 5 (5 Results), p. 6 (5 Results), p. 6 (5 Results), p. 11 (Figure/Table caption), baselines p. 7 (5 Results), p. 6 (5 Results), p. 6 (5 Results), p. 7 (5 Results), results p. 7 (5 Results), p. 6 (5 Results), p. 7 (5 Results), p. 6 (5 Results), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
