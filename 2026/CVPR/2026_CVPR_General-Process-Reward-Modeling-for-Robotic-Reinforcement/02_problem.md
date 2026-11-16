# General Process Reward Modeling for Robotic Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

진행 보상이 단계·시점을 잘못 판단하면 정책이 보상만 높이는 행동을 배울 수 있다.

## Bottleneck and Changed Formulation

다시점 step-aware 보상 모델과 policy-invariant reward shaping을 제안한다.

## System and Robotics Loop

다시점 관측·과제 진행 → dense reward → robot RL.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

보존 정리의 가정, 종료 처리, multi-view 특권, task별 추가 시연.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation·실제 조작에서 reward 평가와 policy 학습을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.html) · [저자 project/code](https://robo-dopamine.github.io/) · [공식 code](https://github.com/FlagOpen/Robo-Dopamine). Exact objective, constraints, success definition은 본문 수동 확인 필요.
