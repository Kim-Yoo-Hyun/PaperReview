# RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

History-dependent manipulation의 memory 설계를 공통 조건에서 비교하기 어렵다.

## Bottleneck and Changed Formulation

Temporal·spatial·object·procedural memory task와 여러 memory-augmented VLA를 비교한다.

## System and Robotics Loop

현재 관측·history representation → π0.5 기반 VLA → manipulation action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

task dictionary와 goal/evaluator, history cutoff, raw ID와 split.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

16 manipulation task와 14 memory variant를 보고하며 memory 효용은 task에 의존한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/dai26c.html) · [저자 project/code](https://robomme.github.io/) · [공식 code](https://github.com/RoboMME/robomme_benchmark). Exact objective, constraints, success definition은 본문 수동 확인 필요.
