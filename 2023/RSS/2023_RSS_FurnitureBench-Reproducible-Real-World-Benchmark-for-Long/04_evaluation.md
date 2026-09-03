# Evaluation - FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2305.12821; PDF retrieval source: https://arxiv.org/pdf/2305.12821. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS), p. 8 (VI. BENCHMARKING RESULTS), p. 6 (Figure/Table caption), p. 8 (VI. BENCHMARKING RESULTS), p. 9 (Figure/Table caption)): The "pushing" skill in drawer achieves 30% success rate, which is slightly worse than that of the "grasping" skill (60%), with BC.

## Evaluation Body Digest

- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** But, this benchmark environment and tasks can be also used for research in TAMP.
- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** To validate our benchmark for the full-assembly evaluation, we additionally benchmark a simpler task, one_leg assembly, with 1000 demonstrations.
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** A trained model is evaluated for 10 episodes, where their initial states are set following the provided task initialization guide tool.
- **p. 8 / VI. BENCHMARKING RESULTS - extractive body cue:** In summary, the one_leg assembly experiments verify that our benchmark is tractable but the algorithms require a huge amount of data to solve a part ...
- **p. 8 / VI. BENCHMARKING RESULTS - extractive body cue:** In Table IV, the IQL-R3M policies trained with 2000 demonstrations in the mixed dataset (Mixed data) show significant improvements, 4.6 and 3.7 completed phases on ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** Our benchmark first measures the number of completed part assembly.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 10: Full-assembly benchmark results. We report the number of completed phases averaged over 10 episodes and the error bars indicating the minimum and maximum ...
- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** The "pushing" skill in drawer achieves 30% success rate, which is slightly worse than that of the "grasping" skill (60%), with BC.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** V. EXPERIMENTAL SETUP (p. 6); VI. BENCHMARKING RESULTS (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| VI. BENCHMARKING RESULTS | BENCHMARK / DATASET | The "pushing" skill in drawer achieves 30% success rate, which is slightly worse than that of the "grasping" skill (60%), with BC. | p. 7 (VI. BENCHMARKING RESULTS) |
| VI. BENCHMARKING RESULTS | BENCHMARK / DATASET | However, in lamp and round_table, where the round-shaped parts need to be screwed, IQL struggles and achieves only 10% and 0% success rates, respectively. | p. 7 (VI. BENCHMARKING RESULTS) |
| VI. BENCHMARKING RESULTS | BENCHMARK / DATASET | Figures 8 and 10 show that IQL-R3M achieves 4 phases on average and 40% success rate on the low randomness level. | p. 8 (VI. BENCHMARKING RESULTS) |
| Figure/Table caption | BENCHMARK / DATASET | Fig. 8: Correlation between FurnitureBench and Furni- tureSim. We compare the performance of IL and offline RL methods with respect to the dataset size ... | p. 6 (Figure/Table caption) |
| VI. BENCHMARKING RESULTS | BENCHMARK / DATASET | Does more data improve the performance? | p. 8 (VI. BENCHMARKING RESULTS) |

## Dataset / Benchmark Role

- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** But, this benchmark environment and tasks can be also used for research in TAMP.
- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** To validate our benchmark for the full-assembly evaluation, we additionally benchmark a simpler task, one_leg assembly, with 1000 demonstrations.
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** A trained model is evaluated for 10 episodes, where their initial states are set following the provided task initialization guide tool.
- **p. 8 / VI. BENCHMARKING RESULTS - extractive body cue:** In summary, the one_leg assembly experiments verify that our benchmark is tractable but the algorithms require a huge amount of data to solve a part ...
- **p. 8 / VI. BENCHMARKING RESULTS - extractive body cue:** In Table IV, the IQL-R3M policies trained with 2000 demonstrations in the mixed dataset (Mixed data) show significant improvements, 4.6 and 3.7 completed phases on ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** Our benchmark first measures the number of completed part assembly.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: FurnitureBench: reproducible real-world furniture assembly benchmark. Benchmarking furniture assembly poses to address many robotic manipulation challenges: long-horizon planning, dexterous control, and visual perception. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Real-world furniture assembly environment. Our reproducible robot system (a) and visual observations from the front-view camera (b) and wrist camera (c). of long-horizon ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 3: 3D printed furniture models. Each furniture is designed inspired by IKEA furniture. Due to the limitations imposed by using a single robotic arm, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Overview of a furniture assembly task, chair. Furniture assembly requires many dexterous skills, including grasping, re-orienting, inserting, and screwing. The part in contact ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 5: Reproducibility analysis. We evaluate the number of completed subtasks (i.e., phases) of an IQL policy on the one_leg assembly task in 10 newly ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: Task initialization GUI tool. To evaluate our bench- marks with the proper distribution of initial poses of furniture parts, we provide a task ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: FurnitureSim: simulated version of FurnitureBench. FurnitureSim provides realistic physics simulation and render- ing: (a) fast online rendering and (b) photorealistic offline rendering with ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 8: Correlation between FurnitureBench and Furni- tureSim. We compare the performance of IL and offline RL methods with respect to the dataset size between ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | But, this benchmark environment and tasks can be also used for research in TAMP. | embodiment, simulator version and control stack | p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS) |
| Task/environment | To validate our benchmark for the full-assembly evaluation, we additionally benchmark a simpler task, one_leg assembly, with 1000 demonstrations. | reset, timeout, object/scene variation | p. 7 (VI. BENCHMARKING RESULTS), p. 6 (V. EXPERIMENTAL SETUP) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (I. INTRODUCTION), p. 7 (2) The furniture parts are rearranged using our provided) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 10: Full-assembly benchmark results. We report the number of completed phases averaged over 10 episodes and the error bars indicating the minimum and ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| The "pushing" skill in drawer achieves 30% success rate, which is slightly worse than that of the "grasping" skill (60%), with BC. | definition/direction/unit from same section | p. 7 (VI. BENCHMARKING RESULTS) |
| First 5 skills of each furniture task are independently evaluated and the average success rates over 10 trials are reported in percentage. | definition/direction/unit from same section | p. 7 (VI. BENCHMARKING RESULTS) |
| Fig. 8: Correlation between FurnitureBench and Furni- tureSim. We compare the performance of IL and offline RL methods with respect to the dataset size ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 11: Simulation benchmark results. Using our Furni- tureSim simulator, we evaluate BC and IQL with diverse visual encoders in the one_leg assembly task ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 5. The pre-trained policy is expected to complete over 3 phases on average (such as picking up the leg and occasionally inserting it), ... | definition/direction/unit from same section | p. 35 (Figure/Table caption) |
| Fig. 17: Furniture 3D models. IKEA model furniture (left), 3D furniture model (middle), and 3D printed furniture model (right). Each furniture model introduces unique ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| We provide three different levels of randomness in the initial states: (a) low fixes part poses and allows only a little human error, (b) ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL SETUP) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We evaluate our benchmark with imitation learning (BC) and the state-of-the-art offline RL (IQL) methods. | comparison identity and matched condition | p. 6 (V. EXPERIMENTAL SETUP) |
| Please refer to Section D for implementation details. • BC (Behavioral Cloning [48]) fits a policy to the demonstration state-action pairs (s, a) with ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTAL SETUP) |
| We evaluate an IL algorithm (BC [48] with the ResNet-18 encoder [20]) and the state-of-the-art offline RL algorithm (IQL [28] with R3M features [41]) ... | comparison identity and matched condition | p. 7 (VI. BENCHMARKING RESULTS) |
| In Table IV, the IQL-R3M policies trained with 2000 demonstrations in the mixed dataset (Mixed data) show significant improvements, 4.6 and 3.7 completed phases ... | comparison identity and matched condition | p. 8 (VI. BENCHMARKING RESULTS) |
| 3This paper focuses on benchmarking end-to-end learning approaches since engineering furniture assembly procedures using TAMP without having access to state information is beyond the ... | comparison identity and matched condition | p. 7 (VI. BENCHMARKING RESULTS) |
| This result means that the policies mostly fail to grasp the table leg without the wrist camera. | comparison identity and matched condition | p. 8 (VI. BENCHMARKING RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 3This paper focuses on benchmarking end-to-end learning approaches since engineering furniture assembly procedures using TAMP without having access to state information is beyond the ... | component/input/data sensitivity | p. 7 (VI. BENCHMARKING RESULTS) |
| This result means that the policies mostly fail to grasp the table leg without the wrist camera. | component/input/data sensitivity | p. 8 (VI. BENCHMARKING RESULTS) |
| Without the wrist camera input, the performance drops significantly from 3.8 and 3.0 to 2.0 and 1.3 on the low and medium randomness levels, ... | component/input/data sensitivity | p. 8 (VI. BENCHMARKING RESULTS) |
| Fig. 13: AprilTag placeholder. For easy and accurate marker placement, all 3D models have AprilTag placeholders on their surfaces with corresponding AprilTag IDs. of ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate ... | The "pushing" skill in drawer achieves 30% success rate, which is slightly worse than that of the "grasping" skill (60%), with BC. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS), p. 8 (VI. BENCHMARKING RESULTS), p. 6 (Figure/Table caption), p. 8 (VI. BENCHMARKING RESULTS), p. 9 (Figure/Table caption) |
| Primary metric/result | However, in lamp and round_table, where the round-shaped parts need to be screwed, IQL struggles and achieves only 10% and 0% success rates, respectively. | numeric claim only at cited anchor | p. 7 (VI. BENCHMARKING RESULTS) |

