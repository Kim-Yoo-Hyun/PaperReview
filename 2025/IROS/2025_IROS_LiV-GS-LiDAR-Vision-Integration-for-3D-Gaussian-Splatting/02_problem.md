# Problem

- Year/Venue: 2025 / IROS
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Paper link: ./2025/IROS/2025_IROS_LiV-GS-LiDAR-Vision-Integration-for-3D-Gaussian-Splatting/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Notably, LiV-GS is the first method that directly aligns discrete and sparse LiDAR data with continuous differentiable Gaussian maps in large-scale outdoor scenes, overcoming the limitation of fixed ...
- Traditional map representations such as point clouds, voxels, and surfels suffer from bounded-resolution in mapping , while implicit neural fields demand expensive computational resources.

## 해결하려는 문제
- — We present LiV-GS, a LiDAR-visual SLAM system in outdoor environments that leverages 3D Gaussian as a differentiable spatial representation.
- To reliably and stably update Gaussians outside the LiDAR field of view, we introduce a novel conditional Gaussian constraint that aligns these Gaussians closely with the nearest reliable ...
- The system aligns point clouds with Gaussian maps using shared covariance attributes for front-end tracking and integrates the normal orientation into the loss function to refines the Gaussian ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
