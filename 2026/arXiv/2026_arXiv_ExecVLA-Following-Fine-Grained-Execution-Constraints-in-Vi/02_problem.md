# ExecVLA: Following Fine-Grained Execution Constraints in Vision-Language-Action Models with Bi-Level Action Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

목표 달성 외에 세부 수행 방식 제약을 따르게 한다.

## Bottleneck and Changed Formulation

목표/실행 수준의 action representation과 reasoning 신호를 분리한다.

## System and Robotics Loop

관측·실행 제약 지시 → bi-level representation → robot action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

constraint label, evaluator geometry, KineVLA→ExecVLA version, 공개 checkpoint.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO와 Realman robot의 execution-constraint 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2603.17524). Exact objective, constraints, success definition은 본문 수동 확인 필요.
