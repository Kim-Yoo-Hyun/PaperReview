# Method

- Year/Venue: 2021 / NeurIPS
- Category: Foundations: SLAM and Sensor Geometry
- Tags: SLAM, RGB-D, geometry
- Paper link: ./2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/paper.pdf
- Code/Project: https://github.com/princeton-vl/DROID-SLAM
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We introduce DROID-SLAM, a new deep learning based SLAM system.
- DROIDSLAM consists of recurrent iterative updates of camera pose and pixelwise depth through a Dense Bundle Adjustment layer.

## 원리적 동기
- The SLAM problem has been approached from a number of different angles.
- A key element for accuracy has been full Bundle Adjustment (BA), which jointly optimizes the camera poses and the 3D map in a single optimization problem.
- We introduce DROID-SLAM, a new deep learning based SLAM system.

## 핵심 방법론
- AUC (train) AUC (test) BundleFusion ElasticFusion RFusion DVO-SLAM ORB-SLAM2 BAD-SLAM 84.10 89.06 17.37 193.89 156.10 280.05 33.84 34.02 51.94 71.83 104.28 153.47 Ours 340.42 207.79 # successful datasets ...
- It successfully tracks all 9 sequences while achieving 83% lower ATE than DeepFactors and which succeeds on all videos and 90% lower ATE than DeepV2D .
- 30 25 20 15 10 5 0 ETH-3D SLAM Benchmark Ours BAD SLAM ORB-SLAM2 DVO-SLAM BundleFusion 0 1 2 3
