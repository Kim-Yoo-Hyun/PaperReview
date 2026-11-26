# PROSPECT: Unified Streaming Vision-Language Navigation via Semantic–Spatial Fusion and Latent Predictive Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Streaming VLN에서 의미 정보와 공간 정보를 함께 이용하고 미래 상태를 학습할 필요가 있다.

## Bottleneck and Changed Formulation

CUT3R 공간 표현과 SigLIP 의미 표현을 융합하고 학습 중 미래 2D·3D latent prediction을 보조 목표로 사용한다.

## System and Robotics Loop

단안 RGB 프레임과 언어 지시로 전진·회전·정지 행동을 예측한다. 미래 표현 예측 분기는 훈련 시에만 사용한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

미래 target 접근, inference 비용 산정, map/history memory 조건.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

VLN-CE와 실제 항법을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/11673313/) · [저자 project/code](https://github.com/Debactor/PROSPECT). Exact objective, constraints, success definition은 본문 수동 확인 필요.
