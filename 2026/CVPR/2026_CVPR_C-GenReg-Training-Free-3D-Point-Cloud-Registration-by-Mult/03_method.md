# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, sensor fusion, LiDAR, Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_C-GenReg-Training-Free-3D-Point-Cloud-Registration-by-Mult/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- For the VFM branch, we use K =4 input views from the L=50 views, and the probability temperature parameter is τm = 0.1.
- Standard point cloud registration consists of feature extraction, feature matching, and robust pose estimation (e.g.
- C-GenReg: A training-free point cloud registration framework.

## 원리적 동기
- Generated RGB Branch World Foundation Model Geometric Branch Geometric Feature Extractor (𝑹∗ , 𝒕∗ ) Geometric Feature Matching Figure 1.
- C-GenReg: A training-free point cloud registration framework.
- For the VFM branch, we use K =4 input views from the L=50 views, and the probability temperature parameter is τm = 0.1.

## 핵심 방법론
- For the VFM branch, we use K =4 input views from the L=50 views, and the probability temperature parameter is τm = 0.1.
- All learning-based methods are trained on the official 3DMatch training split.
- The geometric feature extractor is based on GeoTransformer , while the probabilistic fusion module follows the Noisy-AND formulation.
- It reduces the mean RTE by nearly half compared to GeoTransformer and consistently 4.
