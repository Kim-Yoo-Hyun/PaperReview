# Learning Human Objectives by Evaluating Hypothetical Behavior

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

적은 human feedback으로 reward를 학습한다.

## Bottleneck and Changed Formulation

가상 행동을 생성하고 평가를 받아 human objective를 추정한다.

## System and Robotics Loop

모델이 만든 hypothetical trajectory → expert feedback → reward model.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

가상 trajectory 실현 가능성, feedback 형태, model bias.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Navigation·driving 성격의 simulated task를 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v119/reddy20a.html) · [저자 project/code](https://github.com/rddy/ReQueST). Exact objective, constraints, success definition은 본문 수동 확인 필요.
