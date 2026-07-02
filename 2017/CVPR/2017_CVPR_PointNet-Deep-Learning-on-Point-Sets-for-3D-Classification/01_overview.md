# PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation

- Year/Venue: 2017 / CVPR
- Category: Foundations: 3D Geometry and Point Clouds
- Tags: 3D geometry, point cloud, representation
- Paper link: ./2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/paper.pdf
- Code/Project: https://github.com/charlesq34/pointnet
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Guibas PointNet Point cloud is an important type of geometric data structure.
- Due to its irregular format, most researchers transform such data to regular 3D voxel grids or collections of images.
- This, however, renders data unnecessarily voluminous and causes issues.

## Core Idea
- We propose a novel deep net architecture that consumes raw point cloud (set of points) without voxelization or rendering.
- Key to our approach is the use of a single symmetric function, max pooling.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Empirically, it shows strong performance on par or even better than state of the art.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose a novel deep net architecture that consumes raw point cloud (set of points) without voxelization or rendering.
- Key to our approach is the use of a single symmetric function, max pooling.
- Our network, named PointNet, provides a unified architecture for applications ranging from object classification, part segmentation, to scene semantic parsing.

## Abstract Cue
- Guibas PointNet Point cloud is an important type of geometric data structure.
