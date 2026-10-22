# Adaptive Action Chunking at Inference-time for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

고정 action chunk 길이가 반응성과 일관성의 균형을 제한한다.

## Bottleneck and Changed Formulation

Action entropy를 이용해 추론 중 실행할 chunk 길이를 조정한다.

## System and Robotics Loop

VLA 예측 sample → uncertainty cue → 실행 길이 → 다음 관측.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

entropy 추정 sample 수, 최소 이동량, sensor/inference timing.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation과 real-robot manipulation 비교를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2604.04161) · [저자 project/code](https://lance-lot.github.io/adaptive-chunking.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
