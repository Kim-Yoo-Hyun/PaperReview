# Problem

- Year/Venue: 2022 / CoRL
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, quadruped locomotion, Reinforcement Learning, behavior diversity
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/walk-these-ways
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- However, this creates a hard learning problem due to creation of challenging or infeasible locomotion scenarios.
- The examples above illustrate that even for the most advanced sim-to-real systems, the real world offers new challenges.
- For instance, if the robot is only presented with flat ground and terrain geometry is not varied during training, it may fail to traverse non-flat terrains such as ...

## 해결하려는 문제
- As an alternative, we propose learning a single policy that encodes a structured family of locomotion strategies that solve training tasks in different ways, resulting in Multiplicity of ...
- : Learned locomotion policies can rapidly adapt to diverse environments similar to those experienced during training but lack a mechanism for fast tuning when they fail in an ...
- Different strategies generalize differently and can be chosen in real-time for new tasks or environments, bypassing the need for time-consuming retraining.

## 선행 연구 / 배경 단서
- However, this creates a hard learning problem due to creation of challenging or infeasible locomotion scenarios.
- For instance, if the robot is only presented with flat ground and terrain geometry is not varied during training, it may fail to traverse non-flat terrains such as ...
- The examples above illustrate that even for the most advanced sim-to-real systems, the real world offers new challenges.
