# Evaluation

- Year/Venue: 2026 / ECCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2026/ECCV/2026_ECCV_PolicyTrim-Boosting-Intrinsic-Policy-Efficiency-of-Vision/paper.pdf
- Code/Project: https://inceptionwang.github.io/PolicyTrim/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- LIBERO
- ManiSkill

## Metrics
- accuracy
- SR
- success rate

## Evaluation Protocol and Results
- These results suggest that our efficiency gains arise from a fundamentally improved execution strategy rather than any sacrifice in task competence.
- The consistent improvements across diverse physical simulators, action spaces, and model architectures demonstrate that PolicyTrim generalizes well beyond the LIBERO benchmark, confirming that policy efficiency optimization yields substantial ...
- Under identical configurations, the baseline incurs redundant physical actions, whereas PolicyTrim achieves task completion in roughly half the steps. divergence among the evaluated models. π0.5 and GR00T both ...
- These results demonstrate that PolicyTrim provides consistent gains across different VLA decoding architectures, and that its redundancy-aware optimization is not tied to a specific action decoding form.
- Extensive experiments across three benchmarks and three VLA models demonstrate that PolicyTrim improves action chunk utilization by 3× and reduces physical execution steps by 51.4%.
- These results suggest that our efficiency gains arise from a fundamentally improved execution strategy rather than any sacrifice in task competence.

## Baselines
- 3 provides a qualitative comparison between the baseline and PolicyTrim on tasks randomly sampled from LIBERO under identical configurations.
- For action chunk extension, we observe an architectural PolicyTrim 11 Ours Baseline Pick up the black bowl on the wooden cabinet and place it on the plate Ours ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
