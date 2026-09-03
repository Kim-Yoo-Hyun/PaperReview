# Evaluation - DrEureka: Language Model Guided Sim-To-Real Transfer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p094.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p094.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 26 (Figure/Table caption), p. 28 (Figure/Table caption)): The task of forward locomotion is to walk forward at 2 meters-per-second on flat terrains; while it is possible for the robot to walk forward at a higher speed, we ...

## Evaluation Body Digest

- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** We use the simulation environment as well as the real-world controller from Margolis et al.
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** We adopt commercially available, low-cost robots with well-supported open-sourced simulators as our evaluation platforms.
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** To verify that a policy outputted by a reward-design algorithm itself is not effective for real-world deployment, we also compare against Eureka [9], which designs ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** Note that while CEM and BayRn tackle the same problem, their iterative procedure is conceptually different from DrEureka, which trains all policies in parallel; thus, ...
- **p. 21 / Figure/Table caption - extractive body cue:** Fig. 8: Forward locomotion training curves for 16 DR configurations. All runs are trained with the same reward function. B3. LLM Reward Reflection The following ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** Therefore, the differences in performance between DrEureka and Human-Designed can be attributed to the different DR parameters as well as reward functions DrEureka produces.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: DrEureka takes the task and safety instruction, along with environment source code, and runs Eureka to generate a regularized reward function and policy. ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** The blue paragraph describes the instruction, and the green paragraph is the reward aware parameter prior computed in Algorithm 2.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** V. EXPERIMENTAL SETUP (p. 5); VI. RESULTS AND ANALYSIS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTAL SETUP | EMPIRICAL / REAL-ROBOT OR HARDWARE | The task of forward locomotion is to walk forward at 2 meters-per-second on flat terrains; while it is possible for the robot to walk ... | p. 5 (V. EXPERIMENTAL SETUP) |
| V. EXPERIMENTAL SETUP | EMPIRICAL / REAL-ROBOT OR HARDWARE | DrEureka's average and best policies outperform Human-Designed and a prior reward-design baseline. | p. 6 (V. EXPERIMENTAL SETUP) |
| V. EXPERIMENTAL SETUP | EMPIRICAL / REAL-ROBOT OR HARDWARE | Additionally, we consider two classes of DrEureka ablations that probe (1) whether some fixed DR configuration can generally outperform DrEureka samples, and (2) the ... | p. 6 (V. EXPERIMENTAL SETUP) |
| V. EXPERIMENTAL SETUP | EMPIRICAL / REAL-ROBOT OR HARDWARE | To understand the best and the average performance of DrEureka, we train policies for all 16 configurations and evaluate all policies in the real ... | p. 5 (V. EXPERIMENTAL SETUP) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 9: Policies trained on DrEureka DR configurations exert less torque in the real world. E. Additional Ablation Results Sampling from DrEureka priors enables ... | p. 26 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** We use the simulation environment as well as the real-world controller from Margolis et al.
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** We adopt commercially available, low-cost robots with well-supported open-sourced simulators as our evaluation platforms.
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** To verify that a policy outputted by a reward-design algorithm itself is not effective for real-world deployment, we also compare against Eureka [9], which designs ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** Note that while CEM and BayRn tackle the same problem, their iterative procedure is conceptually different from DrEureka, which trains all policies in parallel; thus, ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: DrEureka takes the task and safety instruction, along with environment source code, and runs Eureka to generate a regularized reward function and policy. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Our quadruped locomotion, dexterous cube rotation, and walk- ing globe tasks. Walking globe is a novel task to show DrEureka's capability for guiding ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: DrEureka prompt for generating domain randomization parameters. The blue paragraph describes the instruction, and the green paragraph is the reward aware parameter prior ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: The default real-world environment as well as additional envi- ronments to test DrEureka's robustness for quadrupedal locomotion. Default Socks Grass Sidewalk 0.0 0.5
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Real-world robustness evaluation. DrEureka performs consistently across different terrains and maintains advantages over Human-Designed. DrEureka uses physical knowledge to construct DR ranges. DrEureka ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Walking Globe sim and real environments. In lab settings, we loosely strap the robot horizontally to a center point to prevent robot from ...
- **p. 20 / Figure/Table caption - extractive body cue:** Fig. 7: Visualization of DR parameter ranges sampled by DrEureka for forward locomotion: Blue represents the lower bound of the sampled DR parameter range and ...
- **p. 21 / Figure/Table caption - extractive body cue:** Fig. 8: Forward locomotion training curves for 16 DR configurations. All runs are trained with the same reward function. B3. LLM Reward Reflection The following ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We use the simulation environment as well as the real-world controller from Margolis et al. | embodiment, simulator version and control stack | p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP) |
| Task/environment | We adopt commercially available, low-cost robots with well-supported open-sourced simulators as our evaluation platforms. | reset, timeout, object/scene variation | p. 5 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 3 (III. PROBLEM SETTING), p. 3 (IV. METHOD) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 4 (IV. METHOD), p. 4 (IV. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 8: Forward locomotion training curves for 16 DR configurations. All runs are trained with the same reward function. B3. LLM Reward Reflection The ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Therefore, the differences in performance between DrEureka and Human-Designed can be attributed to the different DR parameters as well as reward functions DrEureka produces. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL SETUP) |
| Fig. 1: DrEureka takes the task and safety instruction, along with environment source code, and runs Eureka to generate a regularized reward function and ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| The blue paragraph describes the instruction, and the green paragraph is the reward aware parameter prior computed in Algorithm 2. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTAL SETUP) |
| DrEureka uses GPT-4 [65] as the backbone LLM, and we use the original Eureka hyperparameters for reward generation before sampling 16 DR configurations. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTAL SETUP) |
| DrEureka's average and best policies outperform Human-Designed and a prior reward-design baseline. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL SETUP) |
| Fig. 9: Policies trained on DrEureka DR configurations exert less torque in the real world. E. Additional Ablation Results Sampling from DrEureka priors enables ... | definition/direction/unit from same section | p. 26 (Figure/Table caption) |
| Fig. 12: Comparison between DrEureka and Human-Designed reward functions on the simulation locomotion task. DrEureka has higher sample efficiency and asymptotic performance, while Human-Designed ... | definition/direction/unit from same section | p. 27 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Forward locomotion specifically uses a teacher-student variant of PPO in which the teacher Sim-to-real Configuration Forward Velocity (m/s) Meters Traveled (m) Human-Designed [25] 1.32 ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTAL SETUP) |
| DrEureka's average and best policies outperform Human-Designed and a prior reward-design baseline. | comparison identity and matched condition | p. 6 (V. EXPERIMENTAL SETUP) |
| We primarily compare to the human-designed reward function and DR configuration from the original task implementations [25, 30] as reference; We refer to this ... | comparison identity and matched condition | p. 5 (V. EXPERIMENTAL SETUP) |
| Note that this baseline for forward locomotion trains a velocity-conditioned policy and utilizes a reward function with a velocity curriculum that gradually increases as ... | comparison identity and matched condition | p. 5 (V. EXPERIMENTAL SETUP) |
| Fig. 13: DrEureka with safety instruction successfully learns transferable gait from simulation to real. In contrast, removing the safety instruction leads to behavior that ... | comparison identity and matched condition | p. 28 (Figure/Table caption) |
| Fig. 2: Our quadruped locomotion, dexterous cube rotation, and walk- ing globe tasks. Walking globe is a novel task to show DrEureka's capability for ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Forward locomotion specifically uses a teacher-student variant of PPO in which the teacher Sim-to-real Configuration Forward Velocity (m/s) Meters Traveled (m) Human-Designed [25] 1.32 ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTAL SETUP) |
| In the second category of ablations, we consider an ablation that only has access to the set of physics parameters but without the reward-aware ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTAL SETUP) |
| Fig. 9: Policies trained on DrEureka DR configurations exert less torque in the real world. E. Additional Ablation Results Sampling from DrEureka priors enables ... | component/input/data sensitivity | p. 26 (Figure/Table caption) |
| 1In both Without Prior and Uninformative Prior experiments, 15 out of the 16 policies resulted in jerky and dangerous behavior, many times immediately triggering ... | component/input/data sensitivity | p. 5 (V. EXPERIMENTAL SETUP) |
| Fig. 2: Our quadruped locomotion, dexterous cube rotation, and walk- ing globe tasks. Walking globe is a novel task to show DrEureka's capability for ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Fig. 1: DrEureka takes the task and safety instruction, along with environment source code, and runs Eureka to generate a regularized reward function and ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we propose DrEureka (Domain Randomization Eureka), a novel algorithm that leverages LLMs to automate reward design and domain randomization parameter configuration ... | The task of forward locomotion is to walk forward at 2 meters-per-second on flat terrains; while it is possible for the robot to walk ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 26 (Figure/Table caption), p. 28 (Figure/Table caption) |
| Primary metric/result | DrEureka's average and best policies outperform Human-Designed and a prior reward-design baseline. | numeric claim only at cited anchor | p. 6 (V. EXPERIMENTAL SETUP) |

