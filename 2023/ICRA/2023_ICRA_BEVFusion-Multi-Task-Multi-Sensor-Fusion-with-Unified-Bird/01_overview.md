# BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation

- Year/Venue: 2023 / ICRA
- Category: Sensor Fusion, LiDAR, and Autonomous Driving
- Tags: sensor fusion, LiDAR, 3D perception
- Paper link: ./2023/ICRA/2023_ICRA_BEVFusion-Multi-Task-Multi-Sensor-Fusion-with-Unified-Bird/paper.pdf
- Code/Project: https://github.com/mit-han-lab/bevfusion
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Such density differences will become even more drastic for sparser LiDARs (or radars).
- To achieve this, we diagnose and lift the key efficiency bottlenecks in the view transformation with optimized BEV pooling, reducing latency by more than 40×.
- It establishes the new state of the art on the nuScenes benchmark, achieving 1.3% higher mAP and NDS on 3D object detection and 13.6% higher mIoU on BEV ...

## Core Idea
- In this paper, we propose BEVFusion, an efficient and generic multi-task multi-sensor fusion framework.
- In this paper, we propose BEVFusion to unify multi-modal space for task-agnostic learning.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- I: BEVFusion achieves state-of-the-art 3D object detection performance on nuScenes (val and test) without bells and whistles.
- To achieve this, we diagnose and lift the key efficiency bottlenecks in the view transformation with optimized BEV pooling, reducing latency by more than 40×.
- Code to reproduce our results is available at https://github.com/mit-han-lab/bevfusion.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this paper, we propose BEVFusion, an efficient and generic multi-task multi-sensor fusion framework.
- In this paper, we propose BEVFusion to unify multi-modal space for task-agnostic learning.
- Although they have demonstrated remarkable performance on large-scale detection benchmarks, these point-level fusion methods barely work on semantic-oriented tasks, such as BEV map segmentation , , , .

## Abstract Cue
- — Multi-sensor fusion is essential for an accurate and reliable autonomous driving system.
