# A State-Distribution Matching Approach to Non-Episodic Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

비에피소드 RL에서 backward policy가 어떤 분포로 reset할지 정한다.

## Bottleneck and Changed Formulation

시연 state 분포를 맞추는 backward policy로 task-relevant reset을 학습한다.

## System and Robotics Loop

Demonstration states → reset policy → forward learner.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

demonstration 접근, forward/backward budget, independent evaluation.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

EARL의 sparse-reward continuous control task를 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v162/sharma22a.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
