# DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras

- Year/Venue: 2021 / NeurIPS
- Category: Foundations: SLAM and Sensor Geometry
- Tags: SLAM, RGB-D, geometry
- Paper link: ./2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/paper.pdf
- Code/Project: https://github.com/princeton-vl/DROID-SLAM
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The SLAM problem has been approached from a number of different angles.
- A key element for accuracy has been full Bundle Adjustment (BA), which jointly optimizes the camera poses and the 3D map in a single optimization problem.
- Previous work has investigated replacing hand-crafted with learned features, using neural 3D representations, and combining learned energy terms with classical optimization backends.

## Core Idea
- We introduce DROID-SLAM, a new deep learning based SLAM system.
- DROIDSLAM consists of recurrent iterative updates of camera pose and pixelwise depth through a Dense Bundle Adjustment layer.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Despite training on monocular video, it can leverage stereo or RGB-D video to achieve improved performance at test time.
- Monocular ORB-SLAM DeepV2D TartanVO Ours MH000 1.30 6.15 4.88 0.08 MH001 0.04 2.12 0.26 0.05 MH002 2.37 4.54 2.00 0.04 MH003 2.45 3.89 0.94 0.02 MH004 X 2.71 ...
- DROID-SLAM is accurate, achieving large improvements over prior work, and robust, suffering from substantially fewer catastrophic failures.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Despite training on monocular video, it can leverage stereo or RGB-D video to achieve improved performance at test time.
- We introduce DROID-SLAM, a new deep learning based SLAM system.
- DROID-SLAM is accurate, achieving large improvements over prior work, and robust, suffering from substantially fewer catastrophic failures.

## Abstract Cue
- We introduce DROID-SLAM, a new deep learning based SLAM system.
