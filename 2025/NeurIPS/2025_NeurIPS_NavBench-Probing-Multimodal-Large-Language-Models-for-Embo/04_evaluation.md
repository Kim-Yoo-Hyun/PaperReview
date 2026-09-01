# Evaluation - NavBench: Probing Multimodal Large Language Models for Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=nf8PKQKtl2; PDF retrieval source: https://openreview.net/pdf/1ef1a313c6a3eea3eea8cfe4ac568866df673dec.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (5.3 Discussion), p. 8 (Figure/Table caption), p. 9 (5.3 Discussion), p. 10 (5.3 Discussion), p. 8 (C Progress Level), p. 10 (5.3 Discussion)): As shown in Table 2, the presence of map information consistently improves success rates, with the largest gain observed under medium difficulty, yielding an increase of 4.86 percentage points.

## Evaluation Body Digest

- **p. 10 / 5.3 Discussion - extractive PDF cue:** Real-World Validation To assess the feasibility of our real-world deployment pipeline, we conduct a pilot study in an indoor environment using GPT-4o and Qwen2.5-VL-7B, the ...
- **p. 7 / C Progress Level - extractive PDF cue:** For real-world deployment, we integrate our pipeline with a dual-arm composite mobile robot equipped with an Intel RealSense D435 camera and a Water Drop 2 ...
- **p. 7 / C Progress Level - extractive PDF cue:** To demonstrate the real-world feasibility of MLLM-guided embodied navigation, we implement a modular pipeline that complements our benchmark evaluation, as illustrated in Figure 5.
- **p. 9 / C Progress Level - extractive PDF cue:** Among open-source models, Qwen2.5-VL-7B achieves the best overall performance (45.26%, 21.77%), approaching GPT-4o-mini (46.42%, 27.99%) and demonstrating potential for practical deployment in real-world robotics.
- **p. 9 / 5.3 Discussion - extractive PDF cue:** Effect of Map Information on Action Decisions Although our benchmark evaluations assume no access to map information, reflecting real-world constraints, we investigate whether providing map ...
- **p. 8 / C Progress Level - extractive PDF cue:** Evaluation Metrics Our benchmark includes both multiple-choice reasoning and embodied navigation execution tasks.
- **p. 8 / C Progress Level - extractive PDF cue:** Success Rate (SR) measures the percentage of episodes where the target object is visible from the agent's final viewpoint, defined as being within a 3-meter ...
- **p. 10 / 5.3 Discussion - extractive PDF cue:** These results show that both can handle simple navigation tasks in real-world settings.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.3 Discussion | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 2, the presence of map information consistently improves success rates, with the largest gain observed under medium difficulty, yielding an ... | p. 9 (5.3 Discussion) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7: Model performance on Local Observation-Action Reasoning. Evaluation Metrics Our benchmark includes both multiple-choice reasoning and embodied naviga- tion execution tasks. For multiple-choice ... | p. 8 (Figure/Table caption) |
| 5.3 Discussion | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 7, models show consistent performance across both, with GPT-4o clearly outperforming all others, consistent with its strong results in Navigation ... | p. 9 (5.3 Discussion) |
| 5.3 Discussion | EMPIRICAL / REAL-ROBOT OR HARDWARE | Their success trends mirror execution performance in Table 1, where both models outperform others in their categories. | p. 10 (5.3 Discussion) |
| C Progress Level | EMPIRICAL / REAL-ROBOT OR HARDWARE | Among closed models, o4-mini achieves the highest comprehension average (59.66%) and maintains competitive execution performance (28.98%). | p. 8 (C Progress Level) |

## Dataset / Benchmark Role

