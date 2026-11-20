# LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (44 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2306.03310.
> PDF retrieval source: https://arxiv.org/pdf/2306.03310. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / NeurIPS
- Authors: Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, Imitation Learning, Benchmark
- Official paper: https://arxiv.org/abs/2306.03310
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html
- Full-text retrieval: https://arxiv.org/pdf/2306.03310
- Code/Project: https://libero-project.github.io/main.html
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (44 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

조작 과업을 순차적으로 배울 때 과거 지식의 전이와 망각을 측정하는 벤치마크다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Lifelong learning offers a promising paradigm of building a generalist agent that learns and adapts over its lifespan.
- **p. 1 / Abstract - extractive body cue:** Unlike traditional lifelong learning problems in image and text domains, which primarily involve the transfer of declarative knowledge of entities and concepts, lifelong learning in ...
- **p. 1 / Abstract - extractive body cue:** To advance research in LLDM, we introduce LIBERO, a novel benchmark of lifelong learning for robot manipulation.
- **p. 1 / Abstract - extractive body cue:** Specifically, LIBERO highlights five key research topics in LLDM: 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of both; 2) how ...
- **p. 1 / Abstract - extractive body cue:** We develop an extendible procedural generation pipeline that can in principle generate infinitely many tasks.
- **p. 4 / 2 Background - extractive body cue:** A robot in the real world, however, often cannot choose which task to encounter first.
- **p. 1 / 1 Introduction - extractive body cue:** Consider a scenario where a robot, initially trained to retrieve juice from a fridge, fails

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We present an initial study using LIBERO to investigate five major research topics in LLDM (Figure 1): 1) knowledge transfer with different types of distribution ...
- **p. 1 / Abstract - extractive body cue:** To advance research in LLDM, we introduce LIBERO, a novel benchmark of lifelong learning for robot manipulation.
- **p. 3 / 2 Background - extractive body cue:** We present four task suites in Section 4.2: three task suites for studying the transfer of knowledge about spatial relationships, object concepts, and task goals ...
- **p. 1 / 1 Introduction - extractive body cue:** A longstanding goal in machine learning is to develop a generalist agent that can perform a wide range of tasks.
- **p. 2 / 1 Introduction - extractive body cue:** LIBERO is scalable, extendable, and designed explicitly for studying lifelong learning in robot manipulation.
- **p. 1 / Abstract - extractive body cue:** Specifically, LIBERO highlights five key research topics in LLDM: 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of both; 2) how ...
- **p. 6 / 2 Background - extractive body cue:** architecture [75] uses a similar ResNet-based visual backbone, but a transformer decoder [66] as the temporal backbone to process outputs from ResNet, which are a ...
- **p. 6 / 2 Background - extractive body cue:** For all the lifelong learning algorithms and neural architectures, we use behavioral cloning (BC) [4] to train policies for individual tasks (See (2)).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In the end, a robot executes a policy by sampling a continuous value for end-effector action from the output distribution. | standardized observation, action, task state와 evaluation split | p. 6 (2 Background), p. 4 (2 Background) |
| State/latent | robot, executes, policy, sampling, continuous, value, end-effector, action, output, distribution, Neural, Architecture | benchmark state/goal와 method decision | p. 6 (2 Background), p. 4 (2 Background), p. 3 (2 Background) |
| Output/action | (T2) Neural Architecture Design An important research question in LLDM is how to design effective neural architectures to abstract the multi-modal observations (images, language descriptions, and robot states) and transfer only relevant ... | policy/controller trajectory 또는 measured result | p. 4 (2 Background), p. 3 (2 Background), p. 5 (2 Background) |
| Objective/outcome | The robot's objective is to learn a policy π that maximizes the expected return: maxπ J(π) = Est,at∼π,µ0[PH t=1 g(st)]. | success metric, robustness, generalization과 reproducibility | p. 3 (2 Background), p. 3 (2 Background), p. 5 (2 Background) |

## Main Claims and Actual Contribution

- 물체·공간 배치·목표 등을 달리한 태스크 묶음과 시연을 구축한다.
- 동일한 태스크 순서에서 평생학습 알고리즘과 정책 구조를 비교한다.

[검증한 원문](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 8 (5 Experiments), p. 6 (5 Experiments) |
| Embodiment/environment | But since PACKNET splits the network into different sub-networks, the essential capacity of the network for learning any individual task is smaller. | hardware/simulator version and reset protocol | p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Dataset/benchmark | Q5: How robust are different LL algorithms to task ordering in LLDM? | role, split, size and leakage | p. 8 (5 Experiments), p. 8 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Metric | All metrics are computed in terms of success rate, as previous literature has shown that the success rate is a more reliable metric than training loss for manipulation policies [42] (Detailed explanation ... | definition, denominator, direction and uncertainty | p. 6 (5 Experiments), p. 6 (5 Experiments), p. 27 (Figure/Table caption) |
| Baseline/ablation | Study on Lifelong Learning Algorithms (Q1, Q3) Table 2 reports the lifelong learning performance of the three lifelong learning algorithms, together with the SEQL and MTL baselines. | fair input/data/compute/action matching | p. 8 (5 Experiments), p. 8 (5 Experiments), p. 43 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 5 Experiments - extractive body cue:** Q5: How robust are different LL algorithms to task ordering in LLDM?
- **p. 8 / 5 Experiments - extractive body cue:** Therefore, we conjecture that PACKNET is not rich enough to learn on LIBEROLONG; 3) EWC works worse than SEQL, showing that the regularization on the ...
- **p. 9 / 5 Experiments - extractive body cue:** This finding highlights an important direction for future research: developing algorithms or architectures that are robust to varying task orderings.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 4 (2 Background), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (2 Background), p. 1 (Abstract)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (44 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** A robot in the real world, however, often cannot choose which task to encounter first. (p. 4, 2 Background).
- **Actual contribution:** We present an initial study using LIBERO to investigate five major research topics in LLDM (Figure 1): 1) knowledge transfer with different types of distribution shift; 2) neural architecture design; ... (p. 2, 1 Introduction).
- **Evaluation boundary:** Table 2: Performance of three lifelong algorithms and the SEQL and MTL baselines on the four task suites, where the policy is fixed to be RESNET-T. Results are averaged over ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** Consider a scenario where a robot, initially trained to retrieve juice from a fridge, fails (p. 1, 1 Introduction).
