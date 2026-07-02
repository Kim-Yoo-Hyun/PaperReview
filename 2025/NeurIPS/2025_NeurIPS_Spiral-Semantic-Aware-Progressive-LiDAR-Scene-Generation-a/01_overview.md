# Spiral: Semantic-Aware Progressive LiDAR Scene Generation and Understanding

- Year/Venue: 2025 / NeurIPS poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, semantic, alignment, Diffusion, Generation, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Spiral-Semantic-Aware-Progressive-LiDAR-Scene-Generation-a/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address this limitation while preserving the advantages of range-view representations, such as computational efficiency and simplified network design, we propose S PIRAL, a novel range-view LiDAR diffusion ...
- While recent voxel-based approaches can generate both geometric structures and semantic labels, existing range-view methods are limited to producing unlabeled LiDAR scenes.

## Core Idea
- To address this limitation while preserving the advantages of range-view representations, such as computational efficiency and simplified network design, we propose S PIRAL, a novel range-view LiDAR diffusion ...
- Furthermore, we introduce novel semantic-aware metrics to evaluate the quality of the generated labeled range-view data.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments on the SemanticKITTI and nuScenes datasets demonstrate that S PIRAL achieves state-of-the-art performance with the smallest parameter size, outperforming two-step methods that combine the generative and segmentation ...
- Despite having the smallest parameter size of only 61M, Spiral achieves the best performance across all semantic-aware metrics, outperforming the two-step method, R2DM & SPVCNN++ , by 31.03%, ...
- Compared with the second best method (R2DM & RangeNet++ ), Spiral achieves improvements of 49.03%, 67.84%, and 46.79% on S-FRD, S-FPD, and S-JSD, respectively.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments on the SemanticKITTI and nuScenes datasets demonstrate that S PIRAL achieves state-of-the-art performance with the smallest parameter size, outperforming two-step methods that combine the generative and segmentation ...
- To address this limitation while preserving the advantages of range-view representations, such as computational efficiency and simplified network design, we propose S PIRAL, a novel range-view LiDAR diffusion ...
- Furthermore, we introduce novel semantic-aware metrics to evaluate the quality of the generated labeled range-view data.

## Abstract Cue
- Leveraging recent diffusion models, LiDAR-based large-scale 3D scene generation has achieved great success.