- **p. 10 / 5.3 Discussion - extractive PDF cue:** Real-World Validation To assess the feasibility of our real-world deployment pipeline, we conduct a pilot study in an indoor environment using GPT-4o and Qwen2.5-VL-7B, the ...
- **p. 7 / C Progress Level - extractive PDF cue:** For real-world deployment, we integrate our pipeline with a dual-arm composite mobile robot equipped with an Intel RealSense D435 camera and a Water Drop 2 ...
- **p. 7 / C Progress Level - extractive PDF cue:** To demonstrate the real-world feasibility of MLLM-guided embodied navigation, we implement a modular pipeline that complements our benchmark evaluation, as illustrated in Figure 5.
- **p. 9 / C Progress Level - extractive PDF cue:** Among open-source models, Qwen2.5-VL-7B achieves the best overall performance (45.26%, 21.77%), approaching GPT-4o-mini (46.42%, 27.99%) and demonstrating potential for practical deployment in real-world robotics.
- **p. 9 / 5.3 Discussion - extractive PDF cue:** Effect of Map Information on Action Decisions Although our benchmark evaluations assume no access to map information, reflecting real-world constraints, we investigate whether providing map ...
- **p. 8 / C Progress Level - extractive PDF cue:** Evaluation Metrics Our benchmark includes both multiple-choice reasoning and embodied navigation execution tasks.
- **p. 8 / C Progress Level - extractive PDF cue:** Success Rate (SR) measures the percentage of episodes where the target object is visible from the agent's final viewpoint, defined as being within a 3-meter ...
- **p. 10 / 5.3 Discussion - extractive PDF cue:** These results show that both can handle simple navigation tasks in real-world settings.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: NavBench evaluates MLLMs across three comprehension tasks and a step-by-step execution task, assessing their ability to understand navigation behavior, track progress, reason about ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Illustration of the Navigation Comprehension task. employ prompt-based guidance for instruction following [51, 52, 53, 54]. These approaches reduce reliance on task-specific training ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: NavBench construction pipeline and statistics. (a) QA generation for comprehension tasks at global, progress, and local levels. (b) Execution pipeline combining automatic difficulty ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Radar chart of average complexity scores across cognitive, spatial, and execution dimensions for different difficulty levels. Difficulty Categorization Based on the final scores, ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Overview of the real-world embodied navigation pipeline. To demonstrate the real-world feasibility of MLLM-guided embodied navigation, we implement a modular pipeline that complements ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Performance comparison on Navigation Comprehension and Execution.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: Model Performance under Different Instruction Perturbations.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 7: Model performance on Local Observation-Action Reasoning. Evaluation Metrics Our benchmark includes both multiple-choice reasoning and embodied naviga- tion execution tasks. For multiple-choice questions, ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Real-World Validation To assess the feasibility of our real-world deployment pipeline, we conduct a pilot study in an indoor environment using GPT-4o and Qwen2.5-VL-7B, ... | embodiment, simulator version and control stack | p. 10 (5.3 Discussion), p. 7 (C Progress Level) |
| Task/environment | For real-world deployment, we integrate our pipeline with a dual-arm composite mobile robot equipped with an Intel RealSense D435 camera and a Water Drop ... | reset, timeout, object/scene variation | p. 7 (C Progress Level), p. 7 (C Progress Level) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 4 (C Progress Level) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (C Progress Level), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 7: Model performance on Local Observation-Action Reasoning. Evaluation Metrics Our benchmark includes both multiple-choice reasoning and embodied naviga- tion execution tasks. For multiple-choice ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| As shown in Table 2, the presence of map information consistently improves success rates, with the largest gain observed under medium difficulty, yielding an ... | definition/direction/unit from same section | p. 9 (5.3 Discussion) |
| Map SR SPL Avg Gain Easy ✗ 67.36 54.31 60.84 - ✓ 70.14 54.11 62.13 +1.29 Med. ✗ 41.67 35.71 38.69 - ✓ 46.53 ... | definition/direction/unit from same section | p. 9 (C Progress Level) |
| Avg Accuracy SR SPL SR SPL SR SPL GPT-4o 51.33 42.90 65.80 53.34 67.36 54.31 41.67 35.71 27.78 21.15 41.33 GPT-4o + CoT 60.42 ... | definition/direction/unit from same section | p. 10 (5.3 Discussion) |
| Figure 1: NavBench evaluates MLLMs across three comprehension tasks and a step-by-step execution task, assessing their ability to understand navigation behavior, track progress, reason ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 2: Illustration of the Navigation Comprehension task. employ prompt-based guidance for instruction following [51, 52, 53, 54]. These approaches reduce reliance on task-specific ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Success Rate (SR) measures the percentage of episodes where the target object is visible from the agent's final viewpoint, defined as being within a ... | definition/direction/unit from same section | p. 8 (C Progress Level) |
| Each model is tested on 10 cases, achieving success rates of 60% and 40%, respectively. | definition/direction/unit from same section | p. 10 (5.3 Discussion) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in Figure 7, models show consistent performance across both, with GPT-4o clearly outperforming all others, consistent with its strong results in Navigation ... | comparison identity and matched condition | p. 9 (5.3 Discussion) |
| Their success trends mirror execution performance in Table 1, where both models outperform others in their categories. | comparison identity and matched condition | p. 10 (5.3 Discussion) |
| Table 3: Performance comparison with and without CoT prompting. | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| Figure 1: NavBench evaluates MLLMs across three comprehension tasks and a step-by-step execution task, assessing their ability to understand navigation behavior, track progress, reason ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Table 1: Performance comparison on Navigation Comprehension and Execution. | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Using GPT-4o, we compare performance with and without map input across different difficulty levels. | comparison identity and matched condition | p. 9 (5.3 Discussion) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Effect of Map Information on Action Decisions Although our benchmark evaluations assume no access to map information, reflecting real-world constraints, we investigate whether providing ... | component/input/data sensitivity | p. 9 (5.3 Discussion) |
| Avg Accuracy SR SPL SR SPL SR SPL GPT-4o 51.33 42.90 65.80 53.34 67.36 54.31 41.67 35.71 27.78 21.15 41.33 GPT-4o + CoT 60.42 ... | component/input/data sensitivity | p. 10 (5.3 Discussion) |
| Figure 1: NavBench evaluates MLLMs across three comprehension tasks and a step-by-step execution task, assessing their ability to understand navigation behavior, track progress, reason ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Using GPT-4o, we compare performance with and without map input across different difficulty levels. | component/input/data sensitivity | p. 9 (5.3 Discussion) |
| Table 3: Performance comparison with and without CoT prompting. | component/input/data sensitivity | p. 10 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are as follows: (1) We introduce NavBench, a benchmark for evaluating MLLMs in embodied navigation under zero-shot settings. | As shown in Table 2, the presence of map information consistently improves success rates, with the largest gain observed under medium difficulty, yielding an ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (5.3 Discussion), p. 8 (Figure/Table caption), p. 9 (5.3 Discussion), p. 10 (5.3 Discussion), p. 8 (C Progress Level), p. 10 (5.3 Discussion) |
| Primary metric/result | Figure 7: Model performance on Local Observation-Action Reasoning. Evaluation Metrics Our benchmark includes both multiple-choice reasoning and embodied naviga- tion execution tasks. For multiple-choice ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / C Progress Level - extractive PDF cue:** Normalization Each raw complexity score Φ is normalized to the range r1, 9s using a non-linear mapping: ˆΦ " round ˆ 1 ` 8 ¨ ...
- **p. 10 / 5.3 Discussion - extractive PDF cue:** Test samples are grouped by length into short (1-2 steps), medium (3-4), and long (5+).
- **p. 1 / Abstract - extractive PDF cue:** NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and local observation-action reasoning, ...
- **p. 3 / 1 Introduction - extractive PDF cue:** The benchmark includes 432 navigation cases across 72 scenes.
- **p. 4 / C Progress Level - extractive PDF cue:** 3 Benchmark Design 3.1 Task Formulation We evaluate the navigation capabilities of MLLMs by decomposing the task into two core components: Navigation Comprehension, which assesses ...
- **p. 6 / C Progress Level - extractive PDF cue:** We collect 500 examples for each format, yielding a total of 1,000 samples.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This suggests execution failures often stem from temporal and spatial reasoning limitations, reinforcing the diagnostic value of NavBench. | p. 10 (5.3 Discussion) |
| body limitation/failure cue | Based on thought traces and action sequences, we identify four common error types: (a) Incorrect Plan: the plan misaligns with the instruction; (b) Misaligned ... | p. 10 (5.3 Discussion) |
| body limitation/failure cue | The models' failure in this setting highlights their limited ability to reason about temporal order within complex instructions. | p. 9 (5.3 Discussion) |
| body limitation/failure cue | In particular, Progress Estimation remains a consistent weakness across models; aside from GPT-4o (42.90%), all others perform poorly, highlighting current MLLMs' limitations in temporal ... | p. 9 (C Progress Level) |
| body limitation/failure cue | All physical experiments are conducted in a controlled indoor lab to assess robustness and feasibility. | p. 7 (C Progress Level) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation Details Proprietary models are accessed via APIs, while open-source models are deployed using vLLM [64] and lmdeploy [65] on a single NVIDIA A6000 ... | p. 7 (C Progress Level) |
| (a) (b) (c) Execution Based on the instruction, what steps should I take to reach the goal? | p. 2 (1 Introduction) |
| Step-by-step Navigation Comprehension - Progress Level Given the steps taken so far, how far along am I in the instruction? | p. 2 (1 Introduction) |
| (c) Benchmark statistics, including comprehension (comp.) task distribution, QA counts, and execution statistics (e.g., instruction length, steps, distance). simulator setup centers on abstracted decision-making, ... | p. 5 (C Progress Level) |
| Navigation Comprehension Source Raw Datasets R2R / RxR … Step A1 Extract Multimodal Navigation Data Step A2 Navigation Execution Sample Navigation Episodes MatterPort3D Simulator ... | p. 5 (C Progress Level) |
| These features are computed from agent poses and scene connectivity data. | p. 6 (C Progress Level) |
| The score is computed as: Φexecution " γ1 ¨ logp1 ` Nq ` γ2 ¨ logp1 ` Tq ` γ3 ¨ F ` γ4 ... | p. 6 (C Progress Level) |
| Difficulty Categorization Based on the final scores, each case is categorized into one of three levels, as illustrated in Figure 4: • Easy (score ... | p. 7 (C Progress Level) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5.3 Discussion - extractive PDF cue:** This suggests execution failures often stem from temporal and spatial reasoning limitations, reinforcing the diagnostic value of NavBench.
- **p. 10 / 5.3 Discussion - extractive PDF cue:** Based on thought traces and action sequences, we identify four common error types: (a) Incorrect Plan: the plan misaligns with the instruction; (b) Misaligned Action: ...
- **p. 9 / 5.3 Discussion - extractive PDF cue:** The models' failure in this setting highlights their limited ability to reason about temporal order within complex instructions.
- **p. 9 / C Progress Level - extractive PDF cue:** In particular, Progress Estimation remains a consistent weakness across models; aside from GPT-4o (42.90%), all others perform poorly, highlighting current MLLMs' limitations in temporal reasoning.
- **p. 7 / C Progress Level - extractive PDF cue:** All physical experiments are conducted in a controlled indoor lab to assess robustness and feasibility.

- **PDF anchors reviewed:** datasets p. 10 (5.3 Discussion), p. 7 (C Progress Level), p. 7 (C Progress Level), p. 9 (C Progress Level), p. 9 (5.3 Discussion), p. 8 (C Progress Level), metrics p. 8 (Figure/Table caption), p. 9 (5.3 Discussion), p. 9 (C Progress Level), p. 10 (5.3 Discussion), p. 2 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 9 (5.3 Discussion), p. 10 (5.3 Discussion), p. 10 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (5.3 Discussion), results p. 9 (5.3 Discussion), p. 8 (Figure/Table caption), p. 9 (5.3 Discussion), p. 10 (5.3 Discussion), p. 8 (C Progress Level), p. 10 (5.3 Discussion).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
