# Evaluation

- Year/Venue: 2025 / RA-L
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, diffusion policy, model-based planning, contact-rich manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://computationalrobotics.seas.harvard.edu/GPC/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy
- IoU
- SSIM

## Evaluation Protocol and Results
- Across diverse robotic manipulation tasks—state- and visionbased, in simulation and on real hardware—GPC consistently outperforms standard behavior cloning and compares favorably to other inference-time adaptation baselines.
- While MPC-style planning has demonstrated robustness across robotics and control, it typically relies on carefully engineered models and objectives, making direct integration with modern generative policies challenging.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
