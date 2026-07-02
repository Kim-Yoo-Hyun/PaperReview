# Towards Learning to Complete Anything in Lidar

- Year/Venue: 2025 / ICML poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_Towards-Learning-to-Complete-Anything-in-Lidar/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, contemporary methods can only complete and recognize objects from a closed vocabulary labeled in existing Lidar datasets.
- Towards Learning to Complete Anything in Lidar 20 classes labeled in existing Lidar datasets.
- However, prior work can only localize and complete around † Work done during a research internship at NVIDIA.

## Core Idea
- We propose the first method for Zero-Shot Lidar Panoptic Scene Completion.
- We propose CAL (Complete Anything in Lidar) for Lidar-based shape-completion in-the-wild.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- This is far below the label diversity and scale compared to state-of-the-art image-based datasets (Kirillov et al., 2023).
- We show that our model can be prompted on standard benchmarks for Semantic and Panoptic Scene Completion, localize objects as (amodal) 3D bounding boxes, and recognize objects beyond ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose CAL (Complete Anything in Lidar) for Lidar-based shape-completion in-the-wild.
- We propose the first method for Zero-Shot Lidar Panoptic Scene Completion.
- Our approach is enabled by our pseudo-labeling engine, which mines 3D shape priors from unlabeled Lidar sequences using 2D vision foundation models.

## Abstract Cue
- object shapes from multiple such partial observations across the dataset.
