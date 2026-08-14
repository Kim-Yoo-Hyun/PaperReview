# Problem

- Year/Venue: 2024 / ICRA
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, legged locomotion, Navigation, robust perception
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://bit.ly/45NBTuh
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Generally, given an accurate map, it is not difficult for existing navigation planners to guide the robot towards the local goal safely.
- In a quantitative comparison with existing heuristic-based locally reactive planners, our policy increases the success rate over 30 % when facing perception failures.
- Unlike previous works relying on heuristics and anomaly detection to update navigational information, we train our navigation policy to reconstruct the environment information in the latent space from ...

## 해결하려는 문제
- We validate our approach in simulation and on the real quadruped robot ANYmal running in real-time (<10 ms CPU inference).
- Generally, given an accurate map, it is not difficult for existing navigation planners to guide the robot towards the local goal safely.
- In a quantitative comparison with existing heuristic-based locally reactive planners, our policy increases the success rate over 30 % when facing perception failures.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
