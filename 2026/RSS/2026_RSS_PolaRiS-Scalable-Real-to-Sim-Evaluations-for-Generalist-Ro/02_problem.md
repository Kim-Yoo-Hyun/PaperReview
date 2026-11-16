# PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

시뮬레이션의 정책 순위가 실제 로봇 성능을 충분히 반영하지 못한다.

## Bottleneck and Changed Formulation

짧은 실환경 스캔으로 시뮬레이터를 만들고 simulation co-training으로 잔여 차이를 줄인다.

## System and Robotics Loop

실환경 영상 → 재구성 환경 → generalist 정책 평가.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

평가 전에 허용된 co-training 데이터, 독립 실환경 trial, 장면 선택 편향.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

실제·시뮬레이션의 짝지은 rollout으로 정책 순위 상관을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p062.html) · [저자 project/code](https://polaris-evals.github.io/) · [공식 code](https://github.com/arhanjain/PolaRiS). Exact objective, constraints, success definition은 본문 수동 확인 필요.
