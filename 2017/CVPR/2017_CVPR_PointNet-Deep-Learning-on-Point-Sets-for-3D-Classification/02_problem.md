# Problem

- Year/Venue: 2017 / CVPR
- Category: Foundations: 3D Geometry and Point Clouds
- Tags: 3D geometry, point cloud, representation
- Paper link: ./2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/paper.pdf
- Code/Project: https://github.com/charlesq34/pointnet
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Guibas PointNet Point cloud is an important type of geometric data structure.
- Due to its irregular format, most researchers transform such data to regular 3D voxel grids or collections of images.
- This, however, renders data unnecessarily voluminous and causes issues.

## 해결하려는 문제
- We propose a novel deep net architecture that consumes raw point cloud (set of points) without voxelization or rendering.
- Key to our approach is the use of a single symmetric function, max pooling.
- Our network, named PointNet, provides a unified architecture for applications ranging from object classification, part segmentation, to scene semantic parsing.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
