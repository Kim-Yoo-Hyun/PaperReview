# Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Pixel-level interactive world model에서 VLA RL을 수행할 때 multi-view 불일치와 rollout 오차 누적이 발생한다.

## Bottleneck and Changed Formulation

Unified multimodal model 기반 dynamics, interleaved multi-view decoding 및 chunk-level branched rollout을 결합한다.

## System and Robotics Loop

Multi-view observation + VLA action chunk → imagined next observation/reward → RL update.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Multi-view conditioning, rollout branching state 분포, reward model과 실제 transfer 검증.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 ICML abstract는 simulation과 real-world task에서 policy 성능 및 sample efficiency 평가를 명시한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/zhang26ez.html) · [저자 project/code](https://github.com/LAMDA-RL/VLA-MBPO). Exact objective, constraints, success definition은 본문 수동 확인 필요.
