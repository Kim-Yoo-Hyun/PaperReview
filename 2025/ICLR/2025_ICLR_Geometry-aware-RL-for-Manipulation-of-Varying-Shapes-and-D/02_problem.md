# Problem

- Year/Venue: 2025 / ICLR Oral
- Category: Robot Learning and Data
- Tags: Robotics, Reinforcement Learning, SE(3) equivariance, deformable manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://thobotics.github.io/hepi
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- These tasks present a range of manipulation challenges, emphasizing the role of geometric structure and requiring complex exploration strategies to coordinate the agents in completing the tasks.

## 해결하려는 문제
- We introduce two categories of tasks: rigid manipulation on diverse geometries and deformable object manipulation, all implemented in NVIDIA IsaacLab (Mittal et al., 2023) to leverage its GPU-based ...
- Additionally, we introduce a novel Rigid-Insertion-Two-Agents task, where two linear actuators work together to control an object, guiding it to a target randomly positioned in the upper hemisphere ...
- Finally, we introduce Cloth-Hanging, where four actuators control the corners of a cloth to hang it onto a hanger, with randomized starting positions and orientations in 3D space.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
