# Evaluation - HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10011640; PDF retrieval source: https://arxiv.org/pdf/2503.00923. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 20 (Figure/Table caption), p. 8 (5 Experiment), p. 8 (5 Experiment), p. 7 (5 Experiment), p. 7 (5 Experiment), p. 20 (Figure/Table caption)): Figure 9: Extreme State: Policy's state distribution in the extreme cases A.8 History Length Experiments We investigate the impact of observation history length on HWC-Loco's performance. Setting H = 10 ...

## Evaluation Body Digest

- **p. 9 / 5 Experiment - extractive body cue:** Second, the humanoid robot used in real-world deployment has only 19 degrees of freedom, which limits whole-body coordination and constrains the expression of complex recovery ...
- **p. 7 / 5 Experiment - extractive body cue:** [64] b) Goal Tracking performance: The ability to accurately follow velocity commands by maximizing task rewards rT detailed in Appendix A.2 [43]. c) Human-Like behavior: ...
- **p. 7 / 5 Experiment - extractive body cue:** 2) Robustness: How well can HWC-Loco stabilize the humanoid robot under varying levels of disturbance?
- **p. 8 / 5 Experiment - extractive body cue:** When faced with challenging terrain, the robot prioritizes safety by activating the recovery policy.
- **p. 8 / 5 Experiment - extractive body cue:** 2) Impulse disturbances on the CoM, implemented by directly altering the robot's CoM velocity [65, 28].
- **p. 9 / 5 Experiment - extractive body cue:** We deploy HWC-Loco on a real humanoid robot and evaluate its performance under various external force disturbances.
- **p. 16 / A.2 Implementation Details - extractive body cue:** The objective is to enable the robot to track goal commands across a variety of terrains.
- **p. 16 / A.2 Implementation Details - extractive body cue:** We train this high-level policy in the simulation environment mentioned detailed in Section 4.2, focusing on locomotion goals as the primary task.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 5 Experiment (p. 7); A.2 Implementation Details (p. 15); A.8 History Length Experiments (p. 20); B Experiment (p. 21); B.1 H1 Experiments (p. 21); B.2 G1 Experiments (p. 24).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 9: Extreme State: Policy's state distribution in the extreme cases A.8 History Length Experiments We investigate the impact of observation history length on ... | p. 20 (Figure/Table caption) |
| 5 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | HWC-Loco reaches a success rate of 81.27%, outperforming all baselines by a significant margin. | p. 8 (5 Experiment) |
| 5 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 2, HWC-Loco consistently achieves the highest success rates across all types of disturbances. | p. 8 (5 Experiment) |
| 5 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, in the high-speed stair terrain setting, HWC-Loco has a significantly higher success rate than all other policies, although its goal-tracking ability slightly decreases. | p. 7 (5 Experiment) |
| 5 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our evaluation metric includes a) Success Rate: The proportion of successful traverse across different scenarios. | p. 7 (5 Experiment) |

## Dataset / Benchmark Role

