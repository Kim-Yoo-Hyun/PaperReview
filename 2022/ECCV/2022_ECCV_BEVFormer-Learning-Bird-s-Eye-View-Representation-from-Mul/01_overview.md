# BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers

- Year/Venue: 2022 / ECCV
- Category: Sensor Fusion, LiDAR, and Autonomous Driving
- Tags: sensor fusion, 3D perception, Planning
- Paper link: ./2022/ECCV/2022_ECCV_BEVFormer-Learning-Bird-s-Eye-View-Representation-from-Mul/paper.pdf
- Code/Project: https://github.com/fundamentalvision/BEVFormer
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The significant challenges are that autonomous driving is time-critical and objects in the scene change rapidly, and thus simply stacking BEV features of cross timestamps brings extra computational ...
- Apart from the low cost for deployment, cameras own the desirable advantages to detect long-range distance objects and identify vision-based road elements (e.g., traffic lights, stoplines), compared to ...

## Core Idea
- For temporal information, we propose temporal selfattention to recurrently fuse the history BEV information.
- Compared with training tasks individually, multi-task learning saves computational cost and reduces the inference time by sharing more modules,

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our approach achieves the new state-of-the-art 56.9% in terms of NDS metric on the nuScenes test set, which is 9.0 points higher than previous best arts and on ...
- We further show that BEVFormer remarkably improves the accuracy of velocity estimation and recall of objects under low visibility conditions.
- The code is available at https://github.com/zhiqi-li/BEVFormer. *: 4.1 Datasets We conduct experiments on two challenging public autonomous driving datasets, namely nuScenes dataset and Waymo open dataset .

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our approach achieves the new state-of-the-art 56.9% in terms of NDS metric on the nuScenes test set, which is 9.0 points higher than previous best arts and on ...
- For temporal information, we propose temporal selfattention to recurrently fuse the history BEV information.
- We further show that BEVFormer remarkably improves the accuracy of velocity estimation and recall of objects under low visibility conditions.

## Abstract Cue
- 3D visual perception tasks, including 3D detection and map segmentation based on multi-camera images, are essential for autonomous driving systems.
