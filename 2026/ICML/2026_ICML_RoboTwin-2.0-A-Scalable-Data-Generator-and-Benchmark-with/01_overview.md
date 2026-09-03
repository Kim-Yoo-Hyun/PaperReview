# RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=itonej9GIV.
> PDF retrieval source: https://openreview.net/pdf/7cbb20fa3292d18ddb89823a5e7c3df7e52a3eb3.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Robotics, Benchmark
- Official paper: https://openreview.net/forum?id=itonej9GIV
- Full-text retrieval: https://openreview.net/pdf/7cbb20fa3292d18ddb89823a5e7c3df7e52a3eb3.pdf
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 benchmark 문제를 이해하기 위해 읽는다. 본문은 First, they lack automated quality control: without an expert-level validation loop, many generated trajectories include execution failures or suboptimal grasps, which degrade policy learning.를 문제로 두고, In summary, our main contributions are as follows: (1) We develop an automated expert data generation framework that integrates multimodal large language models with simulation-in-theloop feedback to ensure high-quality, expert-level tr ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Simulation-based data synthesis has emerged as a powerful paradigm for enhancing real-world robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** However, existing synthetic datasets remain insufficient for robust bimanual manipulation due to two challenges: (1) the lack of an efficient, scalable data generation method for ...
- **p. 1 / Abstract - extractive body cue:** We present RoboTwin 2.0, a scalable simulation framework that enables automated.
- **p. 2 / Abstract - extractive body cue:** large-scale generation of diverse and realistic data, along with unified evaluation protocols for dual-arm manipulation.
- **p. 2 / Abstract - extractive body cue:** We first construct RoboTwin-OD, a largescale object library comprising 731 instances across 147 categories, each annotated with semantic and manipulation-relevant labels.
- **p. 2 / 1 Introduction - extractive body cue:** First, they lack automated quality control: without an expert-level validation loop, many generated trajectories include execution failures or suboptimal grasps, which degrade policy learning.
- **p. 2 / 1 Introduction - extractive body cue:** RoboTwin 2.0 integrates three key components: (1) an automated expert data generation pipeline that leverages multimodal large language models (MLLMs) and simulationin-the-loop feedback to iteratively ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** In summary, our main contributions are as follows: (1) We develop an automated expert data generation framework that integrates multimodal large language models with simulation-in-theloop ...
- **p. 2 / 1 Introduction - extractive body cue:** To address these challenges, we introduce RoboTwin 2.0, a scalable simulation-based data generation framework designed to produce high-quality, diverse, realistic, and interaction-rich datasets for bimanual ...
- **p. 2 / 1 Introduction - extractive body cue:** Building on these components, we introduce three new resources to support scalable research in bimanual manipulation: (1) the RoboTwin-OD asset library, comprising 731 annotated object ...
- **p. 3 / 2 Method - extractive body cue:** To address these limitations, we propose an automated expert data generation pipeline that integrates programmatic code synthesis with multimodal execution feedback (Fig.3).
- **p. 4 / 2 Method - extractive body cue:** This diagnostic capability enables the system to address root causes rather than merely responding to superficial execution errors.
- **p. 3 / 2 Method - extractive body cue:** Language Description Place the toy-car in basket and move basket Auto Expert Data Collection Code Gen Code Exec Images and Error Feedback Cluttered Table, Background, ...
- **p. 3 / 2 Method - extractive body cue:** The system adopts a closed-loop architecture with two agents: a code-generation agent and a vision-language model (VLM) observer.
- **p. 4 / 2 Method - extractive body cue:** Multiple trials are used to account for stochastic variations in simulation dynamics, robot controllers, and sensor noise.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Language Description Place the toy-car in basket and move basket Auto Expert Data Collection Code Gen Code Exec Images and Error Feedback Cluttered Table, Background, Light, Tabletop Height, Instruction Robust Robot Manipulation ... | standardized observation, action, task state와 evaluation split | p. 3 (2 Method), p. 2 (1 Introduction) |
| State/latent | Language, Description, Place, toy-car, basket, move, Auto, Expert, Data, Collection, Code, Gen | benchmark state/goal와 method decision | p. 3 (2 Method), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Output/action | RoboTwin 2.0 integrates three key components: (1) an automated expert data generation pipeline that leverages multimodal large language models (MLLMs) and simulationin-the-loop feedback to iteratively validate and refine task execution ... | policy/controller trajectory 또는 measured result | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (2 Method) |
| Objective/outcome | Each task is defined by a task name (e.g., Handover Block) and a natural language description of the objective. | success metric, robustness, generalization과 reproducibility | p. 4 (2 Method), p. 4 (2 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** In summary, our main contributions are as follows: (1) We develop an automated expert data generation framework that integrates multimodal large language models with simulation-in-theloop ...
- **p. 2 / 1 Introduction - extractive body cue:** To address these challenges, we introduce RoboTwin 2.0, a scalable simulation-based data generation framework designed to produce high-quality, diverse, realistic, and interaction-rich datasets for bimanual ...
- **p. 2 / 1 Introduction - extractive body cue:** Building on these components, we introduce three new resources to support scalable research in bimanual manipulation: (1) the RoboTwin-OD asset library, comprising 731 annotated object ...
- **p. 3 / 2 Method - extractive body cue:** To address these limitations, we propose an automated expert data generation pipeline that integrates programmatic code synthesis with multimodal execution feedback (Fig.3).
- **p. 4 / 2 Method - extractive body cue:** This diagnostic capability enables the system to address root causes rather than merely responding to superficial execution errors.
- **p. 8 / 4 Experiment - extractive body cue:** Results show that our method improves success rates, particularly for robots with constrained planning spaces, achieving an average improvement of 8.3% across all embodiments.
- **p. 9 / 4 Experiment - extractive body cue:** This also suggests that the low success rate of pretrained VLAs in simulation is not due to a Real-to-Sim gap, since we provide clean simulation ...
- **p. 9 / 4 Experiment - extractive body cue:** Stack Bowls Two 0.0% 0.0% 30.0% 41.0% 8.0% 55.0% 49.0% 62.0% Pick Dual Bottles 0.0% 0.0% 13.0% 12.0% 12.0% 15.0% 17.0% 7.0% Move Can Pot ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 8 (4 Experiment), p. 9 (4 Experiment) |
| Embodiment/environment | We design experiments to evaluate the effectiveness of RoboTwin 2.0 in three key aspects: (1) automating the generation of high-quality expert code for manipulation tasks; (2) improving policy robustness to environmental variation ... | hardware/simulator version and reset protocol | p. 7 (4 Experiment), p. 10 (4 Experiment) |
| Dataset/benchmark | This setup directly tests whether RoboTwin 2.0 enables robust policy generalization without additional real-world data from visually complex environments. | role, split, size and leakage | p. 7 (4 Experiment), p. 10 (4 Experiment), p. 10 (4 Experiment), p. 7 (50 Tasks for Data Generation and Benchmarking) |
| Metric | We evaluate performance with four metrics: ASR (Average Success Rate), Top5-ASR (success over the top-5 candidates per task), CR-Iter (average refinement iterations before termination), and Token (average number of tokens in generated ... | definition, denominator, direction and uncertainty | p. 8 (4 Experiment), p. 8 (4 Experiment), p. 9 (4 Experiment) |
| Baseline/ablation | Stack Bowls Two 0.0% 0.0% 30.0% 41.0% 8.0% 55.0% 49.0% 62.0% Pick Dual Bottles 0.0% 0.0% 13.0% 12.0% 12.0% 15.0% 17.0% 7.0% Move Can Pot 4.0% 0.0% 12.0% 21.0% 13.0% 35.0% 18.0% ... | fair input/data/compute/action matching | p. 9 (4 Experiment), p. 8 (4 Experiment), p. 8 (4 Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 12 / 6 Conclusion - extractive body cue:** Our system integrates MLLM-based task generation, embodiment-adaptive behavior synthesis, and comprehensive domain randomization to address key limitations in prior synthetic data generator.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Visualization of domain randomization and our texture library. Scene Clutter. To enhance robustness to environmental variation, we augment tabletop scenes with task-irrelevant distractors ...
- **p. 8 / 4 Experiment - extractive body cue:** Overall, three findings emerge: (1) vision-language feedback not only detects failures but also guides precise repairs; (2) architectural improvements in RoboTwin 2.0 accelerate convergence and ...
- **p. 12 / 6 Conclusion - extractive body cue:** RoboTwin 2.0 provides a foundation for unified benchmarks and scalable sim-to-real pipelines, with future work focusing on real-world deployment and multi-object task complexity.
- **p. 9 / 4 Experiment - extractive body cue:** These results demonstrate that our approach provides additional feasible grasp options that effectively mitigate the planning limitations of low-DoF manipulators.
- **p. 9 / 4 Experiment - extractive body cue:** Stack Bowls Two 0.0% 0.0% 30.0% 41.0% 8.0% 55.0% 49.0% 62.0% Pick Dual Bottles 0.0% 0.0% 13.0% 12.0% 12.0% 15.0% 17.0% 7.0% Move Can Pot ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Overview of RoboTwin 2.0. RoboTwin 2.0 is a scalable framework for bimanual manipu- lation, integrating an expert data generation pipeline with a 50-task ...

## Why Read It

VLA and generalist robot policies의 benchmark 문제를 이해하기 위해 읽는다. 본문은 First, they lack automated quality control: without an expert-level validation loop, many generated trajectories include execution failures or suboptimal grasps, which degrade policy learning.를 문제로 두고, In summary, our main contributions are as follows: (1) We develop an automated expert data generation framework that integrates multimodal large language models with simulation-in-theloop feedback to ensure high-quality, expert-level tr ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (2 Method), p. 3 (2 Method), p. 4 (2 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
