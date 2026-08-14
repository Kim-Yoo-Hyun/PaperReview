# Problem

- Year/Venue: 2016 / Autonomous Robots
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, humanoid, whole-body control, momentum control, inverse dynamics
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://is.mpg.de/am/publications/herzog_momentum_2016
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Using a reformulation of existing algorithms, we propose a simplification of the problem that allows to achieve real-time control.
- They have important benefits but to the best of our knowledge have never been implemented on a torque controlled humanoid where model inaccuracies, sensor noise and real-time computation ...

## 해결하려는 문제
- Using a reformulation of existing algorithms, we propose a simplification of the problem that allows to achieve real-time control.
- Our results demonstrate that hierarchical inverse dynamics together with momentum control can be efficiently used for feedback control under real robot conditions.
- Extensive experiments on various balancing and tracking tasks show very robust performance in the face of unknown disturbances, even when the humanoid is standing on one foot.

## 선행 연구 / 배경 단서
- 1 We expect autonomous legged robots to perform complex tasks in persistent interaction with an uncertain and changing environment (e.g. in a disaster relief scenario).
- Therefore, we need to design algorithms that can generate precise but compliant motions while optimizing the interactions with the environment.
- In this context, the choice of a control strategy for legged robots is of primary importance as it can drastically improve performance in the face of unexpected disturbances ...
