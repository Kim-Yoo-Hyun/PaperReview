# Problem

- Year/Venue: 2021 / NeurIPS
- Category: Foundations: SLAM and Sensor Geometry
- Tags: SLAM, RGB-D, geometry
- Paper link: ./2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/paper.pdf
- Code/Project: https://github.com/princeton-vl/DROID-SLAM
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- The SLAM problem has been approached from a number of different angles.
- A key element for accuracy has been full Bundle Adjustment (BA), which jointly optimizes the camera poses and the 3D map in a single optimization problem.
- Previous work has investigated replacing hand-crafted with learned features, using neural 3D representations, and combining learned energy terms with classical optimization backends.

## 해결하려는 문제
- Despite training on monocular video, it can leverage stereo or RGB-D video to achieve improved performance at test time.
- We introduce DROID-SLAM, a new deep learning based SLAM system.
- DROID-SLAM is accurate, achieving large improvements over prior work, and robust, suffering from substantially fewer catastrophic failures.

## 선행 연구 / 배경 단서
- On TartanAir, EuRoC, and TUM-RGBD, we have zero failures. • Strong Generalization: Our system, trained only with monocular input, can directly use stereo or RGB-D input to get ...
- The SLAM problem has been approached from a number of different angles.
- A key element for accuracy has been full Bundle Adjustment (BA), which jointly optimizes the camera poses and the 3D map in a single optimization problem.
