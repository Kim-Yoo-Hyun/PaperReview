# Evaluation - RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p152.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p152.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (Figure/Table caption), p. 15 (Figure/Table caption), p. 7 (A. Quantitative Analysis), p. 9 (B. Qualitative Analysis), p. 9 (B. Qualitative Analysis), p. 14 (Figure/Table caption)): Fig. 12: Success rates of ACT, Diffusion Policy, and BAKU on RoboMIND.

## Evaluation Body Digest

- **p. 7 / A. Quantitative Analysis - extractive body cue:** In addition to the diversity across robot, the varied task horizons in the dataset directly impact the temporal generalization capabilities of policies in real-world scenarios.
- **p. 8 / B. Qualitative Analysis - extractive body cue:** RoboMIND features standardized settings to form a large-scale real-world manipulation dataset. ‘As shown in Figure 8, we compare our dataset with Open XEmbodiment, another large-scale ...
- **p. 7 / A. Quantitative Analysis - extractive body cue:** A manipulation dataset with different robotic embodiment types improves generalization to various actions and joint DoFs in downstream tasks.
- **p. 8 / A. Quantitative Analysis - extractive body cue:** This wide variety of objects increases the dataset's complexity and supports better generalization to unseen objects in downstream tasks.
- **p. 10 / A. Experiment Setup - extractive body cue:** The dataset features tasks performed by four
- **p. 10 / A. Experiment Setup - extractive body cue:** 11: Diverse task examples across 4 robotic embodiments in RoboMIND.
- **p. 9 / A. Experiment Setup - extractive body cue:** The robotic platforms used in this study are equipped as follows: (1) Franka Emika Panda [34]
- **p. 9 / B. Qualitative Analysis - extractive body cue:** stances where robots encountered failures during the execution of operational tasks.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** A. Experiment Setup (p. 9).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Fig. 12: Success rates of ACT, Diffusion Policy, and BAKU on RoboMIND. | p. 11 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Fig. 17: Success rates of models trained with different ratios of real-world and simulation data, | p. 15 (Figure/Table caption) |
| A. Quantitative Analysis | BENCHMARK / DATASET | A manipulation dataset with different robotic embodiment types improves generalization to various actions and joint DoFs in downstream tasks. | p. 7 (A. Quantitative Analysis) |
| B. Qualitative Analysis | BENCHMARK / DATASET | For the FR-PlacePlateInPlateRack task performed by Franka, a successful execution shows the robotic arm accurately placing a plate into the plate rack. | p. 9 (B. Qualitative Analysis) |
| B. Qualitative Analysis | BENCHMARK / DATASET | For the AX-PutCazrot task performed by AgileX, successful execution demonstrates the robot's collaborative manipulation to place a carrot onto the plate, In the failure ... | p. 9 (B. Qualitative Analysis) |

## Dataset / Benchmark Role

