# Evaluation - DextAIRity: Deformable Manipulation Can be a Breeze

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.01197; PDF retrieval source: https://arxiv.org/pdf/2203.01197. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (V. EVALUATION), p. 8 (V. EVALUATION), p. 8 (V. EVALUATION), p. 6 (V. EVALUATION), p. 7 (V. EVALUATION), p. 6 (V. EVALUATION)): II shows performance averaged over 10 test episodes; our policy achieves over 80% on all cloth types, outperforming [FlingBot] and [Pick&Place] by roughly 60% and 40% respectively.

## Evaluation Body Digest

- **p. 5 / V. EVALUATION - extractive PDF cue:** For both tasks, we evaluate task completion rate and ability to generalize to unseen cloths and bags on a real-world robot platform.
- **p. 6 / V. EVALUATION - extractive PDF cue:** The failure of [FlingBot] is due to its limited move speed, which needs to Large Rect X-Large Rect Shirt Dress Pick&Place 36.2 / 13.1 38.0 ...
- **p. 5 / V. EVALUATION - extractive PDF cue:** Simulation Task Generation: We generate five tasks for training and evaluation in simulation: • (Train) Normal Rect contains rectangular cloths that are smaller in size ...
- **p. 6 / V. EVALUATION - extractive PDF cue:** We also investigate these approaches' performance on cloth that is significantly larger than the robot's reach range.
- **p. 7 / V. EVALUATION - extractive PDF cue:** We directly evaluate the trained model with our real-world setup.
- **p. 7 / V. EVALUATION - extractive PDF cue:** II shows performance averaged over 10 test episodes; our policy achieves over 80% on all cloth types, outperforming [FlingBot] and [Pick&Place] by roughly 60% and ...
- **p. 8 / V. EVALUATION - extractive PDF cue:** Small Bag Yellow Bag Blue Bag Shake 0.00 / 0.56 0.00 / 0.68 0.00 / 0.65 DextAIRity-fixed 0.40 / 0.86 0.52 / 0.92 0.56 / ...
- **p. 7 / V. EVALUATION - extractive PDF cue:** Bag opening Task-performance for bag opening is measured by two metrics: 1) success rate: p = 1 N ∑N 1 sgn(Ai ≥ˆA), and 2) normalized ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** V. EVALUATION (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | II shows performance averaged over 10 test episodes; our policy achieves over 80% on all cloth types, outperforming [FlingBot] and [Pick&Place] by roughly 60% ... | p. 7 (V. EVALUATION) |
| V. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, [DextAIRity] achieves 60% success rate at the first interaction step and achieved a final success rate, after 4 blowing steps, of 88%. | p. 8 (V. EVALUATION) |
| V. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | We found that dynamic action [Shake] generally fails to open the bag while [DextAIRity-fixed] achieved a roughly 50% success rate on the testing bags. | p. 8 (V. EVALUATION) |
| V. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | Although the edgecoincident grasping policy provides a marginal improvement to final performance, it improves training efficiency significantly because the system no longer needs to ... | p. 6 (V. EVALUATION) |
| V. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | Bag opening Task-performance for bag opening is measured by two metrics: 1) success rate: p = 1 N ∑N 1 sgn(Ai ≥ˆA), and 2) ... | p. 7 (V. EVALUATION) |

## Dataset / Benchmark Role

