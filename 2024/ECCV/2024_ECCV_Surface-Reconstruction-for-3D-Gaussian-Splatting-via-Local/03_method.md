# Method

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_Surface-Reconstruction-for-3D-Gaussian-Splatting-via-Local/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- This paper introduces local structural hints during training to address the challenge.
- We then propose to construct a signed distance field by a moving least square (MLS) function over the Gaussians in each local region.
- We first leverage the prior knowledge from monocular normal and depth estimations to refine the covariance and mean of Gaussian primitives, enhancing their organization and providing crucial normal ...

## 원리적 동기
- Given multi-view images with corresponding camera poses, 3DGS initializes Gaussian primitives from a sparse point cloud that comes from COLMAP and renders a novel view with a dedicated ...
- This paper presents a novel approach for surface mesh reconstruction from 3D Gaussian Splatting (3DGS) , a technique renowned for its efficiency in novel view synthesis but challenged ...
- This paper introduces local structural hints during training to address the challenge.

## 핵심 방법론
- Our primary goal is to reconstruct the scene geometry from 3D Gaussians by aligning Gaussians with the real-world surface.
- With these attributes, a 3D Gaussian can be written as G(\bm {x}) = \exp (-\frac {1}{2}(\bm {x}-\bm {\mu })^T\mathbf {\Sigma }^{-1}(\bm {x}-\bm {\mu })), \label {eqn:density} (1)
- Given a set of M posed RGB images I = {I1 , . . . , IM } with corresponding camera parameters, 3DGS represents the scene as tons ...
- 3.1 Preliminary: 3D Gaussian Splatting and Its Variants 3D Gaussian Splatting represents a 3D scene as a bunch of 3D Gaussian blobs, each of which is defined by ...
