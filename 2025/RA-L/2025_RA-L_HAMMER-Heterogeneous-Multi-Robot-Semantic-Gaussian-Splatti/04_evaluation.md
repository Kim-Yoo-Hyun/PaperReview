# Evaluation

- Year/Venue: 2025 / RA-L
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, Gaussian Splatting, semantic
- Paper link: ./2025/RA-L/2025_RA-L_HAMMER-Heterogeneous-Multi-Robot-Semantic-Gaussian-Splatti/paper.pdf
- Code/Project: https://hammer-project.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Replica

## Metrics
- accuracy
- mAP
- PSNR
- SSIM
- LPIPS
- SR
- collision

## Evaluation Protocol and Results
- Radiance field-based methods can achieve photorealistic novel-view synthesis and even capture thin, transparent, and reflective surface geometries that are challenging to model with traditional representations.
- In real-world experiments, HAMMER creates better maps compared to baselines and is useful for downstream tasks, such as semantic navigation (e.g., “go to the couch”).

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
