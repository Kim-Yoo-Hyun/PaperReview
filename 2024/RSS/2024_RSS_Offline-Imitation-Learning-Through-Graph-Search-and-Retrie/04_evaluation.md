# Evaluation - Offline Imitation Learning Through Graph Search and Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p054.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p054.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS)): We find that our method can achieve a success rate greater than 80% in the considered task and outperform all baselines in execution time.

## Evaluation Body Digest

- **p. 6 / V. EXPERIMENTS - extractive body cue:** Bottom: Our real-world tasks. and Worse-Better20 (the whole worse-human dataset with 20% data of the better-human dataset). • Nut Assembly In this task, the robot ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Experiment Setup 1) Simulation Experiments: We use the image-based Robomimic benchmark [30] as our testbed in simulation, which provides several robotic manipulation tasks with FrankaPanda ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Specifically, we use three tasks that contain human demonstrations of diverse qualities (Worse, Okay, Better): • Can Pick-and-Place In this task, the robot is required ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The robot is required to push a blue cylinder toward a green cube on the table. • Spoon Scooping In this task, the robot is ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Real-world Results As shown in Table II, our results in simulation also transferred to the real-world experiments well.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We conjecture that this is because all the used demonstrations eventually lead to successes and the suboptimal behaviors in those datasets are mainly caused by ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** We would like to understand how they affect weight distribution over the dataset and the resulting learning performance.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** In contrast, our method can identify the good behavior in the dataset, and avoid learning these failure behavior patterns (see next sections).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** offline robot transition/trajectory dataset과 deployment MDP.
- **Input boundary:** dataset state/observation, action, reward와 return-to-go.
- **Output/decision under evaluation:** dataset-supported action sequence.
- **Primary target:** offline policy value, OOD safety와 closed-loop success.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find that our method can achieve a success rate greater than 80% in the considered task and outperform all baselines in execution time. | p. 7 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | A good method is expected to achieve a high success rate with low execution time. • Normalized Proficiency (NP) is a metric we use ... | p. 6 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The second finding is that our algorithm can also improve the success rate of state-of-the-art algorithms. | p. 7 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 9: Relative Success rate and Normalized Proficiency improvement compared to baseline BC (DP) under different α. | p. 8 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3) Evaluation Metric: To evaluate the performance of a trained policy, we use the following metrics. • Success rate (SR) is defined as the ... | p. 6 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / V. EXPERIMENTS - extractive body cue:** Bottom: Our real-world tasks. and Worse-Better20 (the whole worse-human dataset with 20% data of the better-human dataset). • Nut Assembly In this task, the robot ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Experiment Setup 1) Simulation Experiments: We use the image-based Robomimic benchmark [30] as our testbed in simulation, which provides several robotic manipulation tasks with FrankaPanda ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Specifically, we use three tasks that contain human demonstrations of diverse qualities (Worse, Okay, Better): • Can Pick-and-Place In this task, the robot is required ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The robot is required to push a blue cylinder toward a green cube on the table. • Spoon Scooping In this task, the robot is ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Real-world Results As shown in Table II, our results in simulation also transferred to the real-world experiments well.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We conjecture that this is because all the used demonstrations eventually lead to successes and the suboptimal behaviors in those datasets are mainly caused by ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** We would like to understand how they affect weight distribution over the dataset and the resulting learning performance.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** In contrast, our method can identify the good behavior in the dataset, and avoid learning these failure behavior patterns (see next sections).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Collecting high-quality human demonstrations for imitation learning can be very difficult. Consider the problem of using a spoon, tying a rubber band, and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of our algorithm. We first build a graph to represent the demonstration dataset and run a graph search to evaluate the goodness ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Identifying connectivity. Augmented edge: We add a bidirectional edge between two nodes u and v if they both lie in the tolerance range ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: The real world robot manipulation setup. We conduct experiments on a UR5 robot arm with Robotiq gripper. We use 3 workspace cameras with ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Illustration of the used tasks. Above: Tasks from the robomimic benchmark. Bottom: Our real-world tasks. and Worse-Better20 (the whole worse-human dataset with 20% ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Dataset weight distribution plot (cumulative distribution function using sample statistics) v.s. different temperatures. As β1 decreases or β2 increases, we can see a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Success rate and Normalized Proficiency metric under different β1 and β2. The results are computed on the Can WB20. In general, we observe ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Visualization of calculated weight w for transitions on a demonstration trajectory. We select 4 trajectories (part) from 4 different tasks. We use red ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Bottom: Our real-world tasks. and Worse-Better20 (the whole worse-human dataset with 20% data of the better-human dataset). • Nut Assembly In this task, the ... | embodiment, simulator version and control stack | p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Task/environment | Experiment Setup 1) Simulation Experiments: We use the image-based Robomimic benchmark [30] as our testbed in simulation, which provides several robotic manipulation tasks with ... | reset, timeout, object/scene variation | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Observation/sensor | dataset state/observation, action, reward와 return-to-go | calibration, preprocessing, privileged input | p. 3 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES) |
| Output/decision | dataset-supported action sequence | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 4 (IV. POLICY LEARNING) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 3) Evaluation Metric: To evaluate the performance of a trained policy, we use the following metrics. • Success rate (SR) is defined as the ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| A good method is expected to achieve a high success rate with low execution time. • Normalized Proficiency (NP) is a metric we use ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| 7: Success rate and Normalized Proficiency metric under different β1 and β2. | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| In this case, following the suboptimal trajectories will not harm the success rate much. | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| We find that both low and high α will affect the success rate and proficiency. | definition/direction/unit from same section | p. 8 (V. EXPERIMENTS) |
| Then we plot the change in success rate and normalized proficiency in Figure 7. | definition/direction/unit from same section | p. 8 (V. EXPERIMENTS) |
| Fig. 2: Overview of our algorithm. We first build a graph to represent the demonstration dataset and run a graph search to evaluate the ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| We first study how much performance gain our method can achieve compared to the state-of-the-art imitation learning baseline. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We first study how much performance gain our method can achieve compared to the state-of-the-art imitation learning baseline. | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| DP [8] is a state-of-the-art behavior cloning baseline based on the diffusion model [21]. | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| Our proposed method can outperform the baselines in both success rate (SR) and normalized proficiency (NP) across different tasks. | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| We observe that the baselines appear to repeat the failed human attempts during demo collection more frequently compared to our method. | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| 9: Relative Success rate and Normalized Proficiency improvement compared to baseline BC (DP) under different α. | comparison identity and matched condition | p. 8 (V. EXPERIMENTS) |
| IQL [24] is a strong offline RL baseline. | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Hyperparameter Analysis Having known that our method indeed strengthened desired behavior, in this section, we further study the effect of the main hyperparameters in ... | component/input/data sensitivity | p. 8 (V. EXPERIMENTS) |
| Specifically, in the simulation experiment, the last average pooling layer of ResNet-18 is replaced by a spatial softmax [15] as in previous works [30, ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| Fig. 3: Identifying connectivity. Augmented edge: We add a bidirectional edge between two nodes u and v if they both lie in the tolerance ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| As a direct approach that uses graph search rather than deep RL, our method enjoys high time efficiency. | We find that our method can achieve a success rate greater than 80% in the considered task and outperform all baselines in execution time. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Primary metric/result | A good method is expected to achieve a high success rate with low execution time. • Normalized Proficiency (NP) is a metric we use ... | numeric claim only at cited anchor | p. 6 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Task Can (WO) Can (WB) NutAssembly (WO) NutAssembly (WB) Transport SR(↑) NP(↑) SR(↑) NP(↑) SR(↑) NP(↑) SR(↑) NP(↑) SR(↑) NP(↑) DP 0.77±0.02 0.46±0.06 0.80±0.02 0.47±0.06 ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The results are averaged on the last checkpoint of 3 seeds.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Each checkpoint evaluation takes 30 trials.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Task Pushing Spoon Scooping Band Tying Tweezer SR(↑) TTS(↓) SR(↑) TTS(↓) SR(↑) TTS(↓) SR(↑) TTS(↓) DP 0.58±0.14 12.0±1.6 0.63±0.08 30.2±1.8 0.57±0.14 34.8±2.6 0.48±0.04 41.2±2.8 IQL-DP ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** We select 4 trajectories (part) from 4 different tasks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, in many cases, they will get stuck or go out of distribution, leading to a complete failure. | p. 8 (V. EXPERIMENTS) |
| body limitation/failure cue | Interestingly, we have the following findings: (1) All the temporal segments that lead to the failures are weakened and have low weights. | p. 8 (V. EXPERIMENTS) |
| body limitation/failure cue | The robot is required to push a blue cylinder toward a green cube on the table. • Spoon Scooping In this task, the robot ... | p. 6 (V. EXPERIMENTS) |
| body limitation/failure cue | This task highlights the challenge of robust perception against partial occlusion and fine-grained manipulation. • Tweezer Manipulation In this task, the robot needs to ... | p. 6 (V. EXPERIMENTS) |
| body limitation/failure cue | Then, through both quantitative and qualitative analysis, we show that our method identify and chain useful behaviors in the dataset to learn a robust ... | p. 5 (V. EXPERIMENTS) |
| body limitation/failure cue | We observe that the baselines appear to repeat the failed human attempts during demo collection more frequently compared to our method. | p. 7 (V. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 3) Evaluation Metric: To evaluate the performance of a trained policy, we use the following metrics. • Success rate (SR) is defined as the ... | p. 6 (V. EXPERIMENTS) |
| Each checkpoint evaluation takes 30 trials. | p. 7 (V. EXPERIMENTS) |
| The results are averaged on the last checkpoint of 3 seeds. | p. 7 (V. EXPERIMENTS) |
| Finally, we present hyperparameter analysis to study design choices of our method. | p. 5 (V. EXPERIMENTS) |
| Hyperparameter Analysis Having known that our method indeed strengthened desired behavior, in this section, we further study the effect of the main hyperparameters in ... | p. 8 (V. EXPERIMENTS) |
| Defining the first similarity term using an exponential form, we design the weight reallocation criterion at the vertex v as walloc(u)/v = exp [β1S(u, ... | p. 5 (IV. POLICY LEARNING) |
| Here, the cost function is the number of steps taken to reach og. | p. 3 (IV. POLICY LEARNING) |
| We introduce the implementation details in the remaining sections. | p. 3 (IV. POLICY LEARNING) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / V. EXPERIMENTS - extractive body cue:** However, in many cases, they will get stuck or go out of distribution, leading to a complete failure.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Interestingly, we have the following findings: (1) All the temporal segments that lead to the failures are weakened and have low weights.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The robot is required to push a blue cylinder toward a green cube on the table. • Spoon Scooping In this task, the robot is ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** This task highlights the challenge of robust perception against partial occlusion and fine-grained manipulation. • Tweezer Manipulation In this task, the robot needs to first ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Then, through both quantitative and qualitative analysis, we show that our method identify and chain useful behaviors in the dataset to learn a robust policy.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We observe that the baselines appear to repeat the failed human attempts during demo collection more frequently compared to our method.

- **Evidence anchors reviewed:** datasets p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), metrics p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), baselines p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), results p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
