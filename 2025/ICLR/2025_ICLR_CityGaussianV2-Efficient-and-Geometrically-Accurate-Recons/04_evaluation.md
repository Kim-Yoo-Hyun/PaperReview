# Evaluation

- Year/Venue: 2025 / ICLR Poster
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2025/ICLR/2025_ICLR_CityGaussianV2-Efficient-and-Geometrically-Accurate-Recons/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy
- mAP
- PSNR
- SSIM
- LPIPS

## Evaluation Protocol and Results
- For instance, as indicated in its own paper (Xiong et al., 2024), such a protocol significantly underestimates the geometric accuracy of SuGaR, which demonstrates promising performance in mesh ...
- Recently, GauU-Scene (Xiong et al., 2024) introduced the first benchmark, but its evaluation protocol overlooks boundary effects, leading to unreliable assessments.
- For instance, as indicated in its own paper (Xiong et al., 2024), such a protocol significantly underestimates the geometric accuracy of SuGaR, which demonstrates promising performance in mesh ...
- Recently, GauU-Scene (Xiong et al., 2024) introduced the first benchmark, but its evaluation protocol overlooks boundary effects, leading to unreliable assessments.

## Baselines
- For all the compared methods, we first extract mesh and then sample points from the surface.
- Moreover, GauU-Scene does not align the surface points extraction process across methods, leading to unfair comparison.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
