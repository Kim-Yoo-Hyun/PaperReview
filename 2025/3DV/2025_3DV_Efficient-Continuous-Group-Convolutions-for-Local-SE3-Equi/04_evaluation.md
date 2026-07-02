# Evaluation

- Year/Venue: 2025 / 3DV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: equivariant, point cloud, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_Efficient-Continuous-Group-Convolutions-for-Local-SE3-Equi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- ModelNet40

## Metrics
- accuracy
- mIoU
- mAP

## Evaluation Protocol and Results
- Our experiments show that our approach achieves competitive or superior performance across a range of datasets and tasks, including object classification and semantic segmentation, with negligible computational overhead.
- In particular, for 3D data, expanding equivariance to the SE(3) group (rotation and translation) results in a 6D convolution operation, which is not tractable for larger data samples ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
