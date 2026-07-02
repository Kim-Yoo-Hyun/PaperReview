# Problem

- Year/Venue: 2025 / IROS
- Category: Navigation and Embodied AI
- Tags: Navigation, Gaussian Splatting
- Paper link: ./2025/IROS/2025_IROS_GRaD-Nav-Efficiently-Learning-Visual-Drone-Navigation-with/paper.pdf
- Code/Project: https://qianzhong-chen.github.io/gradnav.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- These problems are particularly challenging for drones, with complex nonlinear and unstable dynamics, and strong dynamic coupling between control and perception.
- Traditional approaches to this problem have predominantly relied on a stack of different modules including perception, localization, mapping, planning, and control –.
- However, the integration of these different modules has many issues, including high system complexity and computational overhead, communication latency between modules, multiple points of failure, and difficult-to-characterize error ...

## 해결하려는 문제
- Drone hardware experiments demonstrate our method’s high training efficiency compared to state-of-theart RL methods, zero shot sim-to-real transfer for real robot deployment without fine tuning, and ability to ...
- In this paper, we propose a novel framework that integrates 3D Gaussian Splatting (3DGS) with differentiable deep reinforcement learning (DDRL) to train vision-based drone navigation policies.
- By leveraging highfidelity 3D scene representations and differentiable simulation, our method improves sample efficiency and sim-to-real transfer.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
