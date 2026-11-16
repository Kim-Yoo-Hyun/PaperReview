# Lifelong Autonomous Improvement of Navigation Foundation Models in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

시연으로만 학습한 항법 foundation policy는 배포 경험으로 자율 개선하기 어렵다.

## Bottleneck and Changed Formulation

Offline RL 사전학습과 지속적인 자율 운영·online 적응을 하나의 항법 학습 시스템으로 구성한다.

## System and Robotics Loop

시각 관측·항법 목표 → 정책 행동 → 실제 배포 데이터 → 정책 갱신.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

목표 생성·reset·인간 개입의 범위, 정책 입력의 언어 여부, 이전 장소 회귀.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

실세계 open-world 항법 배포에서 자율 수집 데이터로 적응하는 시스템을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/stachowicz25a.html) · [저자 project/code](https://github.com/kylestach/lifelong-nav-rl). Exact objective, constraints, success definition은 본문 수동 확인 필요.
