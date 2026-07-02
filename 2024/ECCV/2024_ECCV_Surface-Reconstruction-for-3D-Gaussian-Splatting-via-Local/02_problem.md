# Problem

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_Surface-Reconstruction-for-3D-Gaussian-Splatting-via-Local/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Given multi-view images with corresponding camera poses, 3DGS initializes Gaussian primitives from a sparse point cloud that comes from COLMAP and renders a novel view with a dedicated ...
- This paper presents a novel approach for surface mesh reconstruction from 3D Gaussian Splatting (3DGS) , a technique renowned for its efficiency in novel view synthesis but challenged ...
- This paper introduces local structural hints during training to address the challenge.

## 해결하려는 문제
- Extensive experimental results demonstrate the effectiveness of our method in achieving superior mesh quality compared with the SoTA surface reconstruction for 3DGS.
- This paper introduces local structural hints during training to address the challenge.
- This paper presents a novel approach for surface mesh reconstruction from 3D Gaussian Splatting (3DGS) , a technique renowned for its efficiency in novel view synthesis but challenged ...

## 선행 연구 / 배경 단서
- Given multi-view images with corresponding camera poses, 3DGS initializes Gaussian primitives from a sparse point cloud that comes from COLMAP and renders a novel view with a dedicated ...
- 3D Gaussian Splatting (3DGS) has garnered significant attention in the realm of 3D computer vision for its exceptional efficiency in modeling 3D radiance fields.
- With the dynamic densification operation on Gaussians including splitting and cloning, the final scene will be represented by millions of tiny Gaussians with unparalleled rendering efficiency.
