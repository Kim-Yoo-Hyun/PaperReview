# Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Source-Supported Evaluation Scope

RSS abstract는 VLA·diffusion policy를 이용한 두 simulation 조작 과제를 명시한다.

## Metrics, Baselines, and Generalization

고정 정책·목표 predicate·유한 horizon·복구 구간·실제 성공과 진척의 차이.

정확한 dataset/split·trial 수·baseline budget·metric 정의·ablation 수치는 이번 초록 정리에서 확정하지 않았다. 이는 원문에 미보고됐다는 뜻이 아니다.

## Reproducibility and Limitations

RSS official abstract의 두 simulation 과제를 기록한다. arXiv 초록의 추가 cloth demonstration은 venue 본문에서 동일성을 확인하기 전 평가 범위에 합치지 않았다.

공개 code/project가 있어도 실행 재현을 뜻하지 않는다. 실제 로봇·simulation·이론/survey의 범위를 위 평가 설명대로 구별한다.

## Proposed Comparison — Researcher Interpretation

같은 rollout의 truncation 길이를 바꾸어 TD·MC·liveness 순위와 완주 결과를 비교한다.

아직 실행하지 않았으며 예상 이득을 측정 결과로 기록하지 않는다.

## Evidence

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p154.html). Code/project·확인 날짜는 [overview](./01_overview.md)를 따른다.
