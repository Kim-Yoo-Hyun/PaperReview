# EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_EmbodiedOcc-Embodied-3D-Occupancy-Prediction-for-Vision-ba/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Most existing methods focus on offline perception from one or a few views and cannot be applied to embodied agents that demand to gradually perceive the scene through ...
- Most existing methods still focus on local 3D occupancy prediction by integrati
- Due to the low costs of camera sensors, vision-based 3D occupancy prediction is gaining increasing popularity and produces a comprehensive understanding of both semantics and structures of the ...

## Core Idea
- Following existing works , we use a pre-trained EfficientNet-B7 to initialize the image encoder in our local module.
- We use mIoU and IoU as the evaluation metrics.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our EmbodiedOcc outperforms existing methods by a large margin and accomplishes the embodied occupancy prediction with high accuracy and efficiency.
- Intelligent agents first perceive their surrounding environments and then make decisions based on the perception results.
- We reorganize an EmbodiedOccScanNet benchmark based on local annotations to facilitate the evaluation of the embodied 3D occupancy prediction task.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- For each update, we extract semantic and structural features from the observed image and efficiently incorporate them via deformable crossattention to refine the regional Gaussians.
- Our EmbodiedOcc outperforms existing methods by a large margin and accomplishes the embodied occupancy prediction with high accuracy and efficiency.
- In this paper, we formulate an embodied 3D occupancy prediction task to target this practical scenario and propose a Gaussian-based EmbodiedOcc framework to accomplish it.

## Abstract Cue
- 3D occupancy prediction provides a comprehensive description of the surrounding scenes and has become an essential task for 3D perception.
