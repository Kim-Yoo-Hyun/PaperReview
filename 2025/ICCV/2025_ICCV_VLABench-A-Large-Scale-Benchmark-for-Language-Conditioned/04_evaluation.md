# Evaluation - VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (3.3. Benchmark), p. 6 (3.3. Benchmark), p. 6 (3.4. Dataset Construction), p. 5 (3.3. Benchmark), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption)): In addition to the success rate (SR), considering the long-horizon nature and high difficulty level of our tasks, we introduce the intention score (IS) and progress score (PS) for more ...

## Evaluation Body Digest

- **p. 6 / 3.4. Dataset Construction - extractive body cue:** Following the approach of previous benchmarks built on Mujoco [38, 47], the dataset is stored in the same format, with similar visual rendering quality and ...
- **p. 5 / 3.3. Benchmark - extractive body cue:** The evaluation episodes use objects seen in the training set, with minimal differences. - Track 2: Cross-category visual generalization.
- **p. 5 / 3.3. Benchmark - extractive body cue:** The evaluation episodes use unseen categories of objects as the target entity for evaluation. - Track 3: Common sense application.
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** During the data construction process, we introduced diverse task variants and domain randomization across different episodes of the same task to ensure the diversity of ...
- **p. 6 / 3.3. Benchmark - extractive body cue:** The progress score refers to the completion level of subtasks in a long-horizon task and serves as a softer process supervision metric compared to the ...
- **p. 5 / 3.3. Benchmark - extractive body cue:** In addition to the success rate (SR), considering the long-horizon nature and high difficulty level of our tasks, we introduce the intention score (IS) and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Evaluation pipeline for VLMs. Step 1: Sample the required four-view images, as well as those segmented with numerical information, from the simulation. Meanwhile, ...
- **p. 5 / 3.3. Benchmark - extractive body cue:** Intention score is a useful soft metric measuring the correctness trend in selecting the target object for the operation especially when sub-tasks are not yet ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 3.3. Benchmark (p. 4); 3.4. Dataset Construction (p. 6); 4. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3.3. Benchmark | BENCHMARK / DATASET | In addition to the success rate (SR), considering the long-horizon nature and high difficulty level of our tasks, we introduce the intention score (IS) ... | p. 5 (3.3. Benchmark) |
| 3.3. Benchmark | BENCHMARK / DATASET | The progress score refers to the completion level of subtasks in a long-horizon task and serves as a softer process supervision metric compared to ... | p. 6 (3.3. Benchmark) |
| 3.4. Dataset Construction | BENCHMARK / DATASET | Subsequently, the selected skills generate trajectories using RRT [29], with quaternion interpolation achieved through spherical linear interpolation. | p. 6 (3.4. Dataset Construction) |
| 3.3. Benchmark | BENCHMARK / DATASET | Intention score is a useful soft metric measuring the correctness trend in selecting the target object for the operation especially when sub-tasks are not ... | p. 5 (3.3. Benchmark) |
| Figure/Table caption | BENCHMARK / DATASET | Table 2. Overall experiment result of 6 evaluation tracks of fine-tuned VLAs. The detailed result of each task is reported in Table 9. above, ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 3.4. Dataset Construction - extractive body cue:** Following the approach of previous benchmarks built on Mujoco [38, 47], the dataset is stored in the same format, with similar visual rendering quality and ...
- **p. 5 / 3.3. Benchmark - extractive body cue:** The evaluation episodes use objects seen in the training set, with minimal differences. - Track 2: Cross-category visual generalization.
- **p. 5 / 3.3. Benchmark - extractive body cue:** The evaluation episodes use unseen categories of objects as the target entity for evaluation. - Track 3: Common sense application.
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** During the data construction process, we introduced diverse task variants and domain randomization across different episodes of the same task to ensure the diversity of ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Overview of VLABench. VLABench is a large-scale language-conditioned manipulation benchmark to evaluate the compre- hensive skill learning and generalization ability of action policies ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Comparison of popular benchmarks in robot learning. SemLang: semantically non-template rich language instructions. LogiRea- son: task logic and relevant information reasoning. Knowledge: tasks ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. Task examples in each dimension. The first row showcases examples of primitive tasks from Section 3.1, while the second row presents examples of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Evaluation pipeline for VLMs. Step 1: Sample the required four-view images, as well as those segmented with numerical information, from the simulation. Meanwhile, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Overall experiment result of 6 evaluation tracks of fine-tuned VLAs. The detailed result of each task is reported in Table 9. above, we ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Evaluation progress score for Voxposer and CoPA. Vox- poser w/o refers to the version without visual perception, where ground truth labels are directly ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Radar charts depicting the performance of all VLM mod- els across six dimensions. The reason why only GLM-4V-9B is evaluated in a zero-shot ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Following the approach of previous benchmarks built on Mujoco [38, 47], the dataset is stored in the same format, with similar visual rendering quality ... | embodiment, simulator version and control stack | p. 6 (3.4. Dataset Construction), p. 5 (3.3. Benchmark) |
| Task/environment | The evaluation episodes use objects seen in the training set, with minimal differences. - Track 2: Cross-category visual generalization. | reset, timeout, object/scene variation | p. 5 (3.3. Benchmark), p. 5 (3.3. Benchmark) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 8 (4.3. Comprehensive Ability of VLMs), p. 7 (4.2. Zero-shot Ability of Agent) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The progress score refers to the completion level of subtasks in a long-horizon task and serves as a softer process supervision metric compared to ... | definition/direction/unit from same section | p. 6 (3.3. Benchmark) |
| In addition to the success rate (SR), considering the long-horizon nature and high difficulty level of our tasks, we introduce the intention score (IS) ... | definition/direction/unit from same section | p. 5 (3.3. Benchmark) |
| Figure 3. Evaluation pipeline for VLMs. Step 1: Sample the required four-view images, as well as those segmented with numerical information, from the simulation. ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Intention score is a useful soft metric measuring the correctness trend in selecting the target object for the operation especially when sub-tasks are not ... | definition/direction/unit from same section | p. 5 (3.3. Benchmark) |
| Figure 4. Evaluation progress score for Voxposer and CoPA. Vox- poser w/o refers to the version without visual perception, where ground truth labels are ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| VLABench organizes evaluations into three categories: assessments of pretrained or fine-tuned visionlanguage-action (VLA) models, heuristic workflows that integrate foundation models with various algorithms, and ... | definition/direction/unit from same section | p. 4 (3.3. Benchmark) |
| Table 2. Overall experiment result of 6 evaluation tracks of fine-tuned VLAs. The detailed result of each task is reported in Table 9. above, ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 5. Radar charts depicting the performance of all VLM mod- els across six dimensions. The reason why only GLM-4V-9B is evaluated in a ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The progress score refers to the completion level of subtasks in a long-horizon task and serves as a softer process supervision metric compared to ... | comparison identity and matched condition | p. 6 (3.3. Benchmark) |
| Table 1. Comparison of popular benchmarks in robot learning. SemLang: semantically non-template rich language instructions. LogiRea- son: task logic and relevant information reasoning. Knowledge: ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Figure 4. Evaluation progress score for Voxposer and CoPA. Vox- poser w/o refers to the version without visual perception, where ground truth labels are ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| During the data construction process, we introduced diverse task variants and domain randomization across different episodes of the same task to ensure the diversity ... | component/input/data sensitivity | p. 6 (3.4. Dataset Construction) |
| Figure 4. Evaluation progress score for Voxposer and CoPA. Vox- poser w/o refers to the version without visual perception, where ground truth labels are ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Pretrained VLAs are expected to possess robust generalization and versatility similar to LLMs. | component/input/data sensitivity | p. 6 (4.1. Generalization Ability of VLAs) |
| VLABench organizes evaluations into three categories: assessments of pretrained or fine-tuned visionlanguage-action (VLA) models, heuristic workflows that integrate foundation models with various algorithms, and ... | component/input/data sensitivity | p. 4 (3.3. Benchmark) |
| Building upon Track 1, replace the instructions with unseen and more complex ones. - Track 5: Cross-domain behavior transferability. | component/input/data sensitivity | p. 5 (3.3. Benchmark) |
| The evaluation tasks are replaced with ones that differ from those in the training set, but require similar actions. - Track 6: Long-horizon task ... | component/input/data sensitivity | p. 5 (3.3. Benchmark) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We summarize contributions as follows: • We propose VLABench, the first benchmark designed to comprehensively evaluate the capabilities of VLAs and VLMs in robotics ... | In addition to the success rate (SR), considering the long-horizon nature and high difficulty level of our tasks, we introduce the intention score (IS) ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (3.3. Benchmark), p. 6 (3.3. Benchmark), p. 6 (3.4. Dataset Construction), p. 5 (3.3. Benchmark), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | The progress score refers to the completion level of subtasks in a long-horizon task and serves as a softer process supervision metric compared to ... | numeric claim only at cited anchor | p. 6 (3.3. Benchmark) |

