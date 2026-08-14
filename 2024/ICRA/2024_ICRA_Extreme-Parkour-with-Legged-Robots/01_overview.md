# Extreme Parkour with Legged Robots

- Year/Venue: 2024 / ICRA
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, quadruped locomotion, parkour, Reinforcement Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://extreme-parkour.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- However, low cost poses a new challenge for parkour which is not as prominent in prior walking works.
- Second, each parkour behavior from jumping to handstand are very different in nature, so combining them within a single neural network is a challenging learning problem.
- In addition to precise control from noisy actuation, training extreme parkour controllers has two conceptual challenges as well.

## Core Idea
- Humans can perform parkour by traversing obstacles in a highly dynamic fashion requiring precise eye-muscle coordination and movement.
- Getting robots to do the same task requires overcoming similar challenges.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- 7 4.2 Emergent results . . . . . . . . . . . . . . . . . . . . . . . . ...
- We show how a single neural net policy operating directly from a camera image, trained in simulation with largescale RL, can overcome imprecise sensing and actuation to output ...
- We show our robot can perform a high jump on obstacles 2x its height, long jump across gaps 2x its length, do a handstand and run across tilted ...

## Limitation
- We found that even if a human expert is providing the heading direction, it is sub-optimal because in extremely long or high jumps over obstacles or ramps, even ...
- Even if the actions were correct, executing them on laggy and noisy actuators will lead to catastrophic failure.
- However, low cost poses a new challenge for parkour which is not as prominent in prior walking works.

## Contribution
- We show how a single neural net policy operating directly from a camera image, trained in simulation with largescale RL, can overcome imprecise sensing and actuation to output ...
- We show our robot can perform a high jump on obstacles 2x its height, long jump across gaps 2x its length, do a handstand and run across tilted ...
- Getting robots to do the same task requires overcoming similar challenges.

## Abstract Cue
- Humans can perform parkour by traversing obstacles in a highly dynamic fashion requiring precise eye-muscle coordination and movement.
