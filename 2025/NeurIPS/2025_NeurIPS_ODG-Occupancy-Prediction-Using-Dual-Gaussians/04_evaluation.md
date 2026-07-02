# Evaluation

- Year/Venue: 2025 / NeurIPS poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_ODG-Occupancy-Prediction-Using-Dual-Gaussians/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- nuScenes
- Waymo
- Occ3D

## Metrics
- accuracy
- mIoU
- mAP
- Chamfer

## Evaluation Protocol and Results
- For experiments on Waymo, we sample 20% of the data matching practices in previous works .
- 4.1 Experiment Setup Datasets: We evaluate our model on the Occ3D benchmark which bootstraps the nuScenes and Waymo-Open dataset.1 nuScenes consists of 1,000 scenes with a split of ...
- Evaluation Metrics: We evaluate our model under the mIoU and RayIoU metric: P |Pr ∩ Gr | |P ∩ G| mIoU = , RayIoU = Pr∈R , |P ...
- During inference, we adopt the standard practice and make use of the camera visibility masks provided by the dataset and only evaluate in unoccluded regions.
- Extensive experiments on the Occ3D-nuScenes and Occ3D-Waymo benchmarks demonstrate our proposed method sets new state-of-the-art results while maintaining low inference cost.
- For experiments on Waymo, we sample 20% of the data matching practices in previous works .

## Baselines
- Following previous works , we use ResNet-50 as image backbone to extract multi-camera image features.
- For experiments on Waymo, we sample 20% of the data matching practices in previous works .

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
