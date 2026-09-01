# Evaluation - Momentum Control with Hierarchical Inverse Dynamics on a Torque-Controlled Humanoid

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1410.7284; PDF retrieval source: https://arxiv.org/pdf/1410.7284. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.2 Low-level torque control), p. 8 (4.2 Low-level torque control), p. 13 (5.3 Tracking Experiments in Double Support), p. 13 (5.3 Tracking Experiments in Double Support), p. 7 (4 Experimental Setup), p. 10 (5.2 Balance Control Experiments)): This controller design allowed us to achieve good torque tracking performance.

## Evaluation Body Digest

- **p. 9 / 5.1 Processing Time - extractive PDF cue:** In the following, however, we construct a more complex stepping task in simulation for the full 25 DoF robot.
- **p. 15 / 5.4 Single Support Experiments - extractive PDF cue:** Indeed, while in simulation Cartesian tracking is perfect, on the real robot the tracking performance of the Cartesian task of the swing foot is not ...
- **p. 9 / 5.1 Processing Time - extractive PDF cue:** Going from a 14 DoF robot to a 25 DoF robot with similar task setup makes the peak computation time rise from 1ms to 3ms.
- **p. 11 / 5.2.2 Comparison of momentum controllers - extractive PDF cue:** For both momentum control tasks, the robot was able to withstand impacts with high peak forces and strong impulses without falling.
- **p. 15 / 5.4 Single Support Experiments - extractive PDF cue:** The goal of this experiment is to show that the controller can handle more complicated tasks involving contact switching and that the robot is able ...
- **p. 16 / 5.4 Single Support Experiments - extractive PDF cue:** While the robot is performing the task, it is pushed strongly at the hip from the front as can be seen in the video.
- **p. 7 / 4.1 Sarcos Humanoid Robot - extractive PDF cue:** The legs of the robot are 0.82m high.
- **p. 7 / 4.1 Sarcos Humanoid Robot - extractive PDF cue:** Moving the CoP across this link makes the foot bend and causes the robot to fall.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 4 Experimental Setup (p. 7); 4.5 Experimental tools (p. 8); 5 Experiments (p. 8); 5.2 Balance Control Experiments (p. 10); 5.3 Tracking Experiments in Double Support (p. 13); 5.4 Single Support Experiments (p. 15).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2 Low-level torque control | EMPIRICAL / REAL-ROBOT OR HARDWARE | This controller design allowed us to achieve good torque tracking performance. | p. 8 (4.2 Low-level torque control) |
| 4.2 Low-level torque control | EMPIRICAL / REAL-ROBOT OR HARDWARE | It is important to note that such performance was necessary to achieve good performance in the hierarchical inverse dynamics controller. | p. 8 (4.2 Low-level torque control) |
| 5.3 Tracking Experiments in Double Support | EMPIRICAL / REAL-ROBOT OR HARDWARE | As a consequence, the tracking of the CoG, which is in a lower priority, is not ideal but still achieves a reasonable performance. | p. 13 (5.3 Tracking Experiments in Double Support) |
| 5.3 Tracking Experiments in Double Support | EMPIRICAL / REAL-ROBOT OR HARDWARE | CoG velocity tracking is still achieved reasonably well. | p. 13 (5.3 Tracking Experiments in Double Support) |
| 4 Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | They should also ease the reproduction of the experimental results on other platforms. | p. 7 (4 Experimental Setup) |

## Dataset / Benchmark Role

