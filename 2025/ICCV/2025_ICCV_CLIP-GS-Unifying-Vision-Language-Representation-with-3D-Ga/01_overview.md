# CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting

- Year/Venue: 2025 / ICCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Vision-Language Model, 3D Vision, Gaussian Splatting
- Paper link: ./2025/ICCV/2025_ICCV_CLIP-GS-Unifying-Vision-Language-Representation-with-3D-Ga/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This limitation constrains the potential of point cloud-based 3D multimodal representation learning.
- Existing works in 3D representation learning have made remarkable progress, particularly through the development of transformer-based approaches , as well as mamba-based approaches .
- Compared to the emerging 3D representation technique, 3D Gaussian Splatting (3DGS), the spatially sparse point cloud cannot depict the texture information of 3D objects, resulting in inferior reconstruction ...

## Core Idea
- We introduce the GS Tokenizer to generate serialized gaussian tokens, which are then processed through transformer layers pre-initialized with weights from point cloud models, resulting in the 3DGS ...
- In this paper, we present CLIPGS, a novel multimodal representation learning framework grounded in 3DGS.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Leveraging the well-aligned multimodal representations, CLIP-GS demonstrates versatility and outperforms point cloud-based models on various 3D tasks, including multimodal retrieval, zero-shot, and few-shot classification.
- How- ever, the emphasis predominantly remains on point cloud, which, as a sparse spatial representation, offers limited 3D reconstruction capabilities compared to the emerging 3D modeling method 3D ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We introduce the GS Tokenizer to generate serialized gaussian tokens, which are then processed through transformer layers pre-initialized with weights from point cloud models, resulting in the 3DGS ...
- How- ever, the emphasis predominantly remains on point cloud, which, as a sparse spatial representation, offers limited 3D reconstruction capabilities compared to the emerging 3D modeling method 3D ...
- Leveraging the well-aligned multimodal representations, CLIP-GS demonstrates versatility and outperforms point cloud-based models on various 3D tasks, including multimodal retrieval, zero-shot, and few-shot classification.

## Abstract Cue
- cilitating CLIP-GS in learning unified multimodal representations.
