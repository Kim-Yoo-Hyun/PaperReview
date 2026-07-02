# GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics

- Year/Venue: 2025 / IROS
- Category: Navigation and Embodied AI
- Tags: Navigation, Gaussian Splatting
- Paper link: ./2025/IROS/2025_IROS_GRaD-Nav-Efficiently-Learning-Visual-Drone-Navigation-with/paper.pdf
- Code/Project: https://qianzhong-chen.github.io/gradnav.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- These problems are particularly challenging for drones, with complex nonlinear and unstable dynamics, and strong dynamic coupling between control and perception.
- Traditional approaches to this problem have predominantly relied on a stack of different modules including perception, localization, mapping, planning, and control –.
- However, the integration of these different modules has many issues, including high system complexity and computational overhead, communication latency between modules, multiple points of failure, and difficult-to-characterize error ...

## Core Idea
- In this paper, we propose a novel framework that integrates 3D Gaussian Splatting (3DGS) with differentiable deep reinforcement learning (DDRL) to train vision-based drone navigation policies.
- C ONCLUSIONS In this paper, we present a novel framework that integrates 3DGS with DDRL to train a vision-based drone navigation policy.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Moreover, by curriculum training in a mixture of different surrounding environments, we achieve in-task generalization, the ability to solve new instances of a task not seen during training.
- Drone hardware experiments demonstrate our method’s high training efficiency compared to state-of-theart RL methods, zero shot sim-to-real transfer for real robot deployment without fine tuning, and ability to ...
- By leveraging highfidelity 3D scene representations and differentiable simulation, our method improves sample efficiency and sim-to-real transfer.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Drone hardware experiments demonstrate our method’s high training efficiency compared to state-of-theart RL methods, zero shot sim-to-real transfer for real robot deployment without fine tuning, and ability to ...
- In this paper, we propose a novel framework that integrates 3D Gaussian Splatting (3DGS) with differentiable deep reinforcement learning (DDRL) to train vision-based drone navigation policies.
- By leveraging highfidelity 3D scene representations and differentiable simulation, our method improves sample efficiency and sim-to-real transfer.

## Abstract Cue
- — Autonomous visual navigation is an essential element in robot autonomy.
