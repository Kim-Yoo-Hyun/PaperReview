# Method

- Year/Venue: 2024 / ICRA
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, quadruped locomotion, parkour, Reinforcement Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://extreme-parkour.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- Humans can perform parkour by traversing obstacles in a highly dynamic fashion requiring precise eye-muscle coordination and movement.
- Getting robots to do the same task requires overcoming similar challenges.
- Classically, this is done by independently engineering perception, actuation, and control systems to very low tolerances.

## 원리적 동기
- However, low cost poses a new challenge for parkour which is not as prominent in prior walking works.
- Second, each parkour behavior from jumping to handstand are very different in nature, so combining them within a single neural network is a challenging learning problem.
- Humans can perform parkour by traversing obstacles in a highly dynamic fashion requiring precise eye-muscle coordination and movement.

## 핵심 방법론
- 4 3.1 Unified Reward for Extreme Parkour . . . . . . . . . . . . . . . . . . . . . ...
- 5 3.2 Reinforcement Learning from Scandots (Phase 1) . . . . . . . . . . . . . . . . . .
- 6 3.3 Distilling Direction and Exteroception (Phase 2) . . . . . . . . . . . . . . . . . . .
