# Method

- Year/Venue: 2019 / Science Robotics
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, legged locomotion, Reinforcement Learning, sim-to-real
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://leggedrobotics.github.io/rl-blindloco/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We used a simple parameterized controller that generates foot trajectories in the form of a sine wave; the corresponding joint positions were computed using inverse kinematics.
- We use a history consisting of the current state and two past states that correspond to t − 0.01 and t − 0.02 seconds.
- To this end, we use supervised learning to obtain an actionto-torque relationship that includes all software and hardware dynamics within one control loop.

## 원리적 동기
- Legged robotic systems are attractive alternatives to tracked/wheeled robots for applications in rough terrain and complex cluttered environments.
- Their freedom to choose contact points with the environment enables them to overcome obstacles comparable to their leg length.
- We used a simple parameterized controller that generates foot trajectories in the form of a sine wave; the corresponding joint positions were computed using inverse kinematics.

## 핵심 방법론
- We used a simple parameterized controller that generates foot trajectories in the form of a sine wave; the corresponding joint positions were computed using inverse kinematics.
- We use a history consisting of the current state and two past states that correspond to t − 0.01 and t − 0.02 seconds.
- To this end, we use supervised learning to obtain an actionto-torque relationship that includes all software and hardware dynamics within one control loop.
- We found that the excitation must cover a wide range of frequency spectra since, otherwise, the trained model generates unnatural oscillation even during the training phase.
- This section describes in detail the simulation environment, the training process, and the deployment on the physical system.
