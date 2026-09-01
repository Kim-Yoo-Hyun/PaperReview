# Evaluation - Learning to Walk from Three Minutes of Real-World Data with Semi-structured Dynamics Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=evCXwlCMIi; PDF retrieval source: https://arxiv.org/pdf/2410.09163. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 16 (Figure/Table caption), p. 17 (Figure/Table caption)): Figure 12: Simulated benchmark results. Better performance is achieved when using our semi- structured dynamics models and a multi-step loss. Plots show the mean and standard deviation for episodic rewards. ...

## Evaluation Body Digest

- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- or ...
- **p. 18 / Figure/Table caption - extractive PDF cue:** Figure 12: Simulated benchmark results. Better performance is achieved when using our semi- structured dynamics models and a multi-step loss. Plots show the mean and ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an unseen environment showcases ...
- **p. 14 / A.2 Reward Function and Termination Condition - extractive PDF cue:** Reward Term Expression Weight Maximize forward velocity vx t+1 0.42 Limit base yaw rate exp  -(ωz t+1)2/0.2  0.11 Limit base roll exp  ...
- **p. 15 / Figure/Table caption - extractive PDF cue:** Figure 6: Predicted external forces and actual external force estimates over one second of real-world data for the floating base and the joints of the ...
- **p. 13 / A.2 Reward Function and Termination Condition - extractive PDF cue:** The reward function is a weighted sum of the terms in Table 3.
- **p. 13 / A Implementation Details - extractive PDF cue:** In this appendix, we provide details of our implementation for the Unitree Go1 Quadruped, including the observation and action spaces, the reward function, the termination ...
- **p. 14 / A.2 Reward Function and Termination Condition - extractive PDF cue:** The reward at each time step is a weighted sum of these terms.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** A Implementation Details (p. 13); B Additional Experiments (p. 15); B.5 Additional Simulated Terrain Experiments (p. 17); C Simulated Benchmark Experiments (p. 18).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 12: Simulated benchmark results. Better performance is achieved when using our semi- structured dynamics models and a multi-step loss. Plots show the mean ... | p. 18 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an unseen environment ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2: The SSRL framework. A deterministic policy is used to collect data from the real world while a stochastic policy is utilized in ... | p. 2 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Real-world results. Left-SSRL efficiently performs policy optimization, even when data is scarce. Center-With our approach, the quadruped steadily learns to walk faster. ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- ... | p. 16 (Figure/Table caption) |

## Dataset / Benchmark Role

