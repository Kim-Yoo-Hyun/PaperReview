# Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps

- Year/Venue: 2025 / IROS
- Category: Navigation and Embodied AI
- Tags: Robotics, Navigation, Gaussian Splatting
- Paper link: ./2025/IROS/2025_IROS_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We use a language-embedded GSplat to enable open-vocabulary specification of goal locations like “go to the microwave.” of the existing localization module or used as a correction mechanism ...

## Core Idea
- —We present Splat-Nav, a real-time robot navigation pipeline for Gaussian Splatting (GSplat) scenes, a powerful new 3D scene representation.
- We present a brief introduction to 3D Gaussian uses the predicted depth map at sampled poses to enforce Splatting , a radiance field method for deriving volumetric step-wise ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We demonstrate improved safety compared to point cloudbased methods in extensive simulation experiments.
- In a total of 126 hardware flights, we demonstrate equivalent safety and speed compared to motion capture and visual odometry, but without a manual frame alignment required by ...
- We show online re-planning at more than 2 Hz and pose estimation at about 25 Hz, an order of magnitude faster than Neural Radiance Field (NeRF)-based navigation methods, ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- —We present Splat-Nav, a real-time robot navigation pipeline for Gaussian Splatting (GSplat) scenes, a powerful new 3D scene representation.
- We demonstrate improved safety compared to point cloudbased methods in extensive simulation experiments.
- 1: Splat-Nav, consists of a safe planning module, Splat-Plan, and robust localization module, Splat-Loc, both operating on a Gaussian Splatting environment representation.

## Abstract Cue
- —We present Splat-Nav, a real-time robot navigation pipeline for Gaussian Splatting (GSplat) scenes, a powerful new 3D scene representation.