- **p. 9 / 5 Experiment - extractive body cue:** Second, the humanoid robot used in real-world deployment has only 19 degrees of freedom, which limits whole-body coordination and constrains the expression of complex recovery ...
- **p. 7 / 5 Experiment - extractive body cue:** [64] b) Goal Tracking performance: The ability to accurately follow velocity commands by maximizing task rewards rT detailed in Appendix A.2 [43]. c) Human-Like behavior: ...
- **p. 7 / 5 Experiment - extractive body cue:** 2) Robustness: How well can HWC-Loco stabilize the humanoid robot under varying levels of disturbance?
- **p. 8 / 5 Experiment - extractive body cue:** When faced with challenging terrain, the robot prioritizes safety by activating the recovery policy.
- **p. 8 / 5 Experiment - extractive body cue:** 2) Impulse disturbances on the CoM, implemented by directly altering the robot's CoM velocity [65, 28].
- **p. 9 / 5 Experiment - extractive body cue:** We deploy HWC-Loco on a real humanoid robot and evaluate its performance under various external force disturbances.
- **p. 16 / A.2 Implementation Details - extractive body cue:** The objective is to enable the robot to track goal commands across a variety of terrains.
- **p. 16 / A.2 Implementation Details - extractive body cue:** We train this high-level policy in the simulation environment mentioned detailed in Section 4.2, focusing on locomotion goals as the primary task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: An example of recovering from a Hard Kick: The humanoid robot withstands external disturbance by automatically detecting hazardous states and adjusting its motion ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Overview of HWC-Loco: The framework consists of two stages: (a) Training goal-tracking policy to effectively enable human-like locomotion across diverse terrains (Section 4.1) ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Proportion of goal-tracking policy. While the low-level policies can achieve varying lev- els of optimality, a fundamental challenge is coor- dinating these policies ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Locomotion performance in simulated environments. Each evaluation runs for 1200 steps, which is equivalent to 12 seconds of real clock time.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Robustness of Locomotion across Various Terrains under Different Disturbances Policy External Force/Torque Disturbances Impulse Disturbances on CoM Payload on Upper Body Low-freq. ↑ ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Comparison of Embodiments Success Rate ↑ Goal Tracking ↑ Human-like ↓ Unitree H1 97.13 ± 0.43 1.10 ± 0.00 3.18 ± 0.01
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Motion Tracking under Disturbances Punching ↑ Dancing ↑ Expressive Walking ↑ HWC-Loco 94.01 ± 0.49 86.44 ± 0.60 94.53 ± 0.23
- **p. 15 / Figure/Table caption - extractive body cue:** Table 5: Double-DQN Parameters Parameter Value Batch Size 128 Learning Rate 1e-4 Gamma

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Second, the humanoid robot used in real-world deployment has only 19 degrees of freedom, which limits whole-body coordination and constrains the expression of complex ... | embodiment, simulator version and control stack | p. 9 (5 Experiment), p. 7 (5 Experiment) |
| Task/environment | [64] b) Goal Tracking performance: The ability to accurately follow velocity commands by maximizing task rewards rT detailed in Appendix A.2 [43]. c) Human-Like ... | reset, timeout, object/scene variation | p. 7 (5 Experiment), p. 7 (5 Experiment) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 16 (A.2 Implementation Details), p. 15 (A.2 Implementation Details) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 15 (A.2 Implementation Details), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 9: Extreme State: Policy's state distribution in the extreme cases A.8 History Length Experiments We investigate the impact of observation history length on ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Under low-impulse disturbances, all methods maintain relatively high success rates, with HWC-Loco again achieving the best performance at 94.84%. | definition/direction/unit from same section | p. 8 (5 Experiment) |
| Specifically, under constant disturbances, HWC-Loco demonstrates superior performance with a success rate of 75.95%, which is nearly 25% higher than that of DreamWaQ. | definition/direction/unit from same section | p. 8 (5 Experiment) |
| [64] b) Goal Tracking performance: The ability to accurately follow velocity commands by maximizing task rewards rT detailed in Appendix A.2 [43]. c) Human-Like ... | definition/direction/unit from same section | p. 7 (5 Experiment) |
| Our evaluation metric includes a) Success Rate: The proportion of successful traverse across different scenarios. | definition/direction/unit from same section | p. 7 (5 Experiment) |
| The success rates are reported in Table 4. | definition/direction/unit from same section | p. 9 (5 Experiment) |
| Table 14: Performance comparison with different history lengths (H) History Length Success Rate ↑ Goal-tracking ↑ Human-like ↓ 1 95.13 ± 0.51 1.07 ± ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| As a result, this reward term serves as a back-tracking reward for the safety recovery mechanism, encouraging it to return to a stable goal-tracking ... | definition/direction/unit from same section | p. 17 (A.2 Implementation Details) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| HWC-Loco reaches a success rate of 81.27%, outperforming all baselines by a significant margin. | comparison identity and matched condition | p. 8 (5 Experiment) |
| As shown in Table 3, G1 outperforms H1 across all metrics. | comparison identity and matched condition | p. 9 (5 Experiment) |
| A domain-randomized motion tracking policy serves as the baseline. | comparison identity and matched condition | p. 9 (5 Experiment) |
| To evaluate the effectiveness of different components in HWC-Loco, we design a comparison method using an ablation approach as follows: 1) HWC-Loco-l sets α ... | comparison identity and matched condition | p. 7 (5 Experiment) |
| To enable a comprehensive comparison, evaluations are performed under both low-speed and high-speed command conditions. | comparison identity and matched condition | p. 7 (5 Experiment) |
| Table 14: Performance comparison with different history lengths (H) History Length Success Rate ↑ Goal-tracking ↑ Human-like ↓ 1 95.13 ± 0.51 1.07 ± ... | comparison identity and matched condition | p. 20 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To evaluate the effectiveness of different components in HWC-Loco, we design a comparison method using an ablation approach as follows: 1) HWC-Loco-l sets α ... | component/input/data sensitivity | p. 7 (5 Experiment) |
| 3) DreamWaQ-Humanoid further removes the human imitation objective Df from objective (5), effectively reducing our method to an adaptation of DreamWaQ [18] for humanoid ... | component/input/data sensitivity | p. 7 (5 Experiment) |
| Comparably, when downplaying the sensitivity to safety-critical events and removing the safety-recovery policy, the success data drops significantly from nearly 85% to around 60% ... | component/input/data sensitivity | p. 8 (5 Experiment) |
| The projected gravity refers to the component of gravity expressed in the robot's local coordinate system. | component/input/data sensitivity | p. 15 (A.2 Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To develop a reliable locomotion policy capable of generalizing from the training to the deployment environment, we propose formulating policy optimization as a robust ... | Figure 9: Extreme State: Policy's state distribution in the extreme cases A.8 History Length Experiments We investigate the impact of observation history length on ... | PDF body cue; verify exact table/figure and matched conditions | p. 20 (Figure/Table caption), p. 8 (5 Experiment), p. 8 (5 Experiment), p. 7 (5 Experiment), p. 7 (5 Experiment), p. 20 (Figure/Table caption) |
| Primary metric/result | HWC-Loco reaches a success rate of 81.27%, outperforming all baselines by a significant margin. | numeric claim only at cited anchor | p. 8 (5 Experiment) |

