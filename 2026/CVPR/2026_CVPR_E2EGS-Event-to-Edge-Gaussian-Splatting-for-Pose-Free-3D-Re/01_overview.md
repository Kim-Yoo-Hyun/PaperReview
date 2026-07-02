# E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_E2EGS-Event-to-Edge-Gaussian-Splatting-for-Pose-Free-3D-Re/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, existing event-based NVS methods either assume known poses or rely on depth estimation models that are bounded by their initial observations, failing to generalize as the camera ...
- This assumption makes them vulnerable to common real-world challenges, such as motion blur and adverse lighting conditions that frequently occur during rapid camera movements or in low-light environments.
- The event camera’s movement induces consistent events along edges, while non-edge regions produce sparse noise.

## Core Idea
- We present E2EGS, a pose-free framework operating solely on event streams.
- Edge-guided 3D reconstruction To leverage detected edges during reconstruction, we introduce an edge-guided loss that spatially weights the reconstruction error based on edge confidence.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on both synthetic and real datasets demonstrate that E2EGS achieves superior reconstruction quality and trajectory accuracy, establishing a fully pose-free paradigm for event-based 3D reconstruction.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments on both synthetic and real datasets demonstrate that E2EGS achieves superior reconstruction quality and trajectory accuracy, establishing a fully pose-free paradigm for event-based 3D reconstruction.
- We present E2EGS, a pose-free framework operating solely on event streams.
- The emergence of neural radiance fields (NeRF) and 3D Gaussian splatting (3DGS) has advanced novel view synthesis (NVS).

## Abstract Cue
- These volumetric representation methods typically take camera poses and 2D views as input, leveraging multiview images to learn implicit or explicit 3D scene representations.
