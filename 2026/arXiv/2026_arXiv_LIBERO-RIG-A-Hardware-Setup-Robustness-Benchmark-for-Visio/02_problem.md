# LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Task를 고정한 채 hardware/setup 변화에 대한 VLA 취약성을 측정한다.

## Bottleneck and Changed Formulation

센서·actuation·controller·기하 변화 축을 분리한 benchmark를 제안한다.

## System and Robotics Loop

Native VLA observation/action interface에 setup perturbation을 주입한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

native state 소비, fault axis와 onset, 공개 trial-level logs.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO 기반 여러 VLA와 hardware severity 조건을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.18843) · 저자 프로젝트·코드 주소 미확인. Exact objective, constraints, success definition은 본문 수동 확인 필요.
