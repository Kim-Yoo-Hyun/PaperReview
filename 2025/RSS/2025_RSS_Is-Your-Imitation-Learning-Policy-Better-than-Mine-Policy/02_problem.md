# Is Your Imitation Learning Policy Better than Mine? Policy Comparison with Near-Optimal Stopping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

적은 robot trial로 두 imitation policy를 신뢰성 있게 비교한다.

## Bottleneck and Changed Formulation

순차 검정으로 비교를 멈출 시점을 결정한다.

## System and Robotics Loop

Policy별 binary success trial → sequential evidence → 중단/선택.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

독립성, indifference region, 오류 확률, 다중 비교 처리.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation 및 실제 policy 비교를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss21/p077.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
