# Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VLA의 생성 행동이 지시 의도와 어긋나며 후보 다양성만 늘려도 선택 문제가 남는다.

## Bottleneck and Changed Formulation

지시 재표현과 action sample을 함께 확장하고 contrastive verifier로 prompt·action을 선택한다.

## System and Robotics Loop

VLM instruction rephrasing → VLA action candidates → verifier selection; 계층형 test-time pipeline.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

재표현의 의미 보존, verifier 감독량, rollout-independent evaluation.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

SIMPLER·PolaRiS와 실로봇의 in/out-of-distribution 지시 실행을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2602.12281) · [저자 project/code](https://cover-vla.github.io/) · [공식 code](https://github.com/cover-vla/cover-vla). Exact objective, constraints, success definition은 본문 수동 확인 필요.
