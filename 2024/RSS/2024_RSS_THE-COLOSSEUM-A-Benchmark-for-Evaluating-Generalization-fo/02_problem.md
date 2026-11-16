# THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

학습과 유사한 환경만 평가하면 manipulation policy 일반화가 과대평가된다.

## Bottleneck and Changed Formulation

Manipulation task에 시각·물리 perturbation을 체계적으로 적용하는 simulation benchmark를 제시한다.

## System and Robotics Loop

Task·환경 변화 → manipulation policy → 조건별 성공.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

복합 요인 상호작용, simulator와 실세계 조건의 대응.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation 비교와 대응 실세계 perturbation의 관련성을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss20/p133.html) · [저자 project/code](https://robot-colosseum.github.io/) · [공식 code](https://github.com/robot-colosseum/robot-colosseum). Exact objective, constraints, success definition은 본문 수동 확인 필요.
