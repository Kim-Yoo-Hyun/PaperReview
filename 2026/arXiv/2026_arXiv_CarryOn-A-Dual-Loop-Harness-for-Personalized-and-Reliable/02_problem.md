# CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

개인화된 robot assistance에서 고수준 의도와 실행 신뢰성을 연결한다.

## Bottleneck and Changed Formulation

계획과 action safety/recovery의 dual-loop 구조를 frozen VLA에 결합한다.

## System and Robotics Loop

사용자·scene context → 계획 → VLA·shield·recovery.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

메모리 입력, failure detector, recovery 비용, 공개 구현 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation과 실제 robot assistance 결과를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.21453) · [저자 project/code](https://vincent2311.github.io/Projects/CarryOn/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
