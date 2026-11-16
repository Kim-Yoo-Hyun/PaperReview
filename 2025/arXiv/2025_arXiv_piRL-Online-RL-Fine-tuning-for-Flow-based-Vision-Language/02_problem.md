# πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Flow VLA의 action log-likelihood를 직접 계산하기 어려워 RL 후학습이 까다롭다.

## Bottleneck and Changed Formulation

Flow-Noise의 학습 가능한 noise 과정과 Flow-SDE의 ODE–SDE 변환을 대안으로 제시한다.

## System and Robotics Loop

Flow denoising과 environment interaction의 확률적 정책 인터페이스.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Flow-Noise/Flow-SDE 구분, likelihood 집계, normalizer와 update budget.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

여러 benchmark에서 ID/OOD 개선을 보고한다. 접촉 강성 학습 효과를 직접 입증한 것은 아니다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2510.25889) · [저자 project/code](https://github.com/RLinf/RLinf). Exact objective, constraints, success definition은 본문 수동 확인 필요.
