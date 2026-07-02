# Problem

- Year/Venue: 2025 / 3DV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: equivariant, point cloud, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_Efficient-Continuous-Group-Convolutions-for-Local-SE3-Equi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Approaches learning directly from 3D data often take inspiration from the success in 2D vision and address two of the main challenges in such data representation, order invariance ...
- While efforts have been made to develop efficient SE(3) equivariant networks, existing approaches rely on discretization or only introduce global rotation equivariance.
- While global equivariant designs ensure robustness to whole-scene rotations, they fail with randomly rotated scene parts or elements.

## 해결하려는 문제
- Our experiments show that our approach achieves competitive or superior performance across a range of datasets and tasks, including object classification and semantic segmentation, with negligible computational overhead.
- In the past years, several neural network architectures have been proposed to process such data .
- In particular, for 3D data, expanding equivariance to the SE(3) group (rotation and translation) results in a 6D convolution operation, which is not tractable for larger data samples ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
