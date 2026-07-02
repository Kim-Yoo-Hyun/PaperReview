# Problem

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_CG-SLAM-Efficient-Dense-RGB-D-SLAM-in-a-Consistent-Uncerta/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Dense visual Localization and Mapping (Visual SLAM) is a long-standing problem in 3D computer vision over recent decades, which targets performing pose tracking and scene mapping simultaneously with ...
- Despite their notable successes in surface modeling and novel view synthesis, existing NeRF-based methods are hindered by their computationally intensive and time-consuming volume rendering pipeline.

## 해결하려는 문제
- Through an in-depth analysis of Gaussian Splatting, we propose several techniques to construct a consistent and stable 3D Gaussian field suitable for tracking and mapping.
- Experiments on various datasets demonstrate that CG-SLAM achieves superior tracking and mapping performance with a notable tracking speed of around 15 Hz.
- This paper presents an efficient dense RGB-D SLAM system, i.e., CG-SLAM, based on a novel uncertainty-aware 3D Gaussian field with high consistency and geometric stability.

## 선행 연구 / 배경 단서
- Dense visual Localization and Mapping (Visual SLAM) is a long-standing problem in 3D computer vision over recent decades, which targets performing pose tracking and scene mapping simultaneously with ...
- Traditional visual SLAM systems have shown accurate tracking performance across various scenes, while the underlying 3D representations (e.g., point cloud, mesh, and surfel) demonstrate limitations in facilitating highly ...
