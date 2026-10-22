# Learning High-Frequency Continuous Action Chunks in Latent Space

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

고주파 action의 학습·추론과 chunk 경계 연속성을 함께 다룬다.

## Bottleneck and Changed Formulation

VAE latent action chunk와 Reuse-then-Refine 실행을 결합한다.

## System and Robotics Loop

관측 → latent chunk → 고주파 action decoding·경계 보정.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

controller mode, interpolation baseline, VAE 데이터, refinement timing.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

실제 contact manipulation과 여러 policy backbone 비교를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/wang26lj.html) · [저자 project/code](https://github.com/tars-robotics/RTR). Exact objective, constraints, success definition은 본문 수동 확인 필요.
