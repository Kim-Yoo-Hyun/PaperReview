# PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VLA action의 시간 해상도를 task에 맞게 조절한다.

## Bottleneck and Changed Formulation

여러 시간 granularity의 표현과 router로 적응형 temporal quantization을 구성한다.

## System and Robotics Loop

관측 → temporal 선택·action decoding → robot tracking.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

v2 controller 설정, router 비용, task별 gain, success/time denominator.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation과 실제 manipulation에서 실행 효율·성능을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.25961) · [저자 project/code](https://pacevla.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
