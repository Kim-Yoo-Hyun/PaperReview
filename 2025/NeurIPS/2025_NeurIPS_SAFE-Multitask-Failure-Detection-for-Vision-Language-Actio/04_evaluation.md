# Evaluation

- Year/Venue: 2025 / NeurIPS
- Category: World Models, Safety, and Recovery
- Tags: Robotics, VLA, failure detection, conformal prediction, uncertainty
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://vla-safe.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- LIBERO
- BridgeData

## Metrics
- accuracy
- success rate

## Evaluation Protocol and Results
- Therefore, we use LIBERO-10 in our experiments and test OpenVLA , π0 and π0 -FAST on it.
- Real-world Franka Experiments: We deploy the π0 -FAST-DROID checkpoint 1 on a Franka Emika Panda Robot.
- In experiments, 3 out of 10 tasks are randomly picked and reserved as unseen tasks.
- We train and evaluate the failure detection methods on the Google Robot embodiment and on the WidowX embodiment , respectively.
- We compare SAFE with diverse baselines and show that SAFE achieves state-of-the-art failure detection performance and a favorable trade-off between accuracy and detection time using conformal prediction.
- While vision-language-action models (VLAs) have shown promising robotic behaviors across a diverse set of manipulation tasks, they achieve limited success rates when deployed on novel tasks out of ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
