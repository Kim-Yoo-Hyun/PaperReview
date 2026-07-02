# Method

- Year/Venue: 2024 / CVPR
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: SLAM, Gaussian Splatting, geometry
- Paper link: ./2024/CVPR/2024_CVPR_GS-SLAM-Dense-Visual-SLAM-with-3D-Gaussian-Splatting/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Specifically, we propose an adaptive expansion strategy that adds new or deletes noisy 3D Gaussians in order to efficiently reconstruct new observed scene geometry and improve the mapping ...
- In this paper, we introduce GS-SLAM that first utilizes 3D Gaussian representation in the Simultaneous Localization and Mapping (SLAM) system.
- Compared to recent SLAM methods employing neural implicit representations, our method utilizes a real-time differentiable splatting rendering pipeline that offers significant speedup to map optimization and RGB-D rendering.

## 원리적 동기
- However, these methods face serious challenges in obtaining fine-grained dense maps.
- This strategy is essential to extend 3D Gaussian representation to reconstruct the whole scene rather than synthesize a static object in existing methods.
- Specifically, we propose an adaptive expansion strategy that adds new or deletes noisy 3D Gaussians in order to efficiently reconstruct new observed scene geometry and improve the mapping ...

## 핵심 방법론
- 1 illustrates the tracking performance of our method and the stateof-the-art methods on the Replica dataset.
- This excellent rendering performance is attributed to the efficient 3D Gaussian rendering pipeline and can be further applied to real-time downstream tasks, such as VR , robot navigation ...
