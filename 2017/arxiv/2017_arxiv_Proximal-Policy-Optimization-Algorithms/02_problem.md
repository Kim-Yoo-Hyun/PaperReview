# Problem

- Year/Venue: 2017 / arxiv
- Category: Foundations: RL and Imitation Learning
- Tags: Reinforcement Learning, policy learning, Robotics
- Paper link: ./2017/arxiv/2017_arxiv_Proximal-Policy-Optimization-Algorithms/paper.pdf
- Code/Project: https://github.com/openai/baselines
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Q-learning (with function approximation) fails on many simple problems1 and is poorly understood, vanilla policy gradient methods have poor data effiency and robustness; and trust region policy optimization ...

## 해결하려는 문제
- Our experiments test PPO on a collection of benchmark tasks, including simulated robotic locomotion and Atari game playing, and we show that PPO outperforms other online policy gradient ...
- We propose a new family of policy gradient methods for reinforcement learning, which alternate between sampling data through interaction with the environment, and optimizing a “surrogate” objective function ...
- Whereas standard policy gradient methods perform one gradient update per data sample, we propose a novel objective function that enables multiple epochs of minibatch updates.

## 선행 연구 / 배경 단서
- Q-learning (with function approximation) fails on many simple problems1 and is poorly understood, vanilla policy gradient methods have poor data effiency and robustness; and trust region policy optimization ...
- However, there is room for improvement in developing a method that is scalable (to large models and parallel implementations), data efficient, and robust (i.e., successful on a variety ...
- We propose a novel objective with clipped probability ratios, which forms a pessimistic estimate (i.e., lower bound) of the performance of the policy.
