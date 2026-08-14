# QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation

- Year/Venue: 2018 / CoRL
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Q-learning, manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://ai.googleblog.com/2018/06/scalable-deep-reinforcement-learning.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- While grasping restricts the manipulation problem, it still retains many of its largest challenges: a grasping system should be able to pick up previously unseen objects with reliable ...
- To meet the generalization demands of real-world manipulation, we focus specifically on scalable learning with off-policy algorithms, and study this question in the context of the specific problem ...
- Manipulation with object interaction represents one of the largest open problems in robotics: intelligently interacting with previously unseen objects in open-world environments requires generalizable perception, closed-loop vision-based control, ...

## Core Idea
- The variant of our method that uses on-policy joint finetuning has a failure rate more than four times lower than prior work on the test set, while using ...
- Effective off-policy training is valuable as it allows for rapid iteration on hyperparameters and architecture design without any data collection.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The first two questions are addressed through a set of rigorous real-world quantitative experiments, which we discuss in Section 6.1, question (3) is addressed through qualitative experiments, which ...
- Aside from attaining a very high success rate, our method exhibits behaviors that are quite distinct from more standard grasping systems: using only RGB visionbased perception from an ...
- The experiments in the appendices also study the impact of dataset size and off-policy training on final performance.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To that end, we introduce QT-Opt, a scalable self-supervised vision-based reinforcement learning framework that can leverage over 580k real-world grasp attempts to train a deep neural network Q-function ...
- In contrast to static learning behaviors that choose a grasp point and then execute the desired grasp, our method enables closed-loop vision-based control, whereby the robot continuously updates ...
- Aside from attaining a very high success rate, our method exhibits behaviors that are quite distinct from more standard grasping systems: using only RGB visionbased perception from an ...

## Abstract Cue
- : In this paper, we study the problem of learning vision-based dynamic manipulation skills using a scalable reinforcement learning approach.
