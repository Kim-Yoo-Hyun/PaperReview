# Problem

- Year/Venue: 2024 / CoRL
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, sequential contacts, Reinforcement Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://wococo-humanoid.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- In WoCoCo, we reformulate the problem as the sequential fulfillment of multiple contact stages (detailed in Section 2), which also breaks down the exploration burden into separate stages.
- This then transforms each challenge to a question: Q1: How to reach desired contact states within each stage?
- This drives the robot to explore further stages to maximize cumulative rewards, thus mitigating the shortsightedness caused by the RL policy strategically staying in the current stage to ...

## 해결하려는 문제
- In this work, we propose WoCoCo (Whole-Body Control with Sequential Contacts), a unified framework to learn whole-body humanoid control with sequential contacts by naturally decomposing the tasks into ...
- We demonstrated that endto-end RL-based controllers trained with WoCoCo enable four challenging wholebody humanoid tasks involving diverse contact sequences in the real world without any motion priors: 1) ...
- We further show that WoCoCo is a general framework beyond humanoid by applying it in 22-DoF dinosaur robot loco-manipulation tasks.

## 선행 연구 / 배경 단서
- In WoCoCo, we reformulate the problem as the sequential fulfillment of multiple contact stages (detailed in Section 2), which also breaks down the exploration burden into separate stages.
- Besides, regarding effective policy learning, we also identify three challenges: (1) Contacts are sparse, especially when coupled with other whole-body motion goals such as balancing and posture maintenance; ...
- This then transforms each challenge to a question: Q1: How to reach desired contact states within each stage?
