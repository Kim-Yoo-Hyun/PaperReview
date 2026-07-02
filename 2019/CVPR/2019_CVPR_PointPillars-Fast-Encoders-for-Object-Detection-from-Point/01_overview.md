# PointPillars: Fast Encoders for Object Detection from Point Clouds

- Year/Venue: 2019 / CVPR
- Category: Foundations: 3D Detection and BEV Perception
- Tags: 3D Vision, LiDAR, 3D detection, BEV
- Paper link: ./2019/CVPR/2019_CVPR_PointPillars-Fast-Encoders-for-Object-Detection-from-Point/paper.pdf
- Code/Project: https://github.com/nutonomy/second.pytorch
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Introduction Deploying autonomous vehicles (AVs) in urban environments poses a difficult technological challenge.
- This overhead perspective offers several advantages such as lack of scale ambiguity and the near lack of occlusion.
- A lidar uses a laser scanner to measure the distance to the environment, thus generating a sparse point cloud representation.

## Core Idea
- Performance (AP) arXiv:1812.05784v2 [cs.LG] 7 May 2019 {alex, sourabh, holger, lubing, jiong.yang, oscar}@nutonomy.com Cyclist PP F A S V Runtime (Hz) Figure 1.
- Bird’s eye view performance vs speed for our proposed PointPillars, PP method on the KITTI test set.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Similar performance is achieved on the 3D metric (Table 2).
- To achieve this, autonomous vehicles rely on several sensors out of which the lidar is arguably the most important.
- PointPillars outperforms all other lidar-only methods in terms of both speed and accuracy by a large margin.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Similar performance is achieved on the 3D metric (Table 2).
- To achieve this, autonomous vehicles rely on several sensors out of which the lidar is arguably the most important.
- PointPillars outperforms all other lidar-only methods in terms of both speed and accuracy by a large margin.

## Abstract Cue
- Performance (AP) arXiv:1812.05784v2 [cs.LG] 7 May 2019 {alex, sourabh, holger, lubing, jiong.yang, oscar}@nutonomy.com Cyclist PP F A S V Runtime (Hz) Figure 1.
