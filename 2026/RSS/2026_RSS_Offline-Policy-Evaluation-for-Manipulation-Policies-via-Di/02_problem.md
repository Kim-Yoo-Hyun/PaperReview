# Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

희소 보상·복구 행동·유한 rollout에서 정책 진척을 평가할 때 truncation bias가 발생한다.

## Formulation and Robotics Loop

정책 rollout·목표 상태 → liveness value → offline 정책 평가.

Task completion으로 평가를 정식화한 liveness Bellman operator와 conservative fixed point를 제안한다.

## Assumptions to Verify

고정 정책·목표 predicate·유한 horizon·복구 구간·실제 성공과 진척의 차이.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

TD·Monte Carlo 평가 → liveness evaluation → VLA 제한된 rollout 해석.

실험 rollout 종료와 실제 실패를 구별하고 가치 진단의 target을 정할 최신 기준이다.

## Evidence Boundary

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p154.html). RSS official abstract의 두 simulation 과제를 기록한다. arXiv 초록의 추가 cloth demonstration은 venue 본문에서 동일성을 확인하기 전 평가 범위에 합치지 않았다.
