# Evaluation

- Year/Venue: 2023 / ICRA
- Category: Sensor Fusion, LiDAR, and Autonomous Driving
- Tags: sensor fusion, LiDAR, 3D perception
- Paper link: ./2023/ICRA/2023_ICRA_BEVFusion-Multi-Task-Multi-Sensor-Fusion-with-Unified-Bird/paper.pdf
- Code/Project: https://github.com/mit-han-lab/bevfusion
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- nuScenes
- Waymo

## Metrics
- mIoU
- IoU
- mAP
- NDS

## Evaluation Protocol and Results
- I: BEVFusion achieves state-of-the-art 3D object detection performance on nuScenes (val and test) without bells and whistles.
- Most state-of-the-art sensor fusion methods , , decorate LiDAR points with their corresponding camera features (e.g., semantic labels, CNN features or virtual points).
- Aggregation 0 Interval Reduction: 22.1× Precomputation: 1.9× log scale 500ms 20 40 (c) Improvement breakdown LSS: 136.8ms Ours: 4.8ms 1/16 FPN 512.1ms 12.0ms 1/8 FPN 2127.3ms 45.1ms 1/4 ...
- A Results fi fi (a) Camera-to-BEV transformation Thread 1 Thread 2 Thread 3 4 4 7 : Stored to DRAM (Slow) (b) Ef cient BEV pooling Depth Grid ...
- I: BEVFusion achieves state-of-the-art 3D object detection performance on nuScenes (val and test) without bells and whistles.
- To achieve this, we diagnose and lift the key efficiency bottlenecks in the view transformation with optimized BEV pooling, reducing latency by more than 40×.

## Baselines
- Most state-of-the-art sensor fusion methods , , decorate LiDAR points with their corresponding camera features (e.g., semantic labels, CNN features or virtual points).
- I: BEVFusion achieves state-of-the-art 3D object detection performance on nuScenes (val and test) without bells and whistles.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
