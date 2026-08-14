# Evaluation

- Year/Venue: 2024 / CoRL
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, locomotion, model-based reinforcement learning, real-world learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/utexas.edu/ssrl
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy
- mAP

## Evaluation Protocol and Results
- 4.1 Real-world Results We demonstrate our approach through two real-world experiments where a Unitree Go1 quadruped is trained from scratch to achieve maximum speed on both hard ground ...
- 4.2 Simulated Experiments In addition to the results presented here, we provide extensive ablations on standard RL benchmarks in Appendix C.
- Predictions from semi-structured dynamics models demonstrate greater accuracy and improved generalization beyond training data compared to black-box models.
- After just 3.0 min of real-world data, the quadruped achieves an average velocity of 0.98 m s−1 on hard ground and 0.53 m s−1 on memory foam (Fig.
- Video and code are available at: https://sites.google.com/utexas.edu/ssrl 4.1 Real-world Results We demonstrate our approach through two real-world experiments where a Unitree Go1 quadruped is trained from scratch to ...
- 4.2 Simulated Experiments In addition to the results presented here, we provide extensive ablations on standard RL benchmarks in Appendix C.

## Baselines
- To examine model accuracy, we compare the learned external force predictions τ̄te,i to real-world external force estimates τ e over one second.
- Predictions from semi-structured dynamics models demonstrate greater accuracy and improved generalization beyond training data compared to black-box models.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
