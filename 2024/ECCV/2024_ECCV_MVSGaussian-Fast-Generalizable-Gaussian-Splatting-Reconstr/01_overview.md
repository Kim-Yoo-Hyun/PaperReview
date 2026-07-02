# MVSGaussian: Fast Generalizable Gaussian Splatting Reconstruction from Multi-View Stereo

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_MVSGaussian-Fast-Generalizable-Gaussian-Splatting-Reconstr/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Compared with the vanilla 3D-GS, MVSGaussian achieves better view synthesis with less training computational cost.

## Core Idea
- 2) To further enhance performance, we propose a hybrid Gaussian rendering that integrates an efficient volume rendering design for novel view synthesis.
- We present MVSGaussian, a new generalizable 3D Gaussian representation approach derived from Multi-View Stereo (MVS) that can efficiently reconstruct unseen scenes.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Compared with previous generalizable NeRF-based methods, which typically require minutes of fine-tuning and seconds of rendering per image, MVSGaussian achieves real-time rendering with better synthesis quality for each ...
- Compared with the vanilla 3D-GS, MVSGaussian achieves better view synthesis with less training computational cost.
- We compare our method with state-of-the-art generalizable NeRF methods , as well as the recent generalizable Gaussian method .

## Limitation
- As our method relies on MVS for depth estimation, it inherits limitations from MVS, such as decreased depth accuracy in areas with weak textures or specular reflections, resulting ...

## Contribution
- Compared with the vanilla 3D-GS, MVSGaussian achieves better view synthesis with less training computational cost.
- 2) To further enhance performance, we propose a hybrid Gaussian rendering that integrates an efficient volume rendering design for novel view synthesis.
- We present MVSGaussian, a new generalizable 3D Gaussian representation approach derived from Multi-View Stereo (MVS) that can efficiently reconstruct unseen scenes.

## Abstract Cue
- We present MVSGaussian, a new generalizable 3D Gaussian representation approach derived from Multi-View Stereo (MVS) that can efficiently reconstruct unseen scenes.
