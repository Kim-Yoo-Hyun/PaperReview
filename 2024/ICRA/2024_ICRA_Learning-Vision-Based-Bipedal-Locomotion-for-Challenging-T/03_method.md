# Method

- Year/Venue: 2024 / ICRA
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, bipedal locomotion, sim-to-real, Reinforcement Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- In this paper, we propose a fully-learned system that allows bipedal robots to react to local terrain while maintaining commanded travel speed and direction.
- C ONCLUSION In this work, we proposed a fully learned visual-locomotion system using neural networks.
- Our approach first trains a controller in simulation using a heightmap expressed in the robot’s local frame.

## 원리적 동기
- Robustly achieving such an integration of vision and locomotion remains an open problem for bipedal robots.
- Modern control approaches for vision-based legged locomotion [1–8] often decompose the problem into a control hierarchy, requiring robust whole-body control, footstep planning, accurate odometry estimation, and terrain mapping.
- In this paper, we propose a fully-learned system that allows bipedal robots to react to local terrain while maintaining commanded travel speed and direction.

## 핵심 방법론
- C ONCLUSION In this work, we proposed a fully learned visual-locomotion system using neural networks.
- We use the same metrics used in policy performance.
- To deal with constrained locomotion over complex terrains, we used simulation to train a robust control policy, considering adaptive gaits and collision-free swing leg.
