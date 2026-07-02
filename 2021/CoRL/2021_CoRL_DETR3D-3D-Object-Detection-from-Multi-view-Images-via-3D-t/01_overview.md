# DETR3D: 3D Object Detection from Multi-view Images via 3D-to-2D Queries

- Year/Venue: 2021 / CoRL
- Category: Sensor Fusion, LiDAR, and Autonomous Driving
- Tags: 3D Vision, BEV, 3D detection, camera
- Paper link: ./2021/CoRL/2021_CoRL_DETR3D-3D-Object-Detection-from-Multi-view-Images-via-3D-t/paper.pdf
- Code/Project: https://github.com/WangYueFt/detr3d
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- 3D object detection from visual information is a long-standing challenge for low-cost autonomous driving systems.
- Our framework, termed DETR3D (Multi-View 3D Detection), addresses this problem in a top-down fashion.
- Different from existing works that combine object predictions from the different camera views in a final stage, our method fuses information from all the camera views in each ...

## Core Idea
- : We introduce a framework for multi-camera 3D object detection.
- Our method performs worse than FCOS3D in terms of mATE.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We achieve state-of-the-art performance on the nuScenes autonomous driving benchmark.
- We present our results as follows: first, we detail the dataset, metrics, and implementation in §4.1; then we compare our method to existing works in §4.2; we benchmark ...
- This top-down approach outperforms its bottom-up counterpart in which object bounding box prediction follows per-pixel depth estimation, since it does not suffer from the compounding error introduced by ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We achieve state-of-the-art performance on the nuScenes autonomous driving benchmark.
- In contrast to existing works, which estimate 3D bounding boxes directly from monocular images or use depth prediction networks to generate input for 3D object detection from 2D ...
- : We introduce a framework for multi-camera 3D object detection.

## Abstract Cue
- : We introduce a framework for multi-camera 3D object detection.
