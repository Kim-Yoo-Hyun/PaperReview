# Evaluation - Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v164/rudin22a.html; PDF retrieval source: https://proceedings.mlr.press/v164/rudin22a/rudin22a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 Results), p. 7 (4 Results), p. 8 (4 Results), p. 6 (4 Results), p. 6 (4 Results), p. 8 (4 Results)): (b) Success rate for climbing and descending sloped terrains.

## Evaluation Body Digest

- **p. 6 / 4 Results - extractive body cue:** As such, we simplify the task by reducing the maximum step size of stairs and obstacles and directly train robots on the full range of ...
- **p. 6 / 4 Results - extractive body cue:** On the other hand, below a certain threshold, we see a slow decrease in (a) (b) (c) Figure 4: (a) Average and standard deviation (over ...
- **p. 7 / 4 Results - extractive body cue:** In terms of training time, we see a nearly linear scaling up to 4000 robots, after which simulation throughput gains slow down.
- **p. 7 / 4 Results - extractive body cue:** From the third plot we can conclude that using 2048 to 4096 robots with a batch size of ≈100k or ≈200k provides the best trade-off ...
- **p. 8 / 4 Results - extractive body cue:** 4.3 Sim-to-real Transfer On the physical robot, our policy is fixed.
- **p. 8 / 4 Results - extractive body cue:** Finally, we apply our approach to Agility Robotics' bipedal robot Cassie.
- **p. 7 / 4 Results - extractive body cue:** (b) Success rate for climbing and descending sloped terrains.
- **p. 7 / 4 Results - extractive body cue:** (a) (b) Figure 5: Success rate of the tested policy on increasing terrain complexities.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** 4 Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | (b) Success rate for climbing and descending sloped terrains. | p. 7 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | (a) (b) Figure 5: Success rate of the tested policy on increasing terrain complexities. | p. 7 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find that an additional reward encouraging standing on a single foot is necessary to achieve a walking gait. | p. 8 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4, we compare these results with the baseline, which allows us to select the most favorable trade-off between policy performance and training time. | p. 6 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Using this very large batch size results in the best policy but at the cost of a relatively long training time. | p. 6 (4 Results) |

## Dataset / Benchmark Role

- **p. 6 / 4 Results - extractive body cue:** As such, we simplify the task by reducing the maximum step size of stairs and obstacles and directly train robots on the full range of ...
- **p. 6 / 4 Results - extractive body cue:** On the other hand, below a certain threshold, we see a slow decrease in (a) (b) (c) Figure 4: (a) Average and standard deviation (over ...
- **p. 7 / 4 Results - extractive body cue:** In terms of training time, we see a nearly linear scaling up to 4000 robots, after which simulation throughput gains slow down.
- **p. 7 / 4 Results - extractive body cue:** From the third plot we can conclude that using 2048 to 4096 robots with a batch size of ≈100k or ≈200k provides the best trade-off ...
- **p. 8 / 4 Results - extractive body cue:** 4.3 Sim-to-real Transfer On the physical robot, our policy is fixed.
- **p. 8 / 4 Results - extractive body cue:** Finally, we apply our approach to Agility Robotics' bipedal robot Cassie.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Thousands of robots learning to walk in simulation. 1
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Terrain types used for training and testing in simulation. (a) Randomly rough terrain with variations of 0.1 m. (b) Sloped terrain with an ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: 4000 robots progressing through the terrains with automatic curriculum, after 500 (top) and 1000 (bottom) policy updates. The robots start the training session ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (a) Average and standard deviation (over 5 runs) of the total reward of an episode after 1500 policy updates for different number of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Success rate of the tested policy on increasing terrain complexities. Robots start in the center of the terrain and are given a forward ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: ANYmal C with a fixed arm, ANYmal B, A1 and Cassie in simulation. performance with fewer robots. We believe this is explained by ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Locomotion policy, trained in under 20min, deployed on the physical robot. weight, and the ANYmal B robot, which has comparable dimensions but modified ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | As such, we simplify the task by reducing the maximum step size of stairs and obstacles and directly train robots on the full range ... | embodiment, simulator version and control stack | p. 6 (4 Results), p. 6 (4 Results) |
| Task/environment | On the other hand, below a certain threshold, we see a slow decrease in (a) (b) (c) Figure 4: (a) Average and standard deviation ... | reset, timeout, object/scene variation | p. 6 (4 Results), p. 7 (4 Results) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 5 (1 Introduction), p. 5 (1 Introduction) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| (b) Success rate for climbing and descending sloped terrains. | definition/direction/unit from same section | p. 7 (4 Results) |
| (a) (b) Figure 5: Success rate of the tested policy on increasing terrain complexities. | definition/direction/unit from same section | p. 7 (4 Results) |
| On the other hand, below a certain threshold, we see a slow decrease in (a) (b) (c) Figure 4: (a) Average and standard deviation ... | definition/direction/unit from same section | p. 6 (4 Results) |
| In these two cases, we can retrain a policy without any modifications to the rewards or algorithm hyper-parameters and obtain a very similar performance. | definition/direction/unit from same section | p. 8 (4 Results) |
| Figure 4: (a) Average and standard deviation (over 5 runs) of the total reward of an episode after 1500 policy updates for different number ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| We find that an additional reward encouraging standing on a single foot is necessary to achieve a walking gait. | definition/direction/unit from same section | p. 8 (4 Results) |
| Figure 2: Terrain types used for training and testing in simulation. (a) Randomly rough terrain with variations of 0.1 m. (b) Sloped terrain with ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 3: 4000 robots progressing through the terrains with automatic curriculum, after 500 (top) and 1000 (bottom) policy updates. The robots start the training ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We begin by setting a baseline with nrobots = 20000 and nsteps = 50, resulting in a batch size of 1M samples. | comparison identity and matched condition | p. 6 (4 Results) |
| 4, we compare these results with the baseline, which allows us to select the most favorable trade-off between policy performance and training time. | comparison identity and matched condition | p. 6 (4 Results) |
| Figure 2: Terrain types used for training and testing in simulation. (a) Randomly rough terrain with variations of 0.1 m. (b) Sloped terrain with ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| In these two cases, we can retrain a policy without any modifications to the rewards or algorithm hyper-parameters and obtain a very similar performance. | comparison identity and matched condition | p. 8 (4 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 7: Locomotion policy, trained in under 20min, deployed on the physical robot. weight, and the ANYmal B robot, which has comparable dimensions but ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 3: 4000 robots progressing through the terrains with automatic curriculum, after 500 (top) and 1000 (bottom) policy updates. The robots start the training ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| In order to use the total reward as a single representative metric, we have to remove the curriculum, otherwise a more performant policy sees ... | component/input/data sensitivity | p. 6 (4 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Additionally, we present a novel game-inspired curriculum which automatically adapts the task difficulty to the performance of the policy. | (b) Success rate for climbing and descending sloped terrains. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 Results), p. 7 (4 Results), p. 8 (4 Results), p. 6 (4 Results), p. 6 (4 Results), p. 8 (4 Results) |
| Primary metric/result | (a) (b) Figure 5: Success rate of the tested policy on increasing terrain complexities. | numeric claim only at cited anchor | p. 7 (4 Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Results - extractive body cue:** We start from 128 robots corresponding to the level of parallelization of previous CPU implementations and increase that number up to 16384, which is close ...
- **p. 6 / 4 Results - extractive body cue:** The ideal case of a batch size of 1M samples with 20000 robots is shown in red.
- **p. 7 / 4 Results - extractive body cue:** In terms of training time, we see a nearly linear scaling up to 4000 robots, after which simulation throughput gains slow down.
- **p. 7 / 4 Results - extractive body cue:** From the third plot we can conclude that using 2048 to 4096 robots with a batch size of ≈100k or ≈200k provides the best trade-off ...
- **p. 7 / 4 Results - extractive body cue:** 4.2 Simulation For our simulation and deployment experiments, we use a policy trained with 4096 robots and a batch size of 98304, which we train ...
- **p. 2 / 1 Introduction - extractive body cue:** For quadrupeds, DRL has been used to train blind policies robust to highly uneven ground [16] (12 hours of training).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | As such, we can conclude that increasing the number of robots is beneficial for both final performance and training time, but there is an ... | p. 7 (4 Results) |
| body limitation/failure cue | The purpose of this work is not to obtain the absolute best-performing policy with the highest robustness. | p. 8 (5 Conclusion) |
| body limitation/failure cue | As part of future work, we plan to merge the two approaches. | p. 8 (4 Results) |
| body limitation/failure cue | To that end, we perform robustness and traversability tests. | p. 7 (4 Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Current popular pipelines have the simulation and reward/observation calculation computed on the CPU, making the GPU unsuitable for policy inference because of communication bottle-necks. | p. 2 (1 Introduction) |
| We start from 128 robots corresponding to the level of parallelization of previous CPU implementations and increase that number up to 16384, which is ... | p. 6 (4 Results) |
| This results in large batch sizes of millions of samples for each policy update which improves the learning dynamics, but does not optimize the ... | p. 2 (1 Introduction) |
| Using this very large batch size results in the best policy but at the cost of a relatively long training time. | p. 6 (4 Results) |
| Since we increase nrobots by a few orders of magnitude, we must choose a small nsteps to keep B reasonable and hence optimize training ... | p. 3 (1 Introduction) |
| In terms of training time, we see a nearly linear scaling up to 4000 robots, after which simulation throughput gains slow down. | p. 7 (4 Results) |
| Our implementation is designed to perform every operation and store all the data on the GPU. | p. 3 (1 Introduction) |
| We use the ANYmal C robot with a fixed robotic arm, which adds about 20 % of additional 2Trained on: i9-11900k CPU, NVIDIA RTX ... | p. 7 (4 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4 Results - extractive body cue:** As such, we can conclude that increasing the number of robots is beneficial for both final performance and training time, but there is an upper ...
- **p. 8 / 5 Conclusion - extractive body cue:** The purpose of this work is not to obtain the absolute best-performing policy with the highest robustness.
- **p. 8 / 4 Results - extractive body cue:** As part of future work, we plan to merge the two approaches.
- **p. 7 / 4 Results - extractive body cue:** To that end, we perform robustness and traversability tests.

- **Evidence anchors reviewed:** datasets p. 6 (4 Results), p. 6 (4 Results), p. 7 (4 Results), p. 7 (4 Results), p. 8 (4 Results), p. 8 (4 Results), metrics p. 7 (4 Results), p. 7 (4 Results), p. 6 (4 Results), p. 8 (4 Results), p. 6 (Figure/Table caption), p. 8 (4 Results), baselines p. 6 (4 Results), p. 6 (4 Results), p. 4 (Figure/Table caption), p. 8 (4 Results), results p. 7 (4 Results), p. 7 (4 Results), p. 8 (4 Results), p. 6 (4 Results), p. 6 (4 Results), p. 8 (4 Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
