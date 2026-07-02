# Continuous 3D Perception Model with Persistent State

- Year/Venue: 2025 / CVPR
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, SLAM, representation
- Paper link: ./2025/CVPR/2025_CVPR_Continuous-3D-Perception-Model-with-Persistent-State/paper.pdf
- Code/Project: https://cut3r.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The tabula rasa nature of these approaches poses challenges in handling scenarios with sparse observations or ill-posed conditions.

## Core Idea
- We present a unified framework capable of solving a broad range of 3D tasks.
- We use a ViT-Large model for the image encoder Encoderi , initialized with DUSt3R encoder pretrained weights, and ViT-Base for the decoders.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We evaluate our method on various 3D/4D tasks and demonstrate competitive or state-of-the-art performance in each.
- In addition to reconstructing a scene from images, our method can also infer structure for unseen parts of the scene, given a virtual camera query (shown in blue). ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We evaluate our method on various 3D/4D tasks and demonstrate competitive or state-of-the-art performance in each.
- In addition to reconstructing a scene from images, our method can also infer structure for unseen parts of the scene, given a virtual camera query (shown in blue). ...
- We present a unified framework capable of solving a broad range of 3D tasks.

## Abstract Cue
- We present a unified framework capable of solving a broad range of 3D tasks.
