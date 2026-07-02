# Method

- Year/Venue: 2025 / IROS
- Category: Navigation and Embodied AI
- Tags: Navigation, Gaussian Splatting
- Paper link: ./2025/IROS/2025_IROS_GRaD-Nav-Efficiently-Learning-Visual-Drone-Navigation-with/paper.pdf
- Code/Project: https://qianzhong-chen.github.io/gradnav.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we propose a novel framework that integrates 3D Gaussian Splatting (3DGS) with differentiable deep reinforcement learning (DDRL) to train vision-based drone navigation policies.
- C ONCLUSIONS In this paper, we present a novel framework that integrates 3DGS with DDRL to train a vision-based drone navigation policy.
- Limitations: Our method relies on hand-crafted reward shaping (e.g., trajectory waypoints), limiting it to singletask execution like gate traversal.

## 원리적 동기
- These problems are particularly challenging for drones, with complex nonlinear and unstable dynamics, and strong dynamic coupling between control and perception.
- Traditional approaches to this problem have predominantly relied on a stack of different modules including perception, localization, mapping, planning, and control –.
- In this paper, we propose a novel framework that integrates 3D Gaussian Splatting (3DGS) with differentiable deep reinforcement learning (DDRL) to train vision-based drone navigation policies.

## 핵심 방법론
- C ONCLUSIONS In this paper, we present a novel framework that integrates 3DGS with DDRL to train a vision-based drone navigation policy.
- Limitations: Our method relies on hand-crafted reward shaping (e.g., trajectory waypoints), limiting it to singletask execution like gate traversal.
- By comparing three methods’ real robot test performance in Table V, we can conclude that (i) the sim-to-real gap of our method is reasonably low; (ii) CENet is ...
- By leveraging high-fidelity 3D scene representations and differentiable simulation, our approach enhances sample efficiency and sim-to-real transfer.
- Sim-to-real transfer of generalizable policy After training our policy as discussed in Section III-C.4, we rolled out the final policy and tested it in three different environments separately.
