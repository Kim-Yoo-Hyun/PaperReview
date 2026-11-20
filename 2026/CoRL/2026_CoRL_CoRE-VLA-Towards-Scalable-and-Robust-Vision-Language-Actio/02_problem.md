# CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

서로 다른 센서 구성과 auxiliary sensor 손실에 VLA를 대응시킨다.

## Bottleneck and Changed Formulation

Sensor availability와 task intent를 이용해 sparse expert를 routing한다.

## System and Robotics Loop

RGB·언어·proprioception·optional depth → action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

v2 depth degradation 평가, availability indicator, 공식 CoRL 채택 확인.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO, RoboCasa GR1, 실제 dual-arm 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2607.03693) · 저자 프로젝트·코드 주소 미확인. Exact objective, constraints, success definition은 본문 수동 확인 필요.
