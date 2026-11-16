# Learning from Hindsight for VLA Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Evaluation in One Sentence

v2 abstract는 LIBERO-PRO의 분포 이동 조작과 실제 Franka 학습을 보고한다. 샘플 효율 개선은 해당 비교 조건의 저자 주장이다.

## Evaluation Type and Scope

Abstract/project에 명시된 평가 범위만 기록한다. 아래의 확인 필요 항목과 연구자가 제안한 실험을 paper-reported result로 합치지 않는다.

## Dataset / Benchmark Role

v2 abstract는 LIBERO-PRO의 분포 이동 조작과 실제 Franka 학습을 보고한다. 샘플 효율 개선은 해당 비교 조건의 저자 주장이다.

Resource 이름은 위 source가 evaluation 용도로 명시한 경우만 사용한다. 정확한 training/evaluation role, split, size와 데이터 중복은 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Metrics and Success Definition

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Baselines and Fairness

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. Baseline identity, 같은 observation/action, demonstration/interaction, reward access와 compute 조건을 본문에서 대조한다.

## Ablations and Sensitivity

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Generalization and Failure Cases

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. 특히 v2의 importance correction·label filtering·모방 대조와 우리 selector의 정확한 차이, VLM 감독 비용과 rollout 분모, 원 지시 평가 독립성을 점검한다.

## Statistics, Efficiency, and Reproducibility

Trials/seeds, confidence interval, checkpoint/commit, reset/timeout, hardware와 control latency는 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Proposed Evaluation — Researcher Interpretation

먼저 자연적으로 참인 관련/비관련 목표가 같은 실패에서 발생하는지 확인한다. 이후 고정 pool에서 균등·객체 일치·원 목표만 학습을 대조한다. 현재 주제의 P0/P1/P2 계약은 별도이며 이 노트는 실험 결과가 아니다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2607.09042) · [저자 project/code](https://iamxjy.github.io/lfh-website/). Main table·appendix·negative result는 본문 수동 확인 필요.
