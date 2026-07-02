# Distilling Diffusion Models to Efficient 3D LiDAR Scene Completion

- Year/Venue: 2025 / ICCV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, Diffusion, Generation, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Distilling-Diffusion-Models-to-Efficient-3D-LiDAR-Scene-Co/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Among different types of sensors, 3D LiDAR has become one of the most pletion results under sparse point cloud conditions to progressively approach the multi-step iterative reconstruction quality ...

## Core Idea
- Finally, we introduce a Structural Loss consisting of a scene-wise term and a point-wise term constraining the key landmark points and their relative configuration.
- Diffusion models have been applied to 3D LiDAR scene completion due to their strong training stability and high completion quality.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that ScoreLiDAR significantly accelerates the completion time from 30.55 to 5.37 seconds per frame (>5×) on SemanticKITTI and achieves superior performance compared to state-of-the-art 3D ...
- This paper proposes a novel distillation method tailored for 3D LiDAR scene completion models, dubbed ScoreLiDAR, which achieves efficient yet high-quality scene completion.
- To improve completion quality, we also introduce a novel Structural Loss, which encourages the distilled model to capture the geometric structure of the 3D LiDAR scene.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate that ScoreLiDAR significantly accelerates the completion time from 30.55 to 5.37 seconds per frame (>5×) on SemanticKITTI and achieves superior performance compared to state-of-the-art 3D ...
- Finally, we introduce a Structural Loss consisting of a scene-wise term and a point-wise term constraining the key landmark points and their relative configuration.
- Diffusion models have been applied to 3D LiDAR scene completion due to their strong training stability and high completion quality.

## Abstract Cue
- a scene-wise term constraining the holistic structure and a point-wise term constraining the key landmark points and their relative configuration.
