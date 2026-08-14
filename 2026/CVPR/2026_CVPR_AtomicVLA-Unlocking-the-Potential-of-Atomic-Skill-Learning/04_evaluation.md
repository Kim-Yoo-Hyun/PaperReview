# Evaluation

- Year/Venue: 2026 / CVPR
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, atomic skills, skill composition, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- CALVIN
- LIBERO

## Metrics
- accuracy
- mAP
- success rate

## Evaluation Protocol and Results
- By unifying task planning and action execution within this framework, it achieves strong performance on long-horizon and continual learning tasks in both simulation and real-world settings. world deployments ...
- In simulation, AtomicVLA outperforms π0 by 2.4% on LIBERO, 10% on LIBERO-LONG, and outperforms π0 and π0.5 by 0.22 and 0.25 in average task length on CALVIN.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
