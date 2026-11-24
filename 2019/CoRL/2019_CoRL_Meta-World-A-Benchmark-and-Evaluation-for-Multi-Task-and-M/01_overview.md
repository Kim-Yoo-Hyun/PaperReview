# Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v100/yu20a.html.
> PDF retrieval source: https://proceedings.mlr.press/v100/yu20a.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / CoRL
- Authors: Tianhe Yu, Deirdre Quillen, Zhanpeng He, Ryan Julian, Karol Hausman, Chelsea Finn, Sergey Levine
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Benchmark, Reinforcement Learning, manipulation
- Official paper: https://proceedings.mlr.press/v100/yu20a.html
- Full-text retrieval: https://proceedings.mlr.press/v100/yu20a/yu20a.pdf
- Code/Project: https://meta-world.github.io/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://proceedings.mlr.press/v100/yu20a/yu20a.pdf) 기준이다.

## Why This Paper Is Here

Meta-World는 같은 시뮬레이션 로봇팔로 수행하는 서로 다른 50개 조작 과제를 제공해 다중 작업 학습과 새 기술 적응을 평가한다. [PDF 2쪽](https://proceedings.mlr.press/v100/yu20a/yu20a.pdf#page=2)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Meta-reinforcement learning algorithms can enable robots to acquire new skills much more quickly, by leveraging prior experience to learn how to learn.
- **p. 1 / Abstract - extractive body cue:** However, much of the current research on meta-reinforcement learning focuses on task distributions that are very narrow.
- **p. 1 / Abstract - extractive body cue:** For example, a commonly used meta-reinforcement learning benchmark uses different running velocities for a simulated robot as different tasks.
- **p. 1 / Abstract - extractive body cue:** When policies are meta-trained on such narrow task distributions, they cannot possibly generalize to more quickly acquire entirely new tasks.
- **p. 1 / Abstract - extractive body cue:** Therefore, if the aim of these methods is enable faster acquisition of entirely new behaviors, we must evaluate them on task distributions that are sufficiently ...
- **p. 2 / 1 Introduction - extractive body cue:** We provide an evaluation protocol with evaluation modes of varying difficulty, and observe that current methods only show success in the easiest modes.
- **p. 2 / 1 Introduction - extractive body cue:** Our empirical evaluation of existing methods on this benchmark reveals that, despite some impressive progress in multi-task and meta-reinforcement learning over the past few years, ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we present a benchmark of simulated manipulation tasks with everyday objects, all of which are contained in a shared, table-top environment with ...
- **p. 2 / 1 Introduction - extractive body cue:** For example, one popular evaluation of metalearning involves choosing different running directions for simulated legged robots [10], which then enables fast adaptation to new directions.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose an open-source simulated benchmark for meta-reinforcement learning and multitask learning consisting of 50 distinct robotic manipulation tasks.
- **p. 1 / Abstract - extractive body cue:** Our aim is to make it possible to develop algorithms that generalize to accelerate the acquisition of entirely new, held-out tasks.
- **p. 1 / Abstract - extractive body cue:** We evaluate 6 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks.
- **p. 2 / 1 Introduction - extractive body cue:** This opens the door for future developments in multi-task and meta reinforcement learning: instead of focusing on further increasing performance on current narrow task suites, ...
- **p. 2 / 1 Introduction - extractive body cue:** In order to study the capabilities of current multi-task and meta-reinforcement learning methods and make it feasible to design new algorithms that actually generalize and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We evaluate 6 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks. | standardized observation, action, task state와 evaluation split | p. 1 (Abstract), p. 1 (1 Introduction) |
| State/latent | evaluate, state-of-the-art, meta-reinforcement, learning, multi-task, algorithms, tasks, While, reinforcement, achieved, some, success | benchmark state/goal와 method decision | p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | While reinforcement learning (RL) has achieved some success in domains such as assembly [1], ping pong [2], in-hand manipulation [3], and hockey [4], state-of-the-art methods require substantially more experience than humans to ... | policy/controller trajectory 또는 measured result | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | While these methods have made progress, the development of both classes of approaches has been limited by the lack of established benchmarks and evaluation protocols that reflect realistic use cases. | success metric, robustness, generalization과 reproducibility | p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- 같은 기술 안의 목표 변화와 학습에서 보지 못한 기술을 구별하도록 다중 작업·메타학습 평가 분할을 구성했다. [PDF 4쪽](https://proceedings.mlr.press/v100/yu20a/yu20a.pdf#page=4) · [PDF 5쪽](https://proceedings.mlr.press/v100/yu20a/yu20a.pdf#page=5) · [PDF 6쪽](https://proceedings.mlr.press/v100/yu20a/yu20a.pdf#page=6)
- 여러 학습 기준선을 같은 작업 집합에서 비교하고 과제 수와 새로운 기술이 성공률에 미치는 영향을 보고했다. [PDF 7쪽](https://proceedings.mlr.press/v100/yu20a/yu20a.pdf#page=7) · [PDF 8쪽](https://proceedings.mlr.press/v100/yu20a/yu20a.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 1 (1 Introduction) |
| Embodiment/environment | For example, a commonly used meta-reinforcement learning benchmark uses different running velocities for a simulated robot as different tasks. | hardware/simulator version and reset protocol | p. 1 (Abstract), p. 1 (Abstract) |
| Dataset/benchmark | To this end, we present a benchmark of simulated manipulation tasks with everyday objects, all of which are contained in a shared, table-top environment with a simulated Sawyer arm. | role, split, size and leakage | p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Metric | Figure 8: Learning curves of all methods on MT10, ML10, MT50, and ML45 benchmarks. Y- axis represents success rate averaged over tasks in percentage (%). Off-policy algorithms such as multi-task SAC and ... | definition, denominator, direction and uncertainty | p. 13 (Figure/Table caption), p. 8 (Figure/Table caption), p. 11 (Figure/Table caption) |
| Baseline/ablation | We evaluate 6 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks. | fair input/data/compute/action matching | p. 1 (Abstract), p. 1 (1 Introduction), p. 4 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit some ...
- **p. 1 / Abstract - extractive body cue:** When policies are meta-trained on such narrow task distributions, they cannot possibly generalize to more quickly acquire entirely new tasks.
- **p. 7 / 2 Related Work - extractive body cue:** Our experiments show that current meta-RL methods in fact cannot yet generalize effectively to entirely new tasks and do not even learn the meta-training tasks ...
- **p. 2 / 1 Introduction - extractive body cue:** This opens the door for future developments in multi-task and meta reinforcement learning: instead of focusing on further increasing performance on current narrow task suites, ...
- **p. 7 / 2 Related Work - extractive body cue:** This suggests a number of directions for future work, which we describe below.
- **p. 8 / 2 Related Work - extractive body cue:** We leave these directions for future work, either to be done by ourselves or in the form of open-source contributions.
- **p. 6 / 2 Related Work - extractive body cue:** The positions of objects and goal positions are fixed in all tasks in this evaluation, so as to focus on acquiring the distinct skills, rather ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract)이다.
