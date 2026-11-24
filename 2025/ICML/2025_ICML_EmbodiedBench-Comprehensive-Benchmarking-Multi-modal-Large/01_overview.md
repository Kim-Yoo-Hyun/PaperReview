# EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (56 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v267/yang25f.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/164956. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: Rui Yang, Hanyang Chen, Junyu Zhang, Mark Zhao, Cheng Qian, Kangrui Wang, Qineng Wang, Teja Venkat Koripella, Marziyeh Movahedi, Manling Li, Heng Ji, Huan Zhang, Tong Zhang
- Primary track: Benchmarks and Datasets
- Tier: REFERENCE
- Tags: Benchmark
- Official paper: https://proceedings.mlr.press/v267/yang25f.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25f/yang25f.pdf
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (56 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

EmbodiedBench는 시각 입력을 받는 언어 모델이 고수준 가사 계획부터 저수준 이동·조작까지 어느 수준에서 수행할 수 있는지 평가한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/yang25f/yang25f.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Leveraging Multi-modal Large Language Models (MLLMs) to create embodied agents offers a promising avenue for tackling real-world tasks.
- **p. 1 / Abstract - extractive body cue:** While language-centric embodied agents have garnered substantial attention, MLLM-based embodied agents remain underexplored due to the lack of comprehensive evaluation frameworks.
- **p. 1 / Abstract - extractive body cue:** To bridge this gap, we introduce EMBODIEDBENCH, an extensive benchmark designed to evaluate visiondriven embodied agents.
- **p. 1 / Abstract - extractive body cue:** EMBODIEDBENCH features: (1) a diverse set of 1,128 testing tasks across four environments, ranging from high-level semantic tasks (e.g., household) to low-level tasks involving atomic ...
- **p. 1 / Abstract - extractive body cue:** Through extensive experiments, we evaluated 24 leading proprietary and open-source MLLMs within EMBODIEDBENCH.
- **p. 1 / 1. Introduction - extractive body cue:** Developing embodied agents capable of solving complex tasks in real world remains a significant challenge (Durante et al., 2024).
- **p. 1 / 1. Introduction - extractive body cue:** While these efforts significantly contribute to understanding LLM-based agent design, the evaluation of MLLM embodied agents remains underexplored, posing a challenge for creating more versatile ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are threefold: (1) proposing a comprehensive benchmark suite for evaluating MLLM-based embodied agents with different action levels and fine-grained capability-oriented subsets, (2) the ...
- **p. 1 / 1. Introduction - extractive body cue:** To address these questions, we introduce EMBODIEDBENCH, a comprehensive benchmark comprising 1,128 testing instances across four environments.
- **p. 1 / 1. Introduction - extractive body cue:** EMBODIEDBENCH is designed with two key features that set it apart from existing benchmarks: 1.
- **p. 3 / 3. Problem Formulation - extractive body cue:** Here, S is the complete state space unobservable to the agent; A is the space of high-level or low-level actions for the agents; Ωis the ...
- **p. 3 / 3. Problem Formulation - extractive body cue:** At timestep t, the agent maintains a history ht = (I0, a0, ..., It-1, at-1, It) and selects actions through a policy π(at/L, ht).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Here, S is the complete state space unobservable to the agent; A is the space of high-level or low-level actions for the agents; Ωis the visual perception space, where each observation It ... | standardized observation, action, task state와 evaluation split | p. 3 (3. Problem Formulation), p. 3 (3. Problem Formulation) |
| State/latent | Here, complete, state, space, unobservable, agent, high-level, low-level, actions, agents, visual, perception | benchmark state/goal와 method decision | p. 3 (3. Problem Formulation), p. 3 (3. Problem Formulation), p. 2 (1. Introduction) |
| Output/action | At timestep t, the agent maintains a history ht = (I0, a0, ..., It-1, at-1, It) and selects actions through a policy π(at/L, ht). | policy/controller trajectory 또는 measured result | p. 3 (3. Problem Formulation), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | The objective is to maximize the probability of task success: maxπ E [rτ], where τ is the terminal timestep-either when the task is successfully completed (sτ /= L) or when the maximum ... | success metric, robustness, generalization과 reproducibility | p. 3 (3. Problem Formulation) |

## Main Claims and Actual Contribution

- 네 시뮬레이션 환경에 1,128개 평가 과제를 구성하고 복잡한 지시 이해, 공간 판단, 장기 계획 등 역량별 하위 집합으로 나눴다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/yang25f/yang25f.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/yang25f/yang25f.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/yang25f/yang25f.pdf#page=5)
- 모델별 과제 성공률과 실패 이유를 분석해 고수준 가사 행동과 저수준 조작에서 나타나는 성능 격차를 확인했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/yang25f/yang25f.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/yang25f/yang25f.pdf#page=8) · [PDF 9쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/yang25f/yang25f.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 9 (5.4. Visual-centric Ablation), p. 30 (Figure/Table caption) |
| Embodiment/environment | These findings emphasize two key insights: (1) when designing MLLM-based embodied AI benchmarks, it is essential to consider action-level taxonomy, with greater attention to low-level action tasks, and (2) more advanced methods ... | hardware/simulator version and reset protocol | p. 6 (5.2. Benchmark Results), p. 9 (5.5. Error Analysis) |
| Dataset/benchmark | We benchmark 24 models, including 8 leading proprietary models and 16 SOTA open-source models. | role, split, size and leakage | p. 6 (5.2. Benchmark Results), p. 9 (5.5. Error Analysis), p. 6 (5.1. Experimental Setups), p. 7 (5.2. Benchmark Results) |
| Metric | We use the task success rate as the primary metric in our experiments. | definition, denominator, direction and uncertainty | p. 6 (5.1. Experimental Setups), p. 7 (5.3. Language-centric Ablation), p. 7 (5.2. Benchmark Results) |
| Baseline/ablation | Figure 6. Error Analysis. image. Visual ICL examples are demonstrated in Figure 15. We limit the number of examples to two to avoid over- whelming the model with excessive visual input. This ... | fair input/data/compute/action matching | p. 9 (Figure/Table caption), p. 6 (5.2. Benchmark Results), p. 6 (5.2. Benchmark Results) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6. Conclusion - extractive body cue:** Limitations A key limitation of this work is that our evaluation is conducted solely in simulated environments, without real-world experiments.
- **p. 9 / 5.5. Error Analysis - extractive body cue:** Perception errors make up 33% of failures, with wrong recognition errors (22%) being the most frequent.
- **p. 31 / Figure/Table caption - extractive body cue:** Figure 17. Error Analysis on EB-Navigation. Perception Errors. The first category involves the model's ability to interpret visual observations and recognize the spatial position of ...
- **p. 32 / Figure/Table caption - extractive body cue:** Table 11. Error Taxonomy with Definitions model failed to identify the target object even when it was present in the visual input. This suggests limitations ...
- **p. 6 / 5.2. Benchmark Results - extractive body cue:** These results highlight the importance of fine-grained evaluations to uncover nuanced limitations in current models.
- **p. 6 / 5.2. Benchmark Results - extractive body cue:** In EB-Manipulation, for example, Claude-3.5-Sonnet scores 14.6 and 5.6 points higher than GPT-4o on the complex instruction and visual appearance subsets, respectively, but falls significantly ...
- **p. 8 / 5.4. Visual-centric Ablation - extractive body cue:** Future work could focus on developing methods to better leverage multiple images for enhanced understanding and reasoning.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Problem Formulation)이다.
