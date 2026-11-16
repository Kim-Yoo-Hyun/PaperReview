# JIGGLE: An Active Sensing Framework for Boundary Parameters Estimation in Deformable Surgical Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

가려진 deformable tissue의 부착 조건을 손상 없이 알아내야 한다.

## Bottleneck and Changed Formulation

미분 가능한 soft-body 모델·EKF 추정과 정보 이득/안전 비용을 고려한 능동 조작을 결합한다.

## System and Robotics Loop

Stereo 관측·조작 → attachment 추정 → sensing action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

재료 모델과 attachment 가정, 안전 비용 정의.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

실제 동물 조직의 부착점과 cutting/suturing 변화 실험을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss20/p007.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
