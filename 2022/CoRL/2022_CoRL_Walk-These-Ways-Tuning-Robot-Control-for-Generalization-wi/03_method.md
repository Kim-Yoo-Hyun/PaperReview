# Method

- Year/Venue: 2022 / CoRL
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, quadruped locomotion, Reinforcement Learning, behavior diversity
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/walk-these-ways
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- As an alternative, we propose learning a single policy that encodes a structured family of locomotion strategies that solve training tasks in different ways, resulting in Multiplicity of ...
- During training, the agent receives a combination of task rewards (for velocity tracking), fixed auxiliary rewards (to promote sim-to-real transfer and stable motion), and finally augmented auxiliary rewards ...
- Different strategies generalize differently and can be chosen in real-time for new tasks or environments, bypassing the need for time-consuming retraining.

## 원리적 동기
- However, this creates a hard learning problem due to creation of challenging or infeasible locomotion scenarios.
- The examples above illustrate that even for the most advanced sim-to-real systems, the real world offers new challenges.
- As an alternative, we propose learning a single policy that encodes a structured family of locomotion strategies that solve training tasks in different ways, resulting in Multiplicity of ...

## 핵심 방법론
- During training, the agent receives a combination of task rewards (for velocity tracking), fixed auxiliary rewards (to promote sim-to-real transfer and stable motion), and finally augmented auxiliary rewards ...
