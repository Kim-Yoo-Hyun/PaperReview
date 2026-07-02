# GaussReg: Fast 3D Registration with Gaussian Splatting

- Year/Venue: 2024 / ECCV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_GaussReg-Fast-3D-Registration-with-Gaussian-Splatting/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- But this method faces two issues: a) it is difficult to turn NeRF of unbounded scene to bounded voxel; b) the resolution limitation of the voxel grid makes ...
- To overcome these problems, deep feature extractors are proposed to find more robust correspondences between two point clouds.
- When considering large-scale scene reconstruction based on NeRF, there are two main challenges: 1) Due to the complex occlusions present in real-world scenes, lots of images or videos ...

## Core Idea
- Training Strategy and Loss Function Due to the scale uncertainty in monocular video reconstruction, we performed data augmentation not only on rotation and translation but also on scaling ...
- In this section, we present our proposed GaussReg for 3D Registration with Gaussian Splatting (GS).

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experimental results demonstrate our method achieves state-ofthe-art performance on multiple datasets.
- 4.1 Experiment Setup Dataset As there is currently no scene-level dataset available for our task, it is necessary for us to create a dataset in order to evaluate ...

## Limitation
- Limitations and Future Work We only adopt a simple strategy to fuse and filter two GS models.
- Future work can further explore to address this issue.
- However, the registration of NeRF representations for large-scale scenes remains underexplored due to the inherent complexities of implicitly modeled geometric relationships.

## Contribution
- Experimental results demonstrate our method achieves state-ofthe-art performance on multiple datasets.
- To this end, we propose GaussReg, a novel coarse-to-fine framework, both fast and accurate.
- Most recently, Gaussian Splatting (GS) is introduced, employing explicit 3D Gaussian.

## Abstract Cue
- Point cloud registration is a fundamental problem for largescale 3D scene scanning and reconstruction.
