# Measuring the Stability Assumption Behind Action Chunking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Chunk 실행 중 상태 perturbation이 어떻게 증폭되는지 측정한다.

## Bottleneck and Changed Formulation

Open-loop/closed-loop branch의 finite-horizon divergence를 비교한다.

## System and Robotics Loop

같은 초기 상태·action perturbation → rollout → divergence slope.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

norm 단위, perturbation 크기, branch 동치, 전역 안정성과의 차이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

GR00T manipulation task에서 chunk 안정성 가정의 차이를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.01626) · [저자 project/code](https://aryangoyal7.github.io/publication/2026-stability-action-chunking). Exact objective, constraints, success definition은 본문 수동 확인 필요.
