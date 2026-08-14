# Method

- Year/Venue: 2024 / CoRL
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, locomotion, model-based reinforcement learning, real-world learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/utexas.edu/ssrl
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We introduce a novel framework for learning semi-structured dynamics models for contact-rich systems which seamlessly integrates structured first principles modeling techniques with black-box auto-regressive models.
- Specifically, we develop an ensemble of probabilistic models to estimate external forces, conditioned on historical observations and actions, and integrate these predictions using known Lagrangian dynamics.
- We validate our approach on a realworld Unitree Go1 quadruped robot, learning dynamic gaits – from scratch – on both hard and soft surfaces with just a few ...

## 원리적 동기
- Indeed, modeling contact remains an open problem.
- Effective robotic agents must leverage complex interactions between the robot and its environment, which are difficult to model using first principles.
- We introduce a novel framework for learning semi-structured dynamics models for contact-rich systems which seamlessly integrates structured first principles modeling techniques with black-box auto-regressive models.

## 핵심 방법론
- We inspire our approach by looking to the Lagrangian equation of motion for the robot: M (q)q̈ + C(q, q̇) + G(q) = Bτ + J T F ...
- We instantiate τ̂ e as an ensemble of probabilistic models to help 2 Figure 3: Control architecture.
- This general approach has been used for efficient system identification and controller synthesis across many bodies of work, ranging from classic adaptive control techniques to more recent physics-informed ...
- When the model is accurate, it can generate long rollouts which extrapolate beyond the training data, accelerating policy learning substantially.
- We consider the case where the robot’s observations only include proprioceptive measurements via joint encoders, IMU measurements, and a global velocity estimator.
