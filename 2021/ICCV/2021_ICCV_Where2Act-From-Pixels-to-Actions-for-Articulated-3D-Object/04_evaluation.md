# Evaluation - Where2Act: From Pixels to Actions for Articulated 3D Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2101.02692; PDF retrieval source: https://arxiv.org/pdf/2101.02692. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Metrics and Baselines), p. 7 (5.2. Metrics and Baselines), p. 1 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments), p. 6 (5.2. Metrics and Baselines)): We observe that 3D-ours achieves the best performance. validates that our network learns geometric features more than local normals and curvatures.

## Evaluation Body Digest

- **p. 5 / 5.1. Framework and Settings - extractive body cue:** Equipped with a large-scale PartNetMobility dataset, SAPIEN [49] provides a physics-rich simulation environment that supports robot actuators interacting with 2,346 3D CAD models from 46 ...
- **p. 5 / 5.1. Framework and Settings - extractive body cue:** We conduct our experiments using 15 selected object categories in the PartNet-Mobility dataset, after removing the objects that are either too small (e.g. pens, USB ...
- **p. 8 / 5.4. Real-world Data - extractive body cue:** We visualize our action scoring predictions given certain gripper orientations over three real-world 3D scans from the Replica dataset [42] and Google Scanned Objects [38, ...
- **p. 6 / 5.1. Framework and Settings - extractive body cue:** At the beginning of each interaction simulation, we initialize the robot gripper slightly above a surface position p of interest approaching from orientation R.
- **p. 6 / 5.2. Metrics and Baselines - extractive body cue:** This metric jointly evaluates all the three network modules and mimics the final use case of proposing meaningful actions when a robot actuator wants to ...
- **p. 8 / 5.4. Real-world Data - extractive body cue:** We directly applied our networks trained on synthetic data to real-world data.
- **p. 7 / 5.3. Results and Analysis - extractive body cue:** Our networks also learn representations that generalize successfully to unseen novel object categories.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The Proposed Where2Act Task. Given as input an ar- ticulated 3D object, we learn to propose the actionable information for different robotic manipulation ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 5); 5.3. Results and Analysis (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Metrics and Baselines | EMPIRICAL / REAL-ROBOT OR HARDWARE | We observe that 3D-ours achieves the best performance. validates that our network learns geometric features more than local normals and curvatures. | p. 7 (5.2. Metrics and Baselines) |
| 5.2. Metrics and Baselines | EMPIRICAL / REAL-ROBOT OR HARDWARE | An ablated version Ours w/o OS further proves the improvement provided by the proposed online adaptive data sampling (OS) strategy. | p. 7 (5.2. Metrics and Baselines) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. The Proposed Where2Act Task. Given as input an ar- ticulated 3D object, we learn to propose the actionable information for different robotic ... | p. 1 (Figure/Table caption) |
| 5. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results also show that the networks learn representations that can generalize to novel unseen object categories and real-world data. | p. 5 (5. Experiments) |
| 5. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We set up an interactive simulation environment in SAPIEN [49] and benchmark performance of the proposed method both qualititively and quantitatively. | p. 5 (5. Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 5.1. Framework and Settings - extractive body cue:** Equipped with a large-scale PartNetMobility dataset, SAPIEN [49] provides a physics-rich simulation environment that supports robot actuators interacting with 2,346 3D CAD models from 46 ...
- **p. 5 / 5.1. Framework and Settings - extractive body cue:** We conduct our experiments using 15 selected object categories in the PartNet-Mobility dataset, after removing the objects that are either too small (e.g. pens, USB ...
- **p. 8 / 5.4. Real-world Data - extractive body cue:** We visualize our action scoring predictions given certain gripper orientations over three real-world 3D scans from the Replica dataset [42] and Google Scanned Objects [38, ...
- **p. 6 / 5.1. Framework and Settings - extractive body cue:** At the beginning of each interaction simulation, we initialize the robot gripper slightly above a surface position p of interest approaching from orientation R.
- **p. 6 / 5.2. Metrics and Baselines - extractive body cue:** This metric jointly evaluates all the three network modules and mimics the final use case of proposing meaningful actions when a robot actuator wants to ...
- **p. 8 / 5.4. Real-world Data - extractive body cue:** We directly applied our networks trained on synthetic data to real-world data.
- **p. 7 / 5.3. Results and Analysis - extractive body cue:** Our networks also learn representations that generalize successfully to unseen novel object categories.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The Proposed Where2Act Task. Given as input an ar- ticulated 3D object, we learn to propose the actionable information for different robotic manipulation ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Network Architecture. Our network takes an 2D image or a 3D partial scan as input and extract per-pixel feature fp using (a) Unet ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. (a) Our interactive simulation environment: we show the local gripper frame by the red, green and blue axes, which corre- sponds to the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. We summarize the shape counts in our dataset. Here, pot and washing are short for kitchen pot and washing machine. Action Settings. We ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. We visualize the per-pixel action scoring predictions over the articulated parts given certain gripper orientations for interaction. In each set of results, the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative Evaluations and Comparisons. We com- pare our method to three baseline methods (i.e. B-Random, B- Normal and B-PCPNet). In each entry, we ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation Study. We compare our method to an ablated version, where we remove the online adaptive sampling. It is clear to see that ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. We visualize (a) the actionability scoring and (b) the action proposal predictions on an example cabinet with a door that can be slipped ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Equipped with a large-scale PartNetMobility dataset, SAPIEN [49] provides a physics-rich simulation environment that supports robot actuators interacting with 2,346 3D CAD models from ... | embodiment, simulator version and control stack | p. 5 (5.1. Framework and Settings), p. 5 (5.1. Framework and Settings) |
| Task/environment | We conduct our experiments using 15 selected object categories in the PartNet-Mobility dataset, after removing the objects that are either too small (e.g. pens, ... | reset, timeout, object/scene variation | p. 5 (5.1. Framework and Settings), p. 8 (5.4. Real-world Data) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (4. Method), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (4.1. Network Modules) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 1. The Proposed Where2Act Task. Given as input an ar- ticulated 3D object, we learn to propose the actionable information for different robotic ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Thus, we report the F-score balancing precision and recall for the positive class. | definition/direction/unit from same section | p. 6 (5.2. Metrics and Baselines) |
| We illustrate the estimated actionability scores over the articulated part for the six action primitives in Fig. | definition/direction/unit from same section | p. 8 (5.3. Results and Analysis) |
| A natural set of metrics is to evaluate the binary classification accuracy of the action scoring network Ds. | definition/direction/unit from same section | p. 6 (5.2. Metrics and Baselines) |
| We visualize the predicted action scores in Fig. | definition/direction/unit from same section | p. 7 (5.3. Results and Analysis) |
| For example, for pulling, we predict higher scores over high-curvature regions such as part boundaries and handles, while for pushing, almost all flat surface ... | definition/direction/unit from same section | p. 7 (5.3. Results and Analysis) |
| We show the top-4 rated proposals. are equally highlighted and the pixels around handles are reasonably predicted to be not pushable due to object-gripper ... | definition/direction/unit from same section | p. 8 (5.3. Results and Analysis) |
| Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and some am- biguous cases that are ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We propose two quantitative metrics for evaluating performance of our proposed method, compared with three baseline methods and one ablated version of our method. | comparison identity and matched condition | p. 6 (5.2. Metrics and Baselines) |
| We define the final measure as below. ssr = # successful proposals # total proposals (8) Baselines and Ablation Study. | comparison identity and matched condition | p. 6 (5.2. Metrics and Baselines) |
| SAPIEN integrates one of the state-of-the-art physical simulation engines NVIDIA PhysX [30] to simulate physics-rich interaction details. | comparison identity and matched condition | p. 5 (5.1. Framework and Settings) |
| The baseline methods are not sensitive to the input kinds. | comparison identity and matched condition | p. 7 (5.2. Metrics and Baselines) |
| Quantitative Evaluations and Comparisons. | comparison identity and matched condition | p. 7 (5.2. Metrics and Baselines) |
| 5 presents comparisons among the four directional interaction types. | comparison identity and matched condition | p. 8 (5.3. Results and Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To validate the effectiveness of the proposed method and provide benchmarks for the proposed task, we compare to three baseline methods and one ablated ... | component/input/data sensitivity | p. 6 (5.2. Metrics and Baselines) |
| Table 3. Ablation Study. We compare our method to an ablated version, where we remove the online adaptive sampling. It is clear to see ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| We define the final measure as below. ssr = # successful proposals # total proposals (8) Baselines and Ablation Study. | component/input/data sensitivity | p. 6 (5.2. Metrics and Baselines) |
| The ablation study shown in Table 3 further validates that the online data sampling (OS) strategy helps boost the performance. | component/input/data sensitivity | p. 7 (5.3. Results and Analysis) |
| We conduct our experiments using 15 selected object categories in the PartNet-Mobility dataset, after removing the objects that are either too small (e.g. pens, ... | component/input/data sensitivity | p. 5 (5.1. Framework and Settings) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and ... | We observe that 3D-ours achieves the best performance. validates that our network learns geometric features more than local normals and curvatures. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Metrics and Baselines), p. 7 (5.2. Metrics and Baselines), p. 1 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments), p. 6 (5.2. Metrics and Baselines) |
| Primary metric/result | An ablated version Ours w/o OS further proves the improvement provided by the proposed online adaptive data sampling (OS) strategy. | numeric claim only at cited anchor | p. 7 (5.2. Metrics and Baselines) |

- Numeric sentences retained from the body:
- **p. 5 / 5.1. Framework and Settings - extractive body cue:** Equipped with a large-scale PartNetMobility dataset, SAPIEN [49] provides a physics-rich simulation environment that supports robot actuators interacting with 2,346 3D CAD models from 46 ...
- **p. 5 / 5.1. Framework and Settings - extractive body cue:** Then, we use a Franka Panda Flying gripper with 2 fingers as the robot actuator, which has 8 degree-offreedom (DoF) in total, including the 3 ...
- **p. 5 / 5.1. Framework and Settings - extractive body cue:** In total, there are 773 objects in the training categories and 199 objects in the testing ones.
- **p. 3 / 4.1. Network Modules - extractive body cue:** (2) We represent the 3-DoF gripper orientation by the first two orthonormal axes in the 3×3 rotation matrix, following the proposed 6D-rotation representation in [58].
- **p. 5 / 4.3. Training and Losses - extractive body cue:** After adjusting the relative loss scales to the same level, we obtain the final objective function L = Ls +Lr +100×La.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and some am- biguous cases that are ... | p. 12 (Figure/Table caption) |
| body limitation/failure cue | Figure 5. We visualize (a) the actionability scoring and (b) the action proposal predictions on an example cabinet with a door that can be ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Finally, our method does not explicitly model the part segmentation and part motion axis, which may be incorporated in the future works to further ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | Figure 1. The Proposed Where2Act Task. Given as input an ar- ticulated 3D object, we learn to propose the actionable information for different robotic ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. Network Architecture. Our network takes an 2D image or a 3D partial scan as input and extract per-pixel feature fp using (a) ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | With random interactions, there are many more failed interaction trials than the successful ones. | p. 6 (5.2. Metrics and Baselines) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We empirically find it beneficial to first train the action scoring module Ds and then train the three decoders jointly. | p. 4 (4.3. Training and Losses) |
| We mark orientation Rs from the other hemisphere as negative without trials since the gripper cannot be put inside the object volume. | p. 4 (4.2. Collecting Training Data) |
| (6) This strategy is computationally efficient since we are reusing the 100 proposals computed in Eq. | p. 5 (4.3. Training and Losses) |
| With random interactions, there are many more failed interaction trials than the successful ones. | p. 6 (5.2. Metrics and Baselines) |
| We define one interaction trial successful if the part that we are interacting with exhibits a considerable part motion along the intended direction. | p. 6 (5.1. Framework and Settings) |
| For the 3D experiments, we use PointNet++ segmentation network [34] and implementation [47] with 4 set abstraction layers with single-scale grouping for the encoder ... | p. 3 (4.1. Network Modules) |
| To decode the per-pixel actionable information, we propose three decoding heads: (c) an actionability scoring module Da that predicts a score ap ∈[0,1]; (d) ... | p. 3 (4.1. Network Modules) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / Figure/Table caption - extractive body cue:** Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and some am- biguous cases that are hard ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. We visualize (a) the actionability scoring and (b) the action proposal predictions on an example cabinet with a door that can be slipped ...
- **p. 8 / 6. Conclusion - extractive body cue:** Finally, our method does not explicitly model the part segmentation and part motion axis, which may be incorporated in the future works to further improve ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The Proposed Where2Act Task. Given as input an ar- ticulated 3D object, we learn to propose the actionable information for different robotic manipulation ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Network Architecture. Our network takes an 2D image or a 3D partial scan as input and extract per-pixel feature fp using (a) Unet ...
- **p. 6 / 5.2. Metrics and Baselines - extractive body cue:** With random interactions, there are many more failed interaction trials than the successful ones.

- **Evidence anchors reviewed:** datasets p. 5 (5.1. Framework and Settings), p. 5 (5.1. Framework and Settings), p. 8 (5.4. Real-world Data), p. 6 (5.1. Framework and Settings), p. 6 (5.2. Metrics and Baselines), p. 8 (5.4. Real-world Data), metrics p. 1 (Figure/Table caption), p. 6 (5.2. Metrics and Baselines), p. 8 (5.3. Results and Analysis), p. 6 (5.2. Metrics and Baselines), p. 7 (5.3. Results and Analysis), p. 7 (5.3. Results and Analysis), baselines p. 6 (5.2. Metrics and Baselines), p. 6 (5.2. Metrics and Baselines), p. 5 (5.1. Framework and Settings), p. 7 (5.2. Metrics and Baselines), p. 7 (5.2. Metrics and Baselines), p. 8 (5.3. Results and Analysis), results p. 7 (5.2. Metrics and Baselines), p. 7 (5.2. Metrics and Baselines), p. 1 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments), p. 6 (5.2. Metrics and Baselines).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 4. We visualize the per-pixel action scoring predictions over the articulated parts given certain gripper orientations for interaction. In each set of results, the left two shapes shown in ... (p. 7, Figure/Table caption).
- **Metric evidence:** We set up an interactive simulation environment in SAPIEN [49] and benchmark performance of the proposed method both qualititively and quantitatively. (p. 5, 5. Experiments).
- **Baseline/ablation evidence:** We define the final measure as below. ssr = # successful proposals # total proposals (8) Baselines and Ablation Study. (p. 6, 5.2. Metrics and Baselines).
- **Failure/negative evidence:** With random interactions, there are many more failed interaction trials than the successful ones. (p. 6, 5.2. Metrics and Baselines).
