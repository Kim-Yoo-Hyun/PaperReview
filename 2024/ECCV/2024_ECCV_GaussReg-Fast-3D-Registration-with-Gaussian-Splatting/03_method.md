# Method

- Year/Venue: 2024 / ECCV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_GaussReg-Fast-3D-Registration-with-Gaussian-Splatting/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Training Strategy and Loss Function Due to the scale uncertainty in monocular video reconstruction, we performed data augmentation not only on rotation and translation but also on scaling ...
- In this section, we present our proposed GaussReg for 3D Registration with Gaussian Splatting (GS).
- To this end, we propose GaussReg, a novel coarse-to-fine framework, both fast and accurate.

## 원리적 동기
- But this method faces two issues: a) it is difficult to turn NeRF of unbounded scene to bounded voxel; b) the resolution limitation of the voxel grid makes ...
- To overcome these problems, deep feature extractors are proposed to find more robust correspondences between two point clouds.
- Training Strategy and Loss Function Due to the scale uncertainty in monocular video reconstruction, we performed data augmentation not only on rotation and translation but also on scaling ...

## 핵심 방법론
- Training Strategy and Loss Function Due to the scale uncertainty in monocular video reconstruction, we performed data augmentation not only on rotation and translation but also on scaling ...
- In this section, we present our proposed GaussReg for 3D Registration with Gaussian Splatting (GS).
- We apply two loss functions (overlap-aware circle loss and point matching loss) from the GeoTransformer to constrain our coarse registration network.
- For every point in P ointsA or P ointsB , we use (x, y, z, α, r, g, b) as the input channel to feed into the coarse ...
- We denote the camera poses of training images as B B B M {CiA = (RiA , TiA )}N i=0 and {Cj = (Rj , Tj )}j=0 for ...
