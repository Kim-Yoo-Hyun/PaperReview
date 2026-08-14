# Problem

- Year/Venue: 2024 / CoRL
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, locomotion, model-based reinforcement learning, real-world learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/utexas.edu/ssrl
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Indeed, modeling contact remains an open problem.
- Effective robotic agents must leverage complex interactions between the robot and its environment, which are difficult to model using first principles.
- However, in practice, the black-box neural network models favored in the ∗ These authors contributed equally.

## 해결하려는 문제
- We introduce a novel framework for learning semi-structured dynamics models for contact-rich systems which seamlessly integrates structured first principles modeling techniques with black-box auto-regressive models.
- However, training data are typically scarce in practice, and these black-box models often fail to generalize.
- Specifically, we develop an ensemble of probabilistic models to estimate external forces, conditioned on historical observations and actions, and integrate these predictions using known Lagrangian dynamics.

## 선행 연구 / 배경 단서
- Indeed, modeling contact remains an open problem.
- Effective robotic agents must leverage complex interactions between the robot and its environment, which are difficult to model using first principles.
- However, in practice, the black-box neural network models favored in the ∗ These authors contributed equally.
