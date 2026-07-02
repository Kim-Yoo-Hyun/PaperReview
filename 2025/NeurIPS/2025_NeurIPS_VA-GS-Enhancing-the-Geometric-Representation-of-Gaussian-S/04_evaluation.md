# Evaluation

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, semantic, alignment, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_VA-GS-Enhancing-the-Geometric-Representation-of-Gaussian-S/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- DTU
- Tanks and Temples

## Metrics
- accuracy
- mAP
- Chamfer
- PSNR
- SSIM
- LPIPS

## Evaluation Protocol and Results
- We evaluate our surface reconstruction performance on the DTU and Tanks and Temples (TNT) datasets.
- For novel view synthesis, we evaluate using three widely adopted image quality metrics: PSNR, SSIM, and LPIPS.
- Extensive experiments on standard benchmarks demonstrate that our method achieves stateof-the-art performance in both surface reconstruction and novel view synthesis.
- Specifically, we incorporate edge-aware image cues into the rendering loss to improve surface boundary delineation.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
