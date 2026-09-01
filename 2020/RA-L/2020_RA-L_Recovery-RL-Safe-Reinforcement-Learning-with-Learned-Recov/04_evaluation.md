# Evaluation - Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.15920; PDF retrieval source: https://arxiv.org/pdf/2010.15920. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (V. EXPERIMENTS), p. 6 (Figure/Table caption), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 12 (Figure/Table caption)): Results suggest that Recovery RL with both model-free and modelbased recovery mechanisms significantly outperform prior algorithms across all 3 2D pointmass navigation environments

## Evaluation Body Digest

- **p. 5 / V. EXPERIMENTS - extractive body cue:** Domains: We evaluate Recovery RL on a set of 6 simulation domains (Figure 3) and an image-based obstacle avoidance task on a physical robot (Figure ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We do not report reward per episode, as episodes terminate on task completion or constraint violation.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** ACCEPTED FEBRUARY, 2021 Figure 3: Simulation Experiments Domains: We evaluate Recovery RL on a set of 2D navigation tasks, two contact rich manipulation environments, and ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object extraction ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** THANANJEYAN*, BALAKRISHNA* et al.: RECOVERY RL: SAFE REINFORCEMENT LEARNING WITH LEARNED RECOVERY ZONES 7 Figure 5: Sensitivity Experiments: We report the final number of task ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We then study the sensitivity of Recovery RL to the number of offline transitions used to pretrain πrec and ˆQπ φ,risk (right) and find that ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We find that Recovery RL violates constraints less often than comparisons while maintaining a similar task success rate and more efficiently optimizing the task reward.
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 9: Simulation Experiments Cumulative Violations: We plot the cumulative constraint violations for each algorithm in each simulation domain, with results averaged over 10 runs ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results suggest that Recovery RL with both model-free and modelbased recovery mechanisms significantly outperform prior algorithms across all 3 2D pointmass navigation environments | p. 6 (V. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Simulation Experiments: Left: ratio of successes to constraint violations over the course of online training. In all navigation tasks, we find that ... | p. 6 (Figure/Table caption) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find that without this relabeling, Recovery RL achieves very poor performance as it rarely achieves task successes. | p. 7 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find that the comparison algorithms are relatively sensitive to the value of the penalty parameter λ while given a fixed γrisk, Recovery RL ... | p. 7 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find that Recovery RL violates constraints less often than comparisons while maintaining a similar task success rate and more efficiently optimizing the task ... | p. 5 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / V. EXPERIMENTS - extractive body cue:** Domains: We evaluate Recovery RL on a set of 6 simulation domains (Figure 3) and an image-based obstacle avoidance task on a physical robot (Figure ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We do not report reward per episode, as episodes terminate on task completion or constraint violation.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** ACCEPTED FEBRUARY, 2021 Figure 3: Simulation Experiments Domains: We evaluate Recovery RL on a set of 2D navigation tasks, two contact rich manipulation environments, and ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object extraction ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** THANANJEYAN*, BALAKRISHNA* et al.: RECOVERY RL: SAFE REINFORCEMENT LEARNING WITH LEARNED RECOVERY ZONES 7 Figure 5: Sensitivity Experiments: We report the final number of task ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We then study the sensitivity of Recovery RL to the number of offline transitions used to pretrain πrec and ˆQπ φ,risk (right) and find that ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Recovery RL can safely learn policies for contact-rich tasks from high-dimensional image observations in simulation experiments and on a physical robotic system. We ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Recovery RL: For intuition, we illustrate Recovery RL on a 2D maze navigation task where a constraint violation corresponds to hitting a wall. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Simulation Experiments Domains: We evaluate Recovery RL on a set of 2D navigation tasks, two contact rich manipulation environments, and a visual navigation ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Simulation Experiments: Left: ratio of successes to constraint violations over the course of online training. In all navigation tasks, we find that Recovery ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Sensitivity Experiments: We report the final number of task successes and constraint violations averaged over 10 runs at the end of training for ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Physical Experiment: We evaluate Recovery RL on an image-based obstacle avoidance task (red obstacles) on the dVRK (Figure 1). We supply all algorithms ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Ablations: We first study the affect of different algorithmic components of Recovery RL (left). Results suggest that offline pretraining of πrec and ˆQπ ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7. Results suggest that Recovery RL performs much more poorly when πrec and ˆQπ φ,risk are not pretrained with data from Doffline, indicating the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Domains: We evaluate Recovery RL on a set of 6 simulation domains (Figure 3) and an image-based obstacle avoidance task on a physical robot ... | embodiment, simulator version and control stack | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Task/environment | We do not report reward per episode, as episodes terminate on task completion or constraint violation. | reset, timeout, object/scene variation | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (III. PROBLEM STATEMENT), p. 4 (IV. RECOVERY RL) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We find that Recovery RL violates constraints less often than comparisons while maintaining a similar task success rate and more efficiently optimizing the task ... | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Figure 9: Simulation Experiments Cumulative Violations: We plot the cumulative constraint violations for each algorithm in each simulation domain, with results averaged over 10 ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Figure 8: Simulation Experiments Cumulative Successes: We plot the cumulative task successes for each algorithm in each simulation domain, with results averaged over 10 ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| We do not report reward per episode, as episodes terminate on task completion or constraint violation. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Comparisons: We compare Recovery RL to the following algorithms that ignore constraints (Unconstrained) or enforce constraints via the optimization objective (LR, SQRL, RSPO) or ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| Policy parameters and λ are updated via dual gradient descent. • Safety Q-Functions for RL (SQRL) [30]: combines the LR method with a filtering ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| We hypothesize that the model-based recovery mechanism is better able to compensate for approximation errors in ˆQπ φ,risk, resulting in a more robust recovery ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| Figure 10: Simulation Experiments Reward Learning Curve: We show the total reward attained in each episode smoothed over a 100 episode length window for ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Results suggest that Recovery RL with both model-free and modelbased recovery mechanisms significantly outperform prior algorithms across all 3 2D pointmass navigation environments | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| Finally, we evaluate Recovery RL and prior algorithms on the imagebased obstacle avoidance task illustrated in Figure 1 and find that Recovery RL substantially ... | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| Figure 10: Simulation Experiments Reward Learning Curve: We show the total reward attained in each episode smoothed over a 100 episode length window for ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| Figure 6: Physical Experiment: We evaluate Recovery RL on an image-based obstacle avoidance task (red obstacles) on the dVRK (Figure 1). We supply all ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Recovery RL and all comparisons which have a safety critic are given the same offline dataset Doffline. | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablations: We ablate different components of Recovery RL and study the sensitivity of Recovery RL to the number of transitions in Doffline for the ... | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |
| Figure 7: Ablations: We first study the affect of different algorithmic components of Recovery RL (left). Results suggest that offline pretraining of πrec and ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| We then evaluate Recovery RL on an image-based obstacle avoidance task on the da Vinci Research Kit (dVRK) [20] where the robot must guide ... | component/input/data sensitivity | p. 5 (V. EXPERIMENTS) |
| In the object extraction environments, the goals is to extract the red block without toppling any blocks, and in the case of Object Extraction ... | component/input/data sensitivity | p. 5 (V. EXPERIMENTS) |
| In both object extraction environments, the objective is to grasp and lift the red block without toppling any of the blocks or colliding with ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| In Navigation 1 and 2, the goal is to navigate from the start set to the goal set without colliding into the obstacles (red) ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to ... | Results suggest that Recovery RL with both model-free and modelbased recovery mechanisms significantly outperform prior algorithms across all 3 2D pointmass navigation environments | PDF body cue; verify exact table/figure and matched conditions | p. 6 (V. EXPERIMENTS), p. 6 (Figure/Table caption), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 12 (Figure/Table caption) |
| Primary metric/result | Figure 4: Simulation Experiments: Left: ratio of successes to constraint violations over the course of online training. In all navigation tasks, we find that ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object ... | p. 6 (V. EXPERIMENTS) |
| body limitation/failure cue | We hypothesize that the model-based recovery mechanism is better able to compensate for approximation errors in ˆQπ φ,risk, resulting in a more robust recovery ... | p. 7 (V. EXPERIMENTS) |
| body limitation/failure cue | Figure 7. Results suggest that Recovery RL performs much more poorly when πrec and ˆQπ φ,risk are not pretrained with data from Doffline, indicating ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Figure 12: Physical Experiment Reward Learning Curve: We show the total reward attained in each episode smoothed over a 10 episode length window with ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | Figure 1: Recovery RL can safely learn policies for contact-rich tasks from high-dimensional image observations in simulation experiments and on a physical robotic system. ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: Recovery RL: For intuition, we illustrate Recovery RL on a 2D maze navigation task where a constraint violation corresponds to hitting a ... | p. 3 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For physical experiments we run each algorithm across 3 random seeds and visualize all 3 runs. | p. 5 (V. EXPERIMENTS) |
| Each run for simulation experiments is replicated across 10 random seeds and we report the mean and standard error. | p. 5 (V. EXPERIMENTS) |
| We tune all prior algorithms and report the best hyperparameter settings found on each task for the ratio-based evaluation metric. | p. 6 (V. EXPERIMENTS) |
| We supply all algorithms with an overhead RGB image as input and run each algorithm 3 times. | p. 7 (V. EXPERIMENTS) |
| THANANJEYAN*, BALAKRISHNA* et al.: RECOVERY RL: SAFE REINFORCEMENT LEARNING WITH LEARNED RECOVERY ZONES 7 Figure 5: Sensitivity Experiments: We report the final number of ... | p. 7 (V. EXPERIMENTS) |
| In Section IV-C we discuss how the safety critic and recovery policy are initialized from offline data and in Section IV-D we discuss implementation ... | p. 3 (IV. RECOVERY RL) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / V. EXPERIMENTS - extractive body cue:** In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object extraction ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We hypothesize that the model-based recovery mechanism is better able to compensate for approximation errors in ˆQπ φ,risk, resulting in a more robust recovery policy.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7. Results suggest that Recovery RL performs much more poorly when πrec and ˆQπ φ,risk are not pretrained with data from Doffline, indicating the ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 12: Physical Experiment Reward Learning Curve: We show the total reward attained in each episode smoothed over a 10 episode length window with results ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Recovery RL can safely learn policies for contact-rich tasks from high-dimensional image observations in simulation experiments and on a physical robotic system. We ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Recovery RL: For intuition, we illustrate Recovery RL on a 2D maze navigation task where a constraint violation corresponds to hitting a wall. ...

- **PDF anchors reviewed:** datasets p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), metrics p. 5 (V. EXPERIMENTS), p. 12 (Figure/Table caption), p. 12 (Figure/Table caption), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), baselines p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 13 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (V. EXPERIMENTS), results p. 6 (V. EXPERIMENTS), p. 6 (Figure/Table caption), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 12 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
