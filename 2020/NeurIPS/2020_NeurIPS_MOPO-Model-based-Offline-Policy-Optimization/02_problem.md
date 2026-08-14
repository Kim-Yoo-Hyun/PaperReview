# Problem

- Year/Venue: 2020 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, offline reinforcement learning, model-based RL, distribution shift
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/tianheyu927/mopo
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Reinforcement learning (RL) methods, in contrast, struggle to scale to many real-world applications, e.g., autonomous driving and healthcare , because they rely on costly online trial-and-error.
- First, modelbased RL algorithms effectively receive more supervision, since the model is trained on every transition, even in sparse-reward settings.
- This problem setting offers the promise of utilizing such datasets to acquire policies without any costly or dangerous active exploration.

## 해결하려는 문제
- Our algorithm, Model-based Offline Policy Optimization (MOPO), outperforms standard model-based RL algorithms and prior state-of-the-art model-free offline RL algorithms on existing offline RL benchmarks and two challenging continuous ...
- Instead, we propose to modify the existing model-based RL methods by applying them with rewards artificially penalized by the uncertainty of the dynamics.
- However, it is also challenging, due to the distributional shift between the offline training data and those states visited by the learned policy.

## 선행 연구 / 배경 단서
- Our results suggest that MOPO substantially outperforms these prior methods on the offline RL benchmark D4RL as well as on offline RL problems where the agent must generalize ...
- We empirically compare this approach, model-based offline policy optimization (MOPO), to both MBPO and existing state-of-the-art model-free offline RL algorithms.
- These failures are generally caused by large extrapolation error when the Q-function is evaluated on out-of-distribution actions , which can lead to unstable learning and divergence.
