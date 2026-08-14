# Evaluation

- Year/Venue: 2024 / ICML
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, video prediction, language planning, compositional generalization
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://robodreamer.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- RLBench

## Metrics
- mAP
- success rate

## Evaluation Protocol and Results
- Our approach can successfully synthesize video plans on unseen goals in the RT-X, enables successful robot execution in simulation, and substantially outperforms monolithic baseline approaches to video generation.
- We further show how such a factorization enables us to add additional multimodal goals, allowing us to specify a video we wish to generate given both natural language ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
