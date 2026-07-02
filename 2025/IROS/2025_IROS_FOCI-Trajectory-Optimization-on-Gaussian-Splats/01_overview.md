# FOCI: Trajectory Optimization on Gaussian Splats

- Year/Venue: 2025 / IROS
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting
- Paper link: ./2025/IROS/2025_IROS_FOCI-Trajectory-Optimization-on-Gaussian-Splats/paper.pdf
- Code/Project: https://rffr.leggedrobotics.com/works/foci/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, they suffer from having slow inference speeds because new views have to be created using a computationally expensive ray-casting procedure.

## Core Idea
- Contrary to other approaches, which represent the robot with conservative bounding boxes that underestimate the traversability of the environment, we propose to represent the environment and the robot ...
- Safety Dist. (m) 0.51 0.56 0.27 TABLE III: Comparisons of the performance of our method with a similar 3DGS based planner and simple RRT* planner.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We extensively test our algorithm in both synthetic and real Gaussian Splats, showcasing that collision-free trajectories for the ANYmal legged robot that can be computed in a few ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Contrary to other approaches, which represent the robot with conservative bounding boxes that underestimate the traversability of the environment, we propose to represent the environment and the robot ...
- We extensively test our algorithm in both synthetic and real Gaussian Splats, showcasing that collision-free trajectories for the ANYmal legged robot that can be computed in a few ...
- — 3D Gaussian Splatting (3DGS) has recently gained popularity as a faster alternative to Neural Radiance Fields (NeRFs) in 3D reconstruction and view synthesis methods.

## Abstract Cue
- — 3D Gaussian Splatting (3DGS) has recently gained popularity as a faster alternative to Neural Radiance Fields (NeRFs) in 3D reconstruction and view synthesis methods.
