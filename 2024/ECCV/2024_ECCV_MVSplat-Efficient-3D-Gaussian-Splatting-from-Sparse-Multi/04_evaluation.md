# Evaluation

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_MVSplat-Efficient-3D-Gaussian-Splatting-from-Sparse-Multi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- DTU

## Metrics
- accuracy
- PSNR
- SSIM
- LPIPS

## Evaluation Protocol and Results
- Following pixelSpalt , we evaluate all methods on three target novel viewpoints for each test
- On the large-scale RealEstate10K and ACID benchmarks, MVSplat achieves state-of-the-art performance with the fastest feed-forward inference speed (22 fps).
- We demonstrate the importance of the cost volume representation in learning feed-forward Gaussians via extensive experimental evaluations.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
