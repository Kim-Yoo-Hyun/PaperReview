# Problem

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, semantic
- Paper link: ./2024/ECCV/2024_ECCV_SGS-SLAM-Semantic-Gaussian-Splatting-For-Neural-Dense-SLAM/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Dense Visual Simultaneous Localization and Mapping (SLAM) is a crucial problem in the field of computer vision.
- However, NeRF-based SLAM methods employ multi-layer perceptrons (MLPs) as the implicit neural representation of scenes, which introduces several challenging limitations.
- Traditional visual SLAM systems stand out in sparse mapping using point clouds and voxels, but fall short in dense reconstruction.

## 해결하려는 문제
- We present SGS-SLAM, the first semantic visual SLAM system based on Gaussian Splatting.
- Extensive experiments demonstrate that SGS-SLAM delivers state-of-the-art performance in camera pose estimation, map reconstruction, precise semantic segmentation, and object-level geometric accuracy, while ensuring real-time rendering capabilities.
- We introduce a unique semantic feature loss that effectively compensates for the shortcomings of traditional depth and color losses in object optimization.

## 선행 연구 / 배경 단서
- Dense Visual Simultaneous Localization and Mapping (SLAM) is a crucial problem in the field of computer vision.
- However, NeRF-based SLAM methods employ multi-layer perceptrons (MLPs) as the implicit neural representation of scenes, which introduces several challenging limitations.
- Traditional visual SLAM systems stand out in sparse mapping using point clouds and voxels, but fall short in dense reconstruction.
