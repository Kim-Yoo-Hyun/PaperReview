# Evaluation - RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (68 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=PGUC3mmMoi; PDF retrieval source: https://openreview.net/pdf/c5f8c1cd83b4c3e70c6b81498b10fcef9000dc8b.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 18 (A.1.1 EXPERIMENTAL SETTING), p. 9 (3 DATASET), p. 25 (A.3.1 OPEN-LOOP CROSS-PLATFORM EVALUATION), p. 10 (3 DATASET), p. 18 (A.1.1 EXPERIMENTAL SETTING), p. 7 (3 DATASET)): 60.0%) and achieves a higher average success rate (60.0% vs.

## Evaluation Body Digest

- **p. 26 / A.3.3 CLOSE-LOOP EVALUATION ON REAL-WORLD WIDOWX ROBOT - extractive PDF cue:** Our evaluation focuses on a kitchen environment, where we design four manipulation tasks, each executed 15 times: • Pick the Spoon: The robot must grasp ...
- **p. 5 / 3 DATASET - extractive PDF cue:** This dataset includes 6 types of robot arms, 571 types of scenes, and 15 types of primitive skills.
- **p. 25 / A.3.1 OPEN-LOOP CROSS-PLATFORM EVALUATION - extractive PDF cue:** Our dataset spans over 570 scenes across multiple robotic embodiments, forming a hybrid collection that is both cross-platform and cross-scene.
- **p. 6 / 3 DATASET - extractive PDF cue:** Published as a conference paper at ICLR 2026 Subtasks The robot task is ‘drag the plate… Return the future 10 point of gripper Planner General ...
- **p. 25 / A.3.2 CLOSE-LOOP EVALUATION ON SIMPLERENV - extractive PDF cue:** We conduct a close-loop experiment within SimplerEnv (Li et al., 2024d), a benchmark to evaluate models across various tasks with the WidowX Robot (WR) and ...
- **p. 27 / A.4.2 VQA BENCHMARKS - extractive PDF cue:** Embodied benchmarks such as Where2Place (Zhou et al., 2025a), RoboRefIt (Lu et al., 2023), RoboVQA (Sermanet et al., 2024), and RefSpatial-Bench (Lu et al., 2023) ...
- **p. 4 / 3 DATASET - extractive PDF cue:** By integrating raw teleoperated video recordings of these datasets, followed by rigorous screening and pre-processing, we constructed a high-quality, large-scale database consisting of 230k manipulation ...
- **p. 4 / 3 DATASET - extractive PDF cue:** To enhance dataset diversity, we collected two types of raw manipulation data: (1) In-the-Wild setting (i.e., diverse indoor scenarios), emphasizing the diversity of scenes and ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 3 DATASET (p. 4); A.1 Real-World Experiments for Executor (p. 17); A.1.1 Experimental Setting (p. 17); A.1.3 More results and Visualization (p. 17); A.2 Additional Ablation Experiments for RoboInter-VLA (p. 17); A.2.2 Experiment Results for Data Scaling Law (p. 17); A.2.4 Detailed Results of Planner on Temporal RoboInter-VQA (p. 17); A.3.1 Open-loop Cross-platform Evaluation (p. 17); A.3.2 Close-loop Evaluation on SimplerEnv (p. 17); A.3.3 Close-loop Evaluation on Real-world WidowX Robot (p. 17); A.4 Additional Details of Training and Evaluation (p. 17); A.4.2 VQA Benchmarks (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| A.1.1 EXPERIMENTAL SETTING | BENCHMARK / DATASET | 60.0%) and achieves a higher average success rate (60.0% vs. | p. 18 (A.1.1 EXPERIMENTAL SETTING) |
| 3 DATASET | BENCHMARK / DATASET | The most significant improvement comes from Trace, which introduces dense, temporally grounded information and achieves the strongest overall performance. | p. 9 (3 DATASET) |
| A.3.1 OPEN-LOOP CROSS-PLATFORM EVALUATION | BENCHMARK / DATASET | The results show that all RoboInterVLA variants consistently outperform the vanilla baseline across platforms, with the Modular configuration achieving the best overall accuracy among ... | p. 25 (A.3.1 OPEN-LOOP CROSS-PLATFORM EVALUATION) |
| 3 DATASET | BENCHMARK / DATASET | Under OOD conditions, the gap widens, and IC-E2E achieves a 58.3% success rate, while Vanilla reaches only 38.3%, indicating the superior generalization of IC-E2E. | p. 10 (3 DATASET) |
| A.1.1 EXPERIMENTAL SETTING | BENCHMARK / DATASET | We report success rates for four tasks under ID/OOD settings and the ID→OOD performance drop. | p. 18 (A.1.1 EXPERIMENTAL SETTING) |

## Dataset / Benchmark Role

- **p. 26 / A.3.3 CLOSE-LOOP EVALUATION ON REAL-WORLD WIDOWX ROBOT - extractive PDF cue:** Our evaluation focuses on a kitchen environment, where we design four manipulation tasks, each executed 15 times: • Pick the Spoon: The robot must grasp ...
- **p. 5 / 3 DATASET - extractive PDF cue:** This dataset includes 6 types of robot arms, 571 types of scenes, and 15 types of primitive skills.
- **p. 25 / A.3.1 OPEN-LOOP CROSS-PLATFORM EVALUATION - extractive PDF cue:** Our dataset spans over 570 scenes across multiple robotic embodiments, forming a hybrid collection that is both cross-platform and cross-scene.
- **p. 6 / 3 DATASET - extractive PDF cue:** Published as a conference paper at ICLR 2026 Subtasks The robot task is ‘drag the plate… Return the future 10 point of gripper Planner General ...
- **p. 25 / A.3.2 CLOSE-LOOP EVALUATION ON SIMPLERENV - extractive PDF cue:** We conduct a close-loop experiment within SimplerEnv (Li et al., 2024d), a benchmark to evaluate models across various tasks with the WidowX Robot (WR) and ...
- **p. 27 / A.4.2 VQA BENCHMARKS - extractive PDF cue:** Embodied benchmarks such as Where2Place (Zhou et al., 2025a), RoboRefIt (Lu et al., 2023), RoboVQA (Sermanet et al., 2024), and RefSpatial-Bench (Lu et al., 2023) ...
- **p. 4 / 3 DATASET - extractive PDF cue:** By integrating raw teleoperated video recordings of these datasets, followed by rigorous screening and pre-processing, we constructed a high-quality, large-scale database consisting of 230k manipulation ...
- **p. 4 / 3 DATASET - extractive PDF cue:** To enhance dataset diversity, we collected two types of raw manipulation data: (1) In-the-Wild setting (i.e., diverse indoor scenarios), emphasizing the diversity of scenes and ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: RoboInter manipulation suite includes annotation tools, annotated data, curated VQA dataset, and their applications in VLMs and VLAs. RoboInter provides a dataset with ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison of embodied annotations datasets. Emb.-VQA denotes the availability of cu- rated embodied VQA benchmarks and datasets; E2E-ACT indicates whether the dataset temporally ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of RoboInter-Data and RoboInter-VQA. We collect and annotate 230k ma- nipulation episodes to obtain 10 types of intermediate representation annotations through Data ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: Framework of RoboInter-VLA. Our model follows a plan-then-execute paradigm with a VLM-based Planner and an Executor. The Planner exhibits enhanced understanding and gen- ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Performance comparison on third-party benchmarks. Including Embodied, Ground- ing, and General benchmarks for general VLMs (upper) and embodied VLMs (lower). Model Name Embodied ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Results of RoboInter-VQA spatial and temporal benchmark. G.D. means grounding, A.F. denotes Affordance. Spatial generation uses ACC@IOU>0.1 (%↑), multiple choice and T/F use ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 4: Open-loop evaluation in In-the-Wild setting. We report OLS with different error thresholds (@0.1 to @0.01) and the mean value.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 4: Open-loop evaluation in TableTop setting. We show the curve of OLS@0.05 from 1k to 40k training steps. We mainly report the five variances ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our evaluation focuses on a kitchen environment, where we design four manipulation tasks, each executed 15 times: • Pick the Spoon: The robot must ... | embodiment, simulator version and control stack | p. 26 (A.3.3 CLOSE-LOOP EVALUATION ON REAL-WORLD WIDOWX ROBOT), p. 5 (3 DATASET) |
| Task/environment | This dataset includes 6 types of robot arms, 571 types of scenes, and 15 types of primitive skills. | reset, timeout, object/scene variation | p. 5 (3 DATASET), p. 25 (A.3.1 OPEN-LOOP CROSS-PLATFORM EVALUATION) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report success rates for four tasks under ID/OOD settings and the ID→OOD performance drop. | definition/direction/unit from same section | p. 18 (A.1.1 EXPERIMENTAL SETTING) |
| 60.0%) and achieves a higher average success rate (60.0% vs. | definition/direction/unit from same section | p. 18 (A.1.1 EXPERIMENTAL SETTING) |
| We report the average success rate of each task. | definition/direction/unit from same section | p. 25 (A.3.2 CLOSE-LOOP EVALUATION ON SIMPLERENV) |
| The parameter size of LLM are shown behind the model name. % of success rate is omitted. | definition/direction/unit from same section | p. 25 (A.3.2 CLOSE-LOOP EVALUATION ON SIMPLERENV) |
| 34.4 26.3 58.3 63.1 67.5 99.2 100.0 76.2 94.9 95.6 92.3 Average (weighted) 59.7 60.5 55.8 59.4 60.0 46.8 46.4 63.5 88.7 93.0 83.9 ... | definition/direction/unit from same section | p. 24 (A.2.4 DETAILED RESULTS OF PLANNER ON TEMPORAL ROBOINTER-VQA) |
| We study how our dataset and the pretrained Planner affect the closed-loop success rate. | definition/direction/unit from same section | p. 9 (3 DATASET) |
| EC-E2E records a lower ID success rate than IC-E2E (68.3% vs. | definition/direction/unit from same section | p. 10 (3 DATASET) |
| In ID evaluations, IC-E2E attains an average success rate of 77.3%, compared with 65.0% of Vanilla. | definition/direction/unit from same section | p. 10 (3 DATASET) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| On SimplerEnv, our minimal Vanilla design outperforms common baselines (π0, π0-FAST), though it is slightly below CogACT (61.8 vs. | comparison identity and matched condition | p. 25 (A.3.2 CLOSE-LOOP EVALUATION ON SIMPLERENV) |
| The results show that all RoboInterVLA variants consistently outperform the vanilla baseline across platforms, with the Modular configuration achieving the best overall accuracy among ... | comparison identity and matched condition | p. 25 (A.3.1 OPEN-LOOP CROSS-PLATFORM EVALUATION) |
| Nine Executor variants are evaluated: (a).Vanilla: omits any pretrained VLM from Planner, performing action learning only; (b-e).RoboInter-IC-E2E, EC-E2E, Te-Modular and Im-Modular are stated in ... | comparison identity and matched condition | p. 8 (3 DATASET) |
| (3) Vanilla: A from-scratch baseline without a pretrained Planner and without annotated intermediate representations. | comparison identity and matched condition | p. 18 (A.1.1 EXPERIMENTAL SETTING) |
| Its slightly larger ID→OOD drop compared to EC-E2E indicates that the asynchronous two-module design is somewhat more sensitive to distribution shift, yet still substantially ... | comparison identity and matched condition | p. 18 (A.1.1 EXPERIMENTAL SETTING) |
| We compare two settings: Oracle+Executor and RoboInter-Te-Modular. | comparison identity and matched condition | p. 22 (A.2.2 EXPERIMENT RESULTS FOR DATA SCALING LAW) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 5: Ablation of intermediate representation. We re- port OLS under multiple thresholds. Six representations are evaluated, where finer-grained categories yield larger gains. Variant ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| (3) Vanilla: A from-scratch baseline without a pretrained Planner and without annotated intermediate representations. | component/input/data sensitivity | p. 18 (A.1.1 EXPERIMENTAL SETTING) |
| All models are pretrained on the BridgeV2 without further post-training or finetuning prior to deployment, and all experiments are executed using the same real-world ... | component/input/data sensitivity | p. 26 (A.3.3 CLOSE-LOOP EVALUATION ON REAL-WORLD WIDOWX ROBOT) |
| 22 A.2.3 Ablation for Designs and Intermediate Representations Types of F-CoT . . | component/input/data sensitivity | p. 17 (A.2.2 Experiment Results for Data Scaling Law) |
| The Modular variant achieves strong real-world performance and competitive out-of-distribution (OOD) generalization. | component/input/data sensitivity | p. 18 (A.1.1 EXPERIMENTAL SETTING) |
| For real-world deployment, we apply practical acceleration strategies, including textual caching and chunked execution for EC-E2E, and asynchronous dual-frequency execution for the Modular variant. | component/input/data sensitivity | p. 22 (A.2.1 INFERENCE TIME ANALYSIS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address this gap, we propose the RoboInter Manipulation Suite, illustrated in Figure.1. | 60.0%) and achieves a higher average success rate (60.0% vs. | PDF body cue; verify exact table/figure and matched conditions | p. 18 (A.1.1 EXPERIMENTAL SETTING), p. 9 (3 DATASET), p. 25 (A.3.1 OPEN-LOOP CROSS-PLATFORM EVALUATION), p. 10 (3 DATASET), p. 18 (A.1.1 EXPERIMENTAL SETTING), p. 7 (3 DATASET) |
| Primary metric/result | The most significant improvement comes from Trace, which introduces dense, temporally grounded information and achieves the strongest overall performance. | numeric claim only at cited anchor | p. 9 (3 DATASET) |

- Numeric sentences retained from the body:
- **p. 5 / 3 DATASET - extractive PDF cue:** Published as a conference paper at ICLR 2026 frame where the robot arm contacts the manipulated object is also recorded.
- **p. 6 / 3 DATASET - extractive PDF cue:** Published as a conference paper at ICLR 2026 Subtasks The robot task is ‘drag the plate… Return the future 10 point of gripper Planner General ...
- **p. 18 / A.1.1 EXPERIMENTAL SETTING - extractive PDF cue:** To accommodate network latency, the control loop is limited to lower than 10 Hz, and demonstrations are collected using a SpaceMouse.
- **p. 25 / A.3.1 OPEN-LOOP CROSS-PLATFORM EVALUATION - extractive PDF cue:** Our dataset spans over 570 scenes across multiple robotic embodiments, forming a hybrid collection that is both cross-platform and cross-scene.
- **p. 25 / A.3.2 CLOSE-LOOP EVALUATION ON SIMPLERENV - extractive PDF cue:** The experiments are conducted across 12 tasks, including both Visual Matching and Visual Aggregation.
- **p. 46 / A.7.3 DETAILS OF VQA DATASET - extractive PDF cue:** Task Name Task Type Number Planning Task Temporal & Generation 82,939 Planning with Context Task Temporal & Generation 58,439 Planning Remaining Steps Task Temporal & ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 5: Real-World Experiments. The top charts present results from 15 in-distribution (ID) and 15 out-of-distribution (OOD) trials. The bottom panel illustrates the OOD ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | RoboInter-VLA demonstrates precise action generation (e.g., grasping a pen from the table while avoiding collision) and long-horizon capabilities, such as continuously cleaning the board. | p. 21 (A.1.3 MORE RESULTS AND VISUALIZATION) |
| body limitation/failure cue | The general trend confirms that explicit reasoning enhances robustness at the cost of slower inference, motivating future work on more efficient execution. | p. 22 (A.2.1 INFERENCE TIME ANALYSIS) |
| body limitation/failure cue | Because RoboInter-Data does not include action annotations for WidowX or Google robots, this constitutes a strictly cross-embodiment evaluation. | p. 25 (A.3.2 CLOSE-LOOP EVALUATION ON SIMPLERENV) |
| body limitation/failure cue | This approach can yield robust embodied perception and more accurate task-relevant visual cues. | p. 6 (3 DATASET) |
| body limitation/failure cue | The Planner exhibits enhanced understanding and generation for manipulation, strong general grounding abilities, and robust perception across diverse scenes. | p. 6 (3 DATASET) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| At inference time, we utilize a shorter CoT (only subtask, affordance box, and gripper box), as well as a caching mechanism that stores slowly ... | p. 18 (A.1.1 EXPERIMENTAL SETTING) |
| The base learning rate is 5 × 10-5, with no warmup and no weight decay. | p. 27 (A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR) |
| The RoboInter-IC-E2E Executor is trained with a global batch size of 128 and a per-device batch size of 8. | p. 27 (A.4.1 TRAINING DETAILS OF PLANNER AND EXECUTOR) |
| (2) π0 (Black et al., 2024): Fine-tuned from the official JAX checkpoints of the Droid dataset. | p. 18 (A.1.1 EXPERIMENTAL SETTING) |
| Video-based visual inputs are also used to summarize past events and predict feasible next steps. | p. 5 (3 DATASET) |
| Prompts condition on different amounts of prior information (e.g., past subtasks or overall instructions) and ask the model to predict the subsequent steps or ... | p. 5 (3 DATASET) |
| Each model consists of a base LLM, a vision encoder, and an MLP-based vision-language projector. | p. 6 (3 DATASET) |
| OLS is computed as the average value over 100K transitions from evaluation videos, ensuring statistical stability. | p. 8 (3 DATASET) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / Figure/Table caption - extractive PDF cue:** Figure 5: Real-World Experiments. The top charts present results from 15 in-distribution (ID) and 15 out-of-distribution (OOD) trials. The bottom panel illustrates the OOD test ...
- **p. 21 / A.1.3 MORE RESULTS AND VISUALIZATION - extractive PDF cue:** RoboInter-VLA demonstrates precise action generation (e.g., grasping a pen from the table while avoiding collision) and long-horizon capabilities, such as continuously cleaning the board.
- **p. 22 / A.2.1 INFERENCE TIME ANALYSIS - extractive PDF cue:** The general trend confirms that explicit reasoning enhances robustness at the cost of slower inference, motivating future work on more efficient execution.
- **p. 25 / A.3.2 CLOSE-LOOP EVALUATION ON SIMPLERENV - extractive PDF cue:** Because RoboInter-Data does not include action annotations for WidowX or Google robots, this constitutes a strictly cross-embodiment evaluation.
- **p. 6 / 3 DATASET - extractive PDF cue:** This approach can yield robust embodied perception and more accurate task-relevant visual cues.
- **p. 6 / 3 DATASET - extractive PDF cue:** The Planner exhibits enhanced understanding and generation for manipulation, strong general grounding abilities, and robust perception across diverse scenes.

- **PDF anchors reviewed:** datasets p. 26 (A.3.3 CLOSE-LOOP EVALUATION ON REAL-WORLD WIDOWX ROBOT), p. 5 (3 DATASET), p. 25 (A.3.1 OPEN-LOOP CROSS-PLATFORM EVALUATION), p. 6 (3 DATASET), p. 25 (A.3.2 CLOSE-LOOP EVALUATION ON SIMPLERENV), p. 27 (A.4.2 VQA BENCHMARKS), metrics p. 18 (A.1.1 EXPERIMENTAL SETTING), p. 18 (A.1.1 EXPERIMENTAL SETTING), p. 25 (A.3.2 CLOSE-LOOP EVALUATION ON SIMPLERENV), p. 25 (A.3.2 CLOSE-LOOP EVALUATION ON SIMPLERENV), p. 24 (A.2.4 DETAILED RESULTS OF PLANNER ON TEMPORAL ROBOINTER-VQA), p. 9 (3 DATASET), baselines p. 25 (A.3.2 CLOSE-LOOP EVALUATION ON SIMPLERENV), p. 25 (A.3.1 OPEN-LOOP CROSS-PLATFORM EVALUATION), p. 8 (3 DATASET), p. 18 (A.1.1 EXPERIMENTAL SETTING), p. 18 (A.1.1 EXPERIMENTAL SETTING), p. 22 (A.2.2 EXPERIMENT RESULTS FOR DATA SCALING LAW), results p. 18 (A.1.1 EXPERIMENTAL SETTING), p. 9 (3 DATASET), p. 25 (A.3.1 OPEN-LOOP CROSS-PLATFORM EVALUATION), p. 10 (3 DATASET), p. 18 (A.1.1 EXPERIMENTAL SETTING), p. 7 (3 DATASET).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
