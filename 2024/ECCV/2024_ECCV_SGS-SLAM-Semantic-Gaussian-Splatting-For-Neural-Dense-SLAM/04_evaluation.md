# Evaluation

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, semantic
- Paper link: ./2024/ECCV/2024_ECCV_SGS-SLAM-Semantic-Gaussian-Splatting-For-Neural-Dense-SLAM/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- Replica

## Metrics
- accuracy
- mIoU
- mAP
- PSNR
- SSIM
- LPIPS
- ATE
- RMSE

## Evaluation Protocol and Results
- 4.1 Experimental Setup Datasets We evaluate our method on both synthetic and real-world datasets.
- To compare with other neural implicit SLAM methods, we evaluate synthetic scenes from Replica dataset and real-world scenes from ScanNet and ScanNet++ datasets.
- Metrics We use PSNR, Depth-L1, SSIM, and LPIPS to evaluate the reconstruction quality.
- To evaluate the camera pose, we use the average absolute trajectory error (ATE RMSE).
- Extensive experiments demonstrate that SGS-SLAM delivers state-of-the-art performance in camera pose estimation, map reconstruction, precise semantic segmentation, and object-level geometric accuracy, while ensuring real-time rendering capabilities.
- 4.1 Experimental Setup Datasets We evaluate our method on both synthetic and real-world datasets.

## Baselines
- To compare with other neural implicit SLAM methods, we evaluate synthetic scenes from Replica dataset and real-world scenes from ScanNet and ScanNet++ datasets.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
