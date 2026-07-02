# AGS-Mesh: Adaptive Gaussian Splatting and Meshing with Geometric Priors for Indoor Room Reconstruction Using Smartphones

- Year/Venue: 2025 / 3DV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_AGS-Mesh-Adaptive-Gaussian-Splatting-and-Meshing-with-Geom/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Traditional approaches have addressed the problem by creating textured meshes that can be rendered using conventional graphics pipelines.
- Depth sensors, such as high-precision 3D LiDAR scanners or Kinect sensors, are often used to aid geometric reconstruction; however, these devices are generally expensive for consumer users and ...

## Core Idea
- In this work, we propose an approach for joint surface depth and normal refinement of Gaussian Splatting methods for accurate 3D reconstruction of indoor scenes.
- Moreover, we present a promising alternative to traditional meshing techniques using a depth adaptive TSDF and IsoOctree meshing method that can extract finer details from a Gaussian scene.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our filtering strategy and optimization design demonstrate significant improvements in both mesh estimation and novel-view synthesis for both 3D and 2D Gaussian Splatting-based methods on challeng- 1.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our filtering strategy and optimization design demonstrate significant improvements in both mesh estimation and novel-view synthesis for both 3D and 2D Gaussian Splatting-based methods on challeng- 1.
- In this work, we propose an approach for joint surface depth and normal refinement of Gaussian Splatting methods for accurate 3D reconstruction of indoor scenes.
- We develop a scale-aware meshing strategy inspired by TSDF and octree-based isosurface extraction, which recovers finer details from Gaussian models compared to other commonly used open-source meshing tools.

## Abstract Cue
- Furthermore, we explore the use of alternative meshing strategies for finer geometry extraction.
