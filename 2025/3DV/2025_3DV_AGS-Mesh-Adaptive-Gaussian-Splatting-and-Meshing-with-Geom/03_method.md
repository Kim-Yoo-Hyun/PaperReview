# Method

- Year/Venue: 2025 / 3DV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_AGS-Mesh-Adaptive-Gaussian-Splatting-and-Meshing-with-Geom/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, we propose an approach for joint surface depth and normal refinement of Gaussian Splatting methods for accurate 3D reconstruction of indoor scenes.
- Moreover, we present a promising alternative to traditional meshing techniques using a depth adaptive TSDF and IsoOctree meshing method that can extract finer details from a Gaussian scene.
- Conclusion In this work, we presented two regularization strategies to adaptively integrate unreliable geometric priors into Gaussian Splatting based frameworks allowing for better mesh extraction and novel-view synthesis ...

## 원리적 동기
- Traditional approaches have addressed the problem by creating textured meshes that can be rendered using conventional graphics pipelines.
- Depth sensors, such as high-precision 3D LiDAR scanners or Kinect sensors, are often used to aid geometric reconstruction; however, these devices are generally expensive for consumer users and ...
- In this work, we propose an approach for joint surface depth and normal refinement of Gaussian Splatting methods for accurate 3D reconstruction of indoor scenes.

## 핵심 방법론
- Moreover, we present a promising alternative to traditional meshing techniques using a depth adaptive TSDF and IsoOctree meshing method that can extract finer details from a Gaussian scene.
- Conclusion In this work, we presented two regularization strategies to adaptively integrate unreliable geometric priors into Gaussian Splatting based frameworks allowing for better mesh extraction and novel-view synthesis ...
- We compare our approach with the ZoeDepth monocular network estimates, utilizing the recently proposed Patch-based Depth Correlation Loss for monocular depth supervision.
- Geometric priors significantly aid in surface optimization for the Gaussian models.
