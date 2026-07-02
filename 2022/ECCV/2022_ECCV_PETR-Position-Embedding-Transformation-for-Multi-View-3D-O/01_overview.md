# PETR: Position Embedding Transformation for Multi-View 3D Object Detection

- Year/Venue: 2022 / ECCV
- Category: Foundations: 3D Detection and BEV Perception
- Tags: 3D Vision
- Paper link: ./2022/ECCV/2022_ECCV_PETR-Position-Embedding-Transformation-for-Multi-View-3D-O/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Previous works mainly solved this problem from the perspective of monocular object detection.
- However, such 2D-to-3D transformation in DETR3D may introduce several problems.
- Second, only the image feature at the projected point will be collected, which fails to perform the representation learning from global view.

## Core Idea
- In this paper, we develop position embedding transformation (PETR) for multi-view 3D object detection.
- 2 shows the overall architecture of the proposed PETR.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- PETR achieves state-of-the-art performance (50.4% NDS and 44.1% mAP) on standard nuScenes dataset and ranks 1st place on the benchmark.
- All experiments are trained for 24 epochs (2x schedule) on 8 Tesla V100 GPUs with a batch size of 8.
- 4.1 Datasets and Metrics We validate our method on nuScenes benchmark .

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- PETR achieves state-of-the-art performance (50.4% NDS and 44.1% mAP) on standard nuScenes dataset and ranks 1st place on the benchmark.
- In this paper, we develop position embedding transformation (PETR) for multi-view 3D object detection.

## Abstract Cue
- In this paper, we develop position embedding transformation (PETR) for multi-view 3D object detection.
