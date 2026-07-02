# Surface Reconstruction for 3D Gaussian Splatting via Local Structural Hints

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_Surface-Reconstruction-for-3D-Gaussian-Splatting-via-Local/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Given multi-view images with corresponding camera poses, 3DGS initializes Gaussian primitives from a sparse point cloud that comes from COLMAP and renders a novel view with a dedicated ...
- This paper presents a novel approach for surface mesh reconstruction from 3D Gaussian Splatting (3DGS) , a technique renowned for its efficiency in novel view synthesis but challenged ...
- This paper introduces local structural hints during training to address the challenge.

## Core Idea
- This paper introduces local structural hints during training to address the challenge.
- We then propose to construct a signed distance field by a moving least square (MLS) function over the Gaussians in each local region.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experimental results demonstrate the effectiveness of our method in achieving superior mesh quality compared with the SoTA surface reconstruction for 3DGS.
- Following the setting , 4 scenes are selected from ScanNet for experiments and compared ours with both the GSrec 11 Table 1: The quantitative results of the scene ...
- 1 where our method outperforms both of SuGaR’s variants with a clear margin.

## Limitation
- We have presented a novel framework coined GSrec to address the challenge of misalignment between Gaussians and real-surface for surface reconstruction from 3DGS, leveraging monocular geometry cue and ...

## Contribution
- Extensive experimental results demonstrate the effectiveness of our method in achieving superior mesh quality compared with the SoTA surface reconstruction for 3DGS.
- This paper introduces local structural hints during training to address the challenge.
- This paper presents a novel approach for surface mesh reconstruction from 3D Gaussian Splatting (3DGS) , a technique renowned for its efficiency in novel view synthesis but challenged ...

## Abstract Cue
- This paper presents a novel approach for surface mesh reconstruction from 3D Gaussian Splatting (3DGS) , a technique renowned for its efficiency in novel view synthesis but challenged for surface reconstruction.