- Numeric sentences retained from the body:
- **p. 8 / 5 Experiment - extractive body cue:** Each evaluation runs for 1200 steps, which is equivalent to 12 seconds of real clock time.
- **p. 8 / 5 Experiment - extractive body cue:** Under these general locomotion settings, we design three types of disturbances as follows: 1) External force/torque disturbances, where random forces and torques (up to 200 ...
- **p. 9 / 5 Experiment - extractive body cue:** Second, the humanoid robot used in real-world deployment has only 19 degrees of freedom, which limits whole-body coordination and constrains the expression of complex recovery ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | To evaluate the effectiveness of different components in HWC-Loco, we design a comparison method using an ablation approach as follows: 1) HWC-Loco-l sets α ... | p. 7 (5 Experiment) |
| body limitation/failure cue | Figure 10: Climb Stairs Test. The blue segments indicate the activation of the goal-tracking policy, while the orange segments correspond to the safety recovery ... | p. 21 (Figure/Table caption) |
| body limitation/failure cue | Figure 13: Robustness in Outdoor Settings: The robot responds to external disturbances in an outdoor environment by waving its arms and adjusting its gaits ... | p. 23 (Figure/Table caption) |
| body limitation/failure cue | 6 Limitation Our approach has three main limitations. | p. 9 (5 Experiment) |
| body limitation/failure cue | Importantly, the controller does not rely solely on recovery mode but dynamically switches between goal-tracking and recovery policies, thereby adapting the action distribution to ... | p. 9 (5 Experiment) |
| body limitation/failure cue | 2) Robustness: How well can HWC-Loco stabilize the humanoid robot under varying levels of disturbance? | p. 7 (5 Experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All policies are trained using three random seeds and evaluated in 1000 distinct environments. | p. 7 (5 Experiment) |
| Each evaluation runs for 1200 steps, which is equivalent to 12 seconds of real clock time. | p. 8 (5 Experiment) |
| The training terrain consists of various types, including flat planes, rough surfaces, steps, and slopes. | p. 15 (A.2 Implementation Details) |
| Action Space: The policy outputs continuous actions at ∈Rn, which are utilized as target positions for a PD controller to compute joint torques. | p. 15 (A.2 Implementation Details) |
| 3) α1 and α2 indicate the hyperparameters that are utilized to adjust the importance of the different velocity terms. | p. 17 (A.2 Implementation Details) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5 Experiment - extractive body cue:** To evaluate the effectiveness of different components in HWC-Loco, we design a comparison method using an ablation approach as follows: 1) HWC-Loco-l sets α to ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 10: Climb Stairs Test. The blue segments indicate the activation of the goal-tracking policy, while the orange segments correspond to the safety recovery policy. ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 13: Robustness in Outdoor Settings: The robot responds to external disturbances in an outdoor environment by waving its arms and adjusting its gaits to ...
- **p. 9 / 5 Experiment - extractive body cue:** 6 Limitation Our approach has three main limitations.
- **p. 9 / 5 Experiment - extractive body cue:** Importantly, the controller does not rely solely on recovery mode but dynamically switches between goal-tracking and recovery policies, thereby adapting the action distribution to environmental ...
- **p. 7 / 5 Experiment - extractive body cue:** 2) Robustness: How well can HWC-Loco stabilize the humanoid robot under varying levels of disturbance?

