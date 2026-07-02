# FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry

- Year/Venue: 2026 / IROS
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, Vision-Language
- Paper link: ./2026/IROS/2026_IROS_FAST-LIVGO-A-Degeneracy-Robust-LiDAR-Inertial-Visual-GNSS/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address these limitations, we propose a tightly coupled LiDAR-Inertial-Visual-GNSS fusion framework based on an Error-State Iterated Kalman Filter.
- — Robust state estimation and mapping in long-term, large-scale, and highly dynamic environments remains a key challenge in robotics.
- INTRODUCTION Achieving robust state estimation and environmental mapping in complex, large-scale, and highly dynamic environments remains a core challenge for autonomous systems .

## Core Idea
- To address these limitations, we propose a tightly coupled LiDAR-Inertial-Visual-GNSS fusion framework based on an Error-State Iterated Kalman Filter.
- To better exploit GNSS precision, we develop observation models based on Doppler shifts and fixed-anchor Time-Differenced Carrier Phase, providing millimeter-level relative constraints without augmenting historical anchor states.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments on the public M3DGR dataset and a custom 20 m/s fixed-wing UAV dataset demonstrate that our system reduces accumulated drift and map ghosting, outperforming state-of-the-art methods in ...
- Existing LiDAR-Inertial-Visual Odometry (LIVO) systems achieve strong local accuracy but suffer from accumulated drift over long distances and may fail in geometrically degraded or textureless scenes.
- To overcome single-sensor limitations, multi-sensor fusion, especially LiDAR-Inertial-Visual Odometry (LIVO), has been widely adopted by combining LiDAR’s geometric accuracy with the camera’s robustness in texture-rich areas –, while ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments on the public M3DGR dataset and a custom 20 m/s fixed-wing UAV dataset demonstrate that our system reduces accumulated drift and map ghosting, outperforming state-of-the-art methods in ...
- To address these limitations, we propose a tightly coupled LiDAR-Inertial-Visual-GNSS fusion framework based on an Error-State Iterated Kalman Filter.
- Existing LiDAR-Inertial-Visual Odometry (LIVO) systems achieve strong local accuracy but suffer from accumulated drift over long distances and may fail in geometrically degraded or textureless scenes.

## Abstract Cue
- — Robust state estimation and mapping in long-term, large-scale, and highly dynamic environments remains a key challenge in robotics.
