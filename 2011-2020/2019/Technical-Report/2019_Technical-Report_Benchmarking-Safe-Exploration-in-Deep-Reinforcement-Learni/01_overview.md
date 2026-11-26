# Benchmarking Safe Exploration in Deep Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://cdn.openai.com/safexp-short.pdf.
> PDF retrieval source: https://cdn.openai.com/safexp-short.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / Technical Report
- Authors: Alex Ray, Joshua Achiam, Dario Amodei
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, safe reinforcement learning, Safety Gym, Benchmark, constraints
- Official paper: https://cdn.openai.com/safexp-short.pdf
- Full-text retrieval: https://cdn.openai.com/safexp-short.pdf
- Code/Project: https://github.com/openai/safety-gym
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://cdn.openai.com/safexp-short.pdf) 기준이다.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 14. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

Safety Gym은 연속 제어에서 탐색하는 동안 얻는 보상과 위반 비용을 따로 기록해 제약 강화학습 알고리즘을 비교한다. [PDF 1쪽](https://cdn.openai.com/safexp-short.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Reinforcement learning (RL) agents need to explore their environments in order to learn optimal policies by trial and error.
- **p. 1 / Abstract - extractive body cue:** In many environments, safety is a critical concern and certain errors are unacceptable: for example, robotics systems that interact with humans should never cause injury ...
- **p. 1 / Abstract - extractive body cue:** While it is currently typical to train RL agents mostly or entirely in simulation, where safety concerns are minimal, we anticipate that challenges in simulating ...
- **p. 1 / Abstract - extractive body cue:** Consequently we take the position that safe exploration should be viewed as a critical focus area for RL research, and in this work we make ...
- **p. 1 / Abstract - extractive body cue:** First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe ...
- **p. 1 / 1 Introduction - extractive body cue:** While RL is not yet fully mature or ready to serve as an "off-the-shelf" solution, it appears to offer a viable path to solving hard ...
- **p. 2 / 1 Introduction - extractive body cue:** However, there is not yet a standard set of environments for making progress on safe exploration specifically.2 Different papers use different environments and evaluation procedures, ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** To address the gap, we present Safety Gym: a set of tools for accelerating safe exploration research.
- **p. 2 / 1 Introduction - extractive body cue:** Towards standardizing safety specifications: Based on a range of prior work, we propose to standardize constrained RL [Altman, 1999] as the main formalism for incorporating ...
- **p. 1 / Abstract - extractive body cue:** First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe ...
- **p. 1 / Abstract - extractive body cue:** Second, we present the Safety Gym benchmark suite, a new slate of high-dimensional continuous control environments for measuring research progress on constrained RL.
- **p. 2 / 1 Introduction - extractive body cue:** While "sim-to-real" transfer learning algorithms may mitigate this issue, we expect that in problems centered on AI-human interaction or very complex systems, challenges in building ...
- **p. 2 / 1 Introduction - extractive body cue:** We recommend a protocol for evaluating constrained RL algorithms on Safety Gym environments based on three metrics: task performance of the final policy, constraint satisfaction ...
- **p. 3 / 1 Introduction - extractive body cue:** Our baseline algorithms include Trust Region Policy Optimization (TRPO) [Schulman et al., 2015] and Proximal Policy Optimization (PPO) [Schulman et al., 2017] in their original ...
- **p. 1 / Abstract - extractive body cue:** While it is currently typical to train RL agents mostly or entirely in simulation, where safety concerns are minimal, we anticipate that challenges in simulating ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We recommend a protocol for evaluating constrained RL algorithms on Safety Gym environments based on three metrics: task performance of the final policy, constraint satisfaction of the final policy, and average regret ... | standardized observation, action, task state와 evaluation split | p. 2 (1 Introduction), p. 1 (Abstract) |
| State/latent | recommend, protocol, evaluating, constrained, algorithms, Safety, Gym, environments, three, metrics, task, performance | benchmark state/goal와 method decision | p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/action | While it is currently typical to train RL agents mostly or entirely in simulation, where safety concerns are minimal, we anticipate that challenges in simulating the complexities of the real world (such ... | policy/controller trajectory 또는 measured result | p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Objective/outcome | These are expressed via a reward function and a set of auxiliary cost functions respectively. | success metric, robustness, generalization과 reproducibility | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- 서로 다른 이동 로봇과 목표·위험 요소를 조합해 같은 과제에서도 제어와 안전 제약의 난도를 바꿀 수 있게 했다. [PDF 9쪽](https://cdn.openai.com/safexp-short.pdf#page=9) · [PDF 10쪽](https://cdn.openai.com/safexp-short.pdf#page=10) · [PDF 12쪽](https://cdn.openai.com/safexp-short.pdf#page=12)
- 최종 정책의 보상·제약 위반과 학습 과정 전체의 평균 비용률을 각각 계산해 기준 알고리즘을 비교했다. [PDF 14쪽](https://cdn.openai.com/safexp-short.pdf#page=14) · [PDF 16쪽](https://cdn.openai.com/safexp-short.pdf#page=16)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 21 (5.3 Results), p. 14 (5 Experiments) |
| Embodiment/environment | SG6 has at least one environment for each task, robot, and level. | hardware/simulator version and reset protocol | p. 15 (5 Experiments), p. 21 (5.3 Results) |
| Dataset/benchmark | SGCar: All six Car robot environments with constraints in Safety Gym. | role, split, size and leakage | p. 15 (5 Experiments), p. 21 (5.3 Results), p. 15 (5 Experiments), p. 16 (5 Experiments) |
| Metric | We compare normalized scores like we would compare individual training runs: the average constraint violation should be zero (or within noise of zero), and among approximately constraint-satisfying algorithms, one algorithm dominates an ... | definition, denominator, direction and uncertainty | p. 15 (5 Experiments), p. 16 (5.3 Results), p. 16 (5.3 Results) |
| Baseline/ablation | Advancing SOTA on Safety Gym: Our baseline results for constrained RL indicate a need for stronger and/or better-tuned algorithms to succeed on Safety Gym environments. | fair input/data/compute/action matching | p. 21 (5.3 Results), p. 14 (5 Experiments), p. 21 (5.3 Results) |

## Explicit Limitations and Failure Boundary

- **p. 16 / 5 Experiments - extractive body cue:** [2017], we omit the learned failure predictor they used for cost shaping.
- **p. 21 / 5.3 Results - extractive body cue:** There are a number of avenues we consider promising for future work.
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 6: Diversity of generated layouts for the Safexp-PointPush2-v0 env. 4.2 Safety Gym Benchmark Suite Safety Gym ships with a suite of pre-configured benchmark environments, ...
- **p. 14 / 5 Experiments - extractive body cue:** First and foremost, it corresponds directly to safety outcomes: a lower cost rate means that fewer unsafe things happened.
- **PDF p. 14, §5 Eq. (3) (DOC-QA2 원문 대조):** 실험은 finite-horizon undiscounted return을 최대화하면서 E[Σₜ₌₀ᵀcₜ]≤d를 제약한다. cₜ는 source 종류와 무관하게 unsafe interaction이면 1인 aggregate indicator다. Episode cost와 전체 training steps당 cost rate는 별도 metric이다.
- **p. 15 / 5 Experiments - extractive body cue:** 3Characteristic return and cumulative cost were obtained by averaging over the last five epochs of training to reduce noise.
- **p. 15 / 5 Experiments - extractive body cue:** We compare normalized scores like we would compare individual training runs: the average constraint violation should be zero (or within noise of zero), and among ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract)이다.
