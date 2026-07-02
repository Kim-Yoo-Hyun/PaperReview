# Weakly Supervised Cross-Modal Learning for 4D Radar Scene Flow Estimation

- Year/Venue: 2026 / ICML
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_Weakly-Supervised-Cross-Modal-Learning-for-4D-Radar-Scene/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To overcome the limitation of expensive 3D scene flow annotations, runtime optimization and self-supervised methods have witnessed remarkable progress in recent years.
- To address this problem, we introduce an instance-level flow smoothness loss Lis .
- To overcome these limitations, we propose a task-specific iterative framework for weakly supervised radar scene flow learning, using only images and odometry for auxiliary supervision during training.

## Core Idea
- To overcome these limitations, we propose a task-specific iterative framework for weakly supervised radar scene flow learning, using only images and odometry for auxiliary supervision during training.
- For a fair comparison with the baselines, we use their official loss configuration and hyperparameter settings for network retraining on the VoD radar scene flow dataset.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on the real-world View-of-Delft (VoD) dataset demonstrate that our method not only surpasses state-of-the-art cross-modal supervised approaches that rely on 3D multi-object tracking on dense LiDAR ...
- To enable training on large-scale • We design two novel instance-aware losses by leveraging semantic guidance from images, effectively mitigating the mismatch and ambiguity issues commonly encountered in ...
- Unlike the mainstream trend, we strive to achieve effective radar scene flow estimation through lightweight task-specific network and concise loss design.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments on the real-world View-of-Delft (VoD) dataset demonstrate that our method not only surpasses state-of-the-art cross-modal supervised approaches that rely on 3D multi-object tracking on dense LiDAR ...
- To enable training on large-scale • We design two novel instance-aware losses by leveraging semantic guidance from images, effectively mitigating the mismatch and ambiguity issues commonly encountered in ...
- To overcome these limitations, we propose a task-specific iterative framework for weakly supervised radar scene flow learning, using only images and odometry for auxiliary supervision during training.

## Abstract Cue
- Ψ(ꞏ) (a) SSF: Due to the difficulty of obtaining ground-truth data for 4D radar scene flow estimation, previous methods typically rely on either self-supervised losses or cross-modal supervision using 3D LiDAR data, 2D images, and odometry.
