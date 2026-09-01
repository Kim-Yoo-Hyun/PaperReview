# Evaluation - PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (63 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=T5QLRRHyL1; PDF retrieval source: https://openreview.net/pdf/4bb6ff694eaca45e88773722cf73178602665bfd.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 32 (A.9 Implementation Details for ReAct Agents), p. 32 (A.9 Implementation Details for ReAct Agents), p. 32 (A.9 Implementation Details for ReAct Agents), p. 35 (A.10.2 Implementation Details), p. 10 (Method), p. 11 (Method)): Inference on LLama-3.1-70B (using tensor parallelism over two A100s), resulted in an average generation speed of 11.43 tokens/s.

## Evaluation Body Digest

- **p. 16 / A.1 Open-sourcing PARTNR Dataset and Codebase - extractive PDF cue:** Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights for our trained ...
- **p. 16 / A.1 Open-sourcing PARTNR Dataset and Codebase - extractive PDF cue:** Released code includes our PARTNR benchmark tasks, metrics, baseline oracle skills, large planning model framework, and dataset generation utilities.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** The average wall time to complete and entire episode (planning steps for both agents and simulation time) was 36.0 minutes.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** For those experiments, simulation time and human agent inference time remained unchanged, giving a final wall time of 25.3 minutes per episode.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** Inference on LLama-3.1-70B (using tensor parallelism over two A100s), resulted in an average generation speed of 11.43 tokens/s.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** Each planning step required an average of 52 tokens resulting in a latency of 4.55 seconds per planning step.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** The finetuned model based on Llama-3.1-8B required an average of 0.53s per planning step.
- **p. 35 / A.10.2 Implementation Details - extractive PDF cue:** The models are trained for 40,000 steps, which takes around 24 hours.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** A.1 Open-sourcing PARTNR Dataset and Codebase (p. 16); A.3 Dataset Details and Additional Analysis (p. 17); A.5 The PARTNR Evaluation System (p. 20); A.5.1 Evaluation Predicates (p. 20); A.5.5 Evaluation Metrics (p. 23); A.5.6 Evaluation Function Generation (p. 23); A.6.1 Generation Accuracy for Tasks and Evaluations (p. 24); A.6.2 Visualization of PARTNR Tasks and Evaluation Functions (p. 26); A.9 Implementation Details for ReAct Agents (p. 32); A.10.2 Implementation Details (p. 35); A.11 Additional Results (p. 35); A.13 Human-in-the-loop Evaluation for PARTNR tasks (p. 37).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| A.9 Implementation Details for ReAct Agents | BENCHMARK / DATASET | Inference on LLama-3.1-70B (using tensor parallelism over two A100s), resulted in an average generation speed of 11.43 tokens/s. | p. 32 (A.9 Implementation Details for ReAct Agents) |
| A.9 Implementation Details for ReAct Agents | BENCHMARK / DATASET | Each planning step required an average of 52 tokens resulting in a latency of 4.55 seconds per planning step. | p. 32 (A.9 Implementation Details for ReAct Agents) |
| A.9 Implementation Details for ReAct Agents | BENCHMARK / DATASET | The finetuned model based on Llama-3.1-8B required an average of 0.53s per planning step. | p. 32 (A.9 Implementation Details for ReAct Agents) |
| A.10.2 Implementation Details | BENCHMARK / DATASET | The models are trained for 40,000 steps, which takes around 24 hours. | p. 35 (A.10.2 Implementation Details) |
| Method | BENCHMARK / DATASET | We collect single-user and multi-user data on 1000 tasks from the validation and test set using this tool. | p. 10 (Method) |

## Dataset / Benchmark Role

