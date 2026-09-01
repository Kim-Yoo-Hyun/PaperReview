# Evaluation - MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=3eTr9dGwJv; PDF retrieval source: https://openreview.net/pdf/3f888689e829f4172ae97d1dfac5f1b62ddb30c3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (6 EXPERIMENTS), p. 22 (Figure/Table caption), p. 11 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 10 (6 EXPERIMENTS)): As shown in Figure 6, our system achieves an 80% success rate in graph generation, 87.5% success rate in planning (conditioned on correct graphs), and an overall task success rate ...

## Evaluation Body Digest

- **p. 19 / A.4.1 BENCHMARK DESIGN - extractive body cue:** To rigorously evaluate spatial-functional reasoning and task planning capabilities, we design a comprehensive multi-choice VQA benchmark based on the scenes and tasks in our dataset.
- **p. 17 / A.1.1 REAL-WORLD DATASET SOURCE AND COLLECTION - extractive body cue:** To further enrich the dataset, we incorporated samples from two public benchmarks, OpenFunGraph (Zhang et al., 2025) and SceneFun3D (Delitzas et al., 2024), both of ...
- **p. 18 / A.1.4 MULTI-ASPECT STATISTICS OF THE TRAINING DATASET - extractive body cue:** Our dataset consists of approximately 1,050 subgraphs and 6278 multi-view RGB images, collected across more than 350 diverse household scenes and encompassing 93 distinct task ...
- **p. 10 / 6 EXPERIMENTS - extractive body cue:** Our real-world evaluations show that MomaGraph-R1 delivers robust scene understanding and task planning even in unseen scenarios, while remaining directly compatible with standard mobile humanoid ...
- **p. 10 / 6 EXPERIMENTS - extractive body cue:** To validate the effectiveness of our model in real-world settings, we deploy on the RobotEra Q5, a bimanual humanoid platform with a mobile base.
- **p. 18 / A.1.4 MULTI-ASPECT STATISTICS OF THE TRAINING DATASET - extractive body cue:** 9, the dataset spans four common household room types and captures the correspondence between action types and functional categories, reflecting the diversity and richness of ...
- **p. 11 / 6 EXPERIMENTS - extractive body cue:** Published as a conference paper at ICLR 2026 6.4 QUANTITATIVE REAL-ROBOT EVALUATION To provide rigorous quantitative validation of our system's robustness, we conduct a comprehensive ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** 6.1 BENCHMARK EVALUATION FOR EMBODIED TASK PLANNING We compare the performance of our MomaGraph-R1 with other models across all task tiers in MomaGraph-Bench to rigorously ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 6 EXPERIMENTS (p. 8); A.1 MOMAGRAPH-SCENES DATASET (p. 17); A.1.1 REAL-WORLD DATASET SOURCE AND COLLECTION (p. 17); A.1.3 DATASET ANNOTATION AND FORMAT (p. 17); A.1.4 MULTI-ASPECT STATISTICS OF THE TRAINING DATASET (p. 18); A.4 MOMAGRAPH BENCHMARK (p. 19); A.4.1 BENCHMARK DESIGN (p. 19).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 6 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 6, our system achieves an 80% success rate in graph generation, 87.5% success rate in planning (conditioned on correct graphs), ... | p. 11 (6 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5: Comparison of our RL-based training with SFT and ICL baselines. Our method achieves substantially better performance on both benchmarks. As shown in ... | p. 22 (Figure/Table caption) |
| 6 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | These results demonstrate that MomaGraph remains robust across multiple reasoning and execution stages, achieving a 70% overall success rate on a complex multi-step task. | p. 11 (6 EXPERIMENTS) |
| 6 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | By enforcing multiview consistency, our method significantly improves correspondence reasoning across all opensource models. | p. 9 (6 EXPERIMENTS) |
| 6 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our MomaGraph-R1 achieves performance on par with closed-source giants like Claude-4.5-Sonnet and GPT-5, while clearly surpassing all leading opensource VLMs. | p. 9 (6 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 19 / A.4.1 BENCHMARK DESIGN - extractive body cue:** To rigorously evaluate spatial-functional reasoning and task planning capabilities, we design a comprehensive multi-choice VQA benchmark based on the scenes and tasks in our dataset.
- **p. 17 / A.1.1 REAL-WORLD DATASET SOURCE AND COLLECTION - extractive body cue:** To further enrich the dataset, we incorporated samples from two public benchmarks, OpenFunGraph (Zhang et al., 2025) and SceneFun3D (Delitzas et al., 2024), both of ...
- **p. 18 / A.1.4 MULTI-ASPECT STATISTICS OF THE TRAINING DATASET - extractive body cue:** Our dataset consists of approximately 1,050 subgraphs and 6278 multi-view RGB images, collected across more than 350 diverse household scenes and encompassing 93 distinct task ...
- **p. 10 / 6 EXPERIMENTS - extractive body cue:** Our real-world evaluations show that MomaGraph-R1 delivers robust scene understanding and task planning even in unseen scenarios, while remaining directly compatible with standard mobile humanoid ...
- **p. 10 / 6 EXPERIMENTS - extractive body cue:** To validate the effectiveness of our model in real-world settings, we deploy on the RobotEra Q5, a bimanual humanoid platform with a mobile base.
- **p. 18 / A.1.4 MULTI-ASPECT STATISTICS OF THE TRAINING DATASET - extractive body cue:** 9, the dataset spans four common household room types and captures the correspondence between action types and functional categories, reflecting the diversity and richness of ...
- **p. 11 / 6 EXPERIMENTS - extractive body cue:** Published as a conference paper at ICLR 2026 6.4 QUANTITATIVE REAL-ROBOT EVALUATION To provide rigorous quantitative validation of our system's robustness, we conduct a comprehensive ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** 6.1 BENCHMARK EVALUATION FOR EMBODIED TASK PLANNING We compare the performance of our MomaGraph-R1 with other models across all task tiers in MomaGraph-Bench to rigorously ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Overview of the MomaGraph. Given a task instruction, MomaGraph constructs a task- specific scene graph that highlights relevant objects and parts along with ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Direct planning often fails even for strong closed-source models like GPT-5, producing wrong actions or missing key steps, while our Graph-then-Plan approach with ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Comparison between MomaGraph-R1and LLaVA variants across task tiers. Models T1 T2 T3 T4 Overall Models
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: MomaGraph captures state changes in the environment and dynamically updates the task-specific scene graph accordingly, enabling the graph to evolve as interactions occur ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Examples of evaluation Multi-Choices VQA tasks in the MomaGraph-Bench. We show- case example questions covering six core reasoning capabilities. Beyond these core capabilities, ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Performance comparison on the MomaGraph-Bench. We report accuracy (%) across four tiers (T1-T4) and the overall score, with and without graph-based reasoning. Type ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Performance comparison on the BLINK and MomaGraph-Bench. By enforcing multi- view consistency, our method significantly improves correspondence reasoning across all open- source models.
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 5: Real Robot experiments on the RobotEra Q5 with a D455, demonstrating four household tasks that require spatial, functional, and part-level interactive elements reasoning ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To rigorously evaluate spatial-functional reasoning and task planning capabilities, we design a comprehensive multi-choice VQA benchmark based on the scenes and tasks in our ... | embodiment, simulator version and control stack | p. 19 (A.4.1 BENCHMARK DESIGN), p. 17 (A.1.1 REAL-WORLD DATASET SOURCE AND COLLECTION) |
| Task/environment | To further enrich the dataset, we incorporated samples from two public benchmarks, OpenFunGraph (Zhang et al., 2025) and SceneFun3D (Delitzas et al., 2024), both ... | reset, timeout, object/scene variation | p. 17 (A.1.1 REAL-WORLD DATASET SOURCE AND COLLECTION), p. 18 (A.1.4 MULTI-ASPECT STATISTICS OF THE TRAINING DATASET) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 6 (4 METHOD), p. 5 (4 METHOD) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (4 METHOD), p. 3 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This evaluation includes success rates and failure analysis across different stages to validate overall system performance under realistic, sequential conditions (see Figure 6). | definition/direction/unit from same section | p. 11 (6 EXPERIMENTS) |
| Figure 13: Training reward curves during MomaGraph-R1 training. correctness of the benchmark, all generated questions and answers undergo several rounds of manual verification, during ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| These results demonstrate that MomaGraph remains robust across multiple reasoning and execution stages, achieving a 70% overall success rate on a complex multi-step task. | definition/direction/unit from same section | p. 11 (6 EXPERIMENTS) |
| We report accuracy (%) across four tiers (T1-T4) and the overall score, with and without graph-based reasoning. | definition/direction/unit from same section | p. 9 (6 EXPERIMENTS) |
| Published as a conference paper at ICLR 2026 Table 4: DAPO Training Configuration Parameter Value Model Configuration Base Model Qwen2.5-VL-7B-Instruct Mixed Precision bfloat16 Training ... | definition/direction/unit from same section | p. 21 (A.4.1 BENCHMARK DESIGN) |
| Table 6: Sensitivity analysis of reward weights (wa, wf, wl) in our DAPO training. The model's performance remains stable across different weight configurations. As ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Notably, MomaGraph-R1 delivers a +11.4% relative improvement over its base model (Qwen2.5-VL-7B) under w/ Graph, highlighting the effectiveness of reinforcement learning with graph-based rewards. | definition/direction/unit from same section | p. 9 (6 EXPERIMENTS) |
| This combination underscores the strength of our model and its practicality for real-world deployment. | definition/direction/unit from same section | p. 10 (6 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Across all models, the w/ Graph setting consistently outperforms the w/o Graph baseline, demonstrating that explicitly structuring task-oriented scene graphs provides a tangible benefit ... | comparison identity and matched condition | p. 9 (6 EXPERIMENTS) |
| Our MomaGraph-R1 achieves state-of-the-art performance among open-source VLMs, leading by 3.8% on BLINK and 4.8% on our correspondence benchmark compared to the best competing ... | comparison identity and matched condition | p. 10 (6 EXPERIMENTS) |
| Table 5: Comparison of our RL-based training with SFT and ICL baselines. Our method achieves substantially better performance on both benchmarks. As shown in ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |
| Figure 14: Validation reward curves during MomaGraph-R1 training. B ADDITIONAL ABLATION STUDIES B.1 COMPARISON WITH SFT AND ICL BASELINES To validate our choice of ... | comparison identity and matched condition | p. 21 (Figure/Table caption) |
| 6.1 BENCHMARK EVALUATION FOR EMBODIED TASK PLANNING We compare the performance of our MomaGraph-R1 with other models across all task tiers in MomaGraph-Bench to ... | comparison identity and matched condition | p. 8 (6 EXPERIMENTS) |
| As task complexity increases from Tier 1 to Tier 4, the performance of most open-source baselines drops sharply, reflecting their limited ability to generalize ... | comparison identity and matched condition | p. 9 (6 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We report accuracy (%) across four tiers (T1-T4) and the overall score, with and without graph-based reasoning. | component/input/data sensitivity | p. 9 (6 EXPERIMENTS) |
| Table 1: Comparison between MomaGraph-R1and LLaVA variants across task tiers. Models T1 T2 T3 T4 Overall Models | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Figure 13: Training reward curves during MomaGraph-R1 training. correctness of the benchmark, all generated questions and answers undergo several rounds of manual verification, during ... | component/input/data sensitivity | p. 20 (Figure/Table caption) |
| Figure 14: Validation reward curves during MomaGraph-R1 training. B ADDITIONAL ABLATION STUDIES B.1 COMPARISON WITH SFT AND ICL BASELINES To validate our choice of ... | component/input/data sensitivity | p. 21 (Figure/Table caption) |
| Table 6: Sensitivity analysis of reward weights (wa, wf, wl) in our DAPO training. The model's performance remains stable across different weight configurations. As ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| Closed-source models still maintain the highest absolute performance, benefiting from larger-scale pretraining and proprietary data. | component/input/data sensitivity | p. 9 (6 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial and functional ... | As shown in Figure 6, our system achieves an 80% success rate in graph generation, 87.5% success rate in planning (conditioned on correct graphs), ... | PDF body cue; verify exact table/figure and matched conditions | p. 11 (6 EXPERIMENTS), p. 22 (Figure/Table caption), p. 11 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 10 (6 EXPERIMENTS) |
| Primary metric/result | Table 5: Comparison of our RL-based training with SFT and ICL baselines. Our method achieves substantially better performance on both benchmarks. As shown in ... | numeric claim only at cited anchor | p. 22 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 11 / 6 EXPERIMENTS - extractive body cue:** As shown in Figure 6, our system achieves an 80% success rate in graph generation, 87.5% success rate in planning (conditioned on correct graphs), and ...
- **p. 21 / A.4.1 BENCHMARK DESIGN - extractive body cue:** Published as a conference paper at ICLR 2026 Table 4: DAPO Training Configuration Parameter Value Model Configuration Base Model Qwen2.5-VL-7B-Instruct Mixed Precision bfloat16 Training Setup ...
- **p. 7 / 4 METHOD - extractive body cue:** Our dataset consists of approximately 1,050 task-oriented subgraphs and 6278 multi-view RGB images, collected from a combination of manually collected real-world data, re-annotated existing datasets ...
- **p. 8 / 4 METHOD - extractive body cue:** MomaGraph-Bench is formulated as a multi-choice VQA task which comprises 294 diverse indoor scenes with 1,446 multi-view images, featuring 352 task-oriented scene graphs spanning 1,315 ...
- **p. 19 / A.2 TRAINING DETAILS - extractive body cue:** We train our model using 8× 80GB A100 GPUs for approximately 13 hours based on the EasyR1 (Zheng et al., 2025b) training framework.
- **p. 19 / A.3 TRAINING CURVE - extractive body cue:** The format reward quickly reaches 1.0 within the first 25 steps, showing the model rapidly learns to produce valid JSON-structured outputs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 6: Quantitative real-robot evaluation. (a) Environment setup of the real-robot experiment. (b) Failure analysis illustrating success/failure rates across different reasoning stages. Task Setup. ... | p. 11 (Figure/Table caption) |
| body limitation/failure cue | This work addresses to the fundamental limitations of existing scene graphs for embodied agents: reliance on a single type of relationship, inability to adapt ... | p. 11 (7 CONCLUSION) |
| body limitation/failure cue | Figure 2: Direct planning often fails even for strong closed-source models like GPT-5, producing wrong actions or missing key steps, while our Graph-then-Plan approach ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Moreover, since the benchmark is formulated as a multi-choice VQA task with clearly defined correct answers, it does not require complex evaluation metrics. | p. 20 (A.4.1 BENCHMARK DESIGN) |
| body limitation/failure cue | In contrast, MomaGraph-R1 exhibits a much smaller degradation, preserving strong performance in Tier 3 and Tier 4. | p. 9 (6 EXPERIMENTS) |
| body limitation/failure cue | Our real-world evaluations show that MomaGraph-R1 delivers robust scene understanding and task planning even in unseen scenarios, while remaining directly compatible with standard mobile ... | p. 10 (6 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Published as a conference paper at ICLR 2026 Table 4: DAPO Training Configuration Parameter Value Model Configuration Base Model Qwen2.5-VL-7B-Instruct Mixed Precision bfloat16 Training ... | p. 21 (A.4.1 BENCHMARK DESIGN) |
| MomaGraph-R1 processes these observations together with the task instruction to generate a task-specific subgraph, which explicitly encodes the relevant objects and their spatial-functional relationships, ... | p. 10 (6 EXPERIMENTS) |
| Turn on the light closest to the remote so I can find it and turn on the monitor to watch." To assess system robustness, ... | p. 11 (6 EXPERIMENTS) |
| As shown in Figure 6, our system achieves an 80% success rate in graph generation, 87.5% success rate in planning (conditioned on correct graphs), ... | p. 11 (6 EXPERIMENTS) |
| The format reward quickly reaches 1.0 within the first 25 steps, showing the model rapidly learns to produce valid JSON-structured outputs. | p. 19 (A.3 TRAINING CURVE) |
| ET s encodes the spatial relationships among these nodes, and ET f captures their functional relationships. | p. 5 (4 METHOD) |
| We compute intersection-over-union similarity for task-relevant objects in NT , where N pred T and N gt T denote the predicted and ground truth ... | p. 5 (4 METHOD) |
| Published as a conference paper at ICLR 2026 where wa, wf, and wl are hyperparameters controlling the relative importance of each component. | p. 6 (4 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 11 / Figure/Table caption - extractive body cue:** Figure 6: Quantitative real-robot evaluation. (a) Environment setup of the real-robot experiment. (b) Failure analysis illustrating success/failure rates across different reasoning stages. Task Setup. We ...
- **p. 11 / 7 CONCLUSION - extractive body cue:** This work addresses to the fundamental limitations of existing scene graphs for embodied agents: reliance on a single type of relationship, inability to adapt to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Direct planning often fails even for strong closed-source models like GPT-5, producing wrong actions or missing key steps, while our Graph-then-Plan approach with ...
- **p. 20 / A.4.1 BENCHMARK DESIGN - extractive body cue:** Moreover, since the benchmark is formulated as a multi-choice VQA task with clearly defined correct answers, it does not require complex evaluation metrics.
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** In contrast, MomaGraph-R1 exhibits a much smaller degradation, preserving strong performance in Tier 3 and Tier 4.
- **p. 10 / 6 EXPERIMENTS - extractive body cue:** Our real-world evaluations show that MomaGraph-R1 delivers robust scene understanding and task planning even in unseen scenarios, while remaining directly compatible with standard mobile humanoid ...

- **PDF anchors reviewed:** datasets p. 19 (A.4.1 BENCHMARK DESIGN), p. 17 (A.1.1 REAL-WORLD DATASET SOURCE AND COLLECTION), p. 18 (A.1.4 MULTI-ASPECT STATISTICS OF THE TRAINING DATASET), p. 10 (6 EXPERIMENTS), p. 10 (6 EXPERIMENTS), p. 18 (A.1.4 MULTI-ASPECT STATISTICS OF THE TRAINING DATASET), metrics p. 11 (6 EXPERIMENTS), p. 20 (Figure/Table caption), p. 11 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 21 (A.4.1 BENCHMARK DESIGN), p. 22 (Figure/Table caption), baselines p. 9 (6 EXPERIMENTS), p. 10 (6 EXPERIMENTS), p. 22 (Figure/Table caption), p. 21 (Figure/Table caption), p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), results p. 11 (6 EXPERIMENTS), p. 22 (Figure/Table caption), p. 11 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 10 (6 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
