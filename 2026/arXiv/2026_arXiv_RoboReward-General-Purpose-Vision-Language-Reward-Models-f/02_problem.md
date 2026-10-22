# RoboReward: General-Purpose Vision-Language Reward Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

범용 robot task 성공도를 평가할 VLM reward 모델과 기준을 만든다.

## Bottleneck and Changed Formulation

Robot 자료와 counterfactual negative를 사용해 reward 모델·benchmark를 구성한다.

## System and Robotics Loop

지시·trajectory → task completion reward.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

counterfactual label 검증, temporal clipping, policy shift, benchmark leakage.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공개 robot 자료의 reward 평가와 실제 robot RL을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2601.00675). Exact objective, constraints, success definition은 본문 수동 확인 필요.
