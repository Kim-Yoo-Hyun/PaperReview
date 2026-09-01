# Evaluation - BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (39 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ffBF6hYuQv; PDF retrieval source: https://openreview.net/pdf/26f13e74e0fd6da3fdd307ba96da6dc4438d93a3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 24 (Figure/Table caption), p. 23 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption)): Table 5: Results on GemBench. We show the average success rates on the four evaluation settings of GemBench. BridgeVLA establishes a new state of the art on this benchmark, achieving ...

## Evaluation Body Digest

- **p. 9 / 1) The images in the pre-training dataset are - extractive PDF cue:** mostly captured from third-person views, which differ significantly from the projection images in our robot data; 2) The pre-training task focuses solely on object localization, ...
- **p. 6 / 4 Experiments - extractive PDF cue:** RLBench [19] implements tasks in CoppeliaSim [38] using a Franka Panda robot mounted with a parallel-jaw gripper.
- **p. 7 / 4 Experiments - extractive PDF cue:** The COLOSSEUM benchmark evaluates models in environments with 12 axes of perturbations, which were not seen during training.
- **p. 7 / 4 Experiments - extractive PDF cue:** These tasks ranges from simple pick-and-place to complex long-horizon tasks, requiring the robot to open a drawer and put items into the drawer.
- **p. 6 / 4 Experiments - extractive PDF cue:** Through the experiments, we aim to answer five questions: Q1: How effectively does BridgeVLA learn 3D robot manipulation compared to state-of-the-art methods when sufficient data ...
- **p. 9 / 1) The images in the pre-training dataset are - extractive PDF cue:** To address these issues, we plan to expand both the scale and diversity of the pre-training dataset and explore more expressive action-decoding methods to better ...
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** In the future, we plan to explore pre-training on more diverse tasks, including semantic segmentation and keypoint detection.
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** Extensive experiments show that the proposed method is able to learn 3D manipulation efficiently and effectively in both simulation and the real world.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 6); 1) The images in the pre-training dataset are (p. 9); B Simulation Experiments (p. 22); B.1 Experiments on COLOSSEUM (p. 22); B.2 Experiments on GemBench (p. 23); C Real-Robot Experiments (p. 24); C.1 Experiment Setup (p. 24).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 5: Results on GemBench. We show the average success rates on the four evaluation settings of GemBench. BridgeVLA establishes a new state of ... | p. 24 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 4: Results on the COLOSSEUM Benchmark. The table shows the success rates across 14 generalization settings. The "Avg. Rank" column reports the average ... | p. 23 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 2: Per-task Success Rate in the Basic Setting. Except for SpatialVLA(50), which was trained with 50 trajectories, all other methods were trained with ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 1: Results on RLBench. The "Avg. Rank" column reports the average rank of each method across all 18 tasks, where lower values indicate ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 3: Real-Robot Experiments and Results. We use a Franka Research 3 robot arm and a ZED 2i camera to capture point clouds of ... | p. 9 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 9 / 1) The images in the pre-training dataset are - extractive PDF cue:** mostly captured from third-person views, which differ significantly from the projection images in our robot data; 2) The pre-training task focuses solely on object localization, ...
- **p. 6 / 4 Experiments - extractive PDF cue:** RLBench [19] implements tasks in CoppeliaSim [38] using a Franka Panda robot mounted with a parallel-jaw gripper.
- **p. 7 / 4 Experiments - extractive PDF cue:** The COLOSSEUM benchmark evaluates models in environments with 12 axes of perturbations, which were not seen during training.
- **p. 7 / 4 Experiments - extractive PDF cue:** These tasks ranges from simple pick-and-place to complex long-horizon tasks, requiring the robot to open a drawer and put items into the drawer.
- **p. 6 / 4 Experiments - extractive PDF cue:** Through the experiments, we aim to answer five questions: Q1: How effectively does BridgeVLA learn 3D robot manipulation compared to state-of-the-art methods when sufficient data ...
- **p. 9 / 1) The images in the pre-training dataset are - extractive PDF cue:** To address these issues, we plan to expand both the scale and diversity of the pre-training dataset and explore more expressive action-decoding methods to better ...
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** In the future, we plan to explore pre-training on more diverse tasks, including semantic segmentation and keypoint detection.
- **p. 10 / 1) The images in the pre-training dataset are - extractive PDF cue:** Extensive experiments show that the proposed method is able to learn 3D manipulation efficiently and effectively in both simulation and the real world.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Overview. BridgeVLA is a novel 3D VLA model that aligns the input and output within a unified 2D image space. It is pre-trained ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Model Architecture. (a) 2D Heatmap Pre-training: we train BridgeVLA on 2D object detection datasets. The model takes as inputs an image and a ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Results on RLBench. The "Avg. Rank" column reports the average rank of each method across all 18 tasks, where lower values indicate better ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Per-task Success Rate in the Basic Setting. Except for SpatialVLA(50), which was trained with 50 trajectories, all other methods were trained with 10 ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 3: Real-Robot Experiments and Results. We use a Franka Research 3 robot arm and a ZED 2i camera to capture point clouds of the ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 4: Prediction on Pre-training Data after Fine-tuning. To simulate the multi-view inputs during fine-tuning, we repeat each pre-training im- age three times and feed ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 3. As we can see, BridgeVLA w/o Pre-train is not able to generalize well in both language-related generalization settings and can not even beat ...
- **p. 22 / Figure/Table caption - extractive PDF cue:** Table 3: Training hyperparameters for BridgeVLA Pretrain RLBench Finetune Colosseum Finetune Real-robot Finetune learning rate 5e-5 8e-5

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | mostly captured from third-person views, which differ significantly from the projection images in our robot data; 2) The pre-training task focuses solely on object ... | embodiment, simulator version and control stack | p. 9 (1) The images in the pre-training dataset are), p. 6 (4 Experiments) |
| Task/environment | RLBench [19] implements tasks in CoppeliaSim [38] using a Franka Panda robot mounted with a parallel-jaw gripper. | reset, timeout, object/scene variation | p. 6 (4 Experiments), p. 7 (4 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 10 (1) The images in the pre-training dataset are) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1 Introduction), p. 8 (Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 4: Results on the COLOSSEUM Benchmark. The table shows the success rates across 14 generalization settings. The "Avg. Rank" column reports the average ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Models are evaluated via binary success rates over 25 trials per task, with a maximum of 25 action steps per trial. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| The high success rates of our method showcase its strong capabilities of learning precise manipulation which is highly desirable in many industrial applications. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Table 2: Per-task Success Rate in the Basic Setting. Except for SpatialVLA(50), which was trained with 50 trajectories, all other methods were trained with ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 5: Results on GemBench. We show the average success rates on the four evaluation settings of GemBench. BridgeVLA establishes a new state of ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Table 7: Success Rates of RVT-2 under Different Perturbations of COLOSSEUM. 26 | definition/direction/unit from same section | p. 26 (Figure/Table caption) |
| Replacing heatmap prediction with direct position regression reduced the average success rate from 88.2% to 31.4%, confirming the effectiveness of our heatmap-based design. | definition/direction/unit from same section | p. 10 (1) The images in the pre-training dataset are) |
| Table 1: Results on RLBench. The "Avg. Rank" column reports the average rank of each method across all 18 tasks, where lower values indicate ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 3: Real-Robot Experiments and Results. We use a Franka Research 3 robot arm and a ZED 2i camera to capture point clouds of ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Table 5: Results on GemBench. We show the average success rates on the four evaluation settings of GemBench. BridgeVLA establishes a new state of ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |
| Through the experiments, we aim to answer five questions: Q1: How effectively does BridgeVLA learn 3D robot manipulation compared to state-of-the-art methods when sufficient ... | comparison identity and matched condition | p. 6 (4 Experiments) |
| BridgeVLA outperforms all existing state-of-the-art 3D manipulation methods on both benchmarks, addressing Q3 and Q4. | comparison identity and matched condition | p. 7 (4 Experiments) |
| We highlight that BridgeVLA outperforms the best baseline method by a large margin in Insert Peg (88.0% vs 40.0%) and Sort Shape (60.8% vs ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| Table 2: Per-task Success Rate in the Basic Setting. Except for SpatialVLA(50), which was trained with 50 trajectories, all other methods were trained with ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.3 Ablation Studies To prove the effectiveness of our model design and provide insights for the community, we conduct three ablation studies: Whether we ... | component/input/data sensitivity | p. 10 (1) The images in the pre-training dataset are) |
| Figure 2: Model Architecture. (a) 2D Heatmap Pre-training: we train BridgeVLA on 2D object detection datasets. The model takes as inputs an image and ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| This design preserves alignment between the input feature spaces of fine-tuning and VLM pretraining, which we find crucial for effective vision-language-action (VLA) modeling. | component/input/data sensitivity | p. 10 (1) The images in the pre-training dataset are) |
| Figure 1: Overview. BridgeVLA is a novel 3D VLA model that aligns the input and output within a unified 2D image space. It is ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Table 1: Results on RLBench. The "Avg. Rank" column reports the average rank of each method across all 18 tasks, where lower values indicate ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Figure 4: Prediction on Pre-training Data after Fine-tuning. To simulate the multi-view inputs during fine-tuning, we repeat each pre-training im- age three times and ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the contributions of this paper are threefold: • We introduce BridgeVLA, a novel 3D VLA model that efficiently and effectively learns 3D ... | Table 5: Results on GemBench. We show the average success rates on the four evaluation settings of GemBench. BridgeVLA establishes a new state of ... | PDF body cue; verify exact table/figure and matched conditions | p. 24 (Figure/Table caption), p. 23 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption) |
| Primary metric/result | Table 4: Results on the COLOSSEUM Benchmark. The table shows the success rates across 14 generalization settings. The "Avg. Rank" column reports the average ... | numeric claim only at cited anchor | p. 23 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiments - extractive PDF cue:** Q2: Does BridgeVLA learn more efficiently than existing state-of-the-art methods when data is limited (e.g., 3 trajectories per task)?
- **p. 6 / 4 Experiments - extractive PDF cue:** Following previous works [39, 13, 14, 25, 15], we perform experiments on 18 tasks from RLBench.
- **p. 7 / 4 Experiments - extractive PDF cue:** Models are evaluated via binary success rates over 25 trials per task, with a maximum of 25 action steps per trial.
- **p. 7 / 4 Experiments - extractive PDF cue:** BridgeVLA outperforms all the comparing baseline methods, achieving an average success rate of 88.2% and an average rank of 1.9 across all the 18 tasks, ...
- **p. 7 / 4 Experiments - extractive PDF cue:** Among the 18 tasks, BridgeVLA performs the worst in Place Cups, despite surpassing all the comparing baseline methods.
- **p. 7 / 4 Experiments - extractive PDF cue:** Its training set consists of 16 tasks (31 variations) covering seven core action primitives: press, pick, push, screw, close, open, and stack/put.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 1: Results on RLBench. The "Avg. Rank" column reports the average rank of each method across all 18 tasks, where lower values indicate ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | A common failure mode is that the robot often ignores the target object and moves directly to the destination during pick-and-place manipulation. | p. 9 (Method) |
| body limitation/failure cue | Figure 1: Overview. BridgeVLA is a novel 3D VLA model that aligns the input and output within a unified 2D image space. It is ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Due to space limitations, the details of the environment setup, baselines, and analysis can be found in Appendix B.1 and Appendix B.2. | p. 7 (4 Experiments) |
| body limitation/failure cue | As we can see, most methods completely fails when given only 10 trajectories per task except two 3D related methods: RVT-2 and BridgeVLA. | p. 8 (Method) |
| body limitation/failure cue | Q3: How robust is BridgeVLA in handling visual disturbances (e.g., distractors, background, and lighting)? | p. 6 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The ablated model was also harder to train and more sensitive to hyperparameters-requiring a batch size of 192 and careful learning rate tuning-while our ... | p. 10 (1) The images in the pre-training dataset are) |
| Models are evaluated via binary success rates over 25 trials per task, with a maximum of 25 action steps per trial. | p. 7 (4 Experiments) |
| (5) PolarNet employs PointNext [36] to encode the 3D scene and predicts both heatmaps and offsets for all points to estimate translational actions. | p. 7 (4 Experiments) |
| We performed a hyperparameter grid search and evaluated the model on RLBench. | p. 10 (1) The images in the pre-training dataset are) |
| For every task, we evaluated every baseline over 10 trials to ensure statistical robustness. | p. 8 (Method) |
| 3) ACT [51]: A state-of-the-art 2D non-VLA model using a Conditional Variational Autoencoder (CVAE) to model action distributions. | p. 8 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Results on RLBench. The "Avg. Rank" column reports the average rank of each method across all 18 tasks, where lower values indicate better ...
- **p. 9 / Method - extractive PDF cue:** A common failure mode is that the robot often ignores the target object and moves directly to the destination during pick-and-place manipulation.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Overview. BridgeVLA is a novel 3D VLA model that aligns the input and output within a unified 2D image space. It is pre-trained ...
- **p. 7 / 4 Experiments - extractive PDF cue:** Due to space limitations, the details of the environment setup, baselines, and analysis can be found in Appendix B.1 and Appendix B.2.
- **p. 8 / Method - extractive PDF cue:** As we can see, most methods completely fails when given only 10 trajectories per task except two 3D related methods: RVT-2 and BridgeVLA.
- **p. 6 / 4 Experiments - extractive PDF cue:** Q3: How robust is BridgeVLA in handling visual disturbances (e.g., distractors, background, and lighting)?

- **PDF anchors reviewed:** datasets p. 9 (1) The images in the pre-training dataset are), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 9 (1) The images in the pre-training dataset are), metrics p. 23 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (Figure/Table caption), p. 24 (Figure/Table caption), p. 26 (Figure/Table caption), baselines p. 9 (Figure/Table caption), p. 24 (Figure/Table caption), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (Figure/Table caption), results p. 24 (Figure/Table caption), p. 23 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
