# Evaluation — What Matters in Learning from Offline Human Demonstrations for Robot Manipulation

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2021 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, offline learning, robot dataset, Benchmark, robomimic
- Official paper: https://proceedings.mlr.press/v164/mandlekar22a.html
- Official PDF: https://proceedings.mlr.press/v164/mandlekar22a/mandlekar22a.pdf
- Code/Project: https://robomimic.github.io/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Verified Evaluation Scope

- 공식 PMLR 기록은 5개 simulated, 3개 real-world multi-stage manipulation task와 서로 다른 quality의 dataset을 보고한다.
- Algorithm뿐 아니라 demonstration quality와 stopping criterion에 민감하다는 점을 평가한다.

## Required Comparison Fields

- Embodiment/task와 simulation/real-robot 여부
- Observation, action representation, action horizon과 control rate
- Data source, demonstration quality와 train/test generalization split
- Success뿐 아니라 latency, intervention, failure severity와 reproducibility cost

## Reproducible Minimum

RoboMimic의 한 simulated task에서 BC, BC-RNN과 mixed-quality subset을 비교하고 validation loss와 rollout success의 불일치를 확인한다.

## Manual Review Needed

- Exact trial count, uncertainty interval, baseline configuration와 ablation은 full text에서 확인한다.
