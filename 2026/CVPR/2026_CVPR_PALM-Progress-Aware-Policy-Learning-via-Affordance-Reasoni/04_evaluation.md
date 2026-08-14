# Evaluation

- Year/Venue: 2026 / CVPR
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, affordance, progress estimation, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- CALVIN
- LIBERO
- BridgeData

## Metrics
- mAP
- SR
- success rate

## Evaluation Protocol and Results
- Across extensive simulation and real-world experiments, PALM consistently outperforms baselines, achieving a 91.8% success rate on LIBERO-LONG, a 12.5% improvement in average length on CALVIN ABC D, and ...
- For example, on “clean a cluttered table,” state-of-the-art policies typically succeed initially but fail mid-task, unable to reliably complete the full sequence.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
