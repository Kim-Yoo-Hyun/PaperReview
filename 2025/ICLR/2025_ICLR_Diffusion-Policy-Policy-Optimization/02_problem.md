# Diffusion Policy Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

BC로 학습한 diffusion action policy를 sparse reward 환경에서 안정적으로 RL fine-tuning하는 문제다.

## Bottleneck and Changed Formulation

Denoising 과정을 policy-gradient 최적화에 포함하고 diffusion policy에 맞춘 학습 설계를 제안한다.

## System and Robotics Loop

Observation-conditioned diffusion policy → 연속 action sequence; denoising step과 환경 실행 step은 구분해야 한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

정확한 likelihood 구성, denoising horizon, 실행 chunk와 sim-to-real reset 조건.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Continuous-control/robotic simulation, pixel/state 입력 및 Furniture-Bench sim-to-real assembly 평가를 project에서 확인했다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c0749c39aaff9e9e4c91f7118bf21b1e-Abstract-Conference.html) · [저자 project/code](https://diffusion-ppo.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
