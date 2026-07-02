# HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting

- Year/Venue: 2025 / RA-L
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, Gaussian Splatting, semantic
- Paper link: ./2025/RA-L/2025_RA-L_HAMMER-Heterogeneous-Multi-Robot-Semantic-Gaussian-Splatti/paper.pdf
- Code/Project: https://hammer-project.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, efficient real-time map reconstruction with data streamed from multiple robots and devices remains a challenge.

## Core Idea
- To that end, we propose HAMMER, a server-based multi-robot Gaussian Splatting method that leverages ROS communication infrastructure to generate 3D, metric-semantic maps from asynchronous robot data-streams.
- HAMMER consists of (i) a one-time frame alignment module that transforms local SLAM poses and image data into a global frame and requires no prior relative pose knowledge, ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Radiance field-based methods can achieve photorealistic novel-view synthesis and even capture thin, transparent, and reflective surface geometries that are challenging to model with traditional representations.
- In real-world experiments, HAMMER creates better maps compared to baselines and is useful for downstream tasks, such as semantic navigation (e.g., “go to the couch”).

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To that end, we propose HAMMER, a server-based multi-robot Gaussian Splatting method that leverages ROS communication infrastructure to generate 3D, metric-semantic maps from asynchronous robot data-streams.
- HAMMER consists of (i) a one-time frame alignment module that transforms local SLAM poses and image data into a global frame and requires no prior relative pose knowledge, ...
- —3D Gaussian Splatting offers expressive scene reconstruction and can model a broad range of visual, geometric, and semantic information.

## Abstract Cue
- —3D Gaussian Splatting offers expressive scene reconstruction and can model a broad range of visual, geometric, and semantic information.
