# AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

실제 generalist policy의 반복 평가를 자동화한다.

## Bottleneck and Changed Formulation

평가 job scheduling·자동 success 검출·scene reset을 결합한다.

## System and Robotics Loop

Submitted policy → scene 실행/성공 판정/reset → 평가 결과.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

target start distribution, 자동 judge 오류, 제외 trial, human 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

WidowX/BridgeData 계열 실제 평가와 수동 판정을 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/zhou25a.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