- Numeric sentences retained from the body:
- **p. 6 / 3.3. Benchmark - extractive body cue:** The red part represents the error output of the model, where the red solid arrows represent the dependencies generated by the error, and red dashed ...
- **p. 7 / Model - extractive body cue:** We then assessed the models across 50 episodes for each task, resulting in a total of 250 trials per track.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | To enhance sample efficiency, reject sampling and failure-triggered early termination are applied. | p. 6 (3.4. Dataset Construction) |
| body limitation/failure cue | We hope that VLABench will inspire both the future research on robotics pertaining recipe and promote more robust VLA architectures development. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 5. Radar charts depicting the performance of all VLM mod- els across six dimensions. The reason why only GLM-4V-9B is evaluated in a ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | We also extend the evaluation to cover various skills and long-horizon tasks to assess the overall capability and execution robustness of the workflow. | p. 5 (3.3. Benchmark) |
| body limitation/failure cue | Pretrained VLAs are expected to possess robust generalization and versatility similar to LLMs. | p. 6 (4.1. Generalization Ability of VLAs) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Show me on the placemat Original RGBs Visual Prompted RGBs To generate the skill sequence based on the provided task: ### Task Instruction:… ### ... | p. 6 (3.3. Benchmark) |
| We then assessed the models across 50 episodes for each task, resulting in a total of 250 trials per track. | p. 7 (Model) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 3.4. Dataset Construction - extractive body cue:** To enhance sample efficiency, reject sampling and failure-triggered early termination are applied.
- **p. 8 / 5. Conclusion - extractive body cue:** We hope that VLABench will inspire both the future research on robotics pertaining recipe and promote more robust VLA architectures development.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Radar charts depicting the performance of all VLM mod- els across six dimensions. The reason why only GLM-4V-9B is evaluated in a zero-shot ...
- **p. 5 / 3.3. Benchmark - extractive body cue:** We also extend the evaluation to cover various skills and long-horizon tasks to assess the overall capability and execution robustness of the workflow.
- **p. 6 / 4.1. Generalization Ability of VLAs - extractive body cue:** Pretrained VLAs are expected to possess robust generalization and versatility similar to LLMs.

- **Evidence anchors reviewed:** datasets p. 6 (3.4. Dataset Construction), p. 5 (3.3. Benchmark), p. 5 (3.3. Benchmark), p. 6 (3.4. Dataset Construction), metrics p. 6 (3.3. Benchmark), p. 5 (3.3. Benchmark), p. 6 (Figure/Table caption), p. 5 (3.3. Benchmark), p. 8 (Figure/Table caption), p. 4 (3.3. Benchmark), baselines p. 6 (3.3. Benchmark), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 5 (3.3. Benchmark), p. 6 (3.3. Benchmark), p. 6 (3.4. Dataset Construction), p. 5 (3.3. Benchmark), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
