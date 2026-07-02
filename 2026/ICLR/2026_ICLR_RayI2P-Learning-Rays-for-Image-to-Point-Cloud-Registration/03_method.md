# Method

- Year/Venue: 2026 / ICLR Poster
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, point cloud, 3D Vision
- Paper link: ./2026/ICLR/2026_ICLR_RayI2P-Learning-Rays-for-Image-to-Point-Cloud-Registration/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Following standard protocol (Li & Lee, 2021), we use sequences 0–8 for training and sequences 9–10 for testing.
- For the 3D backbone, we use a 4-stage KPConv (Thomas et al., 2019) where the output channel dimension is also 512.
- We follow the official train/test split, using 850 scenes for training and 150 scenes for testing.

## 원리적 동기
- Following standard protocol (Li & Lee, 2021), we use sequences 0–8 for training and sequences 9–10 for testing.

## 핵심 방법론
- Following standard protocol (Li & Lee, 2021), we use sequences 0–8 for training and sequences 9–10 for testing.
- For the 3D backbone, we use a 4-stage KPConv (Thomas et al., 2019) where the output channel dimension is also 512.
- We follow the official train/test split, using 850 scenes for training and 150 scenes for testing.
- All input images are resized to a resolution of 160 × 512, and point clouds are uniformly downsampled to 40,960 points for both training and evaluation. nuScenes (Caesar ...
- All the attention layers have 512 features channels with 4 attention heads and ReLU activation.
