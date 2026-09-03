# Evaluation - PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (64 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=T5QLRRHyL1; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114714. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (Figure/Table caption), p. 35 (Figure/Table caption), p. 9 (Figure/Table caption), p. 37 (Figure/Table caption), p. 39 (Figure/Table caption), p. 4 (Figure/Table caption)): Table 3: Human-in-the-Loop Evaluation. We evaluate the performance of a 2-person human team and human-LLM teams, comparing them to solo human performance on PARTNR tasks using metrics described in Section ...

## Evaluation Body Digest

- **p. 15 / A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE - extractive body cue:** Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights for our trained ...
- **p. 15 / A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE - extractive body cue:** Released code includes our PARTNR benchmark tasks, metrics, baseline oracle skills, large planning model framework, and dataset generation utilities.
- **p. 16 / A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE - extractive body cue:** After that, set the plants on the shelf next to each other." Evaluation Function Task Instruction Propositions: 0 is_inside(["toy_fire_truck_0"], ["toy_box_0"]) 1 is_inside(["toy_food_0"], ["toy_box_0"]) 2 is_on_top(["plant_0"], ...
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** The average wall time to complete and entire episode (planning steps for both agents and simulation time) was 36.0 minutes.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** For those experiments, simulation time and human agent inference time remained unchanged, giving a final wall time of 25.3 minutes per episode.
- **p. 35 / Figure/Table caption - extractive body cue:** Table 11: Baseline results on PARTNR test set. We measure performance using simulation steps required to finish the episode, success rate and completion rate on ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Analysis of planner baselines in various settings. We compare performance using simula- tion steps, success rate and percent complete on the tasks, and ...
- **p. 37 / Figure/Table caption - extractive body cue:** Table 13: Task performance per task type. Average and standard errors of task success rate for episodes from the validation set categorized by task type. ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE (p. 15); A.2 DATASET DETAILS AND ADDITIONAL ANALYSIS (p. 16); A.4 THE PARTNR EVALUATION SYSTEM (p. 19); A.4.1 EVALUATION PREDICATES (p. 19); A.4.5 EVALUATION METRICS (p. 22); A.4.6 EVALUATION FUNCTION GENERATION (p. 22); A.5.1 GENERATION ACCURACY FOR TASKS AND EVALUATIONS (p. 23); A.5.2 VISUALIZATION OF PARTNR TASKS AND EVALUATION FUNCTIONS (p. 25); A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS (p. 31); A.9.2 IMPLEMENTATION DETAILS (p. 34); A.10 ADDITIONAL RESULTS (p. 34); A.12 HUMAN-IN-THE-LOOP EVALUATION FOR PARTNR TASKS (p. 37).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Table 3: Human-in-the-Loop Evaluation. We evaluate the performance of a 2-person human team and human-LLM teams, comparing them to solo human performance on PARTNR ... | p. 10 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Table 11: Baseline results on PARTNR test set. We measure performance using simulation steps required to finish the episode, success rate and completion rate ... | p. 35 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Table 2: Analysis of planner baselines in various settings. We compare performance using simula- tion steps, success rate and percent complete on the tasks, ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Table 13: Task performance per task type. Average and standard errors of task success rate for episodes from the validation set categorized by task ... | p. 37 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Table 14: Human-in-the-Loop evaluation. We evaluate the performance of 2-person human teams and human-LLM teams, comparing them to solo human performance on PARTNR tasks ... | p. 39 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 15 / A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE - extractive body cue:** Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights for our trained ...
- **p. 15 / A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE - extractive body cue:** Released code includes our PARTNR benchmark tasks, metrics, baseline oracle skills, large planning model framework, and dataset generation utilities.
- **p. 16 / A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE - extractive body cue:** After that, set the plants on the shelf next to each other." Evaluation Function Task Instruction Propositions: 0 is_inside(["toy_fire_truck_0"], ["toy_box_0"]) 1 is_inside(["toy_food_0"], ["toy_box_0"]) 2 is_on_top(["plant_0"], ...
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** The average wall time to complete and entire episode (planning steps for both agents and simulation time) was 36.0 minutes.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** For those experiments, simulation time and human agent inference time remained unchanged, giving a final wall time of 25.3 minutes per episode.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: We present PARTNR, a benchmark for planning and reasoning in embodied multi-agent tasks, featuring 100,000 everyday tasks and evaluation functions generated semi-automatically, spanning ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1: Comparison to similar embodied benchmarks. We compare PARTNR to embodied AI benchmarks, focusing on natural language and multi-agent collaboration tasks. Comparison axes are ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: The PARTNR generation pipeline. Task and evaluation generators produce episodes, which are filtered and annotated for correctness. These episodes are then treated as ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Task and evaluation example. Language tasks have inherent complexity and ambiguity; both of which are supported by the structures of our evaluation functions. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Distribution of task types in PARTNR. The left plot displays the percentage of tasks with each characteristic. Constraint-free tasks by definition exclude the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Decentralized architecture. The hu- man and robot agents use a 2-layer hierarchical architecture, with high-level LLM planners that call low-level skills. Both agents ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Analysis of planner baselines in various settings. We compare performance using simula- tion steps, success rate and percent complete on the tasks, and ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 3: Human-in-the-Loop Evaluation. We evaluate the performance of a 2-person human team and human-LLM teams, comparing them to solo human performance on PARTNR tasks ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights for our ... | embodiment, simulator version and control stack | p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE), p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE) |
| Task/environment | Released code includes our PARTNR benchmark tasks, metrics, baseline oracle skills, large planning model framework, and dataset generation utilities. | reset, timeout, object/scene variation | p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE), p. 16 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 11: Baseline results on PARTNR test set. We measure performance using simulation steps required to finish the episode, success rate and completion rate ... | definition/direction/unit from same section | p. 35 (Figure/Table caption) |
| Table 2: Analysis of planner baselines in various settings. We compare performance using simula- tion steps, success rate and percent complete on the tasks, ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Table 13: Task performance per task type. Average and standard errors of task success rate for episodes from the validation set categorized by task ... | definition/direction/unit from same section | p. 37 (Figure/Table caption) |
| Table 3: Human-in-the-Loop Evaluation. We evaluate the performance of a 2-person human team and human-LLM teams, comparing them to solo human performance on PARTNR ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Table 14: Human-in-the-Loop evaluation. We evaluate the performance of 2-person human teams and human-LLM teams, comparing them to solo human performance on PARTNR tasks ... | definition/direction/unit from same section | p. 39 (Figure/Table caption) |
| Table 7: Manually-annotated generation accuracy of 100k-scale PARTNR tasks and evaluation functions. Altogether, we find that 83% of episodes are generated without any task ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Figure 1: We present PARTNR, a benchmark for planning and reasoning in embodied multi-agent tasks, featuring 100,000 everyday tasks and evaluation functions generated semi-automatically, ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Table 12: Analysis of collaboration characteristics for LLM agents. Average and standard errors for task offloading, extraneous effort, and exploration efficiency are reported over ... | definition/direction/unit from same section | p. 36 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Released code includes our PARTNR benchmark tasks, metrics, baseline oracle skills, large planning model framework, and dataset generation utilities. | comparison identity and matched condition | p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE) |
| Table 10: Baseline results on PARTNR validation set. We measure performance using simulation steps required to finish the episode, success rate and completion rate ... | comparison identity and matched condition | p. 35 (Figure/Table caption) |
| Table 2: Analysis of planner baselines in various settings. We compare performance using simula- tion steps, success rate and percent complete on the tasks, ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| The marker sets indicate either a spread of surface points (for distance/occlusion checking) or the location of key points of interest such as faucets ... | comparison identity and matched condition | p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE) |
| Additionally all baselines had a maximum timeout of 20000 simulation steps. | comparison identity and matched condition | p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS) |
| All decentralized baselines had a maximum timeout of 50 replanning calls, while centralized baselines had a maximum timeout of 100 replanning calls (to account ... | comparison identity and matched condition | p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1: We present PARTNR, a benchmark for planning and reasoning in embodied multi-agent tasks, featuring 100,000 everyday tasks and evaluation functions generated semi-automatically, ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Table 7: Manually-annotated generation accuracy of 100k-scale PARTNR tasks and evaluation functions. Altogether, we find that 83% of episodes are generated without any task ... | component/input/data sensitivity | p. 23 (Figure/Table caption) |
| Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights for our ... | component/input/data sensitivity | p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE) |
| Figure 9: PARTNR tasks visualized in PrediViz. The design distills the task and scene to only the components necessary for verification. In example task ... | component/input/data sensitivity | p. 26 (Figure/Table caption) |
| Figure 13: HITL on Web-browser. Our HITL sys- tem can be deployed on web browsers enabling large-scale collection. We adapt the existing human-in-the-loop (HITL) ... | component/input/data sensitivity | p. 37 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To bridge this gap, we introduce Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR), a novel benchmark that evaluates the ability of embodied AI ... | Table 3: Human-in-the-Loop Evaluation. We evaluate the performance of a 2-person human team and human-LLM teams, comparing them to solo human performance on PARTNR ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (Figure/Table caption), p. 35 (Figure/Table caption), p. 9 (Figure/Table caption), p. 37 (Figure/Table caption), p. 39 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Primary metric/result | Table 11: Baseline results on PARTNR test set. We measure performance using simulation steps required to finish the episode, success rate and completion rate ... | numeric claim only at cited anchor | p. 35 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 15 / A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE - extractive body cue:** We prepared 60 scenes divided into train, val, and test splits to support our experiments.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** Inference on LLama-3.1-70B (using tensor parallelism over two A100s), resulted in an average generation speed of 11.43 tokens/s.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** Each planning step required an average of 52 tokens resulting in a latency of 4.55 seconds per planning step.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** The finetuned model based on Llama-3.1-8B required an average of 0.53s per planning step.
- **p. 34 / A.9.2 IMPLEMENTATION DETAILS - extractive body cue:** The models are trained for 40,000 steps, which takes around 24 hours.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** Inference on LLama-3.1-70B (using tensor parallelism over two A100s), resulted in an average generation speed of 11.43 tokens/s.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 8: Top three failure modes of 100k-scale task and evaluation generation reported for each task type. Failures of task generation are led by ... | p. 24 (Figure/Table caption) |
| body limitation/failure cue | Table 2: Analysis of planner baselines in various settings. We compare performance using simula- tion steps, success rate and percent complete on the tasks, ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | PARTNR serves as a challenging benchmark that highlights the substantial limitations of current models. | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | Figure 14: HITL Interface. Participants control human and robot agents using keyboard/mouse controls to complete the PARTNR tasks. Each participant has access to their ... | p. 38 (Figure/Table caption) |
| body limitation/failure cue | Each scene is manually adjusted by a human to ensure simulation robustness and minimize potential issues. | p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE) |
| body limitation/failure cue | The marker sets indicate either a spread of surface points (for distance/occlusion checking) or the location of key points of interest such as faucets ... | p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train all models on 4 A100 GPUs, with a batch size of 2 per GPU. | p. 34 (A.9.2 IMPLEMENTATION DETAILS) |
| For those experiments, simulation time and human agent inference time remained unchanged, giving a final wall time of 25.3 minutes per episode. | p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS) |
| Additionally all baselines had a maximum timeout of 20000 simulation steps. | p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS) |
| The models are trained for 40,000 steps, which takes around 24 hours. | p. 34 (A.9.2 IMPLEMENTATION DETAILS) |
| Accompanying this paper, we will release the code and data necessary to reproduce our experiments. | p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE) |
| For the purpose of this submission, the anonymized code is included in the supplementary zip file. | p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 24 / Figure/Table caption - extractive body cue:** Table 8: Top three failure modes of 100k-scale task and evaluation generation reported for each task type. Failures of task generation are led by the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Analysis of planner baselines in various settings. We compare performance using simula- tion steps, success rate and percent complete on the tasks, and ...
- **p. 10 / 5 CONCLUSION - extractive body cue:** PARTNR serves as a challenging benchmark that highlights the substantial limitations of current models.
- **p. 38 / Figure/Table caption - extractive body cue:** Figure 14: HITL Interface. Participants control human and robot agents using keyboard/mouse controls to complete the PARTNR tasks. Each participant has access to their partner's ...
- **p. 15 / A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE - extractive body cue:** Each scene is manually adjusted by a human to ensure simulation robustness and minimize potential issues.
- **p. 15 / A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE - extractive body cue:** The marker sets indicate either a spread of surface points (for distance/occlusion checking) or the location of key points of interest such as faucets (for ...

- **Evidence anchors reviewed:** datasets p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE), p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE), p. 16 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS), metrics p. 35 (Figure/Table caption), p. 9 (Figure/Table caption), p. 37 (Figure/Table caption), p. 10 (Figure/Table caption), p. 39 (Figure/Table caption), p. 23 (Figure/Table caption), baselines p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE), p. 35 (Figure/Table caption), p. 9 (Figure/Table caption), p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS), results p. 10 (Figure/Table caption), p. 35 (Figure/Table caption), p. 9 (Figure/Table caption), p. 37 (Figure/Table caption), p. 39 (Figure/Table caption), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
