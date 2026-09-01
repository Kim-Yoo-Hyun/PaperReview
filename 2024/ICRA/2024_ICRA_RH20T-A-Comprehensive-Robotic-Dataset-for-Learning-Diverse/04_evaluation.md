# Evaluation - RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.00595; PDF retrieval source: https://arxiv.org/pdf/2307.00595. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS)): Additionally, the inclusion of data from different tasks during pretraining further improves the overall success rate.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** It is evident that all the cameras are calibrated with respect to the robot's base frame, and all the recorded data are synchronized in the ...
- **p. 3 / III. RH20T DATASET - extractive PDF cue:** We introduce our robotic manipulation dataset, RobotHuman demonstration in 20TB (RH20T), to the community.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Additionally, the robot model is rendered in the scene based on the joint angles recorded in our dataset.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** With 40 robot demonstrations, the results of pretraining on our dataset outperform the counterpart trained with 75 demonstrations without pretraining.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** When training the network with 75 demonstrations, we observe that pretraining the model with selected data from our dataset, despite differences in camera viewpoints, robot ...
- **p. 3 / III. RH20T DATASET - extractive PDF cue:** Properties of RH20T RH20T is designed with the objective of enabling general robotic manipulation, which means that the robot can perform various skills based on ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We divide the task into 3 stages, namely whether the robot can reach the block, grasp it and place it on the weight, and measure ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Experimental Results We present the model's success rates under different training configurations in Tab.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** Dataset (p. 3); III. RH20T DATASET (p. 3); IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | BENCHMARK / DATASET | Additionally, the inclusion of data from different tasks during pretraining further improves the overall success rate. | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | BENCHMARK / DATASET | Experimental Results We present the model's success rates under different training configurations in Tab. | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | BENCHMARK / DATASET | We divide the task into 3 stages, namely whether the robot can reach the block, grasp it and place it on the weight, and ... | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | BENCHMARK / DATASET | This stage aims to refine the model's performance on the target task. | p. 5 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** It is evident that all the cameras are calibrated with respect to the robot's base frame, and all the recorded data are synchronized in the ...
- **p. 3 / III. RH20T DATASET - extractive PDF cue:** We introduce our robotic manipulation dataset, RobotHuman demonstration in 20TB (RH20T), to the community.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Additionally, the robot model is rendered in the scene based on the joint angles recorded in our dataset.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** With 40 robot demonstrations, the results of pretraining on our dataset outperform the counterpart trained with 75 demonstrations without pretraining.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** When training the network with 75 demonstrations, we observe that pretraining the model with selected data from our dataset, despite differences in camera viewpoints, robot ...
- **p. 3 / III. RH20T DATASET - extractive PDF cue:** Properties of RH20T RH20T is designed with the objective of enabling general robotic manipulation, which means that the robot can perform various skills based on ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Overview of our RH20T dataset. We adopt multiple robots and setup diverse environments for the data collection. The robot manipulation episodes include multi-modal ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 2: Statistics on the amount of robotic manipulation for different tasks. # of Robot Manipulations 25 50 100 125 150
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3: Statistics on the execution time of different robotic manip- ulations in our dataset. largest in our community at present. da) Data Hierarchy: Humans ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4: Example of data hierarchy: The leaf nodes in the hierarchy consist of human demonstrations (highlighted in green) and robot manipulations (highlighted in red, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 5: Illustration of our data collection platform high-quality of our dataset. The detailed data format and data access APIs are provided on our website.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 6: We display the point cloud generated by fusing the RGBD data from the multi-view cameras mounted in our data collection platform. The red ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 1: Task description for our dataset. "Src." denotes the source of the task. Note that the task IDs are not necessarily continuous. Task Task ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | It is evident that all the cameras are calibrated with respect to the robot's base frame, and all the recorded data are synchronized in ... | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 3 (III. RH20T DATASET) |
| Task/environment | We introduce our robotic manipulation dataset, RobotHuman demonstration in 20TB (RH20T), to the community. | reset, timeout, object/scene variation | p. 3 (III. RH20T DATASET), p. 5 (IV. EXPERIMENTS) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 3 (III. RH20T DATASET), p. 1 (Abstract) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 3 (III. RH20T DATASET) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We divide the task into 3 stages, namely whether the robot can reach the block, grasp it and place it on the weight, and ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Experimental Results We present the model's success rates under different training configurations in Tab. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Additionally, the inclusion of data from different tasks during pretraining further improves the overall success rate. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| This stage aims to refine the model's performance on the target task. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 1: Overview of our RH20T dataset. We adopt multiple robots and setup diverse environments for the data collection. The robot manipulation episodes include ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Fig. 3: Statistics on the execution time of different robotic manip- ulations in our dataset. largest in our community at present. da) Data Hierarchy: ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| With 40 robot demonstrations, the results of pretraining on our dataset outperform the counterpart trained with 75 demonstrations without pretraining. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| The experimental results in Tab. demonstrate that the model pretrained on our dataset consistently outperforms its counterpart without pretraining, indicating that our dataset enhances ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| To assess the efficacy of our dataset, we adopt the Action Chunking with Transformers (ACT) model as our baseline network. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| Consequently, this paper primarily focuses on demonstrating the dataset's effectiveness in enhancing the transferability of a baseline model within a few-shot learning framework. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| This comparison highlights the comprehensiveness of our dataset, which is the most extensive dataset for robotic manipulation to date. | comparison identity and matched condition | p. 3 (Dataset) |
| []] provides a comparison between our dataset and previous representative publicly available datasets. a) Diversity: The diversity of RH20T encompasses multiple aspects. | comparison identity and matched condition | p. 3 (III. RH20T DATASET) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| With 40 robot demonstrations, the results of pretraining on our dataset outperform the counterpart trained with 75 demonstrations without pretraining. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| Comparing the results of training for 500 epochs with pretraining to training for 750 epochs without pretraining, we find that pretraining on our dataset ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| We evaluate the performance of the ACT model both with and without pre-training on our dataset. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Following pre-training, we fine-tune the ACT model on specific portions of the newly collected data, focusing on the task involving grasping and weight placement. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| To enhance environment diversity, we frequently replaced over 50 table covers with different textures and materials, and introduced irrelevant objects to create distractions. | component/input/data sensitivity | p. 3 (III. RH20T DATASET) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce our robotic manipulation dataset, RobotHuman demonstration in 20TB (RH20T), to the community. | Additionally, the inclusion of data from different tasks during pretraining further improves the overall success rate. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Primary metric/result | Experimental Results We present the model's success rates under different training configurations in Tab. | numeric claim only at cited anchor | p. 6 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 3 / Dataset - extractive PDF cue:** Force Sensing 8.30k 12 1 v RoboTurk 28 2.10k 2 1 X RoboNet 162k N/A 7 x BridgeData Il 7.20k 4 1 x BC-Z 26.0k ...
- **p. 3 / III. RH20T DATASET - extractive PDF cue:** To ensure task diversity, we selected 48 tasks from RLBench [19], 29 tasks from MetaWorld [EO], and introduced 70 self-proposed tasks that are frequently encountered ...
- **p. 3 / III. RH20T DATASET - extractive PDF cue:** In total, it contains 147 tasks, consisting of 42 skills (i.e., verbs).
- **p. 3 / III. RH20T DATASET - extractive PDF cue:** To ensure applicability across different robot configurations, we used 4 popular robot arms, 4 different robotic grippers, and 3 types of force-torque sensors, resulting in ...
- **p. 3 / III. RH20T DATASET - extractive PDF cue:** [TM1 c) Scale: Our dataset consists of over 110,000 robot sequences and an equal number of human sequences, with more than 50 million images collected ...
- **p. 3 / III. RH20T DATASET - extractive PDF cue:** On average, each skill contains approximately 750 robot manipulations.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The current limitations of this paper are that (i) the cost of data collection is expensive and (ii) the potential of robotic foundation models ... | p. 6 (V. DISCUSSION AND CONCLUSION) |
| body limitation/failure cue | These results demonstrate that leveraging the diverse training data from our dataset enhances the adaptability and robustness of the robotic manipulation model. | p. 6 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| During pre-training phase, the model is trained with a learning rate of 2 x 10-5 for 10 epochs; while during fine-tuning phase, the model ... | p. 5 (IV. EXPERIMENTS) |
| Epochs Reach Pick Place 500 35 10 0 v 500 70 15 15 v 500 65 20 15 75 730 55 5 0 v ... | p. 6 (IV. EXPERIMENTS) |
| Although it is less than the original implementation [#3], we increase the sample density per epoch by including all valid subtrajectories of the newly ... | p. 5 (IV. EXPERIMENTS) |
| 750 epochs are sufficient for the model to converge well. | p. 6 (IV. EXPERIMENTS) |
| We make our tele-operation pretty intuitive and the average training time is less than 1 hour. | p. 4 (200 Hz) |
| Robot Gripper 6DoF F/T Sensor Tactile Cfg 1 Flexiv Dahuan AG95 OptoForce N/A Cfg 2 Flexiv Dahuan AG95 ATI Axia80-M20 N/A URS ATI Axia80-M20 ... | p. 3 (III. RH20T DATASET) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / V. DISCUSSION AND CONCLUSION - extractive PDF cue:** The current limitations of this paper are that (i) the cost of data collection is expensive and (ii) the potential of robotic foundation models is ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** These results demonstrate that leveraging the diverse training data from our dataset enhances the adaptability and robustness of the robotic manipulation model.

- **PDF anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 3 (III. RH20T DATASET), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 3 (III. RH20T DATASET), metrics p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 3 (Dataset), p. 3 (III. RH20T DATASET), results p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
