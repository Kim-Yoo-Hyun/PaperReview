# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_FreeSplatter-Pose-free-Gaussian-Splatting-for-Sparse-view/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Our approach employs a streamlined transformer architecture where self-attention blocks facilitate information exchange among multi-view image tokens, decoding them into pixel-aligned 3D Gaussian primitives within a unified reference ...
- We introduce FreeSplatter, a scalable feed-forward framework that generates high-quality 3D Gaussians from uncalibrated sparse-view images while estimating camera parameters within seconds.
- We develop two specialized variants–for object-centric and scene-level reconstruction–trained on comprehensive datasets.

## 원리적 동기
- While generalizable reconstruction models address sparse-view reconstruction using learned priors in a feed-forward manner, they still require accurate camera parameters, sidestepping a fundamental challenge in real-world applications.
- However, these approaches fail in sparse-view scenarios where traditional camera calibration techniques like Structure-from-Motion (SfM) struggle due to insufficient image overlaps.
- Our approach employs a streamlined transformer architecture where self-attention blocks facilitate information exchange among multi-view image tokens, decoding them into pixel-aligned 3D Gaussian primitives within a unified reference ...

## 핵심 방법론
- The overall training objective is: RRA@15◦ ↑ Table 2.
- We focus on reconstructing observed areas and adopt Splatt3R’s target-view masking strategy, computing rendering loss only for visible regions to prevent negative training guidance from occluded areas. (5) ...
- PF-LRM FreeSplatter-O GSO RRE ↓ RRA@15◦ ↑ RRA@30◦ ↑ TE↓ 3.99 8.96 0.956 0.909 0.976 0.936 0.041 0.090 OmniObject3D (6) where the rendering loss Lrender is a combination ...
- FreeSplatterS leverages a diverse training set comprising BlendedMVS , ScanNet++, and CO3Dv2—a subset of DUSt3R’s training data encompassing outdoor scenes, indoor environments, and real-world objects.
- Experimental Settings Training Datasets.
