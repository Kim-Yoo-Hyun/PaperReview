# Evaluation - ArticuBot: Learning Universal Articulated Object Manipulation Policy via Large Scale Simulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p156.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p156.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (B. Table-Top Franka Arm Results), p. 12 (C. Mobile X-Arm Results), p. 13 (C. Mobile X-Arm Results), p. 13 (C. Mobile X-Arm Results)): If we compute the normalized opening performance for ArticuBot only in cases where the grasp is successful (Le., the same starting conditions as FlowBot3D), the performance of ArticuBot further improves ...

## Evaluation Body Digest

- **p. 13 / C. Mobile X-Arm Results - extractive body cue:** Although our training data includes multi-door objects, demonstrations are generated for opening the closest door to the initial pose of the robot.
- **p. 7 / V. SIMULATION RESULTS - extractive body cue:** We use the PartNet-Mobility [55] dataset for the assets of the articulated object.
- **p. 12 / B. Table-Top Franka Arm Results - extractive body cue:** 8 (zoom-in for better views) visualizes ArticuBot's predictions on some of the real-world test objects.
- **p. 12 / B. Table-Top Franka Arm Results - extractive body cue:** FlowBot3D achieves a reasonable normalized opening performance of 0.38, starting from the state where the robot gripper already grasps the ‘object.
- **p. 13 / C. Mobile X-Arm Results - extractive body cue:** Some of the tested real-world objects are quite challenging, for example, cabinet C3 has a very small handle that protrudes only 2 cm from the ...
- **p. 7 / V. SIMULATION RESULTS - extractive body cue:** We extracted 332 objects from 5 different categories: storage furniture,
- **p. 12 / C. Mobile X-Arm Results - extractive body cue:** As shown, ArticuBot achieves a grasping success rate of 0.9 and normalized opening performance of 0.54, showing it can
- **p. 12 / B. Table-Top Franka Arm Results - extractive body cue:** We also find OpenVLA fails to grasp or open any test objects, resulting in a grasping success rate and normalized opening performance of 0.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** V. SIMULATION RESULTS (p. 7); VI. REAL-WORLD EXPERIMENTS (p. 10); B. Table-Top Franka Arm Results (p. 12); C. Mobile X-Arm Results (p. 12).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| B. Table-Top Franka Arm Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | If we compute the normalized opening performance for ArticuBot only in cases where the grasp is successful (Le., the same starting conditions as FlowBot3D), ... | p. 12 (B. Table-Top Franka Arm Results) |
| C. Mobile X-Arm Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown, ArticuBot achieves a grasping success rate of 0.9 and normalized opening performance of 0.54, showing it can | p. 12 (C. Mobile X-Arm Results) |
| C. Mobile X-Arm Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 5) Objects in real kitchens and lounges are usually occluded by neighboring objects, and we believe that adding this type of occlusion could further ... | p. 13 (C. Mobile X-Arm Results) |
| C. Mobile X-Arm Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | We think that incorporating interaction history with current visual observations could further improve performance, especially for objects whose articulation are ambiguous to judge just ... | p. 13 (C. Mobile X-Arm Results) |

## Dataset / Benchmark Role

