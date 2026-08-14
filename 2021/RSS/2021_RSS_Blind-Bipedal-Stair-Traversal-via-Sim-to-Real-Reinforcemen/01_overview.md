# Blind Bipedal Stair Traversal via Sim-to-Real Reinforcement Learning

- Year/Venue: 2021 / RSS
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, bipedal locomotion, Reinforcement Learning, sim-to-real, proprioception
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://www.roboticsproceedings.org/rss17/p061.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- —Accurate and precise terrain estimation is a difficult problem for robot locomotion in real-world environments.
- For such blind bipedal platforms, the problem appears difficult (even for humans) due to the surprise elevation changes.
- In this paper, we explore the limits of such an approach by investigating the problem of traversing stair-like terrain without any external perception or terrain models on a ...

## Core Idea
- Importantly, this only requires modifying an existing flat-terrain training RL framework to include stair-like terrain randomization, without any changes in reward function.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our main contribution is to show that sim-to-real reinforcement learning (RL) can achieve robust locomotion over stair-like terrain on the bipedal robot Cassie using only proprioceptive feedback.
- While planar bipedal robots have been shown to be able to reject disturbances like large unexpected dropsteps , the vast majority of approaches seeking to enable such robots ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our main contribution is to show that sim-to-real reinforcement learning (RL) can achieve robust locomotion over stair-like terrain on the bipedal robot Cassie using only proprioceptive feedback.
- Importantly, this only requires modifying an existing flat-terrain training RL framework to include stair-like terrain randomization, without any changes in reward function.
- —Accurate and precise terrain estimation is a difficult problem for robot locomotion in real-world environments.

## Abstract Cue
- —Accurate and precise terrain estimation is a difficult problem for robot locomotion in real-world environments.
