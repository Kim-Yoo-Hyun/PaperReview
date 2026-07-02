# OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, semantic
- Paper link: ./2024/ECCV/2024_ECCV_OpenIns3D-Snap-and-Lookup-for-3D-Open-vocabulary-Instance/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, unlike 2D data that can be easily collected from the internet, constructing a large-scale 3D-text dataset poses a challenge.
- This limitation impacts its performance in dynamic and everchanging contexts.
- Lastly, the 3D mask proposals are refined by removing masks lacking class assignments after both global and local Lookup.

## Core Idea
- In this work, we introduce OpenIns3D, a new 3D-input-only framework for 3D open-vocabulary scene understanding.
- Following OpenMask3D, we used Mask3D to generate mask proposals for OpenScene for evaluation.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- This approach yet simple, achieves state-of-the-art performance across a wide range of 3D open-vocabulary tasks, including recognition, object detection, and instance segmentation, on both indoor and outdoor datasets.
- When integrated with powerful 2D open-world models, it achieves excellent results in scene understanding tasks.
- Replica and ScanNet200 are evaluated by following the settings of OpenMask3D .

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- This approach yet simple, achieves state-of-the-art performance across a wide range of 3D open-vocabulary tasks, including recognition, object detection, and instance segmentation, on both indoor and outdoor datasets.
- When integrated with powerful 2D open-world models, it achieves excellent results in scene understanding tasks.
- In this work, we introduce OpenIns3D, a new 3D-input-only framework for 3D open-vocabulary scene understanding.

## Abstract Cue
- In this work, we introduce OpenIns3D, a new 3D-input-only framework for 3D open-vocabulary scene understanding.
