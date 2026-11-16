# Causal Imitation Learning under Expert-Observable and Expert-Unobservable Confounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Expert만 아는 정보와 양측 모두 모르는 confounder를 imitation에서 구별해야 한다.

## Bottleneck and Changed Formulation

Trajectory history를 instrumental variable로 이용하는 conditional moment 기반 DML-IL을 제안한다.

## System and Robotics Loop

expert trajectory history → instrumental-variable regression → imitation policy.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

instrument relevance/exclusion, 시간적 confounding, history 접근, imitation-gap 가정.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

MuJoCo를 포함한 연속 상태·행동 환경에서 causal IL baseline과 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/4415e8cb0741bc0beb79b316f0856108-Abstract-Conference.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
