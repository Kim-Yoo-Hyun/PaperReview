# Evaluation

- Year/Venue: 2023 / NeurIPS
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: 3D Vision, occupancy, sensor fusion, Benchmark
- Paper link: ./2023/NeurIPS/2023_NeurIPS_Occ3D-A-Large-Scale-3D-Occupancy-Prediction-Benchmark-for/paper.pdf
- Code/Project: https://tsinghua-mars-lab.github.io/Occ3D/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- KITTI
- SemanticKITTI
- nuScenes
- Waymo
- Occ3D

## Metrics
- accuracy
- mIoU
- IoU
- mAP

## Evaluation Protocol and Results
- To benchmark our proposed Occ3D datasets and our CTF-Occ model, we evaluate existing 3D occupancy prediction methods on Occ3D-nuScenes and Occ3D-Waymo.
- Lastly, we propose a new model, dubbed Coarse-to-Fine Occupancy (CTF-Occ) network, which demonstrates superior performance on the Occ3D benchmarks.
- To benchmark our proposed Occ3D datasets and our CTF-Occ model, we evaluate existing 3D occupancy prediction methods on Occ3D-nuScenes and Occ3D-Waymo.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
