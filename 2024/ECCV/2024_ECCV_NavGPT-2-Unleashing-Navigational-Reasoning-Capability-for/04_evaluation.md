# Evaluation

- Year/Venue: 2024 / ECCV
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, Navigation
- Paper link: ./2024/ECCV/2024_ECCV_NavGPT-2-Unleashing-Navigational-Reasoning-Capability-for/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Habitat
- HM3D
- R2R
- RxR

## Metrics
- accuracy
- mAP
- SPL
- SR
- nDTW
- success rate

## Evaluation Protocol and Results
- All experiments are conducted on a single NVIDIA A100 GPU.
- We adopt a comprehensive set of navigation metrics to evaluate performance , including Trajectory Length (TL), which measures the average path length in meters; Navigation Error (NE), the ...
- We demonstrate the data efficiency of the proposed methods and eliminate the gap between LM-based agents and state-of-the-art VLN specialists.
- All experiments are conducted on a single NVIDIA A100 GPU.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
