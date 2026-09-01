# Evaluation - FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Simulation), p. 6 (Figure/Table caption), p. 7 (4.2. Real-World), p. 7 (4.3. Ablation Studies), p. 8 (4.4. Analysis on DGMoE), p. 3 (Figure/Table caption)): Furthermore, FedVLA consistently outperforms FedAvg, which only achieves an average success rate of 51.7%.

## Evaluation Body Digest

- **p. 6 / 4.2. Real-World - extractive PDF cue:** We collect real-world robotic demonstrations for household-related tasks, including Clean Up, Trash Collection, Open Drawer, and Sorting Pills, as shown in Figure 4.
- **p. 6 / 4.1. Simulation - extractive PDF cue:** We utilize the MuJoCo engine [21] to simulate tasks from the Meta-World robot manipulation benchmark [30].
- **p. 7 / 4.3. Ablation Studies - extractive PDF cue:** These findings strongly support that IOSP helps decompose complex visual scenes into task-relevant object representations, DGMoE module routes the adaptive knowledge, EDA ensures the integrity ...
- **p. 7 / 4.2. Real-World - extractive PDF cue:** Real-world evaluation across four tasks.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Validation loss comparison in ablation study across four tasks.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Visualization of expert activation distribution per task for different object types.
- **p. 7 / 4.3. Ablation Studies - extractive PDF cue:** We compare the task success rate and record the validation loss during the training process.
- **p. 7 / 4.2. Real-World - extractive PDF cue:** In contrast, FedAvg exhibits a significant performance drop across all tasks, with an average success rate of 53.3%, which is 10.0% lower than our method.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Simulation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Furthermore, FedVLA consistently outperforms FedAvg, which only achieves an average success rate of 51.7%. | p. 6 (4.1. Simulation) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Simulation evaluation across four tasks. Performance Comparison. The evaluation results in the simulation environment are presented in Table 1. Fed- VLA achieves ... | p. 6 (Figure/Table caption) |
| 4.2. Real-World | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, FedAvg exhibits a significant performance drop across all tasks, with an average success rate of 53.3%, which is 10.0% lower than our ... | p. 7 (4.2. Real-World) |
| 4.3. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | We compare the task success rate and record the validation loss during the training process. | p. 7 (4.3. Ablation Studies) |
| 4.4. Analysis on DGMoE | EMPIRICAL / REAL-ROBOT OR HARDWARE | The proposed DGMoE achieves consistently lower expert activation densities compared to vanilla topk MoE, which assigns tokens to a fixed number of experts, where ... | p. 8 (4.4. Analysis on DGMoE) |

## Dataset / Benchmark Role

