# Evaluation - Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.11989; PDF retrieval source: https://arxiv.org/pdf/2410.11989. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS)): This makes it highly likely for the robot to navigate near the target, resulting in a significantly higher success rate compared to "Appearance" and "Positional Shift" (in 80 trials, it ...

## Evaluation Body Digest

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** 2) Environment and Task Setups: To verify our method's ability to enable robots to perform long-term tasks in dynamic environments, we designed an experiment in ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To evaluate the robot's ability to detect and adapt to environmental changes, we categorized the modifications to the objects in the second task into three ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** (3) In dynamic environments, DovSG significantly outperforms Ok-Robot (which assumes a static scene) in long-term tasks, thanks to its ability to adapt to scene changes.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** As a result, Ok-Robot's success rate for long-term tasks in dynamic environments is approximately 30% lower than DovSG.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** (3) Task Success Rate: This metric represents the overall task completion success rate.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** This results in a 10.7% higher pick-up success rate than Ok-Robot, which relies solely on AnyGrasp.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Two proposed grasp strategies in DovSG. In the first row, we cropped the point cloud input into anyGrasp within a certain range around ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** (2) How effectively does this facilitate the completion of consecutive tasks without manual resets?

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This makes it highly likely for the robot to navigate near the target, resulting in a significantly higher success rate compared to "Appearance" and ... | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Additionally, in "Appearance" and "Positional Shift" scenarios, DovSG achieves a scene change recognition success rate approximately 28% higher than the GPT-4o. | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In this section, We evaluate DovSG's performance in dynamic, real-world environments to answer two key questions: (1) How well does our system adapt to ... | p. 6 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** 2) Environment and Task Setups: To verify our method's ability to enable robots to perform long-term tasks in dynamic environments, we designed an experiment in ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To evaluate the robot's ability to detect and adapt to environmental changes, we categorized the modifications to the objects in the second task into three ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** (3) In dynamic environments, DovSG significantly outperforms Ok-Robot (which assumes a static scene) in long-term tasks, thanks to its ability to adapt to scene changes.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** As a result, Ok-Robot's success rate for long-term tasks in dynamic environments is approximately 30% lower than DovSG.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Overview of Our DovSG System. DovSG is a mobile robotic system designed to perform long-term tasks in real-world environments. It can detect changes ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. To address the challenge of scene perception, our per- ception module integrates advanced tools such as Recognize- Anything [6], Grounding DINO [7], Segment ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2. Initialization and Construction of 3D Scene Graphs. We first use the RGB-D-based DROID-SLAM [31] model to predict the pose of each frame in ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. Adaptation in interactions with manually modified scenes. (1) We train the scene-specific regression MLP of the ACE model using RGB images and their ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Two proposed grasp strategies in DovSG. In the first row, we cropped the point cloud input into anyGrasp within a certain range around ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. This heuristic strategy is only activated when AnyGrasp can't provide a suitable grasp, ensuring optimal interaction with the object's geometry 2) Place: We ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. Degrees of environmental modifications. The left column shows the initial state of the scene, while the two columns on the right represent the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 2) Environment and Task Setups: To verify our method's ability to enable robots to perform long-term tasks in dynamic environments, we designed an experiment ... | embodiment, simulator version and control stack | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Task/environment | To evaluate the robot's ability to detect and adapt to environmental changes, we categorized the modifications to the objects in the second task into ... | reset, timeout, object/scene variation | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 5 (III. METHOD), p. 4 (III. METHOD) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 5 (III. METHOD), p. 3 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| (3) Task Success Rate: This metric represents the overall task completion success rate. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| This results in a 10.7% higher pick-up success rate than Ok-Robot, which relies solely on AnyGrasp. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Fig. 4. Two proposed grasp strategies in DovSG. In the first row, we cropped the point cloud input into anyGrasp within a certain range ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| (2) How effectively does this facilitate the completion of consecutive tasks without manual resets? | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Fig. 1. To address the challenge of scene perception, our per- ception module integrates advanced tools such as Recognize- Anything [6], Grounding DINO [7], ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Fig. 2. Initialization and Construction of 3D Scene Graphs. We first use the RGB-D-based DROID-SLAM [31] model to predict the pose of each frame ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 3. Adaptation in interactions with manually modified scenes. (1) We train the scene-specific regression MLP of the ACE model using RGB images and ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In contrast, DovSG, supported by precise relocalization, can accurately identify the voxel index where changes have occurred in the scene, significantly outperforming the baseline. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| Our evaluation focuses on three key aspects: Dynamic Scene Adaptation and Scene Graph Generation: We recorded RGB observations during the robot's task execution and ... | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| 3) Baselines: To demonstrate our approach's adaptability to changing environments and the effectiveness of scene graph prediction, we evaluated scene changes and scene graph ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| (2) How effectively does this facilitate the completion of consecutive tasks without manual resets? | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| (2) How effectively does this facilitate the completion of consecutive tasks without manual resets? | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately ... | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |
| This detailed evaluation provides a comprehensive analysis of the effectiveness of our method across different components of task execution. | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |
| Fig. 4. Two proposed grasp strategies in DovSG. In the first row, we cropped the point cloud input into anyGrasp within a certain range ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Fig. 1. Overview of Our DovSG System. DovSG is a mobile robotic system designed to perform long-term tasks in real-world environments. It can detect ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Fig. 1. To address the challenge of scene perception, our per- ception module integrates advanced tools such as Recognize- Anything [6], Grounding DINO [7], ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling ... | This makes it highly likely for the robot to navigate near the target, resulting in a significantly higher success rate compared to "Appearance" and ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Primary metric/result | Additionally, in "Appearance" and "Positional Shift" scenarios, DovSG achieves a scene change recognition success rate approximately 28% higher than the GPT-4o. | numeric claim only at cited anchor | p. 7 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Overall, for each method, each level of modification was tested through 20 long-term tasks per room across 4 rooms, resulting in a total of 80 ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** This makes it highly likely for the robot to navigate near the target, resulting in a significantly higher success rate compared to "Appearance" and "Positional ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In contrast, for "Appearance", where a new object emerges, the robot does not face the challenge of misjudging the original object's position, generally leading to ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately ... | p. 7 (IV. EXPERIMENTS) |
| body limitation/failure cue | 2) Mobile control: Once the target location is determined, we use the A* [34] algorithm to generate a collision-free navigation path from the start ... | p. 5 (III. METHOD) |
| body limitation/failure cue | A buffer of 0.1 is added to account for potential collisions. | p. 6 (III. METHOD) |
| body limitation/failure cue | In the first row, we cropped the point cloud input into anyGrasp within a certain range around the target object, allowing anyGrasp to focus ... | p. 6 (III. METHOD) |
| body limitation/failure cue | Although Ok-Robot can occasionally succeed in locating the correct object under minor changes (e.g., "Minor Adjustment"), it struggles with larger modifications such as "Appearance" ... | p. 7 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| With three modification levels, each method was subjected to 240 long-term task experiments, in which objects or their positions were randomized in every trial. | p. 6 (IV. EXPERIMENTS) |
| Overall, for each method, each level of modification was tested through 20 long-term tasks per room across 4 rooms, resulting in a total of ... | p. 6 (IV. EXPERIMENTS) |
| This makes it highly likely for the robot to navigate near the target, resulting in a significantly higher success rate compared to "Appearance" and ... | p. 7 (IV. EXPERIMENTS) |
| In contrast, for "Appearance", where a new object emerges, the robot does not face the challenge of misjudging the original object's position, generally leading ... | p. 7 (IV. EXPERIMENTS) |
| To align the scene relative to the detected floor, we applied RANSAC to fit a plane to the 3D floor points and computed a ... | p. 3 (III. METHOD) |
| Leveraging the transformation of the scene's coordinate system from the previous steps-where the ground plane serves as the origin and the z-axis points upwards-we ... | p. 3 (III. METHOD) |
| (3) For each valid projected point i, we compute the depth and color difference: ∆zi = | p. 5 (III. METHOD) |
| (4) For each object in Oneed_process, we recompute the spatial relationships as described in Sec. | p. 5 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately causing ...
- **p. 5 / III. METHOD - extractive body cue:** 2) Mobile control: Once the target location is determined, we use the A* [34] algorithm to generate a collision-free navigation path from the start point ...
- **p. 6 / III. METHOD - extractive body cue:** A buffer of 0.1 is added to account for potential collisions.
- **p. 6 / III. METHOD - extractive body cue:** In the first row, we cropped the point cloud input into anyGrasp within a certain range around the target object, allowing anyGrasp to focus more ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Although Ok-Robot can occasionally succeed in locating the correct object under minor changes (e.g., "Minor Adjustment"), it struggles with larger modifications such as "Appearance" or ...

- **PDF anchors reviewed:** datasets p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), metrics p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (Figure/Table caption), p. 6 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), results p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
