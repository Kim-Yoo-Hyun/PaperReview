# VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Benchmark, long-horizon
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 benchmark 문제를 이해하기 위해 읽는다. 본문은 The second task further intensifies the difficulty, requiring the robot to decompose the task into subtasks and execute the steps to operate a coffee machine-a long-horizon challenge that has previously been difficult ...를 문제로 두고, We summarize contributions as follows: • We propose VLABench, the first benchmark designed to comprehensively evaluate the capabilities of VLAs and VLMs in robotics manipulation tasks, covering multiple dimensions such as skills, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** General-purposed embodied agents are designed to understand the users' natural instructions or intentions and act precisely to complete universal tasks.
- **p. 1 / Abstract - extractive body cue:** Recently, methods based on foundation models especially Vision-LanguageAction models (VLAs) have shown a substantial potential to solve language-conditioned manipulation (LCM) tasks well.
- **p. 1 / Abstract - extractive body cue:** However, existing benchmarks do not adequately meet the needs of VLAs and relative algorithms.
- **p. 1 / Abstract - extractive body cue:** To better define such general-purpose tasks in the context of LLMs and advance the research in VLAs, we present VLABench, an open-source benchmark for evaluating ...
- **p. 1 / Abstract - extractive body cue:** VLABench provides 100 carefully designed categories of tasks, with strong randomization in each category of task and a total of 2000+ objects.
- **p. 2 / 1. Introduction - extractive body cue:** The second task further intensifies the difficulty, requiring the robot to decompose the task into subtasks and execute the steps to operate a coffee machine-a ...
- **p. 2 / 1. Introduction - extractive body cue:** This automated data construction approach facilitates future research on pretraining robotics data. • Our experiments demonstrate that current pre-trained VLAs have yet to exhibit the ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We summarize contributions as follows: • We propose VLABench, the first benchmark designed to comprehensively evaluate the capabilities of VLAs and VLMs in robotics manipulation ...
- **p. 2 / 1. Introduction - extractive body cue:** To better define the types of language-conditioned manipulation tasks suited for foundation models and provide a standardized evaluation suite to advance robotics research, we introduce ...
- **p. 8 / 4.3. Comprehensive Ability of VLMs - extractive body cue:** This dataset consists of a complex set of tasks designed to assess the VLM's ability to perceive visual stimuli and comprehend verbal instructions.
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** During the data construction process, we introduced diverse task variants and domain randomization across different episodes of the same task to ensure the diversity of ...
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** As human teleoperation is timeconsuming and not scalable [38, 47], we developed an efficient, scalable automated data collection pipeline based on our custom skill library.
- **p. 7 / Model - extractive body cue:** We also discuss in detail the potential issues with current VLAs, such as multimodal data co-training and model architecture designs.
- **p. 7 / 4.2. Zero-shot Ability of Agent - extractive body cue:** For our evaluation of foundation model-based algorithms, we reviewed two state-of-the-art frameworks, Voxposer [25] and CoPA [24], and the comparison results are shown in Figure ...
- **p. 8 / 4.2. Zero-shot Ability of Agent - extractive body cue:** The reason why only GLM-4V-9B is evaluated in a zero-shot setting is that it does not support multigraph inference, which is required for the other ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The strong generalization capabilities has inspired two main approaches in language-conditioned manipulation: pre-training visionlanguage-action models using large-scale robotics data, as demonstrated by RT-2 and Palm-E [5, 14, 50], and ... | standardized observation, action, task state와 evaluation split | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | strong, generalization, capabilities, inspired, main, approaches, language-conditioned, manipulation, pre-training, visionlanguage-action, models, large-scale | benchmark state/goal와 method decision | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 8 (4.3. Comprehensive Ability of VLMs) |
| Output/action | Such tasks require agents to master multiple capabilities: interpreting natural language instructions, understanding complex environments, making decisions, formulating plans, and executing precise actions. | policy/controller trajectory 또는 measured result | p. 2 (1. Introduction), p. 8 (4.3. Comprehensive Ability of VLMs), p. 7 (4.2. Zero-shot Ability of Agent) |
| Objective/outcome | The final trajectory is smoothed using a Bezier curve to optimize path quality. | success metric, robustness, generalization과 reproducibility | p. 6 (3.4. Dataset Construction), p. 6 (3.4. Dataset Construction), p. 7 (Model) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We summarize contributions as follows: • We propose VLABench, the first benchmark designed to comprehensively evaluate the capabilities of VLAs and VLMs in robotics manipulation ...
- **p. 2 / 1. Introduction - extractive body cue:** To better define the types of language-conditioned manipulation tasks suited for foundation models and provide a standardized evaluation suite to advance robotics research, we introduce ...
- **p. 8 / 4.3. Comprehensive Ability of VLMs - extractive body cue:** This dataset consists of a complex set of tasks designed to assess the VLM's ability to perceive visual stimuli and comprehend verbal instructions.
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** During the data construction process, we introduced diverse task variants and domain randomization across different episodes of the same task to ensure the diversity of ...
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** As human teleoperation is timeconsuming and not scalable [38, 47], we developed an efficient, scalable automated data collection pipeline based on our custom skill library.
- **p. 5 / 3.3. Benchmark - extractive body cue:** In addition to the success rate (SR), considering the long-horizon nature and high difficulty level of our tasks, we introduce the intention score (IS) and ...
- **p. 6 / 3.3. Benchmark - extractive body cue:** The progress score refers to the completion level of subtasks in a long-horizon task and serves as a softer process supervision metric compared to the ...
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** Subsequently, the selected skills generate trajectories using RRT [29], with quaternion interpolation achieved through spherical linear interpolation.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 5 (3.3. Benchmark), p. 6 (3.3. Benchmark) |
| Embodiment/environment | Following the approach of previous benchmarks built on Mujoco [38, 47], the dataset is stored in the same format, with similar visual rendering quality and trajectory accuracy. | hardware/simulator version and reset protocol | p. 6 (3.4. Dataset Construction), p. 5 (3.3. Benchmark) |
| Dataset/benchmark | The evaluation episodes use unseen categories of objects as the target entity for evaluation. - Track 3: Common sense application. | role, split, size and leakage | p. 6 (3.4. Dataset Construction), p. 5 (3.3. Benchmark), p. 5 (3.3. Benchmark), p. 6 (3.4. Dataset Construction) |
| Metric | The progress score refers to the completion level of subtasks in a long-horizon task and serves as a softer process supervision metric compared to the success rate. | definition, denominator, direction and uncertainty | p. 6 (3.3. Benchmark), p. 5 (3.3. Benchmark), p. 6 (Figure/Table caption) |
| Baseline/ablation | The progress score refers to the completion level of subtasks in a long-horizon task and serves as a softer process supervision metric compared to the success rate. | fair input/data/compute/action matching | p. 6 (3.3. Benchmark), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 3.4. Dataset Construction - extractive body cue:** To enhance sample efficiency, reject sampling and failure-triggered early termination are applied.
- **p. 8 / 5. Conclusion - extractive body cue:** We hope that VLABench will inspire both the future research on robotics pertaining recipe and promote more robust VLA architectures development.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Radar charts depicting the performance of all VLM mod- els across six dimensions. The reason why only GLM-4V-9B is evaluated in a zero-shot ...
- **p. 5 / 3.3. Benchmark - extractive body cue:** We also extend the evaluation to cover various skills and long-horizon tasks to assess the overall capability and execution robustness of the workflow.
- **p. 6 / 4.1. Generalization Ability of VLAs - extractive body cue:** Pretrained VLAs are expected to possess robust generalization and versatility similar to LLMs.

## Why Read It

VLA and generalist robot policies의 benchmark 문제를 이해하기 위해 읽는다. 본문은 The second task further intensifies the difficulty, requiring the robot to decompose the task into subtasks and execute the steps to operate a coffee machine-a long-horizon challenge that has previously been difficult ...를 문제로 두고, We summarize contributions as follows: • We propose VLABench, the first benchmark designed to comprehensively evaluate the capabilities of VLAs and VLMs in robotics manipulation tasks, covering multiple dimensions such as skills, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 7 (Model), p. 7 (4.2. Zero-shot Ability of Agent), p. 8 (4.2. Zero-shot Ability of Agent), p. 6 (3.4. Dataset Construction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
