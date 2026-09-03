# Evaluation - Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=meRCKuUpmc; PDF retrieval source: https://arxiv.org/pdf/2412.15109. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 19 (A.6.5 DETAILED REAL-WORLD RESULTS), p. 9 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (Figure/Table caption), p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS)): Table 1: LIBERO-LONG results. For each task, we present the average performance of top-3 checkpoints averaged over 20 rollouts. The metric "Avg. Success" measures the average success rate across ten ...

## Evaluation Body Digest

- **p. 16 / A.4 LIBERO-LONG EXPERIMENT DETAILS - extractive body cue:** LIBERO (Liu et al., 2024) is a novel benchmark for lifelong learning in robot manipulation, comprising four task suites: LIBERO-SPATIAL, LIBERO-OBJECT, LIBERO-GOAL, and LIBERO100.
- **p. 19 / A.6.4 ACROSS EMBODIMENTS EXPERIMENTS - extractive body cue:** We refer the subset mix-up recipe in Octo (Ghosh et al., 2024), remove all the subset that includes franka robots, filter subsets with odd action ...
- **p. 19 / A.6.4 ACROSS EMBODIMENTS EXPERIMENTS - extractive body cue:** We attribute marginal improvements in general manipulation tasks to the diversity of objects, tasks, scenes, and language instructions in OXE.
- **p. 16 / A.5 CALVIN ABC-D EXPERIMENT DETAILS - extractive body cue:** The CALVIN benchmark includes four distinct but structurally similar environments-Env A, B, C and D.
- **p. 17 / A.5 CALVIN ABC-D EXPERIMENT DETAILS - extractive body cue:** CALVIN offers rich observations for robot learning.
- **p. 17 / A.5 CALVIN ABC-D EXPERIMENT DETAILS - extractive body cue:** We use images from both fixed and grippermounted cameras, resized to 224x224 pixels, along with robot state information, which includes end-effector position, orientation, and gripper ...
- **p. 14 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** We tokenize the robot state using an MLP.
- **p. 14 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For all simulation results, we use eight 4090 GPUS to pre-train and fine-tune.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** A.1 IMPLEMENTATION DETAILS (p. 14); A.3 BASELINE IMPLEMENTATION (p. 16); A.4 LIBERO-LONG EXPERIMENT DETAILS (p. 16); A.5 CALVIN ABC-D EXPERIMENT DETAILS (p. 16); A.6 REAL WORLD EXPERIMENT DETAILS (p. 17); A.6.3 REAL-WORLD IMPLEMENTATION DETAILS (p. 19); A.6.4 ACROSS EMBODIMENTS EXPERIMENTS (p. 19); A.6.5 DETAILED REAL-WORLD RESULTS (p. 19).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: LIBERO-LONG results. For each task, we present the average performance of top-3 checkpoints averaged over 20 rollouts. The metric "Avg. Success" measures ... | p. 6 (Figure/Table caption) |
| A.6.5 DETAILED REAL-WORLD RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The raw records of the real-world experiments are shown in Table A-V, Table A-VI, Table A-VII, and Table A-VIII, which we use to calculate ... | p. 19 (A.6.5 DETAILED REAL-WORLD RESULTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Real-world Benchmark of four generalization-centric tasks. Left: We use a Franka Research 3 robot with a Robotiq-2f-85 gripper and two RealSense D435i ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4: Real-world main results. We evaluate all the methods with 15 (cases) × 3 (repeated trials) rollouts per task. Our method achieves better ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2: CALVIN ABC-D results. We present the average success rates of top-3 checkpoints computed over 1000 rollouts for each task and the average ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 16 / A.4 LIBERO-LONG EXPERIMENT DETAILS - extractive body cue:** LIBERO (Liu et al., 2024) is a novel benchmark for lifelong learning in robot manipulation, comprising four task suites: LIBERO-SPATIAL, LIBERO-OBJECT, LIBERO-GOAL, and LIBERO100.
- **p. 19 / A.6.4 ACROSS EMBODIMENTS EXPERIMENTS - extractive body cue:** We refer the subset mix-up recipe in Octo (Ghosh et al., 2024), remove all the subset that includes franka robots, filter subsets with odd action ...
- **p. 19 / A.6.4 ACROSS EMBODIMENTS EXPERIMENTS - extractive body cue:** We attribute marginal improvements in general manipulation tasks to the diversity of objects, tasks, scenes, and language instructions in OXE.
- **p. 16 / A.5 CALVIN ABC-D EXPERIMENT DETAILS - extractive body cue:** The CALVIN benchmark includes four distinct but structurally similar environments-Env A, B, C and D.
- **p. 17 / A.5 CALVIN ABC-D EXPERIMENT DETAILS - extractive body cue:** CALVIN offers rich observations for robot learning.
- **p. 17 / A.5 CALVIN ABC-D EXPERIMENT DETAILS - extractive body cue:** We use images from both fixed and grippermounted cameras, resized to 224x224 pixels, along with robot state information, which includes end-effector position, orientation, and gripper ...
- **p. 14 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** We tokenize the robot state using an MLP.
- **p. 14 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For all simulation results, we use eight 4090 GPUS to pre-train and fine-tune.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: In contrast to previous methods that (a) conduct end-to-end naive behavior cloning from large-scale robotic data or (b) use decoupled visual prediction and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Pipeline of Seer. Seer consists of three parts: Multi-Modal Encoder, Conditional Visual Foresight and Inverse Dynamics Prediction. In Multi-Modal Encoder, Seer incorporates the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: LIBERO-LONG results. For each task, we present the average performance of top-3 checkpoints averaged over 20 rollouts. The metric "Avg. Success" measures the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: CALVIN ABC-D results. We present the average success rates of top-3 checkpoints computed over 1000 rollouts for each task and the average number ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Data efficiency and Scalability. The two figures on the left depict Seer's performance on LIBERO and CALVIN using different proportions of the downstream ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Ablation studies on fine-tuning and pre-training objectives. Integrating the conditional visual foresight objective Lfore and inverse dynamics prediction objective Linv yields the best ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Real-world Benchmark of four generalization-centric tasks. Left: We use a Franka Research 3 robot with a Robotiq-2f-85 gripper and two RealSense D435i cameras. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Real-world main results. We evaluate all the methods with 15 (cases) × 3 (repeated trials) rollouts per task. Our method achieves better performances ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | LIBERO (Liu et al., 2024) is a novel benchmark for lifelong learning in robot manipulation, comprising four task suites: LIBERO-SPATIAL, LIBERO-OBJECT, LIBERO-GOAL, and LIBERO100. | embodiment, simulator version and control stack | p. 16 (A.4 LIBERO-LONG EXPERIMENT DETAILS), p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS) |
| Task/environment | We refer the subset mix-up recipe in Octo (Ghosh et al., 2024), remove all the subset that includes franka robots, filter subsets with odd ... | reset, timeout, object/scene variation | p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS), p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 3 (3 METHOD), p. 15 (A.1 IMPLEMENTATION DETAILS) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 5 (3 METHOD), p. 3 (3 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4: Real-world Benchmark of four generalization-centric tasks. Left: We use a Franka Research 3 robot with a Robotiq-2f-85 gripper and two RealSense D435i ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| The raw records of the real-world experiments are shown in Table A-V, Table A-VI, Table A-VII, and Table A-VIII, which we use to calculate ... | definition/direction/unit from same section | p. 19 (A.6.5 DETAILED REAL-WORLD RESULTS) |
| Table 1: LIBERO-LONG results. For each task, we present the average performance of top-3 checkpoints averaged over 20 rollouts. The metric "Avg. Success" measures ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 2: CALVIN ABC-D results. We present the average success rates of top-3 checkpoints computed over 1000 rollouts for each task and the average ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| High-precision tasks require a concentrated and precise action distribution. | definition/direction/unit from same section | p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS) |
| In the simulation benchmark, we report the scores for Roboflamingo, Susie, GR-1, and the 3D Diffusor Actor from their respective papers. | definition/direction/unit from same section | p. 16 (A.3 BASELINE IMPLEMENTATION) |
| We also incorporated the robot state to help the policy understand the robot's self-state, including the position and orientation of the end effector and ... | definition/direction/unit from same section | p. 16 (A.4 LIBERO-LONG EXPERIMENT DETAILS) |
| Figure 3: Data efficiency and Scalability. The two figures on the left depict Seer's performance on LIBERO and CALVIN using different proportions of the ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1: LIBERO-LONG results. For each task, we present the average performance of top-3 checkpoints averaged over 20 rollouts. The metric "Avg. Success" measures ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 2: CALVIN ABC-D results. We present the average success rates of top-3 checkpoints computed over 1000 rollouts for each task and the average ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 4: Real-world main results. We evaluate all the methods with 15 (cases) × 3 (repeated trials) rollouts per task. Our method achieves better ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| We then fine-tune these two baselines on the downstream tasks and report performances. | comparison identity and matched condition | p. 19 (A.6.3 REAL-WORLD IMPLEMENTATION DETAILS) |
| In real-world experiments involving the MVP and MPI baselines, we replace the MAE pre-trained vision encoder in our network with the MVP pre-trained and ... | comparison identity and matched condition | p. 19 (A.6.3 REAL-WORLD IMPLEMENTATION DETAILS) |
| Figure 1: In contrast to previous methods that (a) conduct end-to-end naive behavior cloning from large-scale robotic data or (b) use decoupled visual prediction ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We refer the subset mix-up recipe in Octo (Ghosh et al., 2024), remove all the subset that includes franka robots, filter subsets with odd ... | component/input/data sensitivity | p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS) |
| Table 3: Ablation studies on fine-tuning and pre-training objectives. Integrating the conditional visual foresight objective Lfore and inverse dynamics prediction objective Linv yields the ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 5: Generalization evaluation. We design a generalization test per task with different dis- turbances. Top Left: In Flip Bowl, we put several bowls ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| Thanks to the strong design of our policy, MVP and MPI show competitive performance, though they only approach the results of our policy without ... | component/input/data sensitivity | p. 16 (A.3 BASELINE IMPLEMENTATION) |
| Figure 1: In contrast to previous methods that (a) conduct end-to-end naive behavior cloning from large-scale robotic data or (b) use decoupled visual prediction ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| We use LIBERO-90 as the pretraining dataset, while LIBERO-LONG is utilized for the downstream finetuning and evaluation. | component/input/data sensitivity | p. 16 (A.4 LIBERO-LONG EXPERIMENT DETAILS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Additionally, We evaluate our method on six challenging real-world tasks with over 900 trials. | Table 1: LIBERO-LONG results. For each task, we present the average performance of top-3 checkpoints averaged over 20 rollouts. The metric "Avg. Success" measures ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 19 (A.6.5 DETAILED REAL-WORLD RESULTS), p. 9 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (Figure/Table caption), p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS) |
| Primary metric/result | The raw records of the real-world experiments are shown in Table A-V, Table A-VI, Table A-VII, and Table A-VIII, which we use to calculate ... | numeric claim only at cited anchor | p. 19 (A.6.5 DETAILED REAL-WORLD RESULTS) |

