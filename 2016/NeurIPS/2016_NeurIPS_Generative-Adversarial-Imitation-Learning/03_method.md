# Method

- Year/Venue: 2016 / NeurIPS
- Category: Foundations: RL and Imitation Learning
- Tags: Robotics, Imitation Learning, Reinforcement Learning
- Paper link: ./2016/NeurIPS/2016_NeurIPS_Generative-Adversarial-Imitation-Learning/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose a new general framework for directly extracting a policy from data, as if it were obtained by reinforcement learning following inverse reinforcement learning.
- We are interested in a specific setting of imitation learning—the problem of learning to perform a task from expert demonstrations—in which the learner is given only samples of ...

## 원리적 동기
- There are two main approaches suitable for this setting: behavioral cloning , which learns a policy as a supervised learning problem over state-action pairs from expert trajectories; and ...
- Inverse reinforcement learning (IRL), on the other hand, learns a cost function that prioritizes entire trajectories over others, so compounding error, a problem for methods that fit single-timestep ...
- We propose a new general framework for directly extracting a policy from data, as if it were obtained by reinforcement learning following inverse reinforcement learning.

## 핵심 방법론
- We are interested in a specific setting of imitation learning—the problem of learning to perform a task from expert demonstrations—in which the learner is given only samples of ...
