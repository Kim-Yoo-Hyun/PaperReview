# Steering Your Diffusion Policy with Latent Space Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

좋은 demonstration policy가 새로운 환경에서 충분한 성능을 내지 못할 때 추가 demonstration 없이 적응시키는 문제다.

## Bottleneck and Changed Formulation

Base diffusion policy의 weight를 고정하고 latent-noise space에서 RL을 수행하는 DSRL을 제안한다.

## System and Robotics Loop

Observation → RL latent-noise policy → frozen BC diffusion policy → robot action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Latent exploration 범위, base policy API, 성공/실패 reward와 reset 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 CoRL abstract는 simulated benchmark, real-world robot task 및 pretrained generalist policy adaptation 평가를 명시한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/wagenmaker25a.html) · [저자 project/code](https://github.com/ajwagen/dsrl). Exact objective, constraints, success definition은 본문 수동 확인 필요.
