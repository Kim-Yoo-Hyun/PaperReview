# WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting

- Year/Venue: 2026 / ICML
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_WorldMirror-Universal-3D-World-Reconstruction-with-Any-Pri/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Unlike existing methods constrained to image-only inputs or customized for a specific task, our framework flexibly integrates diverse geometric priors, including camera poses, intrinsics, and depth maps, while ...
- Traditional SfM (Schonberger & Frahm, 2016) and MVS rely on costly iterative optimization.

## Core Idea
- We present WorldMirror, a unified feed-forward model for comprehensive 3D geometric prediction tasks.
- Model Training Our model is trained end-to-end by minimizing a composite loss function L that integrates supervision for all prediction

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- WorldMirror achieves state-of-the-art performance across diverse benchmarks from camera, point map, depth, and surface normal estimation 1.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- WorldMirror achieves state-of-the-art performance across diverse benchmarks from camera, point map, depth, and surface normal estimation 1.
- We present WorldMirror, a unified feed-forward model for comprehensive 3D geometric prediction tasks.
- Unlike existing methods constrained to image-only inputs or customized for a specific task, our framework flexibly integrates diverse geometric priors, including camera poses, intrinsics, and depth maps, while ...

## Abstract Cue
- to novel view synthesis, while maintaining the efficiency of feed-forward inference.
