# Efficient Evaluation of Multi-Task Robot Policies With Active Experiment Selection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Multi-task robot policy 평가를 적은 실험으로 수행한다.

## Bottleneck and Changed Formulation

비용을 고려한 active experiment selection과 task/policy 정보를 활용한다.

## System and Robotics Loop

Policy·task·prior·관측 결과 → 다음 평가 선택.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

prior 언어 정보, 관측 noise, offline matrix와 실제 online 실행 차이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

실제 및 simulated 평가 자료를 이용한 효율 비교를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/anwar25a.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
