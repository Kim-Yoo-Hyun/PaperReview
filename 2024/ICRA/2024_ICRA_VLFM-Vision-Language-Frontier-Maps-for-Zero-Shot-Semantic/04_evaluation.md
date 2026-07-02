# Evaluation

- Year/Venue: 2024 / ICRA
- Category: Navigation and Embodied AI
- Tags: Vision-Language Navigation, Robotics, Navigation, semantic
- Paper link: ./2024/ICRA/2024_ICRA_VLFM-Vision-Language-Frontier-Maps-for-Zero-Shot-Semantic/paper.pdf
- Code/Project: https://github.com/bdaiinstitute/vlfm
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- COCO
- Matterport3D
- Habitat
- HM3D

## Metrics
- accuracy
- mAP
- SPL
- SR
- success rate

## Evaluation Protocol and Results
- Remarkably, VLFM achieves state-of-the-art results on all three datasets as measured by success weighted by path length (SPL) for the Object Goal Navigation task.
- We deploy VLFM on Spot and demonstrate its capability to efficiently navigate to target objects within an office building in the real world, without any prior knowledge of ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