- **p. 6 / 4.2. Real-World - extractive PDF cue:** We collect real-world robotic demonstrations for household-related tasks, including Clean Up, Trash Collection, Open Drawer, and Sorting Pills, as shown in Figure 4.
- **p. 6 / 4.1. Simulation - extractive PDF cue:** We utilize the MuJoCo engine [21] to simulate tasks from the Meta-World robot manipulation benchmark [30].
- **p. 7 / 4.3. Ablation Studies - extractive PDF cue:** These findings strongly support that IOSP helps decompose complex visual scenes into task-relevant object representations, DGMoE module routes the adaptive knowledge, EDA ensures the integrity ...
- **p. 7 / 4.2. Real-World - extractive PDF cue:** Real-world evaluation across four tasks.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Validation loss comparison in ablation study across four tasks.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Visualization of expert activation distribution per task for different object types.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Comparison between centralized and federated VLA training. Centralized training collects all user data on the cloud, raising privacy concerns due to potential exposure ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Illustration of the proposed FedVLA framework and its key component. (a) An overview of the FedVLA, which consists of multiple clients and a ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Instruction-Oriented Scene-Parsing module, which de- composes observations into object-level representations guided by task instructions, enhancing task-aware feature extraction through vision-language alignment. The overview ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The clients train their models locally and commu- nicate with the server per round until the model converges. The following sections introduce our ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Simulation evaluation across four tasks. Performance Comparison. The evaluation results in the simulation environment are presented in Table 1. Fed- VLA achieves an ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Real-World Tasks. Each column represents a different task, while each row demonstrates keyframes of task execution. From left to right, the tasks are: ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Real-world evaluation across four tasks.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation studies of proposed FedVLA without IOSP, DG- MoE, and EDA. From Table 3, we can see that each module contributes significantly to ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We collect real-world robotic demonstrations for household-related tasks, including Clean Up, Trash Collection, Open Drawer, and Sorting Pills, as shown in Figure 4. | embodiment, simulator version and control stack | p. 6 (4.2. Real-World), p. 6 (4.1. Simulation) |
| Task/environment | We utilize the MuJoCo engine [21] to simulate tasks from the Meta-World robot manipulation benchmark [30]. | reset, timeout, object/scene variation | p. 6 (4.1. Simulation), p. 7 (4.3. Ablation Studies) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We compare the task success rate and record the validation loss during the training process. | definition/direction/unit from same section | p. 7 (4.3. Ablation Studies) |
| In contrast, FedAvg exhibits a significant performance drop across all tasks, with an average success rate of 53.3%, which is 10.0% lower than our ... | definition/direction/unit from same section | p. 7 (4.2. Real-World) |
| FedVLA achieves an average success rate of 63.3%, closely approaching the 65.0% of centralized training. | definition/direction/unit from same section | p. 6 (4.1. Simulation) |
| Furthermore, FedVLA consistently outperforms FedAvg, which only achieves an average success rate of 51.7%. | definition/direction/unit from same section | p. 6 (4.1. Simulation) |
| Figure 2. Illustration of the proposed FedVLA framework and its key component. (a) An overview of the FedVLA, which consists of multiple clients and ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Validation loss comparison in ablation study across four tasks. | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| The x-axis represents the training rounds, while the y-axis represents the validation loss. | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| Figure 1. Comparison between centralized and federated VLA training. Centralized training collects all user data on the cloud, raising privacy concerns due to potential ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Furthermore, FedVLA consistently outperforms FedAvg, which only achieves an average success rate of 51.7%. | comparison identity and matched condition | p. 6 (4.1. Simulation) |
| The federated averaging (FedAvg) [22] is a strong FL baseline where models are trained locally on each client and simply averaged on the server. | comparison identity and matched condition | p. 6 (4. Experiments) |
| In contrast, supporting objects and background objects, which provide contextual spatial information, activate fewer experts compared to target objects. | comparison identity and matched condition | p. 8 (4.4. Analysis on DGMoE) |
| The proposed DGMoE achieves consistently lower expert activation densities compared to vanilla topk MoE, which assigns tokens to a fixed number of experts, where ... | comparison identity and matched condition | p. 8 (4.4. Analysis on DGMoE) |
| Ablation studies of proposed FedVLA without IOSP, DGMoE, and EDA. | comparison identity and matched condition | p. 7 (4.3. Ablation Studies) |
| To further explore the effectiveness of the IOSP, DGMOE and EDA in FedVLA, we conduct ablation experiments by individually removing each module while keeping ... | comparison identity and matched condition | p. 7 (4.3. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To further explore the effectiveness of the IOSP, DGMOE and EDA in FedVLA, we conduct ablation experiments by individually removing each module while keeping ... | component/input/data sensitivity | p. 7 (4.3. Ablation Studies) |
| Ablation studies of proposed FedVLA without IOSP, DGMoE, and EDA. | component/input/data sensitivity | p. 7 (4.3. Ablation Studies) |
| Validation loss comparison in ablation study across four tasks. | component/input/data sensitivity | p. 8 (4.3. Ablation Studies) |
| We employ the pretrained HPT [28] as the backbone of our VLA model and train it for 1,000 communication rounds between clients and the ... | component/input/data sensitivity | p. 6 (4. Experiments) |
| Figure 2. Illustration of the proposed FedVLA framework and its key component. (a) An overview of the FedVLA, which consists of multiple clients and ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Extensive experiments in both simulation and real-world environments demonstrate that FedVLA achieves performance comparable to centralized training while preserving data privacy. • We introduce ... | Furthermore, FedVLA consistently outperforms FedAvg, which only achieves an average success rate of 51.7%. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Simulation), p. 6 (Figure/Table caption), p. 7 (4.2. Real-World), p. 7 (4.3. Ablation Studies), p. 8 (4.4. Analysis on DGMoE), p. 3 (Figure/Table caption) |
| Primary metric/result | Table 1. Simulation evaluation across four tasks. Performance Comparison. The evaluation results in the simulation environment are presented in Table 1. Fed- VLA achieves ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4. Experiments - extractive PDF cue:** We employ the pretrained HPT [28] as the backbone of our VLA model and train it for 1,000 communication rounds between clients and the server, ...
- **p. 6 / 4. Experiments - extractive PDF cue:** In simulation, the model is trained with a learning rate of 5 × 10-6, while in real-world settings, the learning rate is set to 2×10-5.
- **p. 6 / 4. Experiments - extractive PDF cue:** Each task takes for 15 trials and repeats for 5 times.
- **p. 6 / 4.1. Simulation - extractive PDF cue:** For each task, we collect approximately 30-80 episodes, each consisting of 40-100 steps.
- **p. 6 / 4.2. Real-World - extractive PDF cue:** A RealSense D435i RGB-D camera is mounted above the robot, capturing RGB images in real time at a resolution of 1280 × 720 with a ...
- **p. 6 / 4.2. Real-World - extractive PDF cue:** Each task includes approximately 50 demonstrations, with each trajectory consisting of 20 to 80 steps.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | For evaluation, the success and failure of a trial are recoreded as 1 and 0. | p. 6 (4. Experiments) |
| body limitation/failure cue | For collision detection and dynamics simulation, we employ official physics engines to ensure accurate robotic interactions within the simulation environment. | p. 6 (4.1. Simulation) |
| body limitation/failure cue | The integration of these modules together results in a architecture that supports FedVLA's robustness and adaptability across diverse tasks. | p. 7 (4.3. Ablation Studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each client trains locally with a batch size of 256 using the Adam optimizer. | p. 6 (4. Experiments) |
| In simulation, the model is trained with a learning rate of 5 × 10-6, while in real-world settings, the learning rate is set to ... | p. 6 (4. Experiments) |
| The Clean Up task is harder in the manipulation aspect as it requires the robot interaction for multiple steps. | p. 7 (4.3. Ablation Studies) |
| Specifically, the experimental setups are as follows: (1) remove the IOSP module and directly input the entire scene image and proprioception data into the ... | p. 7 (4.3. Ablation Studies) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4. Experiments - extractive PDF cue:** For evaluation, the success and failure of a trial are recoreded as 1 and 0.
- **p. 6 / 4.1. Simulation - extractive PDF cue:** For collision detection and dynamics simulation, we employ official physics engines to ensure accurate robotic interactions within the simulation environment.
- **p. 7 / 4.3. Ablation Studies - extractive PDF cue:** The integration of these modules together results in a architecture that supports FedVLA's robustness and adaptability across diverse tasks.

- **PDF anchors reviewed:** datasets p. 6 (4.2. Real-World), p. 6 (4.1. Simulation), p. 7 (4.3. Ablation Studies), p. 7 (4.2. Real-World), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), metrics p. 7 (4.3. Ablation Studies), p. 7 (4.2. Real-World), p. 6 (4.1. Simulation), p. 6 (4.1. Simulation), p. 3 (Figure/Table caption), p. 8 (4.3. Ablation Studies), baselines p. 6 (4.1. Simulation), p. 6 (4. Experiments), p. 8 (4.4. Analysis on DGMoE), p. 8 (4.4. Analysis on DGMoE), p. 7 (4.3. Ablation Studies), p. 7 (4.3. Ablation Studies), results p. 6 (4.1. Simulation), p. 6 (Figure/Table caption), p. 7 (4.2. Real-World), p. 7 (4.3. Ablation Studies), p. 8 (4.4. Analysis on DGMoE), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
