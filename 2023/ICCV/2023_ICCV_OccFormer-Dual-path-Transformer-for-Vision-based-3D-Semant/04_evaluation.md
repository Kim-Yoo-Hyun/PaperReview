# Evaluation

- Year/Venue: 2023 / ICCV
- Category: Foundations: 3D Semantic Occupancy
- Tags: 3D Vision, semantic, occupancy, Transformer
- Paper link: ./2023/ICCV/2023_ICCV_OccFormer-Dual-path-Transformer-for-Vision-based-3D-Semant/paper.pdf
- Code/Project: https://github.com/zhangyp15/OccFormer
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- KITTI
- SemanticKITTI
- nuScenes

## Metrics
- mIoU
- IoU
- mAP

## Evaluation Protocol and Results
- Experimental results demonstrate that OccFormer significantly outperforms existing methods for semantic scene completion on SemanticKITTI dataset and for LiDAR semantic segmentation on nuScenes dataset.
- OccFormer achieves a long-range, dynamic, and efficient encoding of the camera-generated 3D voxel features.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
