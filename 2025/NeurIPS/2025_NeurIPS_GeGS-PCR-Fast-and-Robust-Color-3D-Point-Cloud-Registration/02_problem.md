# Problem

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, sensor fusion, LiDAR, point cloud, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_GeGS-PCR-Fast-and-Robust-Color-3D-Point-Cloud-Registration/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To address the challenges of point cloud registration in low-overlap real-world scenarios, we propose GeGS-PCR, a two-stage method that integrates Geometric-3DGS for colored point cloud registration.
- Previous works have focused on keypoints and correspondences, leveraging specialized neural networks to extract features from point clouds, and subsequently determining the rigid transformation using robust estimators like ...
- Despite rapid progress, point cloud registration remains challenging in real-world scenarios with low overlap between point clouds , where registration often fails.

## 해결하려는 문제
- Our method achieves state-of-the-art performance with Registration Recall at 99.9%, Relative Rotation Error as low as 0.013, and Relative Translation Error as low as 0.024, improving precision by ...
- To overcome these limitations, we propose GeGS-PCR, a novel two-stage method that combines geometric, color, and Gaussian information for robust registration.
- Our approach incorporates a dedicated color encoder that enhances color features by extracting multi-level geometric and color data from the original point cloud.

## 선행 연구 / 배경 단서
- To address the challenges of point cloud registration in low-overlap real-world scenarios, we propose GeGS-PCR, a two-stage method that integrates Geometric-3DGS for colored point cloud registration.
- Previous works have focused on keypoints and correspondences, leveraging specialized neural networks to extract features from point clouds, and subsequently determining the rigid transformation using robust estimators like ...
- Despite rapid progress, point cloud registration remains challenging in real-world scenarios with low overlap between point clouds , where registration often fails.
