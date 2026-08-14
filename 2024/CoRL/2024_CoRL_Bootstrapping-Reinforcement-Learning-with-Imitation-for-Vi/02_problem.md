# Problem

- Year/Venue: 2024 / CoRL
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, aerial robotics, Reinforcement Learning, Imitation Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://bootstrap-rl-with-il.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Thus, the ability to explore and learn efficiently in vision-based RL environments from scratch is essential, presenting a key challenge that our research seeks to overcome.
- Due to this simplification, IL typically requires fewer samples and, consequently, has been validated for real-world robot learning problems .
- However, learning from only visual inputs introduces a range of distinct challenges.

## 해결하려는 문제
- Testing in both simulated and real-world scenarios shows our approach can not only learn in scenarios where RL from scratch fails but also outperforms existing IL methods in ...
- To address these challenges, we propose a novel approach that combines the performance of Reinforcement Learning (RL) and the sample efficiency of Imitation Learning (IL) in the task ...
- Our framework contains three phases: training a teacher policy using RL with privileged state information, distilling it into a student policy via IL, and adaptive fine-tuning via RL.

## 선행 연구 / 배경 단서
- Through experiments in both simulation and real-world environments, we demonstrate that our approach, given the same sample budget, outperforms existing IL methods in robustness and performance and succeeds ...
- Thus, the ability to explore and learn efficiently in vision-based RL environments from scratch is essential, presenting a key challenge that our research seeks to overcome.
- Due to this simplification, IL typically requires fewer samples and, consequently, has been validated for real-world robot learning problems .
