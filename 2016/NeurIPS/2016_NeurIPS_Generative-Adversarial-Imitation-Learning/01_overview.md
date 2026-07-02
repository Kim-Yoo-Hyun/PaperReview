# Generative Adversarial Imitation Learning

- Year/Venue: 2016 / NeurIPS
- Category: Foundations: RL and Imitation Learning
- Tags: Robotics, Imitation Learning, Reinforcement Learning
- Paper link: ./2016/NeurIPS/2016_NeurIPS_Generative-Adversarial-Imitation-Learning/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- There are two main approaches suitable for this setting: behavioral cloning , which learns a policy as a supervised learning problem over state-action pairs from expert trajectories; and ...
- Inverse reinforcement learning (IRL), on the other hand, learns a cost function that prioritizes entire trajectories over others, so compounding error, a problem for methods that fit single-timestep ...
- We are interested in a specific setting of imitation learning—the problem of learning to perform a task from expert demonstrations—in which the learner is given only samples of ...

## Core Idea
- We propose a new general framework for directly extracting a policy from data, as if it were obtained by reinforcement learning following inverse reinforcement learning.
- We are interested in a specific setting of imitation learning—the problem of learning to perform a task from expert demonstrations—in which the learner is given only samples of ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our algorithm almost always achieved at least 70% of expert performance for all dataset
- We were able to slightly improve our algorithm’s performance on Reacher using causal entropy regularization—in the 4-trajectory setting, the improvement from λ = 0 to λ = 10−3 ...
- We show that a certain instantiation of our framework draws an analogy between imitation learning and generative adversarial networks, from which we derive a model-free imitation learning algorithm ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose a new general framework for directly extracting a policy from data, as if it were obtained by reinforcement learning following inverse reinforcement learning.
- We show that a certain instantiation of our framework draws an analogy between imitation learning and generative adversarial networks, from which we derive a model-free imitation learning algorithm ...
- One approach is to recover the expert’s cost function with inverse reinforcement learning, then extract a policy from that cost function with reinforcement learning.

## Abstract Cue
- Consider learning a policy from example expert behavior, without interaction with the expert or access to reinforcement signal.
