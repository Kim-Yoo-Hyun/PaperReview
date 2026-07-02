# Evaluation

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_GeoGaussian-Geometry-aware-Gaussian-Splatting-for-Scene-Re/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Replica
- TUM RGB-D

## Metrics
- accuracy
- mAP
- PSNR
- SSIM
- LPIPS

## Evaluation Protocol and Results
- Throughout all experiments, we maintain a consistent learning rate of 0.0002 for Gaussian optimization and γ is set to 0.0002.
- The proposed GeoGaussian approach is trained and evaluated on a desktop PC equipped with an Intel Core i9 12900K 3.50GHz processor and a single GeForce RTX 3090 GPU.
- Following the popular evaluation protocol used in methods , standard photometric rendering quality metrics are employed in the experiment section to evaluate the quality of novel view rendering.
- Particularly, PSNR evaluates on a color-wise basis.
- Our proposed pipeline achieves state-of-the-art performance in novel view synthesis and geometric reconstruction, as evaluated qualitatively and quantitatively on public datasets.
- Throughout all experiments, we maintain a consistent learning rate of 0.0002 for Gaussian optimization and γ is set to 0.0002.

## Baselines
- LPIPS compares features of two images extracted by a pre-trained neural network such as VGG-Net instead of comparing two images directly.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
