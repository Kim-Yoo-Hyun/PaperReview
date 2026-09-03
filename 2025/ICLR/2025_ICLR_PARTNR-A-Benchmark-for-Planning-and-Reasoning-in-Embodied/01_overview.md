# PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (64 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=T5QLRRHyL1.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114714. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Robotics, Benchmark
- Official paper: https://openreview.net/forum?id=T5QLRRHyL1
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/114714
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (64 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Through systematic evaluation, we reveal critical insights into the current limitations of LLM-based planners, opening interesting future research directions.를 문제로 두고, To bridge this gap, we introduce Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR), a novel benchmark that evaluates the ability of embodied AI agents to collaborate with humans across a range ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** We present a benchmark for Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR) designed to study human-robot coordination in household activities.
- **p. 1 / ABSTRACT - extractive body cue:** PARTNR tasks exhibit characteristics of everyday tasks, such as spatial, temporal, and heterogeneous agent capability constraints.
- **p. 1 / ABSTRACT - extractive body cue:** We employ a semi-automated task generation pipeline using Large Language Models (LLMs), incorporating simulation-in-the-loop for the grounding and verification.
- **p. 1 / ABSTRACT - extractive body cue:** PARTNR stands as the largest benchmark of its kind, comprising 100,000 natural language tasks, spanning 60 houses and 5,819 unique objects.
- **p. 1 / ABSTRACT - extractive body cue:** We analyze state-of-the-art LLMs on PARTNR tasks, across the axes of planning, perception and skill execution.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Through systematic evaluation, we reveal critical insights into the current limitations of LLM-based planners, opening interesting future research directions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Curating such a benchmark of large-scale, natural language tasks with tailored evaluation functions presents significant challenges.

## Core Idea

- **p. 1 / 1 INTRODUCTION - extractive body cue:** To bridge this gap, we introduce Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR), a novel benchmark that evaluates the ability of embodied AI agents ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Instead, we propose a semi-automated approach using 1
- **p. 2 / 1 INTRODUCTION - extractive body cue:** LLM-based helper agents LLM Planner We propose modular LLM-based agent baselines to collaborate in our benchmark.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As PARTNR consists of natural language tasks and LLMs have shown strong results in planning (Yao et al., 2023; Ahn et al., 2022; Huang et ...
- **p. 34 / A.9.2 IMPLEMENTATION DETAILS - extractive body cue:** We train the model to predict, for every example, the action taken by the agent, which corresponds to the text after the </reserved_special_token_0>/ token.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** The finetuned model based on Llama-3.1-8B required an average of 0.53s per planning step.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** For all experiments, LLM inferrence is performed on two Nvidia A100 GPUs using the gpt-fast inference engine PyTorch (2023).
- **p. 34 / A.9.2 IMPLEMENTATION DETAILS - extractive body cue:** We train all models on 4 A100 GPUs, with a batch size of 2 per GPU.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | PARTNR consists of 100,000 natural language instructions paired with tailored evaluation functions, focusing on four task types: (1) constraint-free, where sub-tasks can be completed in any manner by either agent, (2) spatial ... | standardized observation, action, task state와 evaluation split | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| State/latent | PARTNR, consists, natural, language, instructions, paired, tailored, evaluation, functions, focusing, four, task | benchmark state/goal와 method decision | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/action | Beyond the conventional challenges of long-horizon planning, partially observed environments, and large state and action spaces, PARTNR emphasizes the need for effective collaboration. | policy/controller trajectory 또는 measured result | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective/outcome | success metric, robustness, generalization과 reproducibility | success metric, robustness, generalization과 reproducibility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 1 / 1 INTRODUCTION - extractive body cue:** To bridge this gap, we introduce Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR), a novel benchmark that evaluates the ability of embodied AI agents ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Instead, we propose a semi-automated approach using 1
- **p. 2 / 1 INTRODUCTION - extractive body cue:** LLM-based helper agents LLM Planner We propose modular LLM-based agent baselines to collaborate in our benchmark.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As PARTNR consists of natural language tasks and LLMs have shown strong results in planning (Yao et al., 2023; Ahn et al., 2022; Huang et ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 3: Human-in-the-Loop Evaluation. We evaluate the performance of a 2-person human team and human-LLM teams, comparing them to solo human performance on PARTNR tasks ...
- **p. 35 / Figure/Table caption - extractive body cue:** Table 11: Baseline results on PARTNR test set. We measure performance using simulation steps required to finish the episode, success rate and completion rate on ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Analysis of planner baselines in various settings. We compare performance using simula- tion steps, success rate and percent complete on the tasks, and ...
- **p. 37 / Figure/Table caption - extractive body cue:** Table 13: Task performance per task type. Average and standard errors of task success rate for episodes from the validation set categorized by task type. ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 10 (Figure/Table caption), p. 35 (Figure/Table caption) |
| Embodiment/environment | Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights for our trained neural network skills and fine-tuned large planning ... | hardware/simulator version and reset protocol | p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE), p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE) |
| Dataset/benchmark | After that, set the plants on the shelf next to each other." Evaluation Function Task Instruction Propositions: 0 is_inside(["toy_fire_truck_0"], ["toy_box_0"]) 1 is_inside(["toy_food_0"], ["toy_box_0"]) 2 is_on_top(["plant_0"], ["shelf ... | role, split, size and leakage | p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE), p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE), p. 16 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS) |
| Metric | Table 11: Baseline results on PARTNR test set. We measure performance using simulation steps required to finish the episode, success rate and completion rate on the tasks, and the average number of ... | definition, denominator, direction and uncertainty | p. 35 (Figure/Table caption), p. 9 (Figure/Table caption), p. 37 (Figure/Table caption) |
| Baseline/ablation | Released code includes our PARTNR benchmark tasks, metrics, baseline oracle skills, large planning model framework, and dataset generation utilities. | fair input/data/compute/action matching | p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE), p. 35 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 24 / Figure/Table caption - extractive body cue:** Table 8: Top three failure modes of 100k-scale task and evaluation generation reported for each task type. Failures of task generation are led by the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Analysis of planner baselines in various settings. We compare performance using simula- tion steps, success rate and percent complete on the tasks, and ...
- **p. 10 / 5 CONCLUSION - extractive body cue:** PARTNR serves as a challenging benchmark that highlights the substantial limitations of current models.
- **p. 38 / Figure/Table caption - extractive body cue:** Figure 14: HITL Interface. Participants control human and robot agents using keyboard/mouse controls to complete the PARTNR tasks. Each participant has access to their partner's ...
- **p. 15 / A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE - extractive body cue:** Each scene is manually adjusted by a human to ensure simulation robustness and minimize potential issues.
- **p. 15 / A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE - extractive body cue:** The marker sets indicate either a spread of surface points (for distance/occlusion checking) or the location of key points of interest such as faucets (for ...
- **p. 37 / Figure/Table caption - extractive body cue:** Figure 13: HITL on Web-browser. Our HITL sys- tem can be deployed on web browsers enabling large-scale collection. We adapt the existing human-in-the-loop (HITL) infrastructure ...

## Why Read It

Planning and control의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Through systematic evaluation, we reveal critical insights into the current limitations of LLM-based planners, opening interesting future research directions.를 문제로 두고, To bridge this gap, we introduce Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR), a novel benchmark that evaluates the ability of embodied AI agents to collaborate with humans across a range ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 34 (A.9.2 IMPLEMENTATION DETAILS), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
