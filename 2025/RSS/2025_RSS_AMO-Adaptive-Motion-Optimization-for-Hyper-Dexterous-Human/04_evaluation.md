# Evaluation - AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p061.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p061.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EVALUATION), p. 8 (IV. EVALUATION), p. 7 (IV. EVALUATION), p. 8 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 7 (IV. EVALUATION)): cate that AMO achieves superior tracking accuracy in roll and pitch directions. ‘The most notable improvement isin pitch tracking, where other baselines struggle to maintain accuracy, whereas our model significantly ...

## Evaluation Body Digest

- **p. 7 / IV. EVALUATION - extractive body cue:** 6: Autonomous tasks performed in the real-world setting.
- **p. 7 / IV. EVALUATION - extractive body cue:** For each task, we collect 50 episodes using the teleoperation system and train an ACT to complete it autonomously.
- **p. 8 / IV. EVALUATION - extractive body cue:** As shown in Fig.7, the task begins with the robot crouching and bending, forward to align its hands with the baskets' height.
- **p. 8 / IV. EVALUATION - extractive body cue:** In this task, the robot must crouch to a considerably low height and adjust its torso orientation to grasp two baskets positioned on either side, ...
- **p. 5 / IV. EVALUATION - extractive body cue:** Our real robot setup is as shown in 3, which is modified from Unitree G1_ [1] with two Dex3-1 dexterous hands.
- **p. 6 / IV. EVALUATION - extractive body cue:** + Ww rand arms: In this baseline, arm joint angles are not set using human references sampled from a MoCap dataset.
- **p. 6 / IV. EVALUATION - extractive body cue:** + ExBody2: [33] is a representative work in leveraging human reference motions to guide robot whole-body control in RL.
- **p. 5 / IV. EVALUATION - extractive body cue:** We conduct our sim experiments in IssacGym simulator 4].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** IV. EVALUATION (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | cate that AMO achieves superior tracking accuracy in roll and pitch directions. ‘The most notable improvement isin pitch tracking, where other baselines struggle to ... | p. 6 (IV. EVALUATION) |
| IV. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | With the most complete setting, the policy achieves a near-perfect success rate. | p. 8 (IV. EVALUATION) |
| IV. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, AMO achieves a significantly larger range of torso motion compared to other baselines, particularly in torso pitch, where it allows the robot ... | p. 7 (IV. EVALUATION) |
| IV. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | While using only a single image slightly reduces the success rate, this task is particularly susceptible to shorter chunk sizes. | p. 8 (IV. EVALUATION) |
| IV. EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | achieves the lowest height tracking eror. | p. 6 (IV. EVALUATION) |

## Dataset / Benchmark Role

- **p. 7 / IV. EVALUATION - extractive body cue:** 6: Autonomous tasks performed in the real-world setting.
- **p. 7 / IV. EVALUATION - extractive body cue:** For each task, we collect 50 episodes using the teleoperation system and train an ACT to complete it autonomously.
- **p. 8 / IV. EVALUATION - extractive body cue:** As shown in Fig.7, the task begins with the robot crouching and bending, forward to align its hands with the baskets' height.
- **p. 8 / IV. EVALUATION - extractive body cue:** In this task, the robot must crouch to a considerably low height and adjust its torso orientation to grasp two baskets positioned on either side, ...
- **p. 5 / IV. EVALUATION - extractive body cue:** Our real robot setup is as shown in 3, which is modified from Unitree G1_ [1] with two Dex3-1 dexterous hands.
- **p. 6 / IV. EVALUATION - extractive body cue:** + Ww rand arms: In this baseline, arm joint angles are not set using human references sampled from a MoCap dataset.
- **p. 6 / IV. EVALUATION - extractive body cue:** + ExBody2: [33] is a representative work in leveraging human reference motions to guide robot whole-body control in RL.
- **p. 5 / IV. EVALUATION - extractive body cue:** We conduct our sim experiments in IssacGym simulator 4].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: AMO enables hyper-dexterous whole-body movements for humanoid robots. (a):
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Teleoperation system overview. The operator provides three end-effector targets: head, left wrist, and right wrist poses. A multi-target IK computes upper goals and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Evaluation of in-distribution (LD.) and out-of distribution (0,0.D.) tracking results. Each figure shows the target vs. the actual commanded direction. The white area ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Autonomous tasks performed in the real-world setting. For each task, we collect 50 episodes using the teleoperation system and train an ACT to ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Basket Picking: A complicated loco-manipulation task that also requires whole-body coordination. ‘The task begins with the robot picking two baskets from left(1) and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 6: Autonomous tasks performed in the real-world setting. | embodiment, simulator version and control stack | p. 7 (IV. EVALUATION), p. 7 (IV. EVALUATION) |
| Task/environment | For each task, we collect 50 episodes using the teleoperation system and train an ACT to complete it autonomously. | reset, timeout, object/scene variation | p. 7 (IV. EVALUATION), p. 8 (IV. EVALUATION) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 3 (A. Problem Formulation and Notations), p. 3 (A. Problem Formulation and Notations) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 4 (A. Problem Formulation and Notations), p. 5 (C. Lower Policy Training) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| With the most complete setting, the policy achieves a near-perfect success rate. | definition/direction/unit from same section | p. 8 (IV. EVALUATION) |
| While using only a single image slightly reduces the success rate, this task is particularly susceptible to shorter chunk sizes. | definition/direction/unit from same section | p. 8 (IV. EVALUATION) |
| cate that AMO achieves superior tracking accuracy in roll and pitch directions. ‘The most notable improvement isin pitch tracking, where other baselines struggle to ... | definition/direction/unit from same section | p. 6 (IV. EVALUATION) |
| Despite this limitation, AMO remains capable of performing stable locomotion with a low tracking error, demonstrating its robustness. | definition/direction/unit from same section | p. 6 (IV. EVALUATION) |
| AMO's advantage lies not only in accurately tracking indistribution (LD.) torso commands but also in its ability to effectively adapt to out-of-distribution (0.0.D.) commands, ... | definition/direction/unit from same section | p. 7 (IV. EVALUATION) |
| We customized an active head with three actuated DoFs to map the human operator's head movement and mounted a ZED Mini [2] camera for ... | definition/direction/unit from same section | p. 5 (IV. EVALUATION) |
| In this section, we aim to address the following questions by conducting experiments in both simulation and in the real world: ‘+ How well ... | definition/direction/unit from same section | p. 5 (IV. EVALUATION) |
| It successfully tracks torso yaw command | definition/direction/unit from same section | p. 7 (IV. EVALUATION) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In contrast, AMO achieves a significantly larger range of torso motion compared to other baselines, particularly in torso pitch, where it allows the robot ... | comparison identity and matched condition | p. 7 (IV. EVALUATION) |
| + wlo priv: This baseline is trained without additional privileged observations si. | comparison identity and matched condition | p. 6 (IV. EVALUATION) |
| baselines, indicating that it barely tracks height command, | comparison identity and matched condition | p. 6 (IV. EVALUATION) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| + wlo priv: This baseline is trained without additional privileged observations si. | component/input/data sensitivity | p. 6 (IV. EVALUATION) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Gisker is the reference lower body joint angles generated by the AMO module. ‘The lower action, Space Giower € IR! isa vector of dimension ... | cate that AMO achieves superior tracking accuracy in roll and pitch directions. ‘The most notable improvement isin pitch tracking, where other baselines struggle to ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EVALUATION), p. 8 (IV. EVALUATION), p. 7 (IV. EVALUATION), p. 8 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 7 (IV. EVALUATION) |
| Primary metric/result | With the most complete setting, the policy achieves a near-perfect success rate. | numeric claim only at cited anchor | p. 8 (IV. EVALUATION) |

