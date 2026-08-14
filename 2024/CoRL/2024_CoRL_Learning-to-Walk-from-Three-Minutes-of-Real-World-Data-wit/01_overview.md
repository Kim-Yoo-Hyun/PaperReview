# Learning to Walk from Three Minutes of Real-World Data with Semi-structured Dynamics Models

- Year/Venue: 2024 / CoRL
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, locomotion, model-based reinforcement learning, real-world learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/utexas.edu/ssrl
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Indeed, modeling contact remains an open problem.
- Effective robotic agents must leverage complex interactions between the robot and its environment, which are difficult to model using first principles.
- However, in practice, the black-box neural network models favored in the ∗ These authors contributed equally.

## Core Idea
- We introduce a novel framework for learning semi-structured dynamics models for contact-rich systems which seamlessly integrates structured first principles modeling techniques with black-box auto-regressive models.
- Specifically, we develop an ensemble of probabilistic models to estimate external forces, conditioned on historical observations and actions, and integrate these predictions using known Lagrangian dynamics.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Video and code are available at: https://sites.google.com/utexas.edu/ssrl 4.1 Real-world Results We demonstrate our approach through two real-world experiments where a Unitree Go1 quadruped is trained from scratch to ...
- 4.2 Simulated Experiments In addition to the results presented here, we provide extensive ablations on standard RL benchmarks in Appendix C.
- Predictions from semi-structured dynamics models demonstrate greater accuracy and improved generalization beyond training data compared to black-box models.

## Limitation
- However there are several key limitations.

## Contribution
- We introduce a novel framework for learning semi-structured dynamics models for contact-rich systems which seamlessly integrates structured first principles modeling techniques with black-box auto-regressive models.
- However, training data are typically scarce in practice, and these black-box models often fail to generalize.
- Specifically, we develop an ensemble of probabilistic models to estimate external forces, conditioned on historical observations and actions, and integrate these predictions using known Lagrangian dynamics.

## Abstract Cue
- : Traditionally, model-based reinforcement learning (MBRL) methods exploit neural networks as flexible function approximators to represent a priori unknown environment dynamics.
