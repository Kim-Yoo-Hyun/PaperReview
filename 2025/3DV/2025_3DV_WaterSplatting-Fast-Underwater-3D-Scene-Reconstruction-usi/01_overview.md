# WaterSplatting: Fast Underwater 3D Scene Reconstruction using Gaussian Splatting

- Year/Venue: 2025 / 3DV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_WaterSplatting-Fast-Underwater-3D-Scene-Reconstruction-usi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Furthermore, it does so while offering real-time rendering performance, addressing the efficiency limitations of existing methods.
- The underwater 3D scene reconstruction is a challenging, yet interesting problem with applications ranging from naval robots to VR experiences.
- The problem was successfully tackled by fully volumetric NeRF-based methods which can model both the geometry and the medium (water).

## Core Idea
- Therefore, we propose a novel approach that fuses volumetric rendering with 3DGS to handle underwater data effectively.
- The same advantages are observed in simulated scenes, where our method renders better details (indicated by the red square) than the SeaThru-NeRF in both easy and hard foggy ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our method outperforms state-of-theart NeRF-based methods in rendering quality on the un- derwater SeaThru-NeRF dataset.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our method outperforms state-of-theart NeRF-based methods in rendering quality on the un- derwater SeaThru-NeRF dataset.
- Therefore, we propose a novel approach that fuses volumetric rendering with 3DGS to handle underwater data effectively.
- Our method employs 3DGS for explicit geometry representation and a separate volumetric field (queried once per pixel) for capturing the scattering medium.

## Abstract Cue
- The underwater 3D scene reconstruction is a challenging, yet interesting problem with applications ranging from naval robots to VR experiences.
