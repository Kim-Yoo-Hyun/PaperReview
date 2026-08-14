# Problem

- Year/Venue: 2025 / CoRL Poster
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, locomotion, end-effector stabilization, multi-rate control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://lecar-lab.github.io/SoFTA/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- While humanoids are increasingly featured in flashy demos—dancing, delivering packages, traversing rough terrain—fine-grained control during locomotion remains a significant challenge.

## 해결하려는 문제
- To address this, we propose SoFTA, a Slow-Fast Two-Agent framework that decouples upper-body and lower-body control into separate agents operating at different frequencies and with distinct rewards.
- While humanoids are increasingly featured in flashy demos—dancing, delivering packages, traversing rough terrain—fine-grained control during locomotion remains a significant challenge.

## 선행 연구 / 배경 단서
- To bridge the gap, we propose SoFTA—a Slow-Fast Two-Agent reinforcement learning (RL) framework that decouples the action and value spaces of the upper and lower body.
- Our key contributions are: • We introduce SoFTA, a novel slow-fast two-agent RL framework that decouples control for locomotion and EE stabilization in both temporal and task objective ...
- SoFTA facilitates stable training and whole-body coordination by this decoupling, resulting in fast and accurate EE control alongside robust locomotion.
