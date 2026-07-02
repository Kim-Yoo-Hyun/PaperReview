# Method

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, sensor fusion, LiDAR, point cloud, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_GeGS-PCR-Fast-and-Robust-Color-3D-Point-Cloud-Registration/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Finally, based on the GeoTransformer, we use self-attention and cross-attention to focus on the color information in the point cloud structure and guide superpoint registration.
- To overcome these limitations, we propose GeGS-PCR, a novel two-stage method that combines geometric, color, and Gaussian information for robust registration.
- Therefore, we introduce LORA optimization within the overall Transformer structure to reduce unnecessary computational overhead.

## 원리적 동기
- To address the challenges of point cloud registration in low-overlap real-world scenarios, we propose GeGS-PCR, a two-stage method that integrates Geometric-3DGS for colored point cloud registration.
- Previous works have focused on keypoints and correspondences, leveraging specialized neural networks to extract features from point clouds, and subsequently determining the rigid transformation using robust estimators like ...
- Finally, based on the GeoTransformer, we use self-attention and cross-attention to focus on the color information in the point cloud structure and guide superpoint registration.

## 핵심 방법론
- Finally, based on the GeoTransformer, we use self-attention and cross-attention to focus on the color information in the point cloud structure and guide superpoint registration.
- Therefore, we introduce LORA optimization within the overall Transformer structure to reduce unnecessary computational overhead.
- We propose a Dual-Modal Color Encoder (DMCE), which is responsible for transforming local neighborhood patches in the point cloud into more robust and rich representations, thus capturing both ...
- 3.1.2 Geometric-3DGS Module The Geometric-3DGS module mainly consists of three components: the 3DGS encoder, attention with 3DGS embeddings, and Gaussian superpoint registration, as shown in Fig.
- 3.2 Fine Registration With Photometric Optimization To improve point cloud registration accuracy, we propose a fine registration method based on photometric optimization.
