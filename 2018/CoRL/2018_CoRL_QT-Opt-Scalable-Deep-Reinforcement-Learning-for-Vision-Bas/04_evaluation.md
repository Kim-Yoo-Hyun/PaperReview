# Evaluation - QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1806.10293; PDF retrieval source: https://arxiv.org/pdf/1806.10293. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 7 (Method), p. 8 (Method), p. 12 (Figure/Table caption), p. 17 (Figure/Table caption), p. 14 (Figure/Table caption)): Table 1: Quantitative results in terms of grasp success rate on test objects. Policies are evaluated with object replacement (test) and without (bin emptying), with the latter showing success rates ...

## Evaluation Body Digest

- **p. 8 / Method - extractive PDF cue:** Our results demonstrate that reinforcement learning with vision-based inputs can scale to large datasets and very large models, and can enable policies that generalize effectively ...
- **p. 8 / Method - extractive PDF cue:** Although our policies are trained on a large amount of robot experience (580k real-world grasps), all of this experience is collected autonomously with minimal human ...
- **p. 7 / Method - extractive PDF cue:** Here, a single robot unloads a cluttered bin filled with 28 test objects, using 30 grasp attempts.
- **p. 7 / Method - extractive PDF cue:** [27] 400k grasps from our dataset 67% Table 1: Quantitative results in terms of grasp success rate on test objects.
- **p. 17 / Figure/Table caption - extractive PDF cue:** Table 8: Data efficiency comparison in simulation. We argue that the algorithm from Levine et al. [27] is less data efficient because it optimizes a ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 9: Comparison of DQN methods. See Appendix F.4 for clipped Double DQN definition. the gripper aperture and distance between the gripper and the floor. ...
- **p. 7 / Method - extractive PDF cue:** The success rate of our method in both cases is very high.
- **p. 8 / Method - extractive PDF cue:** We apply this framework to the task of grasping, learning closed-loop vision-based policies that attain a high success rate on previously unseen objects, and exhibit ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** B Exploration and Dataset Bootstrapping (p. 14).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Quantitative results in terms of grasp success rate on test objects. Policies are evaluated with object replacement (test) and without (bin emptying), ... | p. 7 (Figure/Table caption) |
| Method | EMPIRICAL / REAL-ROBOT OR HARDWARE | The success rate of our method in both cases is very high. | p. 7 (Method) |
| Method | EMPIRICAL / REAL-ROBOT OR HARDWARE | We apply this framework to the task of grasping, learning closed-loop vision-based policies that attain a high success rate on previously unseen objects, and ... | p. 8 (Method) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4: Off-policy and on-policy ablation of termination condition. Quantitative experiments The performance of our algorithm is evaluated empirically in a set of grasping ... | p. 12 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 8: Data efficiency comparison in simulation. We argue that the algorithm from Levine et al. [27] is less data efficient because it optimizes ... | p. 17 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / Method - extractive PDF cue:** Our results demonstrate that reinforcement learning with vision-based inputs can scale to large datasets and very large models, and can enable policies that generalize effectively ...
- **p. 8 / Method - extractive PDF cue:** Although our policies are trained on a large amount of robot experience (580k real-world grasps), all of this experience is collected autonomously with minimal human ...
- **p. 7 / Method - extractive PDF cue:** Here, a single robot unloads a cluttered bin filled with 28 test objects, using 30 grasp attempts.
- **p. 7 / Method - extractive PDF cue:** [27] 400k grasps from our dataset 67% Table 1: Quantitative results in terms of grasp success rate on test objects.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Seven robots are set up to collect grasping episodes with autonomous self-supervision. We study how off-policy deep reinforcement learning can acquire closed-loop dynamic ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: Close-up of a robot cell in our setup (left) and about 1000 visually and physically diverse training ob- jects (right). Each cell (left) ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3: Our distributed RL infrastructure for QT-Opt (see Sec. 4.2). State-action-reward tuples are loaded from an offline data stored and pushed from online real ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative results in terms of grasp success rate on test objects. Policies are evaluated with object replacement (test) and without (bin emptying), with ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Eight grasps from the QT-Opt policy, illustrating some of the strategies discovered by our method: pregrasp manipulation (a, b), grasp readjustment (c, d), ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 2: Off-policy ablation over state representation. Discount and Reward Definition To encourage faster grasps, we experimented with decreasing discount and adding a small reward ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 3: Off-policy ablation over discount and reward. Learned Termination We compare a task-specific scripted termination condition with a task- agnostic termination action learned by ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 4: Off-policy and on-policy ablation of termination condition. Quantitative experiments The performance of our algorithm is evaluated empirically in a set of grasping experiments. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our results demonstrate that reinforcement learning with vision-based inputs can scale to large datasets and very large models, and can enable policies that generalize ... | embodiment, simulator version and control stack | p. 8 (Method), p. 8 (Method) |
| Task/environment | Although our policies are trained on a large amount of robot experience (580k real-world grasps), all of this experience is collected autonomously with minimal ... | reset, timeout, object/scene variation | p. 8 (Method), p. 7 (Method) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 8 (Method), p. 2 (1 Introduction) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 2 (1 Introduction), p. 7 (Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 8: Data efficiency comparison in simulation. We argue that the algorithm from Levine et al. [27] is less data efficient because it optimizes ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Table 1: Quantitative results in terms of grasp success rate on test objects. Policies are evaluated with object replacement (test) and without (bin emptying), ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 9: Comparison of DQN methods. See Appendix F.4 for clipped Double DQN definition. the gripper aperture and distance between the gripper and the ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| The success rate of our method in both cases is very high. | definition/direction/unit from same section | p. 7 (Method) |
| We apply this framework to the task of grasping, learning closed-loop vision-based policies that attain a high success rate on previously unseen objects, and ... | definition/direction/unit from same section | p. 8 (Method) |
| Figure 3: Our distributed RL infrastructure for QT-Opt (see Sec. 4.2). State-action-reward tuples are loaded from an offline data stored and pushed from online ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Table 7: Simulation studies for tuning grasping task parameters The results in Table 7 show that richer state representation results in faster convergence and ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Figure 12: Grasp success is determined by subtracting images before an object is dropped into the bin (left) and after it was dropped (right). ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 5: Off-policy performance with and without clipped Double-Q Learning. Data efficiency As discussed in Section 5 we collected 580k grasp attempts across 7 ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| Figure 9: Comparison of DQN methods. See Appendix F.4 for clipped Double DQN definition. the gripper aperture and distance between the gripper and the ... | comparison identity and matched condition | p. 16 (Figure/Table caption) |
| Table 1: Quantitative results in terms of grasp success rate on test objects. Policies are evaluated with object replacement (test) and without (bin emptying), ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 4: Off-policy and on-policy ablation of termination condition. Quantitative experiments The performance of our algorithm is evaluated empirically in a set of grasping ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |
| To compare our method to prior work, we evaluated the technique proposed by Levine et al. | comparison identity and matched condition | p. 7 (Method) |
| Table 2: Off-policy ablation over state representation. Discount and Reward Definition To encourage faster grasps, we experimented with decreasing discount and adding a small ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 1: Quantitative results in terms of grasp success rate on test objects. Policies are evaluated with object replacement (test) and without (bin emptying), ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 4: Off-policy and on-policy ablation of termination condition. Quantitative experiments The performance of our algorithm is evaluated empirically in a set of grasping ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| The results show both a variant of our method that is trained entirely using off-policy data, without any additional data collection from the latest ... | component/input/data sensitivity | p. 7 (Method) |
| Table 8: Data efficiency comparison in simulation. We argue that the algorithm from Levine et al. [27] is less data efficient because it optimizes ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| Table 2: Off-policy ablation over state representation. Discount and Reward Definition To encourage faster grasps, we experimented with decreasing discount and adding a small ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Table 5: Off-policy performance with and without clipped Double-Q Learning. Data efficiency As discussed in Section 5 we collected 580k grasp attempts across 7 ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We show that our method attains a high success rate across a range of objects not seen during training, and our qualitative experiments show ... | Table 1: Quantitative results in terms of grasp success rate on test objects. Policies are evaluated with object replacement (test) and without (bin emptying), ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 7 (Method), p. 8 (Method), p. 12 (Figure/Table caption), p. 17 (Figure/Table caption), p. 14 (Figure/Table caption) |
| Primary metric/result | The success rate of our method in both cases is very high. | numeric claim only at cited anchor | p. 7 (Method) |

- Numeric sentences retained from the body:
- **p. 7 / Method - extractive PDF cue:** On the bin emptying experiment, our method emptied the bin in 30 grasps or less in 2 of the 5 trials, while the prior method ...
- **p. 7 / Method - extractive PDF cue:** On the bin emptying experiment, our method emptied the bin in 30 grasps or less in 2 of the 5 trials, while the prior method ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 5: Illustrations of the bin emptying experiment (a). The (a, right) shows a very small object getting stuck in the corner and requiring ... | p. 13 (Figure/Table caption) |
| body limitation/failure cue | Figure 4: Eight grasps from the QT-Opt policy, illustrating some of the strategies discovered by our method: pregrasp manipulation (a, b), grasp readjustment (c, ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | The variant of our method that uses on-policy joint finetuning has a failure rate more than four times lower than prior work on the ... | p. 7 (Method) |
| body limitation/failure cue | Although the policy was usually successful, we did observe a few failure cases. | p. 8 (Method) |
| body limitation/failure cue | 4 (c), we show examples where the policy repeatedly regrasps a slippery object on the floor, while in Fig. | p. 7 (Method) |
| body limitation/failure cue | This penalty may in principle result in target values outside of [0, 1], though we found empirically that this does not happen. | p. 6 (2 Related Work) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Effective off-policy training is valuable as it allows for rapid iteration on hyperparameters and architecture design without any data collection. | p. 7 (Method) |
| On the bin emptying experiment, our method emptied the bin in 30 grasps or less in 2 of the 5 trials, while the prior ... | p. 7 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 5: Illustrations of the bin emptying experiment (a). The (a, right) shows a very small object getting stuck in the corner and requiring a ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Eight grasps from the QT-Opt policy, illustrating some of the strategies discovered by our method: pregrasp manipulation (a, b), grasp readjustment (c, d), ...
- **p. 7 / Method - extractive PDF cue:** The variant of our method that uses on-policy joint finetuning has a failure rate more than four times lower than prior work on the test ...
- **p. 8 / Method - extractive PDF cue:** Although the policy was usually successful, we did observe a few failure cases.
- **p. 7 / Method - extractive PDF cue:** 4 (c), we show examples where the policy repeatedly regrasps a slippery object on the floor, while in Fig.
- **p. 6 / 2 Related Work - extractive PDF cue:** This penalty may in principle result in target values outside of [0, 1], though we found empirically that this does not happen.

- **PDF anchors reviewed:** datasets p. 8 (Method), p. 8 (Method), p. 7 (Method), p. 7 (Method), metrics p. 17 (Figure/Table caption), p. 7 (Figure/Table caption), p. 16 (Figure/Table caption), p. 7 (Method), p. 8 (Method), p. 3 (Figure/Table caption), baselines p. 14 (Figure/Table caption), p. 16 (Figure/Table caption), p. 7 (Figure/Table caption), p. 12 (Figure/Table caption), p. 7 (Method), p. 12 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 7 (Method), p. 8 (Method), p. 12 (Figure/Table caption), p. 17 (Figure/Table caption), p. 14 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
