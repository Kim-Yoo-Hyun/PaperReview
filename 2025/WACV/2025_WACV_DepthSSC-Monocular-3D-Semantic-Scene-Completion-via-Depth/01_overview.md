# DepthSSC: Monocular 3D Semantic Scene Completion via Depth-Spatial Alignment and Voxel Adaptation

- Year/Venue: 2025 / WACV
- Category: 3D Semantic Understanding and Alignment
- Tags: semantic, alignment, depth, 3D Vision
- Paper link: ./2025/WACV/2025_WACV_DepthSSC-Monocular-3D-Semantic-Scene-Completion-via-Depth/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Despite numerous existing methods, many face challenges such as inaccurately predicting object shapes and misclassifying object boundaries.
- As illustrated in the first row, VoxFormer fails to adequately utilize depth relationships to distinguish between different vehicles.

## Core Idea
- To address these issues, we propose DepthSSC, an advanced method for semantic scene completion using only monocular cameras.
- We present the results for various distance intervals (12.8 meters, 25.6 meters, and 51.2 meters) and furnish metrics for both geometric evaluation (IoU) and semantic assessment (mIoU).

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Evaluations on the SemanticKITTI and SSCBench-KITTI-360 dataset demonstrate that DepthSSC not only captures intricate 3D structural details effectively but also achieves state-of-theart performance.
- Demonstrates DepthSSC’s superiority in handling complex 3D environments for semantic scene completion.
- The highlighted areas showcase VoxFormer’s challenges with misrecognition and nonrecognition.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Evaluations on the SemanticKITTI and SSCBench-KITTI-360 dataset demonstrate that DepthSSC not only captures intricate 3D structural details effectively but also achieves state-of-theart performance.
- To address these issues, we propose DepthSSC, an advanced method for semantic scene completion using only monocular cameras.
- The highlighted areas showcase VoxFormer’s challenges with misrecognition and nonrecognition.

## Abstract Cue
- The task of 3D semantic scene completion using monocular cameras is gaining significant attention in the field of autonomous driving.
