# Can Vision-Language-Action Models Learn from Real-World Data Continually without Forgetting?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

실제 로봇 VLA를 순차적으로 적응시킬 때 망각과 성능을 함께 평가한다.

## Bottleneck and Changed Formulation

실환경 continual 학습에서 replay와 데이터 정규화 등 기본 recipe를 비교한다.

## System and Robotics Loop

순차 task demonstration → VLA update → 기존/신규 task 실행.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

v3 변경점, normalization 범위, joint training compute, trial 수.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

단일 팔과 양팔 실환경 continual learning을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2605.26820). Exact objective, constraints, success definition은 본문 수동 확인 필요.