- **p. 5 / V. EVALUATION - extractive PDF cue:** For both tasks, we evaluate task completion rate and ability to generalize to unseen cloths and bags on a real-world robot platform.
- **p. 6 / V. EVALUATION - extractive PDF cue:** The failure of [FlingBot] is due to its limited move speed, which needs to Large Rect X-Large Rect Shirt Dress Pick&Place 36.2 / 13.1 38.0 ...
- **p. 5 / V. EVALUATION - extractive PDF cue:** Simulation Task Generation: We generate five tasks for training and evaluation in simulation: • (Train) Normal Rect contains rectangular cloths that are smaller in size ...
- **p. 6 / V. EVALUATION - extractive PDF cue:** We also investigate these approaches' performance on cloth that is significantly larger than the robot's reach range.
- **p. 7 / V. EVALUATION - extractive PDF cue:** We directly evaluate the trained model with our real-world setup.
- **p. 7 / V. EVALUATION - extractive PDF cue:** II shows performance averaged over 10 test episodes; our policy achieves over 80% on all cloth types, outperforming [FlingBot] and [Pick&Place] by roughly 60% and ...
- **p. 8 / V. EVALUATION - extractive PDF cue:** Small Bag Yellow Bag Blue Bag Shake 0.00 / 0.56 0.00 / 0.68 0.00 / 0.65 DextAIRity-fixed 0.40 / 0.86 0.52 / 0.92 0.56 / ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: DextAIRity manipulates deformable objects by controlling an active airflow. We demonstrate DextAIRity with two tasks that are particularly challenging for traditional contact-based manipulation: ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: System and Task Setup. Our system setup consists of (a) three UR5 robot arms, two of which are equipped with parallel-jaw grippers and ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3: Simulating Air-Cloth Interactions. Cloth is simulated as a spring-mass system, and airflow is simulated as a stream of invisible particles. Our policy only ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4: Approach Overview. (a) From a top-down observation, the Grasping Network predicts scores for each grasping action(i.e., center and rotation). The one with highest ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 5: Cloths and Bags used in Real-world Experiments.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6: Cloth unfolding coverage v.s. steps. Rectangle CLOTH3D Large X-Large Shirt Dress Pick&Place
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 7: Qualitative results of cloth unfolding. Grasp predictions are visualized on the top-down image with cloth coverage labeled on the top right (row 1,2,4). ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 8: Qualitative results of bag opening. Bag state (normalized area if the bag is not opened) is labeled on the bottom right. Red arrows ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For both tasks, we evaluate task completion rate and ability to generalize to unseen cloths and bags on a real-world robot platform. | embodiment, simulator version and control stack | p. 5 (V. EVALUATION), p. 6 (V. EVALUATION) |
| Task/environment | The failure of [FlingBot] is due to its limited move speed, which needs to Large Rect X-Large Rect Shirt Dress Pick&Place 36.2 / 13.1 ... | reset, timeout, object/scene variation | p. 6 (V. EVALUATION), p. 5 (V. EVALUATION) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 4 (IV. METHOD), p. 5 (IV. METHOD) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 4 (IV. METHOD), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Bag opening Task-performance for bag opening is measured by two metrics: 1) success rate: p = 1 N ∑N 1 sgn(Ai ≥ˆA), and 2) ... | definition/direction/unit from same section | p. 7 (V. EVALUATION) |
| Results Success rate and normalized area of both the training bag and novel testing bags are shown in Tab. | definition/direction/unit from same section | p. 8 (V. EVALUATION) |
| In contrast, [DextAIRity] achieves 60% success rate at the first interaction step and achieved a final success rate, after 4 blowing steps, of 88%. | definition/direction/unit from same section | p. 8 (V. EVALUATION) |
| 0.851 0.584 Dress Shirt Stop Pick & Place Flingbot Stop 0.237 0.539 0.584 0.809 0.344 0.632 0.543 0.242 0.314 0.362 0.379 0.385 0.373 0.365 ... | definition/direction/unit from same section | p. 7 (V. EVALUATION) |
| For both tasks, we evaluate task completion rate and ability to generalize to unseen cloths and bags on a real-world robot platform. | definition/direction/unit from same section | p. 5 (V. EVALUATION) |
| Fig. 4: Approach Overview. (a) From a top-down observation, the Grasping Network predicts scores for each grasping action(i.e., center and rotation). The one with ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Cloth unfolding Performance is measured by cloth coverage at the end of each episode. | definition/direction/unit from same section | p. 5 (V. EVALUATION) |
| We also investigate these approaches' performance on cloth that is significantly larger than the robot's reach range. | definition/direction/unit from same section | p. 6 (V. EVALUATION) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As a result, coverage of X-Large Rect increases +23.0%, +13.3%, +1.6%, and +0.3% at each blow step compared to the fixed-policy ablation. | comparison identity and matched condition | p. 6 (V. EVALUATION) |
| Ablations: We compared with the following systems: • Pick&Place [18]: predicts a single-arm grasping position and movement direction for quasi-static pick-and-place. • FlingBot [10]: ... | comparison identity and matched condition | p. 6 (V. EVALUATION) |
| II shows performance averaged over 10 test episodes; our policy achieves over 80% on all cloth types, outperforming [FlingBot] and [Pick&Place] by roughly 60% ... | comparison identity and matched condition | p. 7 (V. EVALUATION) |
| Ablations: We compare our system with the following alternative approaches for bag opening: • Shake: moves the bag back-and-forth by rotating last joint and ... | comparison identity and matched condition | p. 7 (V. EVALUATION) |
| Fig. 1: DextAIRity manipulates deformable objects by controlling an active airflow. We demonstrate DextAIRity with two tasks that are particularly challenging for traditional contact-based ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| As a result, coverage of X-Large Rect increases +23.0%, +13.3%, +1.6%, and +0.3% at each blow step compared to the fixed-policy ablation. | component/input/data sensitivity | p. 6 (V. EVALUATION) |
| Our experimental evaluation suggests that DextAIRity is a promising approach for quickly and efficiently unfolding for large cloth items without the need of high-speed ... | component/input/data sensitivity | p. 6 (V. EVALUATION) |
| Ablations: We compare our system with the following alternative approaches for bag opening: • Shake: moves the bag back-and-forth by rotating last joint and ... | component/input/data sensitivity | p. 7 (V. EVALUATION) |
| Fig. 1: DextAIRity manipulates deformable objects by controlling an active airflow. We demonstrate DextAIRity with two tasks that are particularly challenging for traditional contact-based ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our system setup consists of (a) three UR5 robot arms, two of which are equipped with parallel-jaw grippers and one with a commodity centrifugal ... | II shows performance averaged over 10 test episodes; our policy achieves over 80% on all cloth types, outperforming [FlingBot] and [Pick&Place] by roughly 60% ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (V. EVALUATION), p. 8 (V. EVALUATION), p. 8 (V. EVALUATION), p. 6 (V. EVALUATION), p. 7 (V. EVALUATION), p. 6 (V. EVALUATION) |
| Primary metric/result | In contrast, [DextAIRity] achieves 60% success rate at the first interaction step and achieved a final success rate, after 4 blowing steps, of 88%. | numeric claim only at cited anchor | p. 8 (V. EVALUATION) |

