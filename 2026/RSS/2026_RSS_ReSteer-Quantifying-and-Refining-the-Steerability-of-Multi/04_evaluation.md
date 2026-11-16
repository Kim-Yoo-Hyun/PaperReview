# ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Evaluation in One Sentence

LIBERO와 실제 로봇의 지시 전환을 평가한다. 공개 repository는 LIBERO 평가·데이터 생성 경로를 제공하지만 로컬 native 실행은 아직 확인하지 않았다.

## Evaluation Type and Scope

Abstract/project에 명시된 평가 범위만 기록한다. 아래의 확인 필요 항목과 연구자가 제안한 실험을 paper-reported result로 합치지 않는다.

## Dataset / Benchmark Role

LIBERO와 실제 로봇의 지시 전환을 평가한다. 공개 repository는 LIBERO 평가·데이터 생성 경로를 제공하지만 로컬 native 실행은 아직 확인하지 않았다.

Resource 이름은 위 source가 evaluation 용도로 명시한 경우만 사용한다. 정확한 training/evaluation role, split, size와 데이터 중복은 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Metrics and Success Definition

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Baselines and Fairness

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. Baseline identity, 같은 observation/action, demonstration/interaction, reward access와 compute 조건을 본문에서 대조한다.

## Ablations and Sensitivity

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Generalization and Failure Cases

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. 특히 steerability score의 분모·switch timing·초기 능력, estimator와 실제 성공의 관계, 데이터 생성 비용, 제약 유지·철회가 평가에 포함되는 범위을 점검한다.

## Statistics, Efficiency, and Reproducibility

Trials/seeds, confidence interval, checkpoint/commit, reset/timeout, hardware와 control latency는 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Proposed Evaluation — Researcher Interpretation

기존 R8 단일 지시 전환 IO를 Docker에서 먼저 확인한다. 이후 같은 상태에서 전체 재명시·규칙 갱신·oracle 지시를 비교하는 것은 별도 연구 설계이며 아직 실행하지 않았다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p143.html) · [저자 project/code](https://resteer-vla.github.io/) · [공식 code](https://github.com/ChenZhenY/ReSteer). Main table·appendix·negative result는 본문 수동 확인 필요.
