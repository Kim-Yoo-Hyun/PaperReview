# PRISM: Precision Forcing for Generalist Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Evaluation in One Sentence

초록·project는 simulation과 실제 로봇의 connector insertion, 양팔 connector mating, screw tightening을 보고한다. Trial 수·task별 분모·성공 정의와 수치 비교는 본문 대조 전 미확정이다.

## Evaluation Type and Scope

Abstract/project에 명시된 평가 범위만 기록한다. 아래의 확인 필요 항목과 연구자가 제안한 실험을 paper-reported result로 합치지 않는다.

## Dataset / Benchmark Role

초록·project는 simulation과 실제 로봇의 connector insertion, 양팔 connector mating, screw tightening을 보고한다. Trial 수·task별 분모·성공 정의와 수치 비교는 본문 대조 전 미확정이다.

Resource 이름은 위 source가 evaluation 용도로 명시한 경우만 사용한다. 정확한 training/evaluation role, split, size와 데이터 중복은 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Metrics and Success Definition

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Baselines and Fairness

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. Baseline identity, 같은 observation/action, demonstration/interaction, reward access와 compute 조건을 본문에서 대조한다.

## Ablations and Sensitivity

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Generalization and Failure Cases

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. 특히 정밀도 proxy와 실제 공차의 차이·flow-time weighting·SNR gate·auxiliary loss·task별 trial·공개 구현의 논문 일치을 점검한다.

## Statistics, Efficiency, and Reproducibility

Trials/seeds, confidence interval, checkpoint/commit, reset/timeout, hardware와 control latency는 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Proposed Evaluation — Researcher Interpretation

Action-expert 재가중과 geometry adapter 학습을 동일 데이터/label/compute에서 분리하고 정밀도별 성공·일반 task 유지 성능을 함께 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.14704) · [저자 project/code](https://seen-e.github.io/PRISM/) · [공식 code](https://github.com/seen-e/PRISM). Main table·appendix·negative result는 본문 수동 확인 필요.
