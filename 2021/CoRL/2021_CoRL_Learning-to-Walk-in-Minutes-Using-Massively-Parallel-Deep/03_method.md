# Method

- Year/Venue: 2021 / CoRL
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, locomotion, Reinforcement Learning, massively parallel simulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://leggedrobotics.github.io/legged_gym/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- In addition, we present a novel game-inspired curriculum that is well suited for training with thousands of simulated robots in parallel.
- : In this work, we present and study a training set-up that achieves fast policy generation for real-world robotic tasks by using massive parallelism on a single workstation ...
- In this work, we use NVIDIA’s Isaac Gym simulation environment , which runs both the simulation and training on the GPU and is capable of simulating thousands of ...

## 원리적 동기
- The problem is exacerbated by the fact that deep 5th Conference on Robot Learning (CoRL 2021), London, UK. reinforcement learning requires hyper-parameter tuning to obtain a suitable solution ...
- Additionally, we present a novel game-inspired curriculum which automatically adapts the task difficulty to the performance of the policy.
- In addition, we present a novel game-inspired curriculum that is well suited for training with thousands of simulated robots in parallel.

## 핵심 방법론
- In this work, we use NVIDIA’s Isaac Gym simulation environment , which runs both the simulation and training on the GPU and is capable of simulating thousands of ...
- Additionally, we present a novel game-inspired curriculum which automatically adapts the task difficulty to the performance of the policy.
- With our approach we can train a perceptive policy in under 20 minutes on a single GPU, with the complexity of simto-real transfer to the hardware, which increases ...
- We build upon by pushing the parallelization further, optimizing the training algorithm, and applying the approach to a challenging real-world robotics task.
- The proposed curriculum architecture is straightforward to implement, does not require tuning, and is well suited for the massively parallel regime.
