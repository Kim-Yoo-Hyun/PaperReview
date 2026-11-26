# RLVR-World: Training World Models with Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

World model의 likelihood 목표가 실제 예측 평가 지표와 일치하지 않을 수 있다.

## Bottleneck and Changed Formulation

Decoded prediction의 검증 가능한 지표를 reward로 삼아 world model을 RL 후학습한다.

## System and Robotics Loop

Action-conditioned state prediction → decoded metric reward → world model update.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

reward metric과 task 목표 정합성, planner의 model exploitation, 로봇 행동 평가 유무.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

텍스트 환경의 상태 예측과 RT-1 영상 예측을 평가한다. 부록 표 12는 PushT 시뮬레이션에서 각 세계 모델을 CEM 계획기에 넣고 과제 성공률을 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b63a24a1832bd14fa945c71f535c0095-Abstract-Conference.html) · [저자 project/code](https://thuml.github.io/RLVR-World/) · [공식 code](https://github.com/thuml/RLVR-World). Exact objective, constraints, success definition은 본문 수동 확인 필요.
