# Problem

- Year/Venue: 2026 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, contact-rich manipulation, model predictive control, non-prehensile manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://dairlab.github.io/push-anything
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- — Non-prehensile manipulation of diverse objects remains a core challenge in robotics, driven by unknown physical properties and the complexity of contact-rich interactions.
- I NTRODUCTION A key challenge in robotic manipulation is planning dynamic, contact-rich motions with objects of arbitrary geometries, especially within cluttered, multi-contact environments.
- To address this limitation, Venkatesh, Bianchini et al. augment CI-MPC, specifically using Consensus Complementarity Control (C3) , with global exploration through low-dimensional sampling of end effector positions.

## 해결하려는 문제
- To achieve this, we introduce Consensus Complementarity Control Plus (C3+), an enhanced CI-MPC algorithm integrated into a complete pipeline spanning object scanning, mesh reconstruction, and hardware execution.
- On hardware, our system achieves overall 98% success rate across 33 objects, reaching pose goals within tight tolerances.
- Compared to its predecessor C3, C3+ achieves substantially faster solve times, enabling real-time performance even in multi-object pushing tasks.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
