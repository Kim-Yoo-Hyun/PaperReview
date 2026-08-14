# Problem

- Year/Venue: 2021 / CoRL
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, locomotion, Reinforcement Learning, massively parallel simulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://leggedrobotics.github.io/legged_gym/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- The problem is exacerbated by the fact that deep 5th Conference on Robot Learning (CoRL 2021), London, UK. reinforcement learning requires hyper-parameter tuning to obtain a suitable solution ...
- Additionally, we present a novel game-inspired curriculum which automatically adapts the task difficulty to the performance of the policy.
- This represents a speedup of multiple orders of magnitude compared to previous work.

## 해결하려는 문제
- : In this work, we present and study a training set-up that achieves fast policy generation for real-world robotic tasks by using massive parallelism on a single workstation ...
- In addition, we present a novel game-inspired curriculum that is well suited for training with thousands of simulated robots in parallel.
- We evaluate the approach by training the quadrupedal robot ANYmal to walk on challenging terrain.

## 선행 연구 / 배경 단서
- The problem is exacerbated by the fact that deep 5th Conference on Robot Learning (CoRL 2021), London, UK. reinforcement learning requires hyper-parameter tuning to obtain a suitable solution ...
- Additionally, we present a novel game-inspired curriculum which automatically adapts the task difficulty to the performance of the policy.
- In this work, we use NVIDIA’s Isaac Gym simulation environment , which runs both the simulation and training on the GPU and is capable of simulating thousands of ...
