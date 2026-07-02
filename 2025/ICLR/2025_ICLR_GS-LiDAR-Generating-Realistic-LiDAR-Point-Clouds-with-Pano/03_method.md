# Method

- Year/Venue: 2025 / ICLR Poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, sensor fusion, LiDAR, point cloud, 3D Vision
- Paper link: ./2025/ICLR/2025_ICLR_GS-LiDAR-Generating-Realistic-LiDAR-Point-Clouds-with-Pano/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- After training the Gaussians, we continue optimizing the U-Net by supervising the refined ray-drop mask using the same loss function as in Equation 17.
- Additionally, since the LiDAR ray-drop is also related to the characteristics of the LiDAR itself, we introduce a learnable prior Pprior for the raydrop.
- Through alpha-blending, we get a ray-drop probability map from PK Qk−1 Gaussians: Pgs = k=1 ρk ok Gk j=1 (1 − oj Gj ).

## 원리적 동기
- After training the Gaussians, we continue optimizing the U-Net by supervising the refined ray-drop mask using the same loss function as in Equation 17.

## 핵심 방법론
- After training the Gaussians, we continue optimizing the U-Net by supervising the refined ray-drop mask using the same loss function as in Equation 17.
- Additionally, since the LiDAR ray-drop is also related to the characteristics of the LiDAR itself, we introduce a learnable prior Pprior for the raydrop.
- Through alpha-blending, we get a ray-drop probability map from PK Qk−1 Gaussians: Pgs = k=1 ρk ok Gk j=1 (1 − oj Gj ).
- Depth distortion The depth distortion loss aims to reduce the distance between ray-splat intersections, encouraging the 2D Gaussian primitives to concentrate on the surface: X Ldist = ωi ...
