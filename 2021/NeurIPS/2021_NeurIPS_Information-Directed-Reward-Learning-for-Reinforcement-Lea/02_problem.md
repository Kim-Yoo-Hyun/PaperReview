# Information Directed Reward Learning for Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Reward 정확도 대신 정책 결정에 유용한 expert query를 고른다.

## Bottleneck and Changed Formulation

잠재 최적 정책 간 return 차이에 대한 information gain으로 query를 선택한다.

## System and Robotics Loop

Bayesian reward belief·policy 후보 → query → expert feedback.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

reward prior, policy 후보 생성, expert noise, compute 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

여러 환경과 query 유형에서 label efficiency를 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper/2021/hash/1fa6269f58898f0e809575c9a48747ef-Abstract.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
