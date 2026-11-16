# Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

Task completion으로 평가를 정식화한 liveness Bellman operator와 conservative fixed point를 제안한다.

## Observation, State, and Action

정책 rollout·목표 상태 → liveness value → offline 정책 평가.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: 고정 정책·목표 predicate·유한 horizon·복구 구간·실제 성공과 진척의 차이.

## Method-Specific Comparison — Researcher Interpretation

같은 rollout의 truncation 길이를 바꾸어 TD·MC·liveness 순위와 완주 결과를 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p154.html). RSS official abstract의 두 simulation 과제를 기록한다. arXiv 초록의 추가 cloth demonstration은 venue 본문에서 동일성을 확인하기 전 평가 범위에 합치지 않았다.
