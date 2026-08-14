# MOPO: Model-based Offline Policy Optimization

- Year/Venue: 2020 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, offline reinforcement learning, model-based RL, distribution shift
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/tianheyu927/mopo
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Reinforcement learning (RL) methods, in contrast, struggle to scale to many real-world applications, e.g., autonomous driving and healthcare , because they rely on costly online trial-and-error.
- First, modelbased RL algorithms effectively receive more supervision, since the model is trained on every transition, even in sparse-reward settings.
- This problem setting offers the promise of utilizing such datasets to acquire policies without any costly or dangerous active exploration.

## Core Idea
- Instead, we propose to modify the existing model-based RL methods by applying them with rewards artificially penalized by the uncertainty of the dynamics.
- Hence, the central question that this work is trying to answer is: can we develop an offline RL algorithm that generalizes beyond the state and action support of ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our algorithm, Model-based Offline Policy Optimization (MOPO), outperforms standard model-based RL algorithms and prior state-of-the-art model-free offline RL algorithms on existing offline RL benchmarks and two challenging continuous ...
- In our experiments, we aim to study the follow questions: (1) How does MOPO perform on standard offline RL benchmarks in comparison to prior state-of-the-art approaches? (2) Can ...
- We compare against several baselines, including the current state-of-the-art model-free offline RL algorithms.

## Limitation
- Our work opens up a number of questions and directions for future work.
- However, uncertainty estimation does not explain the entire difference nor does it explain why model-free methods cannot also enjoy the benefits of uncertainty estimation.

## Contribution
- Our algorithm, Model-based Offline Policy Optimization (MOPO), outperforms standard model-based RL algorithms and prior state-of-the-art model-free offline RL algorithms on existing offline RL benchmarks and two challenging continuous ...
- Instead, we propose to modify the existing model-based RL methods by applying them with rewards artificially penalized by the uncertainty of the dynamics.
- However, it is also challenging, due to the distributional shift between the offline training data and those states visited by the learned policy.

## Abstract Cue
- Offline reinforcement learning (RL) refers to the problem of learning policies entirely from a large batch of previously collected data.
