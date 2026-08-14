# Evaluation

- Year/Venue: 2026 / CVPR
- Category: Robot Learning and Data
- Tags: Robotics, humanoid, pixel-to-action, visual sim-to-real, articulated object manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- success rate
- collision

## Evaluation Protocol and Results
- Trained entirely on synthetic simulation data, the resulting policy achieves robust zero-shot 1.
- performance across diverse articulated objects—including multiple door types—and outperforms human teleoperators by up to 31.7% in task completion time under the same whole-body control stack.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
