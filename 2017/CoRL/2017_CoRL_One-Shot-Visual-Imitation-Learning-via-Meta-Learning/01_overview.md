# One-Shot Visual Imitation Learning via Meta-Learning

- Year/Venue: 2017 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, meta-learning, visual manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://arxiv.org/abs/1703.07326
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- To accomplish this, we must solve two broad problems.
- For example, when it is conditioned on a single demonstration for task F, it should behave like a good policy for task F. (c) We can phrase this ...
- Demonstrations are an extremely convenient form of information we can use to teach robots to overcome these two challenges.

## Core Idea
- Our proposed architecture consists of three modules: the demonstration network, the context network, and the manipulation network.
- In this paper, we propose a meta-learning framework for achieving such capability, which we call one-shot imitation learning.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experiments show that the use of soft attention allows the model to generalize to conditions and tasks unseen in the training data.
- 2 Additional experiment results are available in the Appendix, including a simple illustrative example of particle reaching tasks and further analysis of block stacking 6 • Can our ...
- We conduct experiments with the block stacking tasks described in Section 3.2.2 These experiments are designed to answer the following questions: • How does training with behavioral cloning ...

## Limitation
- There are a lot of exciting directions for future work.
- We are also interested in enabling the policy to condition on multiple demonstrations, in case where one demonstration does not fully resolve ambiguity in the objective.

## Contribution
- Our experiments show that the use of soft attention allows the model to generalize to conditions and tasks unseen in the training data.
- In this paper, we propose a meta-learning framework for achieving such capability, which we call one-shot imitation learning.
- At training time, our algorithm is presented with pairs of demonstrations for a subset of all tasks.

## Abstract Cue
- Imitation learning has been commonly applied to solve different tasks in isolation.
