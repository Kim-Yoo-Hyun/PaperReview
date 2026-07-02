# SG-PGM: Partial Graph Matching Network with Semantic Geometric Fusion for 3D Scene Graph Alignment and Its Downstream Tasks

- Year/Venue: 2024 / CVPR
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_SG-PGM-Partial-Graph-Matching-Network-with-Semantic-Geomet/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- In this work, we treat 3D scene graph alignment as a partial graph-matching problem and propose to solve it with a graph neural network.
- Experiments show that our method improves the alignment accuracy by 10∼20% in low-overlap and random transformation scenarios and outperforms the existing work in multiple downstream tasks.

## Core Idea
- With the Soft-topK module, our method can also effectively surpass the false-positive matching pairs and therefore yield the highest F1 score.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments show that our method improves the alignment accuracy by 10∼20% in low-overlap and random transformation scenarios and outperforms the existing work in multiple downstream tasks.
- Subsequent downstream tasks such as point cloud registration are achieved by running a pre-trained registration network within the matched regions.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments show that our method improves the alignment accuracy by 10∼20% in low-overlap and random transformation scenarios and outperforms the existing work in multiple downstream tasks.
- Subsequent downstream tasks such as point cloud registration are achieved by running a pre-trained registration network within the matched regions.
- In this work, we treat 3D scene graph alignment as a partial graph-matching problem and propose to solve it with a graph neural network.

## Abstract Cue
- Scene graphs have been recently introduced into 3D of the scene.