- Numeric sentences retained from the body:
- **p. 14 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Directly inputting all 197 tokens into the transformer backbone would create a significant computational burden, particularly when processing long histories.
- **p. 14 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** For all simulation results, we use eight 4090 GPUS to pre-train and fine-tune.
- **p. 14 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** The pre-training process requires about 40 hours for CALVIN ABC-D and and 30 hours for LIBERO-LONG.
- **p. 14 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** The fine-tuning process requires about 24 hours for CALVIN ABC-D and 6 hours for LIBERO-LONG.
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Hyperparameters Pre-training Fine-tuning Batch Size 640 (LIBERO & CALVIN) / 2048 (Real) 512 Learning Rate 1e-4 1e-3 Optimizer AdamW AdamW Learning Rate Schedule Cosine decay ...
- **p. 16 / A.4 LIBERO-LONG EXPERIMENT DETAILS - extractive body cue:** The first three task suites are designed to disentangle the transfer of declarative and procedural knowledge, while LIBERO-100 consists of 100 tasks involving entangled knowledge ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The score will plus one (+1) when (1) pushing the button successfully with no collision, and (2) exceeding 3/4 of the scale. | p. 18 (A.6.2 HIGH-PRECISION AND CONTACT-RICH TASKS) |
| body limitation/failure cue | The score will plus one (+1) when (1) grasping the camera model, and (2) inserting successfully with no collision. | p. 19 (A.6.2 HIGH-PRECISION AND CONTACT-RICH TASKS) |
| body limitation/failure cue | Notably, both tasks require quite precise action predictions and collision-free interactions, showing our model's potential in high-precision and contact-rich tasks. | p. 19 (A.6.2 HIGH-PRECISION AND CONTACT-RICH TASKS) |
| body limitation/failure cue | Specifically, [FRS] tokens are appended to extract representations for two views, and three [INV ] tokens are appended to predict actions across three steps, ... | p. 14 (A.1 IMPLEMENTATION DETAILS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Hyperparameters Pre-training Fine-tuning Batch Size 640 (LIBERO & CALVIN) / 2048 (Real) 512 Learning Rate 1e-4 1e-3 Optimizer AdamW AdamW Learning Rate Schedule Cosine ... | p. 15 (A.1 IMPLEMENTATION DETAILS) |
| The inputs are processed by multiple transformer encoder blocks. | p. 14 (A.1 IMPLEMENTATION DETAILS) |
| In this section, we outline the implementation details of our framework. | p. 14 (A.1 IMPLEMENTATION DETAILS) |
| Hidden size Number of layers Number of heads image encoder 768 12 12 perceiver resampler 768 3 8 transformer backbone 384 24 12 image ... | p. 15 (A.1 IMPLEMENTATION DETAILS) |
| For MTACT and OpenVLA, we reproduce the results using the official code. | p. 16 (A.3 BASELINE IMPLEMENTATION) |
| For MVP and MPI, we replace the vision encoder in our policy with their pretrained versions. | p. 16 (A.3 BASELINE IMPLEMENTATION) |
| The unstructured data includes exploratory and sub-optimal behaviors, comprising approximately 2.4 million interaction steps and 40 million shorthorizon windows. | p. 17 (A.5 CALVIN ABC-D EXPERIMENT DETAILS) |
| Key hyperparameters are listed in Table A-I. | p. 19 (A.6.3 REAL-WORLD IMPLEMENTATION DETAILS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 18 / A.6.2 HIGH-PRECISION AND CONTACT-RICH TASKS - extractive body cue:** The score will plus one (+1) when (1) pushing the button successfully with no collision, and (2) exceeding 3/4 of the scale.
- **p. 19 / A.6.2 HIGH-PRECISION AND CONTACT-RICH TASKS - extractive body cue:** The score will plus one (+1) when (1) grasping the camera model, and (2) inserting successfully with no collision.
- **p. 19 / A.6.2 HIGH-PRECISION AND CONTACT-RICH TASKS - extractive body cue:** Notably, both tasks require quite precise action predictions and collision-free interactions, showing our model's potential in high-precision and contact-rich tasks.
- **p. 14 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Specifically, [FRS] tokens are appended to extract representations for two views, and three [INV ] tokens are appended to predict actions across three steps, ensuring ...

- **Evidence anchors reviewed:** datasets p. 16 (A.4 LIBERO-LONG EXPERIMENT DETAILS), p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS), p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS), p. 16 (A.5 CALVIN ABC-D EXPERIMENT DETAILS), p. 17 (A.5 CALVIN ABC-D EXPERIMENT DETAILS), p. 17 (A.5 CALVIN ABC-D EXPERIMENT DETAILS), metrics p. 9 (Figure/Table caption), p. 19 (A.6.5 DETAILED REAL-WORLD RESULTS), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS), p. 16 (A.3 BASELINE IMPLEMENTATION), baselines p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 19 (A.6.3 REAL-WORLD IMPLEMENTATION DETAILS), p. 19 (A.6.3 REAL-WORLD IMPLEMENTATION DETAILS), p. 1 (Figure/Table caption), results p. 6 (Figure/Table caption), p. 19 (A.6.5 DETAILED REAL-WORLD RESULTS), p. 9 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (Figure/Table caption), p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