- **p. 16 / A.1 Open-sourcing PARTNR Dataset and Codebase - extractive PDF cue:** Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights for our trained ...
- **p. 16 / A.1 Open-sourcing PARTNR Dataset and Codebase - extractive PDF cue:** Released code includes our PARTNR benchmark tasks, metrics, baseline oracle skills, large planning model framework, and dataset generation utilities.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** The average wall time to complete and entire episode (planning steps for both agents and simulation time) was 36.0 minutes.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** For those experiments, simulation time and human agent inference time remained unchanged, giving a final wall time of 25.3 minutes per episode.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights for our ... | embodiment, simulator version and control stack | p. 16 (A.1 Open-sourcing PARTNR Dataset and Codebase), p. 16 (A.1 Open-sourcing PARTNR Dataset and Codebase) |
| Task/environment | Released code includes our PARTNR benchmark tasks, metrics, baseline oracle skills, large planning model framework, and dataset generation utilities. | reset, timeout, object/scene variation | p. 16 (A.1 Open-sourcing PARTNR Dataset and Codebase), p. 32 (A.9 Implementation Details for ReAct Agents) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 10 (Method), p. 11 (Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights for our ... | definition/direction/unit from same section | p. 16 (A.1 Open-sourcing PARTNR Dataset and Codebase) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Released code includes our PARTNR benchmark tasks, metrics, baseline oracle skills, large planning model framework, and dataset generation utilities. | comparison identity and matched condition | p. 16 (A.1 Open-sourcing PARTNR Dataset and Codebase) |
| Additionally all baselines had a maximum timeout of 20000 simulation steps. | comparison identity and matched condition | p. 32 (A.9 Implementation Details for ReAct Agents) |
| All decentralized baselines had a maximum timeout of 50 replanning calls, while centralized baselines had a maximum timeout of 100 replanning calls (to account ... | comparison identity and matched condition | p. 32 (A.9 Implementation Details for ReAct Agents) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights for our ... | component/input/data sensitivity | p. 16 (A.1 Open-sourcing PARTNR Dataset and Codebase) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To bridge this gap, we introduce Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR), a novel benchmark that evaluates the ability of embodied AI ... | Inference on LLama-3.1-70B (using tensor parallelism over two A100s), resulted in an average generation speed of 11.43 tokens/s. | PDF body cue; verify exact table/figure and matched conditions | p. 32 (A.9 Implementation Details for ReAct Agents), p. 32 (A.9 Implementation Details for ReAct Agents), p. 32 (A.9 Implementation Details for ReAct Agents), p. 35 (A.10.2 Implementation Details), p. 10 (Method), p. 11 (Method) |
| Primary metric/result | Each planning step required an average of 52 tokens resulting in a latency of 4.55 seconds per planning step. | numeric claim only at cited anchor | p. 32 (A.9 Implementation Details for ReAct Agents) |

- Numeric sentences retained from the body:
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** Inference on LLama-3.1-70B (using tensor parallelism over two A100s), resulted in an average generation speed of 11.43 tokens/s.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** Each planning step required an average of 52 tokens resulting in a latency of 4.55 seconds per planning step.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** The finetuned model based on Llama-3.1-8B required an average of 0.53s per planning step.
- **p. 35 / A.10.2 Implementation Details - extractive PDF cue:** The models are trained for 40,000 steps, which takes around 24 hours.
- **p. 10 / Method - extractive PDF cue:** We collect single-user and multi-user data on 1000 tasks from the validation and test set using this tool.
- **p. 11 / Method - extractive PDF cue:** Success Rate ↑ Percent Complete ↑ Sim Steps ↓ Task Offloading ↑ Exploration Efficiency ↓ Extraneous Effort ↓ Single-user 0.93 ± 0.01 0.96 ± 0.00 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | PARTNR serves as a challenging benchmark that highlights the substantial limitations of current models. | p. 11 (5 Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train all models on 4 A100 GPUs, with a batch size of 2 per GPU. | p. 35 (A.10.2 Implementation Details) |
| For those experiments, simulation time and human agent inference time remained unchanged, giving a final wall time of 25.3 minutes per episode. | p. 32 (A.9 Implementation Details for ReAct Agents) |
| Additionally all baselines had a maximum timeout of 20000 simulation steps. | p. 32 (A.9 Implementation Details for ReAct Agents) |
| The models are trained for 40,000 steps, which takes around 24 hours. | p. 35 (A.10.2 Implementation Details) |
| Additionally, we measure the number of steps taken by each approach to complete 10 | p. 10 (Method) |
| This allows us to run at-scale evaluation of our tasks with 129 non-expert human participants. | p. 10 (Method) |
| In contrast, two humans working together complete the task faster than a single human (2369 steps vs. | p. 11 (Method) |
| When deployed with real humans-in-the-loop, the finetuned model is faster than ReAct at task completion (3443 steps with finetuned versus 4267 with ReAct). | p. 11 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 11 / 5 Conclusion - extractive PDF cue:** PARTNR serves as a challenging benchmark that highlights the substantial limitations of current models.

- **PDF anchors reviewed:** datasets p. 16 (A.1 Open-sourcing PARTNR Dataset and Codebase), p. 16 (A.1 Open-sourcing PARTNR Dataset and Codebase), p. 32 (A.9 Implementation Details for ReAct Agents), p. 32 (A.9 Implementation Details for ReAct Agents), metrics p. 16 (A.1 Open-sourcing PARTNR Dataset and Codebase), baselines p. 16 (A.1 Open-sourcing PARTNR Dataset and Codebase), p. 32 (A.9 Implementation Details for ReAct Agents), p. 32 (A.9 Implementation Details for ReAct Agents), results p. 32 (A.9 Implementation Details for ReAct Agents), p. 32 (A.9 Implementation Details for ReAct Agents), p. 32 (A.9 Implementation Details for ReAct Agents), p. 35 (A.10.2 Implementation Details), p. 10 (Method), p. 11 (Method).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
