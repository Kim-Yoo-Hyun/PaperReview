# Learning Memory-Based Control for Human-Scale Bipedal Locomotion

- Year/Venue: 2020 / RSS
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, bipedal locomotion, recurrent policy, sim-to-real, online adaptation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://www.roboticsproceedings.org/rss16/p031.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- —Controlling a non-statically stable biped is a difficult problem largely due to the complex hybrid dynamics involved.
- Memory-based controllers, such as recurrent neural networks (RNN), are a potentially powerful choice for solving highly dynamic nonlinear control problems due to their ability to infer important information ...
- The existing work, however, has primarily used simple memoryless network architectures, even though more sophisticated architectures, such as those including memory, often yield superior performance in other RL ...

## Core Idea
- Use of memory-based architectures has the potential to yield better performance in partially-observed domains, which has been observed in a variety of applications .
- The existing work, however, has primarily used simple memoryless network architectures, even though more sophisticated architectures, such as those including memory, often yield superior performance in other RL ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We show that while RNNs are able to significantly outperform memoryless policies in simulation, they do not exhibit superior behavior on the real biped due to overfitting to ...
- Recent work in transferring these trained controllers from simulation onto real robots has also enjoyed encouraging results , but many of these approaches use simple memoryless policy architectures, ...
- In this work, we demonstrate, for the first time, the application of learned, memory-based control to dynamic locomotion on the bipedal robot Cassie produced by Agility Robotics.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Recent work in transferring these trained controllers from simulation onto real robots has also enjoyed encouraging results , but many of these approaches use simple memoryless policy architectures, ...
- Recent work has demonstrated the effectiveness of reinforcement learning (RL) for simulation-based training of neural network controllers that successfully transfer to real bipeds.
- The existing work, however, has primarily used simple memoryless network architectures, even though more sophisticated architectures, such as those including memory, often yield superior performance in other RL ...

## Abstract Cue
- —Controlling a non-statically stable biped is a difficult problem largely due to the complex hybrid dynamics involved.
