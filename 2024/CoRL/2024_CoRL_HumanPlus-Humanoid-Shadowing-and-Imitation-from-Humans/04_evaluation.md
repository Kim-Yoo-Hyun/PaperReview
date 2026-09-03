# Evaluation - HumanPlus: Humanoid Shadowing and Imitation from Humans

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=WnSl42M9Z4; PDF retrieval source: https://arxiv.org/pdf/2406.10454. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (9. Experiments on Imitation), p. 9 (Figure/Table caption), p. 9 (8.1. Comparisons with Other Teleoperation), p. 10 (9. Experiments on Imitation)): Our HIT achieves higher success rates than other baselines across all tasks.

## Evaluation Body Digest

- **p. 10 / 9. Experiments on Imitation - extractive body cue:** Shown in Table 5, we compare our imitation learning method Humanoid Imitation Transformer with three baseline methods: HIT policies with monocular inputs (Monocular), ACT [104], ...
- **p. 10 / 8.1. Comparisons with Other Teleoperation - extractive body cue:** While ALOHA enables precise control of robot joint angles, its fixed hardware setup makes it harder to adapt to people with different heights and body ...
- **p. 9 / 8.1. Comparisons with Other Teleoperation - extractive body cue:** The participants are tasked to perform the Rearrange Objects task and its variant, Rearrange Lower Objects, where an object is placed on a lower table ...
- **p. 9 / 8.1. Comparisons with Other Teleoperation - extractive body cue:** For ALOHA, we build a pair of bimanual arms for pupputeering from two WidowX 250 robots with similar kinematic structure as our humanoid arms.
- **p. 10 / 8.1. Comparisons with Other Teleoperation - extractive body cue:** In contrast, our system has the lowest timeto-completion, has the highest success rate of stable standing, and is the only method that can be used ...
- **p. 9 / 8.1. Comparisons with Other Teleoperation - extractive body cue:** We also record the average success rates of stable standing during teleoperation 9
- **p. 9 / 8. Experiments on Shadowing - extractive body cue:** We show success rates of Humanoid Imitation Transformer (Ours), HIT with monocular input, ACT and open-loop trajectory replay across all tasks.
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** Our HIT achieves higher success rates than other baselines across all tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 8. Experiments on Shadowing (p. 8); 8.2. Robustness Evaluation (p. 10); 9. Experiments on Imitation (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 9. Experiments on Imitation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our HIT achieves higher success rates than other baselines across all tasks. | p. 10 (9. Experiments on Imitation) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5: Comparisons on Imitation. We show success rates of Humanoid Imitation Transformer (Ours), HIT with monocular input, ACT and open-loop trajectory replay across ... | p. 9 (Figure/Table caption) |
| 8.1. Comparisons with Other Teleoperation | EMPIRICAL / REAL-ROBOT OR HARDWARE | We also record the average success rates of stable standing during teleoperation 9 | p. 9 (8.1. Comparisons with Other Teleoperation) |
| 9. Experiments on Imitation | EMPIRICAL / REAL-ROBOT OR HARDWARE | We calculate the success rate for a sub-task by dividing the number of successful attempts by the number of total attempts. | p. 10 (9. Experiments on Imitation) |

## Dataset / Benchmark Role

- **p. 10 / 9. Experiments on Imitation - extractive body cue:** Shown in Table 5, we compare our imitation learning method Humanoid Imitation Transformer with three baseline methods: HIT policies with monocular inputs (Monocular), ACT [104], ...
- **p. 10 / 8.1. Comparisons with Other Teleoperation - extractive body cue:** While ALOHA enables precise control of robot joint angles, its fixed hardware setup makes it harder to adapt to people with different heights and body ...
- **p. 9 / 8.1. Comparisons with Other Teleoperation - extractive body cue:** The participants are tasked to perform the Rearrange Objects task and its variant, Rearrange Lower Objects, where an object is placed on a lower table ...
- **p. 9 / 8.1. Comparisons with Other Teleoperation - extractive body cue:** For ALOHA, we build a pair of bimanual arms for pupputeering from two WidowX 250 robots with similar kinematic structure as our humanoid arms.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Stanford HumanPlus Robot. We present a full-stack system for humanoid robots to learn motion and autonomous skills from human data. Our system enables ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Hardware Details. Our HumanPlus robot has two egocentric RGB cameras mounted on the head, two 6-DoF dexterous hands, and 33 degrees of freedom ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Shadowing and Retargeting. Our system uses one RGB camera for body and hand pose estimation. prior works have done teleoperation in operation spaces ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Model Architectures. Our system consists of a decoder-only transformer for low-level control, Humanoid Shadowing Transformer, and a decoder-only transformer for imitation learning, Humanoid ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Rewards in Simulation. We denote vx as linear x velocity, vy as linear y velocity, vyaw as angular yaw velocity, q as joint ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2: Randomization in Simulation. We uniformly sample from these randomization ranges during training in simulation. pose estimator using a single RGB camera, for real- ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Task Definitions. We illustrate 5 autonomous tasks through imitation learning, and 5 shadowing tasks. Details are in Section 7. a 1000Hz PD controller. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Teleop Comparisons & User Studies. We report averaged completion time for 6 participants on 2 tasks. target poses while saving energy and avoiding ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Shown in Table 5, we compare our imitation learning method Humanoid Imitation Transformer with three baseline methods: HIT policies with monocular inputs (Monocular), ACT ... | embodiment, simulator version and control stack | p. 10 (9. Experiments on Imitation), p. 10 (8.1. Comparisons with Other Teleoperation) |
| Task/environment | While ALOHA enables precise control of robot joint angles, its fixed hardware setup makes it harder to adapt to people with different heights and ... | reset, timeout, object/scene variation | p. 10 (8.1. Comparisons with Other Teleoperation), p. 9 (8.1. Comparisons with Other Teleoperation) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 5 (5. Shadowing of Human Motion) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In contrast, our system has the lowest timeto-completion, has the highest success rate of stable standing, and is the only method that can be ... | definition/direction/unit from same section | p. 10 (8.1. Comparisons with Other Teleoperation) |
| We also record the average success rates of stable standing during teleoperation 9 | definition/direction/unit from same section | p. 9 (8.1. Comparisons with Other Teleoperation) |
| We show success rates of Humanoid Imitation Transformer (Ours), HIT with monocular input, ACT and open-loop trajectory replay across all tasks. | definition/direction/unit from same section | p. 9 (8. Experiments on Shadowing) |
| Our HIT achieves higher success rates than other baselines across all tasks. | definition/direction/unit from same section | p. 10 (9. Experiments on Imitation) |
| Table 1: Rewards in Simulation. We denote vx as linear x velocity, vy as linear y velocity, vyaw as angular yaw velocity, q as ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 3: Teleop Comparisons & User Studies. We report averaged completion time for 6 participants on 2 tasks. target poses while saving energy and ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 4: Model Architectures. Our system consists of a decoder-only transformer for low-level control, Humanoid Shadowing Transformer, and a decoder-only transformer for imitation learning, ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 3: Shadowing and Retargeting. Our system uses one RGB camera for body and hand pose estimation. prior works have done teleoperation in operation ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Overall HIT (Ours) outperforms others. | comparison identity and matched condition | p. 9 (8. Experiments on Shadowing) |
| Shown in Table 3, all baselines do not support whole-body control and require at least two human operators for hand pose estimation. | comparison identity and matched condition | p. 9 (8.1. Comparisons with Other Teleoperation) |
| Our HIT achieves higher success rates than other baselines across all tasks. | comparison identity and matched condition | p. 10 (9. Experiments on Imitation) |
| Firstly, our hardware platform offers fewer degrees of freedom compared to human anatomy. | comparison identity and matched condition | p. 10 (9. Experiments on Imitation) |
| Figure 7: Maximum Force Thresholds. Our low-level policy can withstand larger forces compared to H1 Default controller. either left or right of the basket. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 6: Baseline Teleoperation Systems. with dexterous hands and capability in agile locomo- tion like standing up and walk while wearing shoes. The shoe ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The participants are tasked to perform the Rearrange Objects task and its variant, Rearrange Lower Objects, where an object is placed on a lower ... | component/input/data sensitivity | p. 9 (8.1. Comparisons with Other Teleoperation) |
| Although each skill policy solves its task continuously autonomously without stopping, we document the success rates of consecutive sub-tasks within each task for better ... | component/input/data sensitivity | p. 10 (9. Experiments on Imitation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data. | Our HIT achieves higher success rates than other baselines across all tasks. | PDF body cue; verify exact table/figure and matched conditions | p. 10 (9. Experiments on Imitation), p. 9 (Figure/Table caption), p. 9 (8.1. Comparisons with Other Teleoperation), p. 10 (9. Experiments on Imitation) |
| Primary metric/result | Table 5: Comparisons on Imitation. We show success rates of Humanoid Imitation Transformer (Ours), HIT with monocular input, ACT and open-loop trajectory replay across ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 9 / 8.1. Comparisons with Other Teleoperation - extractive body cue:** For ALOHA, we build a pair of bimanual arms for pupputeering from two WidowX 250 robots with similar kinematic structure as our humanoid arms.
- **p. 10 / 8.1. Comparisons with Other Teleoperation - extractive body cue:** Meta Quest often results in singularities and mismatches between target and actual poses in Cartesian space due to the limited 5 degrees of freedom of ...
- **p. 3 / 1. Introduction - extractive body cue:** Our HumanPlus robot has two egocentric RGB cameras mounted on the head, two 6-DoF dexterous hands, and 33 degrees of freedom in total. eras.
- **p. 4 / 3. HumanPlus Hardware - extractive body cue:** Our humanoid features 33 degrees of freedom, including two 6-DoF hands, two 1-DoF wrists, and a 19-DoF body (two 4-DoF arms, two 5-DoF legs, and ...
- **p. 4 / 3. HumanPlus Hardware - extractive body cue:** Our robot has two RGB webcams (Razer Kiyo Pro) mounted on its head, angled 50 degrees downward, with a pupillary distance of 160mm.
- **p. 4 / 4. Human Body and Hand Data - extractive body cue:** The AMASS dataset aggregates data from several human motion datasets, containing 40 hours of human motion data on a diverse ranges of tasks, and consisting ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, and enables more whole-body skills than ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Table 3: Teleop Comparisons & User Studies. We report averaged completion time for 6 participants on 2 tasks. target poses while saving energy and ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Throughout the development of our system, we encountered several limitations. | p. 10 (9. Experiments on Imitation) |
| body limitation/failure cue | It fails the Wear a Shoe and Walk task completely, where depth perception is crucial. | p. 10 (9. Experiments on Imitation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We record the average task completion time over six participants, with three trials each and three unrecorded practice rounds. | p. 9 (8.1. Comparisons with Other Teleoperation) |
| More recovery steps result in jittery behavior and compromise manipulation performance. | p. 10 (8.2. Robustness Evaluation) |
| Firstly, our hardware platform offers fewer degrees of freedom compared to human anatomy. | p. 10 (9. Experiments on Imitation) |
| This problem is further exacerbated by the lack of off-the-shelf and integrated hardware platforms. | p. 2 (1. Introduction) |
| Typically, learning-based low-level policies are designed to be task-specific due to time-consuming reward engineering [19, 68], enabling the humanoid hardware to demonstrate only one ... | p. 2 (1. Introduction) |
| FP FP 'R):ULVW 'R)+DQG 5*%&DPHUDV Figure 2: Hardware Details. | p. 3 (1. Introduction) |
| The body pose estimation and retargeting runs at 25 fps on an NVIDIA RTX4090 GPU. | p. 5 (4. Human Body and Hand Data) |
| To compute the 1-DoF wrist angle, we use the relative rotation between the forearm and hand global orientations. | p. 5 (4. Human Body and Hand Data) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, and enables more whole-body skills than the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Teleop Comparisons & User Studies. We report averaged completion time for 6 participants on 2 tasks. target poses while saving energy and avoiding ...
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** Throughout the development of our system, we encountered several limitations.
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** It fails the Wear a Shoe and Walk task completely, where depth perception is crucial.

- **Evidence anchors reviewed:** datasets p. 10 (9. Experiments on Imitation), p. 10 (8.1. Comparisons with Other Teleoperation), p. 9 (8.1. Comparisons with Other Teleoperation), p. 9 (8.1. Comparisons with Other Teleoperation), metrics p. 10 (8.1. Comparisons with Other Teleoperation), p. 9 (8.1. Comparisons with Other Teleoperation), p. 9 (8. Experiments on Shadowing), p. 10 (9. Experiments on Imitation), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 9 (8. Experiments on Shadowing), p. 9 (8.1. Comparisons with Other Teleoperation), p. 10 (9. Experiments on Imitation), p. 10 (9. Experiments on Imitation), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 10 (9. Experiments on Imitation), p. 9 (Figure/Table caption), p. 9 (8.1. Comparisons with Other Teleoperation), p. 10 (9. Experiments on Imitation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Shown in Table 5, we compare our imitation learning method Humanoid Imitation Transformer with three baseline methods: HIT policies with monocular inputs (Monocular), ACT [104], and Open-loop trajectory replay, across ... (p. 10, 9. Experiments on Imitation).
- **Metric evidence:** In contrast, our system has the lowest timeto-completion, has the highest success rate of stable standing, and is the only method that can be used for whole-body teleoperation, solving the ... (p. 10, 8.1. Comparisons with Other Teleoperation).
- **Baseline/ablation evidence:** Overall HIT (Ours) outperforms others. (p. 9, 8. Experiments on Shadowing).
- **Failure/negative evidence:** It fails the Wear a Shoe and Walk task completely, where depth perception is crucial. (p. 10, 9. Experiments on Imitation).