- dataset/benchmark/environment role cue 없음

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Unitree Go1 quadruped learning to walk from scratch using SSRL on hard ground (left) and memory foam (right). 1
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: The SSRL framework. A deterministic policy is used to collect data from the real world while a stochastic policy is utilized in conjunction ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3: Control architecture. The policy takes in a history of observations and outputs parameters to a gait generator and offsets to the gait. The ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Real-world results. Left-SSRL efficiently performs policy optimization, even when data is scarce. Center-With our approach, the quadruped steadily learns to walk faster. Right-Predicted ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an unseen environment showcases ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Table 1: Observation space. The action space A ⊂R9 outputs the change in nominal height for the gait generator and offsets to nominal foot positions ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Table 2: Action space. A.2 Reward Function and Termination Condition Reward Function. The reward function is a weighted sum of the terms in Table 3. ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 3: Reward function terms. The reward at each time step is a weighted sum of these terms. Termination Condition. The termination flag dt stops ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | not recovered | embodiment, simulator version and control stack | 본문 anchor 없음 |
| Task/environment | not recovered | reset, timeout, object/scene variation | 본문 anchor 없음 |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 5 (1 Introduction), p. 14 (A.3 Control Architecture) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 3 (1 Introduction), p. 4 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Figure 12: Simulated benchmark results. Better performance is achieved when using our semi- structured dynamics models and a multi-step loss. Plots show the mean ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an unseen environment ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Reward Term Expression Weight Maximize forward velocity vx t+1 0.42 Limit base yaw rate exp  -(ωz t+1)2/0.2  0.11 Limit base roll exp ... | definition/direction/unit from same section | p. 14 (A.2 Reward Function and Termination Condition) |
| Figure 6: Predicted external forces and actual external force estimates over one second of real-world data for the floating base and the joints of ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| The reward function is a weighted sum of the terms in Table 3. | definition/direction/unit from same section | p. 13 (A.2 Reward Function and Termination Condition) |
| In this appendix, we provide details of our implementation for the Unitree Go1 Quadruped, including the observation and action spaces, the reward function, the ... | definition/direction/unit from same section | p. 13 (A Implementation Details) |
| The reward at each time step is a weighted sum of these terms. | definition/direction/unit from same section | p. 14 (A.2 Reward Function and Termination Condition) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an unseen environment ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 2: The SSRL framework. A deterministic policy is used to collect data from the real world while a stochastic policy is utilized in ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Figure 4: Real-world results. Left-SSRL efficiently performs policy optimization, even when data is scarce. Center-With our approach, the quadruped steadily learns to walk faster. ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 10: Training performance of our method with varying simulated contact conditions. B.6 SAC Performance State-of-the-art real-world quadrupedal locomotion results where policies are trained ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |
| Table 4: Hyperparameters for our approach and the baseline approach with black-box models. x → y over epochs a →b denotes a clipped linear ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 9: Training performance when removing the noise estimators and removing both the noise estimators and ensemble. B.5 Additional Simulated Terrain Experiments To further ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This, when combined with the accuracy of our predictions over long-horizons (Section 4.2) provides insight into why our approach enables such effective policy optimization ... | Figure 12: Simulated benchmark results. Better performance is achieved when using our semi- structured dynamics models and a multi-step loss. Plots show the mean ... | PDF body cue; verify exact table/figure and matched conditions | p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 16 (Figure/Table caption), p. 17 (Figure/Table caption) |
| Primary metric/result | Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an unseen environment ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However there are several key limitations. | p. 8 (5 Related Work) |
| body limitation/failure cue | 6 Limitations This paper presents a novel framework for model-based reinforcement learning, which leverages physics-informed, semi-structured dynamics models to enable highly sample-efficient policy learning ... | p. 8 (5 Related Work) |
| body limitation/failure cue | The termination flag dt stops the accumulation of reward after the quadruped falls and is defined by: dt = 1 if /φx t / ... | p. 14 (A.2 Reward Function and Termination Condition) |
| body limitation/failure cue | Figure 8: Our approach is robust to errors in a priori knowledge of the robot's inertial properties. B.4 Modeling Uncertainty Here, we examine the ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: The SSRL framework. A deterministic policy is used to collect data from the real world while a stochastic policy is utilized in ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- ... | p. 16 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In this appendix, we provide details of our implementation for the Unitree Go1 Quadruped, including the observation and action spaces, the reward function, the ... | p. 13 (A Implementation Details) |
| For each foot, the desired foot positions (10) are computed and sent to an inverse kinematics solver to produce desired joint angles qdes ∈R12. | p. 14 (A.3 Control Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5 Related Work - extractive PDF cue:** However there are several key limitations.
- **p. 8 / 5 Related Work - extractive PDF cue:** 6 Limitations This paper presents a novel framework for model-based reinforcement learning, which leverages physics-informed, semi-structured dynamics models to enable highly sample-efficient policy learning in ...
- **p. 14 / A.2 Reward Function and Termination Condition - extractive PDF cue:** The termination flag dt stops the accumulation of reward after the quadruped falls and is defined by: dt = 1 if /φx t / > ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 8: Our approach is robust to errors in a priori knowledge of the robot's inertial properties. B.4 Modeling Uncertainty Here, we examine the benefit ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: The SSRL framework. A deterministic policy is used to collect data from the real world while a stochastic policy is utilized in conjunction ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- or ...

- **PDF anchors reviewed:** datasets 본문 anchor 없음, metrics p. 16 (Figure/Table caption), p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (A.2 Reward Function and Termination Condition), p. 15 (Figure/Table caption), p. 13 (A.2 Reward Function and Termination Condition), baselines p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 17 (Figure/Table caption), p. 19 (Figure/Table caption), results p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 16 (Figure/Table caption), p. 17 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
