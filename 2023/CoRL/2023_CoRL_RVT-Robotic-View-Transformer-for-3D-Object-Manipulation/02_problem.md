# Problem

- Year/Venue: 2023 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D manipulation, Transformer
- Paper link: ./2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/paper.pdf
- Code/Project: https://robotic-view-transformer.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- In simulations, we find that a single RVT model works well across 18 RLBench tasks with 249 task variations, achieving 26% higher relative success than the existing stateof-the-art ...
- But using explicit 3D representations like voxels comes at large computing cost, adversely affecting scalability.

## 해결하려는 문제
- In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate.
- Visual results, code, and trained model are provided at: https://robotic-view-transformer.github.io/.
- Some key features of RVT are an attention mechanism to aggregate information across views and re-rendering of the camera input from virtual views around the robot workspace.

## 선행 연구 / 배경 단서
- A fundamental goal of robot learning is to build systems that can solve various manipulation tasks in unconstrained 3D settings.
- A popular class of learning methods directly processes image(s) viewed from single or multiple cameras.
- These view-based methods have achieved impressive success on a variety of pick-and-place and object rearrangement tasks .
