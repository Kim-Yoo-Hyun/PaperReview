# Evaluation - Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Ma_Hierarchical_Diffusion_Policy_for_Kinematics-Aware_Multi-Task_Robotic_Manipulation_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Ma_Hierarchical_Diffusion_Policy_for_Kinematics-Aware_Multi-Task_Robotic_Manipulation_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Simulation Experiments), p. 8 (Figure/Table caption), p. 6 (5.2. Simulation Experiments), p. 7 (5.2. Simulation Experiments), p. 8 (5.4. Real Robot Experiment), p. 6 (5.1. Trajectory Visualisations)): For red tasks, we expect no improvement of HDP over baselines; with blue tasks, we expect HDP to outperform many of the baselines. reach target take lid off saucepan pick ...

## Evaluation Body Digest

- **p. 4 / 4.1. Dataset Preparation - extractive body cue:** We assume access to a multi-task dataset D = {ξi}ND i=1, containing a total of ND expert demonstrations paired with Dl = {li}ND i=1 language ...
- **p. 6 / 5. Experiments - extractive body cue:** Finally, we show HDP is capable of solving challenging real-world tasks efficiently and effectively on an open oven task with only 20 demonstrations.
- **p. 8 / 5.4. Real Robot Experiment - extractive body cue:** We also conducted a real-world experiment on an opening oven task and a sorting objects into drawer task with a Franka Panda 7 DoF arm.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** For both tasks, the robot needs to accurately predict the trajectories that understand the task context conditioned on languages.
- **p. 6 / 5. Experiments - extractive body cue:** For all simulation experiments, we use 100 demonstrations from RLBench [19] for each task and train for 100K (a) RRT (b) Joint Position (c) RK-Diffuser ...
- **p. 4 / 4.1. Dataset Preparation - extractive body cue:** The observation odemo includes multi-view calibrated RGB-D camera observations and robot states.
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** The Pose Diffusion denotes learning a diffusion policy directly over the end-effector pose trajectories and generate robot controls by solving the inverse kinematics.
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** However, for tasks that require a fine-grained trajectory, e.g., toilet seat up, RRT fails completely.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** 4.1. Dataset Preparation (p. 4); 4.4. Practical Implementation Choices (p. 6); 5. Experiments (p. 6); 5.2. Simulation Experiments (p. 6); 5.4. Real Robot Experiment (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | For red tasks, we expect no improvement of HDP over baselines; with blue tasks, we expect HDP to outperform many of the baselines. reach ... | p. 7 (5.2. Simulation Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. Ablation Study: Success Rates (%) / IK Error Rates (%) of low-level agents with the ground-truth next-best poses. For red tasks, we ... | p. 8 (Figure/Table caption) |
| 5.2. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1, HDP achieves an overall 80.2% success rate across 11 RLBench tasks. | p. 6 (5.2. Simulation Experiments) |
| 5.2. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | For instance, while PerAct + Planner achieves 0% success rate on the open box task it regularly succeeds in grasping the box lid. | p. 7 (5.2. Simulation Experiments) |
| 5.4. Real Robot Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | As a summary, HDP achieves 100% success rate for the opening oven task and 94% success rate for the sorting object into drawer task. | p. 8 (5.4. Real Robot Experiment) |

## Dataset / Benchmark Role

- **p. 4 / 4.1. Dataset Preparation - extractive body cue:** We assume access to a multi-task dataset D = {ξi}ND i=1, containing a total of ND expert demonstrations paired with Dl = {li}ND i=1 language ...
- **p. 6 / 5. Experiments - extractive body cue:** Finally, we show HDP is capable of solving challenging real-world tasks efficiently and effectively on an open oven task with only 20 demonstrations.
- **p. 8 / 5.4. Real Robot Experiment - extractive body cue:** We also conducted a real-world experiment on an opening oven task and a sorting objects into drawer task with a Franka Panda 7 DoF arm.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** For both tasks, the robot needs to accurately predict the trajectories that understand the task context conditioned on languages.
- **p. 6 / 5. Experiments - extractive body cue:** For all simulation experiments, we use 100 demonstrations from RLBench [19] for each task and train for 100K (a) RRT (b) Joint Position (c) RK-Diffuser ...
- **p. 4 / 4.1. Dataset Preparation - extractive body cue:** The observation odemo includes multi-view calibrated RGB-D camera observations and robot states.
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** The Pose Diffusion denotes learning a diffusion policy directly over the end-effector pose trajectories and generate robot controls by solving the inverse kinematics.
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** However, for tasks that require a fine-grained trajectory, e.g., toilet seat up, RRT fails completely.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We introduce HDP, a hierarchical agent for robotic ma- nipulation. At the high-level, HDP learns to predict the next-best end-effector pose. Conditioned on ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. We focus on learning multi-task language-guided agent for robotic manipulation. Unlike a standard motion planner that only samples an arbitrary trajectory to the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Overview of Hierarchical Diffusion Policy (HDP). HDP is a multi-task hierarchical agent for kinematics-aware robotic manip- ulation. HDP consists of two levels: a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Trajectory visualisations of the open box task. iterations. On a real robot, we show HDP can learn effi- ciently and effectively with only ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Success Rates (%) on RLBench Tasks. For red tasks, we expect no improvement of HDP over baselines; with blue tasks, we expect HDP ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Ablation Study: Success Rates (%) / IK Error Rates (%) of low-level agents with the ground-truth next-best poses. For red tasks, we expect ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Real-robot execution sequences. For both tasks, the robot needs to accurately predict the trajectories that understand the task context conditioned on languages. As ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We assume access to a multi-task dataset D = {ξi}ND i=1, containing a total of ND expert demonstrations paired with Dl = {li}ND i=1 ... | embodiment, simulator version and control stack | p. 4 (4.1. Dataset Preparation), p. 6 (5. Experiments) |
| Task/environment | Finally, we show HDP is capable of solving challenging real-world tasks efficiently and effectively on an open oven task with only 20 demonstrations. | reset, timeout, object/scene variation | p. 6 (5. Experiments), p. 8 (5.4. Real Robot Experiment) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 3 (3.1. Diffusion Models), p. 4 (4. Hierarchical Diffusion Policy) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Ablation Study: Success Rates (%) / IK Error Rates (%) of low-level agents with the ground-truth next-best poses. | definition/direction/unit from same section | p. 8 (5.3. Ablation Studies) |
| 1, HDP achieves an overall 80.2% success rate across 11 RLBench tasks. | definition/direction/unit from same section | p. 6 (5.2. Simulation Experiments) |
| For instance, while PerAct + Planner achieves 0% success rate on the open box task it regularly succeeds in grasping the box lid. | definition/direction/unit from same section | p. 7 (5.2. Simulation Experiments) |
| As a summary, HDP achieves 100% success rate for the opening oven task and 94% success rate for the sorting object into drawer task. | definition/direction/unit from same section | p. 8 (5.4. Real Robot Experiment) |
| In addition to this, we perform a series of ablation studies and show: (1) IK errors contribute to the majority of the failure cases ... | definition/direction/unit from same section | p. 6 (5. Experiments) |
| We observe that although Pose Diffusion achieves strong performance on several tasks, e.g., open microwave, it suffers from an overall 24.55% IK error rate. | definition/direction/unit from same section | p. 7 (5.3. Ablation Studies) |
| Figure 1. We introduce HDP, a hierarchical agent for robotic ma- nipulation. At the high-level, HDP learns to predict the next-best end-effector pose. Conditioned ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. We focus on learning multi-task language-guided agent for robotic manipulation. Unlike a standard motion planner that only samples an arbitrary trajectory to ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| HDP outperforms the state-of-the-art methods across RLBench tasks. | comparison identity and matched condition | p. 6 (5.2. Simulation Experiments) |
| For red tasks, we expect no improvement of HDP over baselines; with blue tasks, we expect HDP to outperform many of the baselines. reach ... | comparison identity and matched condition | p. 7 (5.2. Simulation Experiments) |
| Table 2. Ablation Study: Success Rates (%) / IK Error Rates (%) of low-level agents with the ground-truth next-best poses. For red tasks, we ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| More details of the baseline algorithms are available in the appendix. | comparison identity and matched condition | p. 6 (5.2. Simulation Experiments) |
| Hierarchical agents outperform simple low-level continuous control policies. | comparison identity and matched condition | p. 7 (5.2. Simulation Experiments) |
| We observe that both achieve worse performance when compared to the original RK-Diffuser, which indicates that understanding the 3D environment is necessary for generalisable ... | comparison identity and matched condition | p. 8 (5.3. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In addition to this, we perform a series of ablation studies and show: (1) IK errors contribute to the majority of the failure cases ... | component/input/data sensitivity | p. 6 (5. Experiments) |
| Nevertheless, without understanding the task context, the trajectory generated by RRT will cause the lid of the box to fall from the gripper. | component/input/data sensitivity | p. 6 (5.1. Trajectory Visualisations) |
| Sampling-based motion planners might fail without understanding the task context. | component/input/data sensitivity | p. 7 (5.3. Ablation Studies) |
| We perform ablation studies on the selected RLBench tasks to further understand the proposed low-level agent, RKDiffuser. | component/input/data sensitivity | p. 7 (5.3. Ablation Studies) |
| Ablation Study: Success Rates (%) / IK Error Rates (%) of low-level agents with the ground-truth next-best poses. | component/input/data sensitivity | p. 8 (5.3. Ablation Studies) |
| For RKD-RGB, we discard the depth information and use a pretrained ResNet50 to extract the image features; for RKD-ResNet, we ablate using a ResNet ... | component/input/data sensitivity | p. 8 (5.3. Ablation Studies) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce a novel kinematics-aware low-level agent, Robot Kinematics Diffuser (RK-Diffuser), a diffusion-based policy [5] that directly generates the moThis CVPR paper is the ... | For red tasks, we expect no improvement of HDP over baselines; with blue tasks, we expect HDP to outperform many of the baselines. reach ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Simulation Experiments), p. 8 (Figure/Table caption), p. 6 (5.2. Simulation Experiments), p. 7 (5.2. Simulation Experiments), p. 8 (5.4. Real Robot Experiment), p. 6 (5.1. Trajectory Visualisations) |
| Primary metric/result | Table 2. Ablation Study: Success Rates (%) / IK Error Rates (%) of low-level agents with the ground-truth next-best poses. For red tasks, we ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4.3. Low-Level RK-Diffuser - extractive body cue:** For the RGB-D image, we first convert it to a point cloud in the world frame and extract the features with PointNet++ [29]; for the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Although we have demonstrated some robustness of RK-Diffuser to out-of-distribution poses, the nature of behaviour cloning for longer-horizon tasks suggests that error accumulation could ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | In addition to this, we perform a series of ablation studies and show: (1) IK errors contribute to the majority of the failure cases ... | p. 6 (5. Experiments) |
| body limitation/failure cue | The predicted trajectory consistently exceeds the turning radius of the lid hinge, leading to the failure. | p. 7 (5.2. Simulation Experiments) |
| body limitation/failure cue | Specifically, most of the IK errors are caused by invalid quaternions and contribute to 75% of its failure cases. | p. 7 (5.3. Ablation Studies) |
| body limitation/failure cue | Figure 1. We introduce HDP, a hierarchical agent for robotic ma- nipulation. At the high-level, HDP learns to predict the next-best end-effector pose. Conditioned ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Future works could explore improving the framework by designing more unified structures that minimises the compounding error. | p. 8 (6. Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| More implementations and discussions are in the appendix. | p. 6 (4.4. Practical Implementation Choices) |
| For the low-level agent, different from most of the diffusion models that learn to predict a noise prediction model and learn to reconstruct the ... | p. 6 (4.4. Practical Implementation Choices) |
| \vv { a }_ \join t ^ 0 \ left a ro w \v v {a }_\joint ^0 - \alpha \frac {\partial \parallel \vv ... | p. 5 (4.3. Low-Level RK-Diffuser) |
| The forward diffusion processes adds Gaussian noise to x0 in K steps, which gives a sequence of noisy samples {xi}K i=1. | p. 3 (3.1. Diffusion Models) |
| To tackle the large number of visual and language tokens, PerAct adopts PerceiverIO [14], which encodes the inputs with a small set of latent ... | p. 4 (4.2. High-Level Next-Best Pose Agent) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive body cue:** Although we have demonstrated some robustness of RK-Diffuser to out-of-distribution poses, the nature of behaviour cloning for longer-horizon tasks suggests that error accumulation could lead ...
- **p. 6 / 5. Experiments - extractive body cue:** In addition to this, we perform a series of ablation studies and show: (1) IK errors contribute to the majority of the failure cases of ...
- **p. 7 / 5.2. Simulation Experiments - extractive body cue:** The predicted trajectory consistently exceeds the turning radius of the lid hinge, leading to the failure.
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** Specifically, most of the IK errors are caused by invalid quaternions and contribute to 75% of its failure cases.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We introduce HDP, a hierarchical agent for robotic ma- nipulation. At the high-level, HDP learns to predict the next-best end-effector pose. Conditioned on ...
- **p. 8 / 6. Conclusion - extractive body cue:** Future works could explore improving the framework by designing more unified structures that minimises the compounding error.

- **Evidence anchors reviewed:** datasets p. 4 (4.1. Dataset Preparation), p. 6 (5. Experiments), p. 8 (5.4. Real Robot Experiment), p. 8 (5.3. Ablation Studies), p. 6 (5. Experiments), p. 4 (4.1. Dataset Preparation), metrics p. 8 (5.3. Ablation Studies), p. 6 (5.2. Simulation Experiments), p. 7 (5.2. Simulation Experiments), p. 8 (5.4. Real Robot Experiment), p. 6 (5. Experiments), p. 7 (5.3. Ablation Studies), baselines p. 6 (5.2. Simulation Experiments), p. 7 (5.2. Simulation Experiments), p. 8 (Figure/Table caption), p. 6 (5.2. Simulation Experiments), p. 7 (5.2. Simulation Experiments), p. 8 (5.3. Ablation Studies), results p. 7 (5.2. Simulation Experiments), p. 8 (Figure/Table caption), p. 6 (5.2. Simulation Experiments), p. 7 (5.2. Simulation Experiments), p. 8 (5.4. Real Robot Experiment), p. 6 (5.1. Trajectory Visualisations).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
