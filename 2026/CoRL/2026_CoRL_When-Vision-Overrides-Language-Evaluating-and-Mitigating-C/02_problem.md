# When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

장면의 학습 편향 때문에 VLA가 다른 유효한 언어 지시보다 익숙한 행동을 반복한다.

## Bottleneck and Changed Formulation

LIBERO-CF로 반사실적 지시 수행을 평가하고 언어 조건부·비조건부 분기의 차이로 행동을 유도한다.

## System and Robotics Loop

같은 LIBERO 장면의 대체 지시 → VLA/VA 분기 → 조작 행동.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

focused suite의 장면 변경·OR/target-only 종료·두 목표의 기본 능력·guidance 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO-CF와 실제 로봇에서 언어 grounding과 task success를 구별해 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2602.17659) · [저자 project/code](https://vla-cf.github.io/) · [공식 code](https://github.com/yuffish/VLA-CF). Exact objective, constraints, success definition은 본문 수동 확인 필요.
