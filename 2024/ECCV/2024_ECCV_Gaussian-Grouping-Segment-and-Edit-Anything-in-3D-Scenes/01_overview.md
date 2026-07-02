# Gaussian Grouping: Segment and Edit Anything in 3D Scenes

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_Gaussian-Grouping-Segment-and-Edit-Anything-in-3D-Scenes/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing methods rely on manually-labeled datasets, which are both costly and limited in scope, or require accurately scanned point clouds as input.
- Open-world 3D scene understanding is an essential challenge, with far-reaching implications for robotics, AR / VR, and autonomous driving.
- By taking multi-view captures, existing NeRF-based methods lift 2D masks or distill CLIP / DINO features via neural fields rendering.

## Core Idea
- To address this issue, we propose Gaussian Grouping, which extends Gaussian Splatting to jointly reconstruct and segment anything in open-world 3D scenes.
- We augment each Gaussian with a compact Identity Encoding, allowing the Gaussians to be grouped according to their object instance or stuff membership in the 3D scene.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The recent Gaussian Splatting achieves high-quality and realtime novel-view synthesis of the 3D scenes.
- We also provide 3D panoptic segmentation results on Replica and ScanNet dataset.
- Based on Gaussian Grouping, we further propose a local Gaussian Editing scheme, which shows efficacy in versatile scene editing applications, including 3D object removal, inpainting, colorization, style transfer ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To address this issue, we propose Gaussian Grouping, which extends Gaussian Splatting to jointly reconstruct and segment anything in open-world 3D scenes.
- The recent Gaussian Splatting achieves high-quality and realtime novel-view synthesis of the 3D scenes.
- Based on Gaussian Grouping, we further propose a local Gaussian Editing scheme, which shows efficacy in versatile scene editing applications, including 3D object removal, inpainting, colorization, style transfer ...

## Abstract Cue
- The recent Gaussian Splatting achieves high-quality and realtime novel-view synthesis of the 3D scenes.
