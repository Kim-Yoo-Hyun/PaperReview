# Evaluation

- Year/Venue: 2025 / arXiv
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, policy optimization, simulation, robustness
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy

## Evaluation Protocol and Results
- A.4.1 reveals that, while extending both M and N improves accuracy, practical considerations of computational cost necessitate careful tuning of these hyperparameters to achieve optimal performance.
- The results highlight the superiority of RWM trained with autoregressive training (RWM-AR), which consistently achieves the lowest prediction errors across all environments.
- The experiments are designed to assess the accuracy and robustness of RWM, evaluate its architectural and training design choices, and demonstrate its effectiveness across diverse robotic tasks in ...
- We compare the results with an MLP-based baseline also trained autoregressively with the same history and forecast horizon, as shown in Fig.
- A.4.1 reveals that, while extending both M and N improves accuracy, practical considerations of computational cost necessitate careful tuning of these hyperparameters to achieve optimal performance.
- The results highlight the superiority of RWM trained with autoregressive training (RWM-AR), which consistently achieves the lowest prediction errors across all environments.

## Baselines
- We compare the results with an MLP-based baseline also trained autoregressively with the same history and forecast horizon, as shown in Fig.
- 4.3 Generality across Robotic Environments To assess the generality and robustness of RWM across a diverse range of robotic environments, we compare its performance with several baseline methods, ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