- **p. 7 / A. Quantitative Analysis - extractive body cue:** In addition to the diversity across robot, the varied task horizons in the dataset directly impact the temporal generalization capabilities of policies in real-world scenarios.
- **p. 8 / B. Qualitative Analysis - extractive body cue:** RoboMIND features standardized settings to form a large-scale real-world manipulation dataset. ‘As shown in Figure 8, we compare our dataset with Open XEmbodiment, another large-scale ...
- **p. 7 / A. Quantitative Analysis - extractive body cue:** A manipulation dataset with different robotic embodiment types improves generalization to various actions and joint DoFs in downstream tasks.
- **p. 8 / A. Quantitative Analysis - extractive body cue:** This wide variety of objects increases the dataset's complexity and supports better generalization to unseen objects in downstream tasks.
- **p. 10 / A. Experiment Setup - extractive body cue:** The dataset features tasks performed by four
- **p. 10 / A. Experiment Setup - extractive body cue:** 11: Diverse task examples across 4 robotic embodiments in RoboMIND.
- **p. 9 / A. Experiment Setup - extractive body cue:** The robotic platforms used in this study are equipped as follows: (1) Franka Emika Panda [34]
- **p. 9 / B. Qualitative Analysis - extractive body cue:** stances where robots encountered failures during the execution of operational tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of RoboMIND. We introduce RoboMIND (Mult-cmbodiment Intelligence Normative Data for Robot Manipulation), comprising 107k demonstration trajectories across 479 diverse tasks involving 96 ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2: Visualization of teleoperation methods for different robots. (a) Us
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: The Tien Kung humanoid robot configura- tion
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: We define 8 quality assurance criteria in the data collection process. Touch Excess: Unnecessary contact with objects by the robotic arm; Movement not ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Example of language description annotation, The video of the robotic arm placing the apple in the drawer is divided into six segments using ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Analysis and visualization of skill distri different robotic embodiments
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Distribution of objects in RoboMIND, categorized as domestic, industrial, kitchen, office, and retail. The y-axis uses a logarithmic scale for counts above 500, ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Comparison between Open X-Embodiment and Robo- MIND. RoboMIND features heterogeneous embodiments with diverse tasks and skills while providing ease of use due to ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In addition to the diversity across robot, the varied task horizons in the dataset directly impact the temporal generalization capabilities of policies in real-world ... | embodiment, simulator version and control stack | p. 7 (A. Quantitative Analysis), p. 8 (B. Qualitative Analysis) |
| Task/environment | RoboMIND features standardized settings to form a large-scale real-world manipulation dataset. ‘As shown in Figure 8, we compare our dataset with Open XEmbodiment, another ... | reset, timeout, object/scene variation | p. 8 (B. Qualitative Analysis), p. 7 (A. Quantitative Analysis) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 4 (I. INTRODUCTION), p. 4 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 12: Success rates of ACT, Diffusion Policy, and BAKU on RoboMIND. | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Fig. 17: Success rates of models trained with different ratios of real-world and simulation data, | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| ‘The failure data is intended to advance research in areas ike lure detection and recovery, data augmentation, and reward generation for reinforcement leaming. | definition/direction/unit from same section | p. 9 (B. Qualitative Analysis) |
| For the FR-PlacePlateInPlateRack task performed by Franka, a successful execution shows the robotic arm accurately placing a plate into the plate rack. | definition/direction/unit from same section | p. 9 (B. Qualitative Analysis) |
| Fig. 1: Overview of RoboMIND. We introduce RoboMIND (Mult-cmbodiment Intelligence Normative Data for Robot Manipulation), comprising 107k demonstration trajectories across 479 diverse tasks involving ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 5: Example of language description annotation, The video of the robotic arm placing the apple in the drawer is divided into six segments ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 4: We define 8 quality assurance criteria in the data collection process. Touch Excess: Unnecessary contact with objects by the robotic arm; Movement ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| model's manipulation robustness in handling complex and long-horizon tasks. | definition/direction/unit from same section | p. 8 (A. Quantitative Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 8: Comparison between Open X-Embodiment and RoboMIND. | comparison identity and matched condition | p. 9 (B. Qualitative Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The heterogeneous set of embodiment data collected under a unified standard can provide pretraining data for policy models with different action spaces (65, 51], ... | component/input/data sensitivity | p. 7 (A. Quantitative Analysis) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| demonstrate that RoboMIND can be effectively utilized by various single-task imitation learning algorithms and suecessfully adapted t0 VLA large models. ‘The high-quality information provided ... | Fig. 12: Success rates of ACT, Diffusion Policy, and BAKU on RoboMIND. | PDF body cue; verify exact table/figure and matched conditions | p. 11 (Figure/Table caption), p. 15 (Figure/Table caption), p. 7 (A. Quantitative Analysis), p. 9 (B. Qualitative Analysis), p. 9 (B. Qualitative Analysis), p. 14 (Figure/Table caption) |
| Primary metric/result | Fig. 17: Success rates of models trained with different ratios of real-world and simulation data, | numeric claim only at cited anchor | p. 15 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 8 / A. Quantitative Analysis - extractive body cue:** RoboMIND includes over 96 object categories from five usage scenarios, as shown in Figure 1(d), covering most daily life settings: domestic, industrial, kitchen, office, and ...
- **p. 10 / A. Experiment Setup - extractive body cue:** features three Intel RealSense 435i cameras [44] (left, top, and right) with resolutions of 480 x 640, 720 x 1280, and 480 640 pixels, respectively, ...
- **p. 10 / A. Experiment Setup - extractive body cue:** (2) Tien Kung [12] utilizes two Inspire-Robots RHS6DFX dexterous hands and Orbbec Gemini 335 cameras [79] on the head and chest, both at 480 x ...
- **p. 10 / A. Experiment Setup - extractive body cue:** (3) AgileX Cobot Magic V2.0 [87] is fitted with two hand-eye Orbbec Astra ‘cameras [78] and one front-facing camera, all at 480 x 640 resolution, ...
- **p. 10 / B. Single-task Imitation Learning Models - extractive body cue:** We used a total of 45 tasks which were grouped based on the robots performing them.
- **p. 10 / B. Single-task Imitation Learning Models - extractive body cue:** Franka, Tien Kung, AgileX, and URSe carried out 15, 10, 15, and 5 tasks respectively.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In the failure ‘case, the arm fails to locate the correct slot position, causing the plate to slip out of the rack, likely due ... | p. 9 (B. Qualitative Analysis) |
| body limitation/failure cue | Fig. 9: Visualization of failed data collection cases. We present two examples of failure from Franka and AgileX. In the FR-PlacePlateInP lateRack task (the ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Fig. 4: We define 8 quality assurance criteria in the data collection process. Touch Excess: Unnecessary contact with objects by the robotic arm; Movement ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | We also release Sk trajectories of the robot task failure cases. | p. 8 (B. Qualitative Analysis) |
| body limitation/failure cue | The failure cases documented include scenarios where different types of humane operators filed to complete their assigned tasks, as well as in | p. 8 (B. Qualitative Analysis) |
| body limitation/failure cue | Each model was tested ten times, and the testers recorded the success or failure of each test and the reasons if there were any ... | p. 11 (B. Single-task Imitation Learning Models) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In contrast, tasks from Tien Kung and AgileX have longer trajectories (over 500 time steps), better suited for longhorizon task training and skill composition, ... | p. 7 (A. Quantitative Analysis) |
| We calculate the average task horizon (the number of time steps in one trajectory) for each embodiment, as shown in Figure 1(b). | p. 7 (A. Quantitative Analysis) |
| 7: Distribution of objects in RoboMIND, categorized as domestic, industrial, kitchen, office, and retail. | p. 8 (A. Quantitative Analysis) |
| RoboMIND includes over 96 object categories from five usage scenarios, as shown in Figure 1(d), covering most daily life settings: domestic, industrial, kitchen, office, ... | p. 8 (A. Quantitative Analysis) |
| For Diffusion Policy, we followed the implementation in DROID [50]. | p. 10 (B. Single-task Imitation Learning Models) |
| We tested ten trials for each experiment. | p. 12 (C. Vision-Language-Action Large Models) |
| Specifically, we took the official pre-trained VLA models and fine-tuned them on the multitask datasets for each type of robot, and evaluated their performance ... | p. 12 (C. Vision-Language-Action Large Models) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / B. Qualitative Analysis - extractive body cue:** In the failure ‘case, the arm fails to locate the correct slot position, causing the plate to slip out of the rack, likely due to ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Visualization of failed data collection cases. We present two examples of failure from Franka and AgileX. In the FR-PlacePlateInP lateRack task (the second ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: We define 8 quality assurance criteria in the data collection process. Touch Excess: Unnecessary contact with objects by the robotic arm; Movement not ...
- **p. 8 / B. Qualitative Analysis - extractive body cue:** We also release Sk trajectories of the robot task failure cases.
- **p. 8 / B. Qualitative Analysis - extractive body cue:** The failure cases documented include scenarios where different types of humane operators filed to complete their assigned tasks, as well as in
- **p. 11 / B. Single-task Imitation Learning Models - extractive body cue:** Each model was tested ten times, and the testers recorded the success or failure of each test and the reasons if there were any failures.

- **PDF anchors reviewed:** datasets p. 7 (A. Quantitative Analysis), p. 8 (B. Qualitative Analysis), p. 7 (A. Quantitative Analysis), p. 8 (A. Quantitative Analysis), p. 10 (A. Experiment Setup), p. 10 (A. Experiment Setup), metrics p. 11 (Figure/Table caption), p. 15 (Figure/Table caption), p. 9 (B. Qualitative Analysis), p. 9 (B. Qualitative Analysis), p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), baselines p. 9 (B. Qualitative Analysis), results p. 11 (Figure/Table caption), p. 15 (Figure/Table caption), p. 7 (A. Quantitative Analysis), p. 9 (B. Qualitative Analysis), p. 9 (B. Qualitative Analysis), p. 14 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
