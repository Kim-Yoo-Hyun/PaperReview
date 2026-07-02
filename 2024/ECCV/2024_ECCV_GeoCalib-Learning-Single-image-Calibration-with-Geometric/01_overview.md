# GeoCalib: Learning Single-image Calibration with Geometric Optimization

- Year/Venue: 2024 / ECCV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_GeoCalib-Learning-Single-image-Calibration-with-Geometric/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This problem has been extensively studied, and many tools based on 3D geometry are available .
- Current approaches to this problem are based on either classical geometry with lines and vanishing points or on deep neural networks trained end-to-end.
- Experiments on various benchmarks show that GeoCalib is more robust and more accurate than existing classical and learned approaches.

## Core Idea
- Datasets: We conduct this experiment on four popular datasets not seen during training. i) Stanford2D3D consists of images samples from 360° panoramas captured inside university buildings. ii) TartanAir ...
- In this work, we introduce GeoCalib, a deep neural network that leverages universal rules of 3D geometry through an optimization process.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments on various benchmarks show that GeoCalib is more robust and more accurate than existing classical and learned approaches.
- Experiments are performed on a diverse range of real-world images (indoor, outdoor, and natural environments), and we analyze the impacts of our design decisions.
- We show some qualitative examples in Fig.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments on various benchmarks show that GeoCalib is more robust and more accurate than existing classical and learned approaches.
- In this work, we introduce GeoCalib, a deep neural network that leverages universal rules of 3D geometry through an optimization process.
- Current approaches to this problem are based on either classical geometry with lines and vanishing points or on deep neural networks trained end-to-end.

## Abstract Cue
- From a single image, visual cues can help deduce intrinsic and extrinsic camera parameters like the focal length and the gravity direction.
