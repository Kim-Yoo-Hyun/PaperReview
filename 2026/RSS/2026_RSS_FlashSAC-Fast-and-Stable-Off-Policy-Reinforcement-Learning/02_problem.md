# FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

고차원 로봇 제어에서 off-policy critic 오차가 불안정한 bootstrap을 유발한다.

## Bottleneck and Changed Formulation

가중치·feature·gradient norm을 제한하고 병렬 데이터와 replay coverage를 확대한다.

## System and Robotics Loop

상태 또는 시각 관측 → SAC 행동; replay 기반 가치 학습.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

상태/vision별 계산량, update-to-data 비율, 실제 로봇 전이 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

여러 simulator의 제어 과제와 실제 humanoid sim-to-real을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p099.html) · [저자 project/code](https://github.com/Holiday-Robot/FlashSAC). Exact objective, constraints, success definition은 본문 수동 확인 필요.
