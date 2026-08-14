# Learning Locomotion Skills for Cassie: Iterative Design and Sim-to-Real

- Year/Venue: 2019 / CoRL
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, bipedal locomotion, Reinforcement Learning, sim-to-real, Cassie
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://www.cs.ubc.ca/~van/papers/2019-CORL-cassie/index.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- It is difficult to predict the outcomes of changes made to the reward functions, policy architectures, and the set of tasks being trained on.
- However, these systems are relatively stable in comparison to human-scale bipeds, for which convincing demonstrations of DRL methods to dynamic locomotion on real hardware are still lacking, to ...

## Core Idea
- In this paper, we propose a practical method that allows the reward function to be fully redefined on each successive design iteration while limiting the deviation from the ...
- In this paper, we propose a DRL design process that reflects and supports the iterative nature of control policy design.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Impressive results have been demonstrated on planar bipeds , quadruped robots, , and 6legged robots .
- We demonstrate the effectiveness of this iterative-design approach on the bipedal robot Cassie, achieving stable walking with different gait styles at various speeds.
- We demonstrate the successful transfer of policies learned in simulation to the physical robot without any dynamics randomization, and that variable-speed walking policies for the physical robot can ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- It is difficult to predict the outcomes of changes made to the reward functions, policy architectures, and the set of tasks being trained on.
- In this paper, we propose a practical method that allows the reward function to be fully redefined on each successive design iteration while limiting the deviation from the ...
- In this paper, we propose a DRL design process that reflects and supports the iterative nature of control policy design.

## Abstract Cue
- —Deep reinforcement learning (DRL) is a promising approach for developing legged locomotion skills.
