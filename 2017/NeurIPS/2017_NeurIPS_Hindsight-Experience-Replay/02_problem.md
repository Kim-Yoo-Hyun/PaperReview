# Problem

- Year/Venue: 2017 / NeurIPS
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, goal-conditioned RL, sparse rewards
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/openai/baselines
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Reinforcement learning (RL) combined with neural networks has recently led to a wide range of successes in learning policies for sequential decision-making problems.
- However, a common challenge, especially for robotics, is the need to engineer a reward function that not only reflects the task at hand but is also carefully shaped ...
- For example, Popov et al. (2017) use a cost function consisting of five relatively complicated terms which need to be carefully weighted in order to train a policy ...

## 해결하려는 문제
- Our ablation studies show that Hindsight Experience Replay is a crucial ingredient which makes training possible in these challenging environments.
- We demonstrate our approach on the task of manipulating objects with a robotic arm.
- We present a novel technique called Hindsight Experience Replay which allows sample-efficient learning from rewards which are sparse and binary and therefore avoid the need for complicated reward ...

## 선행 연구 / 배경 단서
- Reinforcement learning (RL) combined with neural networks has recently led to a wide range of successes in learning policies for sequential decision-making problems.
- However, a common challenge, especially for robotics, is the need to engineer a reward function that not only reflects the task at hand but is also carefully shaped ...
- For example, Popov et al. (2017) use a cost function consisting of five relatively complicated terms which need to be carefully weighted in order to train a policy ...
