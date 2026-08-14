# Learning Vision-Based Bipedal Locomotion for Challenging Terrain

- Year/Venue: 2024 / ICRA
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, bipedal locomotion, sim-to-real, Reinforcement Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Robustly achieving such an integration of vision and locomotion remains an open problem for bipedal robots.
- Modern control approaches for vision-based legged locomotion [1–8] often decompose the problem into a control hierarchy, requiring robust whole-body control, footstep planning, accurate odometry estimation, and terrain mapping.
- However, such blind controllers will fail in environments where robots must anticipate and adapt to local terrain, which requires visual perception.

## Core Idea
- In this paper, we propose a fully-learned system that allows bipedal robots to react to local terrain while maintaining commanded travel speed and direction.
- C ONCLUSION In this work, we proposed a fully learned visual-locomotion system using neural networks.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We demonstrate that with appropriate domain randomization, this approach allows for successful sim-to-real transfer with no explicit pose estimation and no fine-tuning using real-world data.
- — Reinforcement learning (RL) for bipedal locomotion has recently demonstrated robust gaits over moderate terrains using only proprioceptive sensing.
- These approaches have shown strong empirical demonstrations of blind bipedal locomotion and vision-based quadrupedal locomotion [10–16] in realworld environments.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this paper, we propose a fully-learned system that allows bipedal robots to react to local terrain while maintaining commanded travel speed and direction.
- Our approach first trains a controller in simulation using a heightmap expressed in the robot’s local frame.
- We demonstrate that with appropriate domain randomization, this approach allows for successful sim-to-real transfer with no explicit pose estimation and no fine-tuning using real-world data.

## Abstract Cue
- — Reinforcement learning (RL) for bipedal locomotion has recently demonstrated robust gaits over moderate terrains using only proprioceptive sensing.