- Numeric sentences retained from the body:
- **p. 6 / IV. EVALUATION - extractive body cue:** However, AMO is not necessarily expected to excel in yaw tracking, 4s torso yaw rotation induces minimal CoM displacement compared to roll and pitch.
- **p. 7 / IV. EVALUATION - extractive body cue:** The robot then tums its waist about 90 degrees to the right and throws the trash bottle into the trash bin,
- **p. 7 / IV. EVALUATION - extractive body cue:** For each task, we collect 50 episodes using the teleoperation system and train an ACT to complete it autonomously.
- **p. 5 / C. Lower Policy Training - extractive body cue:** Each tracking error is averaged over 4096 environments and 500 steps.
- **p. 5 / C. Lower Policy Training - extractive body cue:** We then employ ACT [78] with a DinoV2 {17, 53] visual encoder as the policy backbone. ‘The visual observation inchides two stereo images ing and ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | It is evident that w/o AMO struggles with 0.0.D. commands: it fails to track torso pitch and yaw commands before they reach the sampled ... | p. 7 (IV. EVALUATION) |
| body limitation/failure cue | Despite this limitation, AMO remains capable of performing stable locomotion with a low tracking error, demonstrating its robustness. | p. 6 (IV. EVALUATION) |
| body limitation/failure cue | ‘AMO, the policy fails to learn the transformation rlation | p. 6 (IV. EVALUATION) |
| body limitation/failure cue | ‘To further highlight the robustness and hyper-dexterity of, the AMO system, We select several challenging tasks that require adaptive whole-body control and perform imitation | p. 7 (IV. EVALUATION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Specifically, hhand movements are generated via retargeting, while other control signals are computed using inverse kinematies (IK), Our implementation of hand retargeting is based ... | p. 5 (C. Lower Policy Training) |
| A multi-target IK computes upper goals and intermediate goals by matching three weighted targets simultaneously. | p. 4 (B. Adaptation Module Pre-Training) |
| Teleoperation Upper Policy Implementation | p. 5 (C. Lower Policy Training) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / IV. EVALUATION - extractive body cue:** It is evident that w/o AMO struggles with 0.0.D. commands: it fails to track torso pitch and yaw commands before they reach the sampled training ...
- **p. 6 / IV. EVALUATION - extractive body cue:** Despite this limitation, AMO remains capable of performing stable locomotion with a low tracking error, demonstrating its robustness.
- **p. 6 / IV. EVALUATION - extractive body cue:** ‘AMO, the policy fails to learn the transformation rlation
- **p. 7 / IV. EVALUATION - extractive body cue:** ‘To further highlight the robustness and hyper-dexterity of, the AMO system, We select several challenging tasks that require adaptive whole-body control and perform imitation

- **Evidence anchors reviewed:** datasets p. 7 (IV. EVALUATION), p. 7 (IV. EVALUATION), p. 8 (IV. EVALUATION), p. 8 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), metrics p. 8 (IV. EVALUATION), p. 8 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 7 (IV. EVALUATION), p. 5 (IV. EVALUATION), baselines p. 7 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION), results p. 6 (IV. EVALUATION), p. 8 (IV. EVALUATION), p. 7 (IV. EVALUATION), p. 8 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 7 (IV. EVALUATION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** cate that AMO achieves superior tracking accuracy in roll and pitch directions. ‘The most notable improvement isin pitch tracking, where other baselines struggle to maintain accuracy, whereas our model significantly ... (p. 6, IV. EVALUATION).
- **Metric evidence:** Despite this limitation, AMO remains capable of performing stable locomotion with a low tracking error, demonstrating its robustness. (p. 6, IV. EVALUATION).
- **Baseline/ablation evidence:** + wlo priv: This baseline is trained without additional privileged observations si. (p. 6, IV. EVALUATION).
- **Failure/negative evidence:** It is evident that w/o AMO struggles with 0.0.D. commands: it fails to track torso pitch and yaw commands before they reach the sampled training ranges, and it does not ... (p. 7, IV. EVALUATION).
