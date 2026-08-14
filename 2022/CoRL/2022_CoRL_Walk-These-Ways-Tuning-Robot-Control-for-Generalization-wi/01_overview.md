# Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior

- Year/Venue: 2022 / CoRL
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, quadruped locomotion, Reinforcement Learning, behavior diversity
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/walk-these-ways
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- However, this creates a hard learning problem due to creation of challenging or infeasible locomotion scenarios.
- The examples above illustrate that even for the most advanced sim-to-real systems, the real world offers new challenges.
- For instance, if the robot is only presented with flat ground and terrain geometry is not varied during training, it may fail to traverse non-flat terrains such as ...

## Core Idea
- As an alternative, we propose learning a single policy that encodes a structured family of locomotion strategies that solve training tasks in different ways, resulting in Multiplicity of ...
- During training, the agent receives a combination of task rewards (for velocity tracking), fixed auxiliary rewards (to promote sim-to-real transfer and stable motion), and finally augmented auxiliary rewards ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- This necessitates a slow and iterative cycle of reward and environment redesign to achieve good performance on a new task.
- MoB facilitates this if some subset of learned behaviors outperform the gait-free policy by the new task metric.
- To start, we demonstrate generating and switching between structured gaits that are well-known in the locomotion community.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- As an alternative, we propose learning a single policy that encodes a structured family of locomotion strategies that solve training tasks in different ways, resulting in Multiplicity of ...
- : Learned locomotion policies can rapidly adapt to diverse environments similar to those experienced during training but lack a mechanism for fast tuning when they fail in an ...
- Different strategies generalize differently and can be chosen in real-time for new tasks or environments, bypassing the need for time-consuming retraining.

## Abstract Cue
- : Learned locomotion policies can rapidly adapt to diverse environments similar to those experienced during training but lack a mechanism for fast tuning when they fail in an out-of-distribution test environment.
