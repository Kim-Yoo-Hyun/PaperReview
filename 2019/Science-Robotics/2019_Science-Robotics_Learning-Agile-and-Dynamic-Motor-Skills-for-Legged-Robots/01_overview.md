# Learning Agile and Dynamic Motor Skills for Legged Robots

- Year/Venue: 2019 / Science Robotics
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, legged locomotion, Reinforcement Learning, sim-to-real
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://leggedrobotics.github.io/rl-blindloco/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Legged robotic systems are attractive alternatives to tracked/wheeled robots for applications in rough terrain and complex cluttered environments.
- Their freedom to choose contact points with the environment enables them to overcome obstacles comparable to their leg length.
- With such capabilities, legged robots may one day rescue people in forests and mountains, climb stairs to carry payloads in construction sites, inspect unstructured underground tunnels, and explore ...

## Core Idea
- We used a simple parameterized controller that generates foot trajectories in the form of a sine wave; the corresponding joint positions were computed using inverse kinematics.
- We use a history consisting of the current state and two past states that correspond to t − 0.01 and t − 0.02 seconds.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We used the same velocity command profile which results in the base velocity shown in fig.
- In the following subsections, we describe the results in detail.
- Movie S1 summarizes the results and the method of this work.

## Limitation
- In contrast, due to many model-abstraction layers which are necessary to make the computation tractable, prior methods often cannot exploit a sophisticated actuator model in controlling a complex ...

## Contribution
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Abstract Cue
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