- **Evidence anchors reviewed:** datasets p. 9 (5 Experiment), p. 7 (5 Experiment), p. 7 (5 Experiment), p. 8 (5 Experiment), p. 8 (5 Experiment), p. 9 (5 Experiment), metrics p. 20 (Figure/Table caption), p. 8 (5 Experiment), p. 8 (5 Experiment), p. 7 (5 Experiment), p. 7 (5 Experiment), p. 9 (5 Experiment), baselines p. 8 (5 Experiment), p. 9 (5 Experiment), p. 9 (5 Experiment), p. 7 (5 Experiment), p. 7 (5 Experiment), p. 20 (Figure/Table caption), results p. 20 (Figure/Table caption), p. 8 (5 Experiment), p. 8 (5 Experiment), p. 7 (5 Experiment), p. 7 (5 Experiment), p. 20 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 9: Extreme State: Policy's state distribution in the extreme cases A.8 History Length Experiments We investigate the impact of observation history length on HWC-Loco's performance. Setting H = 10 ... (p. 20, Figure/Table caption).
- **Metric evidence:** [64] b) Goal Tracking performance: The ability to accurately follow velocity commands by maximizing task rewards rT detailed in Appendix A.2 [43]. c) Human-Like behavior: Measured as the Wasserstein-1 distance ... (p. 7, 5 Experiment).
- **Baseline/ablation evidence:** To evaluate the effectiveness of different components in HWC-Loco, we design a comparison method using an ablation approach as follows: 1) HWC-Loco-l sets α to a lower value, thereby reducing ... (p. 7, 5 Experiment).
- **Failure/negative evidence:** To evaluate the effectiveness of different components in HWC-Loco, we design a comparison method using an ablation approach as follows: 1) HWC-Loco-l sets α to a lower value, thereby reducing ... (p. 7, 5 Experiment).
