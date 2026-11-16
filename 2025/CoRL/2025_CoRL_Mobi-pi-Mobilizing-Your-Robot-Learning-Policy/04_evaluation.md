# Mobi-π: Mobilizing Your Robot Learning Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Evaluation in One Sentence

RoboCasa 기반 simulated mobile manipulation과 실로봇에서 pose 선택을 비교한다. 이 비교만으로 다른 정책에 선택된 pose를 재사용할 때의 성능을 확정할 수 없다.

## Evaluation Type and Scope

Abstract/project에 명시된 평가 범위만 기록한다. 아래의 확인 필요 항목과 연구자가 제안한 실험을 paper-reported result로 합치지 않는다.

## Dataset / Benchmark Role

RoboCasa 기반 simulated mobile manipulation과 실로봇에서 pose 선택을 비교한다. 이 비교만으로 다른 정책에 선택된 pose를 재사용할 때의 성능을 확정할 수 없다.

Resource 이름은 위 source가 evaluation 용도로 명시한 경우만 사용한다. 정확한 training/evaluation role, split, size와 데이터 중복은 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Metrics and Success Definition

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Baselines and Fairness

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. Baseline identity, 같은 observation/action, demonstration/interaction, reward access와 compute 조건을 본문에서 대조한다.

## Ablations and Sensitivity

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Generalization and Failure Cases

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. 특히 pose 후보와 collision/reachability 처리, 정책별 학습 시야와 데이터 접근, 장면 구축 비용, 실제 도착 상태·평가 분모을 점검한다.

## Statistics, Efficiency, and Reproducibility

Trials/seeds, confidence interval, checkpoint/commit, reset/timeout, hardware와 control latency는 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Proposed Evaluation — Researcher Interpretation

동일 scene·도착 후보·navigation·비용에서 A 선택 재사용, 정책 무관 고정 pose, 제한된 B validation 재선택을 비교한다. 실제 이동 후 상태를 분기하고 전체 시도 분모를 보존한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/yang25b.html) · [저자 project/code](https://mobipi.github.io/) · [공식 code](https://github.com/yjy0625/mobipi). Main table·appendix·negative result는 본문 수동 확인 필요.
