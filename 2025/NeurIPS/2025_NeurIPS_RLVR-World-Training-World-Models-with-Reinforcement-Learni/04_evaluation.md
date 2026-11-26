# RLVR-World: Training World Models with Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Evaluation in One Sentence

텍스트 환경의 상태 예측과 RT-1 영상 예측을 평가한다. 부록 표 12는 PushT 시뮬레이션에서 각 세계 모델을 CEM 계획기에 넣고 과제 성공률을 비교한다.

## Evaluation Type and Scope

Abstract/project에 명시된 평가 범위만 기록한다. 아래의 확인 필요 항목과 연구자가 제안한 실험을 paper-reported result로 합치지 않는다.

## Dataset / Benchmark Role

텍스트 환경의 상태 예측과 RT-1 영상 예측을 평가한다. 부록 표 12는 PushT 시뮬레이션에서 각 세계 모델을 CEM 계획기에 넣고 과제 성공률을 비교한다.

Resource 이름은 위 source가 evaluation 용도로 명시한 경우만 사용한다. 정확한 training/evaluation role, split, size와 데이터 중복은 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Metrics and Success Definition

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Baselines and Fairness

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. Baseline identity, 같은 observation/action, demonstration/interaction, reward access와 compute 조건을 본문에서 대조한다.

## Ablations and Sensitivity

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Generalization and Failure Cases

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. 특히 reward metric과 task 목표 정합성, planner의 model exploitation, 로봇 행동 평가 유무을 점검한다.

## Statistics, Efficiency, and Reproducibility

Trials/seeds, confidence interval, checkpoint/commit, reset/timeout, hardware와 control latency는 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Proposed Evaluation — Researcher Interpretation

같은 planner·rollout budget에 MLE/RL world model을 각각 넣고 예측 지표와 실제 return을 함께 측정한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b63a24a1832bd14fa945c71f535c0095-Abstract-Conference.html) · [저자 project/code](https://thuml.github.io/RLVR-World/) · [공식 code](https://github.com/thuml/RLVR-World). Main table·appendix·negative result는 본문 수동 확인 필요.
