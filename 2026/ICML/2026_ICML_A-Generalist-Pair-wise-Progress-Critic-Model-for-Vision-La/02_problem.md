# A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

실제 로봇에서 행동 생성과 과업 진행 판단을 함께 다루려는 연구다.

## Bottleneck and Changed Formulation

단일 autoregressive 구조로 행동과 두 시점 사이의 진행 차이를 예측하고, 진행 판단을 RL 보상에 사용한다.

## System and Robotics Loop

시각·언어 조건의 행동 출력과 관측 쌍에 대한 progress 출력.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

최종 ICML 모델 크기·동일 weight 여부·reward/done model 및 PPO value의 분리. 2025 preprint 설정을 최종본에 전사하지 않음.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 abstract는 실제 로봇 RL 평가를 보고한다. 정확한 trial·baseline·수치는 최종 본문 확인 필요.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/zhang26if.html) · [저자 project/code](https://github.com/InternRobotics/VLAC). Exact objective, constraints, success definition은 본문 수동 확인 필요.