- Numeric sentences retained from the body:
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** The Go1 is a small quadrupedal robot with 12 degrees of freedom across four legs.
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** The task of forward locomotion is to walk forward at 2 meters-per-second on flat terrains; while it is possible for the robot to walk forward ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** Here, we use the LEAP hand [30], which is a low-cost anthropomorphic robot hand, featuring 16 degrees of freedom distributed among three fingers and a ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** Forward locomotion specifically uses a teacher-student variant of PPO in which the teacher Sim-to-real Configuration Forward Velocity (m/s) Meters Traveled (m) Human-Designed [25] 1.32 ± ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** Sim-to-real Configuration Rotation (rad) Time-to-Fall (s) Human-Designed [25] 3.24 ± 1.66 20.00 ± 0.00 Our Method (Best) 9.39 ± 4.15 20.00 ± 0.00 Our Method ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are several areas of improvement to the ... | p. 9 (VIII. LIMITATIONS) |
| body limitation/failure cue | Sim-to-real Configuration Rotation (rad) Time-to-Fall (s) Human-Designed [25] 3.24 ± 1.66 20.00 ± 0.00 Our Method (Best) 9.39 ± 4.15 20.00 ± 0.00 Our ... | p. 6 (V. EXPERIMENTAL SETUP) |
| body limitation/failure cue | Fig. 6: Walking Globe sim and real environments. In lab settings, we loosely strap the robot horizontally to a center point to prevent robot ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Fig. 13: DrEureka with safety instruction successfully learns transferable gait from simulation to real. In contrast, removing the safety instruction leads to behavior that ... | p. 28 (Figure/Table caption) |
| body limitation/failure cue | Incorporating vision-based inputs could potentially improve the robustness and generalizability of the learned policies in the real world, where visual cues play a critical ... | p. 9 (VIII. LIMITATIONS) |
| body limitation/failure cue | This task is challenging because the policy only receives 16 joint angles and proprioceptive history, encoded via GRU [63], as observations and does not ... | p. 5 (V. EXPERIMENTAL SETUP) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Algorithm 1 DrEureka Reward Design 1: Require: Task description ltask, safety instruction lsafety, RL algorithm A, environment code M, coding LLM LLM, fitness function ... | p. 4 (IV. METHOD) |
| For every DR configuration, we train policies using 3 random seeds and report average as well as standard deviation across trials and seeds. | p. 6 (V. EXPERIMENTAL SETUP) |
| We count these trials as 0m/s, 0m traveled. | p. 5 (V. EXPERIMENTAL SETUP) |
| The blue paragraph describes the instruction, and the green paragraph is the reward aware parameter prior computed in Algorithm 2. | p. 5 (V. EXPERIMENTAL SETUP) |
| Second, we consider a baseline that trains with the human-designed DR (Human-Designed DR) in the original implementation. | p. 6 (V. EXPERIMENTAL SETUP) |
| This is a challenging problem because we do not have access to the real-world environment M ∗at training time. | p. 4 (IV. METHOD) |
| In Eureka, the LLM first takes the task description ltask and a summary of the environment state and action spaces (provided by environment code ... | p. 3 (IV. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / VIII. LIMITATIONS - extractive body cue:** While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are several areas of improvement to the current ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** Sim-to-real Configuration Rotation (rad) Time-to-Fall (s) Human-Designed [25] 3.24 ± 1.66 20.00 ± 0.00 Our Method (Best) 9.39 ± 4.15 20.00 ± 0.00 Our Method ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Walking Globe sim and real environments. In lab settings, we loosely strap the robot horizontally to a center point to prevent robot from ...
- **p. 28 / Figure/Table caption - extractive body cue:** Fig. 13: DrEureka with safety instruction successfully learns transferable gait from simulation to real. In contrast, removing the safety instruction leads to behavior that exploits ...
- **p. 9 / VIII. LIMITATIONS - extractive body cue:** Incorporating vision-based inputs could potentially improve the robustness and generalizability of the learned policies in the real world, where visual cues play a critical role ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** This task is challenging because the policy only receives 16 joint angles and proprioceptive history, encoded via GRU [63], as observations and does not have ...

- **Evidence anchors reviewed:** datasets p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), metrics p. 21 (Figure/Table caption), p. 6 (V. EXPERIMENTAL SETUP), p. 2 (Figure/Table caption), p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), baselines p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 28 (Figure/Table caption), p. 2 (Figure/Table caption), results p. 5 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 26 (Figure/Table caption), p. 28 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Note that while CEM and BayRn tackle the same problem, their iterative procedure is conceptually different from DrEureka, which trains all policies in parallel; thus, this comparison favors the baselines ... (p. 6, V. EXPERIMENTAL SETUP).
- **Metric evidence:** Therefore, the differences in performance between DrEureka and Human-Designed can be attributed to the different DR parameters as well as reward functions DrEureka produces. (p. 6, V. EXPERIMENTAL SETUP).
- **Baseline/ablation evidence:** Forward locomotion specifically uses a teacher-student variant of PPO in which the teacher Sim-to-real Configuration Forward Velocity (m/s) Meters Traveled (m) Human-Designed [25] 1.32 ± 0.44 4.17 ± 1.57 Eureka ... (p. 6, V. EXPERIMENTAL SETUP).
- **Failure/negative evidence:** While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are several areas of improvement to the current implementation: • Lack of visual ... (p. 9, VIII. LIMITATIONS).
