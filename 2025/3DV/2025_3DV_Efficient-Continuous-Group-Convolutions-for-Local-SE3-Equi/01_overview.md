# Efficient Continuous Group Convolutions for Local SE(3) Equivariance in 3D Point Clouds

- Year/Venue: 2025 / 3DV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: equivariant, point cloud, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_Efficient-Continuous-Group-Convolutions-for-Local-SE3-Equi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Approaches learning directly from 3D data often take inspiration from the success in 2D vision and address two of the main challenges in such data representation, order invariance ...
- While efforts have been made to develop efficient SE(3) equivariant networks, existing approaches rely on discretization or only introduce global rotation equivariance.
- While global equivariant designs ensure robustness to whole-scene rotations, they fail with randomly rotated scene parts or elements.

## Core Idea
- Compared to other state-ofthe-art local rotation equivariant methods, E2PN and EPN , the computational resources needed for our approach are significantly lower even when using 4 samples.
- In the past years, several neural network architectures have been proposed to process such data .

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experiments show that our approach achieves competitive or superior performance across a range of datasets and tasks, including object classification and semantic segmentation, with negligible computational overhead.
- In particular, for 3D data, expanding equivariance to the SE(3) group (rotation and translation) results in a 6D convolution operation, which is not tractable for larger data samples ...
- Extending the translation equivariance property of convolutional neural networks to larger symmetry groups has been shown to reduce sample complexity and enable more discriminative feature learning.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our experiments show that our approach achieves competitive or superior performance across a range of datasets and tasks, including object classification and semantic segmentation, with negligible computational overhead.
- In the past years, several neural network architectures have been proposed to process such data .
- In particular, for 3D data, expanding equivariance to the SE(3) group (rotation and translation) results in a 6D convolution operation, which is not tractable for larger data samples ...

## Abstract Cue
- Extending the translation equivariance property of convolutional neural networks to larger symmetry groups has been shown to reduce sample complexity and enable more discriminative feature learning.
