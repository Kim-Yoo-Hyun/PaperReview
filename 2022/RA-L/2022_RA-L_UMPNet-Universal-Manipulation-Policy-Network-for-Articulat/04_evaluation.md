# Evaluation - UMPNet: Universal Manipulation Policy Network for Articulated Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2109.05668; PDF retrieval source: https://arxiv.org/pdf/2109.05668. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 7 (IV. EVALUATION), p. 7 (IV. EVALUATION)): When combined with heuristic filter, the performance improves slightly.

## Evaluation Body Digest

- **p. 5 / IV. EVALUATION - extractive body cue:** Being able to effectively explore the possible states of an object without a specific goal is a critical first step for many robot learning algorithms ...
- **p. 7 / IV. EVALUATION - extractive body cue:** In addition, our system assumes the agent uses a suction-based end-effector, which can provide robust grasps for a large variety of objects and is widely ...
- **p. 7 / IV. EVALUATION - extractive body cue:** In addition, our policy doesn't consider real robot situation, for example, whether the grasping position can be reached by a real robot, the moving trajectory ...
- **p. 4 / IV. EVALUATION - extractive body cue:** Our simulation environment uses objects from PartNetMobility [29] and physics engine from Pybullet [30].
- **p. 5 / IV. EVALUATION - extractive body cue:** While random explorations can be used for simple environments, they are often not sufficient for tasks involving high-dimensional action space, where the majority of the ...
- **p. 6 / IV. EVALUATION - extractive body cue:** The performance for this task is measured by (1) normalized distance Egoal to target state after interaction: Egoal = //⃗jend-⃗jgoal/////⃗jgoal-⃗jinit//, where⃗j is vector of object's ...
- **p. 6 / IV. EVALUATION - extractive body cue:** Given a target state in the form of an RGB-D image, the task is to infer a sequence of actions that manipulate the object toward ...
- **p. 6 / IV. EVALUATION - extractive body cue:** (2) success rate, where a successful case is defined as the normalized distance to the goal state is smaller than 0.1.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** IV. EVALUATION (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | When combined with heuristic filter, the performance improves slightly. | p. 5 (IV. EVALUATION) |
| IV. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | I we can see that [ Where2Act ] is able to achieve similar performance in "single action effects", however, both [ Where2Act ] and ... | p. 5 (IV. EVALUATION) |
| IV. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | As a result, [ UMPNet ] can achieve better performance in both metrics. | p. 6 (IV. EVALUATION) |
| IV. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | (2) success rate, where a successful case is defined as the normalized distance to the goal state is smaller than 0.1. | p. 6 (IV. EVALUATION) |
| IV. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | We observed that there are a few real2sim gaps that could impact real-world performance. | p. 7 (IV. EVALUATION) |

## Dataset / Benchmark Role

- **p. 5 / IV. EVALUATION - extractive body cue:** Being able to effectively explore the possible states of an object without a specific goal is a critical first step for many robot learning algorithms ...
- **p. 7 / IV. EVALUATION - extractive body cue:** In addition, our system assumes the agent uses a suction-based end-effector, which can provide robust grasps for a large variety of objects and is widely ...
- **p. 7 / IV. EVALUATION - extractive body cue:** In addition, our policy doesn't consider real robot situation, for example, whether the grasping position can be reached by a real robot, the moving trajectory ...
- **p. 4 / IV. EVALUATION - extractive body cue:** Our simulation environment uses objects from PartNetMobility [29] and physics engine from Pybullet [30].
- **p. 5 / IV. EVALUATION - extractive body cue:** While random explorations can be used for simple environments, they are often not sufficient for tasks involving high-dimensional action space, where the majority of the ...
- **p. 6 / IV. EVALUATION - extractive body cue:** The performance for this task is measured by (1) normalized distance Egoal to target state after interaction: Egoal = //⃗jend-⃗jgoal/////⃗jgoal-⃗jinit//, where⃗j is vector of object's ...
- **p. 6 / IV. EVALUATION - extractive body cue:** Given a target state in the form of an RGB-D image, the task is to infer a sequence of actions that manipulate the object toward ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Universal Manipulation Policy for Articulated Objects. Instead of predicting a single step action, UMPNet predicts complex closed-loop 6DoF action sequences with varying trajectory ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Approach overview. UMPNet takes visual observation (i.e., RGB-D images) of an articulated object as input and generates a sequence of actions in SE(3) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Goal conditioned manipulation. whether the action will change the object state back to the initial state or forward into the future (i.e., a ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Open-ended state exploration. Arrow length indicates the inferred distance value, color indicates the inferred AoT label. We visualized the uniform samples to better ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Goal conditioned manipulation results. At the beginning or in the middle of a trajectory, the action candidates have positive (red) and negative (blue) ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Action →Articulation. The joint axes (red) are inferred from the actions selected by the learned policy (green), which indicates the system's implicit understanding ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Typical failure cases. UR5 robot, and a suction gripper. Fig. 8 (a) shows the real- world setup. In this experiment, we directly tested ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Real-world experiment. We test the model trained in simulation on a real-world platform. (a) We an RGB-D camera to capture visual observation and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Being able to effectively explore the possible states of an object without a specific goal is a critical first step for many robot learning ... | embodiment, simulator version and control stack | p. 5 (IV. EVALUATION), p. 7 (IV. EVALUATION) |
| Task/environment | In addition, our system assumes the agent uses a suction-based end-effector, which can provide robust grasps for a large variety of objects and is ... | reset, timeout, object/scene variation | p. 7 (IV. EVALUATION), p. 7 (IV. EVALUATION) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (III. APPROACH), p. 4 (III. APPROACH) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (III. APPROACH), p. 4 (III. APPROACH) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| (2) success rate, where a successful case is defined as the normalized distance to the goal state is smaller than 0.1. | definition/direction/unit from same section | p. 6 (IV. EVALUATION) |
| When combined with the heuristic the algorithm [ Where2Act+HP ] can avoid back-and-forth action, however, it is sensitive to error propagation, where one sub-optimal ... | definition/direction/unit from same section | p. 5 (IV. EVALUATION) |
| Note that the error in prismatic joint estimation is higher since these objects often has higher tolerance on the sub-optimal action directions. | definition/direction/unit from same section | p. 7 (IV. EVALUATION) |
| While the algorithm has never been supervised on any of the joint parameters, it is able to estimate the joint axis orientation with an ... | definition/direction/unit from same section | p. 7 (IV. EVALUATION) |
| The model is with binary-classification loss where the action is positive if only the moving distance is larger than a threshold. • Where2Act+HP: an ... | definition/direction/unit from same section | p. 5 (IV. EVALUATION) |
| The performance for this task is measured by (1) normalized distance Egoal to target state after interaction: Egoal = //⃗jend-⃗jgoal/////⃗jgoal-⃗jinit//, where⃗j is vector of ... | definition/direction/unit from same section | p. 6 (IV. EVALUATION) |
| Fig. 2: Approach overview. UMPNet takes visual observation (i.e., RGB-D images) of an articulated object as input and generates a sequence of actions in ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Fig. 4: Open-ended state exploration. Arrow length indicates the inferred distance value, color indicates the inferred AoT label. We visualized the uniform samples to ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to [ AoTOnly ], we can observe that by explicitly predicting the distance value for each action candidate, [ UMPNet ] can better ... | comparison identity and matched condition | p. 5 (IV. EVALUATION) |
| II shows that comparing to prior works [ Inverse ] and other alternative approaches, [ UMPNet ] is able to achieve more precise goal-conditioned ... | comparison identity and matched condition | p. 6 (IV. EVALUATION) |
| Being able to effectively explore the possible states of an object without a specific goal is a critical first step for many robot learning ... | comparison identity and matched condition | p. 5 (IV. EVALUATION) |
| From the qualitative comparisons in Fig. | comparison identity and matched condition | p. 6 (IV. EVALUATION) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Being able to effectively explore the possible states of an object without a specific goal is a critical first step for many robot learning ... | component/input/data sensitivity | p. 5 (IV. EVALUATION) |
| Effect of decomposing AoT and distance prediction. | component/input/data sensitivity | p. 6 (IV. EVALUATION) |
| This heuristic helps to avoid back-and-forth actions, however cannot be applied for goal-conditioned manipulation. • SingleStep: Single-step version of our method that only takes ... | component/input/data sensitivity | p. 5 (IV. EVALUATION) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, we present a unified framework that discovers possible manipulation policies for an articulated object from visual observations. | When combined with heuristic filter, the performance improves slightly. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 7 (IV. EVALUATION), p. 7 (IV. EVALUATION) |
| Primary metric/result | I we can see that [ Where2Act ] is able to achieve similar performance in "single action effects", however, both [ Where2Act ] and ... | numeric claim only at cited anchor | p. 5 (IV. EVALUATION) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EVALUATION - extractive body cue:** There are 504 training object instances, 132 testing object instances from training categories, and 261 object instances in the testing categories.
- **p. 6 / IV. EVALUATION - extractive body cue:** The initial state may be moved to ensure the task can be accomplished in 15 steps.
- **p. 3 / III. APPROACH - extractive body cue:** Our final model uses CEM sampling with 64 samples.
- **p. 4 / III. APPROACH - extractive body cue:** 16 trajectories are collected in each epoch.
- **p. 4 / III. APPROACH - extractive body cue:** After 1000 epochs, it increases by 2 every 400 epochs, until reaching 20. ε-greedy is used during training, where ε decreases linearly from 1 to ...
- **p. 4 / III. APPROACH - extractive body cue:** In position inference, n = 300 and εmin = 0.1.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations and failure cases Assumptions: To allow goal-conditioned manipulation with reversed AoT actions, we assume the action trajectories are bi-directional in time (i.e., they ... | p. 7 (IV. EVALUATION) |
| body limitation/failure cue | Fig. 7: Typical failure cases. UR5 robot, and a suction gripper. Fig. 8 (a) shows the real- world setup. In this experiment, we directly ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Fig. 4: Open-ended state exploration. Arrow length indicates the inferred distance value, color indicates the inferred AoT label. We visualized the uniform samples to ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | I we can see that [ Where2Act ] is able to achieve similar performance in "single action effects", however, both [ Where2Act ] and ... | p. 5 (IV. EVALUATION) |
| body limitation/failure cue | This heuristic helps to avoid back-and-forth actions, however cannot be applied for goal-conditioned manipulation. • SingleStep: Single-step version of our method that only takes ... | p. 5 (IV. EVALUATION) |
| body limitation/failure cue | Fig. 8: Real-world experiment. We test the model trained in simulation on a real-world platform. (a) We an RGB-D camera to capture visual observation ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| (2) Novel state visited - measures the ratio between the number of unique states visited among all interaction steps: ratio = #unique states/#steps. | p. 5 (IV. EVALUATION) |
| I we can see that [ Where2Act ] is able to achieve similar performance in "single action effects", however, both [ Where2Act ] and ... | p. 5 (IV. EVALUATION) |
| The initial state may be moved to ensure the task can be accomplished in 15 steps. | p. 6 (IV. EVALUATION) |
| To compute the prismatic joint, we simply take the average of the action directions. | p. 7 (IV. EVALUATION) |
| To compute the revolute joint, we first compute a common action plane in the 3D space (brown plane in Fig 6). | p. 7 (IV. EVALUATION) |
| 2 as an example, to effectively explore novel states of the object (i.e., a toilet), the algorithm should be able to (a) choose the ... | p. 2 (III. APPROACH) |
| The ground truth label is 1 if and only if the object state is changed in any of the future steps. | p. 3 (III. APPROACH) |
| DistDecoder is a fully-connected neural network trained using MSE loss Ldist for the executed action at. | p. 3 (III. APPROACH) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / IV. EVALUATION - extractive body cue:** Limitations and failure cases Assumptions: To allow goal-conditioned manipulation with reversed AoT actions, we assume the action trajectories are bi-directional in time (i.e., they are ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Typical failure cases. UR5 robot, and a suction gripper. Fig. 8 (a) shows the real- world setup. In this experiment, we directly tested ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Open-ended state exploration. Arrow length indicates the inferred distance value, color indicates the inferred AoT label. We visualized the uniform samples to better ...
- **p. 5 / IV. EVALUATION - extractive body cue:** I we can see that [ Where2Act ] is able to achieve similar performance in "single action effects", however, both [ Where2Act ] and [ ...
- **p. 5 / IV. EVALUATION - extractive body cue:** This heuristic helps to avoid back-and-forth actions, however cannot be applied for goal-conditioned manipulation. • SingleStep: Single-step version of our method that only takes the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Real-world experiment. We test the model trained in simulation on a real-world platform. (a) We an RGB-D camera to capture visual observation and ...

- **Evidence anchors reviewed:** datasets p. 5 (IV. EVALUATION), p. 7 (IV. EVALUATION), p. 7 (IV. EVALUATION), p. 4 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), metrics p. 6 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 7 (IV. EVALUATION), p. 7 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), baselines p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), results p. 5 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 7 (IV. EVALUATION), p. 7 (IV. EVALUATION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** When combined with the heuristic the algorithm [ Where2Act+HP ] can avoid back-and-forth action, however, it is sensitive to error propagation, where one sub-optimal action would affect all following steps ... (p. 5, IV. EVALUATION).
- **Metric evidence:** When combined with the heuristic the algorithm [ Where2Act+HP ] can avoid back-and-forth action, however, it is sensitive to error propagation, where one sub-optimal action would affect all following steps ... (p. 5, IV. EVALUATION).
- **Baseline/ablation evidence:** Compared to [ AoTOnly ], we can observe that by explicitly predicting the distance value for each action candidate, [ UMPNet ] can better differentiate (p. 5, IV. EVALUATION).
- **Failure/negative evidence:** Limitations and failure cases Assumptions: To allow goal-conditioned manipulation with reversed AoT actions, we assume the action trajectories are bi-directional in time (i.e., they are valid in either direction). (p. 7, IV. EVALUATION).