- **p. 9 / 5.1 Processing Time - extractive PDF cue:** In the following, however, we construct a more complex stepping task in simulation for the full 25 DoF robot.
- **p. 15 / 5.4 Single Support Experiments - extractive PDF cue:** Indeed, while in simulation Cartesian tracking is perfect, on the real robot the tracking performance of the Cartesian task of the swing foot is not ...
- **p. 9 / 5.1 Processing Time - extractive PDF cue:** Going from a 14 DoF robot to a 25 DoF robot with similar task setup makes the peak computation time rise from 1ms to 3ms.
- **p. 11 / 5.2.2 Comparison of momentum controllers - extractive PDF cue:** For both momentum control tasks, the robot was able to withstand impacts with high peak forces and strong impulses without falling.
- **p. 15 / 5.4 Single Support Experiments - extractive PDF cue:** The goal of this experiment is to show that the controller can handle more complicated tasks involving contact switching and that the robot is able ...
- **p. 16 / 5.4 Single Support Experiments - extractive PDF cue:** While the robot is performing the task, it is pushed strongly at the hip from the front as can be seen in the video.
- **p. 7 / 4.1 Sarcos Humanoid Robot - extractive PDF cue:** The legs of the robot are 0.82m high.
- **p. 7 / 4.1 Sarcos Humanoid Robot - extractive PDF cue:** Moving the CoP across this link makes the foot bend and causes the robot to fall.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In the following, however, we construct a more complex stepping task in simulation for the full 25 DoF robot. | embodiment, simulator version and control stack | p. 9 (5.1 Processing Time), p. 15 (5.4 Single Support Experiments) |
| Task/environment | Indeed, while in simulation Cartesian tracking is perfect, on the real robot the tracking performance of the Cartesian task of the swing foot is ... | reset, timeout, object/scene variation | p. 15 (5.4 Single Support Experiments), p. 9 (5.1 Processing Time) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 3 (2.1 Modelling Assumptions and Problem Formulation) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| It can be seen that overall the CoG error remains lower with the LQR controller, while the angular momentum behaves similarly. disturbance. | definition/direction/unit from same section | p. 11 (5.2.2 Comparison of momentum controllers) |
| For every push, the change in momentum was damped out quickly and the CoG was tracked after an initial 1.3 2.5 3.8 5.0 CoG ... | definition/direction/unit from same section | p. 11 (5.2.2 Comparison of momentum controllers) |
| An accurate estimation of the floating base pose and twist is important for a good performance of the inverse dynamics controller. | definition/direction/unit from same section | p. 8 (4.3 State estimation) |
| 2 Example of torque tracking performance during a balancing experiment. | definition/direction/unit from same section | p. 8 (4.1 Sarcos Humanoid Robot) |
| In our experiments with a 14 DoF robot, this speedup allows us to run a 1 kHz control-loop as we will demonstrate in the ... | definition/direction/unit from same section | p. 9 (5.1 Processing Time) |
| First, we compare the performance of the balance control when using the LQR 1 2 3 4 5 6 1.5 2 2.5 3 3.5 ... | definition/direction/unit from same section | p. 10 (5.2 Balance Control Experiments) |
| With the proposed decomposition we decreased the computation time by approximately 40%. design and the PD controller described in Section 3 and then test ... | definition/direction/unit from same section | p. 10 (5.2 Balance Control Experiments) |
| As a consequence, the tracking of the CoG, which is in a lower priority, is not ideal but still achieves a reasonable performance. | definition/direction/unit from same section | p. 13 (5.3 Tracking Experiments in Double Support) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| It is worth mentioning again that the foot size of the robot is rather small compared to other humanoids. | comparison identity and matched condition | p. 16 (5.4 Single Support Experiments) |
| We expect to have even better performance once we perform a good identification of the dynamics [1,24] but it is interesting to note that ... | comparison identity and matched condition | p. 8 (4.4 Dynamic model) |
| It would not have been possible by using this algorithm without the simplification. | comparison identity and matched condition | p. 9 (5.1 Processing Time) |
| 2.1 3 3 eq PD control on CoG (2 -c) × 6 PD control on swing foot 4 25 + 6 eq PD control ... | comparison identity and matched condition | p. 9 (5.1 Processing Time) |
| 5 Processing time of a stepping task (see Table 1) using the decomposition proposed in Section 2.3 (red) and the same task performed without ... | comparison identity and matched condition | p. 10 (5.2 Balance Control Experiments) |
| For both momentum control tasks, the robot was able to withstand impacts with high peak forces and strong impulses without falling. | comparison identity and matched condition | p. 11 (5.2.2 Comparison of momentum controllers) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We expect to have even better performance once we perform a good identification of the dynamics [1,24] but it is interesting to note that ... | component/input/data sensitivity | p. 8 (4.4 Dynamic model) |
| It would not have been possible by using this algorithm without the simplification. | component/input/data sensitivity | p. 9 (5.1 Processing Time) |
| The proposed decomposition removed 25 equality constraints and 25 optimization variables. | component/input/data sensitivity | p. 9 (5.1 Processing Time) |
| 5 Processing time of a stepping task (see Table 1) using the decomposition proposed in Section 2.3 (red) and the same task performed without ... | component/input/data sensitivity | p. 10 (5.2 Balance Control Experiments) |
| For both momentum control tasks, the robot was able to withstand impacts with high peak forces and strong impulses without falling. | component/input/data sensitivity | p. 11 (5.2.2 Comparison of momentum controllers) |
| Then an unloading phase occurs during which the contact force regularization enforces a zero contact force to guarantee a continuous transition when the double ... | component/input/data sensitivity | p. 15 (5.4 Single Support Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This leads us to the main contribution of this paper, where we show experiments with extensive quantitative analysis for various tasks (Sections 4 and ... | This controller design allowed us to achieve good torque tracking performance. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.2 Low-level torque control), p. 8 (4.2 Low-level torque control), p. 13 (5.3 Tracking Experiments in Double Support), p. 13 (5.3 Tracking Experiments in Double Support), p. 7 (4 Experimental Setup), p. 10 (5.2 Balance Control Experiments) |
| Primary metric/result | It is important to note that such performance was necessary to achieve good performance in the hierarchical inverse dynamics controller. | numeric claim only at cited anchor | p. 8 (4.2 Low-level torque control) |

- Numeric sentences retained from the body:
- **p. 9 / 5.1 Processing Time - extractive PDF cue:** 2.1 3 3 eq PD control on CoG (2 -c) × 6 PD control on swing foot 4 25 + 6 eq PD control on ...
- **p. 9 / 5.1 Processing Time - extractive PDF cue:** Going from a 14 DoF robot to a 25 DoF robot with similar task setup makes the peak computation time rise from 1ms to 3ms.
- **p. 11 / 5.2.1 Specification of the tasks - extractive PDF cue:** (24) or (23) 14 + 6 eq PD control on posture 2 × 6 eq regularizer on GRFs DoFs: 14 max. time: 0.9 ms Table ...
- **p. 11 / 5.2.2 Comparison of momentum controllers - extractive PDF cue:** The robot was pushed at 4 points on the torso above the hip (from the front, right, back and left) and at 3 points at ...
- **p. 11 / 5.2.2 Comparison of momentum controllers - extractive PDF cue:** At each of the 7 points we applied 4 pushes of increasing impact up to peak forces of 290 N and impulses of 9.5 Ns, ...
- **p. 13 / 5.3 Tracking Experiments in Double Support - extractive PDF cue:** We keep the same task hierarchy as in the balance experiments (see Table 2) and make the CoG track sine curves of 0.3 Hz and ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Also, separating the EoM from kinematic contact constraints allows to keep solutions consistent with the dynamics even in postures where the feet cannot be ... | p. 17 (6.2 Relation to other balancing approaches) |
| body limitation/failure cue | On the other hand, it allows for prioritization of inequality constraints, which we exploit e.g. to give more importance to hardware limitations than to ... | p. 17 (6.3 Relations to other hierarchical inverse dynamics) |
| body limitation/failure cue | The bottom plot shows the CoP of the stance foot, which saturates close to the heel during the push, such that the foot does ... | p. 16 (6.1 Task design and hierarchies) |
| body limitation/failure cue | Moving the CoP across this link makes the foot bend and causes the robot to fall. | p. 7 (4.1 Sarcos Humanoid Robot) |
| body limitation/failure cue | These details are important in order to understand the strengths and limitations of the presented experiments. | p. 7 (4 Experimental Setup) |
| body limitation/failure cue | The highest two priorities satisfy hardware limitations and dynamic constraints, the third priority task tracks a predefined center of gravity and swing foot motion ... | p. 9 (5.1 Processing Time) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We used a computer running a linux kernel patched with Xenomai 2.6.3 for real-time capabilities. | p. 7 (4.1 Sarcos Humanoid Robot) |
| An offboard computer sends control commands to the robot and receives sensor information in real-time at 1 kHz. | p. 7 (4.1 Sarcos Humanoid Robot) |
| The controller essentially computes desired flow directly in terms of valve current. | p. 8 (4.2 Low-level torque control) |
| For all the experiments, we run the hierarchical inverse 4 The movie is also available on www.youtube.com/ watch?v=jMj3Uv2Q8Xg | p. 8 (5 Experiments) |
| All experiments were performed on an Intel Core i7-2600 CPU with a 3.40GHz processor. | p. 9 (5.1 Processing Time) |
| The desired torque commands computed by the controller are directly sent to the robot. | p. 9 (5 Experiments) |
| Concerning computation time, the controller computes a solution in average well below 1ms but a maximum at 1.05ms is reached a few times during ... | p. 15 (5.4 Single Support Experiments) |
| The same is true for joint limits, which can be written as ¨qmin ≤¨qj ≤¨qmax, where the bounds are computed in the form ¨qmin/max ... | p. 3 (2.1 Modelling Assumptions and Problem Formulation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 17 / 6.2 Relation to other balancing approaches - extractive PDF cue:** Also, separating the EoM from kinematic contact constraints allows to keep solutions consistent with the dynamics even in postures where the feet cannot be kept ...
- **p. 17 / 6.3 Relations to other hierarchical inverse dynamics - extractive PDF cue:** On the other hand, it allows for prioritization of inequality constraints, which we exploit e.g. to give more importance to hardware limitations than to contact ...
- **p. 16 / 6.1 Task design and hierarchies - extractive PDF cue:** The bottom plot shows the CoP of the stance foot, which saturates close to the heel during the push, such that the foot does not ...
- **p. 7 / 4.1 Sarcos Humanoid Robot - extractive PDF cue:** Moving the CoP across this link makes the foot bend and causes the robot to fall.
- **p. 7 / 4 Experimental Setup - extractive PDF cue:** These details are important in order to understand the strengths and limitations of the presented experiments.
- **p. 9 / 5.1 Processing Time - extractive PDF cue:** The highest two priorities satisfy hardware limitations and dynamic constraints, the third priority task tracks a predefined center of gravity and swing foot motion and ...

- **PDF anchors reviewed:** datasets p. 9 (5.1 Processing Time), p. 15 (5.4 Single Support Experiments), p. 9 (5.1 Processing Time), p. 11 (5.2.2 Comparison of momentum controllers), p. 15 (5.4 Single Support Experiments), p. 16 (5.4 Single Support Experiments), metrics p. 11 (5.2.2 Comparison of momentum controllers), p. 11 (5.2.2 Comparison of momentum controllers), p. 8 (4.3 State estimation), p. 8 (4.1 Sarcos Humanoid Robot), p. 9 (5.1 Processing Time), p. 10 (5.2 Balance Control Experiments), baselines p. 16 (5.4 Single Support Experiments), p. 8 (4.4 Dynamic model), p. 9 (5.1 Processing Time), p. 9 (5.1 Processing Time), p. 10 (5.2 Balance Control Experiments), p. 11 (5.2.2 Comparison of momentum controllers), results p. 8 (4.2 Low-level torque control), p. 8 (4.2 Low-level torque control), p. 13 (5.3 Tracking Experiments in Double Support), p. 13 (5.3 Tracking Experiments in Double Support), p. 7 (4 Experimental Setup), p. 10 (5.2 Balance Control Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