- **p. 13 / C. Mobile X-Arm Results - extractive body cue:** Although our training data includes multi-door objects, demonstrations are generated for opening the closest door to the initial pose of the robot.
- **p. 7 / V. SIMULATION RESULTS - extractive body cue:** We use the PartNet-Mobility [55] dataset for the assets of the articulated object.
- **p. 12 / B. Table-Top Franka Arm Results - extractive body cue:** 8 (zoom-in for better views) visualizes ArticuBot's predictions on some of the real-world test objects.
- **p. 12 / B. Table-Top Franka Arm Results - extractive body cue:** FlowBot3D achieves a reasonable normalized opening performance of 0.38, starting from the state where the robot gripper already grasps the ‘object.
- **p. 13 / C. Mobile X-Arm Results - extractive body cue:** Some of the tested real-world objects are quite challenging, for example, cabinet C3 has a very small handle that protrudes only 2 cm from the ...
- **p. 7 / V. SIMULATION RESULTS - extractive body cue:** We extracted 332 objects from 5 different categories: storage furniture,

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: System overview of ArticuBot. Top: We combine sampling-based grasping, motion planning, and opening actions to efficiently generate thousands of demonstrations in simulation. These ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 3: Comparison of hierarchical and non-hierarchical poli
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: Comparison of different high-level poli
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6: Real-world test objects for
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 5: The three different real robot setups.
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 7: Comparison of AnticuBot with FlowBotSD and AO-Grasp on 9 test objects in Lab A with table-top Franka, We omit
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 8: Visualizations of the high-level policy's predictions (per-point weights and goal end-effector points) in three of the real-world test cases. The green points represent ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Although our training data includes multi-door objects, demonstrations are generated for opening the closest door to the initial pose of the robot. | embodiment, simulator version and control stack | p. 13 (C. Mobile X-Arm Results), p. 7 (V. SIMULATION RESULTS) |
| Task/environment | We use the PartNet-Mobility [55] dataset for the assets of the articulated object. | reset, timeout, object/scene variation | p. 7 (V. SIMULATION RESULTS), p. 12 (B. Table-Top Franka Arm Results) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 8 (B. Is a Hierarchical Policy Needed?), p. 7 (B. Policy Learning with a Hierarchical Policy Representation) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture), p. 5 (B. Policy Learning with a Hierarchical Policy Representation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| As shown, ArticuBot achieves a grasping success rate of 0.9 and normalized opening performance of 0.54, showing it can | definition/direction/unit from same section | p. 12 (C. Mobile X-Arm Results) |
| We also find OpenVLA fails to grasp or open any test objects, resulting in a grasping success rate and normalized opening performance of 0. | definition/direction/unit from same section | p. 12 (B. Table-Top Franka Arm Results) |
| In our early ‘experiments, we find that Unlike the Franka Arm, the X-Arm lacks impedance control and force sensing. ‘This requires a more precise ... | definition/direction/unit from same section | p. 13 (C. Mobile X-Arm Results) |
| We do notice a drop in the normalized opening performance ‘compared to the table-top Franka experiments. | definition/direction/unit from same section | p. 13 (C. Mobile X-Arm Results) |
| Fig. 2: System overview of ArticuBot. Top: We combine sampling-based grasping, motion planning, and opening actions to efficiently generate thousands of demonstrations in simulation. ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| ‘The results forall test objects and compared methods in lab A are shown in Fig. | comparison identity and matched condition | p. 12 (B. Table-Top Franka Arm Results) |
| If we compute the normalized opening performance for ArticuBot only in cases where the grasp is successful (Le., the same starting conditions as FlowBot3D), ... | comparison identity and matched condition | p. 12 (B. Table-Top Franka Arm Results) |
| We do notice a drop in the normalized opening performance ‘compared to the table-top Franka experiments. | comparison identity and matched condition | p. 13 (C. Mobile X-Arm Results) |
| Fig. 3: Comparison of hierarchical and non-hierarchical poli | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Fig. 4: Comparison of different high-level poli | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Fig. 7: Comparison of AnticuBot with FlowBotSD and AO-Grasp on 9 test objects in Lab A with table-top Franka, We omit | comparison identity and matched condition | p. 11 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We think adding a force-torque sensor on the X-Arm to enable impedance control could help alleviate this issue; fine-tuning the policy in the real-world ... | component/input/data sensitivity | p. 13 (C. Mobile X-Arm Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Instead, we propose to use a hilrarchical policy representation, which consists of 4 high-level policy and a low-level policy. | If we compute the normalized opening performance for ArticuBot only in cases where the grasp is successful (Le., the same starting conditions as FlowBot3D), ... | PDF body cue; verify exact table/figure and matched conditions | p. 12 (B. Table-Top Franka Arm Results), p. 12 (C. Mobile X-Arm Results), p. 13 (C. Mobile X-Arm Results), p. 13 (C. Mobile X-Arm Results) |
| Primary metric/result | As shown, ArticuBot achieves a grasping success rate of 0.9 and normalized opening performance of 0.54, showing it can | numeric claim only at cited anchor | p. 12 (C. Mobile X-Arm Results) |

- Numeric sentences retained from the body:
- **p. 7 / V. SIMULATION RESULTS - extractive body cue:** We extracted 332 objects from 5 different categories: storage furniture,
- **p. 5 / 2. Hierarchical Policy Learning -- Low-level Policy Architecture - extractive body cue:** We filter out all trajectories where the final opened angle (radians for hinge doors and centimeters for drawers) is smaller than a threshold, e.g.. if ...
- **p. 6 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** FFor the current end-effector points {ee?*}/_,, its feature for attention includes the following: the first partis a learnable embedding vf" for each of the 4 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | See Appendix L for visualizations of some of the failure cases of ArticuBot, and some basic failure recovery abilities of ArticuBot. | p. 13 (C. Mobile X-Arm Results) |
| body limitation/failure cue | We leave addressing these limitations as important future work. | p. 13 (C. Mobile X-Arm Results) |
| body limitation/failure cue | Common failure ceases for table-top experiments include: 1, The robot arm runs to joint limits while opening the object, due to the limited space ... | p. 12 (B. Table-Top Franka Arm Results) |
| body limitation/failure cue | The major failure case for FlowBot3D is that the predicted flow is in the wrong direction, e.g., it predicts upwards flows for ‘opening a ... | p. 12 (B. Table-Top Franka Arm Results) |
| body limitation/failure cue | We do not input the optional segmentation mask for the target link to open for FlowBot3D, as such masks are not readily available in ... | p. 11 (A. Setups) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| At inference time, the final predicted subgoal endheffector pose is the averaged prediction from all points in the scene: e¢,(0) = 31 (p;-+8)(0)). | p. 6 (B. Policy Learning with a Hierarchical Policy Representation) |
| At inference time, the final prediction of the sub-goal end-effector Points is then the weighted average of the displacement from each point: €€,(0) = ... | p. 6 (B. Policy Learning with a Hierarchical Policy Representation) |
| We assume the name of the target object to manipulate, such that we can run a openvocabulary segmentation method, e.g., Grounded SAM [39], to ... | p. 3 (B. Sim2real Policy Learning) |
| We then run three different motion planning algorithms, RRT* (22), BIT* [14] and ABIT* [43], to generate the path to reach the | p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture) |
| Motion Planning for reaching the grasping pose: For each of the grasp candidates, we first use inverse kinematics (IK) to compute a target joint ... | p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture) |
| Using a CPU with 128 virtual cores, one optimal opening trajectory ccan be generated within 2 minutes. | p. 5 (2. Hierarchical Policy Learning -- Low-level Policy Architecture) |
| IK is then performed for the ‘end-effector to reach each of the computed poses along the trajectory to open the object. | p. 5 (2. Hierarchical Policy Learning -- Low-level Policy Architecture) |
| takes 3D point cloud as input and outputs delta endeffector transformations as the actions. + DP3 Transformer, which replaces the simplified PointNet encoder in ... | p. 8 (B. Is a Hierarchical Policy Needed?) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 13 / C. Mobile X-Arm Results - extractive body cue:** See Appendix L for visualizations of some of the failure cases of ArticuBot, and some basic failure recovery abilities of ArticuBot.
- **p. 13 / C. Mobile X-Arm Results - extractive body cue:** We leave addressing these limitations as important future work.
- **p. 12 / B. Table-Top Franka Arm Results - extractive body cue:** Common failure ceases for table-top experiments include: 1, The robot arm runs to joint limits while opening the object, due to the limited space of ...
- **p. 12 / B. Table-Top Franka Arm Results - extractive body cue:** The major failure case for FlowBot3D is that the predicted flow is in the wrong direction, e.g., it predicts upwards flows for ‘opening a microwave ...
- **p. 11 / A. Setups - extractive body cue:** We do not input the optional segmentation mask for the target link to open for FlowBot3D, as such masks are not readily available in the ...

- **Evidence anchors reviewed:** datasets p. 13 (C. Mobile X-Arm Results), p. 7 (V. SIMULATION RESULTS), p. 12 (B. Table-Top Franka Arm Results), p. 12 (B. Table-Top Franka Arm Results), p. 13 (C. Mobile X-Arm Results), p. 7 (V. SIMULATION RESULTS), metrics p. 12 (C. Mobile X-Arm Results), p. 12 (B. Table-Top Franka Arm Results), p. 13 (C. Mobile X-Arm Results), p. 13 (C. Mobile X-Arm Results), p. 4 (Figure/Table caption), baselines p. 12 (B. Table-Top Franka Arm Results), p. 12 (B. Table-Top Franka Arm Results), p. 13 (C. Mobile X-Arm Results), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 11 (Figure/Table caption), results p. 12 (B. Table-Top Franka Arm Results), p. 12 (C. Mobile X-Arm Results), p. 13 (C. Mobile X-Arm Results), p. 13 (C. Mobile X-Arm Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