- Numeric sentences retained from the body:
- **p. 6 / V. EVALUATION - extractive PDF cue:** 0 1 2 3 4 5 Episode Step 0.2 0.4 0.6 0.8 1.0 Coverage (%) Sim Large Rect 0 1 2 3 4 5 Episode ...
- **p. 6 / V. EVALUATION - extractive PDF cue:** [DextAIRity] and [FlingBot] achieve similar performance (over 90% coverage after 3 steps), while [Pick&Place] achieves is only 45.9%.
- **p. 7 / V. EVALUATION - extractive PDF cue:** Training of [FlingBot+] takes only 300 epochs, while [FlingBot] requires over 2,000 epochs to converge.
- **p. 7 / V. EVALUATION - extractive PDF cue:** The running time of these three primitives is 3.6s (blow×4), 2.9s (fling), and 1.8s(place).
- **p. 4 / IV. METHOD - extractive PDF cue:** Each blowing step lasts 0.2 s after movement and the blower is kept on during all blowing steps.
- **p. 5 / IV. METHOD - extractive PDF cue:** Both pretraining and fine-tuning are performed in simulation, which take 300 and 200 epochs respectively.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While in this paper we demonstrate the effectiveness of directed air to manipulate deformable objects, we discuss a few limitations and practical considerations of ... | p. 8 (VI. LIMITATIONS AND PRACTICAL CONSIDERATIONS) |
| body limitation/failure cue | The failure of [FlingBot] is due to its limited move speed, which needs to Large Rect X-Large Rect Shirt Dress Pick&Place 36.2 / 13.1 ... | p. 6 (V. EVALUATION) |
| body limitation/failure cue | Fig. 10: Failure Cases. (a) A corner is inadvertently rolled up due to Eddy effects. (b) Multiple layers of the fabric are mistakenly grasped. ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Overall, we find that quasi-static pick-and-place actions are generally inefficient for cloth unfolding and, while dynamic actions such as flinging can drastically improve efficiency, ... | p. 6 (V. EVALUATION) |
| body limitation/failure cue | 7, suggests [FlingBot] can successfully unfold shirts with width within the reach range but it fails (see the pink dress) when items become much ... | p. 7 (V. EVALUATION) |
| body limitation/failure cue | 7) suggest that even on out of distribution clothing, our learned grasping policy attempts to grasp cloth corners and the blowing policy preferentially directs ... | p. 7 (V. EVALUATION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each epoch contains 32 episodes and 64 optimization steps with a batch size of 16 for the grasping network and 128 for the blowing ... | p. 5 (IV. METHOD) |
| Each episode contains at most 5 interaction steps, where each step includes both grasping and blowing actions, and the policy terminates an episode when ... | p. 5 (V. EVALUATION) |
| 6: Cloth unfolding coverage v.s. steps. | p. 6 (V. EVALUATION) |
| [DextAIRity] and [FlingBot] achieve similar performance (over 90% coverage after 3 steps), while [Pick&Place] achieves is only 45.9%. | p. 6 (V. EVALUATION) |
| In each episode, we run the policy 4 times or until the bag is opened. | p. 7 (V. EVALUATION) |
| Training of [FlingBot+] takes only 300 epochs, while [FlingBot] requires over 2,000 epochs to converge. | p. 7 (V. EVALUATION) |
| 9: Bag opening success rate v.s. steps. | p. 8 (V. EVALUATION) |
| 8 show that [DextAIRity] tends to blow horizontally in the first step and adopts a more top-down blowing action in the subsequent steps. | p. 8 (V. EVALUATION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / VI. LIMITATIONS AND PRACTICAL CONSIDERATIONS - extractive PDF cue:** While in this paper we demonstrate the effectiveness of directed air to manipulate deformable objects, we discuss a few limitations and practical considerations of deploying ...
- **p. 6 / V. EVALUATION - extractive PDF cue:** The failure of [FlingBot] is due to its limited move speed, which needs to Large Rect X-Large Rect Shirt Dress Pick&Place 36.2 / 13.1 38.0 ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 10: Failure Cases. (a) A corner is inadvertently rolled up due to Eddy effects. (b) Multiple layers of the fabric are mistakenly grasped. (c) ...
- **p. 6 / V. EVALUATION - extractive PDF cue:** Overall, we find that quasi-static pick-and-place actions are generally inefficient for cloth unfolding and, while dynamic actions such as flinging can drastically improve efficiency, however, ...
- **p. 7 / V. EVALUATION - extractive PDF cue:** 7, suggests [FlingBot] can successfully unfold shirts with width within the reach range but it fails (see the pink dress) when items become much longer.
- **p. 7 / V. EVALUATION - extractive PDF cue:** 7) suggest that even on out of distribution clothing, our learned grasping policy attempts to grasp cloth corners and the blowing policy preferentially directs air ...

- **PDF anchors reviewed:** datasets p. 5 (V. EVALUATION), p. 6 (V. EVALUATION), p. 5 (V. EVALUATION), p. 6 (V. EVALUATION), p. 7 (V. EVALUATION), p. 7 (V. EVALUATION), metrics p. 7 (V. EVALUATION), p. 8 (V. EVALUATION), p. 8 (V. EVALUATION), p. 7 (V. EVALUATION), p. 5 (V. EVALUATION), p. 4 (Figure/Table caption), baselines p. 6 (V. EVALUATION), p. 6 (V. EVALUATION), p. 7 (V. EVALUATION), p. 7 (V. EVALUATION), p. 1 (Figure/Table caption), results p. 7 (V. EVALUATION), p. 8 (V. EVALUATION), p. 8 (V. EVALUATION), p. 6 (V. EVALUATION), p. 7 (V. EVALUATION), p. 6 (V. EVALUATION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
