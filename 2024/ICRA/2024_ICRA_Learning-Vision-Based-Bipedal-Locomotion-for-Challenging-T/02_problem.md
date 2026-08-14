# Problem

- Year/Venue: 2024 / ICRA
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, bipedal locomotion, sim-to-real, Reinforcement Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Robustly achieving such an integration of vision and locomotion remains an open problem for bipedal robots.
- Modern control approaches for vision-based legged locomotion [1–8] often decompose the problem into a control hierarchy, requiring robust whole-body control, footstep planning, accurate odometry estimation, and terrain mapping.
- However, such blind controllers will fail in environments where robots must anticipate and adapt to local terrain, which requires visual perception.

## 해결하려는 문제
- In this paper, we propose a fully-learned system that allows bipedal robots to react to local terrain while maintaining commanded travel speed and direction.
- Our approach first trains a controller in simulation using a heightmap expressed in the robot’s local frame.
- We demonstrate that with appropriate domain randomization, this approach allows for successful sim-to-real transfer with no explicit pose estimation and no fine-tuning using real-world data.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
