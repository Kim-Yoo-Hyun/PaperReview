# Evaluation - BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ffBF6hYuQv; PDF retrieval source: https://arxiv.org/pdf/2506.07961.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments)): BridgeVLA outperforms all the comparing baseline methods in terms of average success rate, significantly outperforming the best baseline method by 7.3%.

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive body cue:** Both visual encoders show strong adaptability on various robotics tasks in both simulation and the real world.
- **p. 7 / 4 Experiments - extractive body cue:** RLBench [17] implements tasks in CoppeliaSim [44] using a Franka Panda robot mounted with a parallel-jaw gripper.
- **p. 7 / 4 Experiments - extractive body cue:** The model is trained on the data from the original RLBench benchmark but evaluated in environments spanning 12 axes of perturbations.
- **p. 8 / 4 Experiments - extractive body cue:** GemBench [19] is a hierarchical generalization benchmark built on the RLBench simulator [17].
- **p. 6 / 4 Experiments - extractive body cue:** Through the experiments, we aim to answer five questions: Q1: How effectively does BridgeVLA learn 3D robot manipulation compared to state-of-the-art methods when sufficient data ...
- **p. 6 / 4 Experiments - extractive body cue:** In this section, we perform extensive experiments in both simulation and the real world to evaluate the proposed method.
- **p. 7 / 4 Experiments - extractive body cue:** Models are evaluated via binary success rates over 25 trials per task, with a maximum of 25 action steps per trial.
- **p. 7 / 4 Experiments - extractive body cue:** The high success rates of our method showcase its strong capabilities of learning precise manipulation which is highly desirable in many industrial applications.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 6); B Simulation Experiments (p. 16); B.3 Detailed Results on COLOSSEUM (p. 17); B.4 Detailed Results on GemBench (p. 17); C Real-Robot Experiments (p. 17); C.1 Experiment Setup (p. 17).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SIMULATION | BridgeVLA outperforms all the comparing baseline methods in terms of average success rate, significantly outperforming the best baseline method by 7.3%. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SIMULATION | BridgeVLA outperforms all the comparing baseline methods, achieving an average success rate of 88.2% and an average rank of 1.9 across all the 18 ... | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SIMULATION | Compared to the state-of-the-art baseline, BridgeVLA improves the average success rate by 7.3%. perturbation, 3) compute the average success rate of all evaluated tasks ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SIMULATION | Models are evaluated via binary success rates over 25 trials per task, with a maximum of 25 action steps per trial. | p. 7 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive body cue:** Both visual encoders show strong adaptability on various robotics tasks in both simulation and the real world.
- **p. 7 / 4 Experiments - extractive body cue:** RLBench [17] implements tasks in CoppeliaSim [44] using a Franka Panda robot mounted with a parallel-jaw gripper.
- **p. 7 / 4 Experiments - extractive body cue:** The model is trained on the data from the original RLBench benchmark but evaluated in environments spanning 12 axes of perturbations.
- **p. 8 / 4 Experiments - extractive body cue:** GemBench [19] is a hierarchical generalization benchmark built on the RLBench simulator [17].
- **p. 6 / 4 Experiments - extractive body cue:** Through the experiments, we aim to answer five questions: Q1: How effectively does BridgeVLA learn 3D robot manipulation compared to state-of-the-art methods when sufficient data ...
- **p. 6 / 4 Experiments - extractive body cue:** In this section, we perform extensive experiments in both simulation and the real world to evaluate the proposed method.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. BridgeVLA outperforms all the comparing baseline methods, achieving an average success rate of 88.2% and an average rank of 1.9 across all the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Both visual encoders show strong adaptability on various robotics tasks in both simulation and the real world. | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | RLBench [17] implements tasks in CoppeliaSim [44] using a Franka Panda robot mounted with a parallel-jaw gripper. | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 12 (Method), p. 2 (1 Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1 Introduction), p. 10 (Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Models are evaluated via binary success rates over 25 trials per task, with a maximum of 25 action steps per trial. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| The high success rates of our method showcase its strong capabilities of learning precise manipulation which is highly desirable in many industrial applications. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Overall Success Rate (%) Models Avg. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| The table shows the success rates across 14 generalization settings. | definition/direction/unit from same section | p. 8 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to the state-of-the-art baseline, BridgeVLA improves the average success rate by 7.3%. perturbation, 3) compute the average success rate of all evaluated tasks ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| Through the experiments, we aim to answer five questions: Q1: How effectively does BridgeVLA learn 3D robot manipulation compared to state-of-the-art methods when sufficient ... | comparison identity and matched condition | p. 6 (4 Experiments) |
| We highlight that BridgeVLA outperforms the best baseline method by a large margin in Insert Peg (88.0% vs 40.0%) and Sort Shape (60.8% vs ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| BridgeVLA outperforms all the comparing baseline methods, achieving an average success rate of 88.2% and an average rank of 1.9 across all the 18 ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| BridgeVLA outperforms all the comparing baseline methods in terms of average success rate, significantly outperforming the best baseline method by 7.3%. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Q2: Does BridgeVLA learn more efficiently than existing state-of-the-art methods when data is limited (e.g., 3 trajectories per task)? | comparison identity and matched condition | p. 6 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Specifically, our evaluation includes three steps: 1) train the model with the original RLBench data without perturbations (100 trajectories per task) on 20 tasks, ... | component/input/data sensitivity | p. 7 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the contributions of this paper are threefold: • We introduce BridgeVLA, a novel 3D VLA model that efficiently and effectively learns 3D ... | BridgeVLA outperforms all the comparing baseline methods in terms of average success rate, significantly outperforming the best baseline method by 7.3%. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Primary metric/result | BridgeVLA outperforms all the comparing baseline methods, achieving an average success rate of 88.2% and an average rank of 1.9 across all the 18 ... | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiments - extractive body cue:** Q2: Does BridgeVLA learn more efficiently than existing state-of-the-art methods when data is limited (e.g., 3 trajectories per task)?
- **p. 7 / 4 Experiments - extractive body cue:** Following previous works [10-14], we perform experiments on 18 tasks from RLBench.
- **p. 7 / 4 Experiments - extractive body cue:** Models are evaluated via binary success rates over 25 trials per task, with a maximum of 25 action steps per trial.
- **p. 7 / 4 Experiments - extractive body cue:** BridgeVLA outperforms all the comparing baseline methods, achieving an average success rate of 88.2% and an average rank of 1.9 across all the 18 tasks, ...
- **p. 7 / 4 Experiments - extractive body cue:** Among the 18 tasks, BridgeVLA performs the worst in Place Cups, despite surpassing all the comparing baseline methods.
- **p. 7 / 4 Experiments - extractive body cue:** Specifically, our evaluation includes three steps: 1) train the model with the original RLBench data without perturbations (100 trajectories per task) on 20 tasks, 2) ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | A common failure mode is that the robot often ignores the target object and moves directly to the 10 | p. 10 (Method) |
| body limitation/failure cue | As we can see, most methods completely fails when given only 10 trajectories per task except two 3D related methods: RVT-2 and BridgeVLA. | p. 10 (Method) |
| body limitation/failure cue | Q3: How robust is BridgeVLA in handling visual disturbances (e.g., distractors, background, and lighting)? | p. 6 (4 Experiments) |
| body limitation/failure cue | 5 Conclusions & Future Work This paper has introduced BridgeVLA, a novel and efficient 3D vision-language-action (VLA) model built on top of a pre-trained ... | p. 12 (Method) |
| body limitation/failure cue | These results address Q3, showcasing that BridgeVLA possesses strong robustness against visual perturbation. | p. 8 (4 Experiments) |
| body limitation/failure cue | Distractor, Lighting, Background, and Height aim to evaluate the robustness 9 | p. 9 (Method) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The ablated model was also harder to train and more sensitive to hyperparameters-requiring a batch size of 192 and careful learning rate tuning-while our ... | p. 11 (Method) |
| Models are evaluated via binary success rates over 25 trials per task, with a maximum of 25 action steps per trial. | p. 7 (4 Experiments) |
| Specifically, our evaluation includes three steps: 1) train the model with the original RLBench data without perturbations (100 trajectories per task) on 20 tasks, ... | p. 7 (4 Experiments) |
| Both visual encoders show strong adaptability on various robotics tasks in both simulation and the real world. | p. 8 (4 Experiments) |
| R3M-MLP and MVP-MLP are two 2D methods that utilize pre-trained visual encoders to process observation images and an MLP for action prediction. | p. 8 (4 Experiments) |
| For every task, we evaluated every baseline over 10 trials to ensure statistical robustness. | p. 10 (Method) |
| 3) ACT [24]: A state-of-the-art 2D non-VLA model using a Conditional Variational Autoencoder (CVAE) to model action distributions. | p. 10 (Method) |
| We performed a hyperparameter grid search and evaluated the model on RLBench. | p. 11 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / Method - extractive body cue:** A common failure mode is that the robot often ignores the target object and moves directly to the 10
- **p. 10 / Method - extractive body cue:** As we can see, most methods completely fails when given only 10 trajectories per task except two 3D related methods: RVT-2 and BridgeVLA.
- **p. 6 / 4 Experiments - extractive body cue:** Q3: How robust is BridgeVLA in handling visual disturbances (e.g., distractors, background, and lighting)?
- **p. 12 / Method - extractive body cue:** 5 Conclusions & Future Work This paper has introduced BridgeVLA, a novel and efficient 3D vision-language-action (VLA) model built on top of a pre-trained vision-language ...
- **p. 8 / 4 Experiments - extractive body cue:** These results address Q3, showcasing that BridgeVLA possesses strong robustness against visual perturbation.
- **p. 9 / Method - extractive body cue:** Distractor, Lighting, Background, and Height aim to evaluate the robustness 9

- **Evidence anchors reviewed:** datasets p. 8 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), metrics p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), baselines p. 8 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), results p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
