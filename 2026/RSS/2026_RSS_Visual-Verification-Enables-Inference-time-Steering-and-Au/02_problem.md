# Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

배포된 generalist 정책이 자율 경험에서 유용한 개선 신호를 얻기 어렵다.

## Bottleneck and Changed Formulation

시각 verifier가 후보 행동을 선택하고 검증된 rollout을 후속 정책 학습에 사용한다.

## System and Robotics Loop

기존 정책의 행동 후보 → gradient-free 시각 검증 → 실행·재학습 데이터.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

verifier 오류와 성공 판정의 독립성, fine-tuning objective, 인간 개입의 집계 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

SIMPLER와 실제 DROID setup에서 steering 및 offline 개선을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p079.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
