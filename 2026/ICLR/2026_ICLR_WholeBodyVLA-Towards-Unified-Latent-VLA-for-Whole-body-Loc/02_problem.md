# WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

이동과 상체 조작을 결합할 때 데이터 부족과 decision–execution 차이를 줄인다.

## Bottleneck and Changed Formulation

Unified latent VLA와 loco-manipulation-oriented low-level RL을 연결한다.

## System and Robotics Loop

시각·언어 → 상체 action·locomotion command → whole-body control.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

실행 가능한 codebase, latent supervision, controller budget.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Humanoid loco-manipulation과 확장 task를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ff7373914a96956f2a7cacbdf3b0b8d8-Abstract-Conference.html) · [저자 project/code](https://opendrivelab.com/WholebodyVLA). Exact objective, constraints, success definition은 본문 수동 확인 필요.
