# Evaluation

- Year/Venue: 2025 / RSS
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, quadruped locomotion, loco-manipulation, human demonstrations
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://www.roboticsproceedings.org/rss21/p122.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- Open X-Embodiment

## Metrics
- accuracy
- mAP
- SR
- success rate
- collision

## Evaluation Protocol and Results
- We validate our system on six real-world manipulation tasks, where it *Authors contributed equally to this work. achieves an average success rate improvement of 41.9% overall and 79.7% ...
- Pretraining with human data contributes a 38.6% success rate improvement overall and 82.7% under OOD settings, enabling consistently better performance with only half the amount of robot data.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
