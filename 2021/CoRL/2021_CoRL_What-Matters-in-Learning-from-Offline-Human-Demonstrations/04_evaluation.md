# Evaluation - What Matters in Learning from Offline Human Demonstrations for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v164/mandlekar22a.html; PDF retrieval source: https://proceedings.mlr.press/v164/mandlekar22a/mandlekar22a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 3 (Dataset), p. 6 (4 Experiments), p. 3 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (4 Experiments), p. 7 (4 Experiments)): Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often suffers from the fact that the ...

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive body cue:** We collected 3 additional real-world datasets with a Franka robotic arm - Lift (Real), Can (Real), and Tool Hang (Real).
- **p. 4 / Dataset - extractive body cue:** To study the effect of observation modalities, we capture a diverse set of sensor streams when collecting the dataset, including end-effector, gripper fingers, and joints, ...
- **p. 6 / 4 Experiments - extractive body cue:** Appendix B shows the average trajectory lengths in each data subset - lower quality datasets contain demonstrations that take more time to solve the task.
- **p. 4 / Dataset - extractive body cue:** Datasets are collected by humans through RoboTurk [15, 17], a remote teleoperation platform.
- **p. 6 / 4 Experiments - extractive body cue:** BC-RNN maintains nearly the same performance as learning from ground-truth observations, providing an optimistic view for learning with real-world raw sensory observations. natural dataset distributions ...
- **p. 3 / Dataset - extractive body cue:** We further show that important design decisions made through our study in simulation directly translate to effective policy learning on real world tasks and datasets.
- **p. 5 / Dataset - extractive body cue:** Results show that less complex tasks (Lift, Can) be learned with a fraction of the data, while more complex tasks might benefit from even larger ...
- **p. 3 / Dataset - extractive body cue:** Differences in supervisor proficiency can manifest in many ways, such as large variations in trajectory length and noise in robot movement or mistakes (e.g. missed ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** Dataset (p. 3); Dataset (p. 4); 4 Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Dataset | BENCHMARK / DATASET | Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often ... | p. 3 (Dataset) |
| 4 Experiments | BENCHMARK / DATASET | However, BC-RNN outperforms BC on all datasets (7%-35% improvement). | p. 6 (4 Experiments) |
| Figure/Table caption | BENCHMARK / DATASET | Table 1: Results on Low-Dimensional Observations. We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), ... | p. 3 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 5: (left) Effect of Policy Selection Criteria. We compare how performance decreases when choosing the policy to evaluate by using the lowest validation ... | p. 6 (Figure/Table caption) |
| 4 Experiments | BENCHMARK / DATASET | 4.1 Algorithm Comparison on Single and Multi-Human Demonstrations (C1, C2) We trained and evaluated all algorithms on the Proficient-Human (PH) and Multi-Human (MH) datasets ... | p. 5 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive body cue:** We collected 3 additional real-world datasets with a Franka robotic arm - Lift (Real), Can (Real), and Tool Hang (Real).
- **p. 4 / Dataset - extractive body cue:** To study the effect of observation modalities, we capture a diverse set of sensor streams when collecting the dataset, including end-effector, gripper fingers, and joints, ...
- **p. 6 / 4 Experiments - extractive body cue:** Appendix B shows the average trajectory lengths in each data subset - lower quality datasets contain demonstrations that take more time to solve the task.
- **p. 4 / Dataset - extractive body cue:** Datasets are collected by humans through RoboTurk [15, 17], a remote teleoperation platform.
- **p. 6 / 4 Experiments - extractive body cue:** BC-RNN maintains nearly the same performance as learning from ground-truth observations, providing an optimistic view for learning with real-world raw sensory observations. natural dataset distributions ...
- **p. 3 / Dataset - extractive body cue:** We further show that important design decisions made through our study in simulation directly translate to effective policy learning on real world tasks and datasets.
- **p. 5 / Dataset - extractive body cue:** Results show that less complex tasks (Lift, Can) be learned with a fraction of the data, while more complex tasks might benefit from even larger ...
- **p. 3 / Dataset - extractive body cue:** Differences in supervisor proficiency can manifest in many ways, such as large variations in trajectory length and noise in robot movement or mistakes (e.g. missed ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Tasks. We collect datasets across 6 operators of varying proficiency and evaluate offline policy learning methods on 8 challenging manipulation tasks that test ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1: Results on Low-Dimensional Observations. We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 2: Results on Suboptimal Human Data. We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Effect of Observation Space and Hyperparameter Choice. We show how the success rate that BC-RNN obtains can drop drastically due to changes to ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Effect of Dataset Size. We study how the BC-RNN success rate changes when lowering the quantity of data to 20% and 50%. Results ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3: Results on Image Observations.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: (left) Effect of Policy Selection Criteria. We compare how performance decreases when choosing the policy to evaluate by using the lowest validation loss, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We collected 3 additional real-world datasets with a Franka robotic arm - Lift (Real), Can (Real), and Tool Hang (Real). | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 4 (Dataset) |
| Task/environment | To study the effect of observation modalities, we capture a diverse set of sensor streams when collecting the dataset, including end-effector, gripper fingers, and ... | reset, timeout, object/scene variation | p. 4 (Dataset), p. 6 (4 Experiments) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 3 (Dataset), p. 4 (Dataset) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 3: Effect of Dataset Size. We study how the BC-RNN success rate changes when lowering the quantity of data to 20% and 50%. ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often ... | definition/direction/unit from same section | p. 3 (Dataset) |
| Table 1: Results on Low-Dimensional Observations. We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 5: (left) Effect of Policy Selection Criteria. We compare how performance decreases when choosing the policy to evaluate by using the lowest validation ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| 4.1 Algorithm Comparison on Single and Multi-Human Demonstrations (C1, C2) We trained and evaluated all algorithms on the Proficient-Human (PH) and Multi-Human (MH) datasets ... | definition/direction/unit from same section | p. 5 (4 Experiments) |
| We first note that less complex tasks (Lift, Can) can yield proficient policies (75%-100% success rate) using a small fraction of the data (20%). | definition/direction/unit from same section | p. 7 (4 Experiments) |
| We train BC-RNN and report the final policy checkpoint success rate, over 30 rollouts, due to the time-consuming nature of real world policy evaluation. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from ... | definition/direction/unit from same section | p. 4 (Dataset) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| BC-RNN is a strong baseline on suboptimal human data, but there is room for improvement. | comparison identity and matched condition | p. 6 (4 Experiments) |
| Results indicate that BC-RNN is a strong baseline, and that Batch RL methods perform poorly across all datasets, even on the simple diagnostic dataset. | comparison identity and matched condition | p. 4 (Dataset) |
| Interestingly, results are lower for MH datasets compared to PH datasets, even though the MH datasets contain 100 more demos (300 demos vs. | comparison identity and matched condition | p. 5 (4 Experiments) |
| The performance gap is larger for longer-horizon tasks (e.g. ⇠55% for Transport (PH) compared to ⇠5% for Square (PH)) and for multi-human data compared ... | comparison identity and matched condition | p. 5 (4 Experiments) |
| However, BC-RNN outperforms BC on all datasets (7%-35% improvement). | comparison identity and matched condition | p. 6 (4 Experiments) |
| We collected these datasets by first training a state-of-the-art RL algorithm [30] on the Lift and Can task, taking agent checkpoints that are saved ... | comparison identity and matched condition | p. 4 (Dataset) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.3 Effect of Observation Space (C5) Learning from image observations can match low-dim agent performance. | component/input/data sensitivity | p. 6 (4 Experiments) |
| (a) Effect of Policy Selection Criteria Dataset BC BC-RNN BCQ CQL Lift (PH) 100.0±0.0 100.0±0.0 98.0±1.6 52.0±13.0 Can (PH) 97.3±1.9 98.0±0.9 86.7±2.5 0.7±0.9 Square ... | component/input/data sensitivity | p. 6 (4 Experiments) |
| In Fig 2a, we study the effect of adding end effector velocities to the observations (+ EEF Vel), and joint positions and velocities to ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| 4.6 Effect of Dataset Size (C3) To study how dataset size impacts performance, we formed smaller 20% and 50% subsets of our human datasets ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| 3.2 Data Collection To study the effect of dataset source, we collected data from three different sources - MachineGenerated, Proficient-Human, and Multi-Human (more details ... | component/input/data sensitivity | p. 4 (Dataset) |
| To study the effect of observation modalities, we capture a diverse set of sensor streams when collecting the dataset, including end-effector, gripper fingers, and ... | component/input/data sensitivity | p. 4 (Dataset) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), and Multi-Human (MH) datasets. | Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often ... | PDF body cue; verify exact table/figure and matched conditions | p. 3 (Dataset), p. 6 (4 Experiments), p. 3 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (4 Experiments), p. 7 (4 Experiments) |
| Primary metric/result | However, BC-RNN outperforms BC on all datasets (7%-35% improvement). | numeric claim only at cited anchor | p. 6 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 3 / Dataset - extractive body cue:** BC BC-RNN BCQ CQL HBC IRIS Lift (MG) 65.3±2.5 70.7±3.4 91.3±1.9 64.0±2.8 47.3±4.1 96.0±1.6 Can (MG) 64.7±3.4 68.7±2.5 75.3±0.9 1.3±0.9 40.7±3.4 48.0±6.5 Lift (PH) 100.0±0.0 ...
- **p. 3 / Dataset - extractive body cue:** We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), and Multi-Human (MH) datasets.
- **p. 3 / Dataset - extractive body cue:** 3 Study Design 3.1 Tasks We conducted our study across 5 simulated and 3 real world tasks.
- **p. 4 / Dataset - extractive body cue:** We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", ...
- **p. 4 / Dataset - extractive body cue:** We collected these datasets by first training a state-of-the-art RL algorithm [30] on the Lift and Can task, taking agent checkpoints that are saved regularly ...
- **p. 5 / Dataset - extractive body cue:** Each agent is trained for N epochs, where each epoch consists of M gradient steps, and evaluated every E epochs, by running 50 rollouts in ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from ... | p. 4 (Dataset) |
| body limitation/failure cue | There is a strong expectation for batch RL algorithms to be able to distinguish between actions leading to successful placement and actions leading to ... | p. 6 (4 Experiments) |
| body limitation/failure cue | The final row of Table 2 shows additional results on a diagnostic dataset termed Can-Paired, where a single operator collected 2 demonstrations for each ... | p. 6 (4 Experiments) |
| body limitation/failure cue | In this section, we summarize the lessons from our study and make recommendations for future work. | p. 8 (5 Discussion) |
| body limitation/failure cue | Differences in supervisor proficiency can manifest in many ways, such as large variations in trajectory length and noise in robot movement or mistakes (e.g. ... | p. 3 (Dataset) |
| body limitation/failure cue | While recent batch RL algorithms have shown an excellent ability to learn from mixed quality machine-generated datasets [26, 27], we empirically find that they ... | p. 3 (Dataset) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| (larger LR) Increasing the learning rate from 1e-4 to 1e-3 affects the performance of image-agents substantially (drop of 35%-63%), while low-dim agents are more ... | p. 7 (4 Experiments) |
| 4.1 Algorithm Comparison on Single and Multi-Human Demonstrations (C1, C2) We trained and evaluated all algorithms on the Proficient-Human (PH) and Multi-Human (MH) datasets ... | p. 5 (4 Experiments) |
| We compare how performance decreases when choosing the policy to evaluate by using the lowest validation loss, or when using the final trained checkpoint, ... | p. 6 (4 Experiments) |
| Opting to use a GMM policy and a ResNet encoder appears to be uniformly better. | p. 7 (4 Experiments) |
| We also emphasize that no real-world hyperparameter tuning took place, so our results are a lower bound. | p. 8 (4 Experiments) |
| We train BC-RNN and report the final policy checkpoint success rate, over 30 rollouts, due to the time-consuming nature of real world policy evaluation. | p. 8 (4 Experiments) |
| In our study, we evaluate each policy checkpoint online in the environment in simulation, and report the best policy success rate per training run. | p. 3 (Dataset) |
| Each agent is trained for N epochs, where each epoch consists of M gradient steps, and evaluated every E epochs, by running 50 rollouts ... | p. 5 (Dataset) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Dataset - extractive body cue:** We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", ...
- **p. 6 / 4 Experiments - extractive body cue:** There is a strong expectation for batch RL algorithms to be able to distinguish between actions leading to successful placement and actions leading to task ...
- **p. 6 / 4 Experiments - extractive body cue:** The final row of Table 2 shows additional results on a diagnostic dataset termed Can-Paired, where a single operator collected 2 demonstrations for each of ...
- **p. 8 / 5 Discussion - extractive body cue:** In this section, we summarize the lessons from our study and make recommendations for future work.
- **p. 3 / Dataset - extractive body cue:** Differences in supervisor proficiency can manifest in many ways, such as large variations in trajectory length and noise in robot movement or mistakes (e.g. missed ...
- **p. 3 / Dataset - extractive body cue:** While recent batch RL algorithms have shown an excellent ability to learn from mixed quality machine-generated datasets [26, 27], we empirically find that they fail ...

- **Evidence anchors reviewed:** datasets p. 8 (4 Experiments), p. 4 (Dataset), p. 6 (4 Experiments), p. 4 (Dataset), p. 6 (4 Experiments), p. 3 (Dataset), metrics p. 5 (Figure/Table caption), p. 3 (Dataset), p. 3 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (4 Experiments), p. 7 (4 Experiments), baselines p. 6 (4 Experiments), p. 4 (Dataset), p. 5 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments), p. 4 (Dataset), results p. 3 (Dataset), p. 6 (4 Experiments), p. 3 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (4 Experiments), p. 7 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 2: Results on Suboptimal Human Data. We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations ... (p. 4, Figure/Table caption).
- **Metric evidence:** We first note that less complex tasks (Lift, Can) can yield proficient policies (75%-100% success rate) using a small fraction of the data (20%). (p. 7, 4 Experiments).
- **Baseline/ablation evidence:** Interestingly, results are lower for MH datasets compared to PH datasets, even though the MH datasets contain 100 more demos (300 demos vs. (p. 5, 4 Experiments).
- **Failure/negative evidence:** We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", "Adequate", and "Worse" human operators, ... (p. 4, Dataset).
