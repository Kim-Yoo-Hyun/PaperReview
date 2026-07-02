# LangOcc: Open Vocabulary Occupancy Estimation via Volume Rendering

- Year/Venue: 2025 / 3DV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_LangOcc-Open-Vocabulary-Occupancy-Estimation-via-Volume-Re/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, most existing camera-based methods rely on costly 3D voxel labels or LiDAR scans for training, limiting their practicality and scalability.
- However, most existing 3D occupancy estimation methods rely on expensive 3D ground-truth labels .
- The 3D occupancy estimation task has become an important challenge in the area of vision-based autonomous driving recently.

## Core Idea
- In this work we present a novel approach for open vocabulary occupancy estimation called LangOcc, that is trained only via camera images, and can detect arbitrary semantics via ...
- Method OccFlowNet CTF-Occ LangOcc (Full) LangOcc (Reduced) Mode L 3D C C mIoU 26.14 28.53 10.71 11.84 pensive manual labelling and additional sensor data, while our method is ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We also achieve a mIoU score of 11.84 on the Occ3D-nuScenes dataset, surpassing previous vision-only semantic occupancy estimation methods (+1.71%), despite not being limited to a specific set ...
- LangOcc outperforms LiDAR-supervised competitors in open vocabulary occupancy with a mAP of 22.7 by a large margin (+4.3%), solely relying on vision-based training.
- Moreover, existing benchmarks usually only reflect a limited predefined set of classes.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- LangOcc outperforms LiDAR-supervised competitors in open vocabulary occupancy with a mAP of 22.7 by a large margin (+4.3%), solely relying on vision-based training.
- However, most existing camera-based methods rely on costly 3D voxel labels or LiDAR scans for training, limiting their practicality and scalability.
- In this work we present a novel approach for open vocabulary occupancy estimation called LangOcc, that is trained only via camera images, and can detect arbitrary semantics via ...

## Abstract Cue
- The 3D occupancy estimation task has become an important challenge in the area of vision-based autonomous driving recently.
