# Evaluation

- Year/Venue: 2021 / ICCV
- Category: Robotics-Enabling 3D Perception
- Tags: Robotics, 3D Vision, active perception, articulated objects, part discovery
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://act-the-part.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- PartNet
- PartNet-Mobility

## Metrics
- accuracy
- mIoU
- IoU
- mAP

## Evaluation Protocol and Results
- Our experiments show AtP learns efficient strategies for part discovery, can generalize to unseen categories, and is capable of conditional reasoning for the task.
- Although trained in simulation, we show convincing transfer to real world data with no fine-tuning.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
