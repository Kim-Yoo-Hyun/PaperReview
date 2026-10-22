# Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

이진 성공 외의 풍부한 신호로 robot policy를 효율적으로 비교한다.

## Bottleneck and Changed Formulation

Progress 등 bounded metric에 기반한 통계적 순차 비교를 제안한다.

## System and Robotics Loop

Trial-level metric → evidence update → policy comparison.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

boundedness, anytime 보장, metric 편향, 반복 model selection.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation과 실제 robot policy 비교를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p076.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