- Numeric sentences retained from the body:
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** A trained model is evaluated for 10 episodes, where their initial states are set following the provided task initialization guide tool.
- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** First 5 skills of each furniture task are independently evaluated and the average success rates over 10 trials are reported in percentage.
- **p. 8 / VI. BENCHMARKING RESULTS - extractive body cue:** We report the number of completed phases averaged over 10 episodes and the error bars indicating the minimum and maximum completed phases.
- **p. 8 / VI. BENCHMARKING RESULTS - extractive body cue:** We evaluate IQLR3M under diverse settings and report the average completed phases over 10 episodes. low med Original low (low randomness data) 3.8 - Original ...
- **p. 7 / 2) The furniture parts are rearranged using our provided - extractive body cue:** 3) A policy controls the robot until it completes the task, stops motions for 5 sec, shows unsafe movements, exceeds 350 steps per skill, or ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 17: Furniture 3D models. IKEA model furniture (left), 3D furniture model (middle), and 3D printed furniture model (right). Each furniture model introduces unique ... | p. 18 (Figure/Table caption) |
| body limitation/failure cue | The failure of these algorithms to even attach a pair of furniture parts despite the high-quality demonstration dataset highlights the need for further algorithmic ... | p. 7 (VI. BENCHMARKING RESULTS) |
| body limitation/failure cue | On the other hand, both algorithms struggle at "inserting" skill, which shows from 0% to 20% success rates. "Inserting" requires precise control to correctly ... | p. 7 (VI. BENCHMARKING RESULTS) |
| body limitation/failure cue | Fig. 3: 3D printed furniture models. Each furniture is designed inspired by IKEA furniture. Due to the limitations imposed by using a single robotic ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | It always achieves the phase 3 (grasping the leg) but fails at inserting 60% of the time. | p. 8 (VI. BENCHMARKING RESULTS) |
| body limitation/failure cue | This result reassures that "inserting" is the most challenging skill as it involves stochastic and frequent collisions. | p. 8 (VI. BENCHMARKING RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Please refer to Section D for implementation details. • BC (Behavioral Cloning [48]) fits a policy to the demonstration state-action pairs (s, a) with ... | p. 6 (V. EXPERIMENTAL SETUP) |
| Each individual trial is conducted according to the following procedure: | p. 7 (V. EXPERIMENTAL SETUP) |
| The task horizon is approximately 500 timesteps. | p. 7 (VI. BENCHMARKING RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 18 / Figure/Table caption - extractive body cue:** Fig. 17: Furniture 3D models. IKEA model furniture (left), 3D furniture model (middle), and 3D printed furniture model (right). Each furniture model introduces unique interactions ...
- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** The failure of these algorithms to even attach a pair of furniture parts despite the high-quality demonstration dataset highlights the need for further algorithmic improvements ...
- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** On the other hand, both algorithms struggle at "inserting" skill, which shows from 0% to 20% success rates. "Inserting" requires precise control to correctly align ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 3: 3D printed furniture models. Each furniture is designed inspired by IKEA furniture. Due to the limitations imposed by using a single robotic arm, ...
- **p. 8 / VI. BENCHMARKING RESULTS - extractive body cue:** It always achieves the phase 3 (grasping the leg) but fails at inserting 60% of the time.
- **p. 8 / VI. BENCHMARKING RESULTS - extractive body cue:** This result reassures that "inserting" is the most challenging skill as it involves stochastic and frequent collisions.

- **Evidence anchors reviewed:** datasets p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS), p. 6 (V. EXPERIMENTAL SETUP), p. 8 (VI. BENCHMARKING RESULTS), p. 8 (VI. BENCHMARKING RESULTS), p. 6 (V. EXPERIMENTAL SETUP), metrics p. 8 (Figure/Table caption), p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS), p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 35 (Figure/Table caption), baselines p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 7 (VI. BENCHMARKING RESULTS), p. 8 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS), p. 8 (VI. BENCHMARKING RESULTS), results p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS), p. 8 (VI. BENCHMARKING RESULTS), p. 6 (Figure/Table caption), p. 8 (VI. BENCHMARKING RESULTS), p. 9 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (35 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Fig. 10: Full-assembly benchmark results. We report the number of completed phases averaged over 10 episodes and the error bars indicating the minimum and maximum completed phases. The background color ... (p. 8, Figure/Table caption).
- **Metric evidence:** The "pushing" skill in drawer achieves 30% success rate, which is slightly worse than that of the "grasping" skill (60%), with BC. (p. 7, VI. BENCHMARKING RESULTS).
- **Baseline/ablation evidence:** We evaluate our benchmark with imitation learning (BC) and the state-of-the-art offline RL (IQL) methods. (p. 6, V. EXPERIMENTAL SETUP).
- **Failure/negative evidence:** On the other hand, both algorithms struggle at "inserting" skill, which shows from 0% to 20% success rates. "Inserting" requires precise control to correctly align a screw and a hole, ... (p. 7, VI. BENCHMARKING RESULTS).
