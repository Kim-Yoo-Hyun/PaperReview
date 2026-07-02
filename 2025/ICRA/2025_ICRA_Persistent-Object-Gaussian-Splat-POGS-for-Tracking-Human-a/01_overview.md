# Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects

- Year/Venue: 2025 / ICRA
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, Gaussian Splatting, Reinforcement Learning
- Paper link: ./2025/ICRA/2025_ICRA_Persistent-Object-Gaussian-Splat-POGS-for-Tracking-Human-a/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The challenge is greater when dealing with irregularly shaped objects for which obtaining an accurate Computer-Aided Design (CAD) model is impractical.
- Recently introduced Gaussian Splats efficiently model object geometry, but lack persistent state estimation for taskoriented manipulation.
- However, many of these approaches fail to effectively integrate geometric information across multiple object viewpoints or timesteps, and do not address the estimation or reconstruction of occluded object ...

## Core Idea
- We present Persistent Object Gaussian Splat (POGS), a system that embeds semantics, self-supervised visual features, and object grouping features into a compact representation that can be continuously updated ...
- After an initial multi-view scene capture and training phase, POGS uses a single stereo camera to integrate depth estimates along with self-supervised vision encoder features for object pose ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- POGS achieves up to 12 consecutive successful object resets and recovers from 80% of in-grasp tool perturbations.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We present Persistent Object Gaussian Splat (POGS), a system that embeds semantics, self-supervised visual features, and object grouping features into a compact representation that can be continuously updated ...
- After an initial multi-view scene capture and training phase, POGS uses a single stereo camera to integrate depth estimates along with self-supervised vision encoder features for object pose ...
- Recently introduced Gaussian Splats efficiently model object geometry, but lack persistent state estimation for taskoriented manipulation.

## Abstract Cue
- — Tracking and manipulating irregularly-shaped, previously unseen objects in dynamic environments is important for robotic applications in manufacturing, assembly, and logistics.
