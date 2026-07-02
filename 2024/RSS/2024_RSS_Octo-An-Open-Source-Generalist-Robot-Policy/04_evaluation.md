# Evaluation

- Year/Venue: 2024 / RSS
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, generalist policy, Imitation Learning
- Paper link: ./2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/paper.pdf
- Code/Project: https://octo-models.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- KITTI
- nuScenes
- Waymo
- CALVIN
- BridgeData
- Open X-Embodiment

## Metrics
- mAP
- success rate

## Evaluation Protocol and Results
- Correspondence to {dibya.ghosh, homer_walke, pertsch, kvablack, oier.mees}@berkeley.edu experience from other robots and tasks offers a possible particular combination of these components into a powerful solution, exposing models to ...
- In experiments across 9 robotic platforms, we demonstrate that Octo serves as a versatile policy initialization that can be effectively finetuned to new observation and action spaces.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
