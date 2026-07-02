# SIU3R: Simultaneous Scene Understanding and 3D Reconstruction Beyond Feature Alignment

- Year/Venue: 2025 / NeurIPS spotlight
- Category: 3D Semantic Understanding and Alignment
- Tags: 3D reconstruction, semantic, alignment, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_SIU3R-Simultaneous-Scene-Understanding-and-3D-Reconstructi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- 2) Information loss in feature compression: To efficiently embed 2D features into 3D representations and save the memory cost during feature rasterization, existing methods usually need to compress ...
- To address the challenges outlined above, we propose SIU3R, a novel generalizable framework achieving SI MULTANEOUS U NDERSTANDING and 3D R ECONSTRUCTION beyond feature alignment (Fig.1 b).
- This framework enables native 2 3D understanding without the need of alignment with 2D models, thereby avoiding limitations on 3D understanding imposed by 2D models and their feature ...

## Core Idea
- Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified Query Decoder for decoding pixel-aligned 2D ...
- In particular, to promote understanding from reconstruction, we propose Multi-View Mask Aggregation module, which utilizes 3D geometric clues in G to aggregate semantic information from all views to ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that our method achieves state-of-the-art performance not only on the individual tasks of 3D reconstruction and understanding, but also on the task of simultaneous understanding ...
- To achieve this, recent approaches resort to 2D-to-3D feature alignment paradigm, which leads to limited 3D understanding capability and potential semantic information loss.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate that our method achieves state-of-the-art performance not only on the individual tasks of 3D reconstruction and understanding, but also on the task of simultaneous understanding ...
- In light of this, we propose SIU3R, the first alignment-free framework for generalizable simultaneous understanding and 3D reconstruction from unposed images.
- To achieve this, recent approaches resort to 2D-to-3D feature alignment paradigm, which leads to limited 3D understanding capability and potential semantic information loss.

## Abstract Cue
- Simultaneous understanding and 3D reconstruction plays an important role in developing end-to-end embodied intelligent systems.
