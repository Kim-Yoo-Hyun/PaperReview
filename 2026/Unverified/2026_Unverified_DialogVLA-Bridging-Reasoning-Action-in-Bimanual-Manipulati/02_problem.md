# DialogVLA: Bridging Reasoning Action in Bimanual Manipulation via Parallel Mixture-of-Experts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

양팔 조작에서 skill phase와 arm role을 action에 연결한다.

## Bottleneck and Changed Formulation

Structured dialog와 parallel skill/arm MoE가 flow action expert를 조건화한다.

## System and Robotics Loop

Multi-view·언어·proprioception → 양팔 action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

공식 proceedings, 원문 공개, source version, code release.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

저자 project는 RoboTwin, RoboCasa GR1 및 실제 양팔 평가를 제시한다.

## Evidence Anchor

[공식 paper/abstract](https://jjjenghi.github.io/dialogvla/) · [저자 project/code](https://jjjenghi.github.io/dialogvla/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
