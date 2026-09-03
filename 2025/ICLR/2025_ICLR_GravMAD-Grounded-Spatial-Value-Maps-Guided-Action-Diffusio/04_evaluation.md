# Evaluation - GravMAD: Grounded Spatial Value Maps Guided Action Diffusion for Generalized 3D Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (33 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=qPzYF2EpXb; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114266. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 32 (Figure/Table caption)): GravMAD (Manual) outperforms Act3D and Voxposer across all tasks and exceeds the best baseline, 3D Diffuser Actor, in 9 out of 12 tasks, with an average success rate improvement of ...

## Evaluation Body Digest

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Additionally, we further validate GravMAD on 10 real-world robotic tasks, with details provided in Appendix D.6.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** For each base task, we collect 20 demonstrations for training and evaluate the final checkpoints using 3 random seeds over 25 episodes.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Final checkpoints are evaluated across 3 seeds with 25 test episodes per task.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** For example, in the "open drawer" task, the robot needs to grasp the center of the small handle for optimal performance.
- **p. 15 / A.2 HEURISTICS FOR SUB-GOAL KEYPOSE DISCOVERY - extractive body cue:** This is particularly relevant for object manipulation tasks, where the robot's interactions with objects can be segmented into discrete sub-goals.
- **p. 18 / A.3.2 INFERENCE PHASE - extractive body cue:** Progress is tracked based on the robot's gripper state (open/closed) and whether it is holding an object.
- **p. 17 / A.3.1 TRAINING PHASE - extractive body cue:** In the first map, mc ∈Rw×h×d, the cost is lower near the positions of the robotic end-effector at these sub-goal keyposes and higher as the ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.2) (ii) Is GravMAD's performance competitive on the 3D manipulation tasks encountered during training?

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 7); A ADDITIONAL IMPLEMENTATION DETAILS (p. 15); 10 Evaluation (p. 19); B ADDITIONAL EXPERIMENTAL DETAILS (p. 20).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | GravMAD (Manual) outperforms Act3D and Voxposer across all tasks and exceeds the best baseline, 3D Diffuser Actor, in 9 out of 12 tasks, with ... | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Despite the Detector's coarse SoM positioning affecting GravMAD (VLM)'s performance, it still outperforms Act3D and Voxposer on all tasks, with a 0.91% higher average ... | p. 9 (4 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Ablation Studies. We evaluate the impact of key design elements by reporting the average success rates across 12 base tasks and 8 ... | p. 10 (Figure/Table caption) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Evaluation metrics include the average success rate and rank. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The success rate measures the proportion of tasks completed according to language instructions. | p. 8 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Additionally, we further validate GravMAD on 10 real-world robotic tasks, with details provided in Appendix D.6.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** For each base task, we collect 20 demonstrations for training and evaluate the final checkpoints using 3 random seeds over 25 episodes.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Final checkpoints are evaluated across 3 seeds with 25 test episodes per task.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** For example, in the "open drawer" task, the robot needs to grasp the center of the small handle for optimal performance.
- **p. 15 / A.2 HEURISTICS FOR SUB-GOAL KEYPOSE DISCOVERY - extractive body cue:** This is particularly relevant for object manipulation tasks, where the robot's interactions with objects can be segmented into discrete sub-goals.
- **p. 18 / A.3.2 INFERENCE PHASE - extractive body cue:** Progress is tracked based on the robot's gripper state (open/closed) and whether it is holding an object.
- **p. 17 / A.3.1 TRAINING PHASE - extractive body cue:** In the first map, mc ∈Rw×h×d, the cost is lower near the positions of the robotic end-effector at these sub-goal keyposes and higher as the ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.2) (ii) Is GravMAD's performance competitive on the 3D manipulation tasks encountered during training?

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Comparison of Pipelines. (a) Imitation learning-based methods learn end-to-end policies that map language and 3D observations to actions for precise manipulation. (b) Foundation ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: GravMAD Overview. (a) GravMap Synthesis: During training, we use Sub-goal Keypose Discovery to obtain sub-goals gpos and gopen. During inference, the Detector, Planner, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Visualization of sub-goal keyposes and sub-task stages. The left sub-figure shows image- based sub-goal keyposes and sub-task stages for "take the chicken off ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Generalization to 8 novel RLBench tasks. Evaluations on 8 novel tasks are conducted using 3 seeds, with 25 test episodes per task, utilizing ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Multi-task test results on 12 base tasks. All models are trained on 12 base tasks with 20 demonstrations each. Final checkpoints are evaluated ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 4: Ablation Studies. We evaluate the impact of key design elements by reporting the average success rates across 12 base tasks and 8 novel ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 5: Detailed description of the modules in GravMAD, including the 3D Scene Encoder and the prediction heads A.3 DETAILS OF GRAVMAP SYNTHESIS A.3.1 TRAINING ...
- **p. 19 / Figure/Table caption - extractive body cue:** Table 3: Hyper-parameters for GravMAD, including Sub-goal Keypose Discovery, GravMap, model configuration, training, and evaluation. Planner then receives this context and outputs a sub-goal, representing ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Additionally, we further validate GravMAD on 10 real-world robotic tasks, with details provided in Appendix D.6. | embodiment, simulator version and control stack | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Task/environment | For each base task, we collect 20 demonstrations for training and evaluate the final checkpoints using 3 random seeds over 25 episodes. | reset, timeout, object/scene variation | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (3 METHOD), p. 6 (3 METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Despite the Detector's coarse SoM positioning affecting GravMAD (VLM)'s performance, it still outperforms Act3D and Voxposer on all tasks, with a 0.91% higher average ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Figure 4: Ablation Studies. We evaluate the impact of key design elements by reporting the average success rates across 12 base tasks and 8 ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Evaluation metrics include the average success rate and rank. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| The success rate measures the proportion of tasks completed according to language instructions. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| GravMAD (Manual) outperforms Act3D and Voxposer across all tasks and exceeds the best baseline, 3D Diffuser Actor, in 9 out of 12 tasks, with ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Figure 15: Visualization of additional novel tasks. • For Chained Diffuser (Oracle), the keyposes come from ideal waypoints predefined in simulation, and the model ... | definition/direction/unit from same section | p. 30 (Figure/Table caption) |
| Table 11: Real-robot Results. Success rates of GravMAD on 10 real-world tasks. These tasks include both manipulation and placement challenges. Above the table are ... | definition/direction/unit from same section | p. 32 (Figure/Table caption) |
| The Rotation Head processes tokens with self-attention and an MLP to predict rotation error. | definition/direction/unit from same section | p. 18 (A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Performance gains are compared to the best-performing baselines, indicated by underlines. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| However, GravMAD exhibits superior generalization across all 8 novel tasks compared to the baseline models. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| GravMAD (Manual) outperforms Act3D and Voxposer across all tasks and exceeds the best baseline, 3D Diffuser Actor, in 9 out of 12 tasks, with ... | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Table 3: Hyper-parameters for GravMAD, including Sub-goal Keypose Discovery, GravMap, model configuration, training, and evaluation. Planner then receives this context and outputs a sub-goal, ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |
| We aim to answer the following questions: (i) Can GravMAD achieve superior generalization in novel 3D manipulation tasks compared to SOTA models? | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| Table 10: Generalization Performance Comparison on Additional Novel Tasks. to effectively harness the potential of large-scale data. Without such improvements, the diminishing returns observed ... | comparison identity and matched condition | p. 31 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 4: Ablation Studies. We evaluate the impact of key design elements by reporting the average success rates across 12 base tasks and 8 ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| Table 10: Generalization Performance Comparison on Additional Novel Tasks. to effectively harness the potential of large-scale data. Without such improvements, the diminishing returns observed ... | component/input/data sensitivity | p. 31 (Figure/Table caption) |
| Without GravMaps, the policy lacks regional context, becoming overly sensitive to precise positions and unable to generalize to 9 | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| 4.4 ABLATIONS Extensive ablation studies are conducted to analyze the role of each key design element in GravMAD, with the results shown in Fig ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Figure 16: Additional Ablation Studies. We represent the gripper closure in the gripper map under "w/o. Cost map" as -1 instead of 0, enabling ... | component/input/data sensitivity | p. 31 (Figure/Table caption) |
| Our pipeline consists of the following three components: 17 | component/input/data sensitivity | p. 17 (A.3.2 INFERENCE PHASE) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are: 1) We propose leveraging key sub-goals in 3D manipulation tasks to bridge the gap between foundation models and learned ... | GravMAD (Manual) outperforms Act3D and Voxposer across all tasks and exceeds the best baseline, 3D Diffuser Actor, in 9 out of 12 tasks, with ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 32 (Figure/Table caption) |
| Primary metric/result | Despite the Detector's coarse SoM positioning affecting GravMAD (VLM)'s performance, it still outperforms Act3D and Voxposer on all tasks, with a 0.91% higher average ... | numeric claim only at cited anchor | p. 9 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Close Close Jar Close Jar Condition Meat On Open Drawer Stack cups Push Buttons Models Success ↑Rank ↓ Drawer Banana Distractor Block Grill Small blocks ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Evaluations on 8 novel tasks are conducted using 3 seeds, with 25 test episodes per task, utilizing the final checkpoints from training on 12 base ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** For each base task, we collect 20 demonstrations for training and evaluate the final checkpoints using 3 random seeds over 25 episodes.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We use 3 random seeds over 25 episodes for each novel task.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Final checkpoints are evaluated across 3 seeds with 25 test episodes per task.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** GravMAD (Manual) outperforms Act3D and Voxposer across all tasks and exceeds the best baseline, 3D Diffuser Actor, in 9 out of 12 tasks, with an ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 11: Failure cause analysis, including (a) visualization of failure examples; (b) comparison of imprecise labels and expected labels. identify ideal areas, leading to ... | p. 26 (Figure/Table caption) |
| body limitation/failure cue | During testing, except for the novel task "push buttons light", which must be completed in 3 time steps, all other tasks must be completed ... | p. 8 (4 EXPERIMENTS) |
| body limitation/failure cue | For further analysis of failure cases, please refer to Appendix B.3. | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | In contrast, omitting the cost map causes zero-gradient issues during training, leading to incorrect predictions and task failure. | p. 10 (8 Novel Tasks) |
| body limitation/failure cue | GravMAD (VLM) also struggles in tasks like "Place Wine" due to inaccuracies in the object positions provided by the Detector, especially when Semantic SAM ... | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | This occurs because the encoder cannot process such input. | p. 10 (8 Novel Tasks) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All models complete 600k training iterations on an NVIDIA RTX4090 GPU, with the final checkpoint selected using three random seeds for evaluation. | p. 8 (4 EXPERIMENTS) |
| For each base task, we collect 20 demonstrations for training and evaluate the final checkpoints using 3 random seeds over 25 episodes. | p. 8 (4 EXPERIMENTS) |
| Final checkpoints are evaluated across 3 seeds with 25 test episodes per task. | p. 9 (4 EXPERIMENTS) |
| The implementation of the Sub-goal Keypose Discovery algorithm starts with a set of pre-computed keyposes, which are frames selected from the demonstration sequence through ... | p. 15 (A.2 HEURISTICS FOR SUB-GOAL KEYPOSE DISCOVERY) |
| The pseudocode in Algorithm 4 outlines the heuristic steps for identifying sub-goal keyposes. | p. 16 (A.2 HEURISTICS FOR SUB-GOAL KEYPOSE DISCOVERY) |
| The detailed hyperparameters of GravMAD are listed in Table 3. | p. 18 (A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD) |
| Natural language parameters are parsed by GPT to generate code that assigns values to gpos and gopen. | p. 18 (A.3.2 INFERENCE PHASE) |
| Simultaneously, the CLIP language encoder converts task instructions into language tokens. | p. 6 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 26 / Figure/Table caption - extractive body cue:** Figure 11: Failure cause analysis, including (a) visualization of failure examples; (b) comparison of imprecise labels and expected labels. identify ideal areas, leading to imprecise ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** During testing, except for the novel task "push buttons light", which must be completed in 3 time steps, all other tasks must be completed in ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** For further analysis of failure cases, please refer to Appendix B.3.
- **p. 10 / 8 Novel Tasks - extractive body cue:** In contrast, omitting the cost map causes zero-gradient issues during training, leading to incorrect predictions and task failure.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** GravMAD (VLM) also struggles in tasks like "Place Wine" due to inaccuracies in the object positions provided by the Detector, especially when Semantic SAM fails ...
- **p. 10 / 8 Novel Tasks - extractive body cue:** This occurs because the encoder cannot process such input.

- **Evidence anchors reviewed:** datasets p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 15 (A.2 HEURISTICS FOR SUB-GOAL KEYPOSE DISCOVERY), p. 18 (A.3.2 INFERENCE PHASE), metrics p. 9 (4 EXPERIMENTS), p. 10 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 30 (Figure/Table caption), baselines p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 19 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 31 (Figure/Table caption), results p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 32 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
