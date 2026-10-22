# Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

이질적인 로봇 데이터를 늘리면 항상 VLA가 좋아지는가.

## Bottleneck and Changed Formulation

EEF-relative 정렬·embodiment mixture·regularization을 통제 비교하고 평가자 편향 통제를 제안한다.

## System and Robotics Loop

이종 robot demonstration → 정렬된 action 표현 → VLA.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

EEF frame, normalization, split, grouped blind protocol.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation과 real-robot 평가에서 데이터 혼합과 negative transfer를 분석한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2602.09722). Exact objective, constraints, success definition은 본문 수동 확인 필요.
