# Evaluation

- Year/Venue: 2025 / NeurIPS poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_QuadricFormer-Scene-as-Superquadrics-for-3D-Semantic-Occup/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- KITTI
- nuScenes

## Metrics
- accuracy
- mIoU
- IoU

## Evaluation Protocol and Results
- Our method achieves state-of-the-art performance.
- Our method achieves comparable performance to GaussianFormer-2 with much fewer primitives.
- In our experiments, we use the RGB images from the left perspective camera of the ego vehicle as model input.
- The annotated voxel grid extends from 6 ■ vegetation ■ manmade ■ terrain ■ sidewalk ■ other flat ■ drive. suf. ■ truck ■ trailer ■ traffic cone ...
- Extensive experiments on the nuScenes and KITTI-360 datasets demonstrate that QuadricFormer achieves state-of-the-art performance while maintaining superior efficiency.
- Our method achieves state-of-the-art performance.

## Baselines
- Our method achieves state-of-the-art performance.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
