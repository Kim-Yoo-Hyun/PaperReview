# Evaluation - Hindsight Experience Replay

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1707.01495; PDF retrieval source: https://arxiv.org/pdf/1707.01495. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments)): 4.3 we check if HER improves performance in the single-goal setup.

## Evaluation Body Digest

- **p. 5 / 4 Experiments - extractive body cue:** We decided to use manipulation environments based on an existing hardware robot to ensure that the challenges we face correspond as closely as possible to ...
- **p. 10 / 4 Experiments - extractive body cue:** 4.6 Deployment on a physical robot We took a policy for the pick-and-place task trained in the simulator (version with the future strategy and k ...
- **p. 6 / 4 Experiments - extractive body cue:** In this task a box is placed on a table in front of the robot and the task is to move it to the target ...
- **p. 6 / 4 Experiments - extractive body cue:** To make exploration in this task easier we recorded a single state in which the box is grasped and start half of the training episodes ...
- **p. 9 / 4 Experiments - extractive body cue:** 0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+HER 0 50 100 150 200 epoch number (every epoch ...
- **p. 9 / 4 Experiments - extractive body cue:** On the right top plot the curves for final, episode and future coincide as all these strategies achieve perfect performance on this task. the final ...
- **p. 5 / 4 Experiments - extractive body cue:** 4.6 we show the results of the experiments on the physical robot.
- **p. 7 / 4 Experiments - extractive body cue:** 5The successful deployment on a physical robot (Sec.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** 4 Experiments (p. 5); A Experiment details (p. 14).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4.3 we check if HER improves performance in the single-goal setup. | p. 5 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In order to verify if HER improves performance we evaluate DDPG with and without HER on all 3 tasks. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4.3 Does HER improve performance even if there is only one goal we care about? | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In this section we evaluate whether HER improves performance in the case where there is only one goal we care about. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | On the right top plot the curves for final, episode and future coincide as all these strategies achieve perfect performance on this task. the ... | p. 9 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 4 Experiments - extractive body cue:** We decided to use manipulation environments based on an existing hardware robot to ensure that the challenges we face correspond as closely as possible to ...
- **p. 10 / 4 Experiments - extractive body cue:** 4.6 Deployment on a physical robot We took a policy for the pick-and-place task trained in the simulator (version with the future strategy and k ...
- **p. 6 / 4 Experiments - extractive body cue:** In this task a box is placed on a table in front of the robot and the task is to move it to the target ...
- **p. 6 / 4 Experiments - extractive body cue:** To make exploration in this task easier we recorded a single state in which the box is grasped and start half of the training episodes ...
- **p. 9 / 4 Experiments - extractive body cue:** 0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+HER 0 50 100 150 200 epoch number (every epoch ...
- **p. 9 / 4 Experiments - extractive body cue:** On the right top plot the curves for final, episode and future coincide as all these strategies achieve perfect performance on this task. the final ...
- **p. 5 / 4 Experiments - extractive body cue:** 4.6 we show the results of the experiments on the physical robot.
- **p. 7 / 4 Experiments - extractive body cue:** 5The successful deployment on a physical robot (Sec.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: Bit-flipping experi- ment. 0 10 20 30 40 50
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Different tasks: pushing (top row), sliding (middle row) and pick-and-place (bottom row). The red ball denotes the goal position. Policies are represented as ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Learning curves for multi-goal setup. An episode is considered successful if the distance between the object and the goal at the end of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Learning curves for the single-goal case. 4.3 Does HER improve performance even if there is only one goal we care about? In this ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Learning curves for the shaped reward r(s, a, g) = -/g -s′ object/2 (it performed best among the shaped rewards we have tried). ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: Ablation study of different strategies for choosing additional goals for replay. The top row shows the highest (across the training epochs) test performance ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 7: The pick-and-place policy deployed on the physical robot. future with k = 4 can be found in Fig. 3. It confirms that the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We decided to use manipulation environments based on an existing hardware robot to ensure that the challenges we face correspond as closely as possible ... | embodiment, simulator version and control stack | p. 5 (4 Experiments), p. 10 (4 Experiments) |
| Task/environment | 4.6 Deployment on a physical robot We took a policy for the pick-and-place task trained in the simulator (version with the future strategy and ... | reset, timeout, object/scene variation | p. 10 (4 Experiments), p. 6 (4 Experiments) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 2 (2 Background), p. 3 (2 Background) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 2 (1 Introduction), p. 3 (2 Background) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+HER 0 50 100 150 200 epoch number (every ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| 0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+count-based exploration DDPG+HER DDPG+HER (version from Sec. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| 1 2 4 8 16 all 0.0 0.2 0.4 0.6 0.8 1.0 highest success rate pushing no HER final random episode future 1 2 ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| After retraining the policy with gaussian noise (std=1cm) added to observations10 the success rate increased to 5/5. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| So far the only additional goals we used for replay were the ones corresponding to 8We also tried to rescale the distances, so that ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| In this section we check how the performance of DDPG with and without HER changes if we replace this reward with one which is ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Figure 3: Learning curves for multi-goal setup. An episode is considered successful if the distance between the object and the goal at the end ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| 4.4 we analyze the effects of using shaped reward functions. | definition/direction/unit from same section | p. 5 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 4.2 we compare the performance of DDPG with and without HER. | comparison identity and matched condition | p. 5 (4 Experiments) |
| 4.6 that the trained policies perform well on the physical robot without any finetuning. | comparison identity and matched condition | p. 5 (4 Experiments) |
| 3This was necessary because we could not successfully train any policies for this task without using the demonstration state. | comparison identity and matched condition | p. 6 (4 Experiments) |
| We have later discovered that training is possible without this trick if only the goal position is sometimes on the table and sometimes in ... | comparison identity and matched condition | p. 6 (4 Experiments) |
| 7We also evaluated DQN (without HER) on our tasks and it was not able to solve any of them. | comparison identity and matched condition | p. 7 (4 Experiments) |
| 4.5 we perform ablation studies of different strategies S for choosing goals for replay, here we include the best version from Sec. | comparison identity and matched condition | p. 7 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In this section we check how the performance of DDPG with and without HER changes if we replace this reward with one which is ... | component/input/data sensitivity | p. 8 (4 Experiments) |
| 4.6 that the trained policies perform well on the physical robot without any finetuning. | component/input/data sensitivity | p. 5 (4 Experiments) |
| 3This was necessary because we could not successfully train any policies for this task without using the demonstration state. | component/input/data sensitivity | p. 6 (4 Experiments) |
| We have later discovered that training is possible without this trick if only the goal position is sometimes on the table and sometimes in ... | component/input/data sensitivity | p. 6 (4 Experiments) |
| 7We also evaluated DQN (without HER) on our tasks and it was not able to solve any of them. | component/input/data sensitivity | p. 7 (4 Experiments) |
| In order to verify if HER improves performance we evaluate DDPG with and without HER on all 3 tasks. | component/input/data sensitivity | p. 7 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and ... | 4.3 we check if HER improves performance in the single-goal setup. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments) |
| Primary metric/result | In order to verify if HER improves performance we evaluate DDPG with and without HER on all 3 tasks. | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** In order to verify if HER improves performance we evaluate DDPG with and without HER on all 3 tasks.
- **p. 7 / 4 Experiments - extractive body cue:** 4.5) 0 50 100 150 200 epoch number (every epoch = 800 episodes = 800x50 timesteps) 0% 20% 40% 60% 80% 100% sliding 0 50 ...
- **p. 8 / 4 Experiments - extractive body cue:** 0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+count-based exploration DDPG+HER 0 50 100 150 200 epoch number ...
- **p. 9 / 4 Experiments - extractive body cue:** 0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+HER 0 50 100 150 200 epoch number (every epoch ...
- **p. 10 / 4 Experiments - extractive body cue:** Initially the policy succeeded in 2 out of 5 trials.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In this task a puck is placed on a long slippery table and the target position is outside of the robot's reach so that ... | p. 6 (4 Experiments) |
| body limitation/failure cue | It does not have to be robust to noisy observations because it is not used during the deployment on the physical robot. | p. 10 (5 Related work) |
| body limitation/failure cue | Our results suggest that domain-agnostic reward shaping does not work well (at least in the simple forms we have tried). | p. 8 (4 Experiments) |
| body limitation/failure cue | Surprisingly neither DDPG, nor DDPG+HER was able to successfully solve any of the tasks with any of these reward functions8.Our results are consistent with ... | p. 8 (4 Experiments) |
| body limitation/failure cue | Figure 5: Learning curves for the shaped reward r(s, a, g) = -/g -s′ object/2 (it performed best among the shaped rewards we have ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | After retraining the policy with gaussian noise (std=1cm) added to observations10 the success rate increased to 5/5. | p. 10 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We take the relative position of the box and the target and then discretize every coordinate using a grid with a stepsize β which ... | p. 7 (4 Experiments) |
| We decided to use manipulation environments based on an existing hardware robot to ensure that the challenges we face correspond as closely as possible ... | p. 5 (4 Experiments) |
| See Appendix A for more details and the values of all hyperparameters. | p. 6 (4 Experiments) |
| The results are averaged across 5 random seeds and shaded areas represent one standard deviation. | p. 7 (4 Experiments) |
| We considered reward functions of the form r(s, a, g) = λ/g -sobject/p -/g -s′ object/p, where s′ is the state of the environment ... | p. 8 (4 Experiments) |
| 0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+count-based exploration DDPG+HER 0 50 100 150 200 epoch ... | p. 8 (4 Experiments) |
| All of these strategies have a hyperparameter k which controls the ratio of HER data to data coming from normal experience replay in the ... | p. 9 (4 Experiments) |
| The top row shows the highest (across the training epochs) test performance and the bottom row shows the average test performance across all training ... | p. 9 (4 Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4 Experiments - extractive body cue:** In this task a puck is placed on a long slippery table and the target position is outside of the robot's reach so that it ...
- **p. 10 / 5 Related work - extractive body cue:** It does not have to be robust to noisy observations because it is not used during the deployment on the physical robot.
- **p. 8 / 4 Experiments - extractive body cue:** Our results suggest that domain-agnostic reward shaping does not work well (at least in the simple forms we have tried).
- **p. 8 / 4 Experiments - extractive body cue:** Surprisingly neither DDPG, nor DDPG+HER was able to successfully solve any of the tasks with any of these reward functions8.Our results are consistent with the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Learning curves for the shaped reward r(s, a, g) = -/g -s′ object/2 (it performed best among the shaped rewards we have tried). ...
- **p. 10 / 4 Experiments - extractive body cue:** After retraining the policy with gaussian noise (std=1cm) added to observations10 the success rate increased to 5/5.

- **Evidence anchors reviewed:** datasets p. 5 (4 Experiments), p. 10 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), metrics p. 9 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), baselines p. 5 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), results p. 5 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** 4.6 we show the results of the experiments on the physical robot. (p. 5, 4 Experiments).
- **Metric evidence:** 0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+HER 0 50 100 150 200 epoch number (every epoch = 800 episodes = 800x50 ... (p. 9, 4 Experiments).
- **Baseline/ablation evidence:** 4.2 we compare the performance of DDPG with and without HER. (p. 5, 4 Experiments).
- **Failure/negative evidence:** These results are indicative of the practical challenges with reward shaping, and that shaped rewards would often constitute a compromise on the metric we truly care about (such as binary ... (p. 5, 2 Background).
