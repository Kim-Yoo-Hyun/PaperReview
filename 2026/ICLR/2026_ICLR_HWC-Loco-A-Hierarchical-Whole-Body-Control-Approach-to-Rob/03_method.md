# Method

- Year/Venue: 2026 / ICLR Poster
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, robust locomotion, safety recovery
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://simonlinsx.github.io/HWC_Loco/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- In this study, we propose HWCLoco, a robust whole-body control algorithm tailored for humanoid locomotion tasks.
- The robots are commanded to follow randomly sampled velocities within the training distribution while navigating a uniformly mixed terrain comprising flat ground, obstacles, slopes, and stairs.
- However, as robots with complex physical structures, learning a control model that can operate robustly across diverse environments remains inherently challenging, particularly under the discrepancies between training and ...

## 원리적 동기
- To develop a reliable locomotion policy capable of generalizing from the training to the deployment environment, we propose formulating policy optimization as a robust optimization problem under misspecified ...
- To address this limitation, we propose a high-level planning policy that dynamically selects which policy to activate based on the scenario.
- In this study, we propose HWCLoco, a robust whole-body control algorithm tailored for humanoid locomotion tasks.

## 핵심 방법론
- The robots are commanded to follow randomly sampled velocities within the training distribution while navigating a uniformly mixed terrain comprising flat ground, obstacles, slopes, and stairs.
